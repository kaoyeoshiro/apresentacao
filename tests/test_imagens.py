"""./ap imagens com o gerador simulado: nada sai para a rede e nada custa."""
import hashlib
import json
import shutil
import time
from pathlib import Path

import numpy as np
import pytest
from PIL import Image

from ferramentas import config, imagens

ESTILO = "SERIES STYLE: quiet still life, one soft window light from the upper left, fine grain."
TOML = '''
[[imagem]]
nome = "heroi"
slide = "abertura"
papel = "heroica"
prompt = "A wooden drawer in the right third of the frame; the left half is empty dark wall."
resolucao = "4K"
refs = ["midia/originais/pasta.png"]
zona_texto = [0, 0, 0.4, 1]
tratamento = { gama = 1.4 }

[[imagem]]
nome = "doc"
slide = "prompt"
papel = "objeto"
prompt = "A single A4 page seen from straight above on a flat off-white backdrop."
aspect = "3:4"
'''


@pytest.fixture
def deck(tmp_path) -> Path:
    tema = tmp_path / "temas" / "t"
    (tema / "imagem" / "refs").mkdir(parents=True)
    (tema / "tema.css").write_text(":root { --cor-fundo: #FCF9F4; --cor-tinta: #0F2641; --cor-destaque: #D49D38; }\n")
    (tema / "imagem" / "estilo.txt").write_text(f"# comentário que não vai ao prompt\n{ESTILO}\n")
    Image.new("RGB", (64, 36), (90, 90, 90)).save(tema / "imagem" / "refs" / "mestra.png")
    (tema / "imagem" / "padroes.toml").write_text(
        'geradores = ["gemini"]\n[tratamento.heroica]\ntom = "duotone"\nlargura = 512\n'
        '[tratamento.objeto]\ntom = "duotone"\nlargura = 256\nalfa = true\ngama = 1.8\n')
    d = tmp_path / "decks" / "x"
    (d / "midia" / "originais").mkdir(parents=True)
    (d / "deck.html").write_text('<link rel="stylesheet" href="../../temas/t/tema.css">\n')
    (d / "imagens.toml").write_text(TOML)
    Image.new("RGB", (64, 48), (150, 120, 80)).save(d / "midia" / "originais" / "pasta.png")
    return d


def _foto(aspect: str, largura: int) -> Image.Image:
    """Quadro escuro à esquerda e um objeto claro à direita, no formato pedido."""
    w, h = (int(v) for v in aspect.split(":"))
    a = np.full((round(largura * h / w), largura, 3), 40, np.uint8)
    a[a.shape[0] // 4: -a.shape[0] // 4, largura * 2 // 3: largura - 8] = 230
    return Image.fromarray(a)


@pytest.fixture
def gerador(monkeypatch):
    """Troca a ponte por um gerador local, anota cada chamada e não dorme de verdade."""
    chamadas, dormiu = [], []

    def ponte(prompt, saida, *, backend, aspect, resolucao, refs):
        chamadas.append({"prompt": prompt, "saida": saida, "backend": backend, "aspect": aspect,
                         "resolucao": resolucao, "refs": list(refs)})
        _foto(aspect, {"1K": 320, "2K": 640, "4K": 960}[resolucao]).save(saida)
        return 0, f"Imagem salva em: {saida}"

    monkeypatch.setattr(imagens, "ponte", ponte)
    monkeypatch.setattr(imagens.time, "sleep", dormiu.append)
    monkeypatch.setattr(imagens, "_ultima", [-imagens.INTERVALO])
    return chamadas, dormiu


def _creditos(deck):
    return {i["arquivo"]: i for i in json.loads((deck / "midia" / "creditos.json").read_text())}


def test_situacao_mostra_o_que_falta_sem_gastar(deck, monkeypatch, capsys):
    monkeypatch.setattr(imagens, "ponte", lambda *a, **k: pytest.fail("a situação não pode chamar o gerador"))
    assert imagens.main([str(deck)]) == 0
    saida = capsys.readouterr().out
    assert "heroi" in saida and "gemini 4K" in saida and "0.11" in saida and "0.05" in saida
    assert "0 de 2 prontas; falta gastar US$ 0.16" in saida


def test_rascunhos_levam_estilo_e_mestra_e_montam_a_folha(deck, gerador):
    chamadas, dormiu = gerador
    folha = imagens.rascunhos(str(deck), n=2)
    assert [c["saida"].name for c in chamadas] == ["heroi-1.png", "heroi-2.png", "doc-1.png", "doc-2.png"]
    c = chamadas[0]
    assert (c["backend"], c["resolucao"], c["aspect"]) == ("gemini", "1K", "16:9")
    assert c["prompt"].startswith(ESTILO + "\n\nImage 1 is a style reference only")
    assert "comentário" not in c["prompt"]
    assert "Image 2 is the object reference" in c["prompt"] and c["prompt"].endswith("empty dark wall.")
    assert c["refs"][0].name == "mestra.png" and c["refs"][1].name == "pasta.png"
    assert chamadas[2]["aspect"] == "3:4" and len(chamadas[2]["refs"]) == 1
    # uma chamada por vez, a 6 s da anterior
    assert len(dormiu) == 4 and dormiu[0] == 0
    assert all(s == pytest.approx(imagens.INTERVALO, abs=0.5) for s in dormiu[1:])
    cred = _creditos(deck)["midia/originais/rascunhos/heroi-1.png"]
    assert cred["estilo_sha256"] == hashlib.sha256(ESTILO.encode()).hexdigest()
    assert cred["custo_usd"] == 0.0336 and cred["modelo"] == "gemini"
    assert cred["refs"][0] == "temas/t/imagem/refs/mestra.png"
    assert folha == deck / "storyboard" / "candidatos.png" and Image.open(folha).width > 900
    # a numeração continua de onde parou
    imagens.rascunhos(str(deck), ["heroi"], n=1)
    assert chamadas[-1]["saida"].name == "heroi-3.png"


def test_teto_recusa_antes_de_chamar_o_gerador(deck, gerador, capsys):
    chamadas, _ = gerador
    with pytest.raises(SystemExit, match="acima do teto"):
        imagens.rascunhos(str(deck), n=3, teto=0.10)   # 6 x 0,0336 = 0,20
    assert chamadas == [] and not (deck / "midia" / "originais" / "rascunhos").exists()
    assert "custo estimado: US$ 0.20 em 6 chamada(s)" in capsys.readouterr().out


def test_final_com_rascunho_trata_credita_e_guarda_o_anterior(deck, gerador):
    chamadas, _ = gerador
    imagens.rascunhos(str(deck), ["heroi"], n=2)
    imagens.final(str(deck), ["heroi=2"])
    c = chamadas[-1]
    assert c["resolucao"] == "4K" and c["refs"][-1].name == "heroi-2.png"
    assert c["prompt"].endswith("\nImage 3 is the approved draft of this image: keep its composition, subject, camera "
                                "angle and framing exactly; render it at full fidelity.")
    orig, webp = deck / "midia" / "originais" / "heroi.png", deck / "midia" / "heroi.webp"
    assert orig.is_file() and webp.is_file() and Image.open(webp).width == 512
    cred = _creditos(deck)
    assert cred["midia/originais/heroi.png"]["custo_usd"] == 0.113
    t = cred["midia/heroi.webp"]["tratamento"]
    assert (t["tom"], t["largura"], t["gama"]) == ("duotone", 512, 1.4)
    assert cred["midia/heroi.webp"]["prompt"] == c["prompt"]
    assert cred["midia/heroi.webp"]["original"] == "midia/originais/heroi.png"
    # de novo: o original anterior vai para rascunhos/, com o crédito
    imagens.final(str(deck), ["heroi"])
    assert (deck / "midia" / "originais" / "rascunhos" / "heroi-antes-1.png").is_file()
    cred = _creditos(deck)
    assert cred["midia/originais/rascunhos/heroi-antes-1.png"]["custo_usd"] == 0.113
    assert "approved draft" not in cred["midia/originais/heroi.png"]["prompt"]


def test_final_recusa_rascunho_que_nao_existe_sem_gastar(deck, gerador):
    chamadas, _ = gerador
    with pytest.raises(SystemExit, match="heroi-7.png não existe"):
        imagens.final(str(deck), ["heroi=7"])
    assert chamadas == []


def test_tratar_reproduz_o_webp_sem_custo_e_situacao_acusa_tratamento_velho(deck, gerador, capsys):
    chamadas, _ = gerador
    imagens.final(str(deck), ["doc"])
    webp = deck / "midia" / "doc.webp"
    antes, n = webp.read_bytes(), len(chamadas)
    assert Image.open(webp).mode == "RGBA"
    webp.unlink()
    imagens.retratar(str(deck))
    assert webp.read_bytes() == antes and len(chamadas) == n
    capsys.readouterr()
    imagens.situacao(str(deck))
    assert any(l.split()[:1] == ["doc"] and " sim " in l for l in capsys.readouterr().out.splitlines())
    (deck / "imagens.toml").write_text(TOML.replace('aspect = "3:4"', 'aspect = "3:4"\ntratamento = { gama = 1.2 }'))
    imagens.situacao(str(deck))
    assert any(l.split()[:1] == ["doc"] and "refazer" in l for l in capsys.readouterr().out.splitlines())


def test_copia_sem_originais_vale_pelo_webp_e_nao_gasta(deck, gerador, capsys):
    """Num checkout novo, midia/originais/ (fora do git) não existe: o WebP com crédito é o final, e nada é refeito."""
    chamadas, _ = gerador
    imagens.final(str(deck), ["heroi", "doc"])
    shutil.rmtree(deck / "midia" / "originais")
    webp, n = (deck / "midia" / "doc.webp").read_bytes(), len(chamadas)
    capsys.readouterr()
    imagens.situacao(str(deck))
    saida = capsys.readouterr().out
    assert "de 2 prontas; falta gastar US$ 0.00" in saida and "0 de 2 prontas" not in saida
    linhas = [l for l in saida.splitlines() if l.split()[:1] in (["heroi"], ["doc"])]
    assert len(linhas) == 2 and all("fora do git" in l and l.endswith("0.00") for l in linhas)
    assert any(l.startswith("doc ") and " sim " in l for l in linhas)
    assert imagens.rascunhos(str(deck)) is None and len(chamadas) == n
    imagens.retratar(str(deck))
    saida = capsys.readouterr().out
    assert "--final" not in saida and "fora do git" in saida
    assert (deck / "midia" / "doc.webp").read_bytes() == webp and len(chamadas) == n


def test_marcador_do_molde_nao_vale_como_final(deck, gerador, capsys):
    """O deck criado do catálogo traz WebPs-marcador com a nota "marcador: ..." no crédito. Uma entrada com o mesmo nome
    continua a gerar: a situação cobra o custo, o --rascunhos sem nomes a pega, e o --tratar não finge que está pronta."""
    from ferramentas import midia
    chamadas, _ = gerador
    Image.new("RGB", (64, 36), (90, 90, 90)).save(deck / "midia" / "heroi.webp")
    midia.creditar(deck, deck / "midia" / "heroi.webp", ferramenta="trazido", nota="marcador: substitua por mídia do deck")
    imagens.situacao(str(deck))
    saida = capsys.readouterr().out
    assert any(l.split()[:1] == ["heroi"] and "marcador" in l and not l.endswith("0.00") for l in saida.splitlines()), saida
    imagens.retratar(str(deck), ["heroi"])
    assert "marcador do molde" in capsys.readouterr().out
    imagens.rascunhos(str(deck), n=1)
    assert any(c["saida"].name.startswith("heroi-") for c in chamadas)
    imagens.final(str(deck), ["heroi"])
    assert "nota" not in _creditos(deck)["midia/heroi.webp"]               # o final substitui o crédito do marcador


def test_limite_de_taxa_espera_o_que_a_ponte_pede_e_tenta_de_novo(deck, gerador, monkeypatch):
    chamadas, dormiu = gerador
    simulada = imagens.ponte
    erros = ['RuntimeError: Gemini erro 429: {"error": {"status": "RESOURCE_EXHAUSTED", '
             '"details": [{"retryDelay": "7s"}]}}']

    def ponte(prompt, saida, **k):
        if erros:
            chamadas.append({"saida": saida})
            return 1, erros.pop()
        return simulada(prompt, saida, **k)

    monkeypatch.setattr(imagens, "ponte", ponte)
    imagens.rascunhos(str(deck), ["doc"], n=1)
    assert len(chamadas) == 2 and 7.0 in dormiu and (deck / "midia" / "originais" / "rascunhos" / "doc-1.png").is_file()
    monkeypatch.setattr(imagens, "ponte", lambda *a, **k: (1, "RuntimeError: GEMINI_KEY não definida no .env"))
    with pytest.raises(SystemExit, match="falhou"):
        imagens.rascunhos(str(deck), ["doc"], n=1)


def test_zona_de_texto_acusa_bordas_e_luz_desigual(deck, tmp_path, capsys):
    a = np.full((360, 640, 3), 40, np.uint8)
    a[90:270, 420:620] = 230
    limpa = tmp_path / "limpa.png"
    Image.fromarray(a).save(limpa)
    desvio, bordas = imagens.medir_zona(limpa, [0, 0, 0.6, 1])
    assert desvio < imagens.LIMITE_DESVIO and bordas == 0
    assert imagens.medir_zona(limpa, [0.5, 0, 1, 1])[1] > imagens.LIMITE_BORDAS
    a[:, :300:24] = 120   # veio de madeira na zona do título
    Image.fromarray(a).save(veio := tmp_path / "veio.png")
    assert imagens.medir_zona(veio, [0, 0, 0.4, 1])[1] > imagens.LIMITE_BORDAS
    b = np.tile(np.linspace(20, 200, 640, dtype=np.uint8)[None, :, None], (360, 1, 3))   # luz desigual, sem bordas
    Image.fromarray(b).save(luz := tmp_path / "luz.png")
    desvio, bordas = imagens.medir_zona(luz, [0, 0, 0.5, 1])
    assert desvio > imagens.LIMITE_DESVIO and bordas == 0
    _, _, itens = imagens.carregar(str(deck))
    Image.fromarray(a).save(deck / "midia" / "originais" / "heroi.png")
    imagens._tratar(deck, itens[0], deck / "midia" / "originais" / "heroi.png")
    assert "AVISO heroi: zona de texto" in capsys.readouterr().out


@pytest.mark.parametrize("troca, erro", [
    (('papel = "objeto"', 'papel = "foto"'), "papel 'foto'"),
    (('aspect = "3:4"', 'aspect = "3:4"\ncor = "azul"'), "chave desconhecida cor"),
    (('aspect = "3:4"', 'aspect = "3:4"\nbackend = "azure-flux"'), "o tema não permite azure-flux"),
    (('refs = ["midia/originais/pasta.png"]', 'refs = ["midia/pasta.webp"]'), "recusa WebP"),
    (('prompt = "A single', f'prompt = "{ESTILO} A single'), "repete o estilo"),
    (('tratamento = { gama = 1.4 }', 'tratamento = { brilho = 2 }'), "tratamento com brilho"),
    (('tratamento = { gama = 1.4 }', 'tratamento = { tom = "duotono" }'), "tratamento tom = 'duotono'"),
    (('zona_texto = [0, 0, 0.4, 1]', 'zona_texto = [0.5, 0, 0.4, 1]'), "zona_texto"),
])
def test_imagens_toml_invalido_para_antes_de_tudo(deck, troca, erro):
    (deck / "imagens.toml").write_text(TOML.replace(*troca))
    with pytest.raises(SystemExit, match=erro):
        imagens.carregar(str(deck))


def test_backend_sem_preco_pede_preco_usd(deck, gerador):
    chamadas, _ = gerador
    padroes = deck.parent.parent / "temas" / "t" / "imagem" / "padroes.toml"
    padroes.write_text(padroes.read_text().replace('["gemini"]', '["gemini", "azure-flux"]'))
    (deck / "imagens.toml").write_text(TOML.replace('aspect = "3:4"', 'aspect = "3:4"\nbackend = "azure-flux"'))
    with pytest.raises(SystemExit, match="preco_usd"):
        imagens.final(str(deck), ["doc"])
    (deck / "imagens.toml").write_text(TOML.replace('aspect = "3:4"', 'aspect = "3:4"\nbackend = "azure-flux"\n'
                                                                      'preco_usd = 0.07'))
    imagens.final(str(deck), ["doc"])
    assert chamadas[-1]["backend"] == "azure-flux" and _creditos(deck)["midia/originais/doc.png"]["custo_usd"] == 0.07


def test_sem_mestra_a_ref_do_objeto_vira_image_1(deck):
    (deck.parent.parent / "temas" / "t" / "imagem" / "refs" / "mestra.png").unlink()
    _, serie, itens = imagens.carregar(str(deck))
    prompt, refs = imagens.compor(itens[0], serie)
    assert "Image 1 is the object reference" in prompt and [r.name for r in refs] == ["pasta.png"]


def test_intervalo_real_entre_chamadas(deck, monkeypatch):
    """Sem trocar o relógio: a segunda chamada espera o que falta do intervalo."""
    monkeypatch.setattr(imagens, "INTERVALO", 0.3)
    monkeypatch.setattr(imagens, "_ultima", [-1.0])
    instantes = []

    def ponte(prompt, saida, **k):
        instantes.append(time.monotonic())
        Image.new("RGB", (32, 18)).save(saida)
        return 0, ""

    monkeypatch.setattr(imagens, "ponte", ponte)
    imagens.rascunhos(str(deck), ["heroi"], n=2)
    assert instantes[1] - instantes[0] >= 0.29


def test_modelo_do_tema_recusa_gerar_ate_a_biblia_ser_escrita(deck, gerador):
    img = deck.parent.parent / "temas" / "t" / "imagem"
    shutil.rmtree(img)
    shutil.copytree(config.TEMAS / "_modelo" / "imagem", img, ignore=shutil.ignore_patterns("._*"))
    _, serie, _ = imagens.carregar(str(deck))
    assert serie["estilo"] == "" and serie["geradores"] == ["gemini"]
    assert set(serie["tratamento"]) == set(imagens.PAPEIS)
    with pytest.raises(SystemExit, match="escreva a bíblia"):
        imagens.rascunhos(str(deck), n=1)
    assert gerador[0] == []


def test_imagens_toml_da_previa_vale_com_o_tema_real():
    _, serie, itens = imagens.carregar(str(config.DECKS / "previa-curso-ia"))
    assert [e["nome"] for e in itens] == ["heroi-aula1", "heroi-aula2", "pasta-aberta", "doc-peticao", "doc-contrato",
                                          "doc-modelo"]
    assert serie["estilo"].startswith("SERIES STYLE") and serie["mestra"].name.startswith("mestra")
    assert itens[3]["tratamento"]["gama"] == 1.8 and itens[5]["tratamento"]["gama"] == 2.6


@pytest.mark.parametrize("tom", ["duotone", "tritone"])
def test_tratamento_no_tema_escuro_nao_sai_em_negativo(tom):
    """No tema noite a tinta é clara e o fundo escuro: o preto da foto vai ao fundo e o branco à tinta."""
    from ferramentas import tratar
    deck = config.DECKS / "_teste-tratar-noite"
    deck.mkdir(exist_ok=True)
    try:
        (deck / "deck.html").write_text('<link rel="stylesheet" href="../../temas/noite/tema.css">', encoding="utf-8")
        cores = tratar.cores_do_tema(deck)
        assert sum(cores["tinta"]) > sum(cores["fundo"])
        rgb = np.array([[[0.0, 0.0, 0.0], [255.0, 255.0, 255.0]]])
        out = tratar.mapear(rgb, cores, tom=tom, intensidade=1, grao=0, lo=0, hi=1)
        assert np.allclose(out[0, 0], cores["fundo"]) and np.allclose(out[0, 1], cores["tinta"])
    finally:
        shutil.rmtree(deck, ignore_errors=True)


@pytest.mark.parametrize("tema", ["noite", "pge"])
def test_temas_sem_mestra_tem_serie_e_geram_com_aviso(tema, capsys):
    """noite e pge têm bíblia, lista e padrões; sem a mestra, o comando avisa e não aborta."""
    img = config.TEMAS / tema / "imagem"
    assert (img / "estilo.txt").is_file() and (img / "proibidos.txt").is_file() and (img / "padroes.toml").is_file()
    deck = config.DECKS / f"_teste-serie-{tema}"
    deck.mkdir(exist_ok=True)
    try:
        (deck / "deck.html").write_text(f'<link rel="stylesheet" href="../../temas/{tema}/tema.css">', encoding="utf-8")
        (deck / "imagens.toml").write_text('[[imagem]]\nnome = "a"\nslide = "s"\npapel = "objeto"\nprompt = "A page."\n',
                                           encoding="utf-8")
        _, serie, itens = imagens.carregar(str(deck))
        assert serie["estilo"].startswith("SERIES STYLE") and serie["geradores"] == ["gemini"]
        assert ("gama" in itens[0]["tratamento"]) == (tema == "pge")   # tema escuro: o papel não leva gama
        imagens._exigir_serie(serie)
        imagens.situacao(str(deck))
        assert "gere a mestra" in capsys.readouterr().out
    finally:
        shutil.rmtree(deck, ignore_errors=True)


@pytest.mark.parametrize("ref", ["../../../segredo.png", "/etc/segredo.png"])
def test_ref_fora_do_deck_e_recusada_antes_de_ir_ao_gerador(deck, gerador, ref):
    chamadas, _ = gerador
    toml = (deck / "imagens.toml").read_text().replace('"midia/originais/pasta.png"', f'"{ref}"')
    (deck / "imagens.toml").write_text(toml)
    with pytest.raises(SystemExit, match="fora da pasta do deck"):
        imagens.rascunhos(str(deck), n=1)
    assert chamadas == []
