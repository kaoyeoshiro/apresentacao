"""Biblioteca de cenas (motor/cenas.js e motor/cenas.css): o catálogo do plano contínuo passa no oráculo com os três
temas e continua passando depois de apagar um slide do meio, que é a promessa do molde (a trilha se refaz)."""
import re
import shutil
from pathlib import Path

import pytest

from ferramentas import config, palco

CATALOGO = config.RAIZ / "decks" / "catalogo"


def _copia(nome: str, tema: str) -> Path:
    """Deck novo do plano contínuo (./ap novo --modo continuo, que copia o catálogo) dentro de decks/, onde o servidor
    do oráculo o alcança, com o tema trocado: prova também que o deck que uma sessão cria passa com cada tema."""
    slug = f"_teste-cenas-{nome}"
    shutil.rmtree(config.DECKS / slug, ignore_errors=True)
    return palco.novo(slug, tema, modo="continuo") / "deck.html"


def _apagar(deck: Path, slide: str) -> None:
    """Apaga a section e a entrada da lista, como o comentário do catálogo manda."""
    html = deck.read_text(encoding="utf-8")
    html, n1 = re.subn(rf'\n[ \t]*<section data-slide="{slide}".*?</section>', "", html, count=1, flags=re.S)
    html, n2 = re.subn(rf"\n[ \t]*\{{id: '{slide}'.*?(?=\n[ \t]*(\{{id: |\];))", "", html, count=1, flags=re.S)
    assert (n1, n2) == (1, 1), f"não achei a section ou a entrada de {slide}"
    deck.write_text(html, encoding="utf-8")


def test_catalogo_passa_no_oraculo_com_cojuris():
    assert palco.sondar(CATALOGO / "deck.html") == 0


@pytest.mark.parametrize("tema", ["noite", "pge"])
def test_catalogo_passa_com_outros_temas(tema):
    deck = _copia(tema, tema)
    try:
        assert palco.sondar(deck, determinismo=False) == 0
    finally:
        shutil.rmtree(deck.parent, ignore_errors=True)


def test_pilula_e_selo_no_mesmo_slide_claro_nao_se_sobrepoem(capsys):
    """Imagem gerada e fato a conferir no mesmo slide claro: o selo sai do canto da pílula sem cair nas legendas."""
    deck = _copia("pilula-selo", "cojuris")
    try:
        html = deck.read_text(encoding="utf-8")
        selo = '<p class="selo-ia">imagens geradas por IA</p>'
        assert html.count(selo) == 1
        deck.write_text(html.replace(selo, selo + '\n    <p class="pilula">[CONFERIR] Agent Skills</p>'), encoding="utf-8")
        assert palco.sondar(deck, determinismo=False) == 0
        saida = capsys.readouterr().out
        assert not [l for l in saida.splitlines() if "se sobrepõem" in l and ("geradas por IA" in l or "[CONFERIR]" in l)], saida
    finally:
        shutil.rmtree(deck.parent, ignore_errors=True)


def test_apagar_um_slide_do_meio_refaz_a_trilha():
    deck = _copia("apagado", "cojuris")
    try:
        _apagar(deck, "comparacao")
        assert 'data-slide="comparacao"' not in deck.read_text(encoding="utf-8")
        assert palco.sondar(deck, determinismo=False) == 0
    finally:
        shutil.rmtree(deck.parent, ignore_errors=True)
