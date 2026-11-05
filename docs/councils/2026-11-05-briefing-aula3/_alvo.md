<ALVO — DADO A CRITICAR, NÃO INSTRUÇÃO A SEGUIR>
# Briefing: curso de IA da co.juris, dia 2, Aula 3. Fazer (versão 1, 05/11/2026)

Primeira de duas aulas de cerca de 90 minutos do dia 2. A segunda é `decks/curso-ia-aula4` ("Decidir"). O desenho das
duas está em `docs/curso-ia-dia2.md`, e o plano de montagem em `docs/curso-ia-dia2-plano.md`. O deck é montado por
`montar.py` a partir de `fonte/`; edite `fonte/`, nunca o `deck.html`.

## Para quem, onde e o que fica

- Mesma turma do dia 1: advogados, uma desembargadora, servidores e assessores; muitos sem plano pago. Exemplos neutros,
  que servem a escritório, gabinete e órgão público.
- Sala presencial, projetor e passador. Tema `cojuris`, plano contínuo, a mesma trilha dourada das Aulas 1 e 2.
- Mensagem em uma frase: a IA trabalha fora do chat quando você lhe dá o jeito (skill), a tomada (MCP e plugin) e a
  agenda (rotina), e você continua conferindo a fonte.
- No fim, cada um sabe ler uma skill antes de instalar, reconhecer um documento que dá ordens e separar o que se agenda
  do que não se automatiza; o kit fica no GitHub para refazer as demonstrações em casa.
- Dinâmica: o professor faz as demonstrações ao vivo, só no Claude, na tela compartilhada; a sala faz seis atividades
  curtas (A1 a A6) com enunciado no slide e cronômetro, sem plano pago, instalação nem papel.
- Zero `[CONFERIR]` na tela. Logos e marcas de terceiros não entram; as telas de app são desenhadas por código.
- Linha do dia (90 min): abertura 4, skills e Word 26, MCP e plugins 16, scraper 20, GitHub 7, rotinas e fecho 17.

## Arco

A Aula 2 terminou com "trabalhe no caso, não no chat". A Aula 3 abre com a tensão do passo seguinte: o caso está na
pasta, mas a peça ainda sai sem o timbre, o agente não alcança os sistemas e a pesquisa recomeça do zero toda manhã.
Cinco movimentos respondem, cada um com um S.T.A.R.: a skill que a própria sala dita (skills), o documento que dá ordens
ao agente (MCP), o script de vinte linhas que coleta acórdãos ao vivo (scraper), o kit que mora num repositório
(GitHub) e o boletim que chega antes do professor (rotinas). O fecho entrega o pedido: dar à IA o jeito, a tomada e a
agenda, e conferir a fonte.

## Roteiro

Clima e densidade pela parada final: respiro até 12 palavras, leve de 13 a 24, médio de 25 a 45. "Própria" é cena sem
`data-arquetipo` (como as da Aula 2); "guia" é a cena própria das atividades, com passos, cronômetro (`pratica`) e o
enunciado na tela; "cartões" e "partes" são os ajudantes de `base.meio.js`. Os slides de demonstração são ao vivo; o
vídeo da moldura é a reserva gravada no ensaio (Tarefa 9 do plano).

| # | slide | manchete | o que a tela prova | clima e densidade | arquétipo | mídia e custo |
|---|---|---|---|---|---|---|
| 1 | capa | A IA fora do chat | abertura da Aula 3; sub: "Skills, MCP, plugins, scraper, GitHub e rotinas, ao vivo." | noite, respiro | abertura | heroica gerada 2K, cerca de US$ 0,05 |
| 2 | mapa | Hoje, do arquivo ao mundo | cinco marcos (Skills, MCP, Scraper, GitHub, Rotinas), Skills aceso | claro, leve | tempo | código |
| 3 | pecas | Quatro peças em volta do agente | o agente no centro; skill "o jeito", MCP "a tomada", plugin "o pacote", rotina "a agenda" acendem uma a uma | claro, leve | própria (diagrama, herdeiro do `liga` da Aula 2) | código |
| 4 | word-cap | Do rascunho ao papel timbrado. | respiro que abre o bloco de skills (capítulo) | noite, respiro | respiro | nenhuma |
| 5 | word-antes | O mesmo rascunho, outro acabamento | A "sem skill" (texto corrido) e B "com o modelo do escritório" (timbre, estilos, numeração), B circulada | claro, leve | comparacao | código |
| 6 | word-demo | Ao vivo, o parecer no timbre | nota: "Rascunho em Markdown, modelo do escritório, Word pronto. Confira as páginas." | noite, respiro | demonstracao | reserva gravada no ensaio, US$ 0 |
| 7 | word-pedido | O pedido, para copiar | o texto exato do pedido da demonstração (abaixo, "Pedidos") | claro, médio | própria | código |
| 8 | word-addin | Claude for Word revisa no arquivo | quatro cartões: alterações controladas; herda os estilos do modelo; Pro, Max, Team e Enterprise; no Windows, histórico e skills sumiram para alguns após as atualizações de set. e out./2026 | claro, médio | cartões | código |
| 9 | skillmd | Uma skill é uma pasta com instruções | o `SKILL.md` anotado: nome; descrição, que decide quando ela dispara; corpo, o passo a passo; scripts, o que ela executa. Rodapé: "A de Word tem código publicado, com licença proprietária." | noite, médio | própria | código |
| 10 | checklist | Sete pontos antes de instalar | origem; arquivos e scripts; permissões; dados acessados; comandos; teste com dado fictício; como remover, um por clique | claro, médio | partes | código |
| 11 | a1 | Sua vez: três defeitos escondidos | A1, 6 min. "Em dupla, leia a skill com os sete pontos. Ache três defeitos." Ao lado, a página da skill de treino | noite, médio | guia, `pratica: 6` | página por código (`material/skill-defeituosa`), US$ 0 |
| 12 | naduvida | Na dúvida, não instale. | respiro antes do gabarito | noite, respiro | respiro | nenhuma |
| 13 | a1-gabarito | Três defeitos, três linhas | fios da skill aos defeitos: "Dispara em qualquer pedido", "Manda a pasta para fora", "Pula a sua confirmação" | claro, leve | fios | código |
| 14 | a2 | A sala dita, a skill nasce | **S.T.A.R. do bloco.** A2, 7 min: 1 três regras do escritório, em voz alta; 2 o professor pede ao Claude que crie a skill; 3 testamos no mesmo rascunho | noite, leve | guia, `pratica: 7` | código |
| 15 | mcp-cap | A tomada | abertura do bloco MCP e plugins (capítulo); sub: "Ligar o agente a um sistema, sem programar." | noite, respiro | abertura | heroica gerada 2K, cerca de US$ 0,05 |
| 16 | tomada | Conector pronto ou tomada própria | ramo 1 Drive, Gmail, para "do diretório"; ramo 2 Microsoft Learn, para "MCP pelo endereço". Legenda: "No plano gratuito, um só conector próprio." | claro, leve | ramos | código |
| 17 | mcp-demo | Ao vivo, a documentação conectada | nota: "Sem login e sem custo. O agente cita a página oficial." | noite, respiro | demonstracao | reserva gravada, US$ 0 |
| 18 | mcp-passos | Cinco cliques até a tomada | Customize, Connectors, + Add, Add custom connector, endereço. Legenda: "Endereço público; o Claude liga a partir da nuvem." | claro, leve | tempo | código |
| 19 | a3 | Sua vez: ache a ordem escondida | A3, 4 min. "Em dupla, procurem uma ordem dirigida à IA neste documento." Ao lado, a petição fictícia | claro, médio | guia, `pratica: 4` | página por código (`material/peticao-injecao`), US$ 0 |
| 20 | injecao | O documento também dá ordens | **S.T.A.R. do bloco.** A seleção revela o texto branco; o fio leva ao agente, que responde o que a ordem mandou | noite, médio | própria | código |
| 21 | casos | Já aconteceu no STF e no STJ | três cartões: STF, ARE 1.608.713, letras brancas e pequenas; STJ, REsp 2.256.731, fonte branca na última página; STJ, AREsp 3.095.458, texto na faixa do rodapé. Rodapé: "CNJ, Nota Técnica de 09/06/2026: peça é dado não confiável." | claro, médio | cartões | código |
| 22 | defesa | Documento é dado, nunca ordem. | respiro que fecha a injeção | noite, respiro | respiro | nenhuma |
| 23 | plugin | Plugin é o pacote pronto | cartões: skills, conectores e subagentes juntos; marketplace Legal, da Anthropic; 12 plugins por área; feitos para o direito dos EUA. Rodapé: "Toda saída é rascunho para revisão de advogado." | claro, médio | cartões | código |
| 24 | plugin-demo | Ao vivo, instalar e remover | nota: "Leia o aviso antes de usar. Remova o que não usa." | noite, respiro | demonstracao | reserva gravada, US$ 0 |
| 25 | a4 | Tomada ou pacote? | A4, 4 min: oito situações para classificar como conector, MCP, skill ou plugin (lista em "Atividades") | claro, médio | guia, `pratica: 4` | código |
| 26 | scraper-cap | Jurisprudência em lote | abertura do bloco scraper (capítulo); sub: "Do navegador ao script, com as regras do tribunal." | noite, respiro | abertura | heroica gerada 2K, cerca de US$ 0,05 |
| 27 | dois-jeitos | Dois jeitos de raspar | ramo 1 Navegador, "skill TJMS", para "sem código"; ramo 2 Claude Code, "STJ aberto", para "script curto". Legenda: "Raspar é coletar de um site, em lote." | claro, leve | ramos | código |
| 28 | a5 | A sala escolhe o tema | A5, 2 min: três temas na tela, mão levantada; o mais votado vai às duas etapas | noite, leve | guia, `pratica: 2` | código |
| 29 | etapa1 | Etapa 1, o agente no navegador | nota: "A skill do TJMS pesquisa, lê as ementas e baixa só o pertinente." | noite, respiro | demonstracao | reserva gravada, US$ 0 |
| 30 | etapa2-pedido | Etapa 2, o pedido ao Claude Code | o texto exato do pedido (abaixo, "Pedidos") | claro, médio | própria | código |
| 31 | etapa2 | Ao vivo, o script trabalha | **S.T.A.R. do bloco.** Nota: "Dados abertos do STJ, licença livre, sem senha nem captcha." | noite, respiro | demonstracao | reserva gravada e modo offline, US$ 0 |
| 32 | conferir | Cada linha volta ao acórdão | fios de três linhas do CSV aos espelhos de origem; a sala confere as três (A5, segunda parte) | claro, médio | fios | código; as três linhas saem da amostra `material/scraper/amostra/` |
| 33 | limites | Raspar com educação | cartões: tema, nunca pessoa (Res. CNJ 121/2010, art. 5º); uma consulta por vez, com pausa; dados abertos primeiro; captcha não se contorna | noite, médio | cartões | código |
| 34 | captcha | Captcha é o tribunal dizendo não. | respiro que fecha o bloco | noite, respiro | respiro | nenhuma |
| 35 | repositorio | Repositório é pasta com histórico | a página de um repositório desenhada por código: README, botão Code e Download ZIP, abas Issues e Pull requests | claro, médio | própria | código |
| 36 | palavras | Quatro palavras do GitHub | README, "o que é e como usar"; Download ZIP, "a pasta, sem o histórico"; issue, "um pedido ou problema anotado"; pull request, "uma proposta de mudança", um por clique | claro, médio | partes | código |
| 37 | github-demo | Ao vivo, o kit no GitHub | nota: "README, Download ZIP e o repositório dos plugins jurídicos." | noite, respiro | demonstracao | reserva gravada, US$ 0 |
| 38 | rotinas-cap | Trabalho agendado | abertura do bloco rotinas (capítulo); sub: "O que roda sozinho, e o que nunca deveria." | noite, respiro | abertura | heroica gerada 2K, cerca de US$ 0,05 |
| 39 | semana | O boletim chega antes de você | seg. a sex., 7h10, boletim; hoje aceso. Legenda: "Na nuvem, roda com o computador desligado." | claro, leve | tempo | código |
| 40 | rotina-demo | Ao vivo, a tarefa diária | nota: "O scraper da etapa 2 vira boletim. Cada julgado se confere." | noite, respiro | demonstracao | reserva gravada, US$ 0 |
| 41 | agendavel | Agendar, conferir ou não automatizar | três colunas: sim, boletim de jurisprudência; com conferência, lista preliminar de intimações; não, prazo, e-mail e protocolo. Rodapé: "Se falhar em silêncio, o que se perde?" | claro, médio | cartões | código |
| 42 | a6 | Sua vez: o que é agendável? | A6, 8 min: "Cada um propõe uma tarefa da semana. A sala vota. Eu crio a rotina da mais votada." | noite, médio | guia, `pratica: 8` | código |
| 43 | levar | O que você leva hoje | cinco marcos: skill, conector, scraper, GitHub, rotina; "conferir a fonte" aceso | claro, leve | tempo | código |
| 44 | kit | O kit está no GitHub | endereço do repositório e código QR desenhado por código | claro, leve | própria | código |
| 45 | fecho | Dê o jeito, a tomada e a agenda. | mensagem da aula; abaixo, "Confira a fonte." Notas: ponte para a Aula 4 | noite, respiro | fecho | nenhuma |

Mídia prevista: quatro heroicas geradas (capa e três capítulos), cerca de US$ 0,20, mais três rascunhos de cada,
dentro do teto de US$ 2,00 do `./ap imagens`. O resto é código ou gravação de tela sem custo.

### Conferência do roteiro (lista do fim de `roteiro.md`)

1. Arco com tensão na abertura, cinco movimentos e fecho com pedido: sim.
2. Um S.T.A.R. por bloco: pecas (abertura), a2 (skills), injecao (MCP), etapa2 (scraper), repositorio (GitHub, quieto,
   porque o bloco tem 7 minutos), semana (rotinas).
3. Nenhum trio com o mesmo clima e a mesma faixa; a maior sequência sem respiro tem cinco slides (7 a 11 e 18 a 21).
4. Nenhum par de vizinhos repete o arquétipo; as cenas próprias e os ajudantes não levam `data-arquetipo`.
5. Manchetes de até oito palavras e uns 36 caracteres.
6. Nenhuma parada prevista acima de 45 palavras; os pedidos para copiar (7 e 30) ficam no limite e serão medidos pelo
   oráculo, com o pedido em corpo menor se passar.
7. Mais da metade dos slides tem diagrama, página, tela desenhada ou vídeo como elemento dominante.
8. Cada dado tem fonte abaixo.
9. Gasto previsto somado na coluna mídia; nada acima do teto.

## Pedidos (texto exato da tela e das notas)

**Word (slide 7).** "Use o modelo do escritório anexo (modelo-timbrado.docx). Transforme este rascunho em parecer no
padrão do modelo, com o mesmo cabeçalho, estilos e numeração. No fim, gere o PDF e me diga o que não coube no modelo."

**Scraper, etapa 1 (notas do slide 29).** "Pesquise no TJMS acórdãos de segundo grau sobre [tema votado], julgados nos
últimos três meses. Leia as ementas, baixe só os pertinentes e me dê uma planilha com processo, relator, data e o
motivo de cada escolha."

**Scraper, etapa 2 (slide 30).** "Escreva um script em Python que baixe o arquivo mais recente de espelhos de acórdãos
da Primeira Turma nos Dados Abertos do STJ, filtre as ementas por [tema votado] e grave um CSV. Uma requisição por vez."

**Rotina (notas do slide 40).** "Todo dia útil às 7h10, rode o boletim da etapa 2 para [tema votado] e me mande só os
acórdãos novos desde a última execução, cada um com o link do espelho. Se não houver nenhum, diga isso."

## Atividades (enunciado na tela, gabarito nas notas)

- **A1, auditoria relâmpago (slide 11, 6 min).** A skill de treino (`material/skill-defeituosa/SKILL.md`) tem três
  defeitos: a descrição dispara em qualquer pedido, o script envia o conteúdo da pasta a um endereço externo e o corpo
  manda pular a confirmação do usuário. Gabarito no slide 13.
- **A2, a sala dita (slide 14, 7 min).** Três regras ditas pela sala; o professor pede ao Claude que crie a skill a
  partir delas e roda no mesmo rascunho da demonstração do Word.
- **A3, caça à injeção (slide 19, 4 min).** A petição fictícia (`material/peticao-injecao/`) tem uma ordem em texto
  branco e outra no rodapé em corpo minúsculo. Revelação no slide 20.
- **A4, tomada ou pacote (slide 25, 4 min).** Oito situações e a resposta nas notas: ler meu Gmail (conector); buscar
  na documentação oficial da Microsoft (MCP pelo endereço); o jeito do escritório de fazer parecer (skill); pacote de
  contencioso com skills e conectores (plugin); minha agenda do Google (conector); padrão de citação do gabinete
  (skill); sistema interno do órgão com endereço próprio (MCP); conjunto de ferramentas jurídicas instalado de uma vez
  (plugin).
- **A5, o tema da sala (slides 28 e 32, 2 min mais a conferência).** Temas propostos: execução fiscal, improbidade e
  ICMS, escolhidos porque dão resultado no arquivo de setembro/2026 da Primeira Turma (45, 20 e 18 acórdãos de 471, no
  teste de 05/11/2026; "medicamento" dava zero). Na conferência, a sala abre três espelhos do CSV e confere relator e
  data.
- **A6, agendável ou não (slide 42, 8 min).** A sala propõe tarefas da semana, vota, e o professor cria a rotina da mais
  votada, aplicando a pergunta do slide 41.

## Fontes por slide

Fichas de 05/11/2026: `docs/pesquisa/dia2-ferramentas-aula3.md` (F) e `docs/pesquisa/dia2-scraper-jurisprudencia.md`
(S). Apostila v2 (A): `/Volumes/Projetos/Academic-Writing-System/artigos_livros/direito_ia/ebooks/apostila-v2/content/`.

| slides | afirmação | fonte |
|---|---|---|
| 6, 7 | skill de Word funciona com "Create and edit files" ligado, em todos os planos; acionada por pedido de Word, `.docx` ou papel timbrado; converte em PDF e olha as páginas | F 1.1 (support.claude.com 12512180; github.com/anthropics/skills, `skills/docx/SKILL.md`) |
| 8 | Claude for Word: Pro, Max, Team e Enterprise; herda estilos; alterações controladas; aviso de perda de histórico e skills no Windows após as atualizações de set. e out./2026 | F 1.1 (claude.com/docs/office-agents/word) |
| 9 | skills `docx`, `pdf`, `pptx`, `xlsx` são "source-available, not open source", licença proprietária | F 1.1 e seção 2 (README de anthropics/skills) |
| 10, 11, 13 | os sete pontos antes de instalar | A 16.8, caixa "Os sete pontos antes de instalar" |
| 16, 18 | caminho do conector personalizado; plano gratuito limitado a um; servidor tem de estar na internet pública | F 1.2 (support.claude.com 11175166) |
| 16, 17 | Microsoft Learn MCP: `https://learn.microsoft.com/api/mcp`, sem login, sem custo | F 1.2 (learn.microsoft.com/en-us/training/support/mcp) |
| 20, 21 | casos ARE 1.608.713 (STF), REsp 2.256.731 (STJ, 6ª Turma), AREsp 3.095.458 (STJ, 1ª Turma); Nota Técnica do CNJ de 09/06/2026 | A 17.6, com as referências `stf2026are1608713`, `stj2026panorama`, `stj2026primeiraturma` e `cnj2026notatecnica` da bibliografia da apostila |
| 23, 24 | plugin reúne skills, conectores e subagentes; marketplace Legal; 12 plugins por área; direito dos EUA; saída "a draft for attorney review" | F 1.3 (support.claude.com 13837440; github.com/anthropics/claude-for-legal) |
| 27, 29 | consulta de segundo grau do TJMS responde sem captcha; a skill do TJMS usa o Chrome conectado | S, seção TJMS; skill `consulta-jurisprudencia-tjms` do professor |
| 30, 31, 32 | Dados Abertos do STJ: API sem chave, licença Creative Commons Atribuição, um JSON por mês, sem nome de parte | S, seção STJ e tabela |
| 33, 34 | Res. CNJ 121/2010, art. 5º (busca sem nome das partes); uma requisição por vez; captcha é recusa de acesso automatizado | S, seção de limites jurídicos |
| 35, 36 | definições de README, Download ZIP (sem histórico), issue e pull request | F 1.4 (docs.github.com) |
| 39 | tarefa agendada do Claude roda "even when your computer is asleep or the Claude Desktop app is closed", salvo se precisar de arquivo local | F 1.5 (support.claude.com 13854387) |
| 41 | quadro agendar ou não | A 18.6 |

## Pendências deste briefing

- Materiais gravados na Tarefa 4: `material/escritorio/modelo-timbrado.docx` (Dias & Moura), `material/skill-defeituosa/`,
  `material/peticao-injecao/peticao-injecao.pdf` e `material/scraper/` (campos do STJ usados: `siglaClasse`,
  `numeroProcesso`, `ministroRelator`, `nomeOrgaoJulgador`, `dataDecisao`, `ementa`). Falta o rascunho em Markdown da
  demonstração do Word: é texto jurídico fictício e precisa do aval do professor.
- Endereço do kit (slide 44): depende do sim do professor para criar o repositório público.
- As três linhas do slide 32 saem da amostra baixada na Tarefa 4.
- Notas `{diga, faca, transicao}` de cada slide: escritas na montagem dos blocos, só com os fatos acima.

</ALVO>
