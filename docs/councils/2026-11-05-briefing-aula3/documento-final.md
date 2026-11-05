# Documento final do conselho: briefing e roteiro da Aula 3 (versão 1)

Data: 2026-11-05. Alvo: `decks/curso-ia-aula3/briefing.md`, versão 1.

## 1. Status

Revisores ativos: A e B (2). Ausentes: nenhum. Rodadas executadas: 2. Na rodada 2, cada letra respondeu às sugestões da rodada 1 da outra (A citou B1 a B12; B citou A1 a A15), de modo que nenhuma sugestão da última rodada ficou sem debate e nenhuma leva a marca `[não debatido]`.

## 2. Consensos

As duas letras convergiram nos pontos abaixo, quase sempre com texto equivalente na rodada 2.

- A aula não cabe em 90 minutos como está; os primeiros cortes são a demonstração ao vivo do plugin (24) e a do GitHub (37).
- A rotina do slide 40 promete o que a própria fonte ressalva: a tarefa agendada roda com o computador desligado, salvo se precisar de arquivo local, e o script e o CSV da etapa 2 são locais.
- O tema votado foi testado só no arquivo de setembro/2026, mas o pedido busca o arquivo mais recente; a conferência do slide 32 precisa de uma amostra por tema.
- "A sala abre três espelhos" contradiz a atividade sem computador do aluno; quem projeta é o professor.
- A4 não pode tratar "conector" e "MCP" como respostas exclusivas; as categorias passam a "conector pronto", "conector próprio (MCP)", "skill" e "plugin".
- A3 tem duas ordens escondidas no material e o slide pede uma; o enunciado e a revelação precisam cobrir as duas.
- A1 pede leitura demais para o projetor; bastam os três trechos com defeito, ampliados.
- A6 precisa de classificação prévia com tarefas prontas, poucas sugestões orais e uma rotina escolhida entre opções seguras.
- Os casos do slide 21 e a Nota Técnica do CNJ exigem leitura da fonte primária antes de ir à tela.
- O aviso de Windows (slide 8) e o número "12 plugins" (slide 23) saem da tela para as notas.
- O slide 34 troca a manchete por "Encontrou captcha? Pare a automação."
- Toda demonstração participativa precisa de um limite de tempo e de uma saída para a reserva gravada; o TJMS (29) é a de maior risco.
- O S.T.A.R. deve estar marcado na tabela para todos os blocos, e o de rotinas sai do calendário (39) para a pergunta do slide 41.

## 3. Divergências

**Slide 8, Claude for Word.** A sustenta que o desenho aprovado promete uma demonstração do add-in e que o roteiro a apagou sem registro, por isso pede que o professor decida entre demonstrar ou retirar a promessa. B quer manter só os cartões, sem demonstração, para ganhar quatro minutos. A divergência é de procedimento, e A tem razão nele: o desenho é decisão do professor e não se altera em silêncio. O mérito fica com B, porque o tempo é o problema mais grave da aula.

**Margem de tempo.** B propõe, além dos cortes de 24 e 37, tirar dois minutos de A1 e dois de A6. A aceita cortar 24 e 37 e cronometrar o resto no ensaio, sem fixar novos tempos, e contesta a estimativa de B de 25 minutos de estouro por falta de conta. A1 encolhe com a leitura reduzida; A6 ganha uma etapa de classificação e por isso não tem como perder minutos.

**A3, legibilidade.** B (rodada 1) queria uma única injeção visível ou a seleção animada automaticamente após 90 segundos; na rodada 2, aderiu à versão de duas ordens. A propõe uma ampliação legível do trecho da petição, sem destacar a ordem. A dificuldade que nenhuma das duas resolve por inteiro é que texto branco projetado não se acha a olho, por definição.

**A4, tamanho.** B (rodada 1) queria reduzir a quatro situações e três categorias, fundindo conector e MCP. A defende manter as oito situações, telegráficas. Oito situações, contadas como estão no briefing, somam 47 palavras antes da manchete e das categorias, acima do teto duro de 45; quatro situações com quatro categorias viram exercício de eliminação.

**Slide 32, dados na tela.** A (rodada 2) aceita que as duplas confiram relator e data na projeção. A (rodada 1) e B (rodada 2) querem recortes sem nomes; B vai além e pede número de processo fictício. Número fictício esvazia a conferência, que existe para mostrar que cada linha volta ao acórdão real.

**Slide 33, referência normativa.** B (rodada 1) quer citar o art. 5º da Res. CNJ 121/2010 no cartão, explicar nas notas a diferença entre os arts. 4º e 5º e trazer a LGPD (art. 6º, I e III). B (rodada 2) aceita "padrão da Res. CNJ 121/2010, art. 5º" na tela. A quer na tela só a regra operacional, com a norma nas notas até a leitura do texto primário, e recusa a LGPD por falta de fonte lida.

**Slide 36, vocabulário do GitHub.** B (rodada 1) quer trocar pull request por "Histórico" e redefinir issue como "mural de avisos". A recusa, porque o desenho promete explicar pull request e o slide já traduz os quatro termos. B (rodada 2) e A (rodada 1) convergem em fundir 35 e 36.

**S.T.A.R. do bloco MCP.** B (rodada 2) quer passá-lo da injeção (20) para a demonstração do conector (17), por ser o momento da "tomada". A (rodada 1) sugeria só que o resultado do MCP citasse a página oficial como virada. A injeção é o que a sala vai lembrar e é a competência prometida no briefing ("reconhecer um documento que dá ordens"), por isso o S.T.A.R. fica onde está.

## 4. Lista final, por severidade

### Críticas

1. **Rotina dos slides 39 e 40** (A1-5 e A2-3; B1-3 e B2-5). ACEITAR, com adaptação. A legenda do slide 39 passa a "Na nuvem, roda com o computador desligado, se não depender de arquivo local." O pedido do slide 40 não pode depender do script local nem de memória "desde a última execução" sem que o ensaio prove as duas coisas. Há ainda um descompasso que o próprio briefing revela: os espelhos do STJ saem em um JSON por mês, de modo que um boletim "todo dia útil às 7h10" tende a voltar vazio quase sempre. Proposta: a rotina consulta diretamente a página pública dos Dados Abertos do STJ (sem o script local), roda uma vez por semana ou quando sai o arquivo do mês, e lista "os acórdãos do arquivo mais recente sobre [tema]", sem estado entre execuções. Se o ensaio com o computador desligado falhar, o slide 40 vira demonstração gravada e a legenda deixa de prometer execução autônoma.

2. **Slide 21, casos e Nota Técnica** (A1-11; B2-11). ACEITAR. Ler na fonte primária ARE 1.608.713, REsp 2.256.731, AREsp 3.095.458 e a Nota Técnica do CNJ de 09/06/2026 antes de montar o slide, anotando no briefing o endereço e o trecho que comprovam a forma de ocultação. O cartão que não for confirmado sai da tela, como manda a regra de fonte lida; a remissão à apostila não basta para número de processo diante de uma desembargadora.

3. **Tempo da aula** (A1-1 e A2-1; B1-1 e B2-1). ADAPTAR. A demonstração do plugin (24) vira cena estática desenhada por código com o aviso do plugin e a lista do que ele traz, com a gravação do ensaio de reserva; a do GitHub (37) sai, e o bloco fica com um slide (item 15). A1 passa a 4 minutos com a leitura reduzida (item 10); A6 mantém 8 minutos porque ganha a classificação prévia (item 11). Nada disso substitui o ensaio cronometrado de ponta a ponta, com teto anotado nas notas de cada demonstração.

4. **Tema votado e arquivo do STJ** (A1-4 e A2-8; B1-8 e B2-4). ACEITAR. O pedido do slide 30 fixa o arquivo testado ("espelhos de acórdãos de setembro de 2026 da Primeira Turma"), e na véspera da aula os três temas são rodados no arquivo mais recente; se algum vier vazio, sai da votação. O slide 32 tem três conjuntos de linhas e recortes (`amostra/execucao`, `amostra/improbidade`, `amostra/icms`), trocados pelo professor com as teclas 1, 2 e 3; tema sem conjunto pronto não vai à votação.

5. **Slide 32 e A5, conferência e dados pessoais** (A1-9 e A2-6; B1-6 e B2-9). ADAPTAR. Texto da atividade: "O professor projeta três linhas do CSV e o recorte de cada espelho; as duplas conferem número, órgão, data e trecho da ementa." Os recortes são desenhados por código a partir do JSON (que não traz nome de parte) e sem o nome do relator; o número do processo é o real, porque um número fictício anula a conferência. A mesma regra alcança a demonstração ao vivo da etapa 1, cujo pedido pede "relator" na planilha: tirar esse campo do pedido ou pedir ao professor que diga se o nome de julgador conta como dado pessoal para a regra da tela.

6. **Slides 33 e 34, norma e captcha** (A1-13 e A2-10; B1-10 e B2-13). ADAPTAR. Manchete do slide 34: "Encontrou captcha? Pare a automação." No cartão do slide 33, a tela traz só a regra operacional, "Pesquise por tema, nunca por pessoa"; a referência ao art. 5º da Res. CNJ 121/2010 fica nas notas até que o texto primário seja lido e anotado. Confirmado o texto, a tela pode levar "padrão da Res. CNJ 121/2010, art. 5º", formulação que não apresenta como proibição ao usuário uma regra que pode ser dirigida aos tribunais.

7. **A4, categorias e tamanho** (A1-8 e A2-5; B1-5 e B2-8). ADAPTAR. Quatro categorias com os mesmos nomes no slide 16, no slide 25 e nas notas: "skill", "conector pronto", "conector próprio (MCP)" e "plugin", explicadas em uma frase antes do cronômetro. As situações caem de oito para seis, de até cinco palavras cada, para caber em 45 palavras, eliminando as duplicatas (Gmail e agenda; pacote e conjunto). Sugestão, com 26 palavras: "Ler meu Gmail", "Documentação oficial da Microsoft", "Modelo de parecer do escritório", "Sistema interno com endereço próprio", "Pacote de contencioso pronto", "Padrão de citação do gabinete". Medir com o oráculo.

### Importantes

8. **Saída para a reserva nas demonstrações participativas** (A1-3 e A2-9; B1-9 e B2-3). ACEITAR. Nas notas `faca` dos slides 6, 14, 29, 31, 40 e 42: uma tentativa ao vivo; sem resultado útil em 60 segundos (40 no TJMS), o professor para, exibe a gravação do ensaio e a sala avalia o resultado preparado. Entradas fictícias e resultados offline ficam prontos para cada etapa, e a página salva do TJMS é apresentada como gravação do ensaio, nunca como coleta ao vivo.

9. **A3, as duas ordens** (A1-7 e A2-4; B1-4 e B2-7). ADAPTAR. O slide 19 mostra a petição com o rodapé ampliado até ficar legível, sem destaque, e o enunciado "Em dupla, achem a ordem dirigida à IA. Quantas há?". O slide 20 revela primeiro a do rodapé e, depois, pela seleção, a de texto branco, que ninguém podia ver; essa segunda revelação é a lição do bloco (o que o olho não vê, o agente lê). A animação automática após 90 segundos fica dispensada.

10. **A1, leitura reduzida** (A1-6; B2-6). ADAPTAR. O slide 11 mostra só os três trechos da skill de treino (descrição, linha do script, instrução de confirmação), ampliados e numerados, com os sete pontos como coluna lateral de referência. O slide 12 não sai, porque eliminá-lo deixa os slides 7 a 14 sem respiro, contra o teto duro de cinco; ele vira o momento da votação ("Quem achou os três?"), em até 12 palavras, e o gabarito vem no clique seguinte.

11. **A6, classificação antes da criação** (A1-10 e A2-7; B1-7 e B2-10). ACEITAR. Três tarefas fictícias na tela para a sala classificar em agendar, agendar com conferência e não automatizar (cerca de 2 minutos, gabarito nas notas); depois, no máximo duas sugestões orais, e o professor cria a rotina de uma delas só se couber na categoria segura. Se nenhuma couber, cria a do boletim já preparado.

12. **Slides 8, 16, 18 e 23, detalhes que envelhecem** (A1-2, A1-12 e A2-2; B1-2, B2-2 e B2-12). ADAPTAR. O aviso de histórico e skills perdidos no Windows e o número "12 plugins" vão para as notas `diga`; planos, menus e o limite do plano gratuito são revalidados na conta do ensaio, com nota de contingência se divergirem. Quanto ao Claude for Word, o roteiro não pode apagar em silêncio a demonstração que o desenho aprovou: a recomendação é retirá-la para ganhar tempo, registrando a mudança no briefing, mas a decisão é do professor.

13. **Pedidos para copiar nos slides 7 e 30** (A1-14; B2-14). ADAPTAR. Nenhum dos dois cai para corpo menor. O slide 30 mostra uma versão de até 30 palavras sem siglas ("planilha" no lugar de CSV, sem "Python" e "JSON"), e o texto literal fica nas notas e no kit. O slide 7 é medido pelo oráculo e, se passar de 45 palavras, segue a mesma regra.

14. **S.T.A.R. marcado em todos os blocos** (B1-12; A2-12). ACEITAR. Marcar `**S.T.A.R. do bloco.**` na tabela nos slides 3, 14, 20, 31, 35 e 41, e passar o de rotinas do slide 39 para o 41, cuja pergunta "Se falhar em silêncio, o que se perde?" é a que a sala leva. Atualizar o item 2 da conferência do roteiro.

### Opcionais

15. **GitHub em um slide** (A1-15; B2-15). ADAPTAR. Com o slide 37 fora (item 3), os slides 35 e 36 viram uma só cena própria: a página do repositório desenhada por código, com os quatro termos (README, Download ZIP, issue, pull request) apontados um por clique sobre ela, com as definições atuais. Pull request fica, porque o desenho promete explicá-lo.

## 5. Rejeitadas

- B1-11 (trocar pull request por "Histórico" e issue por "mural de avisos"): quebra a promessa do desenho e define issue com menos exatidão.
- B1-10, parte da LGPD (art. 6º, I e III, no cartão ou nas notas): não há fonte lida no briefing, o que viola a regra de fonte.
- B2-15, parte do S.T.A.R. (passar da injeção, slide 20, para o slide 17): a injeção é o momento que a sala lembra e a competência prometida.
- A1-15, parte do fecho ("Jeito. Tomada. Agenda. Fonte."): o slide 45 já entrega a frase com "Confira a fonte."; a troca não acrescenta.
- B2-9, parte do número fictício no slide 32: anula a conferência contra a fonte.
- B2-6, parte da eliminação do slide 12: viola o teto de cinco slides sem respiro (adaptada no item 10).
- B2-1, parte do corte de dois minutos em A6: a atividade ganhou uma etapa e não comporta menos tempo.
- B1-1, parte de transformar a criação de A6 em tela estática: a criação ao vivo é a atividade; o item 11 a protege com opções seguras.
- B1-4, parte da seleção animada após 90 segundos: o item 9 resolve com o rodapé legível e a revelação em dois tempos.
- B1-5, parte de três categorias com conector e MCP fundidos: a rodada 2 das duas letras convergiu em quatro categorias.
- A1-2, parte do argumento de que o Claude for Word viola "demonstração só no Claude": o add-in é o próprio Claude dentro do Word; o problema do slide 8 é tempo e promessa do desenho.

## 6. Custo

Copiado de `_custo.json` (gerado em 2026-11-05 08:47:47).

| letra | rodada | tokens de entrada | tokens de saída |
|---|---|---|---|
| a | 1 | 10201 | 2622 |
| b | 1 | 10661 | 2070 |
| a | 2 | 12168 | 1319 |
| b | 2 | 12273 | 1952 |

Total: 45303 tokens de entrada e 7963 de saída.
