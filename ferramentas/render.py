"""Renderizador: abre o deck no Chromium headless (modo render do motor, window.__seek(T) + window.__meta), tira um
quadro por vez e codifica com FFmpeg. Adaptado do motor HTML do claude_video_maker. Opcional: desfoque de movimento
por sub-quadros (obturador).

./ap render decks/<slug>/deck.html --saida x.mp4 [--blur 4] [--paginas 3] [--de 0 --ate 5]
./ap render decks/<slug>/deck.html --verificar 3,11,17
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit

from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import TimeoutError as PlaywrightTimeout
from playwright.sync_api import sync_playwright

from . import config


class _Silencioso(SimpleHTTPRequestHandler):
    """Servidor estático com suporte a Range: o Chrome precisa dele para posicionar <video>."""

    def log_message(self, *a):
        pass

    def _liberado(self) -> bool:
        """Só as pastas permitidas (motor/, temas/ e a pasta do deck); nada de segmento oculto (.env, .git) nem de cache/."""
        partes = unquote(urlsplit(self.path).path).split("/")
        if any(p.startswith(".") or p == "cache" for p in partes if p):
            return False
        alvo = Path(self.translate_path(self.path)).resolve()
        return any(alvo.is_relative_to(r) for r in self.server.permitidos)

    def send_head(self):
        if not self._liberado():
            self.send_error(404, "fora das pastas servidas (motor/, temas/ e a pasta do deck; cache/ e ocultos nunca)")
            return None
        rng = self.headers.get("Range")
        caminho = Path(self.translate_path(self.path))
        if not rng or not caminho.is_file():
            return super().send_head()
        tam = caminho.stat().st_size
        ini, _, fim = rng.replace("bytes=", "").partition("-")
        ini = int(ini or 0)
        fim = min(int(fim) if fim else tam - 1, tam - 1)
        f = open(caminho, "rb")
        f.seek(ini)
        self.send_response(206)
        self.send_header("Content-Type", self.guess_type(str(caminho)))
        self.send_header("Accept-Ranges", "bytes")
        self.send_header("Content-Range", f"bytes {ini}-{fim}/{tam}")
        self.send_header("Content-Length", str(fim - ini + 1))
        self.end_headers()
        self._resto = fim - ini + 1
        return f

    def copyfile(self, source, outputfile):
        resto = getattr(self, "_resto", None)
        if resto is None:
            return super().copyfile(source, outputfile)
        while resto > 0:
            bloco = source.read(min(1 << 16, resto))
            if not bloco:
                break
            try:
                outputfile.write(bloco)
            except (BrokenPipeError, ConnectionResetError):  # o navegador cancelou o pedaço; normal com vídeo
                break
            resto -= len(bloco)
        self._resto = None


def _servir(comp: Path):
    """Servidor HTTP local com a raiz do repositório nas URLs (módulos ES e imagens funcionam como numa página real),
    mas que serve só motor/, temas/ e a pasta do deck: um script de fora não alcança o resto do repositório."""
    srv = ThreadingHTTPServer(("127.0.0.1", 0), partial(_Silencioso, directory=str(config.RAIZ)))
    srv.permitidos = (config.MOTOR.resolve(), config.TEMAS.resolve(), comp.resolve().parent)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


class ErroDoDeck(RuntimeError):
    """O deck lançou erro ao abrir (arquétipo ou andamento que não existe, lista de slides inválida...)."""


def esperar(pg, expr: str, segundos: float) -> None:
    """Espera `expr` ficar verdadeira na página, mas para logo, com a mensagem do deck, se ele lançar erro antes:
    sem isso, um erro de digitação no deck vira 180 s de espera e um TimeoutError sem a causa."""
    fim = time.monotonic() + segundos
    while True:
        try:
            pg.wait_for_function(expr, timeout=500)
            return
        except PlaywrightTimeout:
            if pg.erros_do_deck:
                raise ErroDoDeck(f"o deck parou com erro: {pg.erros_do_deck[0]}") from None
            if time.monotonic() > fim:
                raise


def _abrir(p, comp: Path, args: tuple[str, ...] = ()):
    srv = _servir(comp)
    rel = comp.resolve().relative_to(config.RAIZ).as_posix()
    nav = p.chromium.launch(args=list(args))
    pg = nav.new_page(viewport={"width": 1920, "height": 1920})
    # erro não tratado do script e console.error do deck; recurso que falta (404) não para nada aqui
    pg.erros_do_deck = []
    pg.on("pageerror", lambda e: pg.erros_do_deck.append(str(e)))
    pg.on("console", lambda m: m.type == "error" and not m.text.startswith("Failed to load resource")
          and pg.erros_do_deck.append(m.text))
    try:
        pg.goto(f"http://127.0.0.1:{srv.server_address[1]}/{rel}")
        esperar(pg, "!!(window.__meta && window.__seek)", 180)
    except BaseException:
        nav.close()
        srv.shutdown()
        raise
    meta = pg.evaluate("window.__meta")
    pg.evaluate("document.fonts.ready.then(() => 0)")  # texto em canvas com webfont atrasada sairia na fonte de reserva
    pg.set_viewport_size({"width": meta["largura"], "height": meta["altura"]})
    return srv, nav, pg, meta


class _Resiliente:
    """Página que sobrevive à morte do Chromium no meio do render (memória apertada mata o processo do navegador):
    reabre, repõe o último instante e repete a operação. Como o quadro só depende do instante t, retomar é exato."""

    def __init__(self, p, comp: Path, aberto):
        self.p, self.comp = p, comp
        self.srv, self.nav, self.pg, self.meta = aberto
        self._ult = None

    def _reabrir(self):
        for fechar in (self.nav.close, self.srv.shutdown):
            try:
                fechar()
            except Exception:
                pass
        self.srv, self.nav, self.pg, _ = _abrir(self.p, self.comp)
        if self._ult:
            self.pg.evaluate(*self._ult)

    def _tentar(self, op: str, *a, **k):
        for tentativa in range(4):
            try:
                return getattr(self.pg, op)(*a, **k)
            except PlaywrightError as e:
                msg = str(e).lower()
                if not ("closed" in msg or "crashed" in msg) or tentativa == 3:
                    raise
                print(f"html: o navegador fechou em {op}; reabrindo e repetindo o quadro", flush=True)
                self._reabrir()

    def evaluate(self, expr, arg=None):
        if "__seek" in expr:
            self._ult = (expr, arg)
        return self._tentar("evaluate", expr, arg)

    def screenshot(self, **k):
        return self._tentar("screenshot", **k)

    def fechar(self):
        for fechar in (self.nav.close, self.srv.shutdown):
            try:
                fechar()
            except Exception:
                pass


def stills(comp: Path, tempos: list[float], pasta: Path) -> None:
    pasta.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        srv, nav, pg, meta = _abrir(p, comp)
        for t in tempos:
            pg.evaluate("t => window.__seek(t)", t)
            arq = pasta / f"t{t:06.2f}.png"
            pg.screenshot(path=str(arq), clip={"x": 0, "y": 0, "width": meta["largura"], "height": meta["altura"]})
            print(arq)
        nav.close()
        srv.shutdown()


# Ruído de rasterização do Chromium ao revisitar um instante (antialiasing de canto arredondado, transform de
# identidade, raster parcial): até 5 níveis por canal medidos no catálogo com 61 instantes. Estado escondido de verdade
# (objeto que some, quadro de vídeo errado) passa de 200.
TOLERANCIA = 24


def verificar(comp: Path, tempos: list[float]) -> bool:
    """Contrato "quadro = função pura do tempo": cada instante t renderizado depois de visitar outros
    tempos (e numa página recém-aberta) tem de dar os mesmos pixels, com folga de TOLERANCIA níveis por canal para o
    ruído de rasterização. Falha = estado escondido (animação CSS, relógio, aleatório sem semente, acúmulo entre
    quadros). O Chromium abre sem raster parcial, que é a maior fonte desse ruído."""
    import io

    from PIL import Image, ImageChops

    def foto(pg, meta, t):
        pg.evaluate("t => window.__seek(t)", t)
        return pg.screenshot(type="png", clip={"x": 0, "y": 0, "width": meta["largura"], "height": meta["altura"]})

    def diferenca(a: bytes, b: bytes) -> int:
        """Maior diferença de um canal de um pixel entre os dois quadros, de 0 a 255."""
        if a == b:
            return 0
        dif = ImageChops.difference(Image.open(io.BytesIO(a)).convert("RGB"), Image.open(io.BytesIO(b)).convert("RGB"))
        return max(hi for _, hi in dif.getextrema())

    ok = True
    args = ("--disable-partial-raster",)
    with sync_playwright() as p:
        srv, nav, pg, meta = _abrir(p, comp, args)
        primeira = {t: foto(pg, meta, t) for t in tempos}
        for t in reversed(tempos):          # revisita em outra ordem
            if (d := diferenca(foto(pg, meta, t), primeira[t])) > TOLERANCIA:
                print(f"NÃO determinístico em t={t}s (mesma página, ordem diferente; {d} níveis de diferença)")
                ok = False
        nav.close()
        srv.shutdown()
        srv, nav, pg, meta = _abrir(p, comp, args)   # página nova: isola estado de sessão
        for t in tempos:
            if (d := diferenca(foto(pg, meta, t), primeira[t])) > TOLERANCIA:
                print(f"NÃO determinístico em t={t}s (página nova; {d} níveis de diferença)")
                ok = False
        nav.close()
        srv.shutdown()
    print("determinismo: ok" if ok else "determinismo: FALHOU")
    return ok


def _fatias(n: int, paginas: int) -> list[tuple[int, int]]:
    """Divide os quadros [0, n) em até `paginas` fatias contíguas de quadros inteiros (tamanhos diferem em no máximo 1)."""
    base, resto = divmod(n, paginas)
    fatias, ini = [], 0
    for k in range(paginas):
        fim = ini + base + (k < resto)
        if fim > ini:
            fatias.append((ini, fim))
        ini = fim
    return fatias


def _codificar(pg, meta, arq: Path, i0: int, i1: int, *, de: float, sub: int, crf: int, rotulo: str = "") -> None:
    """Renderiza os quadros de saída [i0, i1) desta página num MP4. O tempo de cada sub-quadro depende só do
    índice global i, então quebrar em fatias não muda nenhum instante; a janela do tmix cobre os sub-quadros
    de um mesmo quadro de saída, e por isso a junção das fatias não mistura quadros vizinhos."""
    W, H, fps = meta["largura"], meta["altura"], meta["fps"]
    filtros = []
    if sub > 1:
        # Obturador de 180°: média dos sub-quadros da metade inicial de cada intervalo.
        filtros.append(f"tmix=frames={sub}:weights={' '.join(['1'] * sub)}")
        filtros.append(f"select='eq(mod(n\\,{sub})\\,{sub - 1})'")
    filtros.append(f"setpts=N/({fps}*TB)")
    ff = subprocess.Popen(
        ["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(fps * sub), "-c:v", "png", "-i", "-",
         "-vf", ",".join(filtros), "-r", str(fps), "-c:v", "libx264", "-preset", "slow", "-crf", str(crf),
         "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(arq)],
        stdin=subprocess.PIPE,
    )
    passo = max(1, (i1 - i0) // 10)
    for i in range(i0, i1):
        for k in range(sub):
            t = de + (i + (k / sub) * 0.5) / fps
            pg.evaluate("t => window.__seek(t)", t)
            ff.stdin.write(pg.screenshot(type="png", clip={"x": 0, "y": 0, "width": W, "height": H}))
        if (i - i0) % passo == 0:
            print(f"html{rotulo} {100 * (i - i0) // (i1 - i0)}%", flush=True)
    ff.stdin.close()
    ff.wait()
    if ff.returncode:
        raise SystemExit("ffmpeg falhou")


def renderizar(comp: Path, saida: Path, *, blur: int = 1, de: float = 0.0, ate: float | None = None, crf: int = 16,
               forcar: bool = False, paginas: int = 1) -> Path:
    from . import lint

    achados = lint.checar(comp)
    for n, m in achados:
        print(f"lint {n}: {m}")
    if any(n == "ERRO" for n, _ in achados) and not forcar:
        raise SystemExit("lint da composição falhou (o render sairia diferente a cada execução); corrija ou use --forcar")
    saida.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        srv, nav, pg, meta = _abrir(p, comp)
        eventos = pg.evaluate("window.__events ? window.__events() : null")
        if eventos:
            saida.with_suffix(".eventos.json").write_text(json.dumps(eventos, ensure_ascii=False))
        fim = ate if ate is not None else meta["duracao"]
        n = round((fim - de) * meta["fps"])
        sub = max(1, blur)
        saida.with_suffix(".render.json").write_text(json.dumps({"blur": sub, "fps": meta["fps"], "paginas": paginas}))
        fatias = _fatias(n, paginas)
        if len(fatias) <= 1:
            r = _Resiliente(p, comp, (srv, nav, pg, meta))
            try:
                _codificar(r, meta, saida, 0, n, de=de, sub=sub, crf=crf)
            finally:
                r.fechar()
        else:
            nav.close()
            srv.shutdown()
    if len(fatias) > 1:
        pasta = Path(tempfile.mkdtemp(prefix=".fatias-", dir=saida.parent))

        def uma(k, i0, i1):
            with sync_playwright() as pk:  # Playwright síncrono não atravessa threads: um por fatia
                r = _Resiliente(pk, comp, _abrir(pk, comp))
                try:
                    _codificar(r, meta, pasta / f"f{k}.mp4", i0, i1, de=de, sub=sub, crf=crf, rotulo=f"[{k}]")
                finally:
                    r.fechar()

        try:
            with ThreadPoolExecutor(len(fatias)) as ex:
                for f in [ex.submit(uma, k, i0, i1) for k, (i0, i1) in enumerate(fatias)]:
                    f.result()
            (pasta / "lista.txt").write_text("".join(f"file 'f{k}.mp4'\n" for k in range(len(fatias))))
            r = subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(pasta / "lista.txt"),
                                "-c", "copy", "-movflags", "+faststart", str(saida)])
            if r.returncode:
                raise SystemExit("ffmpeg falhou ao unir as fatias")
        finally:
            shutil.rmtree(pasta, ignore_errors=True)
    print(saida)
    return saida


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("composicao")
    ap.add_argument("--saida", help="MP4 de saída (ou pasta, com --stills)")
    ap.add_argument("--stills", help="tempos em segundos separados por vírgula: salva PNGs em vez de vídeo")
    ap.add_argument("--blur", type=int, default=1, help="sub-quadros por quadro (4–8 = motion blur)")
    ap.add_argument("--paginas", type=int, choices=[1, 2, 3, 4], default=1,
                    help="fatias de tempo renderizadas em paralelo (uma página e um FFmpeg por fatia); --verificar segue serial")
    ap.add_argument("--de", type=float, default=0.0)
    ap.add_argument("--ate", type=float)
    ap.add_argument("--verificar", help="tempos em segundos separados por vírgula: confere que cada quadro sai idêntico em renders repetidos")
    ap.add_argument("--forcar", action="store_true", help="renderiza mesmo com erro de lint")
    a = ap.parse_args(argv)
    if a.verificar:
        return 0 if verificar(Path(a.composicao), [float(x) for x in a.verificar.split(",")]) else 1
    if a.stills:
        return stills(Path(a.composicao), [float(x) for x in a.stills.split(",")], Path(a.saida or "output/stills"))
    renderizar(Path(a.composicao), Path(a.saida), blur=a.blur, de=a.de, ate=a.ate, forcar=a.forcar, paginas=a.paginas)


if __name__ == "__main__":
    raise SystemExit(main())
