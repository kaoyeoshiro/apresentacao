"""Monta decks/curso-ia-aula2/deck.html a partir de fonte/. Uso:
  python3 montar.py              monta o deck inteiro (deck.html)
  python3 montar.py a-pedir      monta só aquele bloco em decks/_p-a-pedir/deck.html (para ensaiar o bloco)
Cada bloco tem, em fonte/: <bloco>.css, <bloco>.html (as sections), <bloco>.slides.js (SLIDES.push(...)) e
<bloco>.cenas.js (código que usa `m` e preenche CENAS). A base (cabeça, rodapé, ajudantes) vive em fonte/base.*."""
import sys, pathlib, shutil

AQUI = pathlib.Path(__file__).parent
F = AQUI / "fonte"
BLOCOS = ["a-pedir", "b-escolhas", "c-skills", "d-pasta", "e-mao", "f-fecho"]

def ler(nome):
    p = F / nome
    return p.read_text(encoding="utf-8") if p.exists() else ""

def montar(blocos, destino):
    partes = [ler("base.cabeca.html"), ler("base.css")]
    partes += [ler(f"{b}.css") for b in blocos]
    partes += ["</style>\n</head>\n<body>\n<div id=\"palco\"><div id=\"mundo\">\n"]
    partes += [ler(f"{b}.html") for b in blocos]
    partes += ["\n</div></div>\n\n<script type=\"module\">\n", ler("base.topo.js")]
    partes += [ler(f"{b}.slides.js") for b in blocos]
    partes += [ler("base.meio.js")]
    partes += [ler(f"{b}.cenas.js") for b in blocos]
    partes += [ler("base.fim.js"), "</script>\n</body>\n</html>\n"]
    destino.parent.mkdir(exist_ok=True)
    destino.write_text("".join(partes), encoding="utf-8")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        b = sys.argv[1]
        assert b in BLOCOS, f"bloco desconhecido: {b}"
        d = AQUI.parent / f"_p-{b}"
        montar([b], d / "deck.html")
        dest = d / "midia"
        if dest.is_symlink():
            dest.unlink()
        shutil.copytree(AQUI / "midia", dest, dirs_exist_ok=True, ignore=shutil.ignore_patterns("originais", "._*"))
        print(d / "deck.html")
    else:
        montar(BLOCOS, AQUI / "deck.html")
        print(AQUI / "deck.html")
