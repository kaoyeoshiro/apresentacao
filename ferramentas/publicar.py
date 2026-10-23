"""Publica um deck no site da co.juris (Cloudflare Pages), em /apresentacao/<pasta>/.

./ap publicar <deck> --site <pasta do site> --pasta aula-2 --titulo "Título" --descricao "Uma frase" [--rascunho]

Empacota o deck (o mesmo pacote que abre sem internet), copia para <site>/public/apresentacao/<pasta>/ com o arquivo
principal como index.html, e põe (ou atualiza) a linha dele na página de entrada <site>/public/apresentacao/index.html,
entre os marcadores lista-apresentacoes. Não faz commit nem deploy: o site tem o próprio ciclo (npm run deploy).
"""
from __future__ import annotations

import argparse
import html
import re
import shutil
import tempfile
from pathlib import Path

FIM = "<!-- fim-lista-apresentacoes -->"


def _item(pasta: str, numero: int, titulo: str, descricao: str) -> str:
    return (
        f'    <li><a href="/apresentacao/{pasta}/">\n'
        f'      <div class="numero">Apresentação {numero}</div>\n'
        f'      <p class="titulo">{html.escape(titulo)}</p>\n'
        f'      <p class="descricao">{html.escape(descricao)}</p>\n'
        f'    </a></li>\n'
    )


def atualizar_indice(texto: str, pasta: str, titulo: str, descricao: str) -> str:
    """Põe a apresentação na lista; se a pasta já está nela, troca título e descrição e mantém o número."""
    if FIM not in texto:
        raise SystemExit(f"a página de entrada não tem o marcador {FIM}")
    achou = re.search(
        rf'    <li><a href="/apresentacao/{re.escape(pasta)}/">\n      <div class="numero">Apresentação (\d+)</div>.*?</a></li>\n',
        texto, flags=re.S)
    if achou:
        return texto[:achou.start()] + _item(pasta, int(achou.group(1)), titulo, descricao) + texto[achou.end():]
    numero = texto.count('<div class="numero">Apresentação ') + 1
    return texto.replace("    " + FIM, _item(pasta, numero, titulo, descricao) + "    " + FIM, 1)


def copiar_pacote(pacote: Path, destino: Path) -> None:
    """Troca a pasta de destino pelo pacote, sem LEIA-ME nem lixo do sistema; apresentacao.html vira index.html."""
    if destino.exists():
        shutil.rmtree(destino)
    shutil.copytree(pacote, destino, ignore=shutil.ignore_patterns("._*", ".DS_Store", "LEIA-ME.txt"))
    (destino / "apresentacao.html").rename(destino / "index.html")
    vazia = destino / "fontes"
    if vazia.is_dir() and not any(vazia.iterdir()):
        vazia.rmdir()


def publicar(deck: Path, site: Path, pasta: str, titulo: str, descricao: str, rascunho: bool = False) -> Path:
    from ferramentas.palco import empacotar

    base = site / "public" / "apresentacao"
    indice = base / "index.html"
    if not indice.is_file():
        raise SystemExit(f"{indice} não existe: o site ainda não tem a página de entrada de /apresentacao")
    if not re.fullmatch(r"[a-z0-9-]+", pasta):
        raise SystemExit("--pasta só aceita letras minúsculas, números e hífen (ex.: aula-2)")
    with tempfile.TemporaryDirectory() as tmp:
        pacote = empacotar(deck, Path(tmp) / "pacote", rascunho=rascunho)
        pacote = Path(pacote)
        copiar_pacote(pacote.parent if pacote.is_file() else pacote, base / pasta)
    indice.write_text(atualizar_indice(indice.read_text(encoding="utf-8"), pasta, titulo, descricao), encoding="utf-8")
    return base / pasta


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("deck")
    ap.add_argument("--site", required=True, help="pasta do projeto do site (a que tem public/ e wrangler.toml)")
    ap.add_argument("--pasta", required=True)
    ap.add_argument("--titulo", required=True)
    ap.add_argument("--descricao", required=True)
    ap.add_argument("--rascunho", action="store_true", help="publica mesmo com [CONFERIR] no deck")
    a = ap.parse_args(argv)
    deck = Path(a.deck)
    if deck.is_dir():
        deck = deck / "deck.html"
    if not deck.is_file():
        raise SystemExit(f"{deck} não existe")
    destino = publicar(deck, Path(a.site), a.pasta, a.titulo, a.descricao, a.rascunho)
    print(f"copiado para {destino}\nfalta, no site: git add public/apresentacao && git commit && npm run deploy")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
