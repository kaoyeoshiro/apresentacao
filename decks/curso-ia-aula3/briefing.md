# Briefing: curso de IA da co.juris, dia 2, Aula 3. Fazer (versão 2, 05/11/2026)

Primeira de duas aulas de cerca de 90 minutos do dia 2. A segunda é `decks/curso-ia-aula4` ("Decidir"). O desenho das
duas está em `docs/curso-ia-dia2.md`, e o plano de montagem em `docs/curso-ia-dia2-plano.md`. O deck é montado por
`montar.py` a partir de `fonte/`; edite `fonte/`, nunca o `deck.html`.

A versão 2 aplica os 15 itens do conselho de 05/11/2026 (`docs/councils/2026-11-05-briefing-aula3/documento-final.md`
e `decisao.md`) e três decisões do professor da mesma data: o Claude for Word fica só como slide de cartões, sem
demonstração; o nome do ministro relator pode aparecer na tela, por ser agente público no exercício da função e constar
do dado aberto do STJ (nome de parte continua proibido); os temas votáveis do scraper são os que dão resultado no STJ.

## Para quem, onde e o que fica

- Mesma turma do dia 1: advogados, uma desembargadora, servidores e assessores; muitos sem plano pago. Exemplos neutros,
  que servem a escritório, gabinete e órgão público.
- Sala presencial, projetor e passador. Tema `cojuris`, plano contínuo, a mesma trilha dourada das Aulas 1 e 2.
- Mensagem em uma frase: a IA trabalha fora do chat quando você lhe dá o jeito (skill), a tomada (conector e plugin) e a
  agenda (rotina), e você continua conferindo a fonte.
- No fim, cada um sabe ler uma skill antes de instalar, reconhecer um documento que dá ordens e separar o que se agenda
  do que não se automatiza; o kit fica no GitHub para refazer as demonstrações em casa.
- Dinâmica: o professor faz as demonstrações ao vivo, só no Claude, na tela compartilhada; a sala faz seis atividades
  curtas (A1 a A6) com enunciado no slide e cronômetro, sem plano pago, instalação nem papel.
- Zero `[CONFERIR]` na tela. Logos e marcas de terceiros não entram; as telas de app são desenhadas por código.
- Linha do dia (90 min): abertura 4, skills e Word 24, MCP e plugins 16, scraper 20, GitHub 5, rotinas e fecho 21. O
  ensaio cronometrado de ponta a ponta decide se cabe; o teto de cada demonstração vai nas notas.

## Arco

A Aula 2 terminou com "trabalhe no caso, não no chat". A Aula 3 abre com a tensão do passo seguinte: o caso está na
pasta, mas a peça ainda sai sem o timbre, o agente não alcança os sistemas e a pesquisa recomeça do zero toda semana.
Cinco movimentos respondem, cada um com um S.T.A.R.: a skill que a própria sala dita (skills), o documento que dá ordens
que o olho não vê e o agente lê (MCP), o script curto que coleta acórdãos ao vivo (scraper), a página do repositório
(GitHub) e a pergunta "se falhar em silêncio, o que se perde?" (rotinas). O fecho entrega o pedido: dar à IA o jeito, a
tomada e a agenda, e conferir a fonte.

## Regra das demonstrações ao vivo

Uma tentativa ao vivo por demonstração. Sem resultado útil em 60 segundos (40 segundos no TJMS), o professor para, toca
a gravação do ensaio que está na moldura do slide e a sala avalia o resultado preparado. Entradas fictícias e resultados
offline ficam prontos para cada etapa. A página salva do TJMS é apresentada como gravação do ensaio, nunca como coleta
ao vivo. Isso vai nas notas `faca` dos slides 6, 14, 29, 31, 38 e 40. Planos, menus e o limite do plano gratuito são
revalidados na conta do ensaio; o que divergir ganha nota de contingência.

## Roteiro

Clima e densidade pela parada final: respiro até 12 palavras, leve de 13 a 24, médio de 25 a 45. "Própria" é cena sem
`data-arquetipo` (como as da Aula 2); "guia" é a cena própria das atividades, com passos, cronômetro (`pratica`) e o
enunciado na tela; "cartões" e "partes" são os ajudantes de `base.meio.js`.

| # | slide | manchete | o que a tela prova | clima e densidade | arquétipo | mídia e custo |
|---|---|---|---|---|---|---|
| 1 | capa | A IA fora do chat | abertura da Aula 3; sub: "Skills, MCP, plugins, scraper, GitHub e rotinas, ao vivo." | noite, respiro | abertura | heroica gerada 2K, cerca de US$ 0,05 |
| 2 | mapa | Hoje, do arquivo ao mundo | cinco marcos (Skills, MCP, Scraper, GitHub, Rotinas), Skills aceso | claro, leve | tempo | código |
| 3 | pecas | Quatro peças em volta do agente | **S.T.A.R. do bloco.** O agente no centro; skill "o jeito", conector "a tomada", plugin "o pacote", rotina "a agenda" acendem uma a uma | claro, leve | própria (diagrama, herdeiro do `liga` da Aula 2) | código |
| 4 | word-cap | Do rascunho ao papel timbrado. | respiro que abre o bloco de skills (capítulo) | noite, respiro | respiro | nenhuma |
| 5 | word-antes | O mesmo rascunho, outro acabamento | A "sem skill" (texto corrido) e B "com o modelo do escritório" (timbre, estilos, numeração), B circulada | claro, leve | comparacao | código |
| 6 | word-demo | Ao vivo, o parecer no timbre | nota: "Rascunho em Markdown, modelo do escritório, Word pronto. Confira as páginas." | noite, respiro | demonstracao | reserva gravada no ensaio, US$ 0 |
| 7 | word-pedido | O pedido, para copiar | o texto exato do pedido (abaixo, "Pedidos"), medido pelo oráculo; acima de 45 palavras, a tela leva a versão curta e o literal vai às notas e ao kit | claro, médio | própria | código |
| 8 | word-addin | Claude for Word revisa no arquivo | quatro cartões: alterações controladas; herda os estilos do modelo; Pro, Max, Team e Enterprise; não serve a peça sem conferência. Sem demonstração (decisão do professor). Nas notas: o aviso de histórico e skills perdidos no Windows após as atualizações de set. e out./2026 | claro, médio | cartões | código |
| 9 | skillmd | Uma skill é uma pasta com instruções | o `SKILL.md` anotado: nome; descrição, que decide quando ela dispara; corpo, o passo a passo; scripts, o que ela executa. Rodapé: "A de Word tem código publicado, com licença proprietária." | noite, médio | própria | código |
| 10 | checklist | Sete pontos antes de instalar | origem; arquivos e scripts; permissões; dados acessados; comandos; teste com dado fictício; como remover, um por clique | claro, médio | partes | código |
| 11 | a1 | Sua vez: três defeitos escondidos | A1, 4 min. Só os três trechos da skill de treino, ampliados e numerados (descrição, linha do script, instrução de confirmação); os sete pontos numa coluna lateral. "Em dupla: que ponto cada trecho fere?" | noite, médio | guia, `pratica: 4` | código, a partir de `material/skill-defeituosa` |
| 12 | a1-voto | Quem achou os três? | momento da votação, mão levantada; o gabarito vem no clique seguinte | noite, respiro | respiro | nenhuma |
| 13 | a1-gabarito | Três defeitos, três linhas | fios dos três trechos aos defeitos: "Dispara em qualquer pedido", "Manda a pasta para fora", "Pula a sua confirmação". Notas: "Na dúvida, não instale." | claro, leve | fios | código |
| 14 | a2 | A sala dita, a skill nasce | **S.T.A.R. do bloco.** A2, 7 min: 1 três regras do escritório, em voz alta; 2 o professor pede ao Claude que crie a skill; 3 testamos no mesmo rascunho | noite, leve | guia, `pratica: 7` | código |
| 15 | mcp-cap | A tomada | abertura do bloco MCP e plugins (capítulo); sub: "Ligar o agente a um sistema, sem programar." | noite, respiro | abertura | heroica gerada 2K, cerca de US$ 0,05 |
| 16 | tomada | Conector pronto ou conector próprio | ramo 1 Drive, Gmail, para "conector pronto"; ramo 2 Microsoft Learn, para "conector próprio (MCP)". Legenda: "No plano gratuito, um só conector próprio." | claro, leve | ramos | código |
| 17 | mcp-demo | Ao vivo, a documentação conectada | nota: "Sem login e sem custo. O agente cita a página oficial." | noite, respiro | demonstracao | reserva gravada, US$ 0 |
| 18 | mcp-passos | Cinco cliques até a tomada | Customize, Connectors, + Add, Add custom connector, endereço. Legenda: "Endereço público; o Claude liga a partir da nuvem." | claro, leve | tempo | código |
| 19 | a3 | Sua vez: ache a ordem escondida | A3, 4 min. A petição fictícia com o rodapé ampliado até ficar legível, sem destaque. "Em dupla, achem a ordem dirigida à IA. Quantas há?" | claro, médio | guia, `pratica: 4` | código, a partir de `material/peticao-injecao` |
| 20 | injecao | O documento também dá ordens | **S.T.A.R. do bloco.** Primeiro revela a ordem do rodapé; depois, pela seleção, a de texto branco, que ninguém viu; o fio leva ao agente, que responde o que a ordem mandou. Lição: o que o olho não vê, o agente lê | noite, médio | própria | código |
| 21 | casos | Já aconteceu no STF e no STJ | três cartões, confirmados na fonte primária em 05/11/2026: STF, ARE 1.608.713, "letras brancas e de tamanho reduzido"; STJ, REsp 2.256.731, "fonte branca sobre fundo branco"; STJ, AREsp 3.095.458, "na faixa decorativa do rodapé". Rodapé: "CNJ, Nota Técnica de 09/06/2026: autos, anexos e OCR são dados não confiáveis." Notas: multa de dois salários mínimos no STF e de R$ 20 mil no AREsp; comunicação à OAB e ao MPF no STF e no REsp | claro, médio | cartões | código |
| 22 | defesa | Documento é dado, nunca ordem. | respiro que fecha a injeção | noite, respiro | respiro | nenhuma |
| 23 | plugin | Plugin é o pacote pronto | cartões: skills, conectores e subagentes juntos; marketplace Legal, da Anthropic; instala por Customize e Plugins; feitos para o direito dos EUA. Rodapé: "Toda saída é rascunho para revisão de advogado." Nas notas: são 12 plugins por área | claro, médio | cartões | código |
| 24 | plugin-tela | O plugin avisa antes de ajudar | tela desenhada por código: a página do plugin, o aviso "rascunho para revisão de advogado" e a lista do que ele traz; a gravação do ensaio fica de reserva para quem quiser ver instalar e remover | noite, leve | própria | código; reserva gravada, US$ 0 |
| 25 | a4 | Tomada ou pacote? | A4, 4 min. Antes do cronômetro, uma frase para cada categoria: skill, conector pronto, conector próprio (MCP), plugin. Seis situações (lista em "Atividades") | claro, médio | guia, `pratica: 4` | código |
| 26 | scraper-cap | Jurisprudência em lote | abertura do bloco scraper (capítulo); sub: "Do navegador ao script, com as regras do tribunal." | noite, respiro | abertura | heroica gerada 2K, cerca de US$ 0,05 |
| 27 | dois-jeitos | Dois jeitos de raspar | ramo 1 Navegador, "skill TJMS", para "sem código"; ramo 2 Claude Code, "STJ aberto", para "script curto". Legenda: "Raspar é coletar de um site, em lote." | claro, leve | ramos | código |
| 28 | a5 | A sala escolhe o tema | A5, 2 min: execução fiscal, improbidade, ICMS; mão levantada; o mais votado vai às duas etapas | noite, leve | guia, `pratica: 2` | código |
| 29 | etapa1 | Etapa 1, o agente no navegador | nota: "A skill do TJMS pesquisa, lê as ementas e baixa só o pertinente." | noite, respiro | demonstracao | reserva gravada, US$ 0 |
| 30 | etapa2-pedido | Etapa 2, o pedido ao Claude Code | a versão de tela do pedido, até 30 palavras e sem siglas; o literal fica nas notas e no kit | claro, médio | própria | código |
| 31 | etapa2 | Ao vivo, o script trabalha | **S.T.A.R. do bloco.** Nota: "Dados abertos do STJ, licença livre, sem senha nem captcha." | noite, respiro | demonstracao | reserva gravada e modo offline, US$ 0 |
| 32 | conferir | Cada linha volta ao acórdão | A5, segunda parte: três linhas da planilha e o recorte de cada espelho, desenhados por código a partir do JSON; "As duplas conferem número, órgão, data e trecho da ementa." Três variantes, uma por tema (`amostra/execucao.csv`, `improbidade.csv`, `icms.csv`); o professor salta para a do tema votado com a tecla G | claro, médio | fios | código |
| 33 | limites | Raspar com educação | cartões: pesquise por tema, nunca por pessoa; uma consulta por vez, com pausa; dados abertos primeiro; captcha é recusa. No cartão do tema, a referência "padrão da Res. CNJ 121/2010, art. 5º"; nas notas, o texto literal e a ressalva de que a regra se dirige aos tribunais | noite, médio | cartões | código |
| 34 | captcha | Encontrou captcha? Pare a automação. | respiro que fecha o bloco | noite, respiro | respiro | nenhuma |
| 35 | repositorio | Repositório é pasta com histórico | **S.T.A.R. do bloco.** A página de um repositório desenhada por código; um clique por termo, apontado sobre ela: README, "o que é e como usar"; Download ZIP, "a pasta, sem o histórico"; issue, "um pedido ou problema anotado"; pull request, "uma proposta de mudança" | claro, médio | própria | código |
| 36 | rotinas-cap | Trabalho agendado | abertura do bloco rotinas (capítulo); sub: "O que roda sozinho, e o que nunca deveria." | noite, respiro | abertura | heroica gerada 2K, cerca de US$ 0,05 |
| 37 | semana | O boletim chega antes de você | quatro segundas às 7h10, boletim; a de hoje acesa. Legenda: "Na nuvem, roda com o computador desligado, se não depender de arquivo local." | claro, leve | tempo | código |
| 38 | rotina-demo | Ao vivo, a tarefa semanal | nota: "Consulta direta ao STJ, sem arquivo local. Cada julgado se confere." Se o ensaio com o computador desligado falhar, vira gravação e a legenda do 37 deixa de prometer execução autônoma | noite, respiro | demonstracao | reserva gravada, US$ 0 |
| 39 | agendavel | Agendar, conferir ou não automatizar | **S.T.A.R. do bloco.** Três colunas: sim, boletim de jurisprudência; com conferência, lista preliminar de intimações; não, prazo, e-mail e protocolo. Rodapé: "Se falhar em silêncio, o que se perde?" | claro, médio | cartões | código |
| 40 | a6 | Sua vez: o que é agendável? | A6, 8 min: três tarefas fictícias para classificar (2 min); depois até duas sugestões da sala; o professor cria a rotina de uma delas só se couber em "sim" | noite, médio | guia, `pratica: 8` | código |
| 41 | levar | O que você leva hoje | cinco marcos: skill, conector, scraper, GitHub, rotina; "conferir a fonte" aceso | claro, leve | tempo | código |
| 42 | kit | O kit está no GitHub | endereço do repositório e código QR desenhado por código | claro, leve | própria | código |
| 43 | fecho | Dê o jeito, a tomada e a agenda. | mensagem da aula; abaixo, "Confira a fonte." Notas: ponte para a Aula 4 | noite, respiro | fecho | nenhuma |

Mídia prevista: quatro heroicas geradas (capa e três capítulos), cerca de US$ 0,20, mais três rascunhos de cada,
dentro do teto de US$ 2,00 do `./ap imagens`. O resto é código ou gravação de tela sem custo.

### Conferência do roteiro (lista do fim de `roteiro.md`)

1. Arco com tensão na abertura, cinco movimentos e fecho com pedido: sim.
2. Um S.T.A.R. por bloco: pecas (abertura), a2 (skills), injecao (MCP), etapa2 (scraper), repositorio (GitHub),
   agendavel (rotinas).
3. Nenhum trio com o mesmo clima e a mesma faixa; a maior sequência sem respiro tem cinco slides (7 a 11).
4. Nenhum par de vizinhos repete o arquétipo; as cenas próprias e os ajudantes não levam `data-arquetipo`.
5. Manchetes de até oito palavras e uns 36 caracteres.
6. Nenhuma parada prevista acima de 45 palavras; os pedidos (7 e 30) são medidos pelo oráculo e não caem para corpo
   menor.
7. Mais da metade dos slides tem diagrama, página, tela desenhada ou vídeo como elemento dominante.
8. Cada dado tem fonte abaixo; o que não for confirmado na fonte primária sai da tela.
9. Gasto previsto somado na coluna mídia; nada acima do teto.

## Pedidos (texto exato da tela e das notas)

**Word (slide 7).** "Use o modelo do escritório anexo (modelo-timbrado.docx). Transforme este rascunho em parecer no
padrão do modelo, com o mesmo cabeçalho, estilos e numeração. No fim, gere o PDF e me diga o que não coube no modelo."

**Scraper, etapa 1 (notas do slide 29).** "Pesquise no TJMS acórdãos de segundo grau sobre [tema votado], julgados nos
últimos três meses. Leia as ementas, baixe só os pertinentes e me dê uma planilha com processo, relator, data e o
motivo de cada escolha."

**Scraper, etapa 2, versão de tela (slide 30).** "Escreva um programa que baixe os espelhos de acórdãos de setembro de
2026 da Primeira Turma, nos Dados Abertos do STJ, filtre as ementas por [tema] e grave uma planilha."

**Scraper, etapa 2, literal (notas do slide 30 e kit).** "Escreva um script em Python que baixe o arquivo de espelhos
de acórdãos de setembro de 2026 da Primeira Turma nos Dados Abertos do STJ, filtre as ementas por [tema votado] e grave
um CSV com classe, processo, relator, órgão, data e ementa. Uma requisição por vez."

**Rotina (notas do slide 38).** "Toda segunda às 7h10, consulte os Dados Abertos do STJ, abra o arquivo mais recente de
espelhos de acórdãos da Primeira Turma e liste os acórdãos sobre [tema votado], cada um com número, data e ementa
resumida. Diga a data do arquivo consultado." A rotina não guarda estado entre execuções e não usa arquivo local; os
espelhos saem um arquivo por mês, por isso a frequência é semanal.

## Atividades (enunciado na tela, gabarito nas notas)

- **A1, auditoria relâmpago (slides 11 a 13, 4 min).** Os três trechos da skill de treino
  (`material/skill-defeituosa/SKILL.md`): a descrição que dispara em qualquer pedido (fere "permissões" e "dados
  acessados"), a linha do script que envia a pasta a um endereço externo (fere "arquivos e scripts" e "comandos"), a
  instrução de executar sem confirmação (fere "comandos"). Votação no slide 12, gabarito no 13.
- **A2, a sala dita (slide 14, 7 min).** Três regras ditas pela sala; o professor pede ao Claude que crie a skill a
  partir delas e roda no mesmo rascunho da demonstração do Word.
- **A3, caça à injeção (slides 19 e 20, 4 min).** A petição fictícia (`material/peticao-injecao/peticao-injecao.pdf`)
  tem duas ordens: uma no rodapé, em corpo minúsculo (ampliado no slide 19, para ser achada), e outra em texto branco,
  que só a seleção revela no slide 20.
- **A4, tomada ou pacote (slide 25, 4 min).** Categorias: skill, conector pronto, conector próprio (MCP), plugin.
  Situações e gabarito: "Ler meu Gmail" (conector pronto); "Documentação oficial da Microsoft" (conector próprio, MCP);
  "Modelo de parecer do escritório" (skill); "Sistema interno com endereço próprio" (conector próprio, MCP); "Pacote de
  contencioso pronto" (plugin); "Padrão de citação do gabinete" (skill).
- **A5, o tema da sala (slides 28 e 32, 2 min mais a conferência).** Temas: execução fiscal, improbidade e ICMS, que
  deram 45, 20 e 18 acórdãos de 471 no arquivo de setembro/2026 da Primeira Turma, no teste de 05/11/2026 ("medicamento"
  dava zero). Na véspera, os três são rodados de novo no arquivo usado; tema que vier vazio sai da votação. Na
  conferência, as duplas conferem número, órgão, data e trecho da ementa de três linhas contra o recorte do espelho.
- **A6, agendável ou não (slide 40, 8 min).** Três tarefas fictícias e o gabarito pela pergunta do slide 39: "boletim
  semanal de notícias do CNJ" (agendar); "resumo semanal da pasta do caso" (agendar com conferência, com o computador
  ligado e gravação só em `saida/`); "controle de prazos do escritório" (não automatizar: fica no sistema oficial, com
  quem assina). Depois, até duas sugestões orais; a rotina ao vivo só sai se a sugestão couber em "agendar"; senão, o
  professor cria a do boletim já preparado.

## Fontes por slide

Fichas de 05/11/2026: `docs/pesquisa/dia2-ferramentas-aula3.md` (F) e `docs/pesquisa/dia2-scraper-jurisprudencia.md`
(S). Apostila v2 (A): `/Volumes/Projetos/Academic-Writing-System/artigos_livros/direito_ia/ebooks/apostila-v2/content/`.

| slides | afirmação | fonte |
|---|---|---|
| 6, 7 | skill de Word funciona com "Create and edit files" ligado, em todos os planos; acionada por pedido de Word, `.docx` ou papel timbrado; converte em PDF e olha as páginas | F 1.1 (support.claude.com 12512180; github.com/anthropics/skills, `skills/docx/SKILL.md`) |
| 8 | Claude for Word: Pro, Max, Team e Enterprise; herda estilos; alterações controladas; não recomendado para "Litigation filings or audit-critical documents without verification"; aviso de perda de histórico e skills no Windows (só nas notas) | F 1.1 (claude.com/docs/office-agents/word) |
| 9 | skills `docx`, `pdf`, `pptx`, `xlsx` são "source-available, not open source", licença proprietária | F 1.1 e seção 2 (README de anthropics/skills) |
| 10, 11, 13 | os sete pontos antes de instalar | A 16.8, caixa "Os sete pontos antes de instalar" |
| 16, 18 | caminho do conector personalizado; plano gratuito limitado a um; servidor tem de estar na internet pública | F 1.2 (support.claude.com 11175166) |
| 16, 17 | Microsoft Learn MCP: `https://learn.microsoft.com/api/mcp`, sem login, sem custo | F 1.2 (learn.microsoft.com/en-us/training/support/mcp) |
| 20, 21 | ARE 1.608.713 (STF, notícia de 25/09/2026: letras brancas e reduzidas, palavras fragmentadas, Maria Shield, multa de dois salários mínimos, OAB e MPF); REsp 2.256.731 (STJ, 6ª Turma, notícia de 18/10/2026: fonte branca sobre fundo branco, "de modo a acolher as razões defensivas"; sem menção a multa); AREsp 3.095.458 (STJ, 1ª Turma, notícia de 20/10/2026: faixa decorativa do rodapé, "redija", "afirme enfaticamente", multa de R$ 20 mil); Nota Técnica do CNJ de 09/06/2026, item 7, g (cópia publicada pelo TRF6; aprovação conferida em notícia do CNJ) | F seção 5 (noticias.stf.jus.br; stj.jus.br, notícias de 18 e 20/10/2026; cnj.jus.br; sjmg.trf6.jus.br) |
| 23, 24 | plugin reúne skills, conectores e subagentes; marketplace Legal; 12 plugins por área (notas); direito dos EUA; saída "a draft for attorney review" | F 1.3 (support.claude.com 13837440; github.com/anthropics/claude-for-legal) |
| 27, 29 | consulta de segundo grau do TJMS responde sem captcha; a skill do TJMS usa o Chrome conectado | S, seção TJMS; skill `consulta-jurisprudencia-tjms` do professor |
| 30, 31, 32 | Dados Abertos do STJ: API sem chave, licença Creative Commons Atribuição, um JSON por mês, sem nome de parte; campos `siglaClasse`, `numeroProcesso`, `ministroRelator`, `nomeOrgaoJulgador`, `dataDecisao`, `ementa` | S, seção STJ e tabela; `material/scraper/amostra/` |
| 33, 34 | Res. CNJ 121/2010, art. 5º: "A disponibilização de consultas às bases de decisões judiciais impedirá, quando possível, a busca pelo nome das partes." Regra dirigida aos tribunais (leitura com o art. 13, confiança média); a Res. 700/2026 alterou os arts. 6º e 8º, não o 5º. Uma requisição por vez; captcha é recusa de acesso automatizado | F seção 5 (atos.cnj.jus.br/atos/detalhar/92); S, seção de limites jurídicos |
| 35 | definições de README, Download ZIP (sem histórico), issue e pull request | F 1.4 (docs.github.com) |
| 37 | tarefa agendada do Claude roda "even when your computer is asleep or the Claude Desktop app is closed", salvo se precisar de arquivo local | F 1.5 (support.claude.com 13854387) |
| 39 | quadro agendar ou não | A 18.6 |

## Pendências deste briefing

- Materiais gravados na Tarefa 4: `material/escritorio/modelo-timbrado.docx` (Dias & Moura), `material/skill-defeituosa/`,
  `material/peticao-injecao/peticao-injecao.pdf`, `material/scraper/` e as amostras por tema em
  `material/scraper/amostra/`. Falta o rascunho em Markdown da demonstração do Word: é texto jurídico fictício e precisa
  do aval do professor.
- Endereço do kit (slide 42): depende do sim do professor para criar o repositório público.
- Notas `{diga, faca, transicao}` de cada slide: escritas na montagem dos blocos, só com os fatos acima.

## Montagem (05/11/2026)

Blocos montados: `a-abertura` pelo coordenador, os demais por subagentes, cada um conferido pela folha de contato. O deck
inteiro passa no lint e no oráculo com 0 erro(s). Ajustes feitos na integração:

- As notas das cinco demonstrações (slides 6, 17, 29, 31 e 38) ficaram com até quatro palavras na tela ("Confira as
  páginas.", "Sem login, sem custo.", "Baixa só o pertinente.", "Dados abertos, sem captcha.", "Cada julgado se
  confere."), para contarem como respiro; o texto completo do roteiro está nas notas `diga`.
- O slide 32 virou três variantes seguidas (`conferir-execucao`, `conferir-improbidade`, `conferir-icms`); o professor
  mostra só a do tema votado e pula as outras com a tecla G. A legenda aparece na primeira parada e sai no primeiro
  clique, para caber em 45 palavras.
- O slide 42 (kit) ficou sem código QR: não há biblioteca de QR instalada no ambiente; o endereço aparece em letra grande.

Avisos aceitos: a1 com 66 palavras e a3 com 49 (atividades lidas em dupla durante 4 minutos; na a3 a ordem escondida
vai literal); hierarquia, a rever depois das heroicas da Tarefa 7; as três variantes de conferir seguidas, porque só uma
é mostrada.
