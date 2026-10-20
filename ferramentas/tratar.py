"""Tratamento de imagem nas cores do tema do deck, para que fotos geradas por IA pareçam uma série da mesma marca.

./ap tratar <deck> <arquivo> [--tom duotone|tritone] [--intensidade 0.8] [--largura 2048] [--alfa] [--grao 0.02]
            [--niveis auto|claro|fundo] [--gama 1] [--semente N] [--saida nome]

Lê --cor-tinta, --cor-destaque e --cor-fundo do tema.css ligado no deck.html, calcula a luminância
(0,2126R + 0,7152G + 0,0722B), estica os níveis, aplica a gama e mapeia cada pixel entre as cores do tema
(duotone: tinta para fundo; tritone: tinta, destaque, fundo). Níveis: auto usa os percentis 0,5 e 99,5; claro não
estica o escuro (papel sobre o off-white); fundo põe o topo na luminância do fundo da foto, que vira --cor-fundo e
não deixa halo no recorte. Mistura com o original pela intensidade, soma um grão com semente e, com --alfa, torna
transparente o que estiver perto da cor do fundo da foto e ligado à borda, com borda suave de uns 2 px. O fundo é
uma superfície ajustada à faixa da borda (acompanha o degradê da luz) e os limiares saem do ruído dessa faixa; o
miolo do objeto fica opaco mesmo se tiver a cor do fundo. Grava midia/<nome>.webp (qualidade 85), guarda o original
em midia/originais/ e registra o tratamento em midia/creditos.json, herdando o crédito do original quando houver.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageOps

from .midia import _deck, creditar, guardar_original

LUMA = np.array([0.2126, 0.7152, 0.0722])
FOLGA = 2.0  # o recorte começa a esta distância RGB acima do ruído do fundo e fica opaco no dobro


def _hex(v: str) -> tuple[int, int, int]:
    v = v.lstrip("#")
    if len(v) in (3, 4):
        v = "".join(c * 2 for c in v)
    return tuple(int(v[i:i + 2], 16) for i in (0, 2, 4))


def tema_css(pasta: Path) -> Path:
    """O tema.css ligado no deck.html; a pasta dele é a do tema (temas/<nome>/)."""
    doc = (pasta / "deck.html").read_text(encoding="utf-8")
    m = re.search(r"<link[^>]+href=\"([^\"]*tema\.css)\"", doc)
    if not m:
        raise SystemExit(f"{pasta / 'deck.html'} não liga nenhum tema.css")
    return (pasta / m.group(1)).resolve()


def cores_do_tema(pasta: Path) -> dict[str, tuple[int, int, int]]:
    arq = tema_css(pasta)
    css = arq.read_text(encoding="utf-8")
    cores = {}
    for nome in ("tinta", "destaque", "fundo"):
        c = re.search(rf"--cor-{nome}\s*:\s*(#[0-9a-fA-F]{{3,8}})\b", css)
        if not c:
            raise SystemExit(f"{arq} não define --cor-{nome} em hex")
        cores[nome] = _hex(c.group(1))
    return cores


def _fundo_da_borda(rgb: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Cor do fundo da foto em cada pixel: superfície de 2º grau ajustada à faixa da borda, que acompanha o degradê da
    luz de janela (num fundo liso, dá a própria cor). Devolve a superfície e a máscara da faixa."""
    h, w, _ = rgb.shape
    k = max(2, min(h, w) // 20)
    borda = np.zeros((h, w), bool)
    borda[:k] = borda[-k:] = True
    borda[:, :k] = borda[:, -k:] = True
    y, x = np.mgrid[0:h, 0:w] / np.array([h, w], float)[:, None, None]
    termos = np.stack([np.ones_like(x), x, y, x * x, y * y, x * y], axis=-1)
    coef, *_ = np.linalg.lstsq(termos[borda], rgb[borda], rcond=None)
    return termos @ coef, borda


def mapear(rgb: np.ndarray, cores: dict, *, tom="duotone", intensidade=0.8, grao=0.02, semente=0, lo=None, hi=None,
           gama=1.0) -> np.ndarray:
    """rgb em float 0..255 (h, w, 3); devolve o mesmo formato, já tratado. lo e hi fixam os níveis (luminância 0..1);
    sem eles, valem os percentis 0,5 e 99,5. Gama acima de 1 escurece os meios-tons."""
    lum = (rgb @ LUMA) / 255
    p_lo, p_hi = np.percentile(lum, [0.5, 99.5])
    lo = p_lo if lo is None else lo
    hi = p_hi if hi is None else hi
    if hi - lo > 1e-3:
        lum = np.clip((lum - lo) / (hi - lo), 0, 1)
    lum = lum ** gama
    paradas = ["tinta", "fundo"] if tom == "duotone" else ["tinta", "destaque", "fundo"]
    xs = np.linspace(0, 1, len(paradas))
    tinto = np.stack([np.interp(lum, xs, [cores[p][c] for p in paradas]) for c in range(3)], axis=-1)
    out = intensidade * tinto + (1 - intensidade) * rgb
    if grao:
        out += np.random.default_rng(semente).normal(0, grao * 255, lum.shape)[..., None]
    return np.clip(out, 0, 255)


def tratar(deck: str, arquivo: str, *, tom="duotone", intensidade=0.8, largura=2048, alfa=False, grao=0.02,
           semente=0, saida=None, niveis="auto", gama=1.0) -> Path:
    pasta = _deck(deck)
    src = Path(arquivo).resolve()
    if not src.is_file():
        raise SystemExit(f"{src} não existe")
    destino = pasta / "midia" / f"{saida or src.stem}.webp"
    orig = guardar_original(pasta, src, destino)
    cores = cores_do_tema(pasta)

    im = ImageOps.exif_transpose(Image.open(orig))
    if im.width > largura:
        im = im.resize((largura, round(im.height * largura / im.width)), Image.LANCZOS)
    elif im.width < largura:
        print(f"AVISO {src.name}: {im.width} px de largura, menos que os {largura} pedidos (não amplia)")
    a0 = np.asarray(im.getchannel("A"), dtype=float) / 255 if "A" in im.getbands() else None
    rgb = np.asarray(im.convert("RGB"), dtype=float)

    fundo, borda = _fundo_da_borda(rgb) if alfa or niveis == "fundo" else (None, None)
    lo = 0.0 if niveis == "claro" else None
    hi = float(np.median(fundo @ LUMA)) / 255 if niveis == "fundo" else None
    out = Image.fromarray(mapear(rgb, cores, tom=tom, intensidade=intensidade, grao=grao, semente=semente, lo=lo,
                                 hi=hi, gama=gama).round().astype(np.uint8))
    limiar = None
    if alfa or a0 is not None:
        a = np.ones(rgb.shape[:2]) if a0 is None else a0
        if alfa:
            # a mediana tira o ruído do fundo sem engordar o contorno do objeto, como um desfoque faria
            liso = np.asarray(im.convert("RGB").filter(ImageFilter.MedianFilter(5)), dtype=float)
            dist = np.linalg.norm(liso - fundo, axis=-1)
            de = float(np.percentile(dist[borda], 99)) + FOLGA
            limiar = [round(de, 1), round(2 * de, 1)]
            rampa = np.clip((dist - de) / de, 0, 1)
            # só some o fundo ligado à borda: o miolo claro do objeto (papel branco) fica opaco
            marca = ImageOps.expand(Image.fromarray(np.where(rampa < 1, 0, 255).astype(np.uint8)), 1, fill=0)
            ImageDraw.floodfill(marca, (0, 0), 128)
            rampa[np.asarray(marca)[1:-1, 1:-1] != 128] = 1
            corte = Image.fromarray((rampa * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1))
            a = a * np.asarray(corte, dtype=float) / 255
        out.putalpha(Image.fromarray((a * 255).round().astype(np.uint8)))
    destino.parent.mkdir(parents=True, exist_ok=True)
    # method 6 no alfa sem perda leva 25x mais tempo para ganhar menos de 10% de tamanho
    out.save(destino, "WEBP", quality=85, method=4 if out.mode == "RGBA" else 6)

    # o crédito do arquivo tratado herda o do original (prompt, modelo, licença) e acrescenta o tratamento
    arq = pasta / "midia" / "creditos.json"
    itens = {i["arquivo"]: i for i in (json.loads(arq.read_text()) if arq.exists() else [])}

    def rel(p: Path) -> str | None:
        return p.relative_to(pasta).as_posix() if p.is_relative_to(pasta) else None

    base = itens.get(rel(src)) or itens.get(rel(orig)) or itens.get(rel(destino))
    if not base:
        print(f"AVISO {src.name}: sem crédito de origem; anote de onde veio e a licença em midia/creditos.json")
        base = {"ferramenta": "trazido", "origem": f"[CONFERIR] {src.name}, sem crédito registrado"}
    base = {k: v for k, v in base.items() if k not in ("arquivo", "data", "original", "tratamento")}
    creditar(pasta, destino, **base, original=rel(orig), tratamento={
        "ferramenta": "./ap tratar", "tom": tom, "intensidade": intensidade, "largura": out.width, "alfa": alfa,
        "grao": grao, "semente": semente, "niveis": niveis, "gama": gama, "limiar": limiar,
        "cores": {k: "#%02X%02X%02X" % v for k, v in cores.items()}})
    print(destino)
    return destino


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("deck")
    ap.add_argument("arquivo")
    ap.add_argument("--tom", default="duotone", choices=["duotone", "tritone"])
    ap.add_argument("--intensidade", type=float, default=0.8, help="0 mantém o original, 1 só as cores do tema")
    ap.add_argument("--largura", type=int, default=2048, help="reduz até esta largura (não amplia)")
    ap.add_argument("--alfa", action="store_true", help="transparente onde a foto tem a cor do fundo, ligada à borda")
    ap.add_argument("--grao", type=float, default=0.02, help="desvio do grão, em fração de 255 (0 desliga)")
    ap.add_argument("--niveis", default="auto", choices=["auto", "claro", "fundo"],
                    help="auto: percentis 0,5 e 99,5; claro: não estica o escuro; fundo: o fundo da foto vira --cor-fundo")
    ap.add_argument("--gama", type=float, default=1.0, help="acima de 1 escurece os meios-tons")
    ap.add_argument("--semente", type=int, default=0)
    ap.add_argument("--saida", help="nome do arquivo em midia/, sem extensão (padrão: o do original)")
    a = ap.parse_args(argv)
    tratar(a.deck, a.arquivo, tom=a.tom, intensidade=a.intensidade, largura=a.largura, alfa=a.alfa, grao=a.grao,
           semente=a.semente, saida=a.saida, niveis=a.niveis, gama=a.gama)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
