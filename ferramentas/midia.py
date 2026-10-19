"""Matéria-prima para os decks, vinda dos repositórios vizinhos, sempre gravada em decks/<slug>/midia/ com crédito em
midia/creditos.json (ferramenta, modelo, prompt, custo, origem, data).

./ap imagem <deck> <nome> "prompt" [--aspect 16:9] [--resolucao 2K] [--backend gemini] [--ref img.png]
    imagem pelo image-video-api (GPT Image por padrão; Gemini com --backend gemini), via ./cvm imagem.
./ap video-ia <deck> <nome> "prompt" [--segundos 8] [--resolucao 720p] [--imagem quadro.png] [--aprovado HASH]
    clipe pelo Gemini Omni, via ./cvm veo. CUSTA DINHEIRO: sem --aprovado só orça e imprime o HASH; gerar exige o
    "sim" do usuário na conversa para aquele clipe e aquele custo.
./ap trazer <deck> <arquivo> [--nome x] --origem "de onde veio e licença"
            [--perfil tela|demo] [--ate SEG] [--capa SEG] [--com-audio]
    copia um arquivo pronto (clipe do ./cvm html, Remotion, Manim, foto com licença) e registra o crédito. Vídeo
    passa por preparar(): H.264 high yuv420p, quadro-chave a cada 0,5 s, faststart, sem áudio salvo --com-audio,
    largura até 1920 (tela) ou 2560 (demo); --ate corta o fim, --capa grava midia/<nome>-capa.webp daquele instante.
    O original fica em midia/originais/.
./ap midia conferir <deck>
    ffprobe em cada vídeo de midia/: ERRO para HEVC, ProRes, 10 bits, croma 4:2:2 ou 4:4:4; AVISO para quadro-chave
    acima de 1 s e índice (moov) no fim do arquivo. Sai 1 se houver ERRO.
"""
from __future__ import annotations

import argparse
import filecmp
import io
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


def guardar_original(pasta: Path, src: Path, destino: Path) -> Path:
    """Copia src para midia/originais/ (se ainda não estiver lá) e devolve a cópia, de onde o tratamento lê: assim
    reprocessar no lugar (src igual ao destino) não lê o próprio resultado."""
    guarda = pasta / "midia" / "originais"
    if src.parent == guarda:
        return src
    orig = guarda / src.name
    if orig.exists():
        if src == destino or filecmp.cmp(src, orig, shallow=False):
            return orig
        raise SystemExit(f"{orig} já existe com outro conteúdo; renomeie o arquivo de origem")
    guarda.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, orig)
    return orig


# ---------- vídeo ----------

VIDEOS = {".mp4", ".mov", ".m4v", ".webm", ".mkv", ".avi"}
PERFIS = {"tela": 1920, "demo": 2560}  # largura máxima


def _sonda(arq: Path, *args: str) -> str:
    return subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", *args, str(arq)], capture_output=True,
                          text=True, check=True).stdout


def _fps(arq: Path) -> float:
    s = json.loads(_sonda(arq, "-show_entries", "stream=avg_frame_rate,r_frame_rate", "-of", "json"))["streams"][0]
    for k in ("avg_frame_rate", "r_frame_rate"):
        n, _, d = s.get(k, "0/0").partition("/")
        if float(n) > 0 and float(d or 1) > 0:
            return float(n) / float(d or 1)
    return 30.0  # sem taxa declarada


def preparar(arquivo: Path, destino: Path, perfil: str = "tela", *, ate=None, capa=None, com_audio=False) -> Path:
    """Converte para o que o Chromium toca e busca sem engasgar: H.264 high, yuv420p, crf 20, quadro-chave a cada
    0,5 s, índice no começo (faststart). Com capa, grava <nome>-capa.webp daquele instante do vídeo já
    convertido."""
    g = str(max(1, round(_fps(arquivo) * 0.5)))
    larg = PERFIS[perfil]
    cmd = ["ffmpeg", "-y", "-v", "error", "-i", str(arquivo)]
    if ate is not None:
        cmd += ["-t", str(ate)]
    cmd += ["-vf", f"scale='trunc(min({larg},iw)/2)*2':-2:flags=lanczos", "-c:v", "libx264", "-profile:v", "high",
            "-pix_fmt", "yuv420p", "-crf", "20", "-preset", "slow", "-g", g, "-keyint_min", g,
            "-movflags", "+faststart", "-map_metadata", "-1"]
    cmd += ["-c:a", "aac", "-b:a", "160k"] if com_audio else ["-an"]
    destino.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([*cmd, str(destino)], check=True)
    if capa is not None:
        png = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(capa), "-i", str(destino), "-frames:v", "1", "-f",
                              "image2pipe", "-c:v", "png", "-"], capture_output=True, check=True).stdout
        if not png:
            raise SystemExit(f"--capa {capa}: o vídeo não tem quadro nesse instante")
        from PIL import Image
        Image.open(io.BytesIO(png)).save(destino.with_name(f"{destino.stem}-capa.webp"), quality=85, method=6)
    return destino


def _moov_no_fim(arq: Path) -> bool:
    """Lê as caixas do topo do MP4/MOV: o índice (moov) depois dos dados (mdat) obriga o navegador a ir ao fim do
    arquivo antes de tocar."""
    ordem = []
    with open(arq, "rb") as f:
        while len(ordem) < 64:
            cab = f.read(8)
            if len(cab) < 8:
                break
            tam, tipo = int.from_bytes(cab[:4], "big"), cab[4:].decode("latin-1")
            if tam == 1:
                tam = int.from_bytes(f.read(8), "big") - 8
            ordem.append(tipo)
            if tam == 0:
                break
            f.seek(tam - 8, 1)
    return "moov" in ordem and "mdat" in ordem and ordem.index("mdat") < ordem.index("moov")


def checar_video(arq: Path) -> list[tuple[str, str]]:
    s = json.loads(_sonda(arq, "-show_entries", "stream=codec_name,pix_fmt,bits_per_raw_sample:format=duration",
                          "-of", "json"))
    if not s.get("streams"):
        return [("AVISO", "sem faixa de vídeo")]
    st, dur = s["streams"][0], float(s.get("format", {}).get("duration") or 0)
    codec, pix = st.get("codec_name", ""), st.get("pix_fmt", "")
    achados = []
    if codec in ("hevc", "prores"):
        achados.append(("ERRO", f"{codec.upper()}: o Chromium não toca; reconverta com ./ap trazer"))
    if any(b in pix for b in ("p10", "p12")) or int(st.get("bits_per_raw_sample") or 8) > 8:
        achados.append(("ERRO", f"{pix}: mais de 8 bits por cor; reconverta com ./ap trazer"))
    if "422" in pix or "444" in pix:
        achados.append(("ERRO", f"{pix}: croma 4:2:2 ou 4:4:4; reconverta com ./ap trazer"))
    chaves = sorted(float(t) for t, _, fl in (l.partition(",") for l in _sonda(
        arq, "-show_entries", "packet=pts_time,flags", "-of", "csv=p=0").split()) if "K" in fl and t not in ("", "N/A"))
    if chaves:
        maior = max(b - a for a, b in zip(chaves, chaves[1:] + [max(dur, chaves[-1])]))
        if maior > 1:
            achados.append(("AVISO", f"quadro-chave a cada {maior:.1f} s; voltar e buscar engasgam "
                                     "(./ap trazer põe 0,5 s)"))
    if arq.suffix.lower() in (".mp4", ".mov", ".m4v") and _moov_no_fim(arq):
        achados.append(("AVISO", "índice (moov) no fim do arquivo; reconverta com ./ap trazer (faststart)"))
    return achados


def conferir(deck: str) -> int:
    pasta = _deck(deck)
    total = {"ERRO": 0, "AVISO": 0}
    midia = pasta / "midia"
    for v in sorted(midia.iterdir() if midia.is_dir() else []):
        if v.name.startswith("._") or v.suffix.lower() not in VIDEOS:
            continue
        try:
            achados = checar_video(v)
        except subprocess.CalledProcessError:
            achados = [("ERRO", "o ffprobe não conseguiu ler o arquivo")]
        for nivel, msg in achados:
            total[nivel] += 1
            print(f"{nivel:5} {v.name}: {msg}")
    print(f"mídia: {total['ERRO']} erro(s), {total['AVISO']} aviso(s)")
    return 1 if total["ERRO"] else 0


def trazer(deck: str, arquivo: str, *, nome=None, origem: str, perfil="tela", ate=None, capa=None,
           com_audio=False) -> Path:
    pasta = _deck(deck)
    src = Path(arquivo).resolve()
    if not src.is_file():
        raise SystemExit(f"{src} não existe")
    destino = pasta / "midia" / (nome or src.name)
    if src.suffix.lower() not in VIDEOS:
        destino.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, destino)
        creditar(pasta, destino, ferramenta="trazido", origem=origem)
        print(destino)
        return destino
    destino = destino.with_suffix(".mp4")
    orig = guardar_original(pasta, src, destino)
    preparar(orig, destino, perfil, ate=ate, capa=capa, com_audio=com_audio)
    rel = orig.relative_to(pasta).as_posix()
    creditar(pasta, destino, ferramenta="trazido", origem=origem, original=rel,
             preparo={"perfil": perfil, "ate": ate, "audio": com_audio})
    if capa is not None:
        creditar(pasta, destino.with_name(f"{destino.stem}-capa.webp"), ferramenta="trazido", origem=origem,
                 quadro_de=destino.relative_to(pasta).as_posix(), segundo=capa)
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
    s.add_argument("--perfil", default="tela", choices=sorted(PERFIS),
                   help="vídeo: largura até 1920 (tela) ou 2560 (demo)")
    s.add_argument("--ate", type=float, metavar="SEG", help="vídeo: corta o que vier depois deste segundo")
    s.add_argument("--capa", type=float, metavar="SEG", help="vídeo: grava <nome>-capa.webp deste instante")
    s.add_argument("--com-audio", action="store_true", help="vídeo: mantém o áudio (padrão: sem áudio)")
    s = sub.add_parser("conferir")
    s.add_argument("deck")
    a = ap.parse_args(argv)
    if a.cmd == "imagem":
        imagem(a.deck, a.nome, a.prompt, aspect=a.aspect, resolucao=a.resolucao, backend=a.backend, refs=a.ref)
    elif a.cmd == "video-ia":
        video_ia(a.deck, a.nome, a.prompt, segundos=a.segundos, resolucao=a.resolucao, aspect=a.aspect, imagem=a.imagem,
                 aprovado=a.aprovado)
    elif a.cmd == "conferir":
        return conferir(a.deck)
    else:
        trazer(a.deck, a.arquivo, nome=a.nome, origem=a.origem, perfil=a.perfil, ate=a.ate, capa=a.capa,
               com_audio=a.com_audio)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
