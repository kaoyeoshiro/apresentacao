"""Motor de palco: regras do oráculo, linha do tempo do tocador, a demonstração que passa, o deck ruim que reprova e o
pacote que abre por file:// sem rede."""
import json
import re
import shutil
from pathlib import Path

import pytest

from ferramentas import config, lint, midia, palco
from ferramentas import render as html

DEMO = config.DEMO / "deck.html"
RUIM = Path(__file__).parent / "fixtures" / "palco_ruim" / "deck.html"


def _bloco(**m):
    b = {"texto": "Título", "palavras": 1, "fonte": 60, "x": 200, "y": 200, "w": 400, "h": 70, "cor": [242, 239, 233],
         "alfa": 1, "transborda": False, "id": "", "caminho": "[s] > p"}
    b.update(m)
    return b


def _niveis(achados, nivel):
    return [m for n, m in achados if n == nivel]


# ---------- regras puras ----------

def test_bloco_bom_passa():
    assert palco.checar_parada([_bloco()]) == []


def test_texto_pequeno_e_borda():
    assert any("ilegível" in m for m in _niveis(palco.checar_parada([_bloco(fonte=18)]), "ERRO"))
    assert any("pequeno" in m for m in _niveis(palco.checar_parada([_bloco(fonte=27)]), "AVISO"))
    assert any("cortado" in m for m in _niveis(palco.checar_parada([_bloco(x=1700, w=400)]), "ERRO"))
    assert any("margem" in m for m in _niveis(palco.checar_parada([_bloco(x=40)]), "AVISO"))
    assert any("transborda" in m for m in _niveis(palco.checar_parada([_bloco(transborda=True)]), "ERRO"))
    assert any("transparente" in m for m in _niveis(palco.checar_parada([_bloco(alfa=0.5)]), "AVISO"))


def test_sobreposicao_ignora_pai_e_filho():
    a, b = _bloco(caminho="[s] > div:1"), _bloco(caminho="[s] > div:1 > span:1", x=220)
    assert palco.checar_parada([a, b]) == []
    c = _bloco(caminho="[s] > div:10", x=220)
    assert any("sobrepõem" in m for m in _niveis(palco.checar_parada([a, c]), "AVISO"))


def test_palavras_demais():
    assert any("pesado" in m for m in _niveis(palco.checar_parada([_bloco(palavras=50)]), "AVISO"))
    assert any("cheio" in m for m in _niveis(palco.checar_parada([_bloco(palavras=80)]), "ERRO"))


def test_contraste_wcag():
    assert palco.contraste((255, 255, 255), (0, 0, 0)) == pytest.approx(21)
    assert palco.contraste((119, 119, 119), (255, 255, 255)) == pytest.approx(4.48, abs=0.02)


def test_assentado():
    assert palco.checar_assentado([_bloco()], [_bloco(x=201)]) == []
    assert any("em movimento" in m for _, m in palco.checar_assentado([_bloco(y=230)], [_bloco()]))


def test_finais_e_ritmo():
    paradas = [{"n": 0, "slide": 0, "passo": -1}, {"n": 1, "slide": 0, "passo": 0}, {"n": 2, "slide": 0, "passo": 1},
               {"n": 3, "slide": 1, "passo": 0}]
    assert palco.finais(paradas) == [2, 3]
    assert palco.checar_ritmo([{"id": "a", "passos": [1, 2]}]) == []
    assert any("plateia esperando" in m for _, m in palco.checar_ritmo([{"id": "a", "passos": [5]}]))


# ---------- navegador ----------

def test_demo_passa_no_lint():
    assert [m for n, m in lint.checar(DEMO)] == []


def test_linha_do_tempo_e_linha_de_video():
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        srv, nav, pg, meta = html._abrir(p, DEMO)
        info = pg.evaluate("({paradas: __palco.paradas, slides: __palco.slides, linha: __palco.linha})")
        nav.close()
        srv.shutdown()
    passos = [d for s in info["slides"] for d in s["passos"]]
    assert len(info["paradas"]) == 1 + len(passos)
    assert info["paradas"][-1]["t"] == pytest.approx(sum(passos))
    repousos = [tr for tr in info["linha"] if tr["parada"] is not None]
    assert len(repousos) == len(info["paradas"])
    assert all(tr["t0"] == tr["t1"] for tr in repousos)           # nos repousos o tempo do deck não anda
    assert meta["duracao"] == pytest.approx(info["linha"][-1]["T1"])
    k = [p["id"] for p in info["paradas"]].index("video")
    assert repousos[k]["T1"] - repousos[k]["T0"] == pytest.approx(6)     # o `segura` do próprio slide


def test_demo_passa_no_oraculo():
    assert palco.sondar(DEMO, determinismo=True) == 0


def test_deck_ruim_reprova(capsys):
    assert palco.sondar(RUIM, determinismo=False) == 1
    saida = capsys.readouterr().out
    for esperado in ("ilegível", "cortado pela borda", "transborda a própria caixa", "contraste estimado", "slide cheio",
                     "plateia esperando"):
        assert esperado in saida, esperado


def test_pacote_abre_sem_rede(tmp_path):
    arq = palco.empacotar(RUIM, tmp_path / "pacote", com_pdf=False)
    doc = arq.read_text()
    assert '<script type="importmap">' in doc and "../../../motor/" not in doc
    assert palco.conferir_pacote(arq) == []


def test_pdf_tem_uma_pagina_por_slide(tmp_path):
    arq = palco.pdf(RUIM, tmp_path / "x.pdf")
    assert len(re.findall(rb"/Type\s*/Page\b", arq.read_bytes())) == 2


def test_pacote_nao_leva_arquivo_fora_da_pasta(tmp_path):
    pasta = tmp_path / "deck"
    (pasta / "cache").mkdir(parents=True)
    (tmp_path / "segredo.txt").write_text("chave")
    (pasta / "cache" / "real.png").write_bytes(b"x")
    (pasta / "ok.png").write_bytes(b"x")
    doc = '<img src="../segredo.txt"><img src="cache/real.png"><img src="ok.png"><img src="/etc/hosts">'
    novo, copiados = palco._arquivos(doc, pasta / "deck.html", tmp_path / "pacote")
    assert copiados == ["ok.png"]
    assert not (tmp_path / "pacote" / "arquivos").exists()


def test_modo_mundo_move_a_camera():
    from playwright.sync_api import sync_playwright

    deck = Path(__file__).parent / "fixtures" / "palco_mundo" / "deck.html"
    with sync_playwright() as p:
        srv, nav, pg, _ = html._abrir(p, deck)
        caixas = pg.evaluate("[...document.querySelectorAll('[data-slide]')].map((s) => [s.offsetLeft, s.offsetTop])")
        rotulos = []
        for n in (1, 2):
            pg.evaluate("n => __palco.ir(n)", n)
            rotulos.append(pg.evaluate("document.querySelector('[data-slide=b] h1').getBoundingClientRect().left"))
        nav.close()
        srv.shutdown()
    assert caixas == [[0, 0], [2400, 1400]]                  # a posição dada pelo deck vence o CSS do tocador
    assert rotulos[1] == pytest.approx(160, abs=1)           # na parada do slide b, a câmera enquadra b
    assert rotulos[0] > 1920                                 # antes, b estava fora do quadro


def test_viagem_curta_chega_antes_do_fim_do_passo_e_recua_no_meio():
    from playwright.sync_api import sync_playwright

    deck = Path(__file__).parent / "fixtures" / "palco_viagem" / "deck.html"
    with sync_playwright() as p:
        srv, nav, pg, _ = html._abrir(p, deck)
        medidas = []
        for t in (0.85, 1.1, 2.6):                            # meio da viagem, fim da viagem, parada de b
            pg.evaluate("t => __palco.ver(t)", t)
            medidas.append(pg.evaluate("(() => { const r = document.querySelector('[data-slide=b] h1').getBoundingClientRect(); return [r.left, r.width]; })()"))
        nav.close()
        srv.shutdown()
    assert medidas[1][0] == pytest.approx(160, abs=1)        # com viagem de 0,5 s, a câmera já enquadra b em t = 1,1
    assert medidas[1] == pytest.approx(medidas[2], abs=0.5)  # e fica parada até o fim do passo
    assert medidas[0][1] < medidas[1][1] * 0.8               # no meio da viagem, o recuo afasta a câmera


def test_video_que_nao_abre_falha_sem_pendurar():
    deck = Path(__file__).parent / "fixtures" / "palco_sem_video" / "deck.html"
    with pytest.raises(Exception, match="vídeo não abriu"):
        palco.fotografar(deck)


@pytest.mark.parametrize("tema", ["cojuris", "pge"])
def test_demo_com_tema_de_marca_passa_no_oraculo(tema, tmp_path):
    """O deck só usa tokens do contrato: trocar o tema não pode quebrar legibilidade nem contraste, e o pacote leva
    o logo e as fontes do tema."""
    slug = f"_teste-{tema}"
    pasta = palco.novo(slug, tema)
    try:
        doc = (pasta / "deck.html").read_text()
        assert f"../../temas/{tema}/tema.css" in doc and "temas/noite" not in doc
        assert palco.sondar(pasta / "deck.html", determinismo=False) == 0
        arq = palco.empacotar(pasta / "deck.html", tmp_path / "pacote", com_pdf=False)
        levados = {p.relative_to(arq.parent).as_posix() for p in arq.parent.rglob("*") if p.is_file()}
        assert any(p.startswith(f"_repo/temas/{tema}/marca/") for p in levados), levados
        assert any(p.startswith(f"_repo/temas/{tema}/fonts/") for p in levados), levados
        assert palco.conferir_pacote(arq) == []
    finally:
        shutil.rmtree(pasta)


def test_novo_recusa_tema_que_nao_existe():
    with pytest.raises(SystemExit, match="não existe"):
        palco.novo("_teste-inexistente", "nao-ha")
    assert not (config.DECKS / "_teste-inexistente").exists()


def test_creditar_substitui_a_entrada_do_mesmo_arquivo(tmp_path):
    (tmp_path / "midia").mkdir()
    arq = tmp_path / "midia" / "a.png"
    arq.write_bytes(b"x")
    midia.creditar(tmp_path, arq, ferramenta="um", prompt="p1")
    midia.creditar(tmp_path, arq, ferramenta="dois", custo_usd=None)
    itens = json.loads((tmp_path / "midia" / "creditos.json").read_text())
    assert len(itens) == 1 and itens[0]["arquivo"] == "midia/a.png" and itens[0]["ferramenta"] == "dois"
    assert "custo_usd" not in itens[0] and "prompt" not in itens[0]


def test_video_ia_sem_aprovacao_so_orca(tmp_path, monkeypatch):
    """Sem --aprovado, a ponte só pede o orçamento ao ./cvm veo e não copia nem credita nada."""
    deck = tmp_path / "d"
    deck.mkdir()
    (deck / "deck.html").write_text("<!doctype html>")
    vm = tmp_path / "vm"
    vm.mkdir()
    (vm / "cvm").write_text("")
    monkeypatch.setenv("CVM_PROJETO", str(vm))
    chamadas = []
    monkeypatch.setattr(midia, "cvm", lambda *a: chamadas.append(a) or 0)
    assert midia.video_ia(str(deck), "onda", "mar calmo") is None
    assert chamadas and chamadas[0][0] == "veo" and "--aprovado" not in chamadas[0]
    saida = chamadas[0][chamadas[0].index("--saida") + 1]
    assert Path(saida) == vm.resolve() / "videos" / "ap-d" / "public" / "clipes" / "onda.mp4"
    assert not (deck / "midia").exists()


def test_empacotar_nao_apaga_pasta_que_nao_e_pacote(tmp_path):
    (tmp_path / "importante.txt").write_text("x")
    with pytest.raises(SystemExit, match="não é um pacote"):
        palco.empacotar(RUIM, tmp_path, com_pdf=False)
    assert (tmp_path / "importante.txt").exists()


def test_ponte_nao_passa_o_ambiente_python_daqui(tmp_path, monkeypatch):
    vm = tmp_path / "vm"
    vm.mkdir()
    (vm / "cvm").write_text('echo "UV=${UV_PROJECT_ENVIRONMENT:-vazio}" > "$(dirname "$0")/visto.txt"\n')
    monkeypatch.setenv("CVM_PROJETO", str(vm))
    monkeypatch.setenv("UV_PROJECT_ENVIRONMENT", "/ambiente/do/apresentacao")
    assert midia.cvm("veo") == 0
    assert (vm / "visto.txt").read_text().strip() == "UV=vazio"


def test_palco_ignora_mensagem_de_outra_janela():
    """Uma janela qualquer (não a tela do apresentador) não consegue avançar o palco por postMessage."""
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        nav = p.chromium.launch()
        srv = html._servir(RUIM)
        url = f"http://127.0.0.1:{srv.server_address[1]}/{RUIM.resolve().relative_to(config.RAIZ).as_posix()}?vivo"
        pg = nav.new_page()
        pg.goto(url)
        pg.wait_for_timeout(500)
        antes = pg.evaluate("location.hash")
        pg.evaluate("""() => { const f = document.createElement('iframe'); document.body.appendChild(f);
            f.contentWindow.eval("parent.postMessage({palcoComando: 'proxima'}, '*')"); }""")
        pg.wait_for_timeout(2500)                             # o endereço muda quando o passo termina
        depois = pg.evaluate("location.hash")
        with pg.expect_popup() as janela:
            pg.keyboard.press("p")
        ap = janela.value
        ap.wait_for_load_state()
        ap.wait_for_timeout(800)
        ap.keyboard.press("ArrowRight")
        pg.wait_for_timeout(2500)
        pela_tela = pg.evaluate("location.hash")
        nav.close()
        srv.shutdown()
    assert antes == depois
    assert pela_tela != antes                                 # a tela do apresentador que o palco abriu manda


# ---------- base técnica: tempo, ajudantes, contexto da câmera, corte pelo topo, [CONFERIR] ----------

AJUDANTES = Path(__file__).parent / "fixtures" / "palco_ajudantes" / "deck.html"
ACENTO = Path(__file__).parent / "fixtures" / "palco_acento" / "deck.html"


def _pagina(deck, f):
    """Abre o deck em modo render, roda f(pg) e fecha."""
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        srv, nav, pg, _ = html._abrir(p, deck)
        try:
            return f(pg)
        finally:
            nav.close()
            srv.shutdown()


def test_tempo_faixa_degrau_mola_curvas_e_onda():
    r = _pagina(AJUDANTES, lambda pg: pg.evaluate("""async () => {
        const T = await import('/motor/tempo.js');
        const eq = {resposta: 2 * Math.PI / Math.sqrt(240), amortecimento: 24 / (2 * Math.sqrt(240))};
        return {
            faixa: [T.faixa(1, 1, 1), T.faixa(1.0001, 1, 1), T.faixa(0, 1, 1), T.faixa(2, 1, 0), T.faixa(0.5, 1, 0), T.faixa(0.5, 0, 1)],
            mola: [T.molaAR(0), T.molaAR(0.05), T.molaAR(1), T.molaAR(5), T.molaAR(-1)],
            equivale: [T.molaAR(0.1, eq), T.mola(0.1, {rigidez: 240, amortecimento: 24})],
            curvas: [T.sair(0), T.sair(1), T.sair(0.5), T.chegar(0), T.chegar(1), T.chegar(0.5)],
            onda: [T.escalonar(5), T.escalonar([{x: 0, y: 0}, {x: 3, y: 4}, {x: 6, y: 8}], {de: {x: 0, y: 0}}),
                   T.escalonar(5, {de: 'centro', quantidade: 1}), T.escalonar(5, {de: 'bordas', quantidade: 1}),
                   T.escalonar([{x: 0, y: 0, w: 10, h: 10}, {x: 20, y: 0, w: 10, h: 10}]), T.escalonar(1), T.escalonar([])],
        };
    }"""))
    assert r["faixa"] == [0, 1, 0, 1, 0, 0.5]                         # viagem 0 é degrau, nunca NaN
    m = r["mola"]
    assert m[0] == 0 and 0 < m[1] < 1 and m[2] == 1 and m[3] == 1 and m[4] == 0   # assenta em 1 exato
    assert r["equivale"][0] == pytest.approx(r["equivale"][1], abs=1e-12)          # entrar() = resposta 0,41 s e ζ 0,77
    c = r["curvas"]
    assert c[:2] == [0, 1] and c[2] < 0.5 and c[3:5] == [0, 1] and c[5] > 0.5     # sair arranca devagar, chegar pousa
    onda = r["onda"]
    assert onda[0] == pytest.approx([0, 0.1, 0.2, 0.3, 0.4])
    assert onda[1] == pytest.approx([0, 0.2, 0.4])
    assert onda[2] == pytest.approx([1, 0.5, 0, 0.5, 1]) and onda[3] == pytest.approx([0, 0.5, 1, 0.5, 0])
    assert onda[4] == pytest.approx([0, 0.4]) and onda[5] == [0] and onda[6] == []


def test_ajudantes_e_contexto_da_camera_valores_exatos():
    def medir(pg):
        ver = lambda t: pg.evaluate("t => __palco.ver(t)", t)
        js = lambda e: pg.evaluate(e)
        r = {}
        ver(0.0)
        r["t0"] = js("""({texto: document.querySelector('#frase span').textContent, kb: document.querySelector('#foto div').style.transform,
            cursor: document.querySelector('#frase span:nth-child(2) span').style.visibility,
            fundo: document.querySelector('#frase span:nth-child(2) span').style.background,
            anel: document.querySelector('[data-slide=a] svg path').style.visibility})""")
        for t in (0.5, 0.2, 0.5):
            ver(t)
            r.setdefault("meio", []).append(js("document.querySelector('#frase span').textContent"))
        ver(1.0)
        r["t1"] = js("""(() => { const a = document.getElementById('peca').getBoundingClientRect(), b = document.getElementById('origem').getBoundingClientRect();
            return {texto: document.querySelector('#frase span').textContent, resto: document.querySelector('#frase span:nth-child(3)').textContent,
                cursor: document.querySelector('#frase span:nth-child(2) span').style.visibility, kb: document.querySelector('#foto div').style.transform,
                origem: document.querySelector('#foto div').style.transformOrigin, peca: [a.x, a.y, a.width, a.height], alvo: [b.x, b.y, b.width, b.height]}; })()""")
        ver(1.5)
        r["voo"] = [js("document.getElementById('peca').style.transform"), js("document.getElementById('num').textContent")]
        ver(2.0)
        r["t2"] = js("""({peca: document.getElementById('peca').style.transform, num: document.getElementById('num').textContent,
            svgs: document.querySelectorAll('[data-slide=a] svg').length, traco: document.querySelector('[data-slide=a] svg path').style.strokeDasharray,
            d: [...document.querySelectorAll('[data-slide=a] svg path')].map((p) => p.getAttribute('d'))})""")
        ver(1.5)
        ver(2.0)
        r["d2"] = js("[...document.querySelectorAll('[data-slide=a] svg path')].map((p) => p.getAttribute('d'))")
        r["svgs2"] = js("document.querySelectorAll('[data-slide=a] svg').length")
        # contar só escreve quando o texto muda: redesenhar o mesmo instante não mexe no DOM
        r["mutacoes"] = pg.evaluate("""async () => { const mo = new MutationObserver(() => {});
            mo.observe(document.getElementById('num'), {childList: true, characterData: true, subtree: true});
            await __palco.ver(2.0); await __palco.ver(2.0); const n = mo.takeRecords().length; mo.disconnect(); return n; }""")
        r["ctx"] = {}
        for t in (0.5, 2.0, 2.0001, 3.25, 4.0):
            ver(t)
            r["ctx"][t] = js("window.__ctx")
        return r

    r = _pagina(AJUDANTES, medir)
    completo = "O juiz julgou o pedido, e a frase se escreve."
    # digitar: nada em k = 0, prefixo determinístico no meio (mesmo k, mesmo texto em qualquer ordem), tudo em k = 1
    assert r["t0"]["texto"] == "" and r["t0"]["cursor"] == "" and "var(--cor-destaque)" in r["t0"]["fundo"]
    assert r["meio"][0] == r["meio"][2] and completo.startswith(r["meio"][0]) and 0 < len(r["meio"][0]) < len(completo)
    assert r["t1"]["texto"] == completo and r["t1"]["resto"] == "" and r["t1"]["cursor"] == "hidden"
    # kenburns: começa na escala pedida e assenta em scale(1) exato
    assert r["t0"]["kb"] == "scale(1.06)" and r["t1"]["kb"] == "scale(1)" and r["t1"]["origem"] == "70% 55%"
    # voar: em k = 0 a peça ocupa a caixa de origem; em k = 1 o transform fica vazio
    assert r["t1"]["peca"] == pytest.approx(r["t1"]["alvo"], abs=0.5)
    assert r["voo"][0].startswith("translate(") and r["voo"][1] == "4"
    assert r["t2"]["peca"] == "" and r["t2"]["num"] == "8"
    # anotar: uma camada por alvo, traço que termina sem tracejado, o mesmo desenho a cada redesenho
    assert r["t0"]["anel"] == "hidden" and r["t2"]["svgs"] == r["svgs2"] == 2 and r["t2"]["traco"] == "none"
    assert r["t2"]["d"] == r["d2"] and all(d.startswith("M") for d in r["t2"]["d"])
    assert r["mutacoes"] == 0
    # câmera: pose em ctx.camera; kCamera 1 no primeiro slide, degrau na viagem 0 (corte seco), suave na viagem curta
    c = r["ctx"]
    assert c[0.5] == {"i": 0, "camera": {"cx": 960, "cy": 540, "z": 1, "rot": 0}, "kCamera": 1}
    assert c[2.0]["i"] == 0
    assert c[2.0001]["i"] == 1 and c[2.0001]["kCamera"] == 1 and c[2.0001]["camera"]["cx"] == 3360
    assert c[3.25]["kCamera"] == pytest.approx(0.5, abs=1e-6) and c[3.25]["camera"]["cx"] == pytest.approx(4560, abs=0.01)
    assert c[4.0]["kCamera"] == 1 and c[4.0]["camera"]["cx"] == 5760
    # o desenho da anotação sai da semente: página nova, mesmo traço
    assert _pagina(AJUDANTES, lambda pg: (pg.evaluate("__palco.ver(2.0)"),
                   pg.evaluate("[...document.querySelectorAll('[data-slide=a] svg path')].map((p) => p.getAttribute('d'))"))[1]) == r["t2"]["d"]


def test_ajudantes_sao_deterministicos():
    """digitar, voar, anotar e kenburns no meio da animação e nas paradas: mesmo quadro em outra ordem e em página nova
    (T da linha de vídeo: 1,9 e 5,5 no meio dos passos de a, 7 na parada, 12,2 no meio da viagem para c)."""
    assert html.verificar(AJUDANTES, [1.9, 5.5, 7.0, 12.2])


def test_clique_no_meio_toca_o_resto_em_3x():
    """Ao vivo, o segundo clique no meio do passo não salta: o resto toca em 3x e o passo seguinte começa sozinho."""
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        nav = p.chromium.launch()
        srv = html._servir(AJUDANTES)
        pg = nav.new_page(viewport={"width": 1280, "height": 720})
        pg.goto(f"http://127.0.0.1:{srv.server_address[1]}/{AJUDANTES.resolve().relative_to(config.RAIZ).as_posix()}?vivo")
        pg.wait_for_timeout(800)
        pg.keyboard.press("ArrowRight")
        pg.wait_for_timeout(200)
        pg.keyboard.press("ArrowRight")                       # resta 0,8 s do passo de 1 s: em 3x, uns 0,27 s
        logo = pg.evaluate("location.hash")
        pg.wait_for_timeout(700)
        depois = pg.evaluate("location.hash")
        pg.wait_for_timeout(1300)
        fim = pg.evaluate("location.hash")
        nav.close()
        srv.shutdown()
    assert logo == ""                                         # antes, o clique saltava direto para a parada 1
    assert depois == "#parada=1" and fim == "#parada=2"


def test_oraculo_ve_o_acento_cortado_pelo_topo_do_pai():
    def medir(pg):
        pg.evaluate("__palco.ir(1)")
        return pg.evaluate("__palco.medir()")

    blocos = {b["id"]: b for b in _pagina(ACENTO, medir)}
    corta, inteiro = blocos["corta"], blocos["inteiro"]
    assert corta["topoCortado"] and not corta["transborda"]  # a folga da entrelinha justa continua descontada
    assert not inteiro["topoCortado"] and not inteiro["transborda"]
    assert any("corta o topo" in m for m in _niveis(palco.checar_parada([corta]), "ERRO"))
    assert not any("corta o topo" in m for _, m in palco.checar_parada([inteiro]))


def test_pdf_e_pacote_recusam_conferir(tmp_path, monkeypatch):
    deck = tmp_path / "d" / "deck.html"
    deck.parent.mkdir()
    deck.write_text('<!doctype html>\n<p>Lista de out/2026 <b>[CONFERIR]</b></p>\n<!-- fonte: [CONFERIR] -->\n'
                    '<p>[CONFERIR Kalai et al.]</p>\n')
    assert palco.pendencias(deck) == ["linha 2: Lista de out/2026 [CONFERIR]", "linha 3: <!-- fonte: [CONFERIR] -->",
                                      "linha 4: [CONFERIR Kalai et al.]"]
    with pytest.raises(SystemExit, match=r"3 \[CONFERIR\](.|\n)*linha 2"):
        palco.pdf(deck)
    with pytest.raises(SystemExit, match="rascunho"):
        palco.empacotar(deck, tmp_path / "pacote", com_pdf=False)
    assert not (tmp_path / "pacote").exists()
    monkeypatch.setattr(palco, "fotografar", lambda *a, **k: (_ for _ in ()).throw(RuntimeError("passou da trava")))
    with pytest.raises(RuntimeError, match="passou da trava"):
        palco.pdf(deck, rascunho=True)
    assert palco.pendencias(DEMO) == [] and palco.pendencias(RUIM) == []


def test_lint_avisa_getboundingclientrect(tmp_path):
    deck = tmp_path / "deck.html"
    deck.write_text("<script>palco({}); const r = el.getBoundingClientRect();</script>")
    assert [n for n, m in lint.checar(deck) if "getBoundingClientRect" in m] == ["AVISO"]
