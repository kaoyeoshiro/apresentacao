"""Ferramentas de mídia com arquivos sintéticos: tratamento nas cores do tema, preparo de vídeo e a conferência."""
import json
import shutil
import subprocess
from pathlib import Path

import numpy as np
import pytest
from PIL import Image

from ferramentas import midia, tratar

TINTA, DESTAQUE, FUNDO = (15, 38, 65), (212, 157, 56), (252, 249, 244)
FFMPEG = shutil.which("ffmpeg") and shutil.which("ffprobe")
sem_ffmpeg = pytest.mark.skipif(not FFMPEG, reason="ffmpeg/ffprobe não instalados")


@pytest.fixture
def deck(tmp_path) -> Path:
    tema = tmp_path / "temas" / "t" / "tema.css"
    tema.parent.mkdir(parents=True)
    tema.write_text(":root {\n  --cor-fundo: #FCF9F4;\n  --cor-tinta: #0F2641;\n  --cor-destaque: #D49D38;\n"
                    "  --cor-destaque-texto: color-mix(in srgb, var(--cor-destaque) 68%, var(--cor-tinta));\n}\n")
    d = tmp_path / "decks" / "x"
    d.mkdir(parents=True)
    (d / "deck.html").write_text('<link rel="stylesheet" href="../../temas/t/tema.css">\n')
    return d


def _perto(px, cor, tol=10):
    return all(abs(int(a) - b) <= tol for a, b in zip(px, cor))


def _ffmpeg(*args):
    subprocess.run(["ffmpeg", "-y", "-v", "error", *map(str, args)], check=True)


def _clipe(arq: Path, *codec, segundos=3):
    _ffmpeg("-f", "lavfi", "-i", "testsrc=size=320x240:rate=30", "-t", segundos, *codec, arq)
    return arq


# ---------- tratar ----------

def test_cores_do_tema(deck):
    assert tratar.cores_do_tema(deck) == {"tinta": TINTA, "destaque": DESTAQUE, "fundo": FUNDO}


def test_duotone_preto_vira_tinta_e_branco_vira_fundo(deck, tmp_path):
    a = np.zeros((64, 128, 3), np.uint8)
    a[:, 64:] = 255
    src = tmp_path / "foto.png"
    Image.fromarray(a).save(src)
    out = tratar.tratar(str(deck), str(src), intensidade=1, grao=0)
    assert out == deck / "midia" / "foto.webp"
    im = Image.open(out).convert("RGB")
    assert _perto(im.getpixel((20, 32)), TINTA) and _perto(im.getpixel((108, 32)), FUNDO)
    assert (deck / "midia" / "originais" / "foto.png").is_file()
    cred = {i["arquivo"]: i for i in json.loads((deck / "midia" / "creditos.json").read_text())}["midia/foto.webp"]
    assert cred["original"] == "midia/originais/foto.png" and cred["tratamento"]["tom"] == "duotone"


def test_tritone_poe_o_destaque_no_meio_e_grao_tem_semente(deck, tmp_path):
    a = np.tile(np.linspace(0, 255, 256, dtype=np.uint8), (32, 1))
    src = tmp_path / "rampa.png"
    Image.fromarray(np.stack([a] * 3, axis=-1)).save(src)
    out = tratar.tratar(str(deck), str(src), tom="tritone", intensidade=1, grao=0, largura=256)
    assert _perto(Image.open(out).convert("RGB").getpixel((128, 16)), DESTAQUE, tol=14)
    rgb = np.full((8, 8, 3), 128.0)
    um = tratar.mapear(rgb, tratar.cores_do_tema(deck), semente=7)
    assert np.array_equal(um, tratar.mapear(rgb, tratar.cores_do_tema(deck), semente=7))
    assert not np.array_equal(um, tratar.mapear(rgb, tratar.cores_do_tema(deck), semente=8))


def test_alfa_canto_transparente_centro_opaco(deck, tmp_path):
    a = np.full((96, 96, 3), (238, 234, 226), np.uint8)
    a[30:66, 30:66] = (60, 40, 30)
    a[42:54, 42:54] = (238, 234, 226)  # miolo da cor do fundo, cercado pelo objeto
    src = tmp_path / "objeto.png"
    Image.fromarray(a).save(src)
    out = tratar.tratar(str(deck), str(src), alfa=True, saida="pasta")
    assert out.name == "pasta.webp"
    alfa = Image.open(out).getchannel("A")
    assert alfa.getpixel((2, 2)) == 0 and alfa.getpixel((34, 34)) == 255
    assert alfa.getpixel((48, 48)) == 255  # o miolo não vira buraco
    assert 0 < alfa.getpixel((29, 48)) < 255  # borda suave


def test_alfa_acompanha_fundo_em_degrade_e_poupa_papel_claro(deck, tmp_path):
    # luz de janela: o fundo vai de #F7F1EB a #DDD3CB; o papel fica a uns 20 níveis do fundo, sem contorno
    y, x = np.mgrid[0:120, 0:160]
    t = ((x / 159 + y / 119) / 2)[..., None]
    a = (np.array([247, 241, 235]) * (1 - t) + np.array([221, 211, 203]) * t)
    a += np.random.default_rng(1).normal(0, 1.2, a.shape)
    a[30:90, 50:110] = (246, 246, 248)
    src = tmp_path / "papel.png"
    Image.fromarray(np.clip(a, 0, 255).round().astype(np.uint8)).save(src)
    out = tratar.tratar(str(deck), str(src), alfa=True, grao=0)
    alfa = np.asarray(Image.open(out).getchannel("A"))
    assert alfa[2, 2] == 0 and alfa[117, 157] == 0 and alfa[:20].max() < 30  # os dois lados do degradê somem
    assert alfa[34:86, 54:106].min() == 255  # o papel não é comido nem fica translúcido (fora a borda suave)
    cred = {i["arquivo"]: i for i in json.loads((deck / "midia" / "creditos.json").read_text())}["midia/papel.webp"]
    assert len(cred["tratamento"]["limiar"]) == 2


def test_niveis_claro_fundo_e_gama(deck):
    cores = tratar.cores_do_tema(deck)
    cinza = np.full((4, 4, 3), 128.0)
    cinza[0, 0] = 200
    kw = dict(intensidade=1, grao=0)
    # claro: o escuro não é esticado, então o cinza médio fica longe da tinta
    assert tratar.mapear(cinza, cores, lo=0, **kw)[1, 1].mean() > 100
    # fundo: o que tem a luminância do fundo da foto vira --cor-fundo
    assert _perto(tratar.mapear(cinza, cores, lo=0, hi=128 / 255, **kw)[1, 1], FUNDO, tol=2)
    # gama acima de 1 escurece os meios-tons
    assert tratar.mapear(cinza, cores, lo=0, hi=1, gama=2, **kw)[1, 1].mean() < \
        tratar.mapear(cinza, cores, lo=0, hi=1, **kw)[1, 1].mean()


# ---------- vídeo ----------

@sem_ffmpeg
def test_preparar_gera_h264_faststart_e_quadros_chave_curtos(deck, tmp_path):
    src = _clipe(tmp_path / "bruto.mov", "-c:v", "libx264", "-g", "300", "-pix_fmt", "yuv420p")
    out = midia.trazer(str(deck), str(src), origem="teste sintético", ate=2, capa=1)
    assert out == deck / "midia" / "bruto.mp4"
    info = json.loads(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                                      "stream=codec_name,profile,pix_fmt:format=duration", "-of", "json", str(out)],
                                     capture_output=True, text=True, check=True).stdout)
    st = info["streams"][0]
    assert (st["codec_name"], st["profile"], st["pix_fmt"]) == ("h264", "High", "yuv420p")
    assert float(info["format"]["duration"]) == pytest.approx(2, abs=0.1)
    assert not midia._moov_no_fim(out)
    assert midia.checar_video(out) == []
    assert (deck / "midia" / "bruto-capa.webp").is_file() and (deck / "midia" / "originais" / "bruto.mov").is_file()
    cred = {i["arquivo"]: i for i in json.loads((deck / "midia" / "creditos.json").read_text())}
    assert cred["midia/bruto.mp4"]["original"] == "midia/originais/bruto.mov"


@sem_ffmpeg
def test_conferir_avisa_quadro_chave_longo_e_moov_no_fim(deck, capsys):
    (deck / "midia").mkdir()
    _clipe(deck / "midia" / "longo.mp4", "-c:v", "libx264", "-g", "300", "-pix_fmt", "yuv420p")
    assert midia.conferir(str(deck)) == 0
    saida = capsys.readouterr().out
    assert "quadro-chave a cada 3.0 s" in saida and "moov" in saida


def _tem_encoder(nome):
    return FFMPEG and nome in subprocess.run(["ffmpeg", "-hide_banner", "-encoders"], capture_output=True,
                                             text=True).stdout


@sem_ffmpeg
@pytest.mark.parametrize("codec, pix, esperado", [("libx265", "yuv420p", "HEVC"), ("libx264", "yuv422p", "4:2:2"),
                                                  ("libx264", "yuv420p10le", "8 bits")])
def test_conferir_acusa_o_que_o_chromium_nao_toca(deck, codec, pix, esperado, capsys):
    if not _tem_encoder(codec):
        pytest.skip(f"este ffmpeg não tem o encoder {codec}")
    (deck / "midia").mkdir()
    try:
        _clipe(deck / "midia" / "ruim.mp4", "-c:v", codec, "-pix_fmt", pix, segundos=1)
    except subprocess.CalledProcessError:
        pytest.skip(f"{codec} deste ffmpeg não grava {pix}")
    assert midia.conferir(str(deck)) == 1
    assert any(esperado in l and l.startswith("ERRO") for l in capsys.readouterr().out.splitlines())


@sem_ffmpeg
def test_conferir_avisa_av1_sem_erro(deck, capsys):
    """AV1 toca no Chromium do render; o aviso é de desempenho no notebook do palco."""
    if not _tem_encoder("libsvtav1"):
        pytest.skip("este ffmpeg não tem o encoder libsvtav1")
    (deck / "midia").mkdir()
    _clipe(deck / "midia" / "av1.mp4", "-c:v", "libsvtav1", "-pix_fmt", "yuv420p", "-g", "15", "-movflags",
           "+faststart", segundos=1)
    assert midia.conferir(str(deck)) == 0
    assert any(l.startswith("AVISO") and "AV1" in l for l in capsys.readouterr().out.splitlines())


@sem_ffmpeg
def test_conferir_avisa_largura_acima_do_perfil_do_credito(deck, capsys):
    (deck / "midia").mkdir()
    for nome in ("largo.mp4", "solto.mp4"):
        _ffmpeg("-f", "lavfi", "-i", "testsrc=size=2048x64:rate=30", "-t", 1, "-c:v", "libx264", "-g", "15",
                "-pix_fmt", "yuv420p", "-movflags", "+faststart", deck / "midia" / nome)
    midia.creditar(deck, deck / "midia" / "largo.mp4", ferramenta="trazido", preparo={"perfil": "tela"})
    assert midia.conferir(str(deck)) == 0
    linhas = capsys.readouterr().out.splitlines()
    assert any(l.startswith("AVISO largo.mp4") and "perfil tela (1920 px)" in l for l in linhas)
    assert not any("solto.mp4" in l for l in linhas)   # sem crédito vale o demo, 2560 px
