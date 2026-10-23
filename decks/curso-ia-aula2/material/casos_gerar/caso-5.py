"""Gera os autos fictícios do caso 5 da Aula 2 (atomoxetina, TDAH). Texto reescrito; nomes, números e lugares inventados.
Uso: python3 caso-5.py [pasta_de_saida]  (padrão: kit/casos/caso-5). Precisa de Chrome e PyMuPDF."""
import subprocess, pathlib, sys, tempfile
import pymupdf as fitz

AQUI = pathlib.Path(__file__).resolve().parent
SAIDA = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else AQUI.parent.parent / "kit" / "casos" / "caso-5"
TMP = pathlib.Path(tempfile.gettempdir()) / "casos_gerar_caso5"; TMP.mkdir(parents=True, exist_ok=True)
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PROC = "0804417-39.2026.8.12.0099"

CSS = """
@page { size: A4; margin: 26mm 20mm 22mm 20mm; }
body { font: 11pt/1.45 Georgia, 'Times New Roman', serif; color: #1a1a1a; }
h1 { font-size: 13.5pt; text-align: center; margin: 0 0 3pt; letter-spacing: .02em; }
h2 { font-size: 10.5pt; text-align: center; margin: 0 0 14pt; font-weight: normal; }
h3 { font-size: 11pt; margin: 12pt 0 6pt; break-after: avoid; page-break-after: avoid; }
table, tr { break-inside: avoid; }
p { margin: 0 0 8pt; text-align: justify; }
.inst { text-align: center; font-size: 10pt; margin-bottom: 12pt; line-height: 1.35; }
.ass { margin-top: 26pt; text-align: center; font-size: 10.5pt; }
.ass span { display: inline-block; border-top: 1px solid #333; padding-top: 3pt; min-width: 230pt; }
table { border-collapse: collapse; width: 100%; margin: 4pt 0 10pt; font-size: 10.5pt; }
td, th { border: 1px solid #777; padding: 4pt 6pt; vertical-align: top; text-align: left; }
th { background: #eee; }
.campo { font-weight: bold; width: 38%; }
.quebra { page-break-before: always; }
.nota { font-size: 9.5pt; color: #444; }
.recuo { padding-left: 30pt; }
"""

def pagina(corpo):
    return f"<!doctype html><meta charset='utf-8'><style>{CSS}</style>{corpo}"

def gerar(nome, corpo):
    h = TMP / f"{nome}.html"
    h.write_text(pagina(corpo), encoding="utf-8")
    bruto = TMP / f"{nome}-bruto.pdf"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={bruto}", h.as_uri()], check=True, capture_output=True)
    d = fitz.open(bruto)
    n = len(d)
    for i, pg in enumerate(d):
        w = pg.rect.width
        pg.insert_textbox(fitz.Rect(40, 22, w - 40, 40), f"Autos fictícios, material didático  |  Processo {PROC} (fictício)",
                          fontsize=8, fontname="helv", color=(0.35, 0.35, 0.35), align=1)
        pg.draw_line(fitz.Point(56, 42), fitz.Point(w - 56, 42), color=(0.6, 0.6, 0.6), width=0.5)
        pg.insert_textbox(fitz.Rect(40, pg.rect.height - 38, w - 40, pg.rect.height - 22), f"Página {i+1} de {n}",
                          fontsize=8, fontname="helv", color=(0.35, 0.35, 0.35), align=1)
    d.save(SAIDA / f"{nome}.pdf")
    print(nome, n, "pág.")

DPE = "<div class='inst'><b>DEFENSORIA PÚBLICA DO ESTADO DE MATO GROSSO DO SUL</b><br>Defensoria Pública da Comarca de Serra Clara</div>"

INICIAL = DPE + """
<p><b>AO JUÍZO DA VARA ÚNICA DA COMARCA DE VILA BOA ESPERANÇA/MS</b></p>
<p><b>GABRIEL NUNES FERRAZ</b>, brasileiro, criança em idade escolar, representado por sua mãe, <b>MARIANA NUNES FERRAZ</b>, brasileira, solteira, trabalhadora da indústria, residente no Município de Santa Aurora/MS, por meio da DEFENSORIA PÚBLICA DO ESTADO DE MATO GROSSO DO SUL, com fundamento nos arts. 1º, III, 5º, 6º e 196 da Constituição Federal, no art. 173 da Constituição do Estado de Mato Grosso do Sul e na Lei nº 8.080/1990, propõe <b>AÇÃO DE OBRIGAÇÃO DE FAZER COM PEDIDO DE TUTELA DE URGÊNCIA</b> contra o <b>ESTADO DE MATO GROSSO DO SUL</b>, representado pela Procuradoria-Geral do Estado, e o <b>MUNICÍPIO DE SANTA AURORA/MS</b>, representado pelo Prefeito ou pelo Procurador do Município, pelos fatos e fundamentos a seguir.</p>
<h3>I. DOS FATOS</h3>
<p>O autor tem Transtorno de Déficit de Atenção e Hiperatividade (TDAH), CID F90.2, conforme relatório da Dra. Helena Campos Viana (CRM/MS 0000), e precisa usar de forma contínua o medicamento cloridrato de atomoxetina 40 mg, conforme o receituário e o questionário médico que acompanham esta inicial.</p>
<p>A doença provoca diversos efeitos e, sem a medicação, há risco de agravamento do quadro e de descontrole da comorbidade, como afirmou a médica que o acompanha.</p>
<p>O medicamento é inacessível à família em razão do alto custo, em torno de R$ 130,00 (cento e trinta reais) por mês, conforme os orçamentos anexos, e a família não tem condições de custear o tratamento.</p>
<p>Foi feito requerimento à Secretaria de Saúde do Município de Santa Aurora, que negou o medicamento ao autor, conforme documento anexo. Não resta alternativa senão buscar o Poder Judiciário para que os réus forneçam o medicamento ou, não sendo possível pela rede pública, custeiem o tratamento na rede particular.</p>
<h3>II. DO DIREITO</h3>
<p>A saúde é direito de todos e dever do Estado (arts. 6º e 196 da Constituição Federal). A Lei nº 8.080/1990 inclui no campo de atuação do SUS a assistência terapêutica integral, inclusive farmacêutica (art. 6º, I, "d"), e consagra a integralidade da assistência (art. 7º, II). A Constituição Estadual repete a garantia nos arts. 173 a 175.</p>
<p>A obrigação dos entes federados é solidária, de modo que o cidadão pode demandar qualquer deles, isolada ou conjuntamente, como reconhece o Superior Tribunal de Justiça (AgRg no AREsp 420.563/PR, Segunda Turma).</p>
<h3>III. DA TUTELA DE URGÊNCIA</h3>
<p>A probabilidade do direito está nos fundamentos jurídicos e nos documentos médicos, que não deixam dúvida sobre a doença e a necessidade do medicamento. O perigo de dano decorre do próprio quadro clínico, que se prolonga e se agrava com a demora (arts. 297 e 300 do CPC).</p>
<h3>IV. DOS PEDIDOS</h3>
<p>Requer: (a) os benefícios da assistência judiciária gratuita, por ser o autor assistido pela Defensoria Pública (LC Federal nº 80/1994, LC Estadual nº 111/2005 e art. 98, § 1º, do CPC); (b) a tutela provisória de urgência, sem ouvir a parte contrária, para que os réus forneçam o cloridrato de atomoxetina 40 mg; (c) prazo razoável para cumprimento, sob pena de multa diária (arts. 536, § 1º, e 537 do CPC); (d) em caso de descumprimento, o sequestro de verbas públicas suficientes para o custeio do tratamento na rede privada; (e) a citação dos réus; (f) a procedência do pedido, confirmando a tutela, para condenar os réus a fornecer o cloridrato de atomoxetina 40 mg; (g) honorários de sucumbência em favor do fundo da Defensoria Pública; (h) a observância das prerrogativas da Defensoria Pública, inclusive intimação pessoal e prazo em dobro.</p>
<p>Protesta por todos os meios de prova admitidos. Dá à causa o valor de R$ 1.560,00 (mil quinhentos e sessenta reais).</p>
<p>Vila Boa Esperança/MS, data da assinatura digital.</p>
<div class="ass"><span>Marcelo Antunes Prado<br>Defensor Público (assinado digitalmente)</span></div>
"""

PREF = "<div class='inst'><b>PREFEITURA MUNICIPAL DE SANTA AURORA</b><br>Secretaria Municipal de Saúde</div>"

RELATORIO = PREF + """
<h1>LAUDO MÉDICO</h1>
<h2>Emitido em folha de receituário da Secretaria Municipal de Saúde</h2>
<p>Atesto, para os devidos fins, que a criança Gabriel Nunes Ferraz apresenta agitação motora acentuada, dificuldade de concentração, principalmente nas atividades escolares, hiperatividade e impulsividade. Foi encaminhada para atendimento com neuropsicóloga, que, por meio dos testes necessários, confirmou o diagnóstico de TDAH, CID F90.2.</p>
<p>Santa Aurora, 08/05/2026.</p>
<div class="ass"><span>Dra. Helena Campos Viana<br>Médica, CRM/MS 0000</span></div>
"""

RECEITA = PREF + """
<h1>RECEITUÁRIO</h1>
<h2>&nbsp;</h2>
<p><b>Nome:</b> Gabriel Nunes Ferraz</p>
<p class="recuo">Atentah 40 mg<br>Genérico: cloridrato de atomoxetina 40 mg ........ 30<br>Tomar 1 cápsula de manhã.</p>
<p>Data: 08/05/2026.</p>
<div class="ass"><span>Dra. Helena Campos Viana<br>Médica, CRM/MS 0000</span></div>
"""

def linha(c, v):
    return f"<tr><td class='campo'>{c}</td><td>{v}</td></tr>"

LAUDO = """
<div class='inst'><b>DEFENSORIA PÚBLICA DO ESTADO DE MATO GROSSO DO SUL</b><br>Núcleo de Atenção à Saúde (NAS)</div>
<h1>LAUDO MÉDICO PARA AÇÃO JUDICIAL</h1>
<h2>Solicitação de medicamento não padronizado (formulário preenchido à mão pela médica assistente)</h2>
<h3>Dados do paciente e da prescritora</h3>
<table>""" + "".join([
    linha("Paciente", "Gabriel Nunes Ferraz"),
    linha("CPF / Cartão SUS", "em branco"),
    linha("Médica prescritora", "Dra. Helena Campos Viana, CRM/MS 0000"),
]) + """</table>
<h3>Descrição do medicamento</h3>
<table>""" + "".join([
    linha("CID (código e extenso)", "CID F90.2"),
    linha("Princípio ativo", "Cloridrato de atomoxetina 40 mg"),
    linha("Apresentação / concentração", "Cápsulas de 40 mg"),
    linha("Via de administração", "Oral"),
    linha("Necessita procedimento médico-hospitalar?", "( ) Sim ( ) Não (X) Não se aplica"),
    linha("Posologia", "1 cápsula, uma vez ao dia, via oral"),
    linha("Forma de utilização", "(X) uso contínuo, sem pausa ( ) em ciclos"),
    linha("Duração do tratamento", "(X) indeterminada ( ) determinada"),
    linha("Registrado na ANVISA?", "(X) Sim ( ) Não"),
    linha("Indicação conforme a bula (CID previsto)?", "(X) Sim ( ) Não"),
    linha("Se uso off-label, evidências", "em branco"),
    linha("Previsto em Protocolo Clínico e Diretrizes Terapêuticas do Ministério da Saúde para a situação clínica?", "(X) Sim ( ) Não"),
]) + """</table>
<p class="nota quebra">Texto impresso no formulário: "Conforme decisão do STF no Tema 1234, tratando-se de medicamento não incorporado ao SUS, é do autor da ação o ônus de demonstrar, com fundamento na Medicina Baseada em Evidências, a segurança e a eficácia do fármaco, bem como a inexistência de substituto terapêutico incorporado ao SUS. Cite ou anexe as evidências que demonstram que a opinião do médico para esta prescrição encontra respaldo em evidências científicas de alto nível (ensaios clínicos randomizados, revisão sistemática ou meta-análise)."</p>
<table>""" + linha("Resposta da médica", "\"Estudos científicos têm demonstrado que o cloridrato de atomoxetina age de forma constante, auxiliando na melhora do foco, da concentração e no controle de impulsos. Indicado para crianças, adolescentes e adultos com desatenção e hiperatividade.\"<br><i>(Nenhum estudo citado nem anexado.)</i>") + """</table>
<h3>Histórico e situação atual do paciente</h3>
<table>""" + "".join([
    linha("Está sendo atendido no SUS?", "(X) Sim ( ) Não"),
    linha("Forma de elaboração do diagnóstico (exame clínico e exames complementares, anexando os relevantes)", "\"Avaliado por médicos clínicos e avaliado por médica neuropsicóloga, onde realizou todos os testes necessários para diagnóstico. Confirmou a neuropsicóloga que a criança é portadora de TDAH, CID F90.2.\"<br><i>(Nenhum exame ou teste anexado.)</i>"),
    linha("Histórico da doença e situação clínica atual", "\"Há cerca de 2 anos a mãe da criança foi chamada na escola, onde foi comunicada que o menor tinha muita dificuldade de se concentrar e também de aprendizado.\""),
    linha("Histórico dos tratamentos (medicamentos, tempo de uso, doses, efeitos e motivo da substituição)", "\"A criança permaneceu em observação na escola e em casa devido ao comportamento: ansiedade, controle de impulsos. Iniciou com medicação carbamazepina (SUS), biperideno 2,0 mg. Sem melhora no quadro clínico.\""),
    linha("Tratamentos disponíveis no SUS para a patologia que não foram utilizados, e por quê", "\"Não existe medicação do SUS para substituir a medicação necessária (cloridrato de atomoxetina) para tratamento da criança.\""),
]) + """</table>
<table>""" + "".join([
    linha("O paciente já usa o medicamento?", "( ) Sim (X) Não. \"Ainda não está em uso da medicação devido à situação econômica, informa a mãe da criança.\""),
    linha("Outras comorbidades e tratamentos em uso", "\"A criança, no momento, não apresenta outras comorbidades.\""),
    linha("Justifica-se a alegação de urgência?", "(X) Sim. \"É necessária a urgência na liberação do medicamento devido à falta de atenção, dificuldade de aprendizado, hiperatividade e impaciência, causando prejuízo para o sucesso escolar da criança.\""),
    linha("Benefício / resultado esperado", "\"Comprovado cientificamente que o uso desta medicação melhora o comportamento dos portadores de TDAH; esperamos que a criança venha a se beneficiar e apresentar melhoras de todos os sintomas que ora atrapalham o aprendizado do menor.\""),
]) + """</table>
<p>Data: 08/05/2026.</p>
<div class="ass"><span>Dra. Helena Campos Viana<br>Médica, CRM/MS 0000</span></div>
"""

NEGATIVA = PREF + """
<p style="display:flex;justify-content:space-between"><b>OFÍCIO Nº 41/2026/SMS</b><b>Santa Aurora, 10 de maio de 2026.</b></p>
<p>À Sua Senhoria<br><b>Gabriel Nunes Ferraz</b></p>
<p>Prezado Senhor,</p>
<p>Em resposta ao requerimento enviado a esta Secretaria Municipal de Saúde em 04/04/2026, solicitando o fornecimento do medicamento <b>cloridrato de atomoxetina 40 mg</b>, informo que este medicamento não está presente nos itens básicos da RENAME e que, dessa forma, não podemos disponibilizá-lo.</p>
<p>Atenciosamente,</p>
<div class="ass"><span>Joaquim Pereira Matos<br>Secretário Municipal de Saúde</span></div>
<div class="quebra"></div>
<h1 style="margin-top:40pt">REQUERIMENTO</h1>
<h2>&nbsp;</h2>
<p><b>EU, GABRIEL NUNES FERRAZ, VENHO POR MEIO DESTE SOLICITAR A ESTA SECRETARIA MUNICIPAL DE SAÚDE O SEGUINTE MEDICAMENTO: CLORIDRATO DE ATOMOXETINA 40 MG.</b></p>
<p style="text-align:right"><b>SANTA AURORA/MS, 10 DE MAIO DE 2026.</b></p>
<div class="ass" style="margin-top:60pt"><span>Assinatura: Mariana Nunes Ferraz</span></div>
<p class="nota" style="margin-top:30pt">Folha sem número de protocolo, carimbo ou registro de recebimento.</p>
"""

def holerite(comp, pag, itens, desc, bruto, liquido):
    linhas = "".join(f"<tr><td>{a}</td><td style='text-align:right'>{b}</td></tr>" for a, b in itens)
    return f"""<h3>Demonstrativo de pagamento, competência {comp} (pago em {pag})</h3>
<table><tr><th>Rubrica</th><th style='text-align:right'>Valor</th></tr>{linhas}
<tr><td>Total de descontos</td><td style='text-align:right'>({desc})</td></tr>
<tr><td><b>Total bruto</b></td><td style='text-align:right'><b>{bruto}</b></td></tr>
<tr><td><b>Valor líquido a receber</b></td><td style='text-align:right'><b>{liquido}</b></td></tr></table>"""

RENDA = """
<div class='inst'><b>DEFENSORIA PÚBLICA DO ESTADO DE MATO GROSSO DO SUL</b></div>
<h1>DECLARAÇÃO</h1>
<h2>Para assistência jurídica integral e gratuita</h2>
<p>Eu, Mariana Nunes Ferraz, brasileira, solteira, trabalhadora da indústria, residente no Município de Santa Aurora/MS, DECLARO, para receber assistência jurídica integral e gratuita da Defensoria Pública de Mato Grosso do Sul, não dispor de recursos financeiros que me permitam suportar as despesas processuais e o pagamento de honorários advocatícios sem prejuízo do próprio sustento ou da família.</p>
<p>Declaro estar ciente de que estou sujeita à multa de até 10 (dez) vezes o valor das despesas processuais caso seja constatada falsidade nesta declaração, bem como do disposto no art. 299 do Código Penal. Autorizo a Defensoria Pública a requisitar informações para análise e instrução processual, comprometo-me a guardar os documentos originais e a manter atualizado meu cadastro, e estou ciente de que a ausência injustificada às audiências pode acarretar multa (art. 334, § 8º, do CPC).</p>
<p>Vila Boa Esperança/MS, 15 de maio de 2026.</p>
<div class="ass"><span>Mariana Nunes Ferraz<br>Declarante</span></div>
<div class="quebra"></div>
<h1>CONTRACHEQUES DA MÃE DO AUTOR</h1>
<h2>Empregadora: Indústria de Alimentos Serra Clara Ltda. Salário base: R$ 2.126,00. Dependentes declarados: 2.</h2>
""" + holerite("01/2026", "09/02/2026", [("Horas normais", "R$ 1.955,92"), ("Prêmio de produção", "R$ 523,64"), ("Insalubridade", "R$ 324,20"), ("Horas de atestado até 15 dias", "R$ 170,08"), ("Outros adicionais", "R$ 35,82"), ("Desconto de empréstimo consignado", "(R$ 744,00)"), ("INSS", "(R$ 249,74)"), ("Contribuição assistencial e alimentação", "(R$ 50,00)")], "R$ 1.043,74", "R$ 3.009,66", "R$ 1.965,92") \
  + holerite("02/2026", "12/03/2026", [("Horas normais", "R$ 2.126,00"), ("Prêmios de produção e de meta", "R$ 1.275,66"), ("Insalubridade", "R$ 324,20"), ("Prêmio de permanência", "R$ 21,26"), ("Descontos de empréstimo consignado", "(R$ 776,00)"), ("INSS", "(R$ 260,19)"), ("Contribuição assistencial e alimentação", "(R$ 50,00)")], "R$ 1.086,19", "R$ 3.747,12", "R$ 2.660,93") \
  + holerite("03/2026", "10/04/2026", [("Horas normais", "R$ 1.667,46"), ("Prêmio de produção", "R$ 467,59"), ("Horas de atestado até 15 dias", "R$ 458,54"), ("Insalubridade", "R$ 324,20"), ("Horas extras e outros adicionais", "R$ 153,49"), ("Descontos de empréstimo consignado", "(R$ 776,00)"), ("INSS", "(R$ 257,14)"), ("Contribuição assistencial e alimentação", "(R$ 50,00)")], "R$ 1.083,14", "R$ 3.071,28", "R$ 1.988,14") + """
<div class="quebra"></div>
<h1>ORÇAMENTOS DO MEDICAMENTO</h1>
<h2>Três documentos auxiliares de venda, emitidos em 07/05/2026, todos com a observação "orçamento para 6 meses"; nenhum é documento fiscal</h2>
<table>
<tr><th>Estabelecimento</th><th>Produto</th><th>Valor unitário</th><th>Qtde.</th><th>Total</th></tr>
<tr><td>Farmácia Aurora Centro Ltda., orçamento 1</td><td>Atentah 40 mg, caixa com 30 cápsulas</td><td>R$ 135,97</td><td>6</td><td>R$ 815,82, com desconto de R$ 83,82: total R$ 732,00</td></tr>
<tr><td>Drogaria Santa Aurora</td><td>Atentah 40 mg, caixa com 30 cápsulas</td><td>R$ 130,00</td><td>6</td><td>R$ 780,00</td></tr>
<tr><td>Farmácia Aurora Centro Ltda., orçamento 2 (outra loja)</td><td>Atentah 40 mg, caixa com 30 cápsulas</td><td>R$ 135,90</td><td>6</td><td>R$ 815,40</td></tr>
</table>
"""

NATJUS = """
<div class='inst'><b>TRIBUNAL DE JUSTIÇA DO ESTADO DE MATO GROSSO DO SUL</b><br>Núcleo de Apoio Técnico do Judiciário (NATJus)</div>
<h1>NOTA TÉCNICA DO NATJUS Nº 3518/2026</h1>
<h2>Autos: """ + PROC + """ (fictício). Procedimento Comum Cível, Vara Única de Vila Boa Esperança.<br>Requerente: Gabriel Nunes Ferraz. Requeridos: Estado de Mato Grosso do Sul e Município de Santa Aurora.</h2>
<h3>I. Enfermidade e linha terapêutica do SUS</h3>
<p>Segundo o laudo e os demais documentos, o requerente é criança em idade escolar (entre 6 e 10 anos) com Transtorno do Déficit de Atenção com Hiperatividade (CID 10: F90.2). Os documentos descrevem agitação motora acentuada, hiperatividade, impulsividade e dificuldade de concentração, com prejuízo no desempenho escolar, há cerca de dois anos. Não foram apresentados resultados de exames complementares.</p>
<table><tr><th>Princípio ativo</th><th>Posologia</th><th>Incorporado ao SUS?</th></tr><tr><td>Atomoxetina (Atentah)</td><td>40 mg, 1 comprimido ao dia</td><td>NÃO</td></tr></table>
<p>O diagnóstico de TDAH exige avaliação clínica por profissionais capacitados, segundo critérios operacionais, porque os sintomas se confundem com outras condições e com características normais do desenvolvimento (Protocolo Clínico e Diretrizes Terapêuticas do TDAH, Portaria Conjunta SAES/SCTIE/MS nº 14, de 29/07/2022).</p>
<h3>II. Tratamentos realizados e alternativas</h3>
<p>Segundo os documentos médicos e o questionário da Defensoria Pública, o paciente já usou carbamazepina e biperideno, sem melhora do quadro.</p>
<p>O TDAH pede intervenção multimodal, incluindo medidas não medicamentosas (intervenções cognitivas e comportamentais, com destaque para a Terapia Cognitivo-Comportamental). Quanto aos psicoestimulantes, a Conitec avaliou metilfenidato e lisdexanfetamina para crianças e adolescentes com TDAH e recomendou a não incorporação, por evidências de baixa ou muito baixa qualidade e elevado impacto orçamentário; avaliou também a lisdexanfetamina para adultos, igualmente com recomendação desfavorável. Por isso esses medicamentos não são preconizados no PCDT.</p>
<h3>III. O medicamento solicitado</h3>
<p>Atentah (cloridrato de atomoxetina) é inibidor seletivo da recaptação da norepinefrina, indicado para TDAH em adultos, adolescentes e crianças com mais de 6 anos. Entre as reações adversas relatadas estão ansiedade, agitação, insônia, irritabilidade, agressividade, impulsividade e acatisia (bula do Atentah, Apsen Farmacêutica, 2023).</p>
<h3>IV. Classe e registro na ANVISA</h3>
<table><tr><th>Medicamento</th><th>Classe terapêutica</th><th>Registro na ANVISA</th><th>Situação</th></tr><tr><td>Atomoxetina</td><td>Outros produtos que atuam sobre o sistema nervoso</td><td>Sim</td><td>Ativo</td></tr></table>
<h3>V a VIII. Risco, atendimento e oferta no SUS</h3>
<p>Não há dados clínicos que indiquem risco iminente à vida. O paciente está sendo atendido pela rede pública de saúde. A atomoxetina não está incorporada na RENAME 2024 nem em outro ato normativo do SUS para o CID apresentado, razão pela qual não é possível indicar o ente responsável. Não há em tramitação solicitação de avaliação da atomoxetina, segundo a consulta pública a que este Núcleo tem acesso (página de tecnologias em avaliação da Conitec).</p>
<h3>IX. Alternativas no SUS</h3>
<p>A Política Nacional de Saúde Mental (Lei nº 10.216/2001) organiza a atenção em rede comunitária, com os Centros de Atenção Psicossocial (CAPS). O PCDT do TDAH (Portaria Conjunta SAES/SCTIE/MS nº 14/2022) indica o tratamento preconizado pelo SUS. A RENAME 2024 padroniza no Componente Básico da Assistência Farmacêutica anticonvulsivantes (carbamazepina, fenitoína, fenobarbital, valproato de sódio), antidepressivos (amitriptilina, clomipramina, nortriptilina, fluoxetina), antipsicóticos (clorpromazina, haloperidol) e ansiolíticos (clonazepam, diazepam).</p>
<h3>X. Genérico e preço</h3>
<p>A atomoxetina tem genérico e similar. Preço no Painel CMED/ANVISA, alíquota de 17%, consultado em 17/05/2026: ATENTAH (Apsen Farmacêutica S/A) 40 mg, caixa com 30 cápsulas. PF: R$ 103,96; PMC: R$ 138,57; PMVG: R$ 81,58.</p>
<h3>XI. Conclusão</h3>
<p>O paciente é atendido pela rede pública e não há risco iminente à vida; a atomoxetina não está incorporada na RENAME 2024 nem em outro ato normativo do SUS para o CID; não há pedido de avaliação em tramitação na Conitec; o PCDT do TDAH indica o tratamento do SUS e a RENAME 2024 padroniza os medicamentos listados acima. O fornecimento de medicamento não incorporado deve observar eficácia, segurança, custo-efetividade e impacto orçamentário (Temas 6 e 1.234 do STF), e não foram apresentadas evidências científicas robustas, como ensaios clínicos randomizados, meta-análises ou revisões sistemáticas, necessárias à avaliação da tecnologia pleiteada. Este Núcleo manifesta-se <b>desfavorável</b> ao pedido de atomoxetina.</p>
<p>17 de maio de 2026.</p>
<div class="ass"><span>Equipe técnica do NATJus (médicos, enfermeiros e farmacêuticos)<br>assinado por certificação digital</span></div>
"""

DECISAO = """
<div class='inst'><b>PODER JUDICIÁRIO DO ESTADO DE MATO GROSSO DO SUL</b><br>Comarca de Vila Boa Esperança, Vara Única</div>
<h1>DECISÃO</h1>
<h2>Autos: """ + PROC + """ (fictício). Procedimento Comum Cível, fornecimento de medicamentos.<br>Autor: Gabriel Nunes Ferraz. Réus: Município de Santa Aurora e outro.</h2>
<p>Vistos etc.</p>
<p>Gabriel Nunes Ferraz propôs ação com pedido de tutela antecipada contra o Estado de Mato Grosso do Sul e o Município de Santa Aurora, alegando ter TDAH (CID F90.2), conforme relatório da Dra. Helena Campos Viana, e necessitar do uso contínuo de cloridrato de atomoxetina 40 mg. Com a inicial veio a prescrição médica. Antes da análise da tutela, os autos foram ao Núcleo de Apoio Técnico do Judiciário, que emitiu parecer desfavorável. É o relatório. Decido.</p>
<p>A tutela de urgência exige probabilidade do direito e perigo de dano ou risco ao resultado útil do processo (art. 300 do CPC). O direito à saúde é reconhecido em normas internacionais e, no plano interno, no art. 196 da Constituição, com responsabilidade solidária dos entes e inclusão da assistência farmacêutica (art. 6º, I, "d", da Lei nº 8.080/1990). O sistema, porém, previu procedimentos técnicos, científicos, econômicos e operacionais para admitir um tratamento na rede pública, que não foram observados quanto ao fármaco pretendido, pois ele não está incorporado ao SUS. Os Tribunais Superiores enfrentaram o tema nos Temas 793 e 500 do STF e 686 do STJ.</p>
<p>No Tema 1.234, o STF definiu o que são medicamentos não incorporados: os que não estão no SUS, os fora da lista do componente básico, os de uso off-label sem protocolo, os sem registro na ANVISA e os fornecidos para finalidade diversa da prevista nos protocolos. No caso, o NAT emitiu parecer desfavorável conclusivo.</p>
<p>No Tema 6, o STF fixou a regra geral de que a ausência do medicamento nas listas oficiais do SUS (RENAME, RESME, REMUME) impede, em princípio, seu fornecimento por decisão judicial, independentemente do custo, em respeito às políticas públicas e às dificuldades do gestor (art. 21 e seguintes da LINDB).</p>
<p>No caso concreto, o paciente é atendido pelo SUS, o medicamento está registrado na ANVISA, mas não está padronizado em ato normativo do SUS, havendo vários outros medicamentos disponíveis no SUS para o tratamento da doença do autor. Corroborado pelo parecer do NAT, impõe-se o indeferimento da tutela, pois o autor não preencheu os requisitos cumulativos fixados pelo STF no Tema 1.234 para a concessão excepcional de medicamento registrado na ANVISA e não incorporado ao SUS.</p>
<p><b>Dispositivo.</b> Ausentes os requisitos do art. 300 do CPC, <b>indefiro</b> a tutela de urgência. Defiro os benefícios da justiça gratuita. Citem-se os réus. Depois, intime-se o autor para réplica em 15 dias e, em seguida, as partes para indicarem o ponto controvertido e as provas que pretendem produzir, cientes de que o silêncio importará julgamento antecipado. Cópia desta decisão serve de mandado e ofício.</p>
<p>Vila Boa Esperança, data da assinatura digital.</p>
<div class="ass"><span>Renata Figueiredo Lins<br>Juíza de Direito (assinado por certificação digital)</span></div>
"""

DOCS = [
    ("01-peticao-inicial", INICIAL),
    ("02-relatorio-medico", RELATORIO),
    ("03-receita", RECEITA),
    ("04-laudo-defensoria", LAUDO),
    ("05-pedido-e-negativa-administrativa", NEGATIVA),
    ("06-hipossuficiencia-e-orcamentos", RENDA),
    ("07-nota-tecnica-natjus", NATJUS),
    ("08-decisao-tutela", DECISAO),
]

if __name__ == "__main__":
    SAIDA.mkdir(parents=True, exist_ok=True)
    for nome, corpo in DOCS:
        gerar(nome, corpo)
