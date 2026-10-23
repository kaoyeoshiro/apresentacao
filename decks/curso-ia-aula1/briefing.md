# Briefing: curso de IA da co.juris, dia 1, Aula 1. O que é IA e qual usar (versão 3)

Primeira de duas aulas de cerca de 90 minutos, dadas na mesma tarde; a segunda está em `decks/curso-ia-aula2`. A
versão 2 (23 slides) foi reprovada no ensaio por explicar pouco. Esta versão segue o roteiro 3 aprovado pelo usuário,
`docs/councils/2026-10-22-aula1-v3/_alvo.md`, com os 19 itens da "Lista final" de
`docs/councils/2026-10-22-aula1-v3/documento-final.md` aplicados, e as decisões do usuário de 22/10/2026 sobre capa,
placar, corrida EUA e China, grades de modelos, números e respiro. Os fatos estão em `apuracao.md` (anexo deste
briefing) e o parecer fictício medido, em `apuracao-parecer-ficticio.md`.

- Curso pago, o primeiro do professor. Turma mista: advogados, uma desembargadora, servidores e assessores, muitos
  sem plano pago de IA. Exemplos neutros, que servem a escritório, gabinete e órgão público.
- Curso agnóstico: Claude e ChatGPT lado a lado, sem vender marca.
- Mensagem em uma frase: a IA escreve bem por previsão, não por consulta, e por isso cada um escolhe a ferramenta pela
  tarefa e confere na fonte. A capa pergunta "Você confere como?" e o fecho responde.
- Cinco práticas com celular ou mão levantada, cada uma com onde, passos, tempo e o que dizer em voz alta.
- Tema `cojuris`, plano contínuo, um clique por slide, mesma trilha dourada e acabamento da prévia
  (`decks/previa-curso-ia`).
- S.T.A.R. da aula: o placar da prova discursiva da PGE-MS (slide 45). Cada bloco tem o seu momento, e só um: a
  classificação da sala (bloco 1, slide 9), a palavra que se parte em tokens (bloco 2, slide 17), a busca do acórdão
  (bloco 3, slide 31), o placar (bloco 4) e a corrida EUA e China (bloco 5, semente curta para o fim do curso).

## Mapa

| min | bloco | slides | práticas |
|---|---|---|---|
| 3 | Abertura: capa e roteiro | 1 e 2 | |
| 15 | O que é IA | 3 a 12 | 1, classificar seis sistemas (3 min) |
| 25 | Como funciona por dentro | 13 a 28 | 2, contar tokens (4 min); 3, o mesmo pedido três vezes (3 min) |
| 15 | Onde brilha e onde tropeça | 29 a 35 | 4, conferir o acórdão (6 min) |
| 20 | Qual é a melhor IA | 36 a 46 | 5, a sala vota às cegas (3 min) |
| 12 | Fechados e abertos | 47 a 52 | |

Os tempos dos blocos 4 e 5 seguem o item 16 da Lista final (20 e 12 minutos). Os 2 minutos a mais da prática 2 saem
da fala do próprio bloco 2.

## Slides

Densidade pela parada final, nas faixas do oráculo: respiro (até 12 palavras ou texto de 200 px), leve (13 a 24),
médio (25 a 45). Nenhuma imagem nova foi gerada; custo de mídia desta versão, US$ 0.

| # | slide | manchete | o que a tela prova | clima e densidade | arquétipo | mídia e custo |
|---|---|---|---|---|---|---|
| 1 | capa | O que é IA e qual usar | título, subtítulo "A IA escreve bem. Você confere como?" e a frase "O juiz julgou o pedido procedente" escrita palavra por palavra, com as candidatas em leque antes de cada escolha | noite, médio | escolha | código, valores ilustrativos (pílula) |
| 2 | mapa | Entender a IA vem antes de escolher | quatro paradas, "conceito" (o começo) em dourado; dados de 22/10/2026 | claro, leve | tempo | código |
| 3 | definicao | IA imita capacidades humanas | "Sistema que recebe dados, acha padrões e gera previsões ou conteúdo"; entrada (foto da placa) e saída (texto da placa) | claro, médio | comparacao | código |
| 4 | lei | A OCDE define; o PL propõe | fios da OCDE (tradução livre) e do PL 2338/2023 às definições curtas; o PL é projeto, aprovado no Senado em 10/12/2024 | claro, médio | fios | código |
| 5 | cotidiano | Você já usa IA todo dia | frase grande; Waze, Netflix, spam, rosto, teclado | noite, respiro | respiro | nenhuma |
| 6 | regras | Regras escritas ou padrões aprendidos | IA simbólica contra aprendizado de máquina, um exemplo de spam em cada lado (item 6) | claro, médio | comparacao | código |
| 7 | llms | LLMs nascem dos transformers | a trilha se divide: simbólica; máquina, profundo, transformers (2017), LLMs; 2022 é o lançamento do ChatGPT | claro, médio | ramos | código; [CONFERIR] 2022 |
| 8 | tipos | Específica faz uma; generalista, várias | frase grande; "Uso geral, não IA geral (AGI)" (item 3) | claro, respiro | respiro | nenhuma |
| 9 | pratica1 | Você classifica seis sistemas | os seis sistemas numerados, a regra dos dedos e o voluntário (item 11) | noite, médio | objetos | código |
| 10 | gabarito | Quatro específicas, duas generalistas | quatro estações no ramo da específica, duas no da generalista; vale o sistema descrito | claro, médio | ramos | código |
| 11 | generativa | A generativa cria, não só classifica | quatro cartões: texto, imagem, áudio, código, com exemplo jurídico neutro | claro, médio | cena própria (cartões) | código; exemplos ilustrativos (pílula) |
| 12 | previsao | Parece criatividade; é previsão | frase grande | claro, respiro | respiro | nenhuma |
| 13 | funciona | Como funciona por dentro | abertura do bloco 2, sem foto | noite, respiro | abertura | nenhuma |
| 14 | corpus | Ela treinou com trilhões de pedaços | "15 trilhões" de tokens, Llama 3.1 405B, Meta, 2024 | claro, leve | numero | código |
| 15 | parametros | O treino ajusta os parâmetros | "Parâmetros são números ajustados no treino, não textos salvos"; treino contra uso; 405 bilhões de parâmetros (item 2) | claro, médio | comparacao | código |
| 16 | calcula | Sem busca, ela calcula; não consulta | frase grande (item 2) | noite, respiro | respiro | nenhuma |
| 17 | tokens | Ela lê pedaços, não palavras | "inconstitucionalidade" se parte em in, constit, ucional, idade (4); "O réu agravou da decisão." em 8 blocos; tokenizador nomeado | claro, médio | cena própria (tokens) | código |
| 18 | parecer | Parecer de 3 páginas: 2.056 tokens | 2.056 grande; 1.486 palavras, 1,38 token por palavra; medido em 22/10/2026 | claro, respiro (320 px) | numero | código |
| 19 | pratica2 | Palavras viram blocos na tela | a frase do slide 17 no pedido, duas rotas (com e sem internet), QR do tokenizador (item 7) | noite, médio | objetos | QR por código |
| 20 | previsto | A IA prevê um token por vez | dois ciclos de leque: "A sentença foi publicada ontem"; probabilidades inventadas para explicar (item 13) | claro, médio | escolha | código |
| 21 | pratica3 | O mesmo pedido pode variar | o pedido, Claude ou ChatGPT, nova conversa, anotar igual ou diferente, rota sem botão (item 12) | noite, médio | objetos | código |
| 22 | sorteio | Cada resposta é um sorteio com pesos | à esquerda o que vimos no app; à direita o leque raso e o sorteio de "improcedente", que não era a mais provável | claro, médio | escolha com `data-sorteio` | código; mecanismo ilustrado (pílula) |
| 23 | mesa | A janela de contexto é a mesa | dois papéis voam para a árvore: instrução, conversa, anexo e espaço da resposta | claro, leve | viagem | `mesa.webp` (já gerada), US$ 0 nesta versão |
| 24 | tamanho | A mesa tem tamanho | "1 milhão" de tokens: mais de mil páginas (Claude Opus 5.5) | claro, respiro (230 px) | numero | código; [CONFERIR] no app |
| 25 | limite | Passou do limite, algo fica de fora | cabe contra não cabe: partes cortadas ou resumidas (item 4) | claro, médio | comparacao | código; [CONFERIR] varia por produto |
| 26 | meio | No meio, o dado pode se perder | o mesmo dado no início, no meio e no fim do anexo; achado de Liu et al., 2023 (item 4, slide 24B) | claro, médio | objetos | recortes da prévia, US$ 0; exemplo ilustrativo (pílula) |
| 27 | conversa | Conversa nova, mesa limpa | frase grande; salvo memória ligada | noite, respiro | respiro | nenhuma |
| 28 | passos | Do corpus à resposta, em cinco passos | cinco marcos; "previsão gera a resposta" em dourado | claro, médio | tempo | código |
| 29 | linguagem | Ela vai bem em linguagem | resumir, rascunhar, traduzir, explicar, classificar, em letra grande | claro, respiro | respiro | nenhuma |
| 30 | avianca | Ela inventa com a mesma confiança | fios da ordem de sanção (Mata v. Avianca, 22/06/2023) a três fatos; os nomes inventados ficam sem fonte | claro, médio | fios | código |
| 31 | pratica4 | Você confere se o acórdão existe | pedido literal, três passos, QR do STJ (item 1) | noite, médio | objetos | QR por código |
| 32 | conferiram | Os números conferiram? | frase grande; "não encontrei", "tema diferente", "confere" (item 8) | noite, respiro | respiro | nenhuma |
| 33 | fronteira | A fronteira da IA é irregular | ajuda contra fonte externa; conferência humana nos dois lados (Dell'Acqua et al., 2023) | claro, médio | comparacao | código |
| 34 | responde | Quem usa responde pelo que entrega | dar contexto, supervisionar, validar (dourado), corrigir | claro, leve | tempo | código |
| 35 | pior | Hoje é a pior IA que você usará | frase grande, provocação | claro, respiro | respiro | nenhuma |
| 36 | melhor | Qual é a melhor IA? | abertura do bloco 4; "Melhor para quê?" | noite, respiro | abertura | nenhuma |
| 37 | benchmark | Benchmark é o ENEM da IA | a caneta corrige dez itens, 8 de 10 | claro, leve | numero | código; ilustrativo (pílula) |
| 38 | medidas | Seis coisas que os benchmarks medem | seis cartões | claro, médio | cena própria (cartões) | código |
| 39 | legal | Existe prova só para o jurídico | seis barras com nome e peso; 35% em dourado (item 15) | claro, médio | cena própria (pesos) | código |
| 40 | processo | Prova não é processo | frase grande; "No caso real, nada vem limpo." | noite, respiro | respiro | nenhuma |
| 41 | arena | Na arena, pessoas votam às cegas | pergunta, duas respostas sem nome, voto, nomes | claro, médio | tempo | código |
| 42 | pratica5 | A sala vota sem ver o nome | A e B sem nome, "Qual parece mais pronta?", 1 ou 2 dedos, QR da arena (item 9) | noite, médio | comparacao | QR por código; [CONFERIR] respostas do professor |
| 43 | mede | Benchmark mede prova; arena, preferência | frase grande | noite, respiro | respiro | nenhuma |
| 44 | prova | Demos a prova da PGE às IAs | 180 grande; 12 dissertativas de 10, parecer de 30, peça de 30; correção por dois modelos Gemma 4 com gabarito e espelho | claro, respiro (320 px) | numero | código |
| 45 | placar | Nesta prova, o topo ficou próximo | dez barras com nome e nota; colchete dourado sobre os dois primeiros; selo "1 prova (PGE-MS 2021), correção por IA, não é ranking geral" (S.T.A.R.) | noite, mais de 45 | cena própria (placar) | código |
| 46 | limites | O que essa nota não diz | prova contra correção | claro, médio | comparacao | código |
| 47 | aberto | Fechado ou aberto? | abertura do bloco 5 | noite, respiro | abertura | nenhuma |
| 48 | pesos | Aberto é ter os pesos | fechado: só pelo serviço; aberto: baixado e rodado em servidor próprio, conforme licença, configuração e controles do órgão (item 19) | noite, médio | comparacao | código |
| 49 | fechados | Os principais modelos fechados | seis cartões com logo oficial, empresa, família e produto | claro, médio | cena própria (cartões) | logos de `midia/logos`, US$ 0; [CONFERIR] versões nos apps |
| 50 | abertos | Os principais modelos abertos | oito cartões com logo, família e empresa | claro, médio | cena própria (cartões) | logos, US$ 0; [CONFERIR] família Mistral |
| 51 | corrida | Na ponta, EUA e China disputam | EUA contra China, com as empresas das duas grades; na Europa, a Mistral | noite, médio | comparacao | código |
| 52 | fecho | Escolha por tarefa e teste você | teste com seu material, use mais de uma IA, confira na fonte; Aula 2: como pedir bem | noite, leve | fecho | nenhuma |

### O que mudou em relação ao roteiro 3 e por quê

O roteiro tem 49 linhas; com 6A e 6B (slides 6 e 7), 24 e 24B (25 e 26) e a corrida EUA e China (51), o deck fica com
52 slides. Os arquétipos que mudaram:

- Capa (1): sem foto, por decisão do usuário. É o arquétipo escolha na zona noite, com a manchete em 110 px; nenhuma
  cena própria precisou ser escrita. São duas rodadas de leque, o máximo da biblioteca. A foto `heroi-aula1.webp`
  saiu do deck e do `midia/creditos.json`.
- Definição (3): o roteiro pedia respiro, mas a definição completa e o exemplo da placa passam de 12 palavras e não
  cabem em letra de respiro; virou comparação entrada e saída, com a definição logo abaixo da manchete.
- Cotidiano (5) e específica e generalista (8): objetos e comparação no roteiro, viraram respiros. O objetos pede
  recortes fotográficos que não existem e não seriam gerados nesta versão; e, com os slides 6A e 6B, os slides 1 a 11
  ficariam com sete seguidos sem respiro. Os cinco itens do cotidiano ficam numa linha embaixo; os exemplos de
  específica (placa) e generalista (texto, código, imagem) passam para a fala.
- Generativa (11), medidas (38), fechados (49) e abertos (50): cena própria de cartões, escrita uma vez no deck e usada
  quatro vezes. Nenhum arquétipo mostra quatro a oito itens sem ordem; o tempo sugeriria sequência e o ramos aceita
  no máximo três estações por ramo. As duas grades de modelos ficam vizinhas, como pede o roteiro, mas com desenhos
  diferentes: fechados em três colunas, com logo ao lado do nome da empresa e o produto embaixo; abertos em quatro
  colunas, com logo em cima e a família em destaque.
- Tokens (17), Legal Index (39) e placar (45): cenas próprias. A palavra que se parte em blocos é o S.T.A.R. do bloco
  2; as seis barras de peso não cabem no leque do escolha, que pede uma frase e até quatro candidatas; o placar já era
  cena própria na versão 2.
- Linguagem (29): objetos no roteiro, virou respiro com manchete, pelo mesmo motivo do cotidiano.
- Arena (41): comparação no roteiro, virou tempo (os quatro passos da votação), porque a prática 5 (42) é uma
  comparação A e B e as duas seriam vizinhas com o mesmo arquétipo.
- Conferiram (32): respiro; as três categorias do item 8 cabem como três etiquetas curtas, as mesmas palavras do
  passo 3 da prática 4.
- Práticas 1 a 4: arquétipo objetos, em que o pedido se digita na caixa (é o que a sala vai digitar ou fazer) e os
  passos ficam à direita. Para caber em 45 palavras, os protocolos da Lista final foram condensados na tela; a versão
  inteira está nas notas do apresentador.
- Previsto (20): o roteiro pedia três ciclos; a biblioteca faz no máximo duas rodadas de leque. O terceiro ciclo fica
  na fala.

### Respiro (decisão 6 do usuário)

A regra é nunca mais de cinco slides seguidos sem respiro (parada de até 12 palavras ou texto de 200 px). Com 6A e 6B
o roteiro tinha sete seguidos (4 a 10). A correção foi dupla: o cotidiano (5) e a específica e generalista (8) viraram
respiros. O deck fica assim: as maiores sequências sem respiro são 19 a 23 (prática 2, previsto, prática 3, sorteio,
mesa) e 48 a 52 (pesos, fechados, abertos, corrida, fecho), ambas com cinco, no limite. Contam como respiro também os
números de 230 e 320 px (14, 18, 24, 44) e as aberturas. O `./ap sondar` não avisa sequência nem respiro.

### Partitura de luz

Noite: capa, respiros (salvo 8, 12, 29 e 35, que ficam no claro), aberturas, as cinco práticas, o placar, os pesos (48), a corrida (51) e o fecho. Os pesos foram
para a noite porque, no claro, pesos, fechados e abertos seriam três claros médios seguidos; a zona noite da abertura
47 continua neles. A corrida fica na noite pelo mesmo motivo e por ser a semente que fecha o bloco.

## Fala, por bloco

- Abertura. A frase da capa se escreve sozinha: cada palavra saiu de candidatas com peso, e é isso que a aula vai
  abrir por dentro. A pergunta do subtítulo ("Você confere como?") só é respondida no fecho. O roteiro tem quatro
  paradas; os dados de mercado foram verificados em 22/10/2026.
- O que é IA. As capacidades humanas que a IA imita (reconhecer imagens, entender e gerar texto, prever, criar) ficam
  na fala; a tela dá a definição simples e o exemplo da placa. OCDE e PL dizem a mesma coisa com o verbo "inferir"; o
  PL ainda é projeto. A IA simbólica (regras escritas) é a de antes; o aprendizado de máquina tira padrões dos dados,
  e dele vêm o aprendizado profundo, os transformers (Vaswani et al., 2017) e os LLMs, modelos de linguagem grandes.
  "Generalista" é modelo de uso geral, não IA geral (AGI). Prática 1 e gabarito: o que conta é o sistema descrito.
  A generativa produz conteúdo novo, e o que parece criatividade é previsão.
- Como funciona. Treino com trilhões de tokens (Llama 3.1, cerca de 15 trilhões); o treino ajusta números, os
  parâmetros, e o texto não fica guardado. Sem busca, ela calcula; com a busca ligada, o app consulta e entrega.
  Tokens medidos no tokenizador da OpenAI; cada fabricante tem o seu, por isso a prática 2 não promete os mesmos
  blocos em outra ferramenta. A previsão é um token por vez e cada resposta é um sorteio com pesos: repetir a mesma
  saída é peso alto, não falha. A mesa tem tamanho (1 milhão de tokens na API do Claude Opus 5.5; no app, depende do
  plano), o excesso é cortado ou resumido conforme o produto, e o meio de um anexo longo pesa menos (Liu et al.,
  2023, modelos de 2023, não é lei geral). Conversa nova, mesa limpa, salvo memória ligada.
- Onde brilha e tropeça. Linguagem é o forte. Mata v. Avianca: seis decisões inventadas pelo ChatGPT e a multa de
  US$ 5.000 vieram também de os advogados terem sustentado as citações depois de questionados. Na prática 4, o
  critério é conferir número e tema, com ou sem busca ligada. Depois, um relato real de cada categoria que tiver
  aparecido; conferir continua sendo a regra. A fronteira irregular é de Dell'Acqua et al. (758 consultores do BCG);
  a expressão é dos autores. "Hoje é a pior IA que você usará" entra como provocação e transição, não como clímax.
- Qual é a melhor IA. Benchmark é prova padronizada, controlada, repetível e comparável, e prova não é veredito. O
  Legal Index pondera as capacidades pela frequência em tarefas jurídicas reais; as provas são, na maior parte, em
  inglês e de direito estrangeiro. Arena mede preferência: depois da prática 5, perguntar se a sala votou por
  precisão, clareza ou aparência de segurança, e que afirmação exigiria fonte. A prova da PGE-MS é teste do
  professor, não da PGE-MS; o placar mostra o topo próximo (0,8 ponto entre os dois primeiros), sem "empate técnico".
- Fechados e abertos. Aberto é ter os pesos, e isso não garante sigilo sozinho: depende de licença, configuração e
  controles do órgão. Nas grades, "aberto" é peso disponível, não necessariamente licença de código aberto. A ponta
  fechada é americana; entre os abertos fortes há americanos e chineses; na Europa, a Mistral. O tema volta no fim do
  curso (encerramento do dia 2). Fecho: escolher por tarefa, testar com o próprio material, usar mais de uma IA e
  conferir na fonte; na Aula 2, como pedir bem.

## Fontes

Todas lidas em 22/10/2026; o detalhe, com o trecho lido e a ressalva de cada uma, está em `apuracao.md`.

| slide | dado na tela | fonte |
|---|---|---|
| 4 | definição da OCDE, tradução livre | OCDE, OECD/LEGAL/0449, PDF oficial (apuração, item 1) |
| 4 | PL 2338/2023 aprovado no Senado em 10/12/2024, aguardando parecer na Câmara; não é lei | ficha da Câmara (id 2487262) e matéria 157233 do Senado (item 2) |
| 7 | transformers, 2017 | Vaswani et al., "Attention Is All You Need", arXiv:1706.03762, v1 de 12/06/2017, lido nesta sessão |
| 7 | 2022, lançamento do ChatGPT | não lido: openai.com recusou o acesso automático; `[CONFERIR]` na tela |
| 14, 15 | Llama 3.1 405B: cerca de 15 trilhões de tokens; 405 bilhões de parâmetros | model card do Llama 3.1, Meta (item 3) |
| 17 | in, constit, ucional, idade (4); "O réu agravou da decisão." em 8 tokens | `tiktoken` 0.14.0, `o200k_base`, conferido no tokenizador web (item 5) |
| 18 | 2.056 tokens, 1.486 palavras, 1,38 por palavra | parecer fictício medido (item 5c; `apuracao-parecer-ficticio.md`) |
| 19 | QR: https://platform.openai.com/tokenizer | item 5 |
| 24 | 1 milhão de tokens; mais de mil páginas | Anthropic, Models overview (item 4); conta do item 5d |
| 26 | começo e fim melhores que o meio | Liu et al., arXiv:2307.03172 (item 7) |
| 30 | Mata v. Avianca, 22-cv-1461, ordem de 22/06/2023, multa de US$ 5.000, nomes inventados | Opinion and Order on Sanctions, S.D.N.Y., Document 54 (item 6) |
| 31 | QR: https://processo.stj.jus.br/SCON/ | item 12 |
| 33 | Dell'Acqua et al., 2023; 758 consultores (na fala) | HBS Working Paper 24-013 (item 8) |
| 39 | pesos 35, 25, 15, 10, 10, 5 | Artificial Analysis, Capability Indexes Methodology (item 9) |
| 41, 42 | mecanismo da arena; QR https://arena.ai | Chiang et al., arXiv:2403.04132; item 10 |
| 44, 45 | prova discursiva da PGE-MS de 2021, 180 pontos; dez notas | gráfico "Benchmark, PGE-MS 2021, prova discursiva" do professor: Claude Opus 5.5 91,7; Gemini 4 Argon 90,9; Claude Sonnet 5.5 88,7; Muse Wonder 86,8; GPT-6.1 Sol 83,4; GPT-6 Luna 79,4; Muse Spark 1.3 78,0; Gemini 3.8 Flash 77,8; Claude Haiku 5.5 75,5; DeepSeek V4.1 Flash 64,4. Juízes gemma4:26b e gemma4:31b, com gabarito e espelho. O resultado do modelo local saiu do placar e do deck por decisão do usuário |
| 49, 50, 51 | empresas, famílias, produtos, origem por país | item 11 (subagente nas páginas oficiais); grupos por país definidos pelo usuário |

## Pendências [CONFERIR]

Todas aparecem na tela com a pílula e impedem `./ap pdf` e `./ap empacotar` sem `--rascunho`.

- Slide 7: a data de lançamento do ChatGPT (2022).
- Slide 24: o limite da janela nos apps, que depende do plano.
- Slide 25: como cada produto corta ou resume o histórico.
- Slide 42: as duas respostas do duelo, a preparar pelo professor (a tela mostra linhas cinza no lugar delas).
- Slide 49: qual modelo cada app usa hoje (ChatGPT por plano, Grok 4.7 como padrão, Muse no Meta AI, lista do
  Copilot).
- Slide 50: o carro-chefe atual da Mistral.

Só na fala ou no material, sem pílula na tela: a data de 1956 da IA simbólica (sem fonte, saiu da tela); o
reconhecimento de que a busca do STJ pode pedir desafio anti-robô com muitos celulares (rota impressa); as três
tentativas da prática 3, que o professor grava antes; a folha impressa da prática 2; e os termos de marca da
Microsoft, da Moonshot e da Z.ai (`midia/creditos.json`). Reconferir na véspera a ficha do PL 2338/2023 e a grade de
modelos.

## Mídia e custo

| arquivo | uso | origem | custo |
|---|---|---|---|
| `mesa.webp` | slide 23 | gerada para a versão 2 (`./ap imagens`, Gemini 2K) | US$ 0,0504, já gasto |
| `doc-peticao.webp`, `doc-contrato.webp`, `doc-modelo.webp` | slides 23 e 26 | prévia aprovada, crédito copiado | US$ 0 |
| `logos/*.svg`, `logos/gemma.png`, `logos/kimi.png` | slides 49 e 50 | Wikimedia Commons e repositórios oficiais, sem alteração (`apuracao.md`, item 11) | US$ 0 |
| QR do tokenizador, do STJ e da arena | slides 19, 31 e 42 | segno 1.6.6, local; caminho SVG dentro do deck, cor do tema | US$ 0 |

Gasto desta versão: US$ 0. Gasto acumulado do deck: US$ 0,25 (rascunhos da mesa e da capa antiga, a final da mesa),
somado do `midia/creditos.json`. Os rascunhos da capa de tipos móveis ficaram sem uso, porque a capa passou a ser
feita por código. `heroi-aula1.webp` saiu do deck e do crédito. Cada logo tem entrada no crédito com a origem, a
licença do arquivo e a nota "marca registrada, uso só para identificar". O xAI usa o logo do Grok, como pedido; Llama
e Muse não têm logo próprio, e os cartões usam `meta.svg` e `meta-ai.svg` com o nome ao lado. Toda imagem gerada leva
o selo na tela (23 e 26).

## Avisos aceitos

- Placar (45): 58 palavras visíveis, acima de 45. Os dez nomes e notas são o dado do S.T.A.R. e a Lista final (item 5)
  manda mantê-los; a fala conduz a leitura pelo colchete dos dois primeiros.
- Fechados e abertos (49 e 50): duas grades de cartões vizinhas. É o pedido do roteiro (item 16); os desenhos diferem
  (três colunas com logo ao lado do nome; quatro colunas com logo em cima). O oráculo não avisa, porque são cenas
  próprias.
- Cartões em quatro slides (11, 38, 49, 50) e comparação em nove (3, 6, 15, 25, 33, 42, 46, 48, 51): nenhum par
  vizinho, salvo as grades acima.

## Crítica

Três rodadas no mínimo, como manda o passo 7: a primeira feita pela própria sessão, as seguintes por um subagente
crítico (Opus) que não montou o deck, com a rubrica e a lista de `critica.md`. Cada correção foi conferida nos stills
regerados.

### Rodada 1 (a própria sessão: sondar, folha, stills e viagens)

| gravidade | slide | defeito e evidência | correção |
|---|---|---|---|
| alta | 7 llms | "transformers" transbordava a estação (ERRO do sondar) | estação mais larga no slide |
| alta | 39 legal | os percentuais de 68 px transbordavam a caixa (cinco ERROs) | coluna do número com 210 px, trilho com 780 |
| alta | 31 pratica4 | o pedido de 14 palavras saía da caixa e o QR cobria a última linha (`parada-31-pratica4.png`, y 600 a 700) | nas práticas, caixa sobe para 346 px; na prática 4, caixa de 290 px |
| média | 1 capa | rótulo e título se sobrepunham (AVISO) | título em 176 px, subtítulo e frase descem |
| média | 17 tokens | o "8" encostava no ponto final da frase; hierarquia 1,2x (AVISOs) | contagem em 180 px, à direita, em 1600 |
| média | 26 meio | "no meio" com contraste 3,9:1 em 36 px; 46 palavras; a barra do papel do fim saía da folha | legenda em 40 px; achado e etiqueta mais curtos; barra reposicionada |
| média | 31 pratica4 | 48 palavras | passos e legenda do QR mais curtos (45) |
| média | 46 limites | "Correção" a 140 px entrava na margem | volta a 110 px |
| média | deck | três claros médios seguidos em mapa, definição, lei; tamanho, limite, meio; benchmark, medidas, legal | mapa e tamanho para leve (rótulo, rodapé e pílula mais curtos); a legenda do benchmark saiu |
| baixa | 22 sorteio | "pedido." sozinho na segunda linha | `text-wrap: balance` no bloco da esquerda |

### Rodada 2 (subagente crítico)

| gravidade | slide | defeito e evidência | correção |
|---|---|---|---|
| alta | 42 pratica5 | "1 dedo" e "2 dedos" caíam sobre as barras (`parada-42-pratica5.png`, y 700); o seletor das práticas pegava também a etiqueta de dentro da janela | seletor com `>`: só as etiquetas filhas da section |
| alta | 7 llms | "profundo" e "transformers" se liam juntos (`parada-07-llms.png`, x 480 a 1000) | nomes das estações em 36 px no slide |
| média | 12→13, 35→36 | respiro escuro colado na abertura escura: a virada de bloco não mudava a luz (`viagem-36-melhor-35.png`) | previsao (12) e pior (35) viram respiros claros |
| média | 13, 36, 47 | rótulos "Bloco 2, 4, 5" sem bloco 1 e 3 na tela, e o mapa tem quatro etapas | rótulos com o nome da etapa ("Como funciona"; em 36 e 47, o mesmo rótulo dos slides seguintes, "Qual a melhor IA" e "Fechados e abertos") |
| média | 11, 38 | cartões com a metade de baixo vazia, cara de esqueleto | sem altura mínima; grades descem e ganham espaço |
| média | deck | aberturas só com título; pouca imagem | não corrigido: o usuário mandou tirar a foto do fichário e não gerar imagem nova |
| média/baixa | 2 mapa | o marco dourado estava em "qual usar", como se a aula estivesse no fim | o dourado vai para "conceito" |
| baixa | 52 fecho | quatro dourados (a palavra e os números dos passos) | números em tom suave |
| baixa | 26 meio | a barra do papel "no fim" ficava a 65% da folha | barra em 262 px |
| baixa | 49 fechados | "xAI (SpaceXSI)" encostava na borda do cartão | logo do Grok em 44 px, espaço de 16 px |
| baixa | 23 mesa | canto da foto lavado | não corrigido: foto escolhida pelo usuário, sem re-tratar |
| baixa | 18 parecer | manchete repete o número grande | não corrigido: texto do roteiro (depende do usuário) |

### Rodada 3 (subagente crítico, conferência)

Nenhum defeito alto ou médio. As nove correções da rodada 2 aparecem nos stills regerados, sem regressão; nas viagens
11→12→13 e 34→35→36 a borda claro e escuro aparece sem pisca nem terceiro tom; `./ap sondar` com 0 erro e só o aviso
aceito do placar.

| gravidade | slide | defeito e evidência | correção |
|---|---|---|---|
| baixa | 36, 47 | o rótulo da abertura ("Qual usar") diferia do rótulo dos slides seguintes | rótulos alinhados: "Qual a melhor IA" e "Fechados e abertos" |
| baixa | 33 a 35 | três claros seguidos (comparação, tempo, respiro), com densidades diferentes; o oráculo não avisa | mantido: desenhos e faixas diferentes |

