"""Abertura automática, linha do dia e guia do apresentador (motor/palco.js, contrato em docs/palco.md), no deck de
tests/fixtures/palco_guia: capa sem a linha, bloco "um" com dois slides (o segundo herda), bloco "dois" com a prática
de 1 minuto e notas estruturadas, e o bloco "tres", sem slide neste deck. Paradas: 0 (t 0), 1 (capa, t 1), 2 e 3 (a,
t 2 e 3), 4 (b, t 4), 5 (c, t 5)."""
from pathlib import Path

import pytest

from ferramentas import config, palco
from ferramentas import render as html

GUIA = Path(__file__).parent / "fixtures" / "palco_guia" / "deck.html"
URL = GUIA.resolve().relative_to(config.RAIZ).as_posix()
RELOGIO = "window.__relogio = 0; performance.now = () => window.__relogio;"


def _pagina(f):
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        srv, nav, pg, _ = html._abrir(p, GUIA)
        try:
            return f(pg)
        finally:
            nav.close()
            srv.shutdown()


def test_blocos_ritmo_e_relogio_puros():
    r = _pagina(lambda pg: pg.evaluate("""async () => {
        const P = await import('/motor/palco.js');
        const slides = [{id: 'capa', passos: [1]}, {id: 'a', bloco: 'um', passos: [1, 1]}, {id: 'b', passos: [1]},
                        {id: 'c', bloco: 'dois', passos: [1]}];
        const blocos = [{id: 'um', rotulo: 'Um', minutos: 5}, {id: 'dois', rotulo: 'Dois', minutos: 3}, {id: 'tres', rotulo: 'Três'}];
        const d = P.planejarDia(P.planejar(slides), blocos);
        const um = d.blocos[0];
        return {
            porSlide: d.porSlide, erros: d.erros, tempos: d.blocos.map((b) => [b.t0, b.t1]), paradas: d.blocos.map((b) => b.paradas),
            fracao: [1, 2, 3, 4].map((n) => P.fracaoDoBloco(um, n)),
            ritmo: [[200, 5, 0.5], [100, 5, 0.5], [160, 5, 0.5], [10, null, 0]].map((a) => P.ritmoDoBloco(...a)),
            relogio: [P.relogio(75), P.relogio(-12), P.relogio(3599.9)],
            ruins: P.planejarDia(P.planejar([{id: 'x', bloco: 'nao-ha', passos: [1]}]), [{id: 'um'}, {id: 'dois', rotulo: 'D', minutos: 0}]).erros,
        };
    }"""))
    assert r["porSlide"] == [-1, 0, 0, 1] and r["erros"] == []      # "b" herda o bloco de "a"
    assert r["tempos"] == [[1, 4], [4, 5], [None, None]]
    assert r["paradas"] == [[2, 3, 4], [5], []]
    assert r["fracao"] == pytest.approx([0, 0, 1 / 3, 2 / 3])        # chegar à primeira parada do bloco é o começo dele
    assert [x["estado"] for x in r["ritmo"]] == ["atrasado", "adiantado", "no tempo", ""]
    assert r["ritmo"][0]["saldo"] == pytest.approx(50) and r["ritmo"][1]["saldo"] == pytest.approx(-50)
    assert r["relogio"] == ["01:15", "-00:12", "59:59"]
    assert r["ruins"] == ['bloco 1 sem id ou rótulo', 'bloco "dois": minutos 0 inválidos', 'slide "x": bloco "nao-ha" não existe']


def test_linha_do_dia_e_funcao_do_tempo_e_aparece_no_render():
    def medir(pg):
        estado = """(() => { const l = document.getElementById('linha-dia'), cs = getComputedStyle(l);
            return {vis: cs.visibility, op: Number(cs.opacity), atual: [...l.children].findIndex((b) => b.classList.contains('atual')),
                rotulos: [...l.querySelectorAll('.ld-rot')].map((r) => r.textContent),
                cheio: [...l.querySelectorAll('.ld-trilho b')].map((b) => b.style.transform)}; })()"""
        r = {}
        for t in (1.0, 1.2, 2.0, 5.0):
            pg.evaluate("t => __palco.ver(t)", t)
            r[t] = pg.evaluate(estado)
        pg.evaluate("__palco.ir(2)")
        r["blocos"] = [b for b in pg.evaluate("__palco.medir()") if b["caminho"].startswith("#linha-dia")]
        return r

    r = _pagina(medir)
    assert r[1.0]["vis"] == "hidden"                                   # capa com linhaDia: false
    assert 0 < r[1.2]["op"] < 1                                        # entra com o slide, pelo tempo
    a = r[2.0]
    assert a["vis"] == "visible" and a["op"] == 1 and a["atual"] == 0
    assert a["rotulos"] == ["Primeiro bloco", "Segundo bloco", "Terceiro bloco"]
    assert a["cheio"] == ["scaleX(0.3333)", "scaleX(0)", "scaleX(0)"]   # (2 - 1) / (4 - 1) do bloco um
    assert r[5.0]["atual"] == 1 and r[5.0]["cheio"] == ["scaleX(1)", "scaleX(1)", "scaleX(0)"]
    b = r["blocos"]
    assert len(b) == 3 and all(x["sinalizacao"] for x in b)
    assert all(x["fonte"] >= 29.5 and 988 <= x["y"] and x["y"] + x["h"] <= 1037 and x["x"] >= 120 for x in b), b


def test_oraculo_nao_conta_a_sinalizacao_como_conteudo():
    linha = {"texto": "Primeiro bloco", "palavras": 60, "fonte": 30, "x": 200, "y": 1000, "w": 300, "h": 36, "cor": [0, 0, 0],
             "alfa": 1, "transborda": False, "id": "", "caminho": "#linha-dia > div:1 > span:1", "sinalizacao": True}
    assert palco.checar_parada([linha]) == []                          # 60 palavras de sinalização não pesam o slide
    assert palco.checar_hierarquia([linha, {**linha, "fonte": 300, "sinalizacao": False}, linha, linha]) == []


def test_deck_com_linha_do_dia_passa_no_oraculo():
    assert palco.sondar(GUIA, determinismo=True) == 0


def _vivo(p, srv, hash_=""):
    nav = p.chromium.launch()
    ctx = nav.new_context(viewport={"width": 1280, "height": 720})
    ctx.add_init_script(RELOGIO)
    pg = ctx.new_page()
    pg.goto(f"http://127.0.0.1:{srv.server_address[1]}/{URL}?vivo{hash_}")
    pg.wait_for_function("!!document.getElementById('palco-aviso')")
    pg.evaluate("document.fonts.ready")
    return nav, pg


def _quadros(pg):
    pg.evaluate("() => new Promise((r) => { let n = 0; const f = () => (++n > 10 ? r() : requestAnimationFrame(f)); f(); })")


def test_abertura_automatica_toca_a_primeira_parada_sozinha():
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        srv = html._servir(GUIA)
        nav, pg = _vivo(p, srv)
        _quadros(pg)
        pg.evaluate("window.__relogio = 1500")
        pg.wait_for_function("location.hash === '#parada=1'", timeout=15000)
        _quadros(pg)
        sozinha = pg.evaluate("location.hash")
        nav.close()
        # recarregar no meio da aula não toca nada: a abertura só vale na parada 0
        nav, pg = _vivo(p, srv, "#parada=3")
        _quadros(pg)
        pg.evaluate("window.__relogio = 5000")
        _quadros(pg)
        meio = pg.evaluate("location.hash")
        nav.close()
        srv.shutdown()
    assert sozinha == "#parada=1"                                      # não seguiu para a parada 2 sem clique
    assert meio == "#parada=3"


def test_tela_do_apresentador_mostra_bloco_proxima_guia_e_pratica(tmp_path):
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        srv = html._servir(GUIA)
        nav, pg = _vivo(p, srv, "#parada=4")
        with pg.expect_popup() as janela:
            pg.keyboard.press("p")
        ap = janela.value
        ap.wait_for_load_state()
        ap.wait_for_function("document.getElementById('ap-bloco').textContent.includes('Primeiro bloco')", timeout=15000)
        texto = lambda sel: ap.evaluate("s => document.querySelector(s).textContent", sel)
        em_b = {s: texto(s) for s in ("#ap-bloco", "#ap-prox-titulo")}
        ap.keyboard.press("ArrowRight")                                # avança o palco pela tela do apresentador
        _quadros(pg)                                                   # a mensagem chega antes de o relógio andar
        pg.evaluate("window.__relogio = 2000")
        pg.wait_for_function("location.hash === '#parada=5'", timeout=15000)
        ap.wait_for_function("document.getElementById('ap-pratica').textContent === '01:00'", timeout=15000)
        em_c = {s: texto(s) for s in ("#ap-bloco", "#ap-guia", "#ap-prox-titulo")}
        ap.evaluate("window.__relogio += 30000")
        pg.evaluate("window.__relogio += 30000")
        ap.wait_for_function("document.getElementById('ap-pratica').textContent === '00:30'", timeout=15000)
        _quadros(pg)
        na_tela = pg.evaluate("document.getElementById('palco-pratica').textContent")
        ap.screenshot(path=str(tmp_path / "apresentador.png"))
        nav.close()
        srv.shutdown()
    assert "Primeiro bloco" in em_b["#ap-bloco"] and "1 de 3" in em_b["#ap-bloco"] and "de 05:00" in em_b["#ap-bloco"]
    assert "Prática do pedido" in em_b["#ap-prox-titulo"] and "Segundo bloco" in em_b["#ap-prox-titulo"]
    assert "Segundo bloco" in em_c["#ap-bloco"] and "2 de 3" in em_c["#ap-bloco"]
    for trecho in ("Agora é com vocês.", "abrir o app", "pedir mão levantada", "Quem terminou mostra."):
        assert trecho in em_c["#ap-guia"], trecho
    assert "fim" in em_c["#ap-prox-titulo"]
    assert na_tela == "00:30"
