"""Motor de palco: apresentações ao vivo feitas por código (motor/palco.js). Contrato em docs/palco.md.

./ap novo <slug> [--tema cojuris] [--modo continuo|slides]  # decks/<slug>/ com o tema escolhido, a partir do
                                            # catálogo do plano contínuo (padrão) ou da demonstração (slides)
./ap abrir <deck>                           # serve e abre no navegador, para ensaiar e conferir ao vivo
./ap sondar <deck>                          # oráculo: legibilidade, hierarquia e sequência, parada por parada
./ap paradas <deck> [--finais] [--viagens]  # PNG por parada (ou só o fim de cada slide) + folha de contato;
                                            # --viagens: quadros no meio das viagens e no pouso (viagens.png)
./ap pdf <deck> [--todas] [--rascunho]      # uma página por slide (estado final; --todas, por parada)
./ap video <deck> [--blur 2]                # MP4 pela linha de vídeo (segura cada parada)
./ap empacotar <deck> [--saida X] [--rascunho]  # pasta que abre por file://, sem internet, com PDF de emergência
<deck> é decks/<slug>/deck.html ou só decks/<slug>. pdf e empacotar recusam deck com [CONFERIR], salvo --rascunho.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import io
import json
import os
import re
import shutil
import statistics
import subprocess
import time
from pathlib import Path

from . import config
from . import render as html

W, H = 1920, 1080
MARGEM_X, MARGEM_Y = round(W * 0.04), round(H * 0.04)
FONTE_ERRO, FONTE_AVISO = 24, 30
PALAVRAS_AVISO, PALAVRAS_ERRO = 45, 70
CONTRASTE_ERRO, CONTRASTE_AVISO = 3.0, 4.5
ISENCAO_CONTRASTE_MIN = 48          # data-contraste-ok só vale em texto grande (temas/cojuris/regras.md)
PASSO_LONGO = 3.5
# Hierarquia e sequência, calibradas na prévia do curso (decks/previa-curso-ia), que passa, e na versão a04455e dela,
# toda clara e sem nada grande, que reprova.
HIERARQUIA = 1.5                    # o maior texto da parada final contra a mediana dos outros textos
GRANDE = 120                        # px: texto (tamanho na tela) ou foto e vídeo (lado menor na tela) que domina o quadro
RESPIRO_PALAVRAS, RESPIRO_DISPLAY = 12, 200     # parada que respira: poucas palavras ou um texto display
RESPIRO_A_CADA = 5                  # slides seguidos sem respiro que ainda passam
FAIXAS = ((12, "até 12 palavras"), (24, "13 a 24 palavras"), (45, "25 a 45 palavras"), (10**9, "mais de 45 palavras"))
CLARO = 0.5                         # luminância média do still final (0 a 1) a partir da qual o slide é claro
AMPLIACAO = 1.05                    # foto exibida acima disso do tamanho natural perde nitidez no projetor


# ---------- abrir a página em modo render ----------

class _Deck:
    """Deck aberto no Chromium em modo render: expõe o resumo (window.__palco) e tira fotos de cada parada."""

    def __init__(self, p, deck: Path):
        self.srv, self.nav, self.pg, self.meta = html._abrir(p, deck)
        self.pg.wait_for_function("!!window.__palco", timeout=60000)
        self.info = self.pg.evaluate("({titulo: __palco.titulo, slides: __palco.slides, paradas: __palco.paradas, linha: __palco.linha})")

    def foto(self, n: int, ocioso: float = 0.0) -> bytes:
        self.pg.evaluate("([n, o]) => window.__palco.ir(n, o)", [n, ocioso])
        return self.pg.screenshot(type="png", clip={"x": 0, "y": 0, "width": W, "height": H})

    def foto_em(self, t: float) -> bytes:
        self.pg.evaluate("t => window.__palco.ver(t)", t)
        return self.pg.screenshot(type="png", clip={"x": 0, "y": 0, "width": W, "height": H})

    def medir(self) -> list[dict]:
        return self.pg.evaluate("window.__palco.medir()")

    def midias(self) -> list[dict]:
        return self.pg.evaluate("window.__palco.midias()")

    def medir_em(self, t: float) -> list[dict]:
        self.pg.evaluate("t => window.__palco.ver(t)", t)
        return self.medir()

    def videos_em(self, t: float) -> dict[str, float]:
        """Instante de cada vídeo visível no quadro em t (o da seção escondida não conta, mesmo que a cena o mova)."""
        self.pg.evaluate("t => window.__palco.ver(t)", t)
        return {m["src"]: m["tempo"] for m in self.midias() if m["tag"] == "video"}

    def passos_com_video(self, s: dict) -> set[int]:
        """Passos longos do slide em que um vídeo visível anda mais de meio segundo (o clipe toca e a sala assiste)."""
        tocam, t0 = set(), s["t0"]
        for k, d in enumerate(s["passos"]):
            if d > PASSO_LONGO:
                a, b = self.videos_em(t0 + 0.1), self.videos_em(t0 + d - 0.05)
                if any(abs(b[v] - a[v]) > 0.5 for v in a.keys() & b.keys()):
                    tocam.add(k)
            t0 += d
        return tocam

    def fechar(self):
        for f in (self.nav.close, self.srv.shutdown):
            try:
                f()
            except Exception:
                pass


def _abrir(deck: Path):
    from playwright.sync_api import sync_playwright

    pw = sync_playwright().start()
    d = _Deck(pw, deck)
    d._pw = pw
    return d


def _fechar(d: _Deck):
    d.fechar()
    d._pw.stop()


def finais(paradas: list[dict]) -> list[int]:
    """Índices das paradas que encerram cada slide (o slide completo)."""
    ult = {}
    for p in paradas:
        if p["passo"] >= 0:
            ult[p["slide"]] = p["n"]
    return [ult[k] for k in sorted(ult)]


# ---------- oráculo ----------

def _lum(rgb) -> float:
    def c(v):
        v = v / 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (c(x) for x in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contraste(a, b) -> float:
    la, lb = sorted((_lum(a), _lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def _fundo(img, b) -> tuple[int, int, int]:
    """Mediana dos pixels num anel de 6 px em volta da caixa do texto: aproxima o fundo sem contar as letras."""
    import numpy as np

    a = np.asarray(img.convert("RGB"))
    x0, y0 = max(0, int(b["x"]) - 6), max(0, int(b["y"]) - 6)
    x1, y1 = min(W, int(b["x"] + b["w"]) + 6), min(H, int(b["y"] + b["h"]) + 6)
    if x1 <= x0 or y1 <= y0:
        return (0, 0, 0)
    partes = [a[y0:min(y0 + 6, y1), x0:x1], a[max(y1 - 6, y0):y1, x0:x1], a[y0:y1, x0:min(x0 + 6, x1)], a[y0:y1, max(x1 - 6, x0):x1]]
    px = np.concatenate([p.reshape(-1, 3) for p in partes if p.size])
    return tuple(int(v) for v in np.median(px, axis=0))


def _contem(a: dict, b: dict) -> bool:
    return b["caminho"].startswith(a["caminho"] + " > ") or a["caminho"].startswith(b["caminho"] + " > ")


def checar_parada(blocos: list[dict], img=None) -> list[tuple[str, str]]:
    """Regras de legibilidade numa parada. `img` (PIL) habilita o contraste."""
    achados = []
    curto = lambda b: (b["texto"][:38] + "…") if len(b["texto"]) > 39 else b["texto"]
    for b in blocos:
        nome = f'"{curto(b)}"'
        if b["fonte"] < FONTE_ERRO:
            achados.append(("ERRO", f"{nome}: {b['fonte']:.0f} px na tela, ilegível no projetor (mínimo {FONTE_AVISO})"))
        elif b["fonte"] < FONTE_AVISO - 0.5:
            achados.append(("AVISO", f"{nome}: {b['fonte']:.0f} px na tela, pequeno para projeção (mínimo {FONTE_AVISO})"))
        if b["x"] < -1 or b["y"] < -1 or b["x"] + b["w"] > W + 1 or b["y"] + b["h"] > H + 1:
            achados.append(("ERRO", f"{nome}: cortado pela borda do quadro"))
        elif b["x"] < MARGEM_X or b["y"] < MARGEM_Y or b["x"] + b["w"] > W - MARGEM_X or b["y"] + b["h"] > H - MARGEM_Y:
            achados.append(("AVISO", f"{nome}: invade a margem de segurança de 4%"))
        if b["transborda"]:
            achados.append(("ERRO", f"{nome}: o texto transborda a própria caixa"))
        if b.get("topoCortado"):
            achados.append(("ERRO", f"{nome}: o pai corta o topo das letras (acento de maiúscula?); dê padding-top ao pai"))
        if 0.1 <= b["alfa"] < 0.9:
            achados.append(("AVISO", f"{nome}: meio transparente ({b['alfa']:.2f}) numa parada; a animação terminou?"))
        if img is not None:
            fundo = _fundo(img, b)
            cor = [round(b["alfa"] * c + (1 - b["alfa"]) * f) for c, f in zip(b["cor"], fundo)]
            r = contraste(cor, fundo)
            achado = None
            if r < CONTRASTE_ERRO:
                achado = ("ERRO", f"{nome}: contraste estimado {r:.1f}:1 (mínimo {CONTRASTE_AVISO})")
            elif r < CONTRASTE_AVISO and b["fonte"] < 40:
                achado = ("AVISO", f"{nome}: contraste estimado {r:.1f}:1 em texto menor que 40 px")
            motivo = b.get("contrasteOk")
            if achado and motivo and b["fonte"] >= ISENCAO_CONTRASTE_MIN:
                achado = ("ISENTO", f'{nome}: contraste estimado {r:.1f}:1, isento por data-contraste-ok: "{motivo}"')
            elif achado and motivo is not None:
                achado = (achado[0], achado[1] + f"; data-contraste-ok exige motivo e texto de {ISENCAO_CONTRASTE_MIN} px ou mais")
            if achado:
                achados.append(achado)
    # na vertical, a sobreposição mede a faixa da tinta (ty, th), quando o motor a manda: título empilhado pela tinta
    # tem caixas que se cruzam sem que as letras se toquem
    vert = lambda b: (b.get("ty", b["y"]), b.get("th", b["h"]))
    for i, a in enumerate(blocos):
        for b in blocos[i + 1:]:
            if _contem(a, b):
                continue
            (ay, ah), (by, bh) = vert(a), vert(b)
            iw = min(a["x"] + a["w"], b["x"] + b["w"]) - max(a["x"], b["x"])
            ih = min(ay + ah, by + bh) - max(ay, by)
            menor = min(a["w"] * ah, b["w"] * bh)
            if iw > 0 and ih > 0 and menor > 0 and iw * ih / menor > 0.1:
                achados.append(("AVISO", f'"{curto(a)}" e "{curto(b)}" se sobrepõem'))
    n = sum(b["palavras"] for b in blocos)
    if n > PALAVRAS_ERRO:
        achados.append(("ERRO", f"{n} palavras visíveis: slide cheio, divida (máximo {PALAVRAS_AVISO})"))
    elif n > PALAVRAS_AVISO:
        achados.append(("AVISO", f"{n} palavras visíveis: pesado para ler enquanto se ouve (máximo {PALAVRAS_AVISO})"))
    return achados


def checar_assentado(antes: list[dict], agora: list[dict]) -> list[tuple[str, str]]:
    """Texto que ainda anda dentro do próprio slide nos últimos 40 ms antes da parada: a entrada não cabe no passo e a
    parada congela o meio do movimento (e uma escala quase 1 rasteriza diferente a cada render). O deslocamento da
    seção inteira, que é a transição entre slides, não conta."""
    achados = []
    ant = {b["caminho"]: b for b in antes}
    for b in agora:
        a = ant.get(b["caminho"])
        if not a:
            continue
        dx, dy = (b["x"] - b.get("sx", 0)) - (a["x"] - a.get("sx", 0)), (b["y"] - b.get("sy", 0)) - (a["y"] - a.get("sy", 0))
        if max(abs(dx), abs(dy), abs(a["w"] - b["w"]), abs(a["h"] - b["h"])) > 1.5:
            achados.append(("AVISO", f'"{b["texto"][:38]}": ainda em movimento ao chegar na parada; alongue o passo ou adiante a entrada'))
    return achados


def checar_ritmo(slides: list[dict]) -> list[tuple[str, str]]:
    """Passo longo. `ritmoOk` (data-ritmo-ok da seção) isenta só os passos de `videoPassos`, em que um vídeo toca."""
    achados = []
    for s in slides:
        for k, d in enumerate(s["passos"]):
            if d > PASSO_LONGO:
                msg = f'slide "{s["id"]}", passo {k + 1}: {d:g} s de animação com a plateia esperando (até {PASSO_LONGO:g})'
                motivo = s.get("ritmoOk")
                if motivo and k in s.get("videoPassos", ()):
                    achados.append(("ISENTO", f'{msg}; isento por data-ritmo-ok: "{motivo}"'))
                elif motivo is not None:
                    achados.append(("AVISO", msg + "; data-ritmo-ok exige motivo e só isenta passo com vídeo tocando"))
                else:
                    achados.append(("AVISO", msg))
    return achados


def checar_hierarquia(blocos: list[dict]) -> list[tuple[str, str]]:
    """Parada final sem elemento dominante: o maior texto tem menos de HIERARQUIA vezes a mediana dos outros. As linhas
    do próprio maior texto (até 10% menores) não contam como "outros", e com menos de dois outros não há o que medir."""
    fontes = sorted(b["fonte"] for b in blocos)
    if not fontes:
        return []
    maior = fontes[-1]
    outros = [f for f in fontes if f < 0.9 * maior]
    if len(outros) < 2:
        return []
    med = statistics.median(outros)
    if maior >= HIERARQUIA * med:
        return []
    return [("AVISO", f"hierarquia: o maior texto tem {maior:.0f} px, só {maior / med:.1f}x a mediana dos outros ({med:.0f} px); "
                      f"dê ao principal pelo menos {HIERARQUIA:g}x, ou um número, palavra ou imagem grande")]


def ampliacao(m: dict) -> float:
    """Quantos px da tela cada px da imagem ocupa: o encaixe (object-fit) dentro da caixa do layout vezes a escala que a
    câmera e os transforms aplicam (caixa na tela / caixa do layout)."""
    if not (m["nw"] and m["nh"] and m["ow"] and m["oh"]):
        return 0.0
    sx, sy = m["ow"] / m["nw"], m["oh"] / m["nh"]
    encaixe = {"contain": min(sx, sy), "none": 1.0, "scale-down": min(sx, sy, 1.0)}.get(m["fit"], max(sx, sy))
    return encaixe * m["w"] / m["ow"]


def checar_imagens(midias: list[dict]) -> list[tuple[str, str]]:
    achados = []
    for m in midias:
        a = ampliacao(m)
        if m["tag"] == "img" and not m["src"].lower().endswith(".svg") and a > AMPLIACAO:
            achados.append(("AVISO", f'imagem "{m["src"]}" ampliada {a:.2f}x na tela (natural {m["nw"]}×{m["nh"]}); '
                                     "gere ou exporte maior, ou mostre menor"))
    return achados


def maior_elemento(blocos: list[dict], midias: list[dict]) -> float:
    """Maior coisa da parada: o maior texto (px na tela) ou o lado menor da parte visível de uma foto ou vídeo."""
    lados = [min(min(m["x"] + m["w"], W) - max(m["x"], 0), min(m["y"] + m["h"], H) - max(m["y"], 0)) for m in midias]
    return max([b["fonte"] for b in blocos] + lados + [0])


def checar_escala(fins: list[dict]) -> list[tuple[str, str]]:
    """Deck sem nada grande: em mais da metade dos slides, a parada final não passa de GRANDE px em nada."""
    sem = [f["id"] for f in fins if f["maior"] <= GRANDE]
    if len(sem) * 2 <= len(fins):
        return []
    lista = ", ".join(f'"{s}"' for s in sem[:6]) + (", …" if len(sem) > 6 else "")
    return [("AVISO", f"{len(sem)} de {len(fins)} slides sem nada acima de {GRANDE} px (texto, foto ou vídeo): {lista}; "
                      "o deck não muda de escala, dê a alguns um número, palavra ou imagem grande")]


def _faixa(palavras: int) -> int:
    return next(i for i, (teto, _) in enumerate(FAIXAS) if palavras <= teto)


def checar_sequencia(fins: list[dict], respiros: dict[str, bool]) -> list[tuple[str, str]]:
    """Ritmo do deck pelas paradas finais (`lum` de 0 a 1, `palavras`): três ou mais slides seguidos com o mesmo clima
    (claro ou escuro) e a mesma faixa de palavras; e mais de RESPIRO_A_CADA slides seguidos sem respiro, que é a parada
    com até RESPIRO_PALAVRAS palavras ou um texto de RESPIRO_DISPLAY px (`respiros`: slide → tem respiro)."""
    achados = []
    chave = lambda f: (f["lum"] >= CLARO, _faixa(f["palavras"]))
    i = 0
    while i < len(fins):
        j = i
        while j + 1 < len(fins) and chave(fins[j + 1]) == chave(fins[i]):
            j += 1
        if j - i >= 2:
            claro, fx = chave(fins[i])
            achados.append(("AVISO", f'slides "{fins[i]["id"]}" a "{fins[j]["id"]}": {j - i + 1} seguidos '
                                     f'{"claros" if claro else "escuros"} e com {FAIXAS[fx][1]}; troque o clima ou a densidade '
                                     "de um deles"))
        i = j + 1
    seguidos: list[str] = []
    for f in fins + [None]:
        if f is not None and not respiros.get(f["id"]):
            seguidos.append(f["id"])
            continue
        if len(seguidos) > RESPIRO_A_CADA:
            achados.append(("AVISO", f'slides "{seguidos[0]}" a "{seguidos[-1]}": {len(seguidos)} seguidos sem respiro (parada '
                                     f"com até {RESPIRO_PALAVRAS} palavras ou um texto de {RESPIRO_DISPLAY} px); ponha um a "
                                     f"cada {RESPIRO_A_CADA} slides"))
        seguidos = []
    return achados


def checar_arquetipos(slides: list[dict]) -> list[tuple[str, str]]:
    """Vizinhos com o mesmo data-arquetipo: a plateia vê a mesma tela duas vezes seguidas."""
    return [("AVISO", f'slides "{a["id"]}" e "{b["id"]}" seguidos com o mesmo arquétipo "{a["arquetipo"]}"; troque um deles')
            for a, b in zip(slides, slides[1:]) if a.get("arquetipo") and a["arquetipo"] == b.get("arquetipo")]


def sondar(deck: Path, *, determinismo: bool = True) -> int:
    from PIL import Image, ImageStat

    from . import lint

    total = {"ERRO": 0, "AVISO": 0, "ISENTO": 0}

    def relatar(onde, achados):
        for nivel, msg in achados:
            total[nivel] += 1
            print(f"{nivel:5} {onde}: {msg}")

    relatar("lint", lint.checar(deck))
    d = _abrir(deck)
    try:
        slides = d.info["slides"]
        for s in slides:
            s["videoPassos"] = d.passos_com_video(s) if s.get("ritmoOk") else set()
        relatar("ritmo", checar_ritmo(slides))
        relatar("arquétipo", checar_arquetipos(slides))
        fins, ultimas, respiros, vistas = set(finais(d.info["paradas"])), [], {}, set()
        for p in d.info["paradas"][1:]:
            antes = d.medir_em(p["t"] - 0.04)
            img = Image.open(io.BytesIO(d.foto(p["n"])))
            agora, midias = d.medir(), d.midias()
            palavras = sum(b["palavras"] for b in agora)
            maior_texto = max([b["fonte"] for b in agora] + [0])
            respiros[p["id"]] = respiros.get(p["id"]) or palavras <= RESPIRO_PALAVRAS or maior_texto >= RESPIRO_DISPLAY
            onde = f'parada {p["n"]:>2} ({p["id"]}, passo {p["passo"] + 1})'
            achados = checar_parada(agora, img) + checar_assentado(antes, agora)
            for m in midias:                                  # foto ampliada: uma vez por imagem e slide
                if (m["src"], p["id"]) not in vistas and (a := checar_imagens([m])):
                    vistas.add((m["src"], p["id"]))
                    achados += a
            if p["n"] in fins:
                achados += checar_hierarquia(agora)
                lum = ImageStat.Stat(img.convert("L")).mean[0] / 255
                ultimas.append({"id": p["id"], "palavras": palavras, "lum": lum, "maior": maior_elemento(agora, midias)})
            relatar(onde, achados)
        tempos = [tr["T0"] + 0.01 for tr in d.info["linha"] if tr["parada"] is not None]
    finally:
        _fechar(d)
    relatar("hierarquia", checar_escala(ultimas))
    relatar("sequência", checar_sequencia(ultimas, respiros))
    if determinismo:
        alvo = tempos[1:: max(1, len(tempos) // 8)][:8]
        if not html.verificar(deck, alvo):
            total["ERRO"] += 1
    isentos = f", {total['ISENTO']} isenção(ões) declarada(s)" if total["ISENTO"] else ""
    print(f"oráculo do palco: {total['ERRO']} erro(s), {total['AVISO']} aviso(s){isentos}")
    return 1 if total["ERRO"] else 0


# ---------- paradas, folha, PDF, vídeo ----------

def fotografar(deck: Path, indices: list[int] | None = None, *, todas: bool = False) -> tuple[list[tuple[dict, bytes]], dict]:
    d = _abrir(deck)
    try:
        paradas = d.info["paradas"]
        if indices is None:
            indices = [p["n"] for p in paradas[1:]] if todas else finais(paradas)
        fotos = [(paradas[n], d.foto(n)) for n in indices]
        return fotos, d.info
    finally:
        _fechar(d)


def folha(fotos: list[tuple[dict, bytes]], arq: Path, colunas: int = 4) -> Path:
    from PIL import Image, ImageDraw, ImageFont

    tw, th, rot, gap = 480, 270, 40, 16
    linhas = -(-len(fotos) // colunas)
    img = Image.new("RGB", (colunas * (tw + gap) + gap, linhas * (th + rot + gap) + gap), (24, 26, 31))
    dr = ImageDraw.Draw(img)
    fonte = ImageFont.load_default(size=22)
    for k, (p, png) in enumerate(fotos):
        if png is None:                                   # célula vazia, para alinhar as colunas
            continue
        x = gap + (k % colunas) * (tw + gap)
        y = gap + (k // colunas) * (th + rot + gap)
        img.paste(Image.open(io.BytesIO(png)).convert("RGB").resize((tw, th)), (x, y))
        dr.text((x, y + th + 8), p.get("rotulo") or f'{p["n"]} · {p["id"]} · passo {p["passo"] + 1}', fill=(200, 200, 200), font=fonte)
    img.save(arq)
    return arq


POUSO = 0.3   # s depois do pouso da câmera: o conteúdo ainda está entrando


def viagens(deck: Path, pasta: Path) -> Path:
    """Quadros a 35% e 70% de cada viagem de câmera (ou da entrada, fora do modo mundo) e POUSO s depois do pouso,
    enquanto o conteúdo entra: é onde aparecem o papel vazio no meio do caminho, a foto com borda dura e o elemento que
    some. Grava viagem-*.png e a folha viagens.png, uma linha por slide, com as colunas 35%, 70% e pouso."""
    for velho in pasta.glob("viagem-*.png"):
        velho.unlink()
    d = _abrir(deck)
    fotos: list[tuple[dict | None, bytes | None]] = []
    try:
        for i, s in enumerate(d.info["slides"][1:], 1):
            p0, nome = s["passos"][0], "viagem" if s["camera"] else "entrada"
            vg = min(p0 if s["viagem"] is None else s["viagem"], p0)
            linha = [(f"35% da {nome}", "35", s["t0"] + 0.35 * vg) if vg > 0 else None,
                     (f"70% da {nome}", "70", s["t0"] + 0.70 * vg) if vg > 0 else None,
                     (f"pouso +{POUSO:g} s".replace(".", ","), "pouso", s["t0"] + vg + POUSO) if vg + POUSO < p0 - 0.05 else None]
            for q in linha:
                if q is None:
                    fotos.append((None, None))
                    continue
                rot, tag, t = q
                png = d.foto_em(t)
                (pasta / f'viagem-{i + 1:02d}-{s["id"]}-{tag}.png').write_bytes(png)
                fotos.append(({"rotulo": f'{s["id"]} · {rot}'}, png))
    finally:
        _fechar(d)
    arq = folha(fotos, pasta / "viagens.png", colunas=3)
    print(f"{sum(1 for _, png in fotos if png)} quadros de viagem em {pasta}/ e folha em {arq}")
    return arq


def paradas(deck: Path, saida: Path | None = None, *, todas: bool = True, com_viagens: bool = False) -> Path:
    pasta = saida or deck.parent / "storyboard"
    pasta.mkdir(parents=True, exist_ok=True)
    for velho in pasta.glob("parada-*.png"):
        velho.unlink()
    fotos, _ = fotografar(deck, todas=todas)
    for p, png in fotos:
        (pasta / f'parada-{p["n"]:02d}-{p["id"]}.png').write_bytes(png)
    arq = folha(fotos, pasta / "folha.png")
    print(f"{len(fotos)} paradas em {pasta}/ e folha de contato em {arq}")
    if com_viagens:
        viagens(deck, pasta)
    else:                                  # quadros de viagem de uma rodada anterior mostrariam o deck antigo
        for velho in [*pasta.glob("viagem-*.png"), pasta / "viagens.png"]:
            velho.unlink(missing_ok=True)
    return arq


def pendencias(deck: Path) -> list[str]:
    """Cada [CONFERIR] do deck.html (texto, comentário ou código), como "linha N: trecho"."""
    achados = []
    marca = re.compile(r"\[CONFERIR\b[^\]]*\]")   # [CONFERIR] e [CONFERIR fonte ou nota]
    for n, linha in enumerate(deck.read_text(encoding="utf-8").splitlines(), 1):
        if marca.search(linha):
            trecho = " ".join(re.sub(r"<(?!!--)[^>]*>", " ", linha).split())   # sem tags; comentário fica
            i = marca.search(trecho).start()
            achados.append(f"linha {n}: {trecho[max(0, i - 60):i + 40]}")
    return achados


def _recusar_pendencias(deck: Path, rascunho: bool) -> None:
    """PDF e pacote vão para a plateia: dado sem fonte confirmada não sai, a menos que seja rascunho declarado."""
    achados = [] if rascunho else pendencias(deck)
    if achados:
        raise SystemExit(f"{deck} tem {len(achados)} [CONFERIR] sem resolver (use --rascunho para gerar mesmo assim):\n  "
                         + "\n  ".join(achados))


def pdf(deck: Path, saida: Path | None = None, *, todas: bool = False, rascunho: bool = False) -> Path:
    from PIL import Image

    _recusar_pendencias(deck, rascunho)
    fotos, info = fotografar(deck, todas=todas)
    arq = saida or deck.parent / "output" / f"{deck.parent.name}.pdf"
    arq.parent.mkdir(parents=True, exist_ok=True)
    paginas = [Image.open(io.BytesIO(png)).convert("RGB") for _, png in fotos]
    # 144 ppp: 1920×1080 vira 13,33 × 7,5 polegadas, o tamanho de slide widescreen.
    paginas[0].save(arq, "PDF", save_all=True, append_images=paginas[1:], resolution=144, title=info["titulo"])
    print(f"{arq} ({len(paginas)} páginas)")
    return arq


def video(deck: Path, saida: Path | None = None, *, blur: int = 1, paginas: int = 1) -> Path:
    arq = saida or deck.parent / "output" / f"{deck.parent.name}.mp4"
    return html.renderizar(deck, arq, blur=blur, paginas=paginas)


# ---------- empacotar para o palco ----------

_IMPORT = re.compile(r"""(\bfrom\s*|\bimport\s*\(?\s*)(['"])(\.\.?/[^'"]+)\2""")
_UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0 Safari/537.36"


def _modulos(codigo: str, base: Path, mapa: dict[str, str], nomes: dict[Path, str], raizes: tuple[Path, ...]) -> str:
    """Troca cada import relativo por um nome nu (palco/<arquivo>) e põe o módulo no mapa como URL data:, recursivamente.
    Assim o deck abre por file://, onde o Chrome não carrega módulos de arquivo. Só motor/ e a pasta do deck."""

    def troca(m):
        alvo = (base / m.group(3)).resolve()
        raiz = next((r for r in raizes if alvo.is_relative_to(r)), None)
        if not raiz or any(x.startswith(".") or x == "cache" for x in alvo.relative_to(raiz).parts):
            raise SystemExit(f"import fora de motor/ e da pasta do deck: {m.group(3)}")
        if alvo not in nomes:
            nome = f"palco/{alvo.name}"
            while nome in mapa:
                nome = f"palco/{hashlib.sha1(str(alvo).encode()).hexdigest()[:6]}-{alvo.name}"
            nomes[alvo] = nome
            mapa[nome] = ""
            corpo = _modulos(alvo.read_text(encoding="utf-8"), alvo.parent, mapa, nomes, raizes)
            mapa[nome] = "data:text/javascript;base64," + base64.b64encode(corpo.encode()).decode()
        return f"{m.group(1)}{m.group(2)}{nomes[alvo]}{m.group(2)}"

    return _IMPORT.sub(troca, codigo)


def _fontes(doc: str, pasta: Path) -> str:
    """Baixa as folhas do Google Fonts (só latin e latin-ext) e os woff2 para fontes/, e embute o CSS no HTML."""
    import requests

    (pasta / "fontes").mkdir(exist_ok=True)

    def troca(m):
        url = m.group(1).replace("&amp;", "&")
        css = requests.get(url, headers={"User-Agent": _UA}, timeout=30).text
        blocos = re.findall(r"/\*\s*([\w-]+)\s*\*/\s*(@font-face\s*{[^}]*})", css) or [("latin", b) for b in re.findall(r"@font-face\s*{[^}]*}", css)]
        saida = []
        for sub, bloco in blocos:
            if sub not in ("latin", "latin-ext"):
                continue
            for u in re.findall(r"url\((https://[^)]+)\)", bloco):
                nome = hashlib.sha1(u.encode()).hexdigest()[:12] + ".woff2"
                arq = pasta / "fontes" / nome
                if not arq.exists():
                    arq.write_bytes(requests.get(u, timeout=30).content)
                bloco = bloco.replace(u, f"fontes/{nome}")
            saida.append(bloco)
        return "<style>\n" + "\n".join(saida) + "\n</style>"

    doc = re.sub(r'<link[^>]+rel="preconnect"[^>]*>\s*', "", doc)
    return re.sub(r'<link[^>]+href="(https://fonts\.googleapis\.com/[^"]+)"[^>]*>', troca, doc)


def _arquivos(doc: str, deck: Path, pasta: Path) -> tuple[str, list[str]]:
    """Copia imagens, vídeos, folhas de estilo e o que mais o HTML ou o CSS referenciar por caminho relativo. O que é da
    pasta do deck mantém o caminho; o que vem de temas/ ou motor/ vai para _repo/<caminho no repositório>, e por isso
    as fontes e logos que o tema.css aponta com caminho relativo continuam valendo. Folhas .css copiadas têm os url()
    delas seguidos também. Mesma regra do servidor: nada fora dessas pastas, nada oculto (.env, .git), nada em cache/."""
    copiados: list[str] = []
    raiz_deck, raizes = deck.parent.resolve(), (deck.parent.resolve(), config.TEMAS.resolve(), config.MOTOR.resolve())

    def destino_de(origem: Path) -> str | None:
        base = next((b for b in raizes if origem.is_relative_to(b)), None)
        if not base or any(x.startswith(".") or x == "cache" for x in origem.relative_to(base).parts):
            return None
        return origem.relative_to(raiz_deck).as_posix() if base == raiz_deck else "_repo/" + origem.relative_to(config.RAIZ).as_posix()

    def copiar(rel: str, de: Path) -> str | None:
        """Copia o arquivo `rel` (relativo à pasta `de`) e devolve o caminho dele dentro do pacote."""
        if re.match(r"^(https?:|data:|#|mailto:|palco/)", rel) or not rel.strip():
            return None
        origem = (de / rel.split("#")[0].split("?")[0]).resolve()
        if not origem.is_file():
            return None
        dest = destino_de(origem)
        if dest is None:
            print(f"AVISO pacote: {rel} fica de fora (fora do deck, de temas/ e de motor/, oculto ou em cache/)")
            return None
        alvo = pasta / dest
        if dest not in copiados:
            alvo.parent.mkdir(parents=True, exist_ok=True)
            if origem.suffix == ".css":
                css = re.sub(r"""url\((['"]?)([^'")]+)\1\)""", lambda m: _url_css(m, origem.parent, alvo.parent), origem.read_text(encoding="utf-8"))
                alvo.write_text(css, encoding="utf-8")
            else:
                shutil.copy2(origem, alvo)
            copiados.append(dest)
        return dest

    def _url_css(m, de: Path, onde: Path) -> str:
        dest = copiar(m.group(2), de)
        if not dest:
            return m.group(0)
        return f"url({m.group(1)}{Path(os.path.relpath(pasta / dest, onde)).as_posix()}{m.group(1)})"

    def attr(m):
        novo = copiar(m.group(3), deck.parent)
        return f"{m.group(1)}={m.group(2)}{novo}{m.group(2)}" if novo else m.group(0)

    doc = re.sub(r"""\b(src|href|poster)=(['"])([^'"]+)\2""", attr, doc)
    doc = re.sub(r"""url\((['"]?)([^'")]+)\1\)""", lambda m: f"url({m.group(1)}{copiar(m.group(2), deck.parent) or m.group(2)}{m.group(1)})", doc)
    return doc, copiados


def conferir_pacote(arq: Path) -> list[str]:
    """Abre o pacote por file:// com a rede bloqueada, como no palco sem internet, e lista o que falhou."""
    from playwright.sync_api import sync_playwright

    problemas = []
    with sync_playwright() as p:
        nav = p.chromium.launch()
        ctx = nav.new_context(viewport={"width": 1280, "height": 720})
        ctx.route("**/*", lambda r: r.continue_() if r.request.url.startswith(("file:", "data:")) else r.abort())
        pg = ctx.new_page()
        pg.on("requestfailed", lambda r: problemas.append(f"requisição falhou: {r.url[:120]}"))
        pg.on("pageerror", lambda e: problemas.append(f"erro na página: {e}"))
        pg.goto(arq.resolve().as_uri() + "?vivo")
        pg.wait_for_timeout(1500)
        r = pg.evaluate("""async () => {
            await document.fonts.ready;
            const fam = {};
            for (const f of document.fonts) { fam[f.family] = fam[f.family] || f.status === 'loaded'; }
            const videos = [...document.querySelectorAll('video')].map((v) => ({src: v.getAttribute('src'), ok: v.readyState >= 1 && !v.error}));
            const imgs = [...document.images].map((im) => ({src: im.getAttribute('src'), ok: im.complete && im.naturalWidth > 0}));
            return {fam, videos, imgs};
        }""")
        for f, ok in r["fam"].items():
            if not ok:
                problemas.append(f"fonte não carregou: {f}")
        if not r["fam"]:
            print("AVISO pacote: nenhuma fonte web; o texto usa a fonte do sistema de cada computador")
        problemas += [f"vídeo não abriu: {v['src']}" for v in r["videos"] if not v["ok"]]
        problemas += [f"imagem não abriu: {i['src']}" for i in r["imgs"] if not i["ok"]]
        pg.keyboard.press("ArrowRight")
        pg.wait_for_timeout(2500)
        if "parada=1" not in pg.evaluate("location.hash"):
            problemas.append("a seta → não avançou para a parada 1")
        ap = ctx.new_page()
        ap.on("pageerror", lambda e: problemas.append(f"erro na tela do apresentador: {e}"))
        ap.goto(arq.resolve().as_uri() + "?apresentador")
        ap.wait_for_timeout(2000)
        quadros = [f for f in ap.frames if f != ap.main_frame]
        if len(quadros) != 2 or not all(f.evaluate("!!document.querySelector('#palco')") for f in quadros):
            problemas.append("a tela do apresentador não carregou as duas prévias")
        nav.close()
    return problemas


def empacotar(deck: Path, saida: Path | None = None, *, com_pdf: bool = True, rascunho: bool = False) -> Path:
    _recusar_pendencias(deck, rascunho)
    pasta = (saida or deck.parent / "pacote").resolve()
    if pasta.exists():
        # Só se apaga um pacote anterior: pasta vazia ou que tem o apresentacao.html de um empacotamento.
        if not pasta.is_dir() or (any(pasta.iterdir()) and not (pasta / "apresentacao.html").is_file()):
            raise SystemExit(f"{pasta} já existe e não é um pacote; escolha uma pasta nova em --saida")
        shutil.rmtree(pasta)
    pasta.mkdir(parents=True)
    doc = deck.read_text(encoding="utf-8")
    if "fetch(" in doc:
        print("AVISO: o deck usa fetch(), que não funciona por file://; ponha os dados no próprio HTML")
    mapa: dict[str, str] = {}
    nomes: dict[Path, str] = {}
    raizes = (deck.parent.resolve(), config.MOTOR.resolve())
    doc = re.sub(r"(<script[^>]*type=\"module\"[^>]*>)(.*?)(</script>)",
                 lambda m: m.group(1) + _modulos(m.group(2), deck.parent, mapa, nomes, raizes) + m.group(3), doc, flags=re.S)
    doc = _fontes(doc, pasta)
    doc, copiados = _arquivos(doc, deck, pasta)
    mapa_tag = '<script type="importmap">' + json.dumps({"imports": mapa}) + "</script>\n"
    doc = doc.replace("<head>", "<head>\n" + mapa_tag, 1)
    arq = pasta / "apresentacao.html"
    arq.write_text(doc, encoding="utf-8")
    if com_pdf:
        pdf(deck, pasta / "apresentacao-emergencia.pdf", rascunho=True)   # pendências já conferidas acima
    (pasta / "LEIA-ME.txt").write_text(
        "Abra apresentacao.html no Google Chrome (dois cliques ou arrastar para o navegador). Funciona sem internet.\n"
        "Teclas: seta direita, espaço ou Page Down avançam; seta esquerda volta; F tela cheia; P tela do apresentador\n"
        "(permita a janela nova); B tela preta; G índice; ? ajuda. O PDF é a contingência se o computador falhar.\n",
        encoding="utf-8")
    problemas = conferir_pacote(arq)
    tam = sum(f.stat().st_size for f in pasta.rglob("*") if f.is_file()) / 1e6
    print(f"{arq} · {len(mapa)} módulo(s), {len(list((pasta / 'fontes').glob('*')))} arquivo(s) de fonte, {len(copiados)} mídia(s), {tam:.1f} MB")
    for p in problemas:
        print("ERRO  pacote:", p)
    print("pacote: ok, abre sem internet" if not problemas else f"pacote: {len(problemas)} problema(s)")
    if problemas:
        raise SystemExit(1)
    return arq


# ---------- novo e abrir ----------

MODOS = ("continuo", "slides")


def novo(slug: str, tema: str | None = None, modo: str = "continuo") -> Path:
    """Deck novo a partir de um molde, com o link do tema trocado. `continuo` (padrão) copia o catálogo do plano
    contínuo (decks/catalogo, com a mídia-marcador e o crédito dela); `slides` copia a demonstração (decks/demo)."""
    destino = config.DECKS / slug
    if destino.exists():
        raise SystemExit(f"{destino} já existe")
    if modo not in MODOS:
        raise SystemExit(f"modo {modo} não existe; os modos são: {', '.join(MODOS)}")
    if tema and not (config.TEMAS / tema / "tema.css").is_file():
        raise SystemExit(f"tema {tema} não existe; os temas são: {', '.join(sorted(t.name for t in config.TEMAS.iterdir() if t.is_dir() and not t.name.startswith(('.', '_'))))}")
    ignorar = ("._*", "output", "storyboard", "pacote", "cache", "originais")
    if modo == "continuo":
        # a mídia do catálogo é marcador copiado da prévia e leva o crédito junto (cada item diz de onde veio)
        shutil.copytree(config.CATALOGO, destino, ignore=shutil.ignore_patterns(*ignorar))
    else:
        shutil.copytree(config.DEMO, destino, ignore=shutil.ignore_patterns(*ignorar, "creditos.json"))
    if tema:
        d = destino / "deck.html"
        d.write_text(re.sub(r"\.\./\.\./temas/[\w-]+/tema\.css", f"../../temas/{tema}/tema.css", d.read_text(encoding="utf-8")), encoding="utf-8")
    rel = destino.relative_to(config.RAIZ)
    if modo == "continuo":
        print(f"{destino / 'deck.html'} criado a partir do catálogo do plano contínuo (docs/cenas.md); reescreva o "
              f"briefing.md, troque ou apague cada slide e a mídia-marcador de midia/, e rode ./ap sondar {rel}")
    else:
        print(f"{destino / 'deck.html'} criado a partir da demonstração; troque os slides e rode ./ap sondar {rel}")
    return destino


def abrir(deck: Path) -> None:
    srv = html._servir(deck)
    rel = deck.resolve().relative_to(config.RAIZ).as_posix()
    url = f"http://127.0.0.1:{srv.server_address[1]}/{rel}"
    print(f"{url}\n(Ctrl+C encerra; P abre a tela do apresentador)")
    subprocess.run(["open", url], check=False)
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        srv.shutdown()


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("novo")
    s.add_argument("slug")
    s.add_argument("--tema", help="pasta de temas/ (padrão: o do molde)")
    s.add_argument("--modo", choices=MODOS, default="continuo",
                   help="continuo: plano contínuo a partir de decks/catalogo (padrão); slides: slides com transições a partir de decks/demo")
    for nome in ("abrir", "sondar", "paradas", "pdf", "video", "empacotar"):
        s = sub.add_parser(nome)
        s.add_argument("deck")
        if nome in ("paradas", "pdf", "video", "empacotar"):
            s.add_argument("--saida")
        if nome == "paradas":
            s.add_argument("--finais", action="store_true", help="só o estado final de cada slide")
            s.add_argument("--viagens", action="store_true", help="também quadros no meio de cada viagem e no pouso (viagens.png)")
        if nome == "pdf":
            s.add_argument("--todas", action="store_true", help="uma página por parada, não por slide")
        if nome in ("pdf", "empacotar"):
            s.add_argument("--rascunho", action="store_true", help="gera mesmo com [CONFERIR] no deck")
        if nome == "video":
            s.add_argument("--blur", type=int, default=1)
            s.add_argument("--paginas", type=int, choices=[1, 2, 3, 4], default=1)
        if nome == "sondar":
            s.add_argument("--sem-determinismo", action="store_true")
        if nome == "empacotar":
            s.add_argument("--sem-pdf", action="store_true")
    a = ap.parse_args(argv)
    if a.cmd == "novo":
        novo(a.slug, a.tema, a.modo)
        return 0
    deck = Path(a.deck)
    if deck.is_dir():
        deck = deck / "deck.html"
    if not deck.is_file():
        raise SystemExit(f"{deck} não existe")
    saida = Path(a.saida) if getattr(a, "saida", None) else None
    if a.cmd == "abrir":
        abrir(deck)
    elif a.cmd == "sondar":
        return sondar(deck, determinismo=not a.sem_determinismo)
    elif a.cmd == "paradas":
        paradas(deck, saida, todas=not a.finais, com_viagens=a.viagens)
    elif a.cmd == "pdf":
        pdf(deck, saida, todas=a.todas, rascunho=a.rascunho)
    elif a.cmd == "video":
        video(deck, saida, blur=a.blur, paginas=a.paginas)
    elif a.cmd == "empacotar":
        empacotar(deck, saida, com_pdf=not a.sem_pdf, rascunho=a.rascunho)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
