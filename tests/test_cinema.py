"""Estilo cinema (motor/cinema.js, contrato em docs/cinema.md): o molde passa no oráculo com o tema dele e com outro, e
a cena 3D sai de fato no still (WebGL no Chromium headless), que é de onde vêm o PDF, o vídeo e a revisão."""
import io
import shutil

from PIL import Image, ImageStat

from ferramentas import config, palco

MOLDE = config.CINEMA / "deck.html"


def test_molde_cinema_passa_no_oraculo():
    assert palco.sondar(MOLDE) == 0


def test_molde_cinema_passa_com_outro_tema():
    """As cores da cena saem de corDoTema; trocar o tema troca a cena sem quebrar legibilidade. O molde pede tema de
    fundo claro e tinta escura, porque a noite da cena é a tinta escurecida (docs/cinema.md, Regras)."""
    slug = "_teste-cinema-pge"
    shutil.rmtree(config.DECKS / slug, ignore_errors=True)
    deck = palco.novo(slug, "pge", modo="cinema") / "deck.html"
    try:
        assert palco.sondar(deck, determinismo=False) == 0
    finally:
        shutil.rmtree(deck.parent, ignore_errors=True)


def test_cena_3d_aparece_no_still():
    """Sem WebGL no renderizador, o canvas sairia vazio e o oráculo mediria só o texto sobre o fundo liso. Na parada
    do circuito a coluna e a rede acesas põem dourado no quadro; no fecho, o dia clareia a cena inteira."""
    d = palco._abrir(MOLDE)
    try:
        assert d.pg.evaluate("!!document.querySelector('#palco > canvas#cinema')")
        n = {p["id"]: p["n"] for p in d.info["paradas"]}
        circuito = Image.open(io.BytesIO(d.foto(n["circuito"]))).convert("RGB")
        fecho = Image.open(io.BytesIO(d.foto(n["fecho"]))).convert("L")
    finally:
        palco._fechar(d)
    # metade direita, onde está a coluna: dourado é vermelho bem acima do azul
    direita = circuito.crop((960, 0, 1920, 1080)).resize((240, 270))
    dourados = sum(1 for r, g, b in direita.get_flattened_data() if r > 150 and r - b > 80)
    assert dourados > 200, f"só {dourados} pixels dourados: a cena 3D não renderizou"
    assert ImageStat.Stat(fecho).mean[0] > 180, "o fecho deveria terminar no claro da marca"

