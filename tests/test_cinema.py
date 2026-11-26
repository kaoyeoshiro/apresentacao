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



def _no_navegador(js: str):
    """Roda `js` (corpo de função async) numa página do molde, com motor/cinema.js importável."""
    from playwright.sync_api import sync_playwright

    from ferramentas import render as html

    with sync_playwright() as p:
        srv, nav, pg, _ = html._abrir(p, MOLDE)
        try:
            return pg.evaluate(f"async () => {{ {js} }}")
        finally:
            nav.close()
            srv.shutdown()


def test_trajeto_cor_do_tema_e_brilho_nao_dependem_do_quadro_anterior():
    """Revisão de 26/11/2026: pose sem fov herdava o fov do quadro anterior; token inexistente virava preto calado;
    cor fora do sRGB era lida errada; brilho parcial punha NaN no bloom e apagava a cena."""
    r = _no_navegador("""
        const M = await import('/motor/cinema.js');
        const cam = new M.THREE.PerspectiveCamera(50, 16 / 9, 0.1, 100);
        const posar = M.trajeto([{pos: [0, 0, 5], alvo: [0, 0, 0]}, {pos: [0, 0, 6], alvo: [0, 0, 0], fov: 60}]);
        const fov = (u) => { posar(cam, u); return cam.fov; };
        const ida = [fov(0), fov(0.5), fov(0.5)], volta = [fov(1), fov(0.5), fov(0)];
        let semToken = null;
        try { M.corDoTema('--nao-existe'); } catch (e) { semToken = e.message; }
        const raiz = document.documentElement.style;
        raiz.setProperty('--t-oklch', 'oklch(0.7 0.15 70)');
        raiz.setProperty('--t-p3', 'color(display-p3 0.2 0.4 0.6)');
        const cores = ['--t-oklch', '--t-p3'].map((t) => M.corDoTema(t).getHexString());
        const C = M.cinema({palco: document.createElement('div'), brilho: {forca: 0.5}});
        return {ida, volta, semToken, cores, raio: C.bloom.radius, limiar: C.bloom.threshold};
    """)
    assert r["ida"] == [35, 47.5, 47.5] and r["volta"] == [60, 47.5, 35], r
    assert r["semToken"] and "--nao-existe" in r["semToken"]
    for h in r["cores"]:                              # sRGB de verdade: nenhum canal estourado nem zerado por parsing
        assert len(h) == 6 and h not in ("000000", "ffffff"), r["cores"]
    assert r["raio"] == 0.55 and r["limiar"] == 0.8


def test_isencao_de_ritmo_exige_a_cena_3d_visivel(capsys):
    """Com o canvas escondido, a viagem longa não tem o que a sala assistir: o aviso de ritmo volta."""
    slug = "_teste-cinema-escondido"
    shutil.rmtree(config.DECKS / slug, ignore_errors=True)
    deck = palco.novo(slug, "cojuris", modo="cinema") / "deck.html"
    try:
        doc = deck.read_text(encoding="utf-8")
        deck.write_text(doc.replace("</style>", "  #cinema { display: none; }\n</style>", 1), encoding="utf-8")
        palco.sondar(deck, determinismo=False)
        saida = capsys.readouterr().out
        assert "ISENTO ritmo" not in saida and "AVISO ritmo" in saida, saida
    finally:
        shutil.rmtree(deck.parent, ignore_errors=True)


def test_three_leva_a_licenca_mit_no_proprio_codigo():
    """O pacote embute os módulos e não copia o LICENSE: o aviso MIT precisa estar dentro do código copiado."""
    for nome in ("three.module.js", "three.core.js"):
        topo = (config.MOTOR / "vendor" / "three" / nome).read_text(encoding="utf-8")[:2000]
        assert "Permission is hereby granted" in topo, nome
