"""Lint estático de decks. Roda antes de todo render e no ./ap sondar.

./ap lint decks/<slug>            # ou decks/<slug>/deck.html, ou uma folha de motor/ (motor/cenas.css)

Regras (inspiradas no lint de templates do open-edit da VEED, Apache-2.0; ver NOTICE), adaptadas ao
nosso contrato "cada quadro é função pura do tempo":
  ERRO  relógio do sistema (Date.now, new Date(), performance.now) fora do laço de prévia da lib
  ERRO  Math.random (use aleatorio(semente))
  ERRO  setTimeout/setInterval dentro do desenho
  ERRO  CSS transition, animation ou @keyframes: o navegador anima sozinho e o quadro varia entre renders
  ERRO  id duplicado
  AVISO getBoundingClientRect: inclui a escala do tocador e o zoom da câmera (meça com caixa() do motor)
  AVISO família de fonte usada no CSS sem <link> do Google Fonts nem @font-face
  AVISO palco() não chamada
  ERRO  cor literal (hex, nome de cor como white, rgb(), hsl() e afins, fora de comentário e de texto entre aspas) numa
        folha de motor/, como motor/cenas.css: ali só entra var() do tema. Vale para ./ap lint motor/cenas.css e para a
        folha de motor/ que o deck liga. A folha do tema (temas/*/tema.css) é onde a cor literal mora: o lint não a olha
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from . import config

GENERICAS = {"serif", "sans-serif", "monospace", "system-ui", "cursive", "fantasy", "inherit", "initial", "ui-monospace",
             "georgia", "times new roman", "arial", "helvetica"}


def _sem_comentarios(src: str) -> str:
    src = re.sub(r"<!--.*?-->", "", src, flags=re.S)
    src = re.sub(r"/\*.*?\*/", "", src, flags=re.S)
    return re.sub(r"(?<![:\"'])//[^\n]*", "", src)


# Os 148 nomes de cor do CSS; transparent e currentColor ficam de fora, porque não trazem cor própria.
NOMES_COR = """aliceblue antiquewhite aqua aquamarine azure beige bisque black blanchedalmond blue blueviolet brown burlywood
cadetblue chartreuse chocolate coral cornflowerblue cornsilk crimson cyan darkblue darkcyan darkgoldenrod darkgray darkgreen
darkgrey darkkhaki darkmagenta darkolivegreen darkorange darkorchid darkred darksalmon darkseagreen darkslateblue darkslategray
darkslategrey darkturquoise darkviolet deeppink deepskyblue dimgray dimgrey dodgerblue firebrick floralwhite forestgreen fuchsia
gainsboro ghostwhite gold goldenrod gray green greenyellow grey honeydew hotpink indianred indigo ivory khaki lavender
lavenderblush lawngreen lemonchiffon lightblue lightcoral lightcyan lightgoldenrodyellow lightgray lightgreen lightgrey
lightpink lightsalmon lightseagreen lightskyblue lightslategray lightslategrey lightsteelblue lightyellow lime limegreen linen
magenta maroon mediumaquamarine mediumblue mediumorchid mediumpurple mediumseagreen mediumslateblue mediumspringgreen
mediumturquoise mediumvioletred midnightblue mintcream mistyrose moccasin navajowhite navy oldlace olive olivedrab orange
orangered orchid palegoldenrod palegreen paleturquoise palevioletred papayawhip peachpuff peru pink plum powderblue purple
rebeccapurple red rosybrown royalblue saddlebrown salmon sandybrown seagreen seashell sienna silver skyblue slateblue slategray
slategrey snow springgreen steelblue tan teal thistle tomato turquoise violet wheat white whitesmoke yellow yellowgreen""".split()

# Cor escrita à mão numa declaração. O seletor (#abc), o url(#id), a propriedade (white-space), a variável (--cor-red) e a
# função tan() não contam.
COR_LITERAL = re.compile(r"#(?:[0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3,4})\b|\b(?:rgba?|hsla?|hwb|lab|lch|oklab|oklch)\s*\("
                         r"|(?<![-\w])(?:" + "|".join(NOMES_COR) + r")(?![-\w]|\s*\()", re.I)


def checar_css(arq: Path, nome: str | None = None) -> list[tuple[str, str]]:
    """Folha de estilo do motor: a cor vem só do tema, por var(). Comentários, url() e texto entre aspas ("Red Hat Display")
    viram espaço (as linhas ficam)."""
    src = re.sub(r"/\*.*?\*/|url\([^)]*\)|\"[^\"\n]*\"|'[^'\n]*'", lambda m: re.sub(r"[^\n]", " ", m.group(0)), arq.read_text(encoding="utf-8"), flags=re.S)
    nome = nome or arq.name
    achados = []
    for bloco in re.finditer(r"\{([^{}]*)\}", src):          # só o miolo das regras, onde estão as declarações
        for m in COR_LITERAL.finditer(bloco.group(1)):
            n = src[: bloco.start(1) + m.start()].count("\n") + 1
            achados.append(("ERRO", f"{nome}, linha {n}: cor literal {re.sub(r'[(\s]+$', '()', m.group(0))}; use var() do tema (docs/temas.md)"))
    return achados


def checar(arq: Path) -> list[tuple[str, str]]:
    if arq.suffix == ".css":     # só a folha de motor/; a do tema é onde a cor literal mora
        return checar_css(arq) if arq.resolve().is_relative_to(config.MOTOR.resolve()) else []
    bruto = arq.read_text(encoding="utf-8")
    src = _sem_comentarios(bruto)
    achados: list[tuple[str, str]] = []

    def linha(m) -> int:
        return src[: m.start()].count("\n") + 1

    regras = [
        (r"\bDate\.now\s*\(|\bnew\s+Date\s*\(|\bperformance\.now\s*\(", "relógio do sistema: o quadro depende da hora do render"),
        (r"\bMath\.random\s*\(", "Math.random: use aleatorio(semente) de motor/tempo.js"),
        (r"\bset(Timeout|Interval)\s*\(", "timer: o renderizador não espera por ele; derive tudo de t"),
        (r"(?<![-\w])transition\s*:", "CSS transition: anima fora do controle do tempo t"),
        (r"(?<![-\w])animation(-name)?\s*:", "CSS animation: anima fora do controle do tempo t"),
        (r"@keyframes", "@keyframes: anima fora do controle do tempo t"),
    ]
    for padrao, msg in regras:
        for m in re.finditer(padrao, src):
            achados.append(("ERRO", f"linha {linha(m)}: {msg}"))

    for m in re.finditer(r"\bgetBoundingClientRect\s*\(", src):
        achados.append(("AVISO", f"linha {linha(m)}: getBoundingClientRect inclui a escala do tocador e o zoom da câmera; meça com caixa() do motor"))

    ids = re.findall(r'\bid="([^"]+)"', src)
    for i in sorted({i for i in ids if ids.count(i) > 1}):
        achados.append(("ERRO", f'id duplicado: "{i}"'))

    carregadas = {f.replace("+", " ").lower() for f in re.findall(r"family=([A-Za-z0-9+]+)", bruto)}
    carregadas |= {f.lower() for f in re.findall(r"@font-face\s*{[^}]*font-family\s*:\s*['\"]?([^;'\"]+)", src)}
    usadas = set()
    for bloco in re.findall(r"font(?:-family)?\s*:\s*([^;}\n]+)", src):
        for nome in re.findall(r"['\"]([^'\"]+)['\"]", bloco):
            usadas.add(nome.strip().lower())
    for u in sorted(usadas - carregadas - GENERICAS):
        achados.append(("AVISO", f'fonte "{u}" usada sem carregar (cai na fonte padrão do sistema)'))

    if "palco(" not in src:
        achados.append(("AVISO", "palco() não é chamada: o deck não tem tocador nem modo render"))
    for tag in re.findall(r"<link\b[^>]*>", src):
        href = re.search(r"""\bhref=["']([^"']+)["']""", tag)
        if not href or not re.search(r"""\brel=["']?stylesheet""", tag):
            continue
        folha = (arq.parent / href.group(1)).resolve()
        if folha.is_file() and folha.is_relative_to(config.MOTOR.resolve()):
            achados += checar_css(folha, folha.relative_to(config.MOTOR.resolve().parent).as_posix())
    return achados


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("composicao")
    a = ap.parse_args(argv)
    alvo = Path(a.composicao)
    if alvo.is_dir():                     # ./ap lint decks/<slug>, como sondar e paradas
        alvo = alvo / "deck.html"
    if not alvo.is_file():
        raise SystemExit(f"{alvo} não existe")
    achados = checar(alvo)
    for n, m in achados:
        print(f"{n:5s} {m}")
    erros = sum(1 for n, _ in achados if n == "ERRO")
    print(f"lint: {erros} erro(s), {len(achados) - erros} aviso(s)" if achados else "lint: tudo certo")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
