"""Matéria-prima para os decks, vinda dos repositórios vizinhos, sempre gravada em decks/<slug>/midia/ com crédito em
midia/creditos.json (ferramenta, modelo, prompt, custo, origem, data).

./ap imagem <deck> <nome> "prompt" [--aspect 16:9] [--resolucao 2K] [--backend gemini] [--ref img.png]
    imagem pelo image-video-api (GPT Image por padrão; Gemini com --backend gemini), via ./cvm imagem.
./ap video-ia <deck> <nome> "prompt" [--segundos 8] [--resolucao 720p] [--imagem quadro.png] [--aprovado HASH]
    clipe pelo Gemini Omni, via ./cvm veo. CUSTA DINHEIRO: sem --aprovado só orça e imprime o HASH; gerar exige o
    "sim" do usuário na conversa para aquele clipe e aquele custo.
./ap trazer <deck> <arquivo> [--nome x] --origem "de onde veio e licença"
    copia um arquivo pronto (clipe do ./cvm html, Remotion, Manim, foto com licença) e registra o crédito.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
from datetime import date
from pathlib import Path

from . import config


def _deck(deck: str) -> Path:
    p = Path(deck)
    pasta = p.parent if p.suffix == ".html" else p
    if not (pasta / "deck.html").is_file():
        raise SystemExit(f"{pasta} não tem deck.html")
    return pasta.resolve()


def creditar(pasta: Path, arquivo: Path, **campos) -> Path:
    """Cria ou substitui a entrada do arquivo em midia/creditos.json."""
    arq = pasta / "midia" / "creditos.json"
    itens = json.loads(arq.read_text()) if arq.exists() else []
    nome = arquivo.resolve().relative_to(pasta).as_posix()
    itens = [i for i in itens if i["arquivo"] != nome]
    itens.append({"arquivo": nome, "data": date.today().isoformat(), **{k: v for k, v in campos.items() if v is not None}})
    arq.parent.mkdir(parents=True, exist_ok=True)
    arq.write_text(json.dumps(sorted(itens, key=lambda i: i["arquivo"]), ensure_ascii=False, indent=1))
    return arq


def cvm(*args: str) -> int:
    """O ./cvm usa o próprio ambiente Python só se não herdar o nosso (o ./ap exporta UV_PROJECT_ENVIRONMENT)."""
    env = {k: v for k, v in os.environ.items() if k not in ("UV_PROJECT_ENVIRONMENT", "VIRTUAL_ENV")}
    return subprocess.run(["bash", str(config.video_maker() / "cvm"), *args], env=env).returncode


def imagem(deck: str, nome: str, prompt: str, *, aspect="16:9", resolucao="2K", backend=None, refs=()) -> Path:
    pasta = _deck(deck)
    saida = pasta / "midia" / (nome if Path(nome).suffix else f"{nome}.png")
    args = ["imagem", prompt, "--saida", str(saida), "--aspect", aspect, "--resolucao", resolucao]
    if backend:
        args += ["--backend", backend]
    for r in refs:
        args += ["--ref", str(Path(r).resolve())]
    if cvm(*args):
        raise SystemExit("a geração de imagem falhou (mensagem acima)")
    creditar(pasta, saida, ferramenta="image-video-api (./cvm imagem)", modelo=backend or "padrão do image-video-api",
             prompt=prompt, parametros={"aspecto": aspect, "resolucao": resolucao}, licenca="termos do provedor do modelo")
    print(saida)
    return saida


def video_ia(deck: str, nome: str, prompt: str, *, segundos=8, resolucao="720p", aspect="16:9", imagem=None,
             aprovado=None) -> Path | None:
    """O ./cvm veo só grava dentro de videos/<slug>/ do claude_video_maker (é lá que fica o orçamento aprovado).
    Gera em videos/ap-<deck>/public/clipes/ e copia para o deck."""
    pasta = _deck(deck)
    vm = config.video_maker()
    arq = nome if Path(nome).suffix else f"{nome}.mp4"
    origem = vm / "videos" / f"ap-{pasta.name}" / "public" / "clipes" / arq
    args = ["veo", prompt, "--saida", str(origem), "--segundos", str(segundos), "--resolucao", resolucao, "--aspect", aspect]
    if imagem:
        args += ["--imagem", str(Path(imagem).resolve())]
    if aprovado:
        args += ["--aprovado", aprovado]
    r = cvm(*args)
    if not aprovado or r:
        if not aprovado:
            print("Só orçado. Mostre o custo ao usuário; com o sim dele, rode de novo com --aprovado HASH.")
        return None
    destino = pasta / "midia" / arq
    destino.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(origem, destino)
    orc = sorted((origem.parents[2] / "cache").glob("veo-orcamento-*.json"))
    custo = next((json.loads(o.read_text()).get("custo_usd") for o in orc if aprovado in o.name), None)
    creditar(pasta, destino, ferramenta="Gemini Omni (./cvm veo)", prompt=prompt, custo_usd=custo,
             parametros={"segundos": segundos, "resolucao": resolucao, "aspecto": aspect}, origem=str(origem),
             licenca="Gemini API Additional Terms, Use of Generated Content")
    print(destino)
    return destino


def trazer(deck: str, arquivo: str, *, nome=None, origem: str) -> Path:
    pasta = _deck(deck)
    src = Path(arquivo).resolve()
    if not src.is_file():
        raise SystemExit(f"{src} não existe")
    destino = pasta / "midia" / (nome or src.name)
    destino.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, destino)
    creditar(pasta, destino, ferramenta="trazido", origem=origem)
    print(destino)
    return destino


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("imagem")
    for a in ("deck", "nome", "prompt"):
        s.add_argument(a)
    s.add_argument("--aspect", default="16:9")
    s.add_argument("--resolucao", default="2K", choices=["1K", "2K", "4K"])
    s.add_argument("--backend")
    s.add_argument("--ref", action="append", default=[])
    s = sub.add_parser("video-ia")
    for a in ("deck", "nome", "prompt"):
        s.add_argument(a)
    s.add_argument("--segundos", type=int, default=8, choices=[4, 6, 8])
    s.add_argument("--resolucao", default="720p", choices=["360p", "720p", "1080p", "4k"])
    s.add_argument("--aspect", default="16:9", choices=["16:9", "9:16"])
    s.add_argument("--imagem")
    s.add_argument("--aprovado", metavar="HASH")
    s = sub.add_parser("trazer")
    s.add_argument("deck")
    s.add_argument("arquivo")
    s.add_argument("--nome")
    s.add_argument("--origem", required=True, help="de onde veio e sob que licença")
    a = ap.parse_args(argv)
    if a.cmd == "imagem":
        imagem(a.deck, a.nome, a.prompt, aspect=a.aspect, resolucao=a.resolucao, backend=a.backend, refs=a.ref)
    elif a.cmd == "video-ia":
        video_ia(a.deck, a.nome, a.prompt, segundos=a.segundos, resolucao=a.resolucao, aspect=a.aspect, imagem=a.imagem,
                 aprovado=a.aprovado)
    else:
        trazer(a.deck, a.arquivo, nome=a.nome, origem=a.origem)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
