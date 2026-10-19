"""Lint estático de decks. Roda antes de todo render e no ./ap sondar.

./ap lint decks/<slug>/deck.html

Regras (inspiradas no lint de templates do open-edit da VEED, Apache-2.0; ver NOTICE), adaptadas ao
nosso contrato "cada quadro é função pura do tempo":
  ERRO  relógio do sistema (Date.now, new Date(), performance.now) fora do laço de prévia da lib
  ERRO  Math.random (use aleatorio(semente))
  ERRO  setTimeout/setInterval dentro do desenho
  ERRO  CSS transition, animation ou @keyframes: o navegador anima sozinho e o quadro varia entre renders
  ERRO  id duplicado
  AVISO família de fonte usada no CSS sem <link> do Google Fonts nem @font-face
  AVISO palco() não chamada
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

GENERICAS = {"serif", "sans-serif", "monospace", "system-ui", "cursive", "fantasy", "inherit", "initial", "ui-monospace",
             "georgia", "times new roman", "arial", "helvetica"}


def _sem_comentarios(src: str) -> str:
    src = re.sub(r"<!--.*?-->", "", src, flags=re.S)
    src = re.sub(r"/\*.*?\*/", "", src, flags=re.S)
    return re.sub(r"(?<![:\"'])//[^\n]*", "", src)


def checar(arq: Path) -> list[tuple[str, str]]:
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
    return achados


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("composicao")
    a = ap.parse_args(argv)
    achados = checar(Path(a.composicao))
    for n, m in achados:
        print(f"{n:5s} {m}")
    erros = sum(1 for n, _ in achados if n == "ERRO")
    print(f"lint: {erros} erro(s), {len(achados) - erros} aviso(s)" if achados else "lint: tudo certo")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
