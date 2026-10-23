# Briefing: curso de IA da co.juris, dia 1, Aula 1. O que é IA e qual usar (versão 4)

Primeira de duas aulas de cerca de 90 minutos, dadas na mesma tarde; a segunda está em `decks/curso-ia-aula2`. A
versão 4 atende aos 11 pedidos do ensaio da versão 3 (22/10/2026), listados em `docs/curso-ia-andamento.md`, e usa os
recursos novos do motor: abertura automática, linha do dia em cinco blocos, guia do apresentador em todos os slides e
cronômetro nas práticas (`docs/palco.md`, Blocos da aula). Os fatos estão em `apuracao.md` e `apuracao-2.md` (anexos
deste briefing); o parecer fictício medido, em `apuracao-parecer-ficticio.md`.

- Curso pago, o primeiro do professor. Turma mista: advogados, uma desembargadora, servidores e assessores, muitos
  sem plano pago de IA. Exemplos neutros, que servem a escritório, gabinete e órgão público.
- Curso agnóstico: Claude e ChatGPT lado a lado, sem vender marca.
- Mensagem em uma frase: a IA escreve bem por previsão, não por consulta, e por isso cada um escolhe a ferramenta pela
  tarefa e confere na fonte. A capa pergunta "Você confere como?" e o fecho responde.
- Cinco práticas com celular ou mão levantada, cada uma com `pratica: N` (cronômetro na tela do apresentador).
- Tema `cojuris`, plano contínuo, mesma trilha dourada e acabamento da prévia (`decks/previa-curso-ia`). Os slides de
  definição, conta, camadas e fronteira têm mais de um clique, um por parte.
- S.T.A.R. de cada bloco, e só um: a classificação da sala (bloco 1, prática 1), a conta dos pesos acontecendo na tela
  (bloco 2, slide 17), a busca do acórdão (bloco 3, prática 4), o placar da prova da PGE-MS (bloco 4, slide 56, que
  continua sendo o da aula) e a corrida EUA e China (bloco 5).

## Mapa

A linha do dia mostra os cinco blocos embaixo da trilha; fica escondida na capa e nas três aberturas de capítulo.

| min | bloco (`blocos`) | slides | práticas |
|---|---|---|---|
| 16 | O que é IA (`o-que-e`) | 1 a 13 | 1, classificar seis sistemas (3 min) |
| 30 | Como funciona (`funciona`) | 14 a 35 | 2, contar tokens (4 min); 3, o mesmo pedido três vezes (3 min) |
| 14 | Onde tropeça (`tropeca`) | 36 a 42 | 4, conferir o acórdão (6 min) |
| 20 | Qual a melhor (`melhor`) | 43 a 57 | 5, o duelo do prazo (3 min) |
| 10 | Fechado e aberto (`abertos`) | 58 a 63 | |

Soma: 90 minutos. O bloco 2 cresceu de 25 para 30 minutos com a sequência de pesos e a memória; a abertura (3 min)
entrou no bloco 1 e o bloco 5 caiu de 12 para 10.

## Slides

Densidade pela parada final, nas faixas do oráculo: respiro (até 12 palavras ou texto de 200 px), leve (13 a 24),
médio (25 a 45). Nenhuma imagem foi gerada; custo de mídia desta versão, US$ 0. "Novo" marca o que entrou na versão 4.

| # | slide | manchete | o que a tela prova | clima e densidade | arquétipo | mídia e custo |
|---|---|---|---|---|---|---|
| 1 | capa | O que é IA e qual usar | novo: abre sozinha; "O juiz julgou o pedido" se escreve a 150 px, o leque grande escolhe "procedente" e o título entra no fim | noite, leve | cena própria (capa) | código; valores ilustrativos (pílula) |
| 2 | mapa | Entender vem antes de escolher | cinco paradas, as mesmas da linha do dia | claro, leve | tempo | código |
| 3 | definicao | IA imita capacidades humanas | definição de trabalho; placa como entrada e saída | claro, médio | comparacao | código |
| 4 | ocde | A OCDE define IA em cinco partes | novo: cinco trechos, um por clique, e a explicação para leigo à direita | claro, médio | cena própria (partes), 5 cliques | código; tradução livre (pílula) |
| 5 | pl | O PL 2338 ajusta a OCDE | novo: cinco trechos do art. 4º, I, com o que é igual e o que é novo; Senado 10/12/2024, Câmara aguarda parecer | noite, médio | cena própria (partes), 5 cliques | código |
| 6 | cotidiano | Você já usa IA todo dia | frase grande | noite, respiro | respiro | nenhuma |
| 7 | regras | Regras escritas ou padrões aprendidos | simbólica contra aprendizado de máquina | claro, médio | comparacao | código |
| 8 | llms | LLMs nascem dos transformers | a trilha se divide até os LLMs; ChatGPT em 30/11/2022 | claro, médio | ramos | código |
| 9 | tipos | Específica faz uma; generalista, várias | frase grande; uso geral, não AGI | claro, respiro | respiro | nenhuma |
| 10 | pratica1 | Você classifica seis sistemas | seis sistemas e a regra dos dedos (S.T.A.R. do bloco 1) | noite, médio | objetos | código |
| 11 | gabarito | Quatro específicas, duas generalistas | quatro e duas estações | claro, médio | ramos | código |
| 12 | generativa | A generativa cria, não só classifica | quatro cartões | claro, médio | cena própria (cartões) | código; ilustrativos (pílula) |
| 13 | previsao | Parece criatividade; é previsão | frase grande | claro, respiro | respiro | nenhuma |
| 14 | funciona | Como funciona por dentro | abertura do bloco 2: pesos, tokens, previsão e a mesa | noite, respiro | abertura | nenhuma |
| 15 | corpus | Ela treinou com trilhões de pedaços | "15 trilhões" de tokens (Llama 3.1 405B) | claro, leve | numero | código |
| 16 | vetor | A palavra vira uma lista de números | novo: "prazo" vira [2, 1, 3] em caixas de 200 px | claro, leve | cena própria (vetor) | código; ilustrativos (pílula) |
| 17 | conta | Cada número multiplica um peso e soma | novo: coluna A no primeiro clique (2×1 + 1×0 + 3×1 = 5), coluna B no segundo (soma −1); a saída [5, −1] (S.T.A.R. do bloco 2) | noite, médio | cena própria (conta), 2 cliques | código; ilustrativos (pílula) |
| 18 | camadas | Negativo vira zero, e a conta segue | novo: [5, −1] vira [5, 0]; depois a rede de cinco camadas; 405 bilhões de pesos são os parâmetros | claro, médio | cena própria (camadas), 2 cliques | código |
| 19 | parametros | O treino ajusta os pesos | treino contra uso; pesos são parâmetros, não textos salvos | claro, médio | comparacao | código |
| 20 | calcula | Sem busca, ela calcula; não consulta | frase grande | noite, respiro | respiro | nenhuma |
| 21 | tokens | Ela lê pedaços, não palavras | a palavra se parte em 4 e a frase em 8 tokens | claro, médio | cena própria (tokens) | código |
| 22 | parecer | Parecer de 3 páginas: 2.056 tokens | 2.056 grande | claro, respiro (320 px) | numero | código |
| 23 | pratica2 | Palavras viram blocos na tela | a frase, duas rotas, QR do tokenizador | noite, médio | objetos | QR por código |
| 24 | previsto | A IA prevê um token por vez | dois ciclos de leque | claro, médio | escolha | código; inventadas (pílula) |
| 25 | pratica3 | O mesmo pedido pode variar | o pedido e três passos | noite, médio | objetos | código |
| 26 | sorteio | Cada resposta é um sorteio com pesos | leque raso e sorteio | claro, médio | escolha com `data-sorteio` | código; inventados (pílula) |
| 27 | mesa | A janela de contexto é a mesa | novo, desenhado: o retângulo enche de instrução, conversa, anexos e espaço da resposta; o anexo que não coube fica de fora, em dourado | claro, leve | cena própria (mesa) | código (a foto `mesa.webp` saiu) |
| 28 | tamanho | A mesa tem tamanho | "1 milhão" de tokens, Claude Opus 5.5 nos planos pagos | claro, leve | numero | código |
| 29 | limite | Passou do limite, algo fica de fora | cabe contra não cabe: "O começo é resumido ou deixado de fora." | noite, médio | comparacao | código |
| 30 | queda | Quanto maior o texto, mais o acerto cai | novo: GPT-4o de 99,3% para 69,7% com 32 mil tokens (NoLiMa); a perda marcada em dourado | claro, médio | cena própria (queda) | código |
| 31 | conversa | Conversa nova, mesa limpa | frase grande; salvo memória ligada | noite, respiro | respiro | nenhuma |
| 32 | memoria | A memória leva notas à conversa nova | novo: uma nota sai do caderno e pousa na mesa da conversa nova | noite, médio | cena própria (memória) | código |
| 33 | controle | Você vê, corrige e apaga a memória | novo: ChatGPT e Claude, onde fica e a conversa temporária ou anônima | noite, médio | comparacao | código |
| 34 | sigilo | Apagar a conversa não apaga a memória | novo: três linhas ligadas às páginas de ajuda da OpenAI e da Anthropic | claro, médio | fios | código |
| 35 | passos | Do corpus à resposta, em cinco passos | cinco marcos | claro, médio | tempo | código |
| 36 | linguagem | Ela vai bem em linguagem | frase grande | claro, respiro | respiro | nenhuma |
| 37 | avianca | Ela inventa com a mesma confiança | fios da ordem de sanção | claro, médio | fios | código |
| 38 | pratica4 | Você confere se o acórdão existe | pedido, três passos, QR do STJ (S.T.A.R. do bloco 3) | noite, médio | objetos | QR por código |
| 39 | conferiram | Os números conferiram? | frase grande e as três respostas | noite, respiro | respiro | nenhuma |
| 40 | fronteira | A fronteira da IA é irregular | novo, desenhado: contorno serrilhado, três tarefas dentro (1º clique), três fora e o número do estudo (2º clique) | claro, médio | cena própria (fronteira), 2 cliques | código; exemplos do professor (pílula) |
| 41 | responde | Quem usa responde pelo que entrega | quatro marcos | claro, leve | tempo | código |
| 42 | pior | Hoje é a pior IA que você usará | frase grande | claro, respiro | respiro | nenhuma |
| 43 | melhor | Qual é a melhor IA? | abertura do bloco 4 | noite, respiro | abertura | nenhuma |
| 44 | benchmark | Benchmark é o ENEM da IA | a caneta corrige dez itens, 8 de 10 a 140 px | claro, respiro | numero | código; ilustrativo (pílula) |
| 45 | medidas | Seis coisas que os benchmarks medem | seis cartões | claro, médio | cena própria (cartões) | código |
| 46 | aageral | No índice geral, o topo é apertado | novo: sete modelos, melhor variante de cada, notas 58 a 52 | claro, mais de 45 | cena própria (ranking) | código |
| 47 | legal | O índice jurídico pesa seis habilidades | refeito: o que é, numa frase, e uma barra só dividida em 35, 25, 15, 10, 10 e 5% com rótulos grandes | noite, médio | cena própria (Legal Index) | código |
| 48 | aalegal | No índice jurídico, o Opus 5.5 lidera | novo: dez modelos, 63 a 52 | claro, mais de 45 | cena própria (ranking) | código |
| 49 | processo | Prova não é processo | frase grande | noite, respiro | respiro | nenhuma |
| 50 | arena | Na arena, pessoas votam às cegas | quatro passos da votação | claro, médio | tempo | código |
| 51 | agentes | Como agente, o Opus 5.5 abre vantagem | novo: o Top 10 de agentes escolhido pelo professor, com o que o percentual quer dizer | claro, mais de 45 | cena própria (ranking) | código |
| 52 | pratica5 | Qual o prazo do Estado para contestar? | refeito: as duas respostas legíveis, 1 ou 2 dedos, um minuto | noite, médio | comparacao | código; respostas preparadas (pílula) |
| 53 | revelacao | A resposta B esquece o prazo em dobro | novo: fios dos arts. 335, 183 e 219 do CPC; "em dobro" acende | claro, médio | fios | código; respostas preparadas (pílula) |
| 54 | mede | Benchmark mede prova; arena, preferência | frase grande | noite, respiro | respiro | nenhuma |
| 55 | prova | Demos a prova da PGE às IAs | 180 grande, composição da prova, correção por dois Gemma 4 | claro, respiro (320 px) | numero | código |
| 56 | placar | Nesta prova, o topo ficou próximo | dez barras, colchete dourado nos dois primeiros (S.T.A.R. da aula) | noite, mais de 45 | cena própria (placar) | código |
| 57 | limites | O que essa nota não diz | prova contra correção | claro, médio | comparacao | código |
| 58 | aberto | Fechado ou aberto? | abertura do bloco 5 | noite, respiro | abertura | nenhuma |
| 59 | pesos | Aberto é ter os pesos | fechado contra aberto | noite, médio | comparacao | código |
| 60 | fechados | Os principais modelos fechados | seis cartões com logo; OpenAI "GPT-6"; "família mais recente" | claro, médio | cena própria (cartões) | logos, US$ 0 |
| 61 | abertos | Os principais modelos abertos | oito cartões com logo; Mistral "Large 3" | claro, médio | cena própria (cartões) | logos, US$ 0 |
| 62 | corrida | Na ponta, EUA e China disputam | EUA contra China; na Europa, a Mistral (S.T.A.R. do bloco 5) | noite, médio | comparacao | código |
| 63 | fecho | Escolha por tarefa e teste você | três passos; Aula 2: como pedir bem | noite, leve | fecho | nenhuma |

### O que mudou da versão 3 e por quê (os 11 pedidos)

1. Pesos e matrizes: três cenas novas (16 vetor, 17 conta, 18 camadas) seguem o roteiro de sete passos de
   `apuracao-2.md`, item 8, com a conta [2, 1, 3] × matriz 3×2 = [5, −1] → [5, 0]. A conta acontece linha por linha,
   com o par que se multiplica aceso; o slide 19 (parâmetros) fecha com "o treino ajusta os pesos". Vetor, matriz e
   ReLU ficam só na fala, se perguntarem.
2. Capa: cena própria, sem foto, com `autoplay: true`. A frase se escreve a 150 px, o leque de três candidatas cresce
   ao lado, a vencedora voa para a frase e o título da aula entra embaixo. A entrada inteira cabe em 3,5 s.
3. Pendências de conferência: nenhuma no deck nem neste briefing. Cada pendência seguiu a seção 0 de `apuracao-2.md` (tabela em
   Fontes, abaixo).
4. Janela de contexto: a mesa é desenhada por código (slide 27); `mesa.webp` saiu do deck, do `imagens.toml` e do
   `midia/creditos.json`. Os recortes `doc-*.webp`, usados só na mesa antiga e no "meio se perde", saíram também. O
   slide 30 troca de tese: "Quanto maior o texto, mais o acerto cai", com o GPT-4o no NoLiMa; Liu et al. 2023 saiu da
   tela e fica numa nota, para o caso de alguém perguntar.
5. Guia: `notas: {diga, faca, transicao}` nos 63 slides e `pratica` nas cinco práticas (3, 4, 3, 6 e 3 min).
6. Linha do dia: cinco blocos que somam 90 minutos, `bloco` no primeiro slide de cada bloco e `linhaDia: false` na
   capa e nas aberturas 14, 43 e 58.
7. Conceito: OCDE (slide 4) e PL 2338/2023 (slide 5) decompostos em cinco partes cada, um clique por parte. Os dois
   slides repetem o desenho de propósito, como o par palavra e data da prévia: é a mesma leitura feita duas vezes, e o
   segundo muda de clima (claro, depois noite) e fala do que muda. O texto inteiro da OCDE fica nas notas.
8. Fronteira irregular: contorno serrilhado desenhado por código (slide 40), três tarefas dentro e três fora, pílula
   "exemplos do professor" e o número do estudo publicado, com a fonte.
9. Qual a melhor IA: índice geral (46), Legal Index refeito como barra única com uma frase do que ele é (47), ranking
   jurídico (48) e ranking de agentes da arena.ai (51), com a explicação do percentual na tela.
10. Duelo: a proposta de `apuracao-2.md`, item 0.1 (slide 52), com instrução de leitura, voto e tempo, e a revelação
    com o CPC no slide seguinte (53). A resposta A foi encurtada para caber na tela; o texto inteiro está nas notas.
11. Memória: três slides depois de "Conversa nova, mesa limpa" (32 o que é, 33 como controlar, 34 sigilo).

Ficou de fora da versão 3: o slide "lei" (fios OCDE e PL), substituído pelos slides 4 e 5; o slide "meio"; o QR da
arena na prática 5, porque o duelo deixou de ser sobre a arena. O mapa ganhou a quinta etapa, igual à linha do dia.

### Respiro e partitura de luz

As maiores sequências sem respiro têm cinco slides, no limite (23 a 27 e 50 a 54, este com a prática e a revelação).
Contam como respiro também os números de 200 px ou mais (15, 16, 22, 28 e 55). Na noite: capa,
pl, respiros fortes, aberturas, práticas, conta (S.T.A.R. do bloco 2), limite, memória e controle, Legal Index,
placar, pesos, corrida e fecho. Limite e controle foram para a noite para quebrar sequências de três claros médios
que o oráculo apontou; o Legal Index, para quebrar quatro claros seguidos entre os rankings.

## Fala, por bloco

O roteiro de fala de cada slide está nas notas do deck (tela do apresentador, tecla P), com o que dizer, o que fazer e
a ponte para o próximo. Os pontos que não podem escapar:

- O que é IA. A OCDE e o PL dizem a mesma coisa com o verbo "inferir"; o PL ainda é projeto, aprovado no Senado em
  10/12/2024 e aguardando parecer na Câmara. O ChatGPT saiu em 30/11/2022: lançamento de produto, não origem da
  técnica.
- Como funciona. Peso é um número aprendido; a conta é multiplicar e somar, camada após camada, e os bilhões de pesos
  são os parâmetros. Sem busca, ela calcula. A mesa tem tamanho, e mesmo dentro dela o acerto cai quando a resposta
  exige ligar dados espalhados. Apagar a conversa não apaga a memória que saiu dela.
- Onde tropeça. Mata v. Avianca; a fronteira irregular, com os exemplos jurídicos ditos como do professor.
- Qual a melhor. Rankings de 22/10/2026, reconferir na véspera. O percentual da arena de agentes é a diferença, em
  pontos percentuais, em relação ao modelo médio, em tarefas reais. As respostas do duelo são do professor, e isso se
  diz na revelação. A prova da PGE-MS é teste do professor, não da PGE-MS, e o placar não é ranking geral.
- Fechado e aberto. Aberto é ter os pesos; não garante sigilo sozinho.

## Fontes

Todas lidas em 22/10/2026, salvo indicação; o trecho lido e a ressalva de cada uma estão em `apuracao.md` e
`apuracao-2.md`.

| slide | dado na tela | fonte |
|---|---|---|
| 4 | definição da OCDE, tradução livre | OCDE, OECD/LEGAL/0449, PDF oficial (apuração 2, item 6.1); decomposição e explicações do professor |
| 5 | PL 2338/2023, art. 4º, I; Senado 10/12/2024; Câmara aguarda parecer | inteiro teor na Câmara e API de dados abertos, proposição 2487262 (apuração 2, item 6.2) |
| 8 | transformers, 2017; ChatGPT, 30/11/2022 | Vaswani et al., arXiv:1706.03762; post oficial da OpenAI no Internet Archive (apuração 2, item 1.1) |
| 15, 18 | Llama 3.1 405B: cerca de 15 trilhões de tokens; 405 bilhões de parâmetros | model card do Llama 3.1, Meta (apuração, item 3) |
| 16 a 18 | [2, 1, 3] × pesos = [5, −1] → [5, 0] | exemplo do professor, conta refeita em Python (apuração 2, item 8); pílula "números ilustrativos" |
| 21, 22 | tokens medidos; 2.056 tokens no parecer fictício | `tiktoken`, o200k_base (apuração, item 5; `apuracao-parecer-ficticio.md`) |
| 28 | 1 milhão de tokens no Claude Opus 5.5, planos pagos, também no app | central de ajuda da Anthropic, artigo 8606394 (apuração 2, item 1.2) |
| 29 | o começo é resumido ou deixado de fora | texto genérico; nas notas, só o caso documentado do Claude, artigo 11647753 (apuração 2, item 1.3) |
| 30 | GPT-4o de 99,3% para 69,7% com 32 mil tokens | NoLiMa, Modarressi et al., arXiv:2502.05167 (ICML 2025); Chroma, "Context Rot", 14/07/2025; Anthropic, Claude Opus 4.6, 05/02/2026 (apuração 2, itens 2.3 a 2.6) |
| 32 a 34 | memória, onde controlar, conversa temporária e anônima, apagar não é simétrico, 30 dias | páginas de ajuda da OpenAI (8590148, 8914046) e da Anthropic (11817273, 12260368) (apuração 2, item 3) |
| 37 | Mata v. Avianca, ordem de 22/06/2023, multa de US$ 5.000 | Opinion and Order on Sanctions, S.D.N.Y. (apuração, item 6) |
| 40 | fora da fronteira, acerto de 84,5% para 60–70% | Dell'Acqua et al., HBS Working Paper 24-013 (2023, 19 pontos percentuais) e Organization Science 37(2), 2026, pelo resumo do HBS AI Institute de 09/04/2026 (apuração 2, item 7.1); exemplos do professor (item 7.3) |
| 46 | Intelligence Index v4.3.2: Opus 5.5 58; Sonnet 5.5 56; Muse Wonder Full 56; Fable 5.1 53; GPT-6 Astra 53; Gemini 4 Argon 53; Muse Wonder 52 | artificialanalysis.ai, leaderboards (apuração 2, item 4.1); são os sete modelos distintos entre as dez primeiras linhas, melhor variante de cada |
| 47 | pesos 35, 25, 15, 10, 10, 5 | metodologia e FAQ do Legal Index (apuração 2, item 4.2) |
| 48 | Legal Index: 63 a 52, dez modelos | artificialanalysis.ai/indexes/legal (apuração 2, item 4.2) |
| 50 | votação às cegas | Chiang et al., arXiv:2403.04132; nome Arena desde 28/01/2026 (apuração 2, item 5) |
| 51 | Top 10 Agents, 20,92% a 8,09%; 367.936.358 sessões | captura do professor da página inicial, 22/10/2026; percentuais conferidos na coluna "Net Improvement" de arena.ai/leaderboard/agent; significado pelo FAQ da página (apuração 2, item 5.4) |
| 52, 53 | 15 dias (art. 335), em dobro (art. 183), dias úteis (art. 219) | CPC, texto compilado no Planalto (apuração 2, item 0.1); respostas redigidas pelo professor |
| 55, 56 | prova discursiva da PGE-MS 2021, 180 pontos; dez notas | gráfico do professor (Claude Opus 5.5 91,7 a DeepSeek V4.1 Flash 64,4); juízes gemma4:26b e gemma4:31b com gabarito e espelho |
| 60, 61, 62 | famílias, produtos e origem | apuração, item 11; OpenAI "GPT-6" pelo system card de 07/10/2026; Mistral "Large 3" (apuração 2, itens 1.4 e 1.5) |

Destino das pendências de conferência da versão 3, pela seção 0 de `apuracao-2.md`: slide 8 (ChatGPT, 2022) resolvido com a data
oficial; slide 28 (limite no app) resolvido com a central de ajuda; slide 29 (como cada produto corta) reescrito em
texto genérico; slide 52 (respostas do duelo) escrito pelo professor; slide 60 (versões nos apps) reescrito como
"família mais recente", com "GPT-6"; slide 61 (Mistral) resolvido como "Large 3".

Reconferir na véspera: a ficha do PL 2338/2023, os três rankings, a grade de modelos e se os pesos do Mistral Large 4
saíram.

## Mídia e custo

| arquivo | uso | origem | custo |
|---|---|---|---|
| `logos/*.svg`, `logos/gemma.png`, `logos/kimi.png` | slides 60 e 61 | Wikimedia Commons e repositórios oficiais, sem alteração (`apuracao.md`, item 11) | US$ 0 |
| QR do tokenizador e do STJ | slides 23 e 38 | segno 1.6.6, local; caminho SVG dentro do deck | US$ 0 |

Gasto desta versão: US$ 0. Gasto acumulado do deck: US$ 0,25, todo em versões anteriores (rascunhos da capa antiga e da
mesa, a final da mesa), ainda registrado em `midia/creditos.json` pelas entradas de `midia/originais/`. Saíram do deck
e do crédito: `mesa.webp`, `doc-contrato.webp`, `doc-modelo.webp` e `doc-peticao.webp`. O deck não tem mais imagem
gerada, por isso nenhum slide leva selo.

## Avisos aceitos

- Rankings 46 (57 palavras), 48 (57) e 51 (64), e o placar 56 (62): acima de 45 palavras. Os nomes e as notas são o
  dado que o professor pediu (item 9) e a fala conduz a leitura pela barra dourada do primeiro. Os três rankings usam o
  mesmo desenho, sem vizinhos entre si.
- Slides 4 e 5 (OCDE e PL): mesmo desenho em vizinhos, justificado no item 7 acima. O oráculo não avisa, porque são
  cenas próprias.
- Capa: a entrada tem 3,5 s, no limite do passo; toca sozinha ao abrir, enquanto a sala se acomoda.

## Crítica

Três rodadas, como manda o passo 7: a primeira pela própria sessão, as seguintes por um subagente crítico (Opus) que
não montou o deck. Cada correção foi conferida nos stills regerados.

### Rodada 1 (a própria sessão: sondar, folha, stills e viagens)

| gravidade | slide | defeito e evidência | correção |
|---|---|---|---|
| alta | 5 pl | as explicações com rótulo em `<small>` transbordavam a caixa (cinco ERROs) | rótulo integrado à frase ("Como na OCDE: ...", "Novo: ...") |
| alta | 17 conta, 30 queda | "soma" e os percentuais de 130 px transbordavam (quatro ERROs) | entrelinha 1,2 na soma; coluna do número com 480 px |
| alta | 40 fronteira | "dentro" e "listar argumentos" cruzavam o contorno; o contorno entrava na margem (`parada-51-fronteira.png`, x 100 a 350) | contorno mais estreito (centro 660, raio 480); tarefas de dentro em x 400; etiquetas fora do traço |
| média | 4, 5, 52, 60 | 46 a 61 palavras (AVISOs) | números das partes por contador do CSS, trechos e rodapés mais curtos, resposta A mais curta |
| média | deck | 34 de 63 slides sem nada acima de 120 px | soma da conta a 140 px, percentuais da queda a 130 px, letras do duelo a 180 px, placar do benchmark a 140 px |
| média | 26 a 30, 33 a 35, 2 a 4 | três ou mais claros médios seguidos (AVISOs de sequência) | limite e controle na noite; legenda do mapa retirada |
| média | 18 camadas | só a linha do −1 tinha seta; o filtro flutuava entre as linhas | seta nas duas linhas e o filtro entre elas |
| baixa | 5 pl | na viagem a 70% só o título estava na tela | o primeiro trecho entra 0,1 s depois do início do conteúdo |
| baixa | 32 memoria | vão vazio entre o caderno e a mesa | seta tracejada que acende antes da nota voar |
| baixa | 51 agentes | rodapé colado na última linha | linhas de 50 px |

### Rodada 2 (subagente crítico)

| gravidade | slide | defeito e evidência | correção |
|---|---|---|---|
| alta | deck, capa e aberturas | nenhuma imagem; a folha parece uma página só | não corrigido: o pedido proíbe imagem gerada nova e o professor tirou a foto da capa; o peso visual vem dos desenhos por código (capa, conta, camadas, mesa, queda, fronteira, Legal Index) |
| alta | 46, 48, 51, 27 | a 70% da viagem os rankings mostram uma linha só e a mesa, a moldura vazia (`viagem-46-aageral-70.png`, `viagem-27-mesa-70.png`) | linhas e barras começam 0,2 s mais cedo, ainda na viagem; a mesa e os blocos também |
| média | 4 a 13 | OCDE e PL com o mesmo desenho, dez paradas | não corrigido: par deliberado, justificado no item 7 e em Avisos aceitos; trocar a sequência depende do usuário |
| média | 32 memoria | barras-esqueleto no caderno e na nota | não corrigido: escrever notas de exemplo poria dado pessoal fictício na tela; a fala dá os exemplos |
| média | 18 camadas | números inventados sem pílula | pílula "números ilustrativos" |
| média | 34 sigilo | o fio cinza da terceira linha cruzava o dourado; "30 dias." quebrava | as duas linhas da OpenAI juntas, a da Anthropic por último; minuta mais larga; "30 dias" sem quebra |
| média | 1 capa | trilhos do leque curtos (170 px) | trilhos de 230 px, leque 30 px à esquerda |
| baixa | 18 camadas | "zero" sozinho na segunda linha do filtro | filtro numa linha, 32 px |
| baixa | 30 queda | o contador mostrava "0,0%" antes de a barra crescer | o número acende com a barra |
| baixa | 51 agentes | "pontos a mais" ao lado de valores em % | linha de cima: "Pontos percentuais acima do modelo médio, em tarefas reais." |

### Rodada 3 (subagente crítico, conferência)

As sete correções da rodada 2 pegaram, sem regressão nas paradas 01, 27, 28, 37, 40, 44, 57, 59 e 62.

| gravidade | slide | defeito e evidência | correção |
|---|---|---|---|
| alta | 56 placar | a 70% da viagem, quadro quase vazio no S.T.A.R. da aula (`viagem-56-placar-70.png`) | barras, nomes e valores começam antes do pouso; o colchete continua depois das barras |
| média | 56 placar | notas sem unidade logo depois de "180 pontos" | rodapé "% dos 180 pontos; 1 prova (PGE-MS 2021), correção por IA, não é ranking geral" |
| média | 46, 48 | a barra do líder enchia o trilho com "nota de 0 a 100" escrito em cima | escala de 0 a 100 nesses dois (`data-escala="100"`); no 51, a escala segue o máximo |
| média | 30 queda | a barra de 32 mil tokens subia do zero num slide que diz "cai" | ela nasce no tamanho da primeira (99,3%) e encolhe até 69,7%, com o número descendo junto; a perda tracejada vem depois |
| média | 27 mesa | o "espaço da resposta" descia sobre o rótulo no pouso | entra só com opacidade |
| média | todas as viagens | a trilha passa por cima dos nomes da linha do dia por cerca de 0,3 s (`viagem-46-aageral-35.png`, x 1580 a 1740) | não corrigido aqui: é desenho do motor (`motor/palco.js`), que esta tarefa não podia alterar; anotado como pendência do motor (esmaecer a linha do dia durante a viagem ou descer os nomes) |
| baixa | 28 camadas | a pílula ficava ao lado do dado real do Llama | pílula junto das caixas 5 e −1 |
| baixa | 46, 48, 51 | o valor aparecia antes de a barra chegar | o valor acende quando a barra pousa |

### Rodada 4 (a própria sessão, conferência final)

Stills e quadros regerados depois da rodada 3: `viagem-56-placar-70.png` já mostra as colunas subindo com os valores;
`parada-40-queda.png` e `viagem-30-queda-pouso.png` mostram a segunda barra encolhendo de 99,3% para 69,7%;
`parada-57-aageral.png` tem a barra do líder em 58% do trilho; `viagem-27-mesa-pouso.png` sem texto sobre o rótulo;
`parada-28-camadas.png` com a pílula junto das caixas. `./ap sondar` termina com 0 erro e os quatro avisos aceitos.
Nenhum defeito alto ou médio do deck; resta só a pendência do motor da rodada 3, fora do escopo do deck.
