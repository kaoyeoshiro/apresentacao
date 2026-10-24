"""Gera os autos fictícios do caso 2 da Aula 2 em kit/casos/caso-2/. Todo nome, número e lugar é inventado.
Uso: python3 caso-2.py [pasta_saida]  (precisa de Chrome e PyMuPDF)."""
import subprocess, sys, pathlib, tempfile
import pymupdf as fitz

AQUI = pathlib.Path(__file__).resolve().parent
SAIDA = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else AQUI.parent.parent / "kit" / "casos" / "caso-2"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CSS = """
@page { size: A4; margin: 24mm 20mm 20mm 20mm; }
body { font: 10.5pt/1.4 Georgia, 'Times New Roman', serif; color: #1a1a1a; }
h1 { font-size: 13.5pt; text-align: center; margin: 0 0 4pt; }
h2 { font-size: 10.5pt; text-align: center; margin: 0 0 12pt; font-weight: normal; }
h3 { font-size: 11pt; margin: 10pt 0 4pt; }
p { margin: 0 0 7pt; text-align: justify; }
.org { text-align: center; font-size: 10pt; margin-bottom: 12pt; line-height: 1.3; border-bottom: 1px solid #999; padding-bottom: 6pt; }
.org b { font-size: 11pt; }
.pg { break-before: page; }
.ass { margin-top: 22pt; text-align: center; font-size: 10.5pt; }
.ass2 { margin-top: 22pt; display: flex; justify-content: space-around; text-align: center; font-size: 10.5pt; }
table { border-collapse: collapse; width: 100%; font-size: 10pt; margin: 4pt 0 8pt; }
td, th { border: 1px solid #777; padding: 3pt 5pt; vertical-align: top; text-align: left; }
.peq { font-size: 9pt; color: #333; }
.dir { text-align: right; }
ul { margin: 0 0 7pt 18pt; padding: 0; } li { margin-bottom: 2pt; }
table.q { font-size: 9pt; } table.q td, table.q th { padding: 2pt 4pt; }
.rec { font-family: Arial, sans-serif; font-size: 10.5pt; line-height: 1.5; }
"""

def doc(corpo):
    return f"<!doctype html><meta charset='utf-8'><style>{CSS}</style>{corpo}"

DPE = "<div class='org'><b>DEFENSORIA PÚBLICA DO ESTADO DE MATO GROSSO DO SUL</b><br>2ª Defensoria Pública de Vila Boa Esperança</div>"
TJ = "<div class='org'><b>PODER JUDICIÁRIO DO ESTADO DE MATO GROSSO DO SUL</b><br>Comarca de Vila Boa Esperança, 2ª Vara</div>"
MED = ("<div class='org rec'><b>Dr. Henrique Salles Venturini</b>, Neurologista<br>CRM/MS 0000 (fictício), Clínica NeuroVida, "
       "Porto Alvorada do Sul/MS</div>")
PROC = "0805173-90.2025.8.12.0099"
PRE = "0900417-63.2024.8.12.0097"
AUTOR = "Anselmo Rocha Teixeira"

INICIAL = DPE + f"""
<p>AO JUÍZO DA ___ VARA DA COMARCA DE VILA BOA ESPERANÇA/MS</p>
<p><b>{AUTOR.upper()}</b>, brasileiro, aposentado, RG nº 000.000 SSP/MS (fictício), CPF nº 000.000.000-00 (fictício), residente na Rua das Acácias, nº 100, Centro, no Município de Santa Rita do Cerrado/MS, por intermédio da DEFENSORIA PÚBLICA DO ESTADO DE MATO GROSSO DO SUL, propõe</p>
<h1>AÇÃO DE OBRIGAÇÃO DE FAZER<br>com pedido de TUTELA DE URGÊNCIA</h1>
<p>contra o <b>ESTADO DE MATO GROSSO DO SUL</b>, representado pelo Procurador-Geral do Estado, e o <b>MUNICÍPIO DE SANTA RITA DO CERRADO</b>, representado por seu prefeito ou procurador, pelos fatos e fundamentos a seguir.</p>
<h3>I. Da gratuidade da justiça</h3>
<p>O requerente afirma, sob as penas da lei, ser juridicamente necessitado e não ter condições de arcar com custas e honorários sem prejuízo do próprio sustento, pelo que requer a gratuidade integral (Lei Complementar Estadual nº 111/2005, art. 1º, § 1º, e CPC, art. 98).</p>
<h3>II. Dos fatos</h3>
<p>O requerente é portador de Doença de Huntington (CID FO22), diagnosticada a partir de dados clínicos, e necessita urgentemente dos medicamentos Austedo (deutetrabenazina) 6 mg, 9 mg e 12 mg, conforme documentos anexos.</p>
<p>A doença é genética e progressiva, e o medicamento prescrito tem finalidade de controle, segundo os itens 2 e 3 do questionário médico juntado. O médico especialista que o atende atesta que não há tratamento fornecido pelo SUS (item 6.3).</p>
<p>O médico da rede pública de saúde afirma que o medicamento é imprescindível para a saúde do requerente e para sua qualidade de vida, e que a falta dele pode causar grave comprometimento do bem-estar (itens 8 e 10 do questionário).</p>
<p>Os requeridos foram acionados administrativamente pelo CEJUSC Saúde, e a Secretaria de Estado de Saúde respondeu que o medicamento “não está incorporado ao SUS. Em vista disso, os servidores estaduais não possuem competência (autorização legal) para fornecê-los”, conforme cópia da reclamação pré-processual anexa. A Secretaria Municipal de Saúde de Santa Rita do Cerrado, por sua vez, informou que não disponibiliza o Austedo 6 mg, 9 mg e 12 mg, por não integrar a relação de medicamentos essenciais.</p>
<h3>III. Dos fundamentos jurídicos</h3>
<p>A saúde é direito social (CF, art. 6º) e dever do Estado, garantido por políticas que assegurem acesso universal e igualitário às ações e serviços de saúde (CF, art. 196), com atendimento integral (CF, art. 198, II). A Lei nº 8.080/1990 reafirma o dever estatal (art. 2º) e inclui no campo de atuação do SUS a assistência terapêutica integral, inclusive farmacêutica (art. 6º, I, “d”).</p>
<p>O Supremo Tribunal Federal reconhece o direito à saúde como direito público subjetivo e consequência indissociável do direito à vida (RE 271.286 AgR), que não pode sofrer embaraços impostos por autoridades administrativas (RE 226.835). Compete ao Estado, portanto, assegurar o tratamento postulado por quem não tem condições de custeá-lo.</p>
<h3>IV. Da tutela de urgência</h3>
<p>A probabilidade do direito está nos laudos, atestados e exames médicos que acompanham a inicial, que comprovam a doença grave, a necessidade do medicamento, a impossibilidade de substituição e as consequências da falta de tratamento. A urgência consta expressamente dos documentos médicos.</p>
<p>O requerente não tem rendimento suficiente para custear o tratamento, pois é aposentado e recebe apenas um salário mínimo, e depende do Estado para cuidar da saúde. Sendo hipossuficiente, requer a dispensa de caução (CPC, art. 300, § 1º). A medida é reversível, porque eventual revogação apenas interromperia o tratamento.</p>
<h3>V. Dos pedidos</h3>
<p>Ante o exposto, requer:</p>
<p>a) a gratuidade da justiça;</p>
<p>b) a tutela de urgência para determinar que os requeridos forneçam o tratamento de saúde do requerente, consubstanciado nos medicamentos Heliocare Max Defense FPS 90 e Helioral 250 mg comprimido, conforme prescrição médica, ou outros que se reputarem necessários para o tratamento da mesma patologia;</p>
<p>c) a dispensa da audiência de mediação e a citação dos requeridos para contestar;</p>
<p>d) ao final, a procedência do pedido, confirmando a tutela, com a condenação dos réus a fornecer Austedo (deutetrabenazina) 6 mg, 9 mg e 12 mg, conforme prescrição médica, ou outros medicamentos que se reputarem necessários para o tratamento da mesma patologia;</p>
<p>e) a fixação de prazo para cumprimento, sob pena de multa diária ou bloqueio de valores;</p>
<p>f) a condenação dos requeridos em custas e honorários em favor da Defensoria Pública;</p>
<p>g) a intimação pessoal do requerente, admitida a intimação eletrônica.</p>
<p>Requer a produção de todas as provas admitidas, em especial a pericial, para confrontar eventual parecer desfavorável do Núcleo de Apoio Técnico, e a oitiva da testemunha abaixo arrolada.</p>
<p>Dá à causa o valor de R$ 44.125,09 (quarenta e quatro mil, cento e vinte e cinco reais e nove centavos), nos termos do art. 292, II, do CPC.</p>
<p>Vila Boa Esperança/MS, data da assinatura digital.</p>
<div class='ass'>Mariana Lopes Andrade<br>Defensora Pública<br>(assinado digitalmente)</div>
<h3 style='margin-top:18pt'>Rol de testemunhas</h3>
<p>1. Henrique Salles Venturini, médico, CRM/MS 0000 (fictício), que pode ser localizado na Secretaria Municipal de Saúde de Santa Rita do Cerrado/MS.</p>
"""

HIPOS = f"""
<div class='org'><b>DEFENSORIA PÚBLICA DO ESTADO DE MATO GROSSO DO SUL</b><br>Defensoria Pública-Geral do Estado</div>
<h1>DECLARAÇÃO</h1><h2>Anexo I, Resolução CSDP nº 198/2019</h2>
<p>Eu, <b>{AUTOR.upper()}</b>, brasileiro, aposentado, RG nº 000.000 SSP/MS (fictício), CPF nº 000.000.000-00 (fictício), residente na Rua das Acácias, nº 100, Centro, Santa Rita do Cerrado/MS, DECLARO, para receber assistência jurídica integral e gratuita da Defensoria Pública de Mato Grosso do Sul, não dispor de recursos financeiros que me permitam, na defesa de meus direitos e interesses extra ou judicialmente, suportar as despesas processuais e o pagamento de honorários advocatícios, sem prejuízo do próprio sustento ou da família.</p>
<p>Declaro estar ciente de que estou sujeito à multa de até 10 (dez) vezes o valor das despesas processuais, caso seja constatada falsidade nesta declaração, e do que dispõe o art. 299 do Código Penal.</p>
<p>Autorizo a Defensoria Pública a requisitar informações de quem quer que as detenha, ainda que isso importe quebra de sigilo profissional, médico, fiscal, bancário e financeiro, e comprometo-me a guardar os documentos originais e a manter meu cadastro atualizado.</p>
<div class='ass'>________________________________<br>Declarante</div>
<p class='dir' style='margin-top:14pt'>Vila Boa Esperança/MS, 10 de fevereiro de 2025.</p>

<div class='pg'></div>
<div class='org'><b>INSS, INSTITUTO NACIONAL DO SEGURO SOCIAL</b><br>Carta de Concessão / Memória de Cálculo do Benefício</div>
<p class='dir peq'>Página 1 de 6. Emitida em 19/06/2024.</p>
<table>
<tr><th style='width:38%'>Nome</th><td>{AUTOR.upper()}</td></tr>
<tr><th>NIT</th><td>000.00000.00-0 (fictício)</td></tr>
<tr><th>Número do benefício</th><td>000.000.000-0 (fictício)</td></tr>
<tr><th>Data de concessão do benefício</th><td>12/11/2022</td></tr>
</table>
<p>Comunicamos que lhe foi concedida <b>APOSENTADORIA POR INCAPACIDADE PERMANENTE PREVIDENCIÁRIA (32)</b>, requerida em 08/09/2022, com <b>renda mensal de R$ 1.302,00</b>, calculada conforme abaixo, com início de vigência a partir de 08/09/2022.</p>
<p>O pagamento será realizado no órgão pagador indicado, no 4º dia útil de cada mês. Deverá apresentar declaração informando se recebe, ou não, pensão por morte em outro regime de previdência, sob pena de suspensão do benefício em 60 dias.</p>
<p class='peq'>Segue, no original, a tabela de salários de contribuição usada no cálculo (Lei nº 9.876/1999). Nos autos foi juntada apenas esta página 1 das 6 da carta.</p>
"""

QUEST = f"""
<h1>QUESTIONÁRIO PARA PEDIDO JUDICIAL DE MEDICAMENTO(S)</h1>
<h2>Preenchido à mão pelo médico assistente (transcrição)</h2>
<table class='q'>
<tr><th style='width:42%'>Paciente</th><td>{AUTOR}</td></tr>
<tr><th>Atendimento que originou a prescrição</th><td>(X) Particular ( ) Convênio ( ) SUS</td></tr>
<tr><th>Medicamentos e posologia</th><td>Austedo 6 mg, 1 comprimido de 12/12 h por 7 dias; Austedo 9 mg, 1 comprimido de 12/12 h por 14 dias; Austedo 12 mg, 1 comprimido de 12/12 h por 7 dias, após manter 2 comprimidos de 12/12 h continuamente</td></tr>
<tr><th>Duração do tratamento</th><td>(X) Contínuo</td></tr>
<tr><th>Registro na ANVISA</th><td>(X) Sim</td></tr>
<tr><th>Previsto em PCDT da doença</th><td>(X) Não</td></tr>
<tr><th>Consta em padronização oficial (REMUME, RENAME etc.)</th><td>sem resposta</td></tr>
<tr><th>Há estudos de evidência científica? Qual?</th><td>(X) Sim. Qual: em branco</td></tr>
</table>
<table class='q'>
<tr><th style='width:42%'>1. Doença e CID</th><td>Doença de Huntington, CID FO22</td></tr>
<tr><th>2. Características da doença</th><td>Coreia progressiva, necessitando da medicação para controle</td></tr>
<tr><th>3. Como é feito o diagnóstico</th><td>(X) Exame laboratorial. Doença genética</td></tr>
<tr><th>4. Finalidade do medicamento</th><td>(X) Paliativa. Reduzir a coreia</td></tr>
<tr><th>5. Existem tratamentos no SUS com a mesma eficácia?</th><td>“Não”</td></tr>
<tr><th>6. As alternativas oferecidas pelo SUS já foram utilizadas?</th><td>( ) Sim (X) Não</td></tr>
<tr><th>6.3. Por que não foram indicados os medicamentos da rede pública?</th><td>“Não há tratamento para a doença no SUS”</td></tr>
<tr><th>7. Pode ser substituído por alternativa do SUS?</th><td>Não</td></tr>
<tr><th>7.1. Vantagens sobre os fármacos do SUS</th><td>Redução acentuada dos sintomas coreicos para melhora da qualidade de vida</td></tr>
<tr><th>8. O medicamento é imprescindível?</th><td>(X) Sim. Melhora da qualidade de vida</td></tr>
<tr><th>9. É urgente?</th><td>(X) Sim</td></tr>
<tr><th>10. Consequência da não utilização imediata</th><td>(X) Grave comprometimento do bem-estar. Não marcados: risco de morte; perda irreversível de órgãos ou funções</td></tr>
<tr><th>11. Quadro clínico</th><td>Coreia progressiva associada a quadro motor e demência</td></tr>
<tr><th>Local, data e médico</th><td>Porto Alvorada do Sul/MS, 20/01/2025. Dr. Henrique Salles Venturini, neurologista, CRM/MS 0000 (fictício)</td></tr>
<tr><th>Campos do paciente (convênio, tentativa no SUS, termo de consentimento)</th><td>Em branco</td></tr>
</table>

<div class='pg'></div>
{MED}
<div class='rec'>
<p><b>{AUTOR.upper()}</b><br>CPF: 000.000.000-00 (fictício)</p>
<p><b>Receituário</b></p>
<p>AUSTEDO (DEUTETRABENAZINA) 6 MG ........ USO CONTÍNUO<br>AUSTEDO (DEUTETRABENAZINA) 9 MG ........ USO CONTÍNUO<br>AUSTEDO (DEUTETRABENAZINA) 12 MG ........ USO CONTÍNUO</p>
<p>SEMANA 1: tomar 1 comprimido de 6 mg pela manhã e à noite<br>
SEMANA 2: tomar 1 comprimido de 9 mg pela manhã e à noite<br>
SEMANA 3: tomar 1 comprimido de 12 mg pela manhã e à noite<br>
SEMANA 4: tomar 1 comprimido de 6 mg e 1 comprimido de 9 mg juntos pela manhã e à noite<br>
SEMANA 5: tomar 2 comprimidos de 9 mg juntos pela manhã e à noite<br>
SEMANA 6: tomar 1 comprimido de 12 mg e 1 comprimido de 9 mg juntos pela manhã e à noite<br>
SEMANA 7: tomar 2 comprimidos de 12 mg juntos pela manhã e à noite</p>
<p>Tomar os comprimidos sempre com alimentos.</p>
<p>OBS.: seguir criteriosamente este receituário, sob risco de baixa resposta ou efeitos adversos.</p>
<p class='dir' style='margin-top:30pt'>24 de novembro de 2024<br>Dr. Henrique Salles Venturini, CRM/MS 0000 (fictício)</p>
<p class='peq'>Os autos trazem duas vias desta receita, de igual teor.</p>
</div>

<div class='pg'></div>
{MED}
<div class='rec'>
<p><b>{AUTOR.upper()}</b></p>
<h1>LAUDO MÉDICO</h1>
<p><b>Histórico clínico e diagnóstico.</b> Paciente do sexo masculino com diagnóstico confirmado de Doença de Huntington, em seguimento desde 2016, com sintomas motores coreicos progressivos associados a distúrbios comportamentais. Apresenta deterioração funcional significativa relacionada à coreia, com impacto severo na qualidade de vida, no autocuidado, na locomoção e na socialização.</p>
<p><b>Tratamento prévio e atual.</b> O paciente foi submetido ao uso de antipsicóticos típicos e atípicos, com resposta clínica insatisfatória:</p>
<ul><li>Haloperidol 2,5 mg à noite: resposta parcial, com sedação significativa e agravamento de sintomas extrapiramidais;</li>
<li>Fenobarbital 100 mg à noite: sem eficácia comprovada para controle motor na doença;</li>
<li>Escitalopram 10 mg pela manhã: mantido para sintomas depressivos.</li></ul>
<p>Apesar dessas tentativas, não houve controle satisfatório da coreia, que continua limitando as atividades da vida diária e exacerbando os sintomas comportamentais.</p>
<p><b>Justificativa para uso de deutetrabenazina (Austedo).</b> A deutetrabenazina é a única medicação com aprovação regulatória específica (FDA e EMA) para a coreia na Doença de Huntington; é inibidor seletivo do VMAT2 e reduz a liberação de dopamina nas vias motoras de forma mais segura e tolerável que a tetrabenazina. Ainda não está incorporada ao SUS, o que pode ser confirmado no site da CONITEC, e não possui substituto terapêutico de eficácia comprovada na lista do SUS. Os antipsicóticos disponíveis são de uso <i>off-label</i>, com evidência científica limitada e maior perfil de efeitos adversos.</p>
<p><b>Evidência científica.</b> Estudos clínicos de alta qualidade, como os ensaios controlados e randomizados First-HD e ARC-HD, demonstraram que a deutetrabenazina reduz de forma estatisticamente significativa a coreia na doença, com melhor perfil de tolerabilidade. Esses estudos já estão disponíveis com tradução juramentada providenciada pela farmacêutica Teva, conforme exigência judicial.</p>
<p><b>Conclusão e recomendação.</b> Diante do quadro motor refratário, da baixa resposta aos medicamentos atualmente disponíveis no SUS e da necessidade de melhorar a qualidade de vida do paciente, indico a deutetrabenazina (Austedo) como única opção clinicamente apropriada e respaldada por evidência científica robusta para o controle da coreia. Solicito a liberação da medicação, sob responsabilidade médica, conforme diretrizes clínicas internacionais.</p>
<p class='dir' style='margin-top:16pt'>24 de novembro de 2024<br>Dr. Henrique Salles Venturini, CRM/MS 0000 (fictício)</p>
</div>

<div class='pg'></div>
<div class='org'><b>GENOMA DIAGNÓSTICOS</b> (laboratório fictício)<br>Laudo de exame genético</div>
<table>
<tr><th style='width:38%'>Nome</th><td>{AUTOR}</td></tr>
<tr><th>Sexo</th><td>Masculino</td></tr>
<tr><th>Solicitante</th><td>Dr. Henrique Salles Venturini, CRM/MS 0000 (fictício)</td></tr>
<tr><th>Sumário clínico</th><td>Investigação molecular de Doença de Huntington</td></tr>
<tr><th>Material</th><td>DNA extraído de swab bucal enviado ao laboratório</td></tr>
<tr><th>Coleta / entrada / liberação</th><td>28/09/2024 / 17/10/2024 / 21/10/2024</td></tr>
<tr><th>Exame</th><td>Doença de Huntington, expansão HTT (programa de apoio ao paciente do fabricante)</td></tr>
</table>
<p><b>Resultado.</b> Foi identificado um alelo com expansão patogênica no gene HTT: alelo 1 com 17 ± 1 repetições CAG; alelo 2 com 47 ± 1 repetições CAG.</p>
<p class='peq'>Referência: alelo normal abaixo de 27 repetições; intermediário de 27 a 35; penetrância incompleta de 36 a 39; patogênico com penetrância completa acima de 39.</p>
<p><b>Método.</b> Análise da expansão de trinucleotídeos (CAG) no gene HTT por <i>triplet repeat primed PCR</i> (TP-PCR). A técnica não distingue se a detecção de um único alelo resulta de homozigose ou de deleção na região analisada.</p>
<p><b>Comentários.</b> O resultado (um alelo normal com 17 repetições e um alelo com expansão patogênica de 47 repetições) confirma a suspeita clínica de Doença de Huntington, distúrbio progressivo de herança autossômica dominante, com probabilidade de 50% de transmissão do alelo patogênico à prole. Recomenda-se aconselhamento genético.</p>
<div class='ass2'><div>Biólogo responsável<br>(fictício)</div><div>Diretor médico<br>(fictício)</div></div>
"""

NEGATIVA = f"""
<div class='org'><b>ESTADO DE MATO GROSSO DO SUL</b><br>Prefeitura Municipal de Santa Rita do Cerrado, Secretaria Municipal de Saúde</div>
<p class='dir'>Santa Rita do Cerrado, 06 de dezembro de 2024.</p>
<h1>DECLARAÇÃO</h1><br>
<p>Em resposta à solicitação feita para o paciente <b>{AUTOR.upper()}</b>, informo que a Secretaria Municipal de Saúde de Santa Rita do Cerrado <b>NÃO</b> disponibiliza os medicamentos <b>Austedo 6 mg, 9 mg e 12 mg (DEUTETRABENAZIDA)</b>, pois não fazem parte do elenco de medicamentos e insumos da Relação Municipal de Medicamentos Essenciais (REMUME), aprovada por resolução do Conselho Municipal de Saúde.</p>
<p>Também não integram a lista de medicamentos e insumos padronizados de responsabilidade da Farmácia da Atenção Básica dos municípios (Portaria nº 1.555/2013, Componente Básico da Assistência Farmacêutica), nem a Relação Estadual de Medicamentos Essenciais (RESME), pactuada pela Comissão Intergestores Bipartite, nem a lista do Componente Especializado da Assistência Farmacêutica (CEAF), aprovada pelas Portarias de Consolidação GM/MS nº 2/2017 e nº 6/2017. Desta maneira, o referido insumo não é fornecido pelo Sistema Único de Saúde (SUS).</p>
<p>Sem mais para o momento,</p>
<div class='ass'>Patrícia Leme Cordeiro<br>Coordenadora da Assistência Farmacêutica<br>Secretaria Municipal de Saúde de Santa Rita do Cerrado</div>

<div class='pg'></div>
<div class='org'><b>SECRETARIA DE ESTADO DE SAÚDE DE MATO GROSSO DO SUL</b></div>
<h1>ANÁLISE MÉDICA</h1>
<p><b>Processo nº {PRE}</b><br><b>Solicitante:</b> {AUTOR}</p>
<p><b>Objeto:</b> análise com fundamento na medicina baseada em evidência para a medicação deutetrabenazina 6 mg, 9 mg e 12 mg (Austedo), na situação enfermidade CID10 G10, conforme informação e documentação médica que acompanham o pedido.</p>
<p><b>Fundamentação:</b> para a situação específica, identificam-se os seguintes fatos nos autos:</p>
<p>1. Apresentação de teste genético (fls. 3): alelo patogênico com 47 repetições.</p>
<p>2. Cita referência bibliográfica (fls. 11): ensaio First-HD<sup>1</sup> e ensaio ARC-HD<sup>2</sup>.</p>
<p><b>Nota:</b> identifica-se, em ambos os ensaios, como critério de elegibilidade, a exigência de não ter, em eletrocardiograma de 12 derivações, intervalo QT prolongado ou arritmia. Não foi apresentado exame de eletrocardiograma para análise e registro.</p>
<p>3. Fica caracterizada a não apresentação de informações que justifiquem a indicação pelo médico prescritor e o preenchimento dos critérios de elegibilidade para uso da medicação. Acontece a não “comprovação de eficácia e segurança do medicamento por ensaios clínicos randomizados e revisões sistemáticas ou meta-análises” para a situação em análise.</p>
<p><b>Conclusão: Desfavorável</b> para a medicação deutetrabenazina 6 mg, 9 mg e 12 mg (Austedo).</p>
<div class='ass'>Dr. Caio Mendes Rangel<br>Assistente Técnico, médico, CRM/MS 0000 (fictício)</div>
<p class='peq' style='margin-top:18pt'>1. Huntington Study Group. Effect of deutetrabenazine on chorea among patients with Huntington disease: a randomized clinical trial. JAMA, 2016.<br>
2. Frank S. et al. Estudo ARC-HD, segurança e eficácia da deutetrabenazina em doses altas e baixas para a coreia na Doença de Huntington. CNS Drugs, 2025.</p>

<div class='pg'></div>
<div class='org'><b>PROCURADORIA-GERAL DO ESTADO DE MATO GROSSO DO SUL<br>SECRETARIA DE ESTADO DE SAÚDE DE MATO GROSSO DO SUL</b></div>
<h1>RESPOSTA À PROVIDÊNCIA DE SAÚDE</h1>
<table>
<tr><th>Siglas</th><th>Número</th><th>Data</th></tr>
<tr><td>PGE / SES</td><td>0418</td><td>20/12/2024</td></tr>
<tr><td colspan='3'><b>De:</b> Procuradoria-Geral do Estado e Secretaria de Estado de Saúde</td></tr>
<tr><td colspan='3'><b>Para:</b> CEJUSC-TJ Saúde (Termo de Cooperação Técnica)</td></tr>
<tr><td colspan='3'><b>Assunto:</b> Solicitação de fornecimento de medicamentos</td></tr>
</table>
<p><b>Processo nº {PRE}</b><br><b>Solicitante:</b> {AUTOR}</p>
<p>Foi solicitado o fornecimento de: 1. Deutetrabenazina 6 mg, 9 mg e 12 mg (Austedo).</p>
<p><b>Análise médica:</b> 1. Desfavorável à deutetrabenazina 6 mg, 9 mg e 12 mg, conforme documento em anexo.</p>
<p><b>Análise técnica:</b> segundo a Relação Nacional de Medicamentos Essenciais (RENAME), a deutetrabenazina <u>não</u> está incorporada ao SUS. Em vista disso, os servidores estaduais não possuem competência (autorização legal) para fornecê-la.</p>
<p><b>Conclusão:</b> <u>Não</u> é possível fornecer deutetrabenazina 6 mg, 9 mg e 12 mg.</p>
<div class='ass2'><div>Lúcia Prado Nogueira<br>Farmacêutica</div><div>Renata Aguiar Pires<br>CEJUR/SES</div></div>
"""

NATJUS = f"""
<div class='org'><b>NÚCLEO DE APOIO TÉCNICO DO JUDICIÁRIO (NATJus)</b><br>Tribunal de Justiça do Estado de Mato Grosso do Sul</div>
<p><b>Autos:</b> {PROC}<br><b>Ação:</b> Procedimento Comum Cível, Vila Boa Esperança, 2ª Vara<br><b>Requerente:</b> {AUTOR.upper()}<br><b>Requeridos:</b> Estado de Mato Grosso do Sul e Município de Santa Rita do Cerrado</p>
<h1>NOTA TÉCNICA DO NATJus Nº 1290/2025</h1><br>
<p><b>I. Enfermidade.</b> Segundo laudo médico e demais documentos, o requerente tem mais de 60 anos, reside em Santa Rita do Cerrado/MS e tem diagnóstico confirmado de Doença de Huntington (CID10 F022) desde 2016, com sintomas motores coreicos progressivos, transtornos comportamentais e deterioração funcional significativa. Não foram apresentados resultados de exames complementares. Solicita deutetrabenazina (Austedo) 6, 9 e 12 mg, conforme prescrição, e Helioral 250 mg e o protetor solar Heliocare Max Defense FPS 90 (não foi identificada prescrição dos protetores via oral e creme). A doença é hereditária, autossômica dominante, e leva à morte 15 a 20 anos após o início dos sintomas neurológicos.</p>
<p><b>II. Tratamentos realizados e alternativas.</b> Segundo documentos médicos e questionário da Defensoria Pública, o paciente foi submetido a diferentes tentativas terapêuticas com antipsicóticos típicos e atípicos (haloperidol, fenobarbital e escitalopram). A tetrabenazina é tratamento de primeira linha para a coreia (grau A), salvo depressão mal controlada ou ideação suicida; neurolépticos de segunda geração (grau B) são primeira linha quando há transtornos comportamentais ou psicóticos associados (diretriz internacional de Bachoud-Lévi e outros, Front Neurol, 2019). A evidência dos antipsicóticos para a coreia é fraca; olanzapina, risperidona, clozapina e quetiapina têm a evidência mais forte entre eles. A amantadina atenua a coreia só em doses altas, com efeitos adversos limitantes, e a estimulação cerebral profunda é promissora em casos refratários.</p>
<p><b>III. Medicamento solicitado.</b> A deutetrabenazina é inibidor reversível do VMAT2, indicada para a coreia associada à Doença de Huntington e para a discinesia tardia em adultos. Reações adversas: sonolência, depressão, ideação suicida, acatisia, agitação, diarreia, fadiga, insônia, ansiedade, entre outras. O Polypodium leucotomos é extrato fitoterápico fotoprotetor; o protetor solar é cosmético.</p>
<p><b>IV. Registro.</b> Deutetrabenazina e Polypodium leucotomos registrados na ANVISA; protetor solar registrado como cosmético.</p>
<p><b>V. Risco iminente à vida.</b> Não há dados clínicos que indiquem risco iminente à vida do paciente.</p>
<p><b>VI. Atendimento na rede pública.</b> O paciente está sendo atendido por médico particular.</p>
<p><b>VII. Disponibilidade no SUS.</b> A deutetrabenazina, o Polypodium leucotomos e os protetores não estão padronizados na RENAME 2024 nem em outro ato normativo do SUS, bem como não foi avaliada pela CONITEC. Há solicitação de incorporação da deutetrabenazina para pacientes adultos com coreia associada à Doença de Huntington, com status “em análise” no portal da CONITEC, sob demanda da empresa Teva Farmacêutica; a tecnologia está em processo de avaliação, ainda sem decisão final publicada.</p>
<p><b>VIII. Ente responsável.</b> Os itens não estão padronizados, portanto não é possível indicar o ente público responsável.</p>
<p><b>IX. Alternativas no SUS.</b> As Diretrizes de Atenção Integral às Pessoas com Doenças Raras (Portarias de Consolidação nº 2 e nº 6/2017), embora não específicas para a Doença de Huntington, indicam o fluxo de atendimento na rede pública. Não há no SUS proteção solar via oral. A RENAME 2024 padroniza antiparkinsoniano (amantadina), antipsicóticos típicos (clorpromazina, haloperidol) e atípicos (olanzapina, risperidona, clozapina, quetiapina) que podem ser utilizados no tratamento da Doença de Huntington.</p>
<p><b>X. Genérico e preço.</b> A deutetrabenazina não tem genérico ou similar. Preços pelo Painel CMED/ANVISA, alíquota de 17%, consultado em 15/03/2025 (PF, preço de fábrica; PMC, preço máximo ao consumidor; PMVG, preço máximo de venda ao governo):</p>
<table>
<tr><th>AUSTEDO (Teva Farmacêutica Ltda.), comprimido revestido de liberação prolongada, frasco com 60</th><th>PF</th><th>PMC</th><th>PMVG</th></tr>
<tr><td>6 mg</td><td>R$ 18.398,72</td><td>R$ 24.681,23</td><td>R$ 14.437,48</td></tr>
<tr><td>9 mg</td><td>R$ 27.598,09</td><td>R$ 37.021,86</td><td>R$ 21.656,22</td></tr>
<tr><td>12 mg</td><td>R$ 36.797,45</td><td>R$ 49.362,47</td><td>R$ 28.874,96</td></tr>
</table>
<p>O Polypodium leucotomos (fitoterápico) e o protetor solar (cosmético) não constam das listas da CMED.</p>
<p><b>XI. Conclusão.</b> Considerando que o paciente é atendido por médico particular; que os itens não estão padronizados na RENAME 2024; que há solicitação de incorporação da deutetrabenazina em análise na CONITEC, sem decisão final; que a RENAME 2024 padroniza amantadina, clorpromazina, haloperidol, olanzapina, risperidona, clozapina e quetiapina, que podem ser usados na Doença de Huntington; que o paciente pode ser encaminhado a centro especializado em doenças raras; que não há evidência contundente sobre formas específicas de proteção solar; as evidências disponíveis, com diretriz internacional que indica a deutetrabenazina como primeira linha e os antipsicóticos como segunda linha, os tratamentos realizados e os exames apresentados; que não foi identificado nos autos pedido médico referente ao item “b” dos pedidos da inicial; a ausência de evidências científicas apresentadas, a falta de informações sobre tratamentos previamente realizados, a inexistência de laudos complementares e a disponibilidade de outras opções terapêuticas no SUS; e que não foram apresentados os documentos comprobatórios dos requisitos exigidos para medicamentos não incorporados nos Temas nº 1.234 e nº 6 do STF, este Núcleo manifesta-se <b>desfavorável</b> ao pedido de deutetrabenazina nas dosagens solicitadas, de Polypodium leucotomos e de protetor solar.</p>
<p class='dir'>15 de março de 2025.</p>
<div class='ass'>Equipe técnica do NATJus (médicos, enfermeiros e farmacêuticos)<br>(assinado digitalmente)</div>
"""

TUTELA = TJ + f"""
<p><b>Processo nº {PROC}</b><br>Classe: Procedimento Comum Cível<br>Autor: {AUTOR}<br>Réu: Estado de Mato Grosso do Sul e outro<br>Valor da causa: R$ 44.125,09</p>
<h1>DECISÃO</h1><br>
<p>Vistos. Trata-se de ação de conhecimento proposta por {AUTOR} em face do Estado de Mato Grosso do Sul e outro. Aduz ser portador da Doença de Huntington e necessitar de medicamento com princípio ativo deutetrabenazina, nas dosagens de 6, 9 e 12 mg. Requer tutela de urgência, sem oitiva da parte contrária, para obrigar os requeridos a fornecer ou custear os medicamentos. Juntou documentos. O NAT emitiu parecer desfavorável.</p>
<p>Fundamento e decido. Analisando a petição inicial e os documentos, interpreto que há erro material no pedido liminar do item “b”, e que deve constar como objeto a deutetrabenazina nas dosagens de 6, 9 e 12 mg. A análise da tutela se concentrará nessa droga. Caso o pedido se refira de fato aos produtos descritos naquele item, ou os abranja além da deutetrabenazina, a parte deverá esclarecer por nova petição.</p>
<p>A tutela exige elementos que evidenciem a probabilidade do direito e o perigo de dano ou o risco ao resultado útil do processo (CPC, art. 300). Em cognição sumária, a probabilidade do direito não está presente. Para os pedidos de medicamentos não incorporados à RENAME, devem ser atendidos os requisitos dos Temas 6 e 1.234 do STF, entre eles a “ilegalidade do ato de não incorporação do medicamento pela Conitec, ausência de pedido de incorporação ou da mora na sua apreciação, tendo em vista os prazos e critérios previstos nos artigos 19-Q e 19-R da Lei nº 8.080/1990 e no Decreto nº 7.646/2011”, o que não ocorre no caso.</p>
<p>Em consulta ao site da Conitec, o medicamento Austedo está com pedido de incorporação em análise, protocolado em 10/02/2025. O art. 19-R da Lei nº 8.080/1990 fixa o prazo de 180 dias para a decisão de incorporação, prorrogável por mais 90, contado do protocolo, previsão ratificada pelo art. 24 do Decreto nº 7.646/2011. Portanto, a priori, inexiste mora na apreciação do requerimento, e a pretensão carece de um dos requisitos legais. Assim, <b>INDEFIRO</b> o pedido liminar.</p>
<p>No mais: 1. Concedo à parte autora os benefícios da gratuidade da justiça (CPC, art. 98). 2. Observada recomendação do Conselho Superior da Magistratura, deixo de designar audiência de conciliação, sem prejuízo de composição a qualquer tempo. 3. Cite-se o réu para apresentar resposta no prazo legal (CPC, arts. 335 e 183), com a advertência do art. 344 do CPC. 4. Após a contestação, intime-se a parte autora para impugnação em 15 dias e, em seguida, as partes para especificar provas em 5 dias. 5. Após, conclusos para saneamento ou sentença.</p>
<p class='dir'>Vila Boa Esperança, 17 de março de 2025.</p>
<div class='ass'>Carolina Duarte Mesquita<br>Juíza de Direito<br>(assinado digitalmente)</div>
"""

INCOMP = TJ + f"""
<p><b>Processo nº {PROC}</b><br>Classe: Procedimento Comum Cível<br>Autor: {AUTOR}<br>Réu: Estado de Mato Grosso do Sul e outro</p>
<h1>DECISÃO</h1><br>
<p>Vistos. Trata-se de ação de conhecimento proposta por {AUTOR} em face do Estado de Mato Grosso do Sul e outro, em que busca compelir os requeridos a custear ou fornecer o medicamento deutetrabenazina nas dosagens de 6, 9 e 12 mg para o tratamento de sua doença.</p>
<p>Sobre a competência nas demandas de saúde, o STF fixou a seguinte tese no Tema 1.234:</p>
<p style='margin-left:30pt; font-size:10pt'>“Para fins de fixação de competência, as demandas relativas a medicamentos não incorporados na política pública do SUS e medicamentos oncológicos, ambos com registro na ANVISA, tramitarão perante a Justiça Federal, nos termos do art. 109, I, da Constituição Federal, quando o valor do tratamento anual específico do fármaco ou do princípio ativo, com base no Preço Máximo de Venda do Governo (PMVG – situado na alíquota zero), divulgado pela Câmara de Regulação do Mercado de Medicamentos (CMED - Lei 10.742/2003), for igual ou superior ao valor de 210 salários mínimos, na forma do art. 292 do CPC”.</p>
<p>No caso, o parecer do NATJus esclareceu que o custo da caixa do medicamento nas dosagens de 6, 9 e 12 mg é, respectivamente, de R$ 14.437,48, R$ 21.656,22 e R$ 28.874,96 (item X). Além disso, o Questionário para Pedido Judicial de Medicamento, preenchido pelo médico que acompanha o autor, indica que o tratamento é contínuo.</p>
<p>Assim, verifica-se que o custo anual do tratamento supera o limite de alçada da Justiça Estadual, o que atrai a necessidade de a União compor o polo passivo, razão pela qual o processo deve ser remetido à Justiça Federal.</p>
<p>Posto isso, <b>reconheço a incompetência deste Juízo</b> e determino a remessa dos autos à Subseção Judiciária de Lagoa Clara da Justiça Federal em Mato Grosso do Sul, competente para processar e julgar o feito. Sem condenação em custas, pois defiro ao autor a justiça gratuita. Com o trânsito em julgado, procedam-se às anotações e baixas e remetam-se os autos ao juízo competente.</p>
<p class='dir'>Vila Boa Esperança, 16 de janeiro de 2026.</p>
<div class='ass'>Carolina Duarte Mesquita<br>Juíza de Direito<br>(assinado digitalmente)</div>
"""

CUSTOS = """
<div class='org'><b>PROCURADORIA-GERAL DO ESTADO DE MATO GROSSO DO SUL</b></div>
<h1>PARECER TÉCNICO</h1><h2>Documento sem data e sem número no original</h2>
<h3>I. Identificação do tratamento</h3>
<p>O parecer analisa a necessidade, a adequação terapêutica e o custo estimado do tratamento com Austedo (deutetrabenazina), conforme a prescrição médica que consta do laudo do paciente. Trata-se de medicamento de uso contínuo, indicado para os movimentos involuntários (coreia) na Doença de Huntington, cuja interrupção compromete a eficácia terapêutica e a evolução clínica do paciente.</p>
<h3>II. Esquema terapêutico prescrito, 1ª etapa (titulação de 7 semanas)</h3>
<table>
<tr><th>Semana</th><th>Posologia</th><th>Total na semana</th></tr>
<tr><td>1ª</td><td>1 cp de 6 mg pela manhã e à noite</td><td>14 cp de 6 mg</td></tr>
<tr><td>2ª</td><td>1 cp de 9 mg pela manhã e à noite</td><td>14 cp de 9 mg</td></tr>
<tr><td>3ª</td><td>1 cp de 12 mg pela manhã e à noite</td><td>14 cp de 12 mg</td></tr>
<tr><td>4ª</td><td>1 cp de 6 mg e 1 de 9 mg pela manhã e à noite</td><td>14 cp de 6 mg e 14 de 9 mg</td></tr>
<tr><td>5ª</td><td>2 cp de 9 mg pela manhã e à noite</td><td>28 cp de 9 mg</td></tr>
<tr><td>6ª</td><td>1 cp de 12 mg e 1 de 9 mg pela manhã e à noite</td><td>14 cp de 12 mg e 14 de 9 mg</td></tr>
<tr><td>7ª</td><td>2 cp de 12 mg pela manhã e à noite</td><td>28 cp de 12 mg</td></tr>
</table>
<p>Quantitativo total da 1ª etapa: 28 comprimidos de 6 mg, 70 de 9 mg e 56 de 12 mg. O medicamento é vendido só em caixas fechadas de 60 comprimidos, o que impõe a aquisição mínima de 1 caixa de 6 mg, 2 caixas de 9 mg e 1 caixa de 12 mg.</p>
<h3>III. Custos da 1ª etapa</h3>
<p>Valores calculados conforme a Tabela CMED vigente à época da elaboração deste parecer: 6 mg, R$ 14.437,48; 9 mg, R$ 21.656,22 por caixa (2 caixas, R$ 43.312,44); 12 mg, R$ 28.874,96. Valor total estimado da 1ª etapa (7 semanas): <b>R$ 86.624,88</b>.</p>
<h3>IV. 2ª etapa (uso contínuo)</h3>
<p>Após a titulação, o paciente manterá 2 comprimidos de 12 mg pela manhã e 2 à noite, isto é, 120 comprimidos de 12 mg por mês, com custo mensal estimado de <b>R$ 57.749,92</b>. Considerando o período remanescente de 10 meses e meio até o fim do ano, o custo total estimado da 2ª etapa é de <b>R$ 606.374,16</b>.</p>
<h3>V. Custo total estimado do tratamento anual</h3>
<p>1ª etapa (7 semanas): R$ 86.624,88. 2ª etapa (uso contínuo): R$ 606.374,16.<br>Valor total estimado para 12 meses de tratamento: <b>R$ 692.999,04</b>.</p>
<div class='ass'>Renata Aguiar Pires<br>Farmacêutica, CRF/MS 0000 (fictício)</div>
"""

DOCS = [
    ("01-peticao-inicial", INICIAL),
    ("02-declaracao-hipossuficiencia-e-renda", HIPOS),
    ("03-questionario-receita-e-laudo", QUEST),
    ("04-negativa-administrativa", NEGATIVA),
    ("05-nota-tecnica-natjus", NATJUS),
    ("06-decisao-tutela", TUTELA),
    ("07-decisao-incompetencia", INCOMP),
    ("08-parecer-custos", CUSTOS),
]

def carimbar(caminho):
    d = fitz.open(caminho)
    n = len(d)
    for i, pg in enumerate(d):
        w = pg.rect.width
        pg.insert_text((56, 34), "Autos fictícios, material didático", fontsize=8, fontname="helv", color=(0.4, 0.4, 0.4))
        t = f"Página {i+1} de {n}"
        pg.insert_text((w - 56 - fitz.get_text_length(t, "helv", 8), 34), t, fontsize=8, fontname="helv", color=(0.4, 0.4, 0.4))
        pg.draw_line((56, 40), (w - 56, 40), color=(0.7, 0.7, 0.7), width=0.5)
    tmp = pathlib.Path(str(caminho) + ".tmp")
    d.save(str(tmp)); d.close()
    tmp.replace(caminho)

if __name__ == "__main__":
    SAIDA.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        for nome, corpo in DOCS:
            h = pathlib.Path(td) / f"{nome}.html"
            h.write_text(doc(corpo), encoding="utf-8")
            destino = SAIDA / f"{nome}.pdf"
            subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={destino}", h.as_uri()],
                           check=True, capture_output=True)
            carimbar(destino)
            print(nome, len(fitz.open(destino)), "p.")
