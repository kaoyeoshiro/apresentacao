from ferramentas.publicar import FIM, atualizar_indice, copiar_pacote

BASE = f"""<ul>
    <li><a href="/apresentacao/aula-1/">
      <div class="numero">Apresentação 1</div>
      <p class="titulo">Um</p>
      <p class="descricao">Primeira</p>
    </a></li>
    {FIM}
</ul>"""


def test_nova_apresentacao_entra_depois_da_ultima_com_numero_seguinte():
    r = atualizar_indice(BASE, "aula-2", "Dois & mais", "Segunda")
    assert 'href="/apresentacao/aula-2/"' in r and "Apresentação 2" in r
    assert "Dois &amp; mais" in r and r.index("aula-1") < r.index("aula-2") < r.index(FIM)


def test_repetir_a_pasta_troca_o_texto_e_mantem_o_numero():
    r = atualizar_indice(atualizar_indice(BASE, "aula-2", "Dois", "Segunda"), "aula-2", "Dois novo", "Nova")
    assert r.count('href="/apresentacao/aula-2/"') == 1 and "Dois novo" in r and "Apresentação 2" in r


def test_copiar_pacote_renomeia_e_tira_lixo(tmp_path):
    p = tmp_path / "pacote"
    (p / "midia").mkdir(parents=True)
    (p / "fontes").mkdir()
    for n in ("apresentacao.html", "LEIA-ME.txt", "._x", "midia/a.svg"):
        (p / n).write_text("x")
    d = tmp_path / "site" / "aula-9"
    copiar_pacote(p, d)
    assert sorted(f.name for f in d.iterdir()) == ["index.html", "midia"]
