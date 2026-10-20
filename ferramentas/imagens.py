"""Imagens geradas em série, no estilo do tema, a partir de decks/<slug>/imagens.toml: rascunhos baratos, folha de
candidatos, final na resolução pedida e tratamento nas cores do tema, com crédito e trava de custo.

./ap imagens <deck>                               situação de cada imagem e custo do que falta (não gasta nada)
./ap imagens <deck> --rascunhos [nome ...] [-n 3]  rascunhos Gemini 1K em midia/originais/rascunhos/<nome>-<i>.png
                                                   e a folha storyboard/candidatos.png; sem nome, os que não têm
                                                   final (nem midia/<nome>.webp nem original)
./ap imagens <deck> --final nome[=i] [...]         final na resolução do toml, com o rascunho i como ref de
                                                   composição; original em midia/originais/<nome>.png, tratamento em
                                                   midia/<nome>.webp e crédito em midia/creditos.json
./ap imagens <deck> --tratar [nome ...]            refaz só o tratamento a partir dos originais, sem custo
    --teto 2.00   recusa a execução, antes de chamar o gerador, se o custo estimado passar disto (US$)

midia/originais/ fica fora do git: num checkout novo, o WebP com crédito é o final, e só o --tratar precisa do
original de volta. Contrato do imagens.toml em docs/temas.md, seção Imagem.

O prompt enviado é o estilo do tema (temas/<tema>/imagem/estilo.txt), a frase da mestra como Image 1, uma frase por
ref da entrada, o prompt da entrada e, no final com rascunho, a frase do rascunho aprovado. Uma chamada por vez, com
intervalo mínimo de 6 s; no limite de taxa (429) espera o que a ponte disser, ou 30 s, e tenta de novo até 3 vezes.
Com zona_texto, mede a área do título na imagem tratada e avisa se a luz for desigual ou houver bordas ali.
"""
from __future__ import annotations

import argparse
import hashlib
import inspect
import io
import json
import os
import re
import subprocess
import time
import tomllib
from pathlib import Path

import numpy as np
from PIL import Image

from . import config, tratar
from .midia import _deck, creditar

PAPEIS = ("heroica", "objeto", "textura")
CHAVES = {"nome", "slide", "papel", "prompt", "backend", "aspect", "resolucao", "refs", "zona_texto", "tratamento",
          "preco_usd"}
# as opções do ./ap tratar, com os padrões dele
PADRAO_TRATAR = {k: p.default for k, p in inspect.signature(tratar.tratar).parameters.items()
                 if k not in ("deck", "arquivo", "saida")}

# US$ por imagem, lidos na página de preços do Google em 19/10/2026 (plano da Fase 1, seção 7), não reconferidos.
# Backend fora da tabela só gera com preco_usd na entrada do imagens.toml, e a fonte do preço vai para o briefing.
PRECOS = {("gemini", "1K"): 0.0336, ("gemini", "2K"): 0.0504, ("gemini", "4K"): 0.113}
NOTA_CUSTO = "estimado pela tabela de ferramentas/imagens.py, não é valor faturado"
RASCUNHO = ("gemini", "1K")
TETO = 2.0
INTERVALO, ESPERA, TENTATIVAS = 6.0, 30.0, 3
LIMITE_TAXA = re.compile(r"\b429\b|RESOURCE_EXHAUSTED|rate.?limit|too many requests", re.I)
PEDE_ESPERA = re.compile(r"retry.?(?:delay|after)\D{0,12}(\d+(?:\.\d+)?)", re.I)

# cada ref entra no prompt como "Image N is " + frase; o uso de uma ref do imagens.toml completa a mesma frase
FRASE_MESTRA = ("a style reference only: match its light direction, tonal range, grain and lens look; do not copy "
                "its objects or layout.")
FRASE_OBJETO = ("the object reference: keep the exact shape, proportions, color, material and details of the object "
                "it shows; do not copy its background or framing.")
FRASE_RASCUNHO = ("the approved draft of this image: keep its composition, subject, camera angle and framing exactly; "
                  "render it at full fidelity.")

# Zona do título, medida com a imagem reduzida a 640 px de largura (o grão do tratamento some na redução); borda é
# gradiente acima de 6 níveis por pixel. Calibrado em 19/10/2026 nas heroicas tratadas da prévia: a zona livre mede
# desvio 0,050 (heroi-aula1, 0 a 42% da largura) e 0,019 (heroi-aula2, 0 a 50%), com 0,04% e 0,02% de bordas; os
# rascunhos recusados dão 0,63% de bordas (veio de madeira, heroi-aula2-v5), 0,64% (quina de mesa, heroi-aula2-7) e
# desvio 0,10 (horizonte claro atrás do título, heroi-aula1-1).
LIMITE_DESVIO, LIMITE_BORDAS, GRADIENTE = 0.08, 0.003, 6.0


# ---------- imagens.toml e a série do tema ----------

def serie_do_tema(pasta: Path) -> dict:
    """O que o tema define para as imagens: estilo (sem as linhas de comentário #), mestra, geradores permitidos e
    tratamento por papel. Sem temas/<tema>/imagem/, só vale o Gemini e o tratamento padrão do ./ap tratar."""
    img = tratar.tema_css(pasta).parent / "imagem"
    estilo = img / "estilo.txt"
    texto = "\n".join(l for l in estilo.read_text(encoding="utf-8").splitlines()
                      if not l.lstrip().startswith("#")).strip() if estilo.is_file() else ""
    # só os nomes exatos: o image-video-api grava mestra.cache.jpg ao lado de uma ref grande, e o cache velho não vale
    mestra = next((m for n in ("mestra.png", "mestra.jpg", "mestra.jpeg") if (m := img / "refs" / n).is_file()), None)
    arq = img / "padroes.toml"
    padroes = tomllib.loads(arq.read_text(encoding="utf-8")) if arq.is_file() else {}
    return {"pasta": img, "estilo": texto, "mestra": mestra, "geradores": padroes.get("geradores", ["gemini"]),
            "tratamento": padroes.get("tratamento", {})}


def _entrada(e: dict, pasta: Path, serie: dict) -> dict:
    nome = e.get("nome", "?")
    erro = lambda msg: SystemExit(f"imagens.toml, {nome}: {msg}")  # noqa: E731
    if falta := {"nome", "slide", "papel", "prompt"} - set(e):
        raise erro(f"falta {', '.join(sorted(falta))}")
    if sobra := set(e) - CHAVES:
        raise erro(f"chave desconhecida {', '.join(sorted(sobra))} (valem {', '.join(sorted(CHAVES))})")
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", nome):
        raise erro("o nome vira arquivo: só minúsculas, dígitos e hífen")
    if e["papel"] not in PAPEIS:
        raise erro(f"papel {e['papel']!r} (vale {', '.join(PAPEIS)})")
    e = {"backend": "gemini", "aspect": "16:9", "resolucao": "2K", "refs": [], **e}
    if e["backend"] not in serie["geradores"]:
        raise erro(f"o tema não permite {e['backend']} (permite {', '.join(serie['geradores'])}; ver padroes.toml)")
    if e["resolucao"] not in ("1K", "2K", "4K") or not re.fullmatch(r"\d+:\d+", e["aspect"]):
        raise erro("resolucao vale 1K, 2K ou 4K, e aspect é largura:altura, como 16:9")
    if serie["estilo"] and serie["estilo"][:40] in e["prompt"]:
        raise erro("o prompt repete o estilo do tema, que já entra sozinho; deixe só o objeto e a cena")
    refs = []
    for r in e["refs"]:
        arq, uso = (r, FRASE_OBJETO) if isinstance(r, str) else (r.get("arquivo"), r.get("uso"))
        if not arq or not uso or Path(arq).suffix.lower() not in (".png", ".jpg", ".jpeg"):
            raise erro(f"ref {r!r}: caminho PNG ou JPG a partir do deck, ou {{arquivo = ..., uso = ...}} "
                       "(o image-video-api recusa WebP)")
        if Path(arq).is_absolute() or not (pasta / arq).resolve().is_relative_to(pasta.resolve()):
            raise erro(f"ref {arq!r}: fica fora da pasta do deck; a referência vai para o gerador externo")
        refs.append((pasta / arq, uso))
    zona = e.get("zona_texto")
    if zona is not None and not (len(zona) == 4 and 0 <= zona[0] < zona[2] <= 1 and 0 <= zona[1] < zona[3] <= 1):
        raise erro("zona_texto é [x0, y0, x1, y1] em frações de 0 a 1")
    trat = {**serie["tratamento"].get(e["papel"], {}), **e.get("tratamento", {})}
    if sobra := set(trat) - set(PADRAO_TRATAR):
        raise erro(f"tratamento com {', '.join(sorted(sobra))} (valem {', '.join(PADRAO_TRATAR)})")
    # os mesmos valores que o ./ap tratar aceita: um erro de digitação viraria outro tratamento sem aviso
    for chave, valem in (("tom", ("duotone", "tritone")), ("niveis", ("auto", "claro", "fundo"))):
        if chave in trat and trat[chave] not in valem:
            raise erro(f"tratamento {chave} = {trat[chave]!r} (vale {', '.join(valem)})")
    return {**e, "refs": refs, "tratamento": trat}


def carregar(deck: str) -> tuple[Path, dict, list[dict]]:
    pasta = _deck(deck)
    arq = pasta / "imagens.toml"
    if not arq.is_file():
        raise SystemExit(f"{arq} não existe (formato em docs/temas.md, seção Imagem)")
    serie = serie_do_tema(pasta)
    itens = [_entrada(e, pasta, serie) for e in tomllib.loads(arq.read_text(encoding="utf-8")).get("imagem", [])]
    nomes = [e["nome"] for e in itens]
    if dup := {n for n in nomes if nomes.count(n) > 1}:
        raise SystemExit(f"imagens.toml: nome repetido {', '.join(sorted(dup))}")
    return pasta, serie, itens


def _escolher(itens: list[dict], nomes) -> list[dict]:
    por_nome = {e["nome"]: e for e in itens}
    if falta := [n for n in nomes if n not in por_nome]:
        raise SystemExit(f"imagens.toml não tem {', '.join(falta)} (tem {', '.join(por_nome)})")
    return [por_nome[n] for n in nomes]


def _creditos(pasta: Path) -> dict[str, dict]:
    arq = pasta / "midia" / "creditos.json"
    return {i["arquivo"]: i for i in json.loads(arq.read_text())} if arq.exists() else {}


def original(pasta: Path, e: dict) -> Path:
    """O original de onde sai midia/<nome>.webp: o que o crédito do WebP aponta, ou midia/originais/<nome>.png."""
    cred = _creditos(pasta).get(f"midia/{e['nome']}.webp", {})
    return pasta / cred["original"] if cred.get("original") else pasta / "midia" / "originais" / f"{e['nome']}.png"


def marcador(pasta: Path, e: dict) -> bool:
    """midia/<nome>.webp é marcador copiado do molde (o crédito diz "marcador: ..."; ./ap novo traz os do catálogo):
    ocupa o lugar no deck, mas não vale como final."""
    return str(_creditos(pasta).get(f"midia/{e['nome']}.webp", {}).get("nota", "")).startswith("marcador")


def tem_final(pasta: Path, e: dict) -> bool:
    """O WebP tratado (no git) ou o original (fora dele) já existe. Num checkout novo só o WebP vem, e ele basta."""
    if marcador(pasta, e):
        return False
    return (pasta / "midia" / f"{e['nome']}.webp").is_file() or original(pasta, e).is_file()


def rascunhos_de(pasta: Path, nome: str) -> list[Path]:
    achados = []
    for p in (pasta / "midia" / "originais" / "rascunhos").glob(f"{nome}-*.png"):
        if m := re.fullmatch(rf"{re.escape(nome)}-(\d+)\.png", p.name):
            achados.append((int(m.group(1)), p))
    return [p for _, p in sorted(achados)]


def compor(e: dict, serie: dict, rascunho: Path | None = None) -> tuple[str, list[Path]]:
    """Prompt enviado e refs na ordem em que o prompt as numera."""
    refs, frases = [], []
    for arq, uso in ([(serie["mestra"], FRASE_MESTRA)] if serie["mestra"] else []) + e["refs"] + (
            [(rascunho, FRASE_RASCUNHO)] if rascunho else []):
        if not arq.is_file():
            raise SystemExit(f"{e['nome']}: a ref {arq} não existe" + (
                " (midia/originais/ fica fora do git: traga-a da cópia de segurança)" if "originais" in arq.parts
                else ""))
        refs.append(arq)
        frases.append(f"Image {len(refs)} is {uso}")
    fim = [frases.pop()] if rascunho else []
    corpo = "\n".join([" ".join(frases + [e["prompt"].strip()]), *fim])
    return (f"{serie['estilo']}\n\n{corpo}" if serie["estilo"] else corpo), refs


# ---------- custo e gerador ----------

def preco(e: dict, backend: str, resolucao: str) -> float | None:
    return PRECOS.get((backend, resolucao)) if (backend, resolucao) == RASCUNHO else (
        e.get("preco_usd") or PRECOS.get((backend, resolucao)))


def cobrar(chamadas: list[tuple[dict, str, str]], teto: float) -> list[float]:
    """Preço de cada chamada; mostra o total e recusa tudo, antes de gastar, se passar do teto."""
    precos = [preco(e, b, r) for e, b, r in chamadas]
    if sem := sorted({f"{e['nome']} ({b} {r})" for (e, b, r), p in zip(chamadas, precos) if p is None}):
        raise SystemExit(f"sem preço conhecido: {', '.join(sem)}. Leia o preço na página do provedor, anote a fonte "
                         "no briefing e ponha preco_usd na entrada do imagens.toml")
    total = sum(precos)
    print(f"custo estimado: US$ {total:.2f} em {len(precos)} chamada(s) (teto US$ {teto:.2f})")
    if total > teto + 1e-9:
        raise SystemExit("acima do teto: gere menos, ou mostre o custo ao usuário e, com o sim dele, rode com --teto")
    return precos


def ponte(prompt: str, saida: Path, *, backend: str, aspect: str, resolucao: str, refs: list[Path]) -> tuple[int, str]:
    """Uma chamada ao ./cvm imagem do claude_video_maker, que chama o image-video-api; devolve o código de saída e o
    que a ponte escreveu. Os testes trocam esta função por um gerador simulado."""
    env = {k: v for k, v in os.environ.items() if k not in ("UV_PROJECT_ENVIRONMENT", "VIRTUAL_ENV")}  # ver midia.cvm
    args = ["imagem", prompt, "--saida", str(saida), "--aspect", aspect, "--resolucao", resolucao, "--backend", backend]
    for r in refs:
        args += ["--ref", str(r.resolve())]
    r = subprocess.run(["bash", str(config.video_maker() / "cvm"), *args], env=env, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


_ultima = [-INTERVALO]  # instante (time.monotonic) da última chamada ao gerador


def gerar(prompt: str, saida: Path, **params) -> None:
    """Uma chamada por vez, a pelo menos INTERVALO s da anterior; no limite de taxa, espera e tenta de novo."""
    saida.parent.mkdir(parents=True, exist_ok=True)
    saida.unlink(missing_ok=True)  # sobra de execução interrompida não pode passar por imagem nova
    for tentativa in range(TENTATIVAS + 1):
        time.sleep(max(0.0, INTERVALO - (time.monotonic() - _ultima[0])))
        _ultima[0] = time.monotonic()
        codigo, texto = ponte(prompt, saida, **params)
        if codigo == 0 and saida.is_file():
            return
        if not LIMITE_TAXA.search(texto) or tentativa == TENTATIVAS:
            print(texto.strip()[-2000:])
            raise SystemExit(f"a geração de {saida.name} falhou (mensagem acima)")
        m = PEDE_ESPERA.search(texto)
        espera = float(m.group(1)) if m else ESPERA * (tentativa + 1)
        print(f"limite de taxa do gerador; nova tentativa em {espera:.0f} s ({tentativa + 1} de {TENTATIVAS})")
        time.sleep(espera)


def _rel(pasta: Path, p: Path) -> str:
    """Caminho a partir da raiz do repositório (decks/<slug> fica dois níveis abaixo), como no creditos.json."""
    try:
        return p.resolve().relative_to(pasta.parent.parent).as_posix()
    except ValueError:
        return str(p.resolve())


def _creditar(pasta: Path, arq: Path, e: dict, serie: dict, prompt: str, refs: list[Path], backend: str,
              resolucao: str, custo: float) -> None:
    creditar(pasta, arq, ferramenta="image-video-api (./ap imagens)", modelo=backend, prompt=prompt,
             parametros={"aspecto": e["aspect"], "resolucao": resolucao}, refs=[_rel(pasta, r) for r in refs],
             estilo_sha256=hashlib.sha256(serie["estilo"].encode()).hexdigest() if serie["estilo"] else None,
             custo_usd=custo, custo_nota=NOTA_CUSTO, licenca="termos do provedor do modelo")


def _exigir_serie(serie: dict) -> None:
    if not serie["estilo"]:
        raise SystemExit(f"{serie['pasta'] / 'estilo.txt'} não existe ou está vazio: escreva a bíblia da série "
                         "(modelo em temas/_modelo/imagem/)")
    if not serie["mestra"]:
        print(f"AVISO sem {serie['pasta'] / 'refs'}/mestra.png ou .jpg: as imagens saem sem a ref de estilo")


# ---------- zona do título ----------

def medir_zona(arq: Path, zona, fundo=(0, 0, 0)) -> tuple[float, float]:
    """Desvio-padrão da luminância (0 a 1) e fração de pixels de borda na zona [x0, y0, x1, y1]. Imagem com alfa é
    medida sobre a cor de fundo."""
    im = Image.open(arq)
    if "A" in im.getbands():
        im = Image.alpha_composite(Image.new("RGBA", im.size, (*fundo, 255)), im.convert("RGBA"))
    im = im.convert("RGB").resize((640, max(2, round(im.height * 640 / im.width))), Image.BOX)
    lum = np.asarray(im, dtype=float) @ tratar.LUMA
    h, w = lum.shape
    x0, y0 = round(zona[0] * w), round(zona[1] * h)
    z = lum[y0:max(y0 + 2, round(zona[3] * h)), x0:max(x0 + 2, round(zona[2] * w))]
    gy, gx = np.gradient(z)
    return float(z.std() / 255), float((np.hypot(gx, gy) > GRADIENTE).mean())


def conferir_zona(pasta: Path, e: dict, arq: Path) -> list[str]:
    desvio, bordas = medir_zona(arq, e["zona_texto"], tratar.cores_do_tema(pasta)["fundo"])
    achados = []
    if desvio > LIMITE_DESVIO:
        achados.append(f"luz desigual (desvio {desvio:.3f}, limite {LIMITE_DESVIO})")
    if bordas > LIMITE_BORDAS:
        achados.append(f"{bordas:.2%} de bordas (limite {LIMITE_BORDAS:.1%})")
    return achados


def _tratar(pasta: Path, e: dict, orig: Path) -> Path:
    out = tratar.tratar(str(pasta), str(orig), saida=e["nome"], **e["tratamento"])
    if e.get("zona_texto") and (achados := conferir_zona(pasta, e, out)):
        print(f"AVISO {e['nome']}: zona de texto {e['zona_texto']} com {' e '.join(achados)}; o título vai brigar "
              "com a foto. Escolha outro rascunho ou peça a zona vazia no prompt")
    return out


# ---------- comandos ----------

def _quadro(arq: Path) -> bytes:
    """O rascunho num quadro 16:9 de fundo escuro, para a folha não deformar retrato nem quadrado."""
    im = Image.open(arq).convert("RGB")
    w, h = max(im.width, round(im.height * 16 / 9)), max(im.height, round(im.width * 9 / 16))
    q = Image.new("RGB", (w, h), (24, 26, 31))
    q.paste(im, ((w - im.width) // 2, (h - im.height) // 2))
    q.thumbnail((960, 540))
    buf = io.BytesIO()
    q.save(buf, "PNG")
    return buf.getvalue()


def candidatos(pasta: Path, itens: list[dict]) -> Path | None:
    """Folha storyboard/candidatos.png com todos os rascunhos das imagens dadas, rotulados <nome>-<i>."""
    from .palco import folha

    grupos = [ps for e in itens if (ps := rascunhos_de(pasta, e["nome"]))]
    if not grupos:
        return None
    colunas = min(4, max(len(ps) for ps in grupos))
    fotos = []
    for ps in grupos:  # cada imagem começa numa linha; célula vazia (png None) completa a anterior
        fotos += [({"rotulo": p.stem}, _quadro(p)) for p in ps] + [({}, None)] * (-len(ps) % colunas)
    saida = pasta / "storyboard" / "candidatos.png"
    saida.parent.mkdir(parents=True, exist_ok=True)
    folha(fotos, saida, colunas=colunas)
    print(f"{sum(map(len, grupos))} rascunho(s) na folha {saida}")
    return saida


def rascunhos(deck: str, nomes=(), *, n: int = 3, teto: float = TETO) -> Path | None:
    pasta, serie, itens = carregar(deck)
    alvo = _escolher(itens, nomes) if nomes else [e for e in itens if not tem_final(pasta, e)]
    if not alvo:
        print("todas as imagens já têm final (midia/<nome>.webp ou o original); para rascunhar de novo, diga os nomes")
        return None
    if n > 0:
        _exigir_serie(serie)
        if RASCUNHO[0] not in serie["geradores"]:
            raise SystemExit(f"o rascunho é {RASCUNHO[0]} {RASCUNHO[1]}, e o tema não permite {RASCUNHO[0]}")
        precos = cobrar([(e, *RASCUNHO) for e in alvo for _ in range(n)], teto)
        pasta_r = pasta / "midia" / "originais" / "rascunhos"
        for e in alvo:
            prompt, refs = compor(e, serie)
            for _ in range(n):
                antes = rascunhos_de(pasta, e["nome"])
                i = int(antes[-1].stem.rsplit("-", 1)[1]) + 1 if antes else 1
                arq = pasta_r / f"{e['nome']}-{i}.png"
                print(f"rascunho {arq.stem} ({RASCUNHO[0]} {RASCUNHO[1]})")
                gerar(prompt, arq, backend=RASCUNHO[0], aspect=e["aspect"], resolucao=RASCUNHO[1], refs=refs)
                _creditar(pasta, arq, e, serie, prompt, refs, *RASCUNHO, precos.pop(0))
    return candidatos(pasta, alvo)


def _arquivar(pasta: Path, orig: Path, nome: str) -> None:
    """Move o original anterior para rascunhos/<nome>-antes-<k>.png, levando o crédito junto."""
    pasta_r = pasta / "midia" / "originais" / "rascunhos"
    pasta_r.mkdir(parents=True, exist_ok=True)
    k = 1
    while (pasta_r / f"{nome}-antes-{k}.png").exists():
        k += 1
    novo = pasta_r / f"{nome}-antes-{k}.png"
    orig.rename(novo)
    arq = pasta / "midia" / "creditos.json"
    if arq.exists():
        de, para = orig.relative_to(pasta).as_posix(), novo.relative_to(pasta).as_posix()
        itens = [{**i, "arquivo": para} if i["arquivo"] == de else i for i in json.loads(arq.read_text())]
        arq.write_text(json.dumps(sorted(itens, key=lambda i: i["arquivo"]), ensure_ascii=False, indent=1))
    print(f"o original anterior foi para {novo.relative_to(pasta)}")


def final(deck: str, pedidos, *, teto: float = TETO) -> list[Path]:
    pasta, serie, itens = carregar(deck)
    escolhas = []
    for p in pedidos:
        nome, _, i = p.partition("=")
        e = _escolher(itens, [nome])[0]
        rasc = pasta / "midia" / "originais" / "rascunhos" / f"{nome}-{i}.png" if i else None
        if rasc and not rasc.is_file():
            raise SystemExit(f"{rasc} não existe (rascunhos de {nome}: "
                             f"{', '.join(r.stem for r in rascunhos_de(pasta, nome)) or 'nenhum'})")
        escolhas.append((e, rasc))
    _exigir_serie(serie)
    precos = cobrar([(e, e["backend"], e["resolucao"]) for e, _ in escolhas], teto)
    feitos = []
    for (e, rasc), custo in zip(escolhas, precos):
        prompt, refs = compor(e, serie, rasc)
        orig = pasta / "midia" / "originais" / f"{e['nome']}.png"
        novo = orig.with_name(f"{e['nome']}.novo.png")  # o original anterior só sai depois que o novo existir
        print(f"final {e['nome']} ({e['backend']} {e['resolucao']}" + (f", rascunho {rasc.stem})" if rasc else ")"))
        gerar(prompt, novo, backend=e["backend"], aspect=e["aspect"], resolucao=e["resolucao"], refs=refs)
        if orig.exists():
            _arquivar(pasta, orig, e["nome"])
        novo.rename(orig)
        _creditar(pasta, orig, e, serie, prompt, refs, e["backend"], e["resolucao"], custo)
        feitos.append(_tratar(pasta, e, orig))
    return feitos


def retratar(deck: str, nomes=()) -> list[Path]:
    pasta, _, itens = carregar(deck)
    feitos = []
    for e in _escolher(itens, nomes) if nomes else itens:
        orig = original(pasta, e)
        if marcador(pasta, e):
            print(f"{e['nome']}: midia/{e['nome']}.webp é marcador do molde; gere com --rascunhos e --final")
        elif orig.is_file():
            feitos.append(_tratar(pasta, e, orig))
        elif (pasta / "midia" / f"{e['nome']}.webp").is_file():
            print(f"{e['nome']}: o original {orig.relative_to(pasta)} não está nesta cópia (midia/originais/ fica fora "
                  "do git); o WebP atual continua valendo, e refazer o tratamento pede o original da cópia de segurança")
        else:
            print(f"{e['nome']}: sem WebP nem original; gere com --rascunhos e --final")
    return feitos


def _tratada(pasta: Path, e: dict, orig: Path) -> str:
    webp = pasta / "midia" / f"{e['nome']}.webp"
    if not webp.is_file():
        return "não"
    feito = _creditos(pasta).get(f"midia/{e['nome']}.webp", {}).get("tratamento") or {}
    pedido = {**PADRAO_TRATAR, **e["tratamento"]}
    if orig.is_file():
        with Image.open(orig) as im:
            pedido["largura"] = min(pedido["largura"], im.width)
    return "sim" if all(feito.get(k) == v for k, v in pedido.items()) else "refazer"


def situacao(deck: str) -> int:
    pasta, serie, itens = carregar(deck)
    linhas, falta, prontas, fora = [], 0.0, 0, 0
    for e in itens:
        orig = original(pasta, e)
        tratada = "marcador" if marcador(pasta, e) else _tratada(pasta, e, orig)
        zona = "-"
        if e.get("zona_texto") and tratada in ("sim", "refazer"):
            zona = "AVISO" if conferir_zona(pasta, e, pasta / "midia" / f"{e['nome']}.webp") else "ok"
        custo = 0.0 if tem_final(pasta, e) else preco(e, e["backend"], e["resolucao"])
        falta += custo or 0.0
        prontas += tratada == "sim" and zona != "AVISO"
        # sem o original, o WebP que está no git é o final; o original só falta para refazer o tratamento
        fora += not orig.is_file() and tratada in ("sim", "refazer")
        coluna = orig.name if orig.is_file() else "fora do git" if tratada in ("sim", "refazer") else "-"
        linhas.append((e["nome"], e["slide"], e["papel"], f"{e['backend']} {e['resolucao']}",
                       str(len(rascunhos_de(pasta, e["nome"]))), coluna, tratada, zona,
                       "?" if custo is None else f"{custo:.2f}"))
    cab = ("nome", "slide", "papel", "gerador", "rascunhos", "original", "tratada", "zona", "falta US$")
    larg = [max(len(str(c)) for c in col) for col in zip(cab, *linhas)]
    for linha in (cab, *linhas):
        print("  ".join(str(c).ljust(w) for c, w in zip(linha, larg)).rstrip())
    print(f"{prontas} de {len(itens)} prontas; falta gastar US$ {falta:.2f} nos finais"
          + (" e o que tem preço ?, que precisa de preco_usd" if any(l[-1] == "?" for l in linhas) else "")
          + f" (rascunho {RASCUNHO[0]} {RASCUNHO[1]}: US$ {PRECOS[RASCUNHO]} cada)")
    if fora:
        print(f"{fora} original(is) fora do git, que não vêm num checkout novo: os WebP valem como estão, mas --tratar "
              "e as refs em midia/originais/ pedem os originais de volta da cópia de segurança")
    if not serie["estilo"]:
        print(f"AVISO o tema não tem estilo.txt em {serie['pasta']}: a série sai sem bíblia de estilo")
    elif not serie["mestra"]:
        print(f"AVISO o tema não tem refs/mestra.png ou .jpg em {serie['pasta']}: gere a mestra antes dos finais "
              "(docs/temas.md, seção Imagem)")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("deck")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--rascunhos", nargs="*", metavar="NOME", help="rascunhos Gemini 1K e a folha de candidatos")
    g.add_argument("--final", nargs="+", metavar="NOME[=I]", help="final na resolução do toml, com o rascunho I")
    g.add_argument("--tratar", nargs="*", metavar="NOME", help="refaz o tratamento a partir dos originais")
    ap.add_argument("-n", type=int, default=3, help="rascunhos por imagem (0 só refaz a folha)")
    ap.add_argument("--teto", type=float, default=TETO, help="US$ por execução (padrão 2.00)")
    a = ap.parse_args(argv)
    if a.rascunhos is not None:
        rascunhos(a.deck, a.rascunhos, n=a.n, teto=a.teto)
    elif a.final:
        final(a.deck, a.final, teto=a.teto)
    elif a.tratar is not None:
        retratar(a.deck, a.tratar)
    else:
        return situacao(a.deck)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
