"""Gera os autos fictícios do caso 4 da aula 2 (PDFs e gabarito.json) em kit/casos/caso-4/.
Todo o texto é fictício; nomes, números, lugares e datas são inventados. Uso: python3 caso-4.py (precisa do Chrome)."""
import json, pathlib, subprocess, tempfile

AQUI = pathlib.Path(__file__).resolve().parent
SAIDA = AQUI.parent.parent / "kit" / "casos" / "caso-4"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PROC = "0999904-04.2026.8.12.0999"
PRE = "0999903-07.2025.8.12.0999"

CSS = """
@page { size: A4; margin: 24mm 20mm 20mm 20mm;
  @top-center { content: "Autos fictícios, material didático"; font: 9pt Georgia, serif; color: #666; }
  @bottom-center { content: "Página " counter(page) " de " counter(pages); font: 9pt Georgia, serif; color: #666; } }
body { font: 11.5pt/1.5 Georgia, 'Times New Roman', serif; color: #1a1a1a; }
h1 { font-size: 13.5pt; text-align: center; margin: 0 0 4pt; }
h2 { font-size: 11pt; text-align: center; margin: 0 0 14pt; font-weight: normal; }
h3 { font-size: 11pt; margin: 12pt 0 5pt; break-after: avoid; }
.ass { break-inside: avoid; }
p { margin: 0 0 8pt; text-align: justify; }
.cab { text-align: center; font-size: 10pt; margin-bottom: 12pt; line-height: 1.35; }
.ass { margin-top: 22pt; text-align: center; font-size: 10.5pt; line-height: 1.35; }
.dados { font-size: 10.5pt; margin-bottom: 12pt; line-height: 1.4; }
table { border-collapse: collapse; width: 100%; font-size: 10.5pt; margin: 4pt 0 10pt; }
td, th { border: 1px solid #999; padding: 3pt 6pt; text-align: left; vertical-align: top; }
th { background: #eee; }
td + td { white-space: nowrap; }
.quebra { break-before: page; }
.nota { font-size: 9.5pt; color: #444; }
ul { margin: 0 0 8pt 18pt; padding: 0; } li { margin-bottom: 3pt; }
"""

def doc(corpo):
    return f"<!doctype html><meta charset='utf-8'><style>{CSS}</style>{corpo}"

INICIAL = f"""
<p><b>EXCELENTÍSSIMO SENHOR DOUTOR JUIZ DE DIREITO DA VARA CÍVEL DA COMARCA DE SERRA DOURADA, MS</b></p>
<p><b>MARISA HELENA DUARTE LOBO</b>, brasileira, servidora municipal aposentada, CPF fictício 000.000.000-00, residente em Serra Dourada, MS, por suas advogadas (procuração anexa), propõe <b>AÇÃO DE OBRIGAÇÃO DE FAZER COM PEDIDO DE FORNECIMENTO DE MEDICAMENTO E TUTELA DE URGÊNCIA</b> em face do <b>MUNICÍPIO DE SERRA DOURADA</b> e do <b>ESTADO DE SERRA DOURADA</b>, pessoas jurídicas de direito público, pelos fatos e fundamentos a seguir.</p>

<h3>I. Preliminarmente</h3>
<p><b>I.a. Justiça gratuita.</b> A autora declara-se hipossuficiente. É aposentada e recebe renda líquida de R$ 3.355,01, integralmente consumida por moradia, alimentação, saúde e medicamentos. Responde ainda a processo de superendividamento (autos nº 0999902-10.2025.8.12.0999, 8ª Vara Cível desta comarca), o que mostra o comprometimento de sua renda. Junta declaração de hipossuficiência.</p>
<p><b>I.b. Tutela de urgência.</b> Estão presentes a probabilidade do direito e o perigo de dano (art. 300 do CPC). Segundo o médico assistente, o uso de agonista de GLP-1 "é especialmente recomendado em pacientes com excesso de peso e risco cardiovascular aumentado", e o uso é crônico e por tempo indefinido.</p>
<p>A autora usou insulina por muitos anos, medicamento disponível na rede pública. Porém, conforme o laudo anexo, <b>o tratamento com insulina foi SUSPENSO devido a episódios GRAVES de hipoglicemia</b> (desmaios e perda da consciência), o que demonstra que as alternativas disponíveis no SUS não são adequadas ao seu caso e que ela corre risco de morte ou de acidentes graves. O diabetes grave pode causar danos aos rins, olhos, coração e nervos, com risco de cegueira, insuficiência renal, infarto, AVC e amputação.</p>

<h3>II. Dos fatos</h3>
<p>A autora tem Diabetes Mellitus tipo 2, doença crônica que exige tratamento contínuo. Conforme laudo e receita anexos, foi-lhe prescrito <b>OZEMPIC (semaglutida) 1 mg, de uso semanal</b>, como tratamento essencial.</p>
<p>A prescrição decorre da ineficácia e dos riscos do tratamento anterior com insulina, suspenso porque a autora apresentava desmaios constantes, tontura, visão embaçada e dor de cabeça intensa.</p>
<p>O medicamento é de alto custo, com valor aproximado de <b>R$ 1.000,00 (mil reais) por caneta, sendo utilizado semanalmente</b>, gasto incompatível com a renda líquida mensal da autora, de R$ 3.355,01 (comprovante anexo). Suas despesas fixas mensais, conforme comprovantes anexos, são as seguintes.</p>
<table><tr><th>Despesa</th><th>Valor mensal</th></tr>
<tr><td>Água</td><td>R$ 155,71</td></tr><tr><td>Energia elétrica</td><td>R$ 224,17</td></tr>
<tr><td>Internet</td><td>R$ 89,90</td></tr><tr><td>Alimentação</td><td>R$ 800,00</td></tr>
<tr><td>Telefone</td><td>R$ 42,13</td></tr><tr><td>Aluguel</td><td>R$ 900,00</td></tr>
<tr><td>Cartão de crédito</td><td>R$ 1.316,92</td></tr><tr><td>Outros medicamentos</td><td>R$ 269,56</td></tr>
<tr><th>Total</th><th>R$ 3.797,47</th></tr></table>
<p>Sem condições de custear o tratamento, a autora buscou o medicamento na via administrativa. Pediu-o primeiro ao Município, que negou o fornecimento porque o Ozempic (semaglutida) não integra a Lista de Componentes Básicos da Assistência Farmacêutica, informando sua indisponibilidade na rede municipal. Depois, buscou-o junto ao Estado, que também recusou, alegando que a semaglutida não está incorporada ao SUS e que os servidores estaduais não têm competência para fornecê-la. Não lhe restou alternativa senão o Poder Judiciário.</p>

<h3>III. Do direito</h3>
<p><b>III.a. Direito fundamental à saúde.</b> A saúde é direito de todos e dever do Estado (art. 196 da Constituição; arts. 2º e 6º, I, "d", da Lei nº 8.080/1990, que inclui a assistência terapêutica integral, inclusive farmacêutica). O Município é parte legítima, pois os entes respondem solidariamente, conforme o Tema 793 do STF (RE 855.178).</p>
<p><b>III.b. Medicamento não padronizado.</b> Embora a semaglutida não esteja incluída nas listas de medicamentos padronizados pelo SUS, o Judiciário pode determinar seu fornecimento quando presentes os requisitos do Tema 106 do STJ (REsp 1.657.156): laudo médico fundamentado sobre a imprescindibilidade do medicamento e a ineficácia dos fármacos do SUS; incapacidade financeira; registro na ANVISA. Todos os requisitos estão presentes, e o Tribunal de Justiça de Mato Grosso do Sul tem aplicado esse entendimento em agravos de instrumento.</p>
<p><b>III.c. Hipossuficiência e dignidade.</b> A hipossuficiência não se confunde com miserabilidade. Exigir que a autora custeie <b>medicamento de R$ 1.000,00 mensais</b>, diante de sua renda e de seus gastos essenciais, seria obrigá-la a escolher entre viver com dignidade ou com saúde (art. 1º, III, da Constituição).</p>

<h3>IV. Dos pedidos</h3>
<p>Requer: (a) a gratuidade da justiça (art. 98 do CPC); (b) a tutela de urgência, sem oitiva da parte contrária, para o fornecimento do medicamento; (c) a procedência, confirmando a tutela, para que os réus custeiem todo o tratamento até a alta médica definitiva; (d) multa diária em caso de descumprimento; (e) a condenação dos réus em custas e honorários de 20% sobre o valor atualizado da causa; (f) a citação dos réus. Protesta por todos os meios de prova.</p>
<p>Dá-se à causa o valor de <b>R$ 12.000,00 (doze mil reais)</b>.</p>
<p>Serra Dourada, MS, 8 de janeiro de 2026.</p>
<div class="ass">BEATRIZ LEMOS ARANTES, OAB/MS 90.111<br><br>CLÁUDIA RIBAS TEIXEIRA, OAB/MS 90.222<br><span class="nota">Arantes &amp; Teixeira Advocacia (escritório particular)</span></div>
"""

LAUDO = f"""
<div style="font-size:10.6pt;line-height:1.4">
<div class="cab"><b>SERVIÇO DE SAÚDE DO SERVIDOR MUNICIPAL DE SERRA DOURADA</b><br>Centro Médico do Servidor Municipal</div>
<h1>LAUDO MÉDICO</h1><h2>Endocrinologia e Metabologia</h2>
<p><b>Paciente:</b> Marisa Helena Duarte Lobo. Idade: faixa dos 40 anos. CID-10: E11, Diabetes mellitus tipo 2.</p>
<p><b>História clínica e evolução.</b> Diabetes Mellitus tipo 2 diagnosticado há cerca de quinze anos, em seguimento irregular. Em uso crônico de insulinoterapia (NPH e Regular), com episódios de hipoglicemia quando usa a insulina regular, o que levou à suspensão desta. Queixa atual de dificuldade para perder peso e controle glicêmico subótimo. Tem também fatores de risco cardiovascular, como o tabagismo.</p>
<p><b>Tratamento atual.</b> Insulina NPH 8-8-8 UI; Insulina Regular (suspensa devido a hipoglicemias); Metformina XR (Glifage XR) 500 mg 2-0-2; Clonazepam 20 gotas à noite; Amitriptilina 25 mg à noite; Omeprazol 20 mg/dia.</p>
<p><b>Exames laboratoriais recentes (01/06/2025).</b> Hemoglobina glicada 7,9%; glicemia de jejum 148 mg/dL; creatinina 0,79 mg/dL; colesterol total 201 mg/dL; LDL 82 mg/dL.</p>
<p><b>Exame físico.</b> Peso 77,1 kg; altura 1,59 m; IMC 30,5 kg/m² (obesidade grau I).</p>
<p><b>Justificativa clínica.</b> DM2 de longa data, obesidade, uso prévio de múltiplas doses de insulina e dificuldade de controle, além de hipoglicemias relacionadas à insulina regular. Mantém controle glicêmico inadequado (HbA1c 7,9%) e risco cardiovascular elevado por tabagismo, obesidade e tempo de doença.</p>
<p>A semaglutida (análoga de GLP-1), com os nomes comerciais Ozempic ou Wegovy de 1 mg, é indicada para auxiliar no controle glicêmico, na redução de peso e na diminuição do risco cardiovascular, conforme diretrizes da ADA (American Diabetes Association), da EASD (European Association for the Study of Diabetes) e da Sociedade Brasileira de Diabetes (SBD 2025). O uso é de 1 mg semanal, contínuo. Pelo histórico de diabetes e obesidade, o uso é crônico e por período indefinido.</p>
<p>O uso de agonista de GLP-1 é especialmente recomendado em pacientes com excesso de peso e risco cardiovascular aumentado, como neste caso. Evidências robustas (estudo SUSTAIN-6) demonstram benefício cardiovascular, além de melhora significativa no controle glicêmico e perda ponderal.</p>
<p><b>Conclusão.</b> Solicito avaliação para liberação de Semaglutida SC 1 mg semanal para esta paciente, como terapia adjuvante ao tratamento já instituído, visando melhorar o controle glicêmico, reduzir peso corporal e risco de complicações cardiovasculares e evitar hipoglicemias decorrentes do uso de insulina regular.</p>
<div class="ass">Serra Dourada, MS, 21 de agosto de 2025.<br><br>Dr. Henrique Salles Vidal<br>CRM/MS 90.333, RQE 90.334, Endocrinologia e Metabologia</div>
</div>

<div class="quebra"></div>
<div class="cab"><b>SERVIÇO DE SAÚDE DO SERVIDOR MUNICIPAL DE SERRA DOURADA</b><br>Centro Médico do Servidor Municipal</div>
<h1>ATESTADO MÉDICO</h1><h2>&nbsp;</h2>
<p><b>Nome:</b> Marisa Helena Duarte Lobo.</p>
<p>Atesto que a paciente faz acompanhamento clínico nesta unidade de saúde. É portadora de diabetes mellitus insulinodependente e está em tratamento de ansiedade, depressão e insônia há aproximadamente 15 anos, em uso regular das medicações prescritas. Mesmo assim, apresenta muitas vezes episódios de apreensão, angústia e crises de ansiedade, às vezes precisando de internação. Segue em acompanhamento clínico e com especialistas (psiquiatra e endocrinologista).</p>
<p><b>CID:</b> Z00 / Z02.</p>
<div class="ass">Serra Dourada, MS, 10/07/2025.<br><br>Dr. Otávio Brandão Leite<br>Médico, CRM/MS 90.444</div>
"""

RECEITAS = f"""
<div class="cab"><b>SERVIÇO DE SAÚDE DO SERVIDOR MUNICIPAL DE SERRA DOURADA</b><br>Centro Médico do Servidor Municipal</div>
<h1>RECEITUÁRIO MÉDICO</h1><h2>Paciente: Marisa Helena Duarte Lobo</h2>
<p><b>Uso externo</b></p>
<p>1. SEMAGLUTIDA (OZEMPIC 1 MG OU WEGOVY 1 MG) ........ 01 caixa<br>
1ª a 4ª semana: aplicar 19 cliques, subcutâneo, uma vez na semana, por 4 semanas (0,25 mg).<br>
5ª a 8ª semana: aplicar 38 cliques, subcutâneo, uma vez na semana, por 4 semanas (0,5 mg).<br>
A partir da 9ª semana: aplicar 1 mg, subcutâneo, uma vez na semana, até o retorno (cerca de 76 cliques).</p>
<p><b>Uso oral</b></p>
<p>1. Ondansetrona 8 mg: 1 comprimido de 8 em 8 horas, se náuseas ou vômitos.<br>
2. Buscopam composto: 1 comprimido de 6 em 6 horas, se dor abdominal.<br>
3. Lactulona xarope: 10 a 20 mL no café da manhã, se constipação intestinal.</p>
<p>Programa de desconto do laboratório (telefone indicado na receita original).</p>
<div class="ass">Dr. Henrique Salles Vidal<br>Endocrinologista, CRM/MS 90.333, RQE 90.334</div>

<div class="quebra"></div>
<div class="cab"><b>SERVIÇO DE SAÚDE DO SERVIDOR MUNICIPAL DE SERRA DOURADA</b><br>Centro Médico do Servidor Municipal</div>
<h1>RECEITUÁRIOS ANTERIORES</h1><h2>Paciente: Marisa Helena Duarte Lobo</h2>
<p><b>Receituário de 01/06/2025, uso subcutâneo</b><br>
1. Insulina NPH 100 UI/mL ........ 02 frascos. Aplicar 8 UI, via SC, antes do café, do almoço e do jantar.<br>
2. Insulina Regular 100 UI/mL ........ 02 frascos. Aplicar 8 UI, via SC, no almoço.</p>
<p><b>Receituário de 01/06/2025, uso oral</b><br>1. Amitriptilina 25 mg ........ 240 comprimidos. Tomar 4 comprimidos à noite.</p>
<p><b>Receituários de 10/07/2025</b><br>
Uso subcutâneo: Insulina NPH 100 UI/mL, 02 frascos, 8 UI 3 vezes ao dia (antes do café, almoço e jantar); Insulina Regular 100 UI/mL, 02 frascos, 8 UI antes do almoço.<br>
Uso oral: Dipirona 500 mg/mL, 40 gotas de 6 em 6 horas se dor ou febre; Omeprazol 20 mg, 2 comprimidos cedo, em jejum; Clonazepam (notificação de receita B) 2,5 mg/mL, 15 gotas à noite; Amitriptilina 25 mg, 4 comprimidos à noite.</p>
<div class="ass">Dr. Otávio Brandão Leite<br>Médico, CRM/MS 90.444</div>
"""

RENDA = f"""
<h1>DECLARAÇÃO DE ESTADO DE POBREZA PARA FINS JUDICIAIS</h1><h2>&nbsp;</h2>
<p>MARISA HELENA DUARTE LOBO, brasileira, solteira, aposentada, CPF fictício 000.000.000-00, residente em Serra Dourada, MS, declara, sob as penas da lei, que não tem condições de arcar com as despesas do processo sem prejuízo do próprio sustento e do de sua família, e requer a assistência judiciária gratuita (arts. 98 e seguintes do CPC).</p>
<div class="ass">Serra Dourada, MS, 09/08/2025.<br><br>Marisa Helena Duarte Lobo</div>

<h3 style="margin-top:28pt">Demonstrativos de pagamento juntados (Instituto de Previdência de Serra Dourada)</h3>
<p>Beneficiária: Marisa Helena Duarte Lobo, servidora municipal aposentada. Oito demonstrativos mensais, todos emitidos em 10/07/2025.</p>
<table><tr><th>Mês de referência</th><th>Rendimentos</th><th>Descontos</th><th>Valor líquido</th></tr>
<tr><td>Novembro/2024</td><td>R$ 5.795,39</td><td>R$ 2.084,31</td><td>R$ 3.711,08</td></tr>
<tr><td>Dezembro/2024</td><td>R$ 5.795,39</td><td>R$ 2.144,31</td><td>R$ 3.651,08</td></tr>
<tr><td>Janeiro/2025</td><td>R$ 5.795,39</td><td>R$ 2.144,31</td><td>R$ 3.651,08</td></tr>
<tr><td>Fevereiro/2025</td><td>R$ 5.795,39</td><td>R$ 2.225,31</td><td>R$ 3.570,08</td></tr>
<tr><td>Março/2025</td><td>R$ 5.795,39</td><td>R$ 2.084,31</td><td>R$ 3.711,08</td></tr>
<tr><td>Abril/2025</td><td>R$ 5.795,39</td><td>R$ 2.144,31</td><td>R$ 3.651,08</td></tr>
<tr><td>Maio/2025</td><td>R$ 5.795,39</td><td>R$ 2.197,31</td><td>R$ 3.598,08</td></tr>
<tr><td>Junho/2025</td><td>R$ 5.795,39</td><td>R$ 2.440,38</td><td>R$ 3.355,01</td></tr></table>
<p>Descontos do mês de junho/2025: contribuição e assistência do plano de saúde do servidor (R$ 405,68 e R$ 30,00); três consignações bancárias (R$ 1.359,41, R$ 83,00 e R$ 296,18); seguro (R$ 23,04); cartão de crédito consignado (R$ 243,07).</p>

<div class="quebra"></div>
<h3>Comprovantes de despesas juntados</h3>
<p>A autora juntou as cópias abaixo. Os valores indicados são os que aparecem nas próprias cópias.</p>
<table><tr><th>Documento</th><th>Valor</th></tr>
<tr><td>Conta de água</td><td>R$ 155,71</td></tr>
<tr><td>Conta de energia elétrica</td><td>R$ 224,17</td></tr>
<tr><td>Fatura de internet</td><td>valor não legível na cópia</td></tr>
<tr><td>Fatura de telefone celular</td><td>R$ 42,13</td></tr>
<tr><td>Contrato de locação residencial (12 meses), em nome da autora</td><td>aluguel de R$ 900,00</td></tr>
<tr><td>Fatura de cartão de crédito</td><td>R$ 1.316,92</td></tr>
<tr><td>Cupons de farmácia</td><td>valores diversos, entre eles R$ 186,00</td></tr></table>
"""

NEGATIVA = f"""
<div class="cab"><b>PREFEITURA MUNICIPAL DE SERRA DOURADA</b><br>Secretaria Municipal de Saúde, Núcleo de Apoio Técnico à Judicialização</div>
<h1>OFÍCIO Nº 0981/2025/NAJ/SMS</h1><h2>Serra Dourada, 16 de outubro de 2025</h2>
<p class="dados">Paciente: Marisa Helena Duarte Lobo<br>Requerimento: 2025000099991<br>Assunto: solicitação de medicamento<br>Solicitante: Beatriz Lemos Arantes (advogada)</p>
<p>Em atenção ao requerimento que solicita o medicamento <b>SEMAGLUTIDA SC 1 mg (OZEMPIC ou WEGOVY)</b>, informamos que, pela Portaria nº 1.996/2013 do Ministério da Saúde, o Município responde apenas pelos medicamentos do Componente Básico da Assistência Farmacêutica, definidos pela Resolução nº 07/CIB/SES/2020 (elenco da assistência farmacêutica básica de Mato Grosso do Sul).</p>
<p>Como o medicamento solicitado não faz parte desse elenco, <b>informamos a indisponibilidade de fornecimento</b>.</p>
<div class="ass">Núcleo de Apoio Técnico à Judicialização<br>Secretaria Municipal de Saúde de Serra Dourada</div>

<h3 style="margin-top:22pt">Procedimento pré-processual no CEJUSC Saúde (autos nº {PRE})</h3>
<p><b>26/10/2025.</b> O CEJUSC Saúde intima o Município para, em até 10 dias, responder à providência de saúde requerida, segundo o modelo do Termo de Cooperação nº 03.058/2024 (informar estoque, compra em andamento, falta de padronização com alternativas no SUS, ou outro motivo fundamentado).</p>
<p><b>30/10/2025.</b> O Município responde por e-mail, com o mesmo fundamento do ofício acima: "SEMAGLUTIDA 1mg (OZEMPIC ou WEGOVY)" não faz parte do Componente Básico; comunica a indisponibilidade de fornecimento.</p>

<div class="quebra"></div>
<div style="font-size:10.5pt;line-height:1.38">
<div class="cab"><b>PROCURADORIA-GERAL DO ESTADO DE MATO GROSSO DO SUL</b><br><b>SECRETARIA DE ESTADO DE SAÚDE DE MATO GROSSO DO SUL</b></div>
<h1>RESPOSTA À PROVIDÊNCIA DE SAÚDE PGE/SES Nº 1187</h1><h2>07/11/2025</h2>
<p class="dados">Para: CEJUSC Saúde, Termo de Cooperação Técnica 03.058/2024<br>Assunto: solicitação de fornecimento de medicamentos<br>Processo nº {PRE}<br>Solicitante: Marisa Helena Duarte Lobo</p>
<p><b>Foi solicitado o fornecimento de:</b> Semaglutida 2,4 mg.</p>
<p><b>Análise médica:</b> desfavorável a Semaglutida 2,4 mg, conforme documento anexo.</p>
<p><b>Análise técnica:</b> segundo a RENAME, Semaglutida 2,4 mg não está incorporada ao SUS; por isso, os servidores estaduais não têm competência (autorização legal) para fornecê-la.</p>
<p><b>Conclusão:</b> não é possível fornecer Semaglutida 2,4 mg.</p>
<div class="ass">Farmacêutica e servidor da PGE/SES (assinaturas no original)</div>

<h3 style="margin-top:20pt">Anexo: análise com fundamento na medicina baseada em evidências</h3>
<p class="dados">Processo nº {PRE}. Objeto: medicação Ozempic (semaglutida) 1 mg, CID-10 E11. Outras informações: idade de 44 anos; HbA1c de 7,5%; diabetes tipo 2 confirmado nos documentos do pedido.</p>
<p>1. A receita juntada ao pedido tem preenchimento incompleto: <b>sem data e sem validade</b>.</p>
<p>2. Não foram apresentados resultado de exame complementar que comprove ou exclua a enfermidade, informação de tratamentos anteriores (evolução e datas) nem referência bibliográfica que justifique a medicação para a enfermidade.</p>
<p>3. A análise identificou o <b>estudo SELECT</b> (análise pré-especificada publicada na revista Lancet em 2025). Os critérios de elegibilidade desse estudo excluem, entre outras situações, idade menor que 45 anos, HbA1c igual ou maior que 6,5% e histórico de diabetes tipo 1 ou tipo 2. A situação da paciente não está incluída no estudo SELECT, de modo que não há comprovação de evidência científica para o caso.</p>
<p>4. Falta, portanto, a comprovação de eficácia e segurança por ensaios clínicos randomizados e revisões sistemáticas ou meta-análises, e de benefício clínico superior ao que o SUS oferece. A nota de rodapé lembra que, pela Súmula Vinculante nº 60 e pelo item 4.3 do Tema 1234 (RE 1.366.243), cabe ao autor comprovar a eficácia, a segurança e a inexistência de substituto terapêutico no SUS.</p>
<p><b>Conclusão:</b> desfavorável à medicação Ozempic (semaglutida) 1 mg. Sugere enviar exames, histórico de tratamentos e referência bibliográfica e, se houver medicamento incorporado, observar o PCDT. Orienta consultar o médico prescritor.</p>
<div class="ass">Dr. Paulo Mendes Arruda<br>Assistente técnico, médico, CRM/MS 90.555</div>
</div>

<div class="quebra"></div>
<div class="cab"><b>PODER JUDICIÁRIO DO ESTADO DE MATO GROSSO DO SUL</b><br>Comarca de Serra Dourada, CEJUSC Saúde</div>
<h1>CERTIDÃO</h1><h2>&nbsp;</h2>
<p class="dados">Autos: {PRE}<br>Ação: Reclamação Pré-processual, Obrigação de Fazer<br>Requerente: Marisa Helena Duarte Lobo<br>Requerido: Procuradoria-Geral do Estado de Mato Grosso do Sul e outro</p>
<p>Certifico que nesta data o ente não atendeu a providência de saúde requerida. Certifico, ainda, que enviei e-mail ao endereço fornecido pela requerente com a resposta dada pelo(s) requerido(s).</p>
<div class="ass">Serra Dourada, MS, 13 de novembro de 2025.<br><br>Servidor do CEJUSC Saúde (assinado digitalmente)</div>
"""

DECISOES = f"""
<div class="cab"><b>PODER JUDICIÁRIO DO ESTADO DE MATO GROSSO DO SUL</b><br>Comarca de Serra Dourada, 4ª Vara Cível Residual</div>
<p class="dados">Processo nº {PROC}<br>Autora: Marisa Helena Duarte Lobo<br>Réus: Município de Serra Dourada e outro</p>
<p>Vistos. Figuram no polo passivo o Município de Serra Dourada e o Estado de Mato Grosso do Sul. As demandas que envolvem entes públicos devem ser processadas pelo Juízo da Fazenda Pública, segundo a legislação processual e a organização judiciária local. Determino a remessa dos autos a uma das Varas da Fazenda Pública desta comarca. Publique-se. Intimem-se.</p>
<div class="ass">Serra Dourada, data da assinatura digital.<br>Fábio Augusto Reis, Juiz de Direito</div>

<div class="cab" style="margin-top:26pt"><b>PODER JUDICIÁRIO DO ESTADO DE MATO GROSSO DO SUL</b><br>Comarca de Serra Dourada, 1ª Vara de Fazenda Pública e de Registros Públicos</div>
<h1>DECISÃO</h1><h2>Procedimento Comum Cível, fornecimento de medicamentos</h2>
<p>Pelo art. 2º da Resolução nº 334, de 10/10/2024, do TJMS, que alterou a Resolução nº 200/2018, compete à Vara do Juizado Especial da Saúde processar, conciliar e julgar as ações com causa de pedir ou pedido relativos à saúde, até o valor de 60 salários mínimos. O valor desta causa está aquém desse limite e a matéria é de saúde, o que torna este Juízo incompetente.</p>
<p>Além disso, nos termos do art. 2º, § 4º, da Lei nº 12.153/2009, no foro onde estiver instalado Juizado Especial da Fazenda Pública sua competência é absoluta, e a parte não pode optar entre a Justiça Comum e o Juizado. Não há necessidade de prova pericial.</p>
<p>Declino a competência para a Vara do Juizado Especial da Saúde desta comarca. Remetam-se os autos, com urgência.</p>
<div class="ass">Serra Dourada, data da assinatura digital.<br>Luciana Prates Mendes, Juíza de Direito</div>

<div class="quebra"></div>
<div class="cab"><b>PODER JUDICIÁRIO DO ESTADO DE MATO GROSSO DO SUL</b><br>Comarca de Serra Dourada, 4ª Vara do Juizado Especial da Fazenda Pública</div>
<h1>DECISÃO</h1><h2>&nbsp;</h2>
<p>Vistos. 1. O processo foi distribuído à 4ª Vara Cível, que declinou para a 1ª Vara de Fazenda Pública e de Registros Públicos, e só foi redistribuído a este Juízo em 07/03/2026 (16h14), com conclusão nesta data (08/03/2026).</p>
<p>2. A matéria não é mais da competência deste Juizado Especializado da Fazenda Pública, segundo a Resolução nº 334/2024 do TJMS, regulamentada pelo Provimento nº 680/2024 do CSM, que atribui à 1ª Vara do Juizado Especial da Saúde as ações com causa de pedir ou pedido relativos à saúde, inclusive de natureza suplementar.</p>
<p>Tratando-se de matéria de saúde, encaminhem-se os autos, após regularizar eventual pendência no sistema, à <b>1ª Vara do Juizado Especial da Saúde</b> desta comarca, como já determinado anteriormente e não observado na redistribuição, com urgência. Intime-se.</p>
<div class="ass">Serra Dourada, 08 de março de 2026.<br>Rodrigo Alves Teles, Juiz de Direito</div>
"""

NATJUS = f"""
<div class="cab"><b>TRIBUNAL DE JUSTIÇA DO ESTADO DE MATO GROSSO DO SUL</b><br>Núcleo de Apoio Técnico do Judiciário (NATJus)</div>
<h1>NOTA TÉCNICA DO NATJus Nº 0612/2026</h1><h2>&nbsp;</h2>
<p class="dados">Autos: {PROC}<br>Ação: Procedimento do Juizado Especial da Fazenda Pública, Serra Dourada, 1ª Vara do Juizado Especial da Saúde<br>Requerente: Marisa Helena Duarte Lobo<br>Requeridos: Estado de Serra Dourada e Município de Serra Dourada</p>
<p><b>I. Enfermidade e linha terapêutica do SUS.</b> Segundo o laudo e os demais documentos, a requerente tem 45 anos, reside em Serra Dourada/MS e tem Diabetes mellitus tipo 2 (CID-10 E11) há cerca de quinze anos. Não foram apresentados resultados de exames complementares.</p>
<table><tr><th>Princípio ativo</th><th>Posologia</th><th>Incorporado ao SUS?</th></tr>
<tr><td>Semaglutida (Ozempic)</td><td>1 mg, conforme prescrição</td><td>NÃO</td></tr></table>
<p>O DM2 corresponde a 90% a 95% dos casos de diabetes e pode causar complicações agudas e crônicas (doença renal, neuropatia, retinopatia, infarto e AVC), segundo o PCDT de Diabete Melito Tipo 2 (Portaria SECTICS/MS nº 7/2024).</p>
<p><b>II. Tratamentos realizados e alternativas.</b> Segundo documentos médicos e questionário da Defensoria Pública, a paciente usa insulinoterapia crônica com insulinas NPH e Regular, embora a insulina regular tenha sido suspensa por hipoglicemias recorrentes. Usa também Metformina XR (Glifage XR). Faz acompanhamento com psiquiatra e endocrinologista há cerca de 15 anos por ansiedade, depressão e insônia, com relato de internações em crises, e usa Clonazepam, Amitriptilina, Clorpromazina e Clomipramina, além de Omeprazol e Dipirona.</p>
<p>No DM2, a abordagem inicial é a mudança de estilo de vida, seguida de metformina como primeira escolha. Se as metas não forem atingidas, associam-se sulfonilureias, dapagliflozina ou insulina (PCDT, Portaria SECTICS/MS nº 7/2024).</p>
<p><b>III. Medicamento solicitado.</b> A semaglutida é análoga do GLP-1 e reduz a glicemia de forma dependente da glicose, estimulando a insulina e reduzindo o glucagon; reduz também o peso corporal e o apetite. Indicação em bula: adultos com DM2 insuficientemente controlado, como adjuvante à dieta e ao exercício, em monoterapia quando a metformina for inapropriada ou em adição a outros antidiabéticos. Reações muito comuns: náusea e diarreia; comuns: vômito e hipoglicemia; graves: complicações da retinopatia, pancreatite aguda (incomum) e reações anafiláticas (raras). Fonte: bula profissional do Ozempic, Novo Nordisk Farmacêutica do Brasil Ltda., ANVISA, 2024.</p>
<p><b>IV. Registro.</b> A semaglutida (antidiabético) está registrada na ANVISA.</p>
<p><b>V. Risco iminente à vida.</b> Não há dados clínicos que indiquem risco iminente à vida da paciente.</p>
<p><b>VI. Atendimento na rede pública.</b> A paciente é atendida pela rede pública de saúde.</p>
<p><b>VII. Disponibilidade no SUS.</b> A semaglutida não está padronizada na RENAME 2024 nem em outro ato normativo do SUS para a patologia/CID apresentados. <b>Não há em tramitação solicitação de avaliação da semaglutida para as patologias apresentadas</b>, conforme a consulta pública de tecnologias em avaliação da Conitec a que este Núcleo tem acesso.</p>
<p><b>VIII. Ente responsável.</b> Como a semaglutida não está padronizada, não é possível indicar o ente responsável segundo as normas do SUS.</p>
<p><b>IX. Alternativas no SUS.</b> O PCDT do Diabete Melito tipo 2 (Portaria SCTIE/MS nº 54/2020) oferece aos pacientes cadastrados Cloridrato de Metformina, Glibenclamida, Gliclazida, Insulina NPH, Insulina Regular e <b>Dapagliflozina</b>. A RENAME 2024 padroniza no Componente Básico antidiabéticos orais (Glibenclamida, Metformina, Gliclazida), antidepressivos, ansiolíticos, estatina, anti-hipertensivos, bloqueadores de canal de cálcio, betabloqueadores, diuréticos e vasodilatadores. O SUS oferece ainda consultas com nutricionista e educador físico.</p>
<p><b>X. Genérico e preço.</b> A semaglutida tem genérico e similar. Preços do Painel CMED/ANVISA, <b>alíquota de 17%</b>, consultado em 12/03/2026:</p>
<table><tr><th>Apresentação</th><th>PF</th><th>PMC</th><th>PMVG</th></tr>
<tr><td>OZEMPIC (Novo Nordisk) 1,34 mg/mL sol. inj., 1 carpule de 3 mL + 1 sistema aplicador (doses de 1 mg)</td><td>R$ 968,00</td><td>R$ 1.298,54</td><td>R$ 759,59</td></tr></table>
<p><b>XI. Conclusão.</b> A paciente é atendida pela rede pública e não há risco iminente à vida; a semaglutida não está na RENAME 2024 para o CID apresentado; não há pedido de avaliação em tramitação na Conitec; o PCDT oferece metformina, glibenclamida, gliclazida, insulinas NPH e Regular e dapagliflozina. Para o fornecimento de medicamento não incorporado, devem ser observados os critérios de eficácia, segurança, custo-efetividade e impacto orçamentário dos Temas 6 e 1234 do STF, e <b>não foram apresentadas evidências científicas robustas, como ensaios clínicos randomizados, meta-análises ou revisões sistemáticas, em sua integralidade</b>.</p>
<p>Em face do exposto, este Núcleo manifesta-se <b>desfavorável</b> ao pedido de semaglutida.</p>
<div class="ass">Serra Dourada, MS, 12 de março de 2026.<br>Equipe técnica do NATJus (médicos, enfermeiros e farmacêuticos; assinaturas digitais)</div>
"""

DOCS = [
    ("01-peticao-inicial", INICIAL),
    ("02-laudo-medico", LAUDO),
    ("03-receitas", RECEITAS),
    ("04-renda-e-despesas", RENDA),
    ("05-negativa-administrativa", NEGATIVA),
    ("06-decisoes-competencia", DECISOES),
    ("07-nota-tecnica-natjus", NATJUS),
]

GABARITO = {
 "processo": f"{PROC} (fictício)",
 "medicamento": "Semaglutida (Ozempic) 1 mg, uso subcutâneo semanal",
 "representacao": "Advogado particular",
 "data_analise": "24/10/2026",
 "resumo": "Caso bem instruído, mas que não cumpre todos os requisitos. A negativa administrativa e a incapacidade financeira estão provadas e o laudo é fundamentado. Faltam a discussão sobre a Conitec, a prova de que as alternativas do SUS não servem (só a insulina regular foi afastada) e a evidência de alto nível (o laudo só cita o nome de um estudo, sem juntá-lo).",
 "requisitos": [
  {"id": "a", "nome": "Negativa na via administrativa", "situacao": "atendido", "onde": "05-negativa-administrativa.pdf, p. 1 a 3", "obs": "O Município negou a semaglutida 1 mg por ofício e por e-mail ao CEJUSC Saúde; o Estado respondeu que não pode fornecer; a certidão do CEJUSC registra que o ente não atendeu. Ressalva: a resposta do Estado fala em semaglutida 2,4 mg, embora a análise médica anexa trate do Ozempic 1 mg e a ação peça 1 mg."},
  {"id": "b", "nome": "Ilegalidade da não incorporação pela Conitec", "situacao": "nao_encontrado", "onde": "Não encontrei na inicial; 07-nota-tecnica-natjus.pdf, p. 2", "obs": "A inicial não trata da Conitec nem dos arts. 19-Q e 19-R. Só o NATJus informa que não há pedido de avaliação da semaglutida em tramitação para essa doença; a autora não argumenta nada a partir disso."},
  {"id": "c", "nome": "Impossibilidade de substituição por medicamento do SUS", "situacao": "nao_comprovado", "onde": "01-peticao-inicial.pdf, p. 1; 02-laudo-medico.pdf, p. 1; 07-nota-tecnica-natjus.pdf, p. 1 e 2", "obs": "A inicial diz que o tratamento com insulina foi suspenso, mas o laudo mostra que só a insulina regular foi suspensa e que a autora segue com insulina NPH e metformina. Nada se diz sobre dapagliflozina, glibenclamida e gliclazida, que o PCDT oferece segundo o NATJus."},
  {"id": "d", "nome": "Evidência de alto nível (ensaio randomizado ou revisão sistemática)", "situacao": "nao_comprovado", "onde": "02-laudo-medico.pdf, p. 1; 05-negativa-administrativa.pdf, p. 2; 07-nota-tecnica-natjus.pdf, p. 2", "obs": "O laudo apenas menciona o estudo SUSTAIN-6 e diretrizes de sociedades médicas, sem juntar estudo, revisão sistemática ou meta-análise. A análise da SES examinou o estudo SELECT e concluiu que a paciente não se enquadra nele; o NATJus diz que não foram apresentadas evidências robustas."},
  {"id": "e", "nome": "Imprescindibilidade clínica, com laudo fundamentado", "situacao": "atendido", "onde": "02-laudo-medico.pdf, p. 1; 03-receitas.pdf, p. 1", "obs": "O laudo descreve a história da doença, o tratamento atual, exames, IMC e a justificativa. Pontos fracos: não examina as alternativas orais do PCDT e a receita da semaglutida não tem data. O NATJus diz que não vieram exames, mas o laudo transcreve exames."},
  {"id": "f", "nome": "Incapacidade financeira", "situacao": "atendido", "onde": "01-peticao-inicial.pdf, p. 1 e 2; 04-renda-e-despesas.pdf, p. 1 e 2", "obs": "Advogado particular, com declaração de pobreza, oito demonstrativos de pagamento (líquido de R$ 3.355,01 a R$ 3.711,08, bruto de R$ 5.795,39, reduzido por consignações) e comprovantes de despesas. Não há decisão sobre a gratuidade."}
 ],
 "competencia": {
  "valor_anual": "Não calculado nos autos. A inicial fala em R$ 1.000,00 por caneta de uso semanal e, depois, em R$ 1.000,00 mensais; o valor da causa é R$ 12.000,00. O NATJus informa PMVG de R$ 759,59 por apresentação (doses de 1 mg), com alíquota de 17%.",
  "limite": "210 salários mínimos (conferir o valor vigente)",
  "resultado": "Justiça Estadual: os autos foram remetidos à 1ª Vara do Juizado Especial da Saúde porque o valor da causa fica abaixo de 60 salários mínimos; nenhuma decisão examinou o Tema 1234",
  "nota": "Fato dos autos: os preços do NATJus e da inicial, o valor da causa e as decisões de competência. O aluno deve conferir na lista CMED o PMVG com alíquota zero (o NATJus usou 17%), quantas canetas o tratamento anual exige e o salário mínimo vigente. Com qualquer cálculo razoável o valor fica muito abaixo de 210 salários mínimos."
 },
 "conferencia": [
  "Conferir a divergência de dose: o Estado respondeu sobre semaglutida 2,4 mg, enquanto a receita e a ação pedem 1 mg.",
  "Conferir na lista da Conitec se existe pedido de incorporação da semaglutida para diabetes tipo 2, e nas listas RENAME, RESME e REMUME, na data da análise.",
  "Conferir o custo: a inicial é incoerente (R$ 1.000,00 por caneta semanal e R$ 1.000,00 mensais) e o NATJus usou PMVG com alíquota de 17%.",
  "Conferir se há decisão posterior sobre a tutela de urgência e a gratuidade, que não constam dos autos.",
  "Este relatório organiza a leitura; a decisão sobre a defesa é do procurador."
 ]
}

if __name__ == "__main__":
    SAIDA.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        for nome, corpo in DOCS:
            h = pathlib.Path(tmp) / f"{nome}.html"
            h.write_text(doc(corpo), encoding="utf-8")
            subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                            f"--print-to-pdf={SAIDA / (nome + '.pdf')}", h.as_uri()], check=True, capture_output=True)
    (SAIDA / "gabarito.json").write_text(json.dumps(GABARITO, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("ok", sorted(p.name for p in SAIDA.iterdir() if not p.name.startswith("._")))
