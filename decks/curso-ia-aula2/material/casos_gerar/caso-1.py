"""Gera os autos fictícios do caso 1 da Aula 2 (omalizumabe, urticária crônica espontânea) em PDF.
Todo o texto é fictício e anonimizado, criado para fins didáticos.
Uso: python3 caso-1.py [pasta_saida]  (padrão: ../../kit/casos/caso-1; precisa de Chrome e PyMuPDF)"""
import subprocess, sys, pathlib, tempfile
import pymupdf as fitz

AQUI = pathlib.Path(__file__).resolve().parent
SAIDA = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else AQUI.parent.parent / "kit" / "casos" / "caso-1"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PROC = "0806842-39.2026.8.12.0099"
AUTORA = "VALDIRENE SOUZA PRADO"

CSS = """
@page { size: A4; margin: 24mm 20mm 20mm 20mm; }
body { font: 11.5pt/1.5 Georgia, 'Times New Roman', serif; color: #1a1a1a; }
h1 { font-size: 13.5pt; text-align: center; margin: 0 0 4pt; letter-spacing: .02em; }
h2 { font-size: 10.5pt; text-align: center; margin: 0 0 14pt; font-weight: normal; }
h3 { font-size: 11pt; margin: 12pt 0 5pt; }
p { margin: 0 0 7pt; text-align: justify; }
.cab { text-align: center; font-size: 10pt; margin-bottom: 12pt; border-bottom: 1px solid #999; padding-bottom: 6pt; }
.dir { text-align: right; }
.ass { margin-top: 26pt; text-align: center; font-size: 10.5pt; }
.ass div { display: inline-block; border-top: 1px solid #333; padding-top: 4pt; min-width: 240pt; }
table { border-collapse: collapse; width: 100%; font-size: 10pt; margin: 4pt 0 10pt; }
td, th { border: 1px solid #888; padding: 3pt 5pt; text-align: left; vertical-align: top; }
th { background: #eee; }
.mono { font-family: 'Courier New', monospace; }
.peq { font-size: 9.5pt; color: #444; }
.quebra { page-break-before: always; }
ul { margin: 0 0 7pt 18pt; padding: 0; }
"""

def doc(corpo):
    return f"<!doctype html><meta charset='utf-8'><style>{CSS}</style>{corpo}"

DOCS = {}

DOCS["01-peticao-inicial"] = f"""
<p><b>EXCELENTÍSSIMO SENHOR JUIZ DE DIREITO DA __ª VARA CÍVEL DA COMARCA DE VILA BOA ESPERANÇA/MS</b></p>
<p>&nbsp;</p>
<p><b>{AUTORA}</b>, brasileira, convivente, aposentada, CPF [omitido no material didático], residente na Rua dos Ipês, nº 48, Jardim Primavera, nesta cidade de Vila Boa Esperança/MS, representada por seu advogado signatário, propõe a presente <b>AÇÃO DE OBRIGAÇÃO DE FAZER COM PEDIDO DE TUTELA DE URGÊNCIA</b> em face do <b>ESTADO DE MATO GROSSO DO SUL</b>, pessoa jurídica de direito público, e do <b>MUNICÍPIO DE VILA BOA ESPERANÇA</b>, pessoa jurídica de direito público, pelos fatos e fundamentos a seguir.</p>
<h3>Da assistência judiciária gratuita</h3>
<p>A requerente não tem condições de pagar custas, taxas e honorários sem prejuízo do próprio sustento e requer os benefícios da gratuidade (art. 4º da Lei nº 1.060/1950 e art. 5º, LXXIV, da Constituição Federal).</p>
<h3>Da audiência de conciliação</h3>
<p>A autora informa que não tem interesse na audiência de conciliação (art. 319, VII, do CPC).</p>
<h3>Dos fatos</h3>
<p>A autora tem Urticária Crônica Espontânea (UCE), CID-10 L50.1, doença inflamatória da pele com episódios recorrentes de lesões que coçam intensamente e aparecem sem causa aparente, com grande prejuízo à qualidade de vida, ao sono e ao bem-estar físico e emocional, conforme documentos em anexo.</p>
<p>A requerente faz tratamento há vários anos, mas o tratamento convencional otimizado não surte efeito, apesar do uso de medicação nas doses máximas recomendadas. Foi instituído tratamento com anti-histamínico H1 de segunda geração, Bilastine em dose quadruplicada, mantido por mais de 4 meses, sem controle adequado da doença e sem resposta clínica satisfatória, conforme laudo médico em anexo. Segundo o médico que acompanha a autora há anos, o único medicamento indicado para a cura ou melhora da enfermidade é o OMALIZUMAB 300 MG.</p>
<p>O medicamento tem preço muito alto: cada seringa custa em média de R$ 5.500,00 a R$ 8.000,00 em farmácias e grandes redes, podendo passar de R$ 10.000,00 conforme a região, o ICMS local e o distribuidor. Esses valores foram pesquisados na internet, porque a medicação é de alto custo e não se encontra em farmácias convencionais; por essa razão não seguem orçamentos em anexo, mas apenas a pesquisa via internet.</p>
<p>A autora precisa aplicar o Omalizumab 300 mg, por via subcutânea, a cada 4 semanas, por período inicial de 6 meses, com reavaliação clínica periódica para continuidade ou não da medicação, conforme prescrição em anexo, ou seja, 7 seringas do medicamento.</p>
<p>A autora é aposentada e recebe por mês 1 salário mínimo, atualmente de R$ 1.621,00, proveniente da aposentadoria (vide extrato em anexo); seu convivente trabalha como autônomo e recebe em média o mesmo valor, de modo que a renda familiar não ultrapassa 2 salários mínimos. Com esse montante a autora paga água, luz, telefone, outros medicamentos, alimentação e vestuário, valor manifestamente insuficiente para comprar o medicamento.</p>
<p>A autora requereu o fornecimento do medicamento à Secretaria de Saúde do Município de Vila Boa Esperança, porém restou frustrado o requerimento, haja vista que a medicação, de alto custo, não consta na lista para distribuição de medicamentos.</p>
<p>O quadro de saúde da autora é delicado e o medicamento é essencial, porque é a única possibilidade de melhora ou cura; a falta de acesso ao fármaco traz risco iminente de agravamento.</p>
<h3>Do direito</h3>
<p>A saúde é direito de todos e dever do Estado (art. 196 da Constituição Federal; arts. 173 e 175 da Constituição Estadual). União, Estados e Municípios têm obrigação solidária de garantir a saúde, o que inclui atendimento, tratamento e medicamentos, como reconhecem diversos julgados de tribunais estaduais que a autora transcreve. Ao não disponibilizar o medicamento prescrito, os requeridos violaram direito fundamental.</p>
<h3>Da tutela provisória de urgência</h3>
<p>Estão presentes os requisitos do art. 300 do CPC. A probabilidade do direito decorre do dever constitucional dos entes e dos documentos médicos que demonstram a necessidade do Omalizumab 300 mg. O perigo de dano está em que, sem o medicamento, a autora continuará com intenso sofrimento físico e emocional, coceira, irritabilidade e prejuízo ao sono, conforme laudo em anexo. A medida é reversível.</p>
<p>Requer a tutela de urgência, sem ouvir a parte contrária, para que os requeridos, intimados na pessoa dos secretários estadual e municipal de saúde, forneçam em 48 horas o OMALIZUMAB 300 MG (inicialmente 7 seringas), necessário para 6 meses de tratamento ou enquanto for indicado pelo médico, sob pena de multa diária.</p>
<h3>Dos pedidos</h3>
<p>Diante do exposto, requer:</p>
<p>a) a não designação de audiência de conciliação ou mediação;</p>
<p>b) a concessão da justiça gratuita, pois a autora não pode arcar com as custas sem prejuízo do próprio sustento e de sua família, conforme declarado e comprovado pelos documentos em anexo;</p>
<p>c) a concessão da tutela de urgência, sem ouvir a parte contrária, para que os requeridos forneçam em 48 horas o OMALIZUMAB 300 MG (8 seringas), suficiente para 6 meses de tratamento ou enquanto for indicado pelo médico, sob pena de multa diária;</p>
<p>d) a citação dos requeridos para, querendo, apresentar defesa no prazo legal;</p>
<p>e) ao final, a procedência do pedido, confirmando a tutela, para condenar os requeridos a fornecer em 48 horas o OMALIZUMAB 300 MG (8 seringas) ou enquanto for indicado pelo médico, sob pena de multa diária, com juros, correção, custas e honorários.</p>
<p>Protesta por todos os meios de prova admitidos, embora as entenda desnecessárias, por ser a questão de direito.</p>
<p>Dá à causa o valor de R$ 44.000,00 (quarenta e quatro mil reais).</p>
<p>Nestes termos, pede deferimento.</p>
<p class="dir">Vila Boa Esperança/MS, 16 de março de 2026.</p>
<div class="ass"><div>RENATO ALVES CARDOSO<br>Advogado, OAB/MS 98.765</div></div>
"""

DOCS["02-hipossuficiencia"] = f"""
<div class="cab"><b>RENATO ALVES CARDOSO</b>, Advogado, OAB/MS 98.765</div>
<h1>DECLARAÇÃO</h1>
<h2>&nbsp;</h2>
<p><b>{AUTORA}</b>, brasileira, convivente, CPF [omitido no material didático], residente na Rua dos Ipês, nº 48, Jardim Primavera, Vila Boa Esperança/MS, <b>DECLARA</b>, para fins de concessão da assistência judiciária gratuita, que não dispõe de recursos para arcar com despesas judiciais, honorários advocatícios, custas processuais e taxas de certidões, por ser pobre e pela real dificuldade financeira que atravessa, sem prejuízo do próprio sustento. Faz esta declaração sob sua inteira responsabilidade, sujeitando-se, em caso de falsidade, às sanções civis, administrativas e criminais, nos termos do art. 4º da Lei nº 1.060/1950 e da Lei nº 7.510.</p>
<p class="dir">Vila Boa Esperança/MS, 26 de janeiro de 2026.</p>
<div class="ass"><div>{AUTORA}</div></div>

<div class="quebra"></div>
<div class="cab">Ministério do Desenvolvimento e Assistência Social, Família e Combate à Fome<br>Secretaria de Avaliação, Gestão da Informação e Cadastro Único</div>
<h1>COMPROVANTE DE CADASTRO</h1>
<h2>Sua família está cadastrada no Cadastro Único para Programas Sociais do Governo Federal</h2>
<table>
<tr><th>Código familiar</th><td>[omitido]</td><th>Data de cadastro</th><td>18/12/2008</td></tr>
<tr><th>Última atualização</th><td>01/12/2025</td><th>Cadastro atualizado</th><td>SIM</td></tr>
<tr><th>Faixa de renda familiar total</th><td>Entre meio e um salário mínimo</td><th>Faixa de renda familiar por pessoa (per capita)</th><td>Entre R$ 210,01 até meio salário mínimo</td></tr>
<tr><th>Município de cadastramento</th><td colspan="3">VILA BOA ESPERANÇA/MS</td></tr>
<tr><th>Endereço</th><td colspan="3">JARDIM PRIMAVERA, RUA DOS IPÊS, 48</td></tr>
</table>
<p><b>Integrantes da família</b></p>
<table>
<tr><th>Nome</th><th>Estado cadastral</th><th>Parentesco com o responsável familiar</th></tr>
<tr><td>{AUTORA}</td><td>Cadastrado</td><td>Pessoa responsável pela unidade familiar</td></tr>
<tr><td>LUCAS SOUZA PRADO</td><td>Cadastrado</td><td>Filho(a)</td></tr>
</table>
<h1 style="margin-top:22pt">FOLHA RESUMO, CADASTRO ÚNICO</h1>
<table>
<tr><th>Data da entrevista</th><td>01/12/2025</td></tr>
<tr><th>Renda per capita da família</th><td>R$ 810,00</td></tr>
<tr><th>Responsável familiar</th><td>{AUTORA}</td></tr>
<tr><th>Componente</th><td>LUCAS SOUZA PRADO, filho(a)</td></tr>
</table>
<p class="peq">Vila Boa Esperança/MS, 01/12/2025. Assinatura do entrevistador responsável pelo cadastramento.</p>

<div class="quebra"></div>
<div class="cab">Concessionária de energia elétrica<br>Documento auxiliar da nota fiscal de energia elétrica</div>
<h1>CONTA DE ENERGIA ELÉTRICA</h1>
<h2>&nbsp;</h2>
<table>
<tr><th>Titular</th><td>{AUTORA}</td></tr>
<tr><th>Endereço da unidade</th><td>Rua dos Ipês, 48, Jardim Primavera, Vila Boa Esperança/MS</td></tr>
<tr><th>Classificação</th><td>Convencional baixa tensão, residencial, Desconto Social (Tarifa Social de Energia Elétrica)</td></tr>
<tr><th>Referência</th><td>dezembro/2025</td></tr>
<tr><th>Vencimento</th><td>20/01/2026</td></tr>
<tr><th>Total a pagar</th><td>R$ 257,11</td></tr>
</table>
"""

DOCS["03-laudo-medico"] = """
<div class="cab"><b>Clínica AlergoVida, Alergia e Imunologia Clínica</b><br>Rua das Acácias, 120, Centro<br>Dr. Henrique Lacerda Moraes, CRM/MS 99.512</div>
<h1>RELATÓRIO MÉDICO</h1>
<h2>Laudo médico para solicitação de omalizumabe. Data de emissão: 22/01/2026</h2>
<p><b>Paciente:</b> Valdirene Sousa Prado. <b>Idade:</b> entre 40 e 50 anos.</p>
<h3>Relatório médico circunstanciado</h3>
<p>Declaro, para os devidos fins, que a paciente Valdirene Sousa Prado está em acompanhamento médico especializado por quadro de <b>Urticária Crônica Espontânea (UCE)</b>, doença inflamatória cutânea crônica, com episódios recorrentes de urticas intensamente pruriginosas, de aparecimento espontâneo, e importante comprometimento da qualidade de vida, do sono e do bem-estar físico e emocional.</p>
<p>A paciente tem quadro persistente e refratário ao tratamento convencional otimizado, com atividade significativa da doença apesar da terapêutica em doses máximas recomendadas. Foi instituído tratamento com anti-histamínico H1 de segunda geração, <b>Bilastine em dose quadruplicada</b>, mantido por período superior a <b>4 meses</b>, sem controle adequado da doença e sem resposta clínica satisfatória.</p>
<p>A atividade da doença foi documentada por instrumentos validados internacionalmente:</p>
<ul>
<li>UAS7 (Urticaria Activity Score, 7 dias) em setembro/2025: 42 pontos, compatível com atividade grave;</li>
<li>UAS7 atual: 27 pontos, atividade moderada a grave apesar do tratamento otimizado;</li>
<li>UCT (Urticaria Control Test) atual: 3 pontos, doença completamente não controlada.</li>
</ul>
<p>Foi feita investigação laboratorial complementar para excluir causas secundárias de urticária crônica, sem evidência de etiologia alternativa, o que corrobora o diagnóstico de Urticária Crônica Espontânea refratária.</p>
<h3>Diagnóstico</h3>
<p>Urticária Crônica Espontânea (CID-10: L50.1).</p>
<h3>Justificativa técnica para omalizumabe</h3>
<p>A paciente tem falha terapêutica documentada ao tratamento de primeira linha otimizado, tendo utilizado anti-histamínico H1 de segunda geração em dose até quatro vezes superior à habitual, conforme recomendado por consensos internacionais e nacionais para o manejo da urticária crônica espontânea.</p>
<p>Segundo diretrizes internacionais da urticária crônica (EAACI/GA²LEN/EuroGuiDerm/APAAACI), pacientes com UCE não controlada após uso de anti-histamínicos em dose quadruplicada têm indicação formal de tratamento com Omalizumab, considerado terapia de escolha nesta etapa, com comprovada eficácia, segurança e melhora substancial do controle clínico e da qualidade de vida.</p>
<p>A persistência da atividade inflamatória expõe a paciente a intenso sofrimento físico e emocional, prurido persistente e lesões recorrentes, prejuízo do sono e da funcionalidade diária e necessidade potencial de corticosteroides sistêmicos de repetição, terapia não recomendada cronicamente pelos riscos cumulativos.</p>
<p>Diante da refratariedade demonstrada e da gravidade medida por escores validados, o uso do omalizumabe é medida médica necessária, baseada em evidências científicas e diretrizes internacionais, não havendo alternativa terapêutica disponível com eficácia comparável neste contexto clínico.</p>
<h3>Prescrição médica</h3>
<p>Omalizumab 300 mg, via subcutânea, a cada 4 semanas, por período inicial de 6 meses, com reavaliação clínica periódica por UAS7 e UCT.</p>
<h3>Conclusão</h3>
<p>A paciente tem Urticária Crônica Espontânea grave e não controlada, refratária ao tratamento convencional otimizado com anti-histamínico em dose quadruplicada, e preenche critério técnico-científico formal para uso de omalizumabe, tratamento imprescindível para controle da doença, prevenção de agravamento clínico e recuperação da qualidade de vida. Solicita-se com urgência o fornecimento do medicamento Omalizumabe 300 mg via subcutânea a cada 4 semanas, diante da necessidade clínica e da ausência de resposta às terapias previamente instituídas.</p>
<div class="ass"><div>Dr. Henrique Lacerda Moraes<br>CRM/MS 99.512 (assinado digitalmente em 22/01/2026)</div></div>
"""

DOCS["04-receita"] = """
<div class="cab"><b>Clínica AlergoVida, Alergia e Imunologia Clínica</b><br>Rua das Acácias, 120, Centro<br>Dr. Henrique Lacerda Moraes, CRM/MS 99.512</div>
<h1>RECEITA SIMPLES</h1>
<h2>Data de emissão: 22/01/2026. Data de validade: 21/02/2026</h2>
<p><b>Paciente:</b> Valdirene Sousa Prado</p>
<p>&nbsp;</p>
<p class="mono">1. OMALIZUMABE 300 MG ............................ USO CONTÍNUO</p>
<p class="mono">&nbsp;&nbsp;&nbsp;Aplicar 300 mg por via subcutânea a cada 4 semanas.</p>
<div class="ass" style="margin-top:60pt"><div>Dr. Henrique Lacerda Moraes<br>CRM/MS 99.512 (assinado digitalmente em 22/01/2026)</div></div>
"""

DOCS["05-pesquisa-de-preco"] = """
<p class="peq">Impressão de páginas da internet juntada pela autora.</p>
<h1>Quanto custa o omalizumabe?</h1>
<h2>Faixa de preço no Brasil</h2>
<p>O omalizumabe (Xolair) é comercializado no Brasil em duas apresentações, 150 mg/mL e 300 mg/mL, em seringa preenchida. Os preços variam conforme o canal de compra (farmácias especializadas, distribuidoras hospitalares e CMED), o tipo de contrato e a apresentação. Referência de mercado em 2026:</p>
<table>
<tr><th>Apresentação</th><th>Preço estimado (por seringa)</th><th>Canal</th></tr>
<tr><td>Xolair 150 mg/mL (1 seringa)</td><td>R$ 2.800 a R$ 4.200</td><td>Farmácia especializada / CMED</td></tr>
<tr><td>Xolair 300 mg/mL (1 seringa)</td><td>R$ 5.500 a R$ 8.000</td><td>Farmácia especializada / CMED</td></tr>
<tr><td>Hospitalar / distribuidoras</td><td>Preço negociado, pode ser menor</td><td>Compra institucional</td></tr>
</table>
<p>Os preços são estimativas de mercado para 2026. O valor exato varia conforme a farmácia, o canal de compra, descontos de programas do fabricante e a tabela CMED vigente. Consulte sempre a farmácia ou distribuidora antes de qualquer decisão de compra.</p>
<h3>Resultado de buscador: "Xolair 300mg preço" (visão geral criada por IA)</h3>
<p>O Xolair 300 mg (omalizumabe) custa em média entre R$ 4.500 e R$ 8.000 por seringa preenchida no mercado brasileiro. O valor muda conforme a farmácia, os impostos de cada estado e a regulação da CMED.</p>
<ul>
<li>Preço por seringa de 300 mg: R$ 4.500 a R$ 8.000.</li>
<li>Preço por seringa de 150 mg: R$ 2.700 a R$ 4.425 (muitos tratamentos usam a combinação de ampolas).</li>
<li>Custo mensal estimado: de R$ 5.000 a mais de R$ 13.000 por mês, conforme a quantidade de aplicações necessária para o peso e o nível de IgE do paciente.</li>
</ul>
"""

DOCS["06-nota-tecnica-natjus"] = f"""
<div class="cab">Tribunal de Justiça do Estado de Mato Grosso do Sul<br><b>Núcleo de Apoio Técnico do Judiciário (NATJus)</b></div>
<h1>NOTA TÉCNICA DO NATJUS Nº 1147/2026</h1>
<h2>Autos: {PROC} (fictício). Procedimento Comum Cível, Comarca de Vila Boa Esperança, 1ª Vara<br>Requerente: Valdirene Souza Prado. Requeridos: Estado de Mato Grosso do Sul e Município de Vila Boa Esperança</h2>
<h3>I. Enfermidade e linha terapêutica do SUS</h3>
<p>Segundo o laudo médico e os demais documentos, a requerente, na faixa de 40 a 50 anos, reside no município de Vila Boa Esperança/MS e tem Urticária Crônica Espontânea (CID-10 L50.1). Foram apresentados resultados de exames laboratoriais complementares.</p>
<table>
<tr><th>Princípio ativo</th><th>Posologia</th><th>Incorporado ao SUS?</th></tr>
<tr><td>Omalizumabe</td><td>300 mg, via SC, a cada 4 semanas</td><td>SIM*</td></tr>
</table>
<p class="peq">* O medicamento solicitado está incorporado para patologia/CID diferente da apresentada pela paciente.</p>
<p>A UCE caracteriza-se por urticas e/ou angioedema recorrentes por mais de seis semanas, sem fator desencadeante identificado, com prurido intenso, distúrbios do sono e repercussões emocionais. O diagnóstico é clínico.</p>
<h3>II. Tratamentos realizados e alternativas</h3>
<p>Segundo os documentos médicos, a paciente usou Bilastina em dose quadruplicada por mais de 4 meses, sem resposta clínica satisfatória, e foi orientada a evitar Dipirona e anti-inflamatórios não esteroides, usando Paracetamol em caso de dor ou febre. Não constam nos autos informações sobre outros tratamentos farmacológicos e não farmacológicos eventualmente realizados.</p>
<p>O tratamento é escalonado. A primeira linha são os anti-histamínicos H1 de segunda geração, iniciados na dose padrão e elevados até quatro vezes a dose habitual. Na falta de resposta, a segunda linha é o omalizumabe, anticorpo monoclonal anti-IgE indicado para UCE refratária aos anti-histamínicos. A terceira linha inclui imunossupressores, como a ciclosporina A, para casos graves e refratários, com monitorização rigorosa. Corticosteroides sistêmicos só nas exacerbações agudas, por curtos períodos; antagonistas de leucotrienos e outros imunossupressores são opções excepcionais, com evidência mais limitada.</p>
<h3>III. O medicamento solicitado</h3>
<p>O omalizumabe liga-se à IgE livre e reduz a ativação de mastócitos e basófilos. Indicações: asma alérgica persistente moderada a grave, rinossinusite crônica grave com pólipo nasal e urticária crônica espontânea refratária aos anti-histamínicos H1 em adultos e adolescentes acima de 12 anos. Na UCE, diminui o prurido e a atividade da doença. Eventos adversos principais: cefaleia e reações no local da aplicação; raros e graves: anafilaxia, doença do soro, trombocitopenia grave e síndrome de Churg-Strauss. A manutenção deve ser reavaliada periodicamente (fonte: bula, ANVISA).</p>
<h3>IV. Classe e registro na ANVISA</h3>
<table>
<tr><th>Medicamento</th><th>Classe terapêutica</th><th>Registro na ANVISA</th><th>Situação</th></tr>
<tr><td>Omalizumabe</td><td>Outros antialérgicos</td><td>SIM</td><td>Ativo</td></tr>
</table>
<h3>V. Risco iminente à vida</h3>
<p>Não há dados clínicos que indiquem risco iminente à vida da paciente.</p>
<h3>VI. Atendimento ou procura prévia da rede pública</h3>
<p>Não consta nos autos informação de atendimento ou procura prévia da rede pública local relacionada à presente demanda.</p>
<h3>VII. Disponibilidade no SUS</h3>
<p>O Omalizumabe não está incorporado na RENAME 2024 ou em outro ato normativo do SUS para a CID da requerente. Está incorporado ao SUS pelo Componente Especializado da Assistência Farmacêutica (CEAF) para o tratamento da Asma (CID-10 J45.0 e J45.8), na apresentação de 150 mg/mL, solução injetável em seringa preenchida, mediante os critérios do PCDT específico, patologia diferente da apresentada pela requerente.</p>
<p>Não há em tramitação solicitação de avaliação do Omalizumabe para a patologia/CID apresentada, conforme a consulta pública a que este Núcleo tem acesso (tecnologias em avaliação na CONITEC).</p>
<h3>VIII. Ente responsável</h3>
<p>Como o Omalizumabe não está incorporado para a CID apresentada, não é possível indicar ente público responsável segundo as normas do SUS.</p>
<h3>IX. Alternativas existentes no SUS</h3>
<p>A RENAME 2024 tem incorporados no Componente Básico (CBAF) anti-histamínicos sistêmicos (Dexclorfeniramina, Loratadina, Prometazina) e corticosteroides sistêmicos (Dexametasona, Prednisolona, Prednisona e Hidrocortisona).</p>
<h3>X. Genérico e preço</h3>
<p>O Omalizumabe não tem genérico ou similar. Preço conforme tabela CMED/ANVISA (PF: preço de fábrica; PMC: preço máximo ao consumidor; PMVG: preço máximo de venda ao governo), alíquota 17%, consultado em 26/03/2026:</p>
<ul><li>OMLYCLO (CELLTRION HEALTHCARE DISTRIBUICAO DE PRODUTOS FARMACEUTICOS DO BRASIL LTDA) 150 MG/ML SOL INJ SC CT 1 SER PREENC VD TRANS C/ PROT ESP AGU X 0,5 ML; PF: R$ 1.484,66; PMC: R$ 2.052,45; PMVG: R$ 1.165,01.</li></ul>
<h3>XI. Conclusão</h3>
<ul>
<li>Não consta nos autos informação de atendimento ou procura prévia da rede pública local relacionada à demanda, e não há dados clínicos de risco iminente à vida.</li>
<li>O Omalizumabe não está incorporado na RENAME 2024 ou em outro ato normativo do SUS para a CID da requerente; está incorporado no CEAF apenas para Asma (CID-10 J45.0 e J45.8).</li>
<li>Não há em tramitação solicitação de avaliação do Omalizumabe na CONITEC para a patologia/CID apresentada.</li>
<li>A RENAME 2024 tem anti-histamínicos e corticosteroides sistêmicos no CBAF.</li>
<li>Diretrizes nacionais e internacionais orientam a decisão clínica, mas não têm, isoladamente, a robustez metodológica de ensaios clínicos randomizados ou meta-análises e não substituem evidência científica de alta qualidade, sobretudo em contextos regulatórios e judiciais.</li>
<li>Para medicamentos não incorporados devem ser observados eficácia, segurança, custo-efetividade e impacto orçamentário, conforme os Temas 6 e 1.234 do STF. No caso, não foram apresentadas evidências científicas robustas, em sua integralidade, que demonstrem segurança e desfechos clínicos adequados à condição específica da paciente.</li>
</ul>
<p>Em face do exposto, este Núcleo de Apoio Técnico manifesta-se <b>desfavorável</b> ao pedido de Omalizumabe.</p>
<p class="dir">26 de março de 2026.</p>
<div class="ass"><div>Equipe técnica do NATJus (médicos, farmacêuticos e enfermeiros)<br>assinado por certificação digital</div></div>
"""

DOCS["07-decisao-tutela"] = f"""
<div class="cab">Poder Judiciário do Estado de Mato Grosso do Sul<br>Comarca de Vila Boa Esperança, 1ª Vara</div>
<h2>Autos: {PROC} (fictício). Procedimento Comum Cível, fornecimento de medicamentos<br>Autora: Valdirene Souza Prado. Réus: Município de Vila Boa Esperança e outro</h2>
<h1>DECISÃO</h1>
<p>Vistos.</p>
<p>Trata-se de ação de obrigação de fazer com pedido de tutela de urgência ajuizada por Valdirene Souza Prado em face do Município de Vila Boa Esperança e do Estado de Mato Grosso do Sul. A autora alega que tem Urticária Crônica Espontânea (CID-10 L50.1), que necessita do medicamento OMALIZUMAB 300 MG e que não tem meios de custeá-lo. Pede tutela de urgência para o fornecimento. Juntou documentos. O NAT manifestou-se desfavoravelmente ao pedido. É o relatório. Decido.</p>
<p>1) Recebo a petição inicial e defiro os benefícios da gratuidade da justiça, forte na alegação de pobreza.</p>
<p>2) Em juízo não exauriente, a pretensão liminar não merece acolhimento. O Núcleo de Apoio Técnico emitiu parecer desfavorável à concessão do medicamento.</p>
<p>A antecipação de tutela depende das teses fixadas nos Temas 1.234 e 6 do STF, que vinculam o julgador por força das Súmulas Vinculantes 60 e 61. Como regra, é impossível impor ao poder público o fornecimento de medicamentos fora das listas do SUS. Excepcionalmente, a ordem judicial é possível se comprovado: (a) que o remédio foi negado pelo órgão público responsável; (b) que a decisão da CONITEC de não incluir o medicamento é ilegal, que não houve pedido de inclusão ou que houve demora excessiva na análise; (c) que não há outro medicamento das listas do SUS capaz de substituí-lo; (d) que há evidências científicas de que o remédio é eficaz e seguro; (e) que o remédio é indispensável ao tratamento; e (f) que a requerente não tem condições financeiras de comprá-lo.</p>
<p>No caso concreto, não estão comprovados os requisitos cumulativos. A paciente está sendo atendida pela rede pública de saúde. Embora o medicamento seja registrado na ANVISA, não está padronizado na RENAME para a patologia em questão e não há em tramitação solicitação de avaliação para essa patologia, bem como estão ausentes evidências científicas de que os fármacos são eficazes e seguros.</p>
<p>O NAT informou ainda que "a RENAME 2024 tem incorporado no CBAF medicamentos anti-histamínicos sistêmicos (Dexclorfeniramina, Loratadina, Prometazina), corticosteroides sistêmicos (Dexametasona, Prednisolona, Prednisona e Hidrocortisona)". Há, portanto, outros medicamentos que podem ser usados no tratamento, inexistindo provas do uso e da ineficácia deles.</p>
<p>A autora não apresentou elementos que comprovem a integralidade dos requisitos, e não está caracterizado o perigo de dano, pois, segundo o NAT, "não há dados clínicos que indiquem risco iminente à vida da paciente". Sendo cumulativos os requisitos da tutela de urgência, ela deve ser indeferida por ora, sem prejuízo de reanálise diante de novas provas.</p>
<p>3) Posto isso, <b>INDEFIRO O PEDIDO DE ANTECIPAÇÃO DE TUTELA</b>.</p>
<p>4) Deixo de designar audiência de conciliação, na forma da recomendação do Conselho Superior da Magistratura para as causas em que a Fazenda Pública é parte.</p>
<p>5) Cite-se a parte ré para apresentar resposta em 30 (trinta) dias (CPC, arts. 183 e 335).</p>
<p>6) Com a contestação, manifeste-se a autora em 15 (quinze) dias.</p>
<p>Intime-se. Cumpra-se.</p>
<p class="dir">Vila Boa Esperança, 26 de março de 2026.</p>
<div class="ass"><div>Mariana Teixeira Lopes<br>Juíza de Direito (assinado por certificação digital)</div></div>
"""

DOCS["08-relatorio-medico-complementar"] = """
<div class="cab"><b>Dr. Henrique Lacerda Moraes, CRM/MS 99.512</b><br>Alergia e Imunologia, adulto e infantil. Rua das Acácias, 120, Centro</div>
<h1>RELATÓRIO MÉDICO COMPLEMENTAR</h1>
<h2>Justificativa para tratamento com omalizumabe. 20/04/2026</h2>
<p><b>Paciente:</b> Valdirene Sousa Prado. <b>Idade:</b> entre 40 e 50 anos. <b>Diagnóstico:</b> Urticária Crônica Espontânea (UCE), CID-10 L50.1.</p>
<p>Declaro que a paciente está em acompanhamento médico especializado por Urticária Crônica Espontânea, doença inflamatória crônica com episódios recorrentes de urticas e/ou angioedema, com importante repercussão clínica e sobre a qualidade de vida.</p>
<p>A doença está ativa e inadequadamente controlada, apesar do tratamento convencional otimizado. Foi feito tratamento com anti-histamínico H1 de segunda geração (bilastina) em dose quadruplicada, por mais de quatro meses, sem controle satisfatório, o que caracteriza falha terapêutica ao tratamento de primeira linha. Atualmente: UAS7 (Urticaria Activity Score, 7 dias) de 28 pontos, atividade clinicamente significativa; UCT (Urticaria Control Test) de 0 pontos, ausência de controle da doença. Diante disso, a paciente tem indicação médica de omalizumabe, conforme a estratégia terapêutica atualmente empregada para UCE refratária.</p>
<h3>Da necessidade do tratamento</h3>
<p>O omalizumabe é anticorpo monoclonal anti-IgE com indicação terapêutica estabelecida para UCE em pacientes que seguem sintomáticos apesar dos anti-histamínicos H1. A própria Nota Técnica do NATJus deste caso reconhece que o omalizumabe é a segunda linha terapêutica para esses pacientes, que tem registro ativo na ANVISA e que a UCE está entre suas indicações. Não se trata, portanto, de medicamento experimental nem de tratamento sem indicação para a doença da paciente.</p>
<h3>Da questão referente ao SUS e ao CID</h3>
<p>A indicação médica e sanitária do medicamento não se confunde com sua incorporação ao SUS para determinada doença. A paciente tem diagnóstico documentado de UCE (CID-10 L50.1), e não é médica nem tecnicamente admissível substituir ou criar diagnóstico diferente apenas para viabilizar o enquadramento administrativo. A Nota Técnica reconhece que o omalizumabe está incorporado para outra indicação, a asma; a questão, portanto, é de não incorporação específica para UCE, e não de falta de registro, de indicação ou de caráter experimental.</p>
<h3>Da imprescindibilidade no caso concreto</h3>
<p>A necessidade decorre da resposta inadequada ao tratamento convencional e da atividade significativa da doença, demonstrada por UAS7 de 28 pontos e UCT de 0 pontos. A doença sem controle mantém prurido, urticas e angioedema, prejudica o sono, as atividades cotidianas e a qualidade de vida, e pode exigir tratamentos sistêmicos de resgate repetidos. O uso crônico de corticosteroides sistêmicos não é alternativa adequada para o controle contínuo da UCE, pelos riscos da exposição prolongada. Considerando a falha documentada do anti-histamínico H1 em dose quadruplicada e a ausência completa de controle, o omalizumabe é, neste momento, tratamento necessário, sem justificativa clínica para substituí-lo por tratamento ineficaz para o quadro.</p>
<h3>Conclusão</h3>
<p>A paciente tem UCE ativa e não controlada, apesar de tratamento adequado com anti-histamínico H1 de segunda geração em dose quadruplicada, com UAS7 = 28 e UCT = 0. Reitero a indicação de omalizumabe 300 mg por via subcutânea a cada 4 semanas, com acompanhamento clínico periódico e avaliação objetiva da resposta por UAS7 e UCT. Solicito que a necessidade do tratamento seja analisada pelas características clínicas individuais da paciente, independentemente da incorporação específica dessa indicação nas políticas de fornecimento do SUS.</p>
<div class="ass"><div>Dr. Henrique Lacerda Moraes<br>Médico, Alergia e Imunologia, CRM/MS 99.512 (assinado digitalmente em 20/04/2026)</div></div>
"""

def carimbar(caminho):
    d = fitz.open(caminho)
    n = len(d)
    for i, pg in enumerate(d):
        w = pg.rect.width
        pg.insert_textbox(fitz.Rect(40, 22, w - 40, 40), "Autos fictícios, material didático", fontsize=8.5, fontname="helv", color=(.4, .4, .4), align=1)
        pg.draw_line(fitz.Point(56, 40), fitz.Point(w - 56, 40), color=(.7, .7, .7), width=.5)
        pg.insert_textbox(fitz.Rect(40, pg.rect.height - 34, w - 40, pg.rect.height - 18), f"Página {i+1} de {n}", fontsize=8.5, fontname="helv", color=(.4, .4, .4), align=1)
    tmp = caminho.with_suffix(".tmp.pdf")
    d.save(tmp, garbage=3, deflate=True)
    d.close()
    tmp.replace(caminho)

if __name__ == "__main__":
    SAIDA.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmpdir:
        for nome, corpo in DOCS.items():
            h = pathlib.Path(tmpdir) / f"{nome}.html"
            h.write_text(doc(corpo), encoding="utf-8")
            destino = SAIDA / f"{nome}.pdf"
            subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={destino}", h.as_uri()], check=True, capture_output=True)
            carimbar(destino)
            print(nome, len(fitz.open(destino)), "p.")
