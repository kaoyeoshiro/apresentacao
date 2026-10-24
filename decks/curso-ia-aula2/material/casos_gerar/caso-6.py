"""Gera os autos fictícios do caso 6 da Aula 2 em kit/casos/caso-6/.
Todo nome, número e endereço aqui é inventado para a aula. Uso: python3 caso-6.py (precisa de Chrome e PyMuPDF)."""
import subprocess, pathlib, tempfile
import pymupdf

AQUI = pathlib.Path(__file__).resolve().parent
SAIDA = AQUI.parent.parent / "kit" / "casos" / "caso-6"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

PROC = "0809417-53.2025.8.12.0099"
CEJ = "0807722-67.2025.8.12.0098"
AUTOR = "MARCOS VILELA PRADO"
Autor = "Marcos Vilela Prado"
DEF = "Juliana Prates Moura"
MED = "Ricardo Menezes Lobo"
CRM = "CRM/MS 90.417"
CLIN = "Clínica Hepatovida"
COM = "Vila Boa Esperança"
JUIZ = "Fernando Augusto Ribas"

CSS = """
@page { size: A4; margin: 24mm 20mm 20mm 20mm; }
body { font: 11pt/1.45 Georgia, 'Times New Roman', serif; color: #1a1a1a; }
h1 { font-size: 13.5pt; text-align: center; margin: 0 0 4pt; letter-spacing: .02em; }
h2 { font-size: 10.5pt; text-align: center; margin: 0 0 14pt; font-weight: normal; }
h3 { font-size: 11pt; margin: 12pt 0 5pt; }
p { margin: 0 0 7pt; text-align: justify; }
.cab { text-align: center; font-size: 10pt; margin-bottom: 12pt; border-bottom: 1px solid #999; padding-bottom: 6pt; }
.cab b { font-size: 11pt; }
.ass { margin-top: 26pt; text-align: center; font-size: 10.5pt; }
.ass div { display: inline-block; border-top: 1px solid #333; padding: 3pt 30pt 0; }
table { border-collapse: collapse; width: 100%; margin: 6pt 0 10pt; font-size: 10.5pt; }
td, th { border: 1px solid #888; padding: 4pt 6pt; vertical-align: top; text-align: left; }
th { background: #eee; }
.nota { font-size: 9.5pt; border-top: 1px solid #aaa; margin-top: 14pt; padding-top: 4pt; }
.box { border: 1px solid #888; padding: 8pt 10pt; margin: 8pt 0; }
.campo { border-bottom: 1px solid #999; min-height: 14pt; margin: 2pt 0 8pt; font-style: italic; }
.vazio { color: #888; }
"""

def doc(cab, titulo, sub, corpo):
    return (f"<!doctype html><meta charset='utf-8'><style>{CSS}</style>"
            f"<div class='cab'>{cab}</div><h1>{titulo}</h1><h2>{sub}</h2>{corpo}")

CAB_DPE = "<b>DEFENSORIA PÚBLICA DO ESTADO DE MATO GROSSO DO SUL</b><br>Defensoria Pública de Serra Clara"
CAB_CLIN = f"<b>{CLIN}</b><br>Dr. {MED}, Infectologia e Hepatologia, {CRM}, RQE 90.211<br>Rua das Acácias, 100, Pedra Alta/MS"
CAB_TJ = f"<b>PODER JUDICIÁRIO DO ESTADO DE MATO GROSSO DO SUL</b><br>Comarca de {COM}, Vara Única"
CAB_NAT = "<b>NÚCLEO DE APOIO TÉCNICO DO JUDICIÁRIO (NATJus)</b><br>Tribunal de Justiça do Estado de Mato Grosso do Sul"
CAB_CEJ = "<b>PODER JUDICIÁRIO DO ESTADO DE MATO GROSSO DO SUL</b><br>CEJUSC Saúde, pré-processual"

INICIAL = f"""
<p><b>AO JUÍZO DA VARA ÚNICA DA COMARCA DE {COM.upper()}/MS</b></p>
<p><b>{AUTOR}</b>, brasileiro, solteiro, inscrito no CPF n. 000.111.222-33, residente e domiciliado em {COM}/MS,
por meio da DEFENSORIA PÚBLICA DO ESTADO DE MATO GROSSO DO SUL, vem propor, com fundamento nos arts. 497 e seguintes do CPC,
<b>AÇÃO DE OBRIGAÇÃO DE FAZER com pedido de tutela provisória de urgência</b> contra o <b>MUNICÍPIO DE {COM.upper()}/MS</b>
e o <b>ESTADO DE MATO GROSSO DO SUL</b>, representado pelo Procurador-Geral do Estado, pelos motivos a seguir.</p>

<h3>1. Da gratuidade de justiça</h3>
<p>Requer a gratuidade de justiça, pois o autor não tem meios para custear as despesas processuais, conforme declaração de hipossuficiência (art. 98 do CPC).</p>
<h3>2. Das prerrogativas defensoriais</h3>
<p>Requer a observância das prerrogativas da Defensoria Pública (LC federal 80/94 e LC estadual 111/2005): prazo em dobro, dispensa de procuração e intimação pessoal.</p>

<h3>3. Dos fatos</h3>
<p>O autor tem diagnóstico de colangite esclerosante primária, CID K83, conforme laudo médico anexo (doc. 02), que atesta acompanhamento em hepatologia
"desde junho de 2025" por dilatação de vias biliares e alteração de enzimas hepáticas, com colangiorressonância compatível com a doença.
O médico prescreveu <b>ÁCIDO URSODESOXICÓLICO 300 MG (90 COMP / MÊS)</b> (doc. 03).</p>
<p>Não existe tratamento oferecido pelo SUS para a doença do autor, tampouco alternativas terapêuticas no SUS. No questionário médico (doc. 04),
à pergunta sobre tratamentos do SUS com a mesma eficácia, o médico respondeu "Não"; sobre o uso prévio das alternativas do SUS e o motivo de não as indicar, respondeu "Não possui".
O ácido ursodesoxicólico não é padronizado pelo SUS para a colangite esclerosante primária. O medicamento é indispensável para a saúde do autor, conforme informação médica anexa.</p>
<p>Conforme a tabela CMED, o menor Preço Máximo de Venda ao Governo (PMVG) do ácido ursodesoxicólico 300 mg, caixa com 90 comprimidos, é de <b>R$ 305,32</b>.
O preço varia de farmácia a farmácia, e o menor custo mensal é de <b>R$ 520,00</b>, conforme orçamento realizado na Drogaria Ipê Amarelo.</p>
<p>Em vista da urgência, esta Defensoria Pública realizou o cadastro no CEJUSC SAÚDE, autos n. {CEJ}, para que, extrajudicialmente, os entes públicos providenciassem
o medicamento, porém sem êxito. O requerente compareceu à Farmácia Municipal, mas o medicamento não está disponível. Como não tem condições de arcar com o custo,
só lhe restou buscar o Poder Judiciário (art. 8º da Convenção Americana sobre Direitos Humanos).</p>

<h3>4. Da competência da Justiça Estadual e da legitimidade passiva</h3>
<p>O pedido observa a Súmula Vinculante 60 do STF, que remete aos acordos interfederativos homologados no Tema 1.234, no qual se fixaram critérios objetivos de competência.
O medicamento tem registro na Anvisa e não está incorporado ao SUS para a colangite esclerosante primária.</p>
<p>Multiplicando-se o valor do medicamento por 12, obtém-se o custo anual de <b>R$ 3.663,84</b> pelo PMVG e de <b>R$ 6.240,00</b> pelo preço da drogaria,
devendo o feito tramitar perante a Justiça Estadual. A legitimidade do Estado decorre da fixação da competência, e a responsabilidade dos entes é solidária,
de modo que o Estado e o Município compõem adequadamente o polo passivo.</p>

<h3>5. Dos fundamentos jurídicos</h3>
<p><b>5.1. Do cumprimento dos requisitos dos Temas 6 e 1.234.</b> As Súmulas Vinculantes 60 e 61 e o Tema 6 (RE 566.471) exigem, cumulativamente, os requisitos (a) a (f)
do item 2 da tese; o Tema 1.234, itens 4.3 e 4.4, reitera o ônus do autor de demonstrar eficácia e segurança com evidência de alto nível e a inexistência de substituto no SUS.
Passa-se a demonstrar o preenchimento dos requisitos.</p>
<p><b>Requisito a):</b> a negativa administrativa está comprovada no protocolo emitido nos autos do CEJUSC SAÚDE n. {CEJ} (doc. 05), e pelo fato de o autor ter de socorrer-se do Poder Judiciário.</p>
<p><b>Requisito b):</b> o medicamento não está incorporado ao SUS para a colangite esclerosante primária, e não existe outro tratamento no SUS para a doença.
A ilegalidade da decisão administrativa reside justamente no fato de negar ao autor o único tratamento que lhe seria viável, em violação ao art. 196 da Constituição.</p>
<p><b>Requisitos c):</b> o medicamento é imprescindível para o restabelecimento da saúde do autor e não pode ser substituído por outros.</p>
<p><b>Requisito d):</b> a evidência científica de segurança e eficácia do medicamento está atestada nos documentos anexos.<sup>1</sup></p>
<p><b>Requisito e):</b> a incapacidade de pagamento do tratamento deve ser presumida, pois o autor é assistido pela Defensoria Pública, que fez avaliação financeira prévia
para a assistência gratuita. Ademais, o autor está atualmente desempregado.</p>
<p>Comprovado o preenchimento dos requisitos cumulativos dos Temas 6 e 1.234, impõe-se a concessão judicial do medicamento.</p>
<p><b>5.2. Do direito fundamental à saúde.</b> Os arts. 6º e 196 da Constituição asseguram a saúde como direito de todos e dever do Estado.
Os arts. 19-M, 19-N e 19-P da Lei 8.080/1990 não proíbem a dispensação de medicamento fora dos protocolos e listas do SUS, que orientam a prescrição e não a limitam.
Deve-se preferir a alternativa do SUS, mas, sendo ela ineficaz ou contraindicada, não se pode negar o tratamento indispensável. O Tribunal de Justiça de Mato Grosso do Sul
já manteve tutela que obrigou o Poder Público a fornecer ácido ursodesoxicólico a paciente com colangite esclerosante primária (agravo de instrumento julgado pela 2ª Câmara Cível em 2019).</p>
<p>O médico que prescreveu atende em clínica particular, mas conhece o quadro clínico do autor. Não se trata de escolha de tratamento, pois inexiste outro no SUS.
Esgotados os meios administrativos, o autor busca o Judiciário.</p>

<h3>6. Da tutela provisória de urgência</h3>
<p>A probabilidade do direito está na prova documental, em especial o documento médico que comprova a necessidade do ácido ursodesoxicólico 300 mg (90 comp./mês).
O perigo de dano está no risco de agravamento da doença, com grave comprometimento do bem-estar. O autor é hipossuficiente e não pode prestar caução (art. 300, § 1º, do CPC),
e a medida é reversível, pois eventual revogação apenas interrompe o tratamento.</p>

<h3>7. Dos pedidos</h3>
<p>Requer: a) a gratuidade de justiça; b) a tutela de urgência para que os réus forneçam imediatamente o ÁCIDO URSODESOXICÓLICO 300 MG (90 COMP / MÊS), conforme receituário,
pelo prazo prescrito, sob pena de multa ou bloqueio de valores (art. 139, IV, do CPC); c) em caso de descumprimento, o sequestro via SISBAJUD de <b>R$ 6.240,00</b>,
suficiente para 12 meses de tratamento na farmácia de menor preço, com prestação de contas; d) a citação dos réus; e) a inversão do ônus da prova (art. 373, § 1º, do CPC);
f) a procedência do pedido, com a condenação dos réus a fornecer o medicamento pelo prazo prescrito; g) honorários em favor do fundo da Defensoria Pública.</p>
<p>Provará o alegado por todos os meios admitidos, especialmente documental e técnico. Atribui-se à causa o valor de <b>R$ 6.240,00</b>, correspondente a 12 meses de tratamento na rede particular.</p>
<p>Nesses termos, pede deferimento.</p>
<p>Serra Clara/MS, data da assinatura digital.</p>
<div class="ass"><div>{DEF}<br>Defensora Pública (em substituição)<br>assinatura eletrônica</div></div>
<div class="nota"><sup>1</sup> https://ojs.brazilianjournals.com.br/ojs/index.php/BJHR/article/view/74843.</div>
"""

LAUDO = f"""
<table><tr><td><b>Paciente:</b> {AUTOR}</td><td><b>Data de emissão:</b> 15/07/2025</td></tr></table>
<p>Atesto, para fins médicos e terapêuticos, que realizo acompanhamento médico ambulatorial especializado em hepatologia no senhor {Autor}, adulto (entre 35 e 45 anos),
desde junho de 2025, devido a dilatação de vias biliares com consequente alteração de enzimas hepáticas. Durante os exames investigativos, foi realizada ressonância magnética
de abdome superior com colangiorressonância, com imagens compatíveis com colangite esclerosante primária, e por isso faz-se extremamente necessário o uso de ácido ursodesoxicólico
para tratamento, a fim de evitar a progressão da doença para cirrose hepática, carcinoma hepatocelular e transplante hepático. Paciente segue em acompanhamento médico regular.</p>
<p><b>CID: K 83</b></p>
<h3>Exames laboratoriais (resumo)</h3>
<p>11/06/2025: AMA não reagente; AML não reagente; FAN, ANCA e anti-LKM1 não reagentes; sorologias virais para hepatites B e C não reagentes; TGO 40 (ref. 39); TGP 61 (ref. 39);
FA 148 (ref. 171); GGT 217 (ref. 45); bilirrubina total 0,7; albumina 5,1; plaquetas 284.000.<br>
29/11/2024: TGO 52 (ref. 39); TGP 42 (ref. 39); plaquetas 235.000.</p>
<h3>Exames complementares</h3>
<p>US de abdome total (21/09/2024): cisto hepático, cisto renal à esquerda, esplenomegalia discreta.<br>
TC de abdome total (06/11/2024): cisto hepático; dilatação de árvore biliar intra-hepática esquerda com início na origem do ducto.<br>
EDA (03/06/2025): normal.<br>
RM de abdome superior com colangiorressonância (09/06/2025): diminuto pólipo vesicular; pequenas falhas de enchimento agrupadas no interior de ramos segmentares e vias biliares
intra-hepáticas à esquerda, que podem estar relacionadas a cálculo ou lama biliar, com acentuada dilatação de ductos a montante no segmento anterolateral; ducto hepatocolédoco
sem dilatações ou falhas de enchimento evidentes.</p>
<div class="ass"><div>Dr. {MED}<br>{CRM}, assinatura eletrônica em 15/07/2025</div></div>
"""

RECEITA = f"""
<table><tr><td><b>Paciente:</b> {AUTOR}</td><td><b>Data de emissão:</b> 15/07/2025<br><b>Validade:</b> 14/08/2025</td></tr></table>
<p style="margin-top:14pt">1. <b>ÁCIDO URSODESOXICÓLICO 300 MG</b>, 90 comprimidos por mês</p>
<p style="margin-left:18pt">Tome 2 comprimidos pela manhã e 1 comprimido à noite.</p>
<div class="ass" style="margin-top:60pt"><div>Dr. {MED}<br>{CRM}, receituário simples com assinatura eletrônica em 15/07/2025</div></div>
"""

def c(txt, vazio=False):
    return f"<div class='campo{' vazio' if vazio else ''}'>{txt}</div>"

QUEST = f"""
<p>Em atenção aos Enunciados 19 e 58 das Jornadas de Direito da Saúde do CNJ, solicita-se ao médico assistente que responda às perguntas abaixo. Campos manuscritos transcritos.</p>
<table>
<tr><th colspan="2">Dados do paciente</th></tr>
<tr><td>Nome</td><td>{Autor}</td></tr>
<tr><td>Atendimento que originou a prescrição</td><td>(X) Particular ( ) Convênio ( ) SUS</td></tr>
<tr><th colspan="2">Dados da prescrição</th></tr>
<tr><td>Medicamento</td><td>Ácido ursodesoxicólico 300 mg; 2 comprimidos de manhã e 1 à noite</td></tr>
<tr><td>Duração do tratamento</td><td>(X) Contínuo ( ) Temporário</td></tr>
<tr><td>Registro na Anvisa</td><td>(X) Sim ( ) Não. Indicação conforme o registro: ( ) Sim ( ) Não <span class="vazio">[sem marcação]</span></td></tr>
<tr><td>Previsto em PCDT da doença listada abaixo</td><td>(X) Sim ( ) Não</td></tr>
<tr><td>Consta em padronização oficial (REMUME, RENAME, listas estaduais)</td><td>( ) Sim (X) Não</td></tr>
<tr><td>Há estudos de evidência científica (eficácia, eficiência, efetividade e segurança)? Qual?</td><td><span class="vazio">[sem marcação e sem resposta]</span></td></tr>
</table>
<p><b>1. Doença que motivou a prescrição e CID:</b></p>{c("Enfermidade: \"Colangite\". CID: K 74.3")}
<p><b>2. Características da doença:</b></p>{c("[em branco]", True)}
<p><b>3. Como é feito o diagnóstico:</b> ( ) clínico (X) laboratorial (X) imagem ( ) outro.</p>{c("Ressonância abdominal + TC de abdome: dilatação da árvore biliar intra-hepática (E); aumento de TGO, TGP, FA, gama GT e bilirrubinas.")}
<p><b>4. Finalidade do medicamento:</b> (X) profilática ( ) curativa ( ) paliativa ( ) diagnóstico.</p>
<p><b>5. Existem tratamentos oferecidos pelo SUS para a doença com a mesma eficácia? Quais?</b></p>{c("Não")}
<p><b>6. As alternativas terapêuticas do SUS já foram utilizadas?</b> ( ) Sim ( ) Não</p>{c("Não possui")}
<p><b>6.1. Período de tratamento e resposta obtida:</b></p>{c("[em branco]", True)}
<p><b>6.2. O paciente faz uso de outros tratamentos (farmacológicos ou não) para a doença? Quais?</b></p>{c("[em branco]", True)}
<p><b>6.3. Por que não foram indicados medicamentos da rede pública?</b></p>{c("Não possui.")}
<p><b>7. O tratamento pode ser substituído por alternativa do SUS?</b> ( ) Sim (X) Não</p>
<p><b>7.1. Vantagens do tratamento proposto em comparação com os oferecidos pelo SUS:</b></p>{c("Paciente necessita do medicamento para retardar a evolução e progressão da doença hepática, melhorar os parâmetros bioquímicos de colestase e reduzir o risco de evolução de complicações.")}
<p><b>8. O medicamento é imprescindível?</b> (X) Sim ( ) Não. Justifique:</p>{c("[em branco]", True)}
<p><b>9. A disponibilização é urgente?</b> (X) Sim ( ) Não</p>
<p><b>10. Consequências da não utilização imediata:</b> ( ) risco de morte (X) perda irreversível de órgãos ou funções (X) grave comprometimento do bem-estar ( ) outras.</p>
<p><b>11. Quadro clínico e peculiaridades do paciente:</b></p>{c("Paciente com dor abdominal intensa, vômitos frequentes e perda de peso, causando debilidade.")}
<p>Local e data: {COM}/MS, 21/08/2025. Profissional: carimbo e assinatura do médico assistente.</p>
<p><b>Parte a ser preenchida pelo paciente</b> (convênio, tentativa de obter o medicamento pelo SUS, negativa verbal ou escrita e data): <span class="vazio">[todos os campos em branco]</span>.</p>
"""

PROTO = f"""
<div class="box"><b>Portal de Serviços do e-SAJ, Providências de Saúde</b> (impressão de tela de 26/08/2025, 12:02, usuário da Defensoria Pública)<br><br>
Seu pedido foi encaminhado com sucesso e será encaminhado para o ente responsável. Se aprovado, você receberá um e-mail informando sobre o andamento.<br><br>
O protocolo <b>{CEJ}</b> foi cadastrado em 26/08/2025 12:02.</div>
<h3 style="margin-top:22pt">Senha de acesso à consulta de processo</h3>
<div class="box">Processo: <b>{CEJ}</b>, Reclamação Pré-processual (CEJUSC Saúde).<br>
Senha: ab3cd7. Responsável pela senha: {Autor}.<br>
A senha é de uso pessoal e permite acesso à tramitação processual no site do Tribunal de Justiça.<br><br>
Pré-processual, 28 de agosto de 2025.</div>
"""

LAUDO2 = f"""
<table><tr><td><b>Paciente:</b> {AUTOR}</td><td><b>Data de emissão:</b> 18/09/2025</td></tr></table>
<p>Atesto, para fins médicos e terapêuticos, que realizo acompanhamento médico ambulatorial especializado em hepatologia no senhor {Autor}, adulto (entre 35 e 45 anos),
desde junho de 2025, devido a dilatação de vias biliares com consequente alteração de enzimas hepáticas. Durante os exames investigativos, foi <b>descartada a possibilidade de
colangite biliar primária</b> e realizada ressonância magnética de abdome superior com colangiorressonância, com imagens compatíveis com colangite esclerosante primária,
razão do diagnóstico da referida patologia por exame de imagem. Assim, faz-se extremamente necessário o uso de ácido ursodesoxicólico para tratamento, a fim de evitar a progressão
da doença para cirrose hepática, carcinoma hepatocelular e transplante hepático. Paciente segue em acompanhamento médico regular.</p>
<p><b>CID: K 83, colangite esclerosante primária</b></p>
<h3>Exames</h3>
<p>Repete os exames laboratoriais e complementares do laudo de 15/07/2025 (doc. 02), entre eles AMA não reagente (11/06/2025) e a colangiorressonância de 09/06/2025.</p>
<div class="ass"><div>Dr. {MED}<br>{CRM}, assinatura eletrônica em 18/09/2025</div></div>
"""

NT = f"""
<p><b>Autos:</b> {PROC}. <b>Ação:</b> Procedimento Comum Cível, {COM}, Vara Única.<br>
<b>Requerente:</b> {AUTOR}. <b>Requeridos:</b> Município de {COM} e Estado de Mato Grosso do Sul.</p>
<h3>I. Enfermidade e linha terapêutica do SUS</h3>
<p>Segundo laudo médico e demais documentos, o requerente é adulto (entre 35 e 45 anos), reside em {COM}/MS e é portador de colangite esclerosante primária (CID-10 K83).
Foram apresentados exames, entre eles colangiorressonância (dilatação de ductos e lama ou cálculos biliares) e exames de sangue com alteração de TGO, TGP e gama GT.</p>
<table><tr><th>Princípio ativo</th><th>Posologia</th><th>Incorporado ao SUS?</th></tr>
<tr><td>Ácido ursodesoxicólico</td><td>300 mg, 3 comprimidos/dia</td><td>SIM*</td></tr></table>
<p>*O medicamento está incorporado para patologia/CID diferente do apresentado pelo paciente.</p>
<p>A colangite esclerosante primária é doença crônica e progressiva das vias biliares, com inflamação e fibrose dos ductos, que pode levar à colestase, à cirrose e à insuficiência
hepática, e se associa a maior risco de colangiocarcinoma (Sociedade Brasileira de Hepatologia).</p>
<h3>II. Tratamentos realizados e alternativas</h3>
<p><b>Não constam nos autos informações acerca de tratamentos farmacológicos e não farmacológicos eventualmente realizados.</b></p>
<p>O tratamento busca controlar sintomas e complicações e preservar a função hepática. Usam-se medicamentos para prurido e antibióticos nas colangites bacterianas;
nos estreitamentos relevantes das vias biliares, procedimentos endoscópicos; na doença avançada, o transplante hepático, disponível no SUS. O acompanhamento regular com
hepatologia e o tratamento de doença inflamatória intestinal associada também fazem parte da conduta.</p>
<h3>III. Medicamento solicitado</h3>
<p>O ácido ursodesoxicólico é ácido biliar com ação colerética e anticolestática, citoprotetora e imunomoduladora. A bula indica o uso em doenças hepatobiliares e colestáticas
crônicas, como a cirrose biliar primária, e na dissolução de cálculos biliares de colesterol, entre outras. A eficácia aparece na melhora das enzimas hepáticas e dos sintomas
colestáticos; o fármaco tem boa tolerabilidade, com diarreia como reação mais frequente (Anvisa, bulário eletrônico).</p>
<h3>IV. Classe e registro na Anvisa</h3>
<p>Colagogos, coleréticos e hepatoprotetores. Registro na Anvisa: sim, ativo.</p>
<h3>V. Risco iminente à vida</h3>
<p>Não há dados clínicos que indiquem risco iminente à vida do paciente.</p>
<h3>VI. Atendimento ou procura prévia da rede pública</h3>
<p><b>Não consta nos autos informação de atendimento ou procura prévia da rede pública local relacionada à presente demanda.</b></p>
<h3>VII. Disponibilidade no SUS</h3>
<p>O ácido ursodesoxicólico <b>não está incorporado na RENAME 2024 ou em outro ato normativo do SUS para a patologia/CID apresentado.</b>
O medicamento está incorporado pelo Ministério da Saúde para o tratamento da <b>colangite biliar primária, CID-10 K74.3</b>, por meio do CEAF, exigido o preenchimento
dos critérios de inclusão do PCDT dessa doença. <b>Não há em tramitação solicitação de avaliação do ácido ursodesoxicólico para a patologia/CID apresentado</b>,
conforme a consulta pública a que este Núcleo tem acesso (página de tecnologias em avaliação da Conitec).</p>
<h3>VIII. Ente responsável</h3>
<p>Como o medicamento não está incorporado para a patologia/CID apresentado, não é possível indicar ente responsável segundo as normas do SUS.</p>
<h3>IX. Alternativas disponíveis no SUS</h3>
<p>A CPRE (colangiopancreatografia retrógrada endoscópica, 02.09.01.001-1) é terapêutica eficaz, padronizada e oferecida pelo SUS para o tratamento da colangite, assim como
os procedimentos de coledocoplastia (04.07.03.005-0), colocação de prótese biliar (04.07.03.008-5) e dilatação percutânea de estenoses e anastomoses biliares (04.07.03.010-7).</p>
<h3>X. Genérico e preço</h3>
<p>O ácido ursodesoxicólico tem genérico e similar. Preços da tabela CMED/Anvisa, <b>alíquota de 17%</b>, consultada em 24/09/2025: ácido ursodesoxicólico (EMS S/A) 300 mg,
caixa com 30 comprimidos: PF R$ 156,26; PMC R$ 216,02; <b>PMVG R$ 122,62</b>.</p>
<h3>XI. Conclusão</h3>
<p>Não consta nos autos informação de atendimento ou procura prévia da rede pública local relacionada à demanda, e não há dados clínicos de risco iminente à vida.
O medicamento não está incorporado na RENAME 2024 ou em outro ato normativo do SUS para o CID apresentado; está incorporado para a colangite biliar primária (K74.3), via CEAF,
segundo o PCDT dessa doença; não há solicitação de avaliação em tramitação para o CID do autor; e o SUS oferece a CPRE e os procedimentos cirúrgicos acima.</p>
<p>Na Manifestação nº 0412/2025, de 10/09/2025, este Núcleo apontou divergência entre o laudo, que indicava colangite esclerosante primária (CID K83), e o questionário médico,
que indicava "Colangite" com CID K74.3 (colangite biliar primária), e suspendeu o parecer até o esclarecimento. O laudo atualizado de 18/09/2025 esclareceu a inconsistência
e estabeleceu o diagnóstico de colangite esclerosante primária (CID-10 K83.0).</p>
<p>Para medicamentos não incorporados ao SUS, devem ser observados critérios de eficácia, segurança, custo-efetividade e impacto orçamentário, conforme os Temas 6 e 1.234 do STF.
No caso, <b>não foram apresentadas evidências científicas robustas, em sua integralidade, que demonstrem segurança e desfechos clínicos adequados à condição específica do paciente.</b></p>
<p>Em face do exposto, este Núcleo de Apoio Técnico manifesta-se <b>DESFAVORÁVEL</b> ao pedido de ácido ursodesoxicólico.</p>
<p>24 de setembro de 2025.</p>
<div class="ass"><div>Equipe técnica do NATJus (médicos, enfermeiros e farmacêuticos)<br>assinatura por certificação digital</div></div>
"""

DECISAO = f"""
<p><b>Processo nº {PROC}</b><br>Classe: Procedimento Comum Cível, fornecimento de medicamentos<br>Autor: {Autor}<br>Réus: Estado de Mato Grosso do Sul e outro</p>
<p>Trata-se de ação de obrigação de fazer com pedido de tutela antecipada proposta por {Autor} contra o Município de {COM} e o Estado de Mato Grosso do Sul, para obter
o fornecimento de ácido ursodesoxicólico 300 mg, pois faz acompanhamento médico ambulatorial desde junho de 2025, devido à dilatação de vias biliares com alteração de enzimas hepáticas.
Alega que vem tentando receber o medicamento na via administrativa, sem sucesso, e pede tutela de urgência para o fornecimento imediato.</p>
<p>O Núcleo de Apoio Técnico emitiu parecer desfavorável (Nota Técnica, doc. 07).</p>
<p>É o relato. Decido.</p>
<p>A tutela deve ser indeferida. O art. 300 do CPC exige a probabilidade do direito e o perigo de dano. Analisadas as alegações e os documentos, não há probabilidade do direito.</p>
<p>A Súmula Vinculante 61 determina que a concessão judicial de medicamento registrado na Anvisa, mas não incorporado às listas do SUS, observe as teses do Tema 6 (RE 566.471),
que exige, cumulativamente e com ônus do autor, os requisitos (a) a (f) do item 2 da tese, e impõe ao juiz a consulta prévia ao NATJus, sem decidir apenas com base no laudo do autor.</p>
<p>Em atendimento aos requisitos do Tema 6, <b>em que pese não haver documentos que comprovem a negativa do pedido na via administrativa, essa é presumida</b>, em razão de o
medicamento não estar disponível na lista dos medicamentos fornecidos pelo SUS.</p>
<p>Ademais, as informações técnicas indicam que o ácido ursodesoxicólico não está incorporado à RENAME 2024 nem tem previsão em outro ato normativo do SUS para a patologia do autor.
O fármaco foi incorporado exclusivamente para a colangite biliar primária (CID-10 K74.3), por meio do CEAF, condicionada a dispensação aos critérios do respectivo PCDT,
sem notícia de pedido de avaliação para incorporação na patologia dos autos. O SUS disponibiliza alternativas terapêuticas para as colangites, entre elas a CPRE e os procedimentos
de coledocoplastia, colocação de prótese biliar e dilatação percutânea de estenoses e anastomoses biliares.</p>
<p>Diante da falta de preenchimento dos critérios diagnósticos oficiais, da ausência de evidências científicas robustas para o uso do fármaco na doença atestada pelos exames e da
existência de alternativas terapêuticas no SUS, falta a probabilidade do direito, o que torna desnecessário examinar o segundo requisito. Liminar contra a Fazenda Pública para
medicamento sem eficácia comprovada para a condição específica ofende a política pública de saúde e os precedentes da Suprema Corte. Os requisitos da tutela de urgência não estão
preenchidos de forma cumulativa, sem prejuízo de reavaliação após a instrução.</p>
<p>Ante o exposto, <b>INDEFIRO</b> o pedido de tutela provisória de urgência, por não vislumbrar a probabilidade do direito e o risco iminente à vida, em observância às diretrizes do Tema 1.234 do STF.</p>
<p>Deixo de designar audiência de conciliação (art. 334, § 4º, II, do CPC), por envolver verba pública. Citem-se os requeridos para contestar. Decorrido o prazo, intime-se a parte autora
para manifestação em 15 dias. Após, conclusos.</p>
<p>{COM}, data da assinatura digital.</p>
<div class="ass"><div>{JUIZ}<br>Juiz de Direito, assinatura digital</div></div>
"""

DOCS = [
    ("01-peticao-inicial", CAB_DPE, "PETIÇÃO INICIAL", "Ação de obrigação de fazer com pedido de tutela de urgência", INICIAL),
    ("02-laudo-medico", CAB_CLIN, "LAUDO MÉDICO", "15/07/2025", LAUDO),
    ("03-receita", CAB_CLIN, "RECEITA SIMPLES", "15/07/2025", RECEITA),
    ("04-questionario-medico", CAB_DPE, "QUESTIONÁRIO PARA PEDIDO JUDICIAL DE MEDICAMENTO", "Respondido pelo médico assistente em 21/08/2025", QUEST),
    ("05-protocolo-cejusc", CAB_CEJ, "PEDIDO NO CEJUSC SAÚDE", "Protocolo e senha de acesso", PROTO),
    ("06-laudo-complementar", CAB_CLIN, "LAUDO MÉDICO COMPLEMENTAR", "18/09/2025", LAUDO2),
    ("07-nota-tecnica-natjus", CAB_NAT, "NOTA TÉCNICA DO NATJus Nº 2876/2025", "Parecer sobre o pedido de medicamento", NT),
    ("08-decisao-tutela", CAB_TJ, "DECISÃO", "Pedido de tutela provisória de urgência", DECISAO),
]

def carimbar(caminho):
    """Cabeçalho "Autos fictícios, material didático", número do processo e paginação em cada página."""
    d = pymupdf.open(caminho)
    n = len(d)
    cinza = (0.35, 0.35, 0.35)
    direita = f"{PROC} (fictício)"
    for i, pg in enumerate(d):
        w = pg.rect.width
        pg.insert_text((62, 36), "Autos fictícios, material didático", fontsize=8.5, fontname="helv", color=cinza)
        pg.insert_text((w - 62 - pymupdf.get_text_length(direita, fontsize=7.5), 36), direita, fontsize=7.5, fontname="helv", color=cinza)
        pg.insert_text((w / 2 - 18, pg.rect.height - 30), f"p. {i + 1} de {n}", fontsize=8.5, fontname="helv", color=cinza)
    tmp = caminho.with_suffix(".tmp.pdf")
    d.save(tmp, garbage=3, deflate=True)
    d.close()
    tmp.replace(caminho)

if __name__ == "__main__":
    SAIDA.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmpdir:
        for nome, cab, t, s, corpo in DOCS:
            h = pathlib.Path(tmpdir) / f"{nome}.html"
            h.write_text(doc(cab, t, s, corpo), encoding="utf-8")
            destino = SAIDA / f"{nome}.pdf"
            subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={destino}", h.as_uri()],
                           check=True, capture_output=True)
            carimbar(destino)
            print(nome, len(pymupdf.open(destino)), "p.")
