"""Gera os autos fictícios do caso 3 (aula 2). Todo o texto é fictício.
Uso: python3 caso-3.py [DESTINO]  (padrão: ../../kit/casos/caso-3). Precisa do Chrome."""
import subprocess, sys, pathlib, tempfile

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
AQUI = pathlib.Path(__file__).resolve().parent
DEST = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else AQUI.parent.parent / "kit" / "casos" / "caso-3"
PROC = "0899413-29.2026.8.12.0099"
CEJ = "0899571-87.2026.8.12.0098"

CSS = """
@page { size: A4; margin: 0; }
* { box-sizing: border-box; }
body { margin: 0; font: 11pt/1.45 Georgia, 'Times New Roman', serif; color: #1a1a1a; }
.pg { width: 210mm; height: 297mm; padding: 14mm 20mm 16mm; position: relative; page-break-after: always; }
.pg:last-child { page-break-after: auto; }
.topo { font: 8.5pt Helvetica, Arial, sans-serif; color: #666; border-bottom: 1px solid #bbb; padding-bottom: 3pt; margin-bottom: 12pt; display: flex; justify-content: space-between; }
.rod { position: absolute; bottom: 9mm; left: 20mm; right: 20mm; font: 8.5pt Helvetica, Arial, sans-serif; color: #666; border-top: 1px solid #bbb; padding-top: 3pt; display: flex; justify-content: space-between; }
.inst { text-align: center; font-weight: bold; font-size: 11.5pt; margin: 0; }
.sub { text-align: center; font-size: 10pt; margin: 0 0 12pt; }
h1 { font-size: 13pt; text-align: center; margin: 6pt 0 10pt; }
h3 { font-size: 11pt; margin: 10pt 0 5pt; }
p { margin: 0 0 7pt; text-align: justify; }
.rec { text-indent: 2.2em; }
.ass { margin-top: 18pt; text-align: center; font-size: 10.5pt; }
.ass .l { display: inline-block; border-top: 1px solid #333; padding-top: 3pt; min-width: 70mm; }
table { border-collapse: collapse; width: 100%; font-size: 9.8pt; margin: 4pt 0 9pt; }
td, th { border: 1px solid #777; padding: 3pt 5pt; vertical-align: top; text-align: left; }
th { background: #eee; }
.cx { border: 1px solid #777; padding: 6pt 8pt; margin: 0 0 9pt; font-size: 10.2pt; }
.cit { margin: 4pt 2.2em 9pt; font-size: 10pt; border-left: 3px solid #999; padding-left: 8pt; }
.peq { font-size: 9.5pt; }
.mao { font-family: 'Comic Sans MS', 'Bradley Hand', cursive; color: #1f3a8a; }
.q { margin: 0 0 6pt; }
"""

def doc(titulo_doc, paginas):
    n = len(paginas)
    out = []
    for i, corpo in enumerate(paginas, 1):
        out.append(f"<div class='pg'><div class='topo'><span>Autos fictícios, material didático</span><span>Processo {PROC} (fictício)</span></div>"
                   f"{corpo}<div class='rod'><span>{titulo_doc}</span><span>Página {i} de {n}</span></div></div>")
    return f"<!doctype html><meta charset='utf-8'><style>{CSS}</style>" + "".join(out)

DPE_SA = "<p class='inst'>DEFENSORIA PÚBLICA DO ESTADO DE MATO GROSSO DO SUL</p><p class='sub'>2ª Defensoria Pública da Comarca de Serra Alta</p>"
DPE_VBE = "<p class='inst'>DEFENSORIA PÚBLICA DO ESTADO DE MATO GROSSO DO SUL</p><p class='sub'>2ª Defensoria Pública da Comarca de Vila Boa Esperança</p>"

INICIAL = [
DPE_SA + """
<p><b>AO JUÍZO DA __ª VARA DA COMARCA DE VILA BOA ESPERANÇA/MS</b></p>
<p><b>URGENTE. LIMINAR. PRIORIDADE NA TRAMITAÇÃO. PESSOA COM DEFICIÊNCIA</b></p>
<p class='rec'><b>ROSA MARIA ANDRADE LEMES</b>, brasileira, solteira, interditada, CPF nº 111.222.333-44, residente no Centro de Vila Boa Esperança/MS, representada por sua curadora, <b>CLARICE ANDRADE LEMES</b>, brasileira, casada, do lar, CPF nº 555.666.777-88, residente no mesmo endereço, por intermédio da DEFENSORIA PÚBLICA DO ESTADO DE MATO GROSSO DO SUL, propõe <b>AÇÃO DE OBRIGAÇÃO DE FAZER COM PEDIDO DE TUTELA DE URGÊNCIA</b> em face do <b>MUNICÍPIO DE VILA BOA ESPERANÇA/MS</b> e do <b>ESTADO DE MATO GROSSO DO SUL</b>, pelos fatos e fundamentos a seguir.</p>
<h3>I. DA PRIORIDADE NA TRAMITAÇÃO</h3>
<p class='rec'>A requerente é pessoa com deficiência, com transtorno psiquiátrico crônico grave (CID 10: F20.0), conforme documentação médica anexa, e faz jus à prioridade do art. 9º, VII, da Lei nº 13.146/2015 e do art. 1.048, I, do CPC.</p>
<h3>II. DOS FATOS</h3>
<p><b>II.I. Do quadro clínico e da imprescindibilidade terapêutica</b></p>
<p class='rec'>A requerente, com idade entre 60 e 65 anos, tem Esquizofrenia Paranoide (CID 10: F20.0), conforme laudo médico circunstanciado do Dr. Rodrigo Albuquerque Teles (CRM/MS 0000 (fictício)), do Centro de Atenção Psicossocial (CAPS) de Vila Boa Esperança/MS.</p>
<p class='rec'>O quadro é grave: alucinações visuais e auditivas, irritabilidade e elevado risco de heteroagressividade. Pela cronicidade da doença, a autora está acamada e depende de terceiros para todas as atividades básicas da vida diária, conforme o questionário médico anexo.</p>
<p class='rec'>Para controlar os sintomas psicóticos, a agitação psicomotora e a desorganização do pensamento, o médico prescreveu o uso contínuo de <b>RISPERIDONA 2 mg</b>, 01 (um) comprimido à noite. O laudo é categórico ao afirmar que a medicação é indispensável e insubstituível no momento, fundamental para a estabilidade clínica. A falta do fármaco traz risco iminente de descompensação psiquiátrica, agravamento do quadro e internação hospitalar, com perigo para a paciente e seus cuidadores.</p>
""",
"""
<p><b>II.II. Da tentativa de solução extrajudicial e da pretensão resistida</b></p>
<p class='rec'>Diante da impossibilidade financeira de custear o tratamento, a Defensoria Pública buscou a via administrativa. Em 19/01/2026, encaminhou o Ofício nº 87/2026 à Secretaria Municipal de Saúde de Vila Boa Esperança/MS, pedindo o fornecimento urgente do fármaco, sem resposta efetiva do Município até a presente data.</p>
<p class='rec'>Paralelamente, houve tentativa de conciliação no CEJUSC/TJ Saúde (Processo nº """ + CEJ + """). O ESTADO DE MATO GROSSO DO SUL respondeu negativamente, ao argumento de que a paciente não preenche os requisitos do Protocolo Clínico e Diretrizes Terapêuticas (PCDT) do Ministério da Saúde, embora reconheça que o medicamento está incorporado ao SUS e integra o Grupo 1B do Componente Especializado da Assistência Farmacêutica (CEAF).</p>
<p class='rec'>A negativa é expressa na autorização estadual anexa, que registra "Não autorizado" para a Risperidona 2 mg porque a paciente já usa Quetiapina.</p>
<p class='rec'>Ocorre que o médico assistente consignou que, embora a paciente utilize Quetiapina, a associação com a Risperidona é tecnicamente necessária e insubstituível para o caso concreto, não cabendo à Administração substituir a conduta de quem acompanha a paciente:</p>
<div class='cit'>"Diante do exposto, declaro que a medicação RISPERIDONA é imprescindível e insubstituível no momento para o tratamento da paciente, sendo fundamental para manutenção da estabilidade clínica. A ausência da medicação implica em grave risco à saúde da paciente, com possibilidade de descompensação significativa do quadro psiquiátrico." (trecho do laudo do CAPS)</div>
<h3>III. DO DIREITO</h3>
<p class='rec'>A saúde é direito de todos e dever do Estado (arts. 6º e 196 da CF) e se liga à dignidade da pessoa humana (art. 1º, III, CF) e ao mínimo existencial; a reserva do possível não pode ser oposta genericamente. A Lei nº 8.080/1990 consagra a integralidade da assistência (art. 7º, II).</p>
<p class='rec'><b>Responsabilidade solidária (Tema 793 do STF).</b> A obrigação é comum aos entes federados (art. 23, II, CF), de modo que Estado e Município são legitimados passivos. Regras internas de repartição, como a inclusão do fármaco no Grupo 1B do CEAF, não podem ser opostas ao cidadão.</p>
<p class='rec'><b>Ilegalidade da negativa baseada no PCDT.</b> É incontroverso que a RISPERIDONA 2 mg é medicamento incorporado ao SUS. Não se discute a eficácia do fármaco nem sua inclusão nas políticas públicas, mas um entrave burocrático de elegibilidade. O PCDT orienta a Administração, mas não é absoluto e não se sobrepõe ao laudo individualizado do médico do CAPS, que atestou a imprescindibilidade da medicação e a ineficácia de outras alternativas isoladas. Pela teoria dos motivos determinantes, a negativa ignora a realidade da paciente (risco de agressividade e internação).</p>
""",
"""
<p class='rec'>O Tribunal de Justiça de Mato Grosso do Sul tem precedentes que qualificam como formalidade excessiva a exigência de cadastro no PCDT diante de necessidade clínica demonstrada por laudo fundamentado. Assim, o laudo circunstanciado e o questionário médico suprem qualquer exigência protocolar, porque a medicina baseada em evidências aplicada ao caso pela equipe do CAPS demonstra que a Risperidona é a única alternativa eficaz para a estabilidade da autora.</p>
<p class='rec'><b>Requisitos do Tema 106 do STJ.</b> Ainda que se apliquem os requisitos do REsp 1.657.159, a procedência se impõe: (i) há laudo fundamentado atestando a imprescindibilidade; (ii) a incapacidade financeira é notória, pois a autora é assistida pela Defensoria Pública; (iii) o medicamento tem registro na ANVISA e é padronizado no SUS.</p>
<h3>IV. DA TUTELA DE URGÊNCIA</h3>
<p class='rec'>Presentes os requisitos do art. 300 do CPC. A probabilidade do direito decorre da prescrição, do laudo e da admissão do Estado de que o medicamento é padronizado. O perigo de dano é grave: sem a Risperidona há risco de descompensação psicótica, auto e heteroagressividade e internação psiquiátrica evitável. Requer o fornecimento em 48 (quarenta e oito) horas.</p>
<h3>V. DOS PEDIDOS</h3>
<p>a) a gratuidade da justiça (art. 98 do CPC), dada a hipossuficiência da autora, assistida pela Defensoria Pública, conforme declaração anexa;<br>
b) a tramitação prioritária;<br>
c) a TUTELA DE URGÊNCIA, <i>inaudita altera parte</i>, para que o ESTADO DE MATO GROSSO DO SUL e o MUNICÍPIO DE VILA BOA ESPERANÇA/MS forneçam imediatamente RISPERIDONA 2 mg, 01 comprimido à noite, de uso contínuo, em quantidade suficiente para o tratamento mensal, sob pena de multa diária;<br>
d) em caso de descumprimento, o bloqueio de valores suficientes para a compra na rede privada;<br>
e) a citação dos réus; f) a intimação do Ministério Público, diante da incapacidade civil da autora;<br>
g) a confirmação da tutela e a procedência, com fornecimento regular e ininterrupto enquanto durar a necessidade clínica;<br>
h) subsidiariamente, se o Juízo entender necessário, a consulta ao NATJus, sem prejuízo da liminar.</p>
<p class='rec'>Provará o alegado pelos documentos já juntados: documentos pessoais, laudos médicos, declaração de hipossuficiência e ofício administrativo. Dá à causa o valor de R$ 1.621,00, para fins meramente fiscais.</p>
<p class='rec'>Serra Alta/MS, 26 de fevereiro de 2026.</p>
<div class='ass'><span class='l'>Patrícia Mendes Lacerda<br>Defensora Pública em substituição legal<br>(assinado digitalmente)</span></div>
"""]

LAUDO = ["""
<p class='inst'>CENTRO DE ATENÇÃO PSICOSSOCIAL DE VILA BOA ESPERANÇA</p><p class='sub'>Secretaria Municipal de Saúde de Vila Boa Esperança/MS</p>
<h1>LAUDO MÉDICO</h1>
<p><b>Paciente:</b> Rosa Maria Andrade Lemes &nbsp;&nbsp; <b>Idade:</b> entre 60 e 65 anos &nbsp;&nbsp; <b>Sexo:</b> feminino</p>
<p>Declaro, para os devidos fins, que a paciente acima identificada está em <b>acompanhamento regular no Centro de Atenção Psicossocial (CAPS)</b>, com diagnóstico de <b>transtorno psiquiátrico crônico do espectro da esquizofrenia (CID F20)</b>.</p>
<p>Trata-se de paciente com quadro clínico grave, associado a importante limitação funcional, acamada e dependente de terceiros para cuidados integrais, conforme descrito em prontuário recente.</p>
<p>A paciente faz uso contínuo de medicação antipsicótica, com destaque para a <b>RISPERIDONA 2 mg</b>, previamente prescrita e utilizada de forma regular como parte essencial do tratamento psiquiátrico.</p>
<h3>Justificativa médica para uso da medicação</h3>
<p>A risperidona é medicação antipsicótica indispensável para o controle dos sintomas da paciente, incluindo sintomas psicóticos, agitação, alterações comportamentais e desorganização do pensamento.</p>
<p>A suspensão ou ausência desta medicação está associada a alto risco de descompensação psiquiátrica, podendo levar a agravamento do quadro clínico, agitação psicomotora, risco de auto e heteroagressividade e necessidade de internação psiquiátrica.</p>
<p>Atualmente, conforme relatado, a medicação <b>não se encontra disponível pelo SUS</b>, impossibilitando a continuidade adequada do tratamento.</p>
<h3>Conclusão</h3>
<p>Diante do exposto, declaro que a medicação <b>RISPERIDONA é imprescindível e insubstituível no momento para o tratamento da paciente</b>, sendo fundamental para manutenção da estabilidade clínica.</p>
<p>A ausência da medicação implica em grave risco à saúde da paciente, com possibilidade de descompensação significativa do quadro psiquiátrico.</p>
<p>O presente laudo é emitido para fins de apresentação junto à Defensoria Pública, visando obtenção judicial da medicação pelo sistema público de saúde.</p>
<p><b>CID:</b> F20, Esquizofrenia</p>
<div class='ass'><span class='l'>Dr. Rodrigo Albuquerque Teles<br>Médico Clínico Geral, CRM/MS 0000 (fictício)<br>CAPS, ambulatório especializado em saúde mental</span></div>
<p class='peq' style='margin-top:14pt'>Documento gerado pelo sistema municipal de saúde por Rodrigo Albuquerque Teles em 18/11/2025, 14:21.</p>
"""]

VIA = """
<div class='cx' style='margin-bottom:14pt'>
<p class='inst' style='font-size:11pt'>RECEITUÁRIO DE CONTROLE ESPECIAL</p><p class='sub' style='margin-bottom:8pt'>CAPS de Vila Boa Esperança · {via}</p>
<p><b>Emitente:</b> Rodrigo Albuquerque Teles, médico clínico, CRM/MS 0000 (fictício)</p>
<p><b>Paciente:</b> Rosa Maria Andrade Lemes</p>
<table><tr><th>Medicamento</th><th>Posologia</th><th>Qtd.</th></tr>
<tr><td>1. RISPERIDONA, 2 mg, comprimido, uso contínuo</td><td>Tomar 01 comprimido à noite. Via oral. Duração: indeterminado. Recomendações: (em branco)</td><td>30</td></tr></table>
<p style='text-align:center;margin-top:10pt'><span class='mao'>R. A. Teles</span><br>Rodrigo Albuquerque Teles, médico clínico</p>
<table><tr><th colspan='2'>Identificação do comprador</th></tr><tr><td>Nome:</td><td>Identidade / órgão emissor:</td></tr><tr><td>Endereço:</td><td>Cidade / UF:</td></tr></table>
<table><tr><th colspan='2'>Identificação do fornecedor</th></tr><tr><td>Assinatura do farmacêutico:</td><td>Data de fornecimento: ___/___/____</td></tr></table>
<p class='peq'>Documento emitido pelo sistema municipal de saúde. Impresso por Rodrigo Albuquerque Teles.</p>
</div>"""
RECEITA = [VIA.format(via="1ª via") + VIA.format(via="2ª via")]

QUEST = [DPE_VBE + """
<h1 style='margin-top:0'>QUESTIONÁRIO PARA PEDIDO JUDICIAL DE MEDICAMENTO(S)</h1>
<p class='peq'>Formulário da Defensoria Pública preenchido à mão pelo médico. Abaixo, as respostas manuscritas aparecem em azul; o que está "(em branco)" não foi preenchido no original.</p>
<p class='peq'>Em atenção ao Enunciado 19 da I Jornada de Direito da Saúde e ao Enunciado 58 da II Jornada de Direito da Saúde do CNJ, solicita-se que Vossa Senhoria responda às indagações abaixo.</p>
<table>
<tr><th colspan='2'>Dados da paciente</th></tr>
<tr><td>Nome</td><td class='mao'>Rosa Maria Andrade Lemes</td></tr>
<tr><td>Cartão SUS</td><td class='mao'>700 0000 0000 0000</td></tr>
<tr><td>Atendimento que originou a prescrição</td><td>(X) SUS. Unidade: <span class='mao'>CAPS Vila Boa Esperança MS</span></td></tr>
<tr><th>Medicamento (DCB/DCI)</th><th>Posologia e via de administração</th></tr>
<tr><td class='mao'>Risperidona 2 mg</td><td class='mao'>Tomar 01 comprimido noite</td></tr>
</table>
<p class='q'>Duração do tratamento: (X) Contínuo (&nbsp;&nbsp;) Temporário</p>
<p class='q'>Registro na ANVISA: (X) Sim (&nbsp;&nbsp;) Não. Indicação em conformidade com a aprovação no registro: (&nbsp;&nbsp;) Sim (&nbsp;&nbsp;) Não <i>(em branco)</i></p>
<p class='q'>Previsto em PCDT da doença listada abaixo: (X) Sim (&nbsp;&nbsp;) Não</p>
<p class='q'>Consta em padronização oficial (ex.: REMUME, RENAME ou listas regionais ou estaduais): (X) Sim (&nbsp;&nbsp;) Não</p>
<p class='q'>Caso não aprovado pela ANVISA, é aprovado por órgão estrangeiro? <i>(em branco)</i></p>
<p class='q'>Há estudos de evidência científica (eficácia, eficiência, efetividade e segurança) do medicamento? (&nbsp;&nbsp;) Não (X) Sim. Qual a evidência científica? <i>(em branco)</i></p>
<p class='q'><b>1. Qual(is) doença(s) acomete(m) a paciente e motivou(aram) a prescrição?</b> <span class='mao'>Esquizofrenia paranoide</span>. Enfermidade / CID: <span class='mao'>Esquizofrenia paranoide, F20.0</span></p>
<p class='q'><b>2. Características da(s) doença(s):</b> <span class='mao'>Alucinações visuais e auditivas, irritabilidade e risco de heteroagressividade caso não utilize medicações de uso contínuo.</span></p>
<p class='q'><b>3. Como é feito o diagnóstico?</b> (X) Exame(s) clínico(s) (&nbsp;&nbsp;) Laboratorial(is) (&nbsp;&nbsp;) Imagem (&nbsp;&nbsp;) Outro(s). Especifique: <span class='mao'>anamnese</span></p>
<p class='q'><b>4. Qual a finalidade do medicamento?</b> (X) Profilática (&nbsp;&nbsp;) Curativa (&nbsp;&nbsp;) Paliativa (&nbsp;&nbsp;) Diagnóstico. Especifique: <span class='mao'>evitar alucinações visuais e auditivas</span></p>
""",
DPE_VBE + """
<p class='q'><b>5. Existem tratamentos oferecidos pelo SUS para a doença com a mesma eficácia do tratamento indicado? Se sim, quais?</b> <span class='mao'>Não. Com o mesmo grau de respaldo científico não temos disponível pelo SUS.</span></p>
<p class='q'><b>6. As alternativas terapêuticas oferecidas pelo SUS já foram utilizadas?</b> (X) Sim (&nbsp;&nbsp;) Não</p>
<p class='q'><b>6.1. Especifique o período de tratamento e a resposta obtida:</b> <span class='mao'>Quetiapina. Outro tipo de antipsicótico que estamos utilizando no tratamento, com melhora parcial.</span></p>
<p class='q'><b>6.2. A paciente faz uso de outro(s) tratamento(s) para a doença? Qual(is)?</b> <span class='mao'>Sim, em uso de antipsicóticos e ansiolíticos.</span></p>
<p class='q'><b>6.3. (Em caso negativo) Justifique por que não foram indicados os medicamentos da rede pública:</b> <i>(em branco)</i></p>
<p class='q'><b>7. O tratamento indicado pode ser substituído por alguma alternativa oferecida pelo SUS?</b> (&nbsp;&nbsp;) Sim (X) Não</p>
<p class='q'><b>7.1. Quais as vantagens do tratamento proposto em comparação com os fármacos ou tratamentos oferecidos pelo SUS?</b> <span class='mao'>Grau de eficácia e respaldo científico frente ao diagnóstico de esquizofrenia paranoide.</span></p>
<p class='q'><b>8. O(s) medicamento(s) é(são) imprescindível(is) para a paciente?</b> (X) Sim (&nbsp;&nbsp;) Não. Justifique: <i>(em branco)</i></p>
<p class='q'><b>9. A disponibilização é urgente?</b> (X) Sim (&nbsp;&nbsp;) Não</p>
<p class='q'><b>10. A não utilização imediata poderá ocasionar:</b> (&nbsp;&nbsp;) Risco de morte (&nbsp;&nbsp;) Perda irreversível de órgãos ou funções (X) Grave comprometimento do bem-estar (&nbsp;&nbsp;) Outras</p>
<p class='q'><b>11. Especificar o quadro clínico e as peculiaridades da paciente e demais considerações finais:</b> <span class='mao'>Paciente em acompanhamento contínuo, a qual esteve estável quando fazia uso de todos os psicofármacos; a falta da risperidona pode acarretar deterioração do quadro da paciente.</span></p>
<p class='q'>Local: <span class='mao'>Vila Boa Esperança</span>. Data: <span class='mao'>11/01/2026</span>. Profissional (CRM, carimbo e assinatura): carimbo "Rodrigo A. Teles, Médico, CRM/MS 0000 (fictício)".</p>
<table>
<tr><th colspan='2'>Para preenchimento pela paciente</th></tr>
<tr><td colspan='2'>Possui convênio particular de saúde? (X) Não (&nbsp;&nbsp;) Sim</td></tr>
<tr><td colspan='2'>Buscou obter o medicamento pelo SUS? (X) Sim (&nbsp;&nbsp;) Não</td></tr>
<tr><td>Houve negativa? (X) Sim (&nbsp;&nbsp;) Não</td><td>Negativa: (&nbsp;&nbsp;) Verbal (X) Escrita. Data: ___/___/____ <i>(em branco)</i></td></tr>
<tr><td colspan='2'>Termo de consentimento: autorizo a exposição dos dados médicos em âmbito judicial e administrativo. (X) Sim. Local: <span class='mao'>Vila Boa Esperança MS</span>. Data: <span class='mao'>21/01/2026</span>. Assinatura: <span class='mao'>Clarice Andrade Lemes</span></td></tr>
</table>
"""]

DECL = ["""
<p class='inst'>DEFENSORIA PÚBLICA DO ESTADO DE MATO GROSSO DO SUL</p><p class='sub'>&nbsp;</p>
<h1>DECLARAÇÃO</h1>
<p class='rec'>Eu, Clarice Andrade Lemes, brasileira, casada, do lar, RG (não informado), CPF nº 555.666.777-88, residente em Vila Boa Esperança/MS, DECLARO, para receber assistência jurídica integral e gratuita da DEFENSORIA PÚBLICA DE MATO GROSSO DO SUL, não dispor de recursos financeiros que me permitam, na defesa de meus direitos e interesses, extra ou judicialmente, suportar as despesas processuais e o pagamento de honorários advocatícios, sem prejuízo do próprio sustento ou da família.</p>
<p class='rec'>Declaro estar ciente de que estou sujeita à multa de até 10 (dez) vezes o valor das despesas processuais, caso seja constatada falsidade nesta declaração, e do que dispõe o art. 299 do Código Penal (falsidade ideológica).</p>
<p class='rec'>Para análise e instrução processual, autorizo a Defensoria Pública a requisitar informações de quem quer que as detenha, ainda que isso importe quebra do sigilo profissional, médico, fiscal, bancário e financeiro.</p>
<p class='rec'>Comprometo-me a guardar os documentos originais que instruíram o processo por 5 (cinco) anos após o trânsito em julgado e a manter atualizado meu cadastro na Defensoria Pública.</p>
<p class='rec'>Declaro, ainda, estar ciente de que a ausência injustificada às audiências designadas poderá acarretar multa, nos termos do § 8º do art. 334 do CPC.</p>
<p class='peq'>Os dados pessoais desta declaração são tratados conforme o art. 7º, III, da Lei nº 13.709/2018 (LGPD).</p>
<p class='rec'>Vila Boa Esperança/MS, 18 de janeiro de 2026.</p>
<div class='ass'><span class='mao'>Clarice Andrade Lemes</span><br><span class='l'>DECLARANTE</span></div>
"""]

NEG = [DPE_VBE + """
<p style='display:flex;justify-content:space-between'><b>Ofício nº 87/2026</b><span>Vila Boa Esperança/MS, 18 de janeiro de 2026.</span></p>
<p>À Senhora Secretária Municipal de Saúde de Vila Boa Esperança/MS</p>
<p><b>Assunto:</b> Requisição urgente de medicamento, Risperidona</p>
<p class='rec'>A Defensoria Pública, instituição incumbida da defesa integral e gratuita dos necessitados (art. 5º, LXXIV, e art. 134 da Constituição Federal; Lei Complementar nº 80/1994), solicita o fornecimento do medicamento <b>RISPERIDONA 2 mg (caixa com 30 comprimidos)</b>, de uso contínuo, em favor da paciente <b>Rosa Maria Andrade Lemes</b>, conforme prescrição e laudo médico apresentados.</p>
<p class='rec'>Conforme documentação médica do CAPS de Vila Boa Esperança/MS, a paciente tem <b>Esquizofrenia, CID F20</b>, em acompanhamento psiquiátrico regular, sendo o medicamento imprescindível para a estabilidade clínica e o controle de sintomas psicóticos, agitação e alterações comportamentais.</p>
<p class='rec'>Segundo a curadora, a medicação deixou de ser disponibilizada pela Farmácia Municipal, apesar da indicação médica, sob alegação de que a paciente já usa Quetiapina. O laudo destaca que a falta da medicação pode agravar significativamente o quadro, com risco de descompensação e internação.</p>
<p class='rec'>Requisita-se a adoção das providências para o fornecimento regular de <b>RISPERIDONA 2 mg</b>, em caráter contínuo, com resposta no prazo de <b>05 (cinco) dias</b>.</p>
<div class='ass'><span class='l'>Eduardo Ramos Furtado<br>Defensor Público Substituto<br>(assinado digitalmente em 18/01/2026)</span></div>
<div class='cx' style='margin-top:16pt'><b>Comprovante de envio (e-mail impresso)</b><br>
Assunto: Ofício n. 087/2026. Enviado em 19/01/2026, 18:16, pela assessoria da 2ª Defensoria Pública de Vila Boa Esperança ao endereço da Secretaria Municipal de Saúde. Texto: "De ordem do Defensor Público da 2ª Defensoria Pública de Vila Boa Esperança, encaminho o ofício n. 087/2026. Gentileza acusar recebimento." Dois anexos: documentos pessoais da paciente e da curadora; ofício assinado.</div>
""",
"""
<p class='inst'>PODER JUDICIÁRIO DO ESTADO DE MATO GROSSO DO SUL</p><p class='sub'>CEJUSC-TJ/Saúde</p>
<h1 style='margin-top:0'>PEDIDO DE MEDICAMENTOS (pré-processual)</h1>
<table>
<tr><td style='width:32%'>Autos</td><td>""" + CEJ + """, Reclamação Pré-processual, Obrigação de Fazer</td></tr>
<tr><td>Protocolo</td><td>18/01/2026, 18:43</td></tr>
<tr><td>Medicamento</td><td>Risperidona, 2 mg, comprimido</td></tr>
<tr><td>Solicitante</td><td>Clarice Andrade Lemes (curadora de Rosa Maria Andrade Lemes), por intermédio da Defensoria Pública</td></tr>
<tr><td>Ente responsável</td><td>Risperidona, 2 mg, comprimido: Procuradoria-Geral do Estado de Mato Grosso do Sul</td></tr>
<tr><td>Anexos</td><td>Documentos pessoais da paciente e da curadora</td></tr>
</table>
<p><b>Relato dos fatos:</b> A Defensoria Pública solicita o fornecimento de RISPERIDONA 2 mg (caixa com 30 comprimidos), de uso contínuo, em favor de Rosa Maria Andrade Lemes, conforme prescrição e laudo apresentados. Conforme documentação do CAPS de Vila Boa Esperança/MS, a paciente tem Esquizofrenia, CID F20, em acompanhamento psiquiátrico regular, sendo o medicamento imprescindível para a estabilidade clínica. Segundo a curadora, a medicação deixou de ser disponibilizada pela Farmácia Municipal sob alegação de que a paciente já usa Quetiapina. O laudo destaca risco de descompensação e internação. Requisita-se o fornecimento regular, em caráter contínuo.</p>
<div class='cx'><b>CERTIDÃO</b> (19/01/2026). Requerente: Clarice Andrade Lemes. Requerido: Procuradoria-Geral do Estado de Mato Grosso do Sul. "Certifico e dou fé que o requerimento foi recebido nesta data." Marcos Vieira, servidor do CEJUSC (assinado digitalmente).</div>
<div class='cx'><b>CERTIDÃO</b> (22/01/2026). "Certifico que nesta data foi intimado o ente requerido para se manifestar no prazo de até 10 (dez) dias úteis acerca do pedido de providência de saúde requerida." Segue o modelo de resposta do termo de cooperação, que pede ao ente informar se há o medicamento em estoque e o prazo de entrega; se há compra em andamento; se não há previsão de entrega; se o medicamento não é padronizado e quais alternativas existem no SUS; outra resposta fundamentada; ou, não sendo de sua responsabilidade, quem é o responsável. Marcos Vieira, estagiário (assinado digitalmente).</div>
""",
"""
<p class='inst'>PROCURADORIA-GERAL DO ESTADO E SECRETARIA DE ESTADO DE SAÚDE DE MATO GROSSO DO SUL</p><p class='sub'>Juntado nos autos do CEJUSC em 11/02/2026</p>
<h1 style='margin-top:0'>RESPOSTA À PROVIDÊNCIA DE SAÚDE</h1>
<table><tr><th>Siglas</th><th>Número</th><th>Data</th></tr><tr><td>PGE / SES</td><td>5172</td><td>26/01/2025</td></tr></table>
<p><b>Para:</b> CEJUSC-TJ Saúde. <b>Assunto:</b> solicitação de fornecimento de medicamentos. <b>Processo nº</b> """ + CEJ + """. <b>Solicitante:</b> Rosa Maria Andrade Lemes; responsável: Clarice Andrade Lemes.</p>
<p><b>Pedido:</b> 1. Risperidona 2 mg comprimido.</p>
<p><b>Análise médica:</b> 1. Desfavorável à Risperidona 2 mg, conforme documento em anexo.</p>
<p><b>Análise técnica:</b> Segundo a Relação Nacional de Medicamentos Essenciais (RENAME), a Risperidona 2 mg está incorporada ao SUS e integra o Grupo 1B do CEAF. O Ministério da Saúde financia o medicamento (Portaria nº 1.554/2013, art. 3º, I, "b") e a Secretaria de Estado de Saúde é responsável por adquiri-lo, armazená-lo, distribuí-lo e dispensá-lo, desde que para doenças e situações clínicas contempladas no PCDT do Ministério da Saúde. No entanto, a solicitante não preenche os requisitos do PCDT para receber Risperidona 2 mg, conforme documento em anexo, motivo pelo qual os servidores estaduais não têm competência (autorização legal) para fornecê-la.</p>
<p><b>Conclusão:</b> Não é possível fornecer Risperidona 2 mg.</p>
<p>Fernanda Lopes Rocha, PGE/SES. Carla Mendonça, farmacêutica.</p>
<hr>
<h1 style='font-size:12pt'>ANÁLISE MÉDICA (anexo)</h1>
<p><b>Processo nº</b> """ + CEJ + """. <b>Solicitante:</b> Rosa Maria Andrade Lemes. <b>Objeto:</b> análise com fundamento na medicina baseada em evidência para Risperidona 2 mg comprimido, CID F20.</p>
<p>1. Receita sem data de emissão: preenchimento incompleto e sem validade.<br>
2. Não foram apresentados: exames complementares que comprovem a enfermidade; relatório periódico do tratamento, com evolução e datas; referência bibliográfica para a medicação e a enfermidade.<br>
3. Falta de informações que justifiquem a indicação e preencham os critérios de elegibilidade. Não há "comprovação de eficácia e segurança da medicação por ensaios clínicos randomizados e revisões sistemáticas ou meta-análises", nem prova de benefício clínico comparativo superior ao disponibilizado pelo SUS.</p>
<p><b>Conclusões:</b> I. Receita sem validade. II. A falta de informação não permite avaliar ou impede a paciente de receber o tratamento específico. III. Desfavorável à Risperidona 2 mg comprimido. Sugere-se enviar exames, relatório periódico com evolução e datas, e observar os critérios do PCDT quando a medicação for incorporada. Em nota, invoca a Súmula Vinculante nº 60 e o Tema 1.234 do STF (item 4.3).</p>
<p>26/01/2026. Dr. Henrique Salles, assistente técnico, médico, CRM/MS 0000 (fictício).</p>
""",
"""
<p class='inst'>SECRETARIA DE ESTADO DE SAÚDE DE MATO GROSSO DO SUL</p><p class='sub'>Farmácia Estadual de Medicamentos Especializados · Componente Especializado da Assistência Farmacêutica (CEAF)</p>
<h1 style='margin-top:0;font-size:12pt'>AUTORIZAÇÃO DE MEDICAMENTOS (anexo da resposta estadual)</h1>
<p>Emissão: 16/10/2025. Unidade executante: SMS Vila Boa Esperança. Protocolo 900.25.000412-6. Usuária: Rosa Maria Andrade Lemes.</p>
<table><tr><th>Medicamento</th><th>CID</th><th>M1 a M6</th><th>Autorização</th></tr>
<tr><td>RISPERIDONA 2 MG COMPRIMIDO</td><td>F315</td><td>30 por mês</td><td>Não autorizado. Processo vigente com CID F200, em uso de quetiapina. Favor rever diagnóstico.</td></tr></table>
<p>Data da autorização: 16/10/2025. Órgão autorizador: Farmácia Estadual de Medicamentos Especializados.</p>
<h1 style='margin-top:14pt;font-size:12pt'>HISTÓRICO DE AUTORIZAÇÃO DO CEAF (juntado com a inicial)</h1>
<p>Emissão: 15/09/2025. Unidade: SMS Vila Boa Esperança. Usuária: Rosa Maria Andrade Lemes. Data da autorização: 21/08/2025. Vigência: 03/09/2025 a 02/03/2026.</p>
<table><tr><th>Medicamento</th><th>Mês 1 a 6</th><th>CID</th><th>Autorização</th></tr>
<tr><td>QUETIAPINA 25 MG</td><td>90 por mês</td><td>F200</td><td>Autorizado. Dois antipsicóticos prescritos. Conforme PCDT vigente (Portaria nº 364, de 9 de abril de 2013, que aprova o PCDT da Esquizofrenia), os tratamentos devem ser feitos com um medicamento de cada vez (monoterapia), de acordo com o perfil de segurança e a tolerabilidade do paciente. Em caso de falha terapêutica (definida como o uso de qualquer desses fármacos por pelo menos 6 semanas).</td></tr>
<tr><td>RISPERIDONA 2 MG</td><td>30 por mês</td><td>F200</td><td>Não autorizado.</td></tr></table>
<p class='inst' style='margin-top:18pt'>PODER JUDICIÁRIO DO ESTADO DE MATO GROSSO DO SUL</p><p class='sub'>CEJUSC-TJ/Saúde</p>
<div class='cx'><b>CERTIDÃO</b> (11/02/2026). Autos """ + CEJ + """. Requerente: Clarice Andrade Lemes. Requerido: Procuradoria-Geral do Estado de Mato Grosso do Sul. "Certifico que nesta data o ente não atendeu a providência de saúde requerida. Certifico, ainda, que enviei e-mail para o endereço fornecido pelo(a) requerente encaminhando a resposta fornecida pelo(s) requerido(s)." Lúcio Prado, servidor do CEJUSC (assinado digitalmente).</div>
"""]

JUIZO = "<p class='inst'>PODER JUDICIÁRIO DO ESTADO DE MATO GROSSO DO SUL</p><p class='sub'>Comarca de Vila Boa Esperança · 2ª Vara</p>"
DECISAO = [JUIZO + """
<p>Processo nº """ + PROC + """<br>Classe: Procedimento Comum Cível, Obrigação de Fazer / Não Fazer<br>Autor: Rosa Maria Andrade Lemes, representada por Clarice Andrade Lemes<br>Réus: Estado de Mato Grosso do Sul e Município de Vila Boa Esperança</p>
<h1>DECISÃO</h1>
<p class='rec'>Trata-se de ação de obrigação de fazer com pedido de tutela de urgência ajuizada por ROSA MARIA ANDRADE LEMES, pessoa interditada, representada por sua curadora CLARICE ANDRADE LEMES, em face do MUNICÍPIO DE VILA BOA ESPERANÇA/MS e do ESTADO DE MATO GROSSO DO SUL, para fornecimento do medicamento RISPERIDONA, de uso contínuo.</p>
<p class='rec'>A autora afirma ser pessoa com deficiência, com esquizofrenia (CID F20.0), em acompanhamento pelo CAPS de Vila Boa Esperança/MS, e que o medicamento, prescrito por profissional da rede pública, é imprescindível para a estabilidade clínica e para evitar descompensação psiquiátrica, agitação psicomotora, risco de auto e heteroagressividade e internação. Aduz que tentou obter o fármaco na Secretaria Municipal de Saúde e no CEJUSC/TJ Saúde, sem solução, e que a negativa se fundou no uso de Quetiapina e em critérios do PCDT.</p>
<p class='rec'><b>Decido.</b> Defiro a gratuidade da justiça (art. 98 do CPC), considerando a declaração de hipossuficiência apresentada e o fato de estar assistida pela Defensoria Pública, inexistindo, neste momento, elemento capaz de infirmar a presunção legal. Defiro a prioridade de tramitação, pela condição de pessoa com deficiência e pela documentação médica. Anote-se.</p>
<p class='rec'>A tutela de urgência exige probabilidade do direito e perigo de dano (art. 300 do CPC). A probabilidade do direito encontra suporte suficiente na documentação inicial. O laudo do CAPS informa que a autora, com idade entre 60 e 65 anos, tem transtorno psiquiátrico crônico (esquizofrenia, CID F20), com quadro grave e limitação funcional relevante, acamada e dependente de terceiros. O mesmo documento registra que a Risperidona 2 mg é parte essencial do tratamento, indispensável e insubstituível no momento, para controle de sintomas psicóticos, agitação, alterações comportamentais e desorganização do pensamento.</p>
<p class='rec'>Há demonstração de resistência administrativa: a documentação indica negativa para a Risperidona, com fundamento no PCDT e no uso de Quetiapina.</p>
""",
JUIZO + """
<p class='rec'>Embora os Protocolos Clínicos e Diretrizes Terapêuticas sejam instrumentos relevantes de racionalização, segurança e organização da política pública, não têm caráter absoluto a ponto de impedir a análise judicial do caso concreto, sobretudo quando há laudo médico individualizado, emitido por profissional da própria rede pública, indicando a necessidade específica da associação medicamentosa. Nesta fase de cognição sumária, não é razoável substituir a conduta do profissional que acompanha a paciente por negativa administrativa genérica fundada exclusivamente em protocolo.</p>
<p class='rec'>O perigo de dano é evidente. A autora é interditada, acamada e dependente de terceiros, e a interrupção do tratamento pode agravar o quadro, com risco à sua integridade física.</p>
<p class='rec'>Ante o exposto, <b>DEFIRO A TUTELA DE URGÊNCIA</b> para determinar que o ESTADO DE MATO GROSSO DO SUL e o MUNICÍPIO DE VILA BOA ESPERANÇA/MS, solidariamente, forneçam à autora, no prazo de 30 (trinta) dias, o medicamento RISPERIDONA 2 mg, conforme prescrição médica, sob pena de sequestro de valores.</p>
<p class='rec'>Citem-se e intimem-se os requeridos para cumprimento e, querendo, contestação no prazo legal. Intime-se o Ministério Público, diante da incapacidade civil da autora.</p>
<p class='rec'>Vila Boa Esperança, datado e assinado digitalmente.</p>
<div class='ass'><span class='l'>Leonardo Prates Cunha<br>Juiz de Direito</span></div>
"""]

NAT_CAB = "<p class='inst'>NÚCLEO DE APOIO TÉCNICO DO JUDICIÁRIO (NATJus)</p><p class='sub'>Tribunal de Justiça do Estado de Mato Grosso do Sul</p>"
NATJUS = [NAT_CAB + """
<p>Autos: """ + PROC + """<br>Ação: Procedimento Comum Cível, Vila Boa Esperança, 2ª Vara<br>Requerente: Rosa Maria Andrade Lemes<br>Requeridos: Município de Vila Boa Esperança e Estado de Mato Grosso do Sul</p>
<h1>Nota Técnica do NATJus nº 3318/2026</h1>
<h3>I. Problema de saúde, diagnóstico, história clínica e CID</h3>
<p class='rec'>Segundo laudo médico e demais documentos, a requerente tem entre 60 e 65 anos, reside em Vila Boa Esperança/MS e é portadora de Esquizofrenia Paranoide (CID-10: F20.0). Quanto aos tratamentos, realiza acompanhamento contínuo (tratamento não farmacológico) e faz uso de Risperidona e Quetiapina, sendo que esta última proporcionou melhora parcial do quadro clínico. Não foram apresentados histórico de tratamentos farmacológicos e não farmacológicos.</p>
<h3>II. Medicamento, incorporação ao SUS e ente responsável (fluxos do Tema 1234 do STF)</h3>
<table><tr><th>Medicamento solicitado</th><th>Posologia</th><th>Ente responsável</th></tr><tr><td>Risperidona</td><td>2 mg, 01 comprimido/noite</td><td>REMUME/Vila Boa Esperança</td></tr></table>
<p class='rec'>A REMUME de Vila Boa Esperança/MS segue as diretrizes da RENAME e contempla a Risperidona 2 mg comprimido, sujeita a receituário de controle especial C1, o que indica sua padronização municipal para dispensação conforme critérios assistenciais e regulatórios.</p>
<p class='rec'>Consta registro da paciente na Farmácia Estadual de Medicamentos Especializados, protocolo 900.25.000188-2, unidade SMS Vila Boa Esperança, para Quetiapina 25 mg comprimido, com vigência de 03/03/2026 a 02/09/2026 e dispensação em 12/02/2026 (a paciente usa a medicação há vários anos). Consta também o protocolo 900.25.000412-6, da mesma unidade, para Risperidona 2 mg comprimido, com situação indeferida.</p>
<p class='rec'>Conforme o PCDT de Esquizofrenia, o fornecimento dos antipsicóticos padronizados (risperidona, quetiapina, ziprasidona, olanzapina, clozapina, clorpromazina, haloperidol e decanoato de haloperidol) depende dos critérios de inclusão, especialmente o diagnóstico de esquizofrenia, recomendado o uso de um medicamento por vez, em monoterapia, com reavaliação e eventual substituição por outro antipsicótico em caso de falha terapêutica.</p>
""",
NAT_CAB + """
<h3>III. Custo do medicamento</h3>
<p class='rec'>A Risperidona tem genérico e similar. Preços do painel da CMED/ANVISA (PF: preço fábrica; PMC: preço máximo ao consumidor; PMVG: preço máximo de venda ao governo), alíquota de 17%, consultados em 03/03/2026:</p>
<p class='cx'>RISPERIDONA (EUROFARMA LABORATÓRIOS S.A.) 2 MG COM REV CT BL AL PLAS PVC/PVDC TRANS X 30; PF: R$ 28,02; PMC: R$ 38,62; PMVG: R$ 21,99.</p>
<h3>IV. Conclusão</h3>
<p class='rec'>A paciente apresentou documentos médicos da rede pública de saúde, e não há dados clínicos que indiquem risco iminente à vida da paciente. A Risperidona está padronizada na REMUME do município de Vila Boa Esperança. Em face do exposto, este Núcleo de Apoio Técnico manifesta-se <b>favorável ao pedido de Risperidona sob responsabilidade do município</b>.</p>
<p class='rec'>03 de março de 2026.</p>
<p class='rec'>Equipe técnica do NATJus (médicos, enfermeiros e farmacêuticos), assinado por certificação digital.</p>
"""]

DOCS = [
    ("01-peticao-inicial", "Petição inicial", INICIAL),
    ("02-laudo-medico", "Laudo médico do CAPS", LAUDO),
    ("03-receita", "Receita (duas vias)", RECEITA),
    ("04-questionario-medico", "Questionário médico da Defensoria", QUEST),
    ("05-declaracao-hipossuficiencia", "Declaração de hipossuficiência", DECL),
    ("06-negativa-administrativa", "Ofício, CEJUSC e resposta do Estado", NEG),
    ("07-decisao-tutela", "Decisão sobre a tutela de urgência", DECISAO),
    ("08-nota-tecnica-natjus", "Nota técnica do NATJus", NATJUS),
]

if __name__ == "__main__":
    DEST.mkdir(parents=True, exist_ok=True)
    tmp = pathlib.Path(tempfile.mkdtemp())
    for nome, titulo, pags in DOCS:
        h = tmp / f"{nome}.html"
        h.write_text(doc(titulo, pags), encoding="utf-8")
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                        f"--print-to-pdf={DEST / (nome + '.pdf')}", h.as_uri()], check=True, capture_output=True)
        print(nome, len(pags))
