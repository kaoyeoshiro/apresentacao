# Briefing: curso de IA da co.juris, dia 1, Aula 1. O que é IA e qual usar (versão 6)

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
- Quatro práticas com celular ou mão levantada (a quinta, o duelo, saiu na versão 6), cada uma com `pratica: N` (cronômetro na tela do apresentador).
- Tema `cojuris`, plano contínuo, mesma trilha dourada e acabamento da prévia (`decks/previa-curso-ia`). Os slides de
  definição, tamanho dos modelos e fronteira têm mais de um clique, um por parte.
- S.T.A.R. de cada bloco, e só um: a classificação da sala (bloco 1, prática 1), os fios das pistas decidindo a palavra
  (bloco 2, slide 16), a busca do acórdão (bloco 3, prática 4), o placar da prova da PGE-MS (bloco 4, slide 56, que
  continua sendo o da aula) e a corrida EUA e China (bloco 5).

## Mapa

A linha do dia mostra os cinco blocos embaixo da trilha; fica escondida na capa e nas três aberturas de capítulo.

| min | bloco (`blocos`) | slides | práticas |
|---|---|---|---|
| 16 | O que é IA (`o-que-e`) | 1 a 13 | 1, classificar seis sistemas (3 min) |
| 30 | Como funciona (`funciona`) | 14 a 34 | 2, contar tokens (4 min); 3, o mesmo pedido três vezes (3 min) |
| 14 | Onde tropeça (`tropeca`) | 35 a 41 | 4, conferir o acórdão (6 min) |
| 17 | Qual a melhor (`melhor`) | 42 a 55 | nenhuma (o duelo saiu na versão 6) |
| 13 | Fechado e aberto (`abertos`) | 56 a 62 | |

Soma: 90 minutos. Na versão 6, os 3 minutos da prática 5 passaram do bloco 4 (20 para 17) ao bloco 5 (10 para 13),
que ganhou tempo para os modelos abertos e fechados. O bloco 2 cresceu de 25 para 30 minutos com a sequência de pesos e a memória; a abertura (3 min)
entrou no bloco 1 e o bloco 5 caiu de 12 para 10.

## Slides

Densidade pela parada final, nas faixas do oráculo: respiro (até 12 palavras ou texto de 200 px), leve (13 a 24),
médio (25 a 45). Nenhuma imagem foi gerada; custo de mídia desta versão, US$ 0. "Novo" marca o que entrou na versão 4; "v5", o que mudou na versão 5 (62 slides, 72 paradas desde a versão 6).

| # | slide | manchete | o que a tela prova | clima e densidade | arquétipo | mídia e custo |
|---|---|---|---|---|---|---|
| 1 | capa | O que é IA e qual usar | v5: fundo claro, logo oficial da co.juris (variável do tema), fio que se traça e o título em duas linhas a 124 px; abre sozinha | claro, leve | cena própria (marca) | logo do tema, US$ 0 |
| 2 | mapa | Entender vem antes de escolher | cinco paradas, as mesmas da linha do dia | claro, leve | tempo | código |
| 3 | definicao | IA imita capacidades humanas | definição de trabalho; placa como entrada e saída | claro, médio | comparacao | código |
| 4 | ocde | A OCDE define IA em cinco partes | novo: cinco trechos, um por clique, e a explicação para leigo à direita | claro, médio | cena própria (partes), 5 cliques | código; tradução livre (pílula) |
| 5 | pl | O PL 2338 ajusta a OCDE | novo: cinco trechos do art. 4º, I, com o que é igual e o que é novo; Senado 10/12/2024, Câmara aguarda parecer | noite, médio | cena própria (partes), 5 cliques | código |
| 6 | cotidiano | Você já usa IA todo dia | frase grande | noite, respiro | respiro | nenhuma |
| 7 | regras | Regras escritas ou padrões aprendidos | simbólica contra aprendizado de máquina | claro, médio | comparacao | código |
| 8 | historia | A IA tem 70 anos; o ChatGPT, quase 4 | v5: seis marcos (1956, anos 80, anos 90, 2012, 2017, 2022) e a legenda com GPT-3 e GPT-6, cada data com fonte (apuracao-2.md, item 10) | claro, médio | tempo | código |
| 9 | tipos | Específica faz uma; generalista, várias | frase grande; uso geral, não AGI | claro, respiro | respiro | nenhuma |
| 10 | pratica1 | Você classifica seis sistemas | seis sistemas e a regra dos dedos (S.T.A.R. do bloco 1) | noite, médio | objetos | código |
| 11 | gabarito | Quatro específicas, duas generalistas | quatro e duas estações | claro, médio | ramos | código |
| 12 | generativa | A generativa cria, não só classifica | quatro cartões | claro, médio | cena própria (cartões) | código; ilustrativos (pílula) |
| 13 | previsao | Parece criatividade; é previsão | frase grande | claro, respiro | respiro | nenhuma |
| 14 | funciona | Como funciona por dentro | abertura do bloco 2: pesos, tokens, previsão e a mesa | noite, respiro | abertura | nenhuma |
| 15 | corpus | Ela treinou com trilhões de pedaços | v6: "+32 trilhões" de tokens (DeepSeek V4, 2026) | claro, leve | numero | código |
| 16 | pistas | Pesos dizem quanto cada pista importa | v6: "juiz", "julgou" e "pedido" ligadas a "procedente" e "improcedente" por fios de espessura igual ao peso; a vencedora acende e entra na frase, sem conta (S.T.A.R. do bloco 2) | claro, leve | cena própria (pistas) | código; ilustrativo (pílula) |
| 17 | ponta | Os de ponta passam de 1 trilhão de pesos | v6: a rede em camadas, "cada fio é um peso" (1º clique); Kimi K3, Qwen3.8 Max, Mistral Large 4 e Muse Spark Open em barras com o marco dourado de 1 trilhão, a linha dos fechados e a fonte (2º clique) | noite, médio | cena própria (ponta), 2 cliques | código |
| 18 | parametros | O treino ajusta os pesos | treino contra uso; pesos são parâmetros, não textos salvos | claro, médio | comparacao | código |
| 19 | calcula | Sem busca, ela calcula; não consulta | frase grande | noite, respiro | respiro | nenhuma |
| 20 | tokens | Ela lê pedaços, não palavras | a palavra se parte em 4 e a frase em 8 tokens | claro, médio | cena própria (tokens) | código |
| 21 | parecer | Parecer de 3 páginas: 2.056 tokens | 2.056 grande | claro, respiro (320 px) | numero | código |
| 22 | pratica2 | Palavras viram blocos na tela | v5: a frase, dois passos e o link clicável do tokenizador; sem folha impressa | noite, médio | objetos | link, código |
| 23 | previsto | A IA prevê um token por vez | dois ciclos de leque | claro, médio | escolha | código; inventadas (pílula) |
| 24 | pratica3 | O mesmo pedido pode variar | o pedido e três passos | noite, médio | objetos | código |
| 25 | sorteio | Cada resposta é um sorteio com pesos | leque raso e sorteio | claro, médio | escolha com `data-sorteio` | código; inventados (pílula) |
| 26 | mesa | A janela de contexto é a mesa | novo, desenhado: o retângulo enche de instrução, conversa, anexos e espaço da resposta; o anexo que não coube fica de fora, em dourado | claro, leve | cena própria (mesa) | código (a foto `mesa.webp` saiu) |
| 27 | tamanho | A mesa tem tamanho | "1 milhão" de tokens, Claude Opus 5.5 nos planos pagos | claro, leve | numero | código |
| 28 | limite | Passou do limite, algo fica de fora | cabe contra não cabe: "O começo é resumido ou deixado de fora." | noite, médio | comparacao | código |
| 29 | queda | Quanto maior o texto, mais o acerto cai | novo: GPT-4o de 99,3% para 69,7% com 32 mil tokens (NoLiMa); a perda marcada em dourado | claro, médio | cena própria (queda) | código |
| 30 | conversa | Conversa nova, mesa limpa | frase grande; salvo memória ligada | noite, respiro | respiro | nenhuma |
| 31 | memoria | A memória leva notas à conversa nova | novo: uma nota sai do caderno e pousa na mesa da conversa nova | noite, médio | cena própria (memória) | código |
| 32 | controle | Você vê, corrige e apaga a memória | novo: ChatGPT e Claude, onde fica e a conversa temporária ou anônima | noite, médio | comparacao | código |
| 33 | sigilo | Apagar a conversa não apaga a memória | novo: três linhas ligadas às páginas de ajuda da OpenAI e da Anthropic | claro, médio | fios | código |
| 34 | passos | Do corpus à resposta, em cinco passos | cinco marcos | claro, médio | tempo | código |
| 35 | linguagem | Ela vai bem em linguagem | frase grande | claro, respiro | respiro | nenhuma |
| 36 | avianca | Ela inventa com a mesma confiança | fios da ordem de sanção | claro, médio | fios | código |
| 37 | pratica4 | Você confere se o acórdão existe | v5: pedido, três passos e o link clicável da pesquisa do STJ (S.T.A.R. do bloco 3) | noite, médio | objetos | link, código |
| 38 | conferiram | Os números conferiram? | frase grande e as três respostas | noite, respiro | respiro | nenhuma |
| 39 | fronteira | A fronteira da IA é irregular | novo, desenhado: contorno serrilhado, três tarefas dentro (1º clique), três fora e o número do estudo (2º clique) | claro, médio | cena própria (fronteira), 2 cliques | código; exemplos do professor (pílula) |
| 40 | responde | Quem usa responde pelo que entrega | quatro marcos | claro, leve | tempo | código |
| 41 | pior | Hoje é a pior IA que você usará | frase grande | claro, respiro | respiro | nenhuma |
| 42 | melhor | Qual é a melhor IA? | abertura do bloco 4 | noite, respiro | abertura | nenhuma |
| 43 | benchmark | Benchmark é o ENEM da IA | a caneta corrige dez itens, 8 de 10 a 140 px | claro, respiro | numero | código; ilustrativo (pílula) |
| 44 | medidas | Seis coisas que os benchmarks medem | seis cartões | claro, médio | cena própria (cartões) | código |
| 45 | aageral | No índice geral, o Opus 5.5 vai à frente | v5: eixo de 50 a 60, escrito na tela; sete modelos, 58 a 52 | claro, mais de 45 | cena própria (ranking) | código |
| 46 | legal | O índice jurídico pesa seis habilidades | refeito: o que é, numa frase, e uma barra só dividida em 35, 25, 15, 10, 10 e 5% com rótulos grandes | noite, médio | cena própria (Legal Index) | código |
| 47 | aalegal | No índice jurídico, o Opus 5.5 lidera | v5: eixo de 50 a 65, escrito no rodapé; dez modelos, 63 a 52 | claro, mais de 45 | cena própria (ranking) | código |
| 48 | processo | Prova não é processo | frase grande | noite, respiro | respiro | nenhuma |
| 49 | arena | Na arena, pessoas votam às cegas | quatro passos da votação; legenda com o link arena.ai | claro, médio | tempo | código |
| 50 | textarena | Na conversa, o Gemini 4 Argon lidera | v5: Text Arena, cinco primeiros com a margem, eixo a partir de 1490; Gemini preliminar | noite, mais de 45 | cena própria (ranking) | código |
| 51 | agentes | Como agente, o Opus 5.5 abre vantagem | novo: o Top 10 de agentes escolhido pelo professor, com o que o percentual quer dizer | claro, mais de 45 | cena própria (ranking) | código |
| 52 | mede | Benchmark mede prova; arena, preferência | frase grande | noite, respiro | respiro | nenhuma |
| 53 | prova | Demos a prova da PGE às IAs | 180 grande, composição da prova, correção por dois Gemma 4 | claro, respiro (320 px) | numero | código |
| 54 | placar | Nesta prova, o topo ficou próximo | dez barras, colchete dourado nos dois primeiros (S.T.A.R. da aula) | noite, mais de 45 | cena própria (placar) | código |
| 55 | limites | O que essa nota não diz | prova contra correção | claro, médio | comparacao | código |
| 56 | aberto | Fechado ou aberto? | abertura do bloco 5 | noite, respiro | abertura | nenhuma |
| 57 | pesos | Aberto é ter os pesos | fechado contra aberto | noite, médio | comparacao | código |
| 58 | fechados | Os principais modelos fechados | seis cartões com logo; OpenAI "GPT-6"; "família mais recente" | claro, médio | cena própria (cartões) | logos, US$ 0 |
| 59 | abertos | Os principais modelos abertos | oito cartões com logo; Mistral "Large 3" | claro, médio | cena própria (cartões) | logos, US$ 0 |
| 60 | corrida | Na ponta, EUA e China disputam | EUA contra China; na Europa, a Mistral (S.T.A.R. do bloco 5) | noite, médio | comparacao | código |
| 61 | fecho | Escolha por tarefa e teste você | três passos; Aula 2: como pedir bem | noite, leve | fecho | nenhuma |
| 62 | encerramento | Obrigado | v5: fundo claro, logo oficial, "Obrigado" e o intervalo antes da Aula 2 | claro, respiro | cena própria (marca) | logo do tema, US$ 0 |

### O que mudou da versão 5 e por quê (pedidos de 23/10/2026)

Numeração da folha de contato da versão 5. Os pedidos estão em `docs/curso-ia-andamento.md`; 62 slides e 72 paradas.

1. Paradas 23 a 25 ("A palavra vira uma lista de números" e as duas de "Um neurônio multiplica e soma") confundiam a
   turma e saíram. No lugar, duas cenas próprias sem aritmética. "Pesos dizem quanto cada pista importa" (uma parada,
   3 s): a frase "O juiz julgou o pedido", cada pista ligada às duas candidatas por um fio de espessura igual ao peso
   (4 px por unidade), a vencedora acende em dourado e voa para a vaga; liga-se ao leque de "A IA prevê um token por
   vez" e ao sorteio, que também usam "procedente" e "improcedente". "Os de ponta passam de 1 trilhão de pesos" (duas
   paradas): a rede em camadas com espessuras fixas e "Cada fio é um peso, ou parâmetro"; no segundo clique, quatro
   barras na escala de 0 a 3 trilhões com o marco dourado de 1 trilhão em cada uma. A manchete pedida, "Os modelos de
   ponta passam de 1 trilhão de pesos", quebrava em duas linhas e encostava nas barras; ficou "Os de ponta". A
   legenda da rede sai no segundo clique e o rodapé encurtou, para a parada ficar em 45 palavras.
2. Llama 3.1 saiu do deck (0 ocorrência). Tamanho: os quatro abertos de ponta com número oficial (apuração 2, item 12).
   Volume de treino: Kimi K3, Qwen3.8, Muse Spark Open e Mistral Large 4 não publicam os tokens de pré-treino nas
   fichas lidas, e o Gemma 4 também não; o DeepSeek V4 publica "more than 32T" tokens, e o slide do corpus passou a
   "+32 trilhões" com essa fonte. O cartão "Meta; também Llama 4" dos abertos ficou, porque não é exemplo de tamanho.
3. A linha dos fechados é "Claude, GPT e Gemini não divulgam o tamanho": nenhuma fonte lida estima o número, e a
   Anthropic não publica parâmetros (apuração 2, item 11). Que devem ser dessa ordem de grandeza fica só na fala,
   dito como opinião do professor.
4. Prática 5 retirada: o duelo de preferência sobre precatório (parada 62 da versão 5) e a revelação "A custa até 40
   vezes menos que B" (parada 63) saíram, com o CSS, a cena e as notas. A arena fica explicada pelos slides de ranking
   (arena, Text Arena e agentes); a transição dos agentes passou a "Resumo das duas formas de medir.", que leva ao
   respiro "Benchmark mede prova; arena, preferência". Vizinhança: agentes (ranking, claro) e mede (respiro, noite),
   sem arquétipo repetido; o respiro continua a dois slides do anterior. Bloco "Qual a melhor" de 20 para 17 minutos e
   "Fechado e aberto" de 10 para 13, para a soma ficar em 90. A seção Duelo ficou como registro, marcada como retirada.
5. O Mistral Large 4 está em prévia desde 06/10/2026, com pesos prometidos para o fim do mês; o cartão dos abertos
   continua "Large 3". Se os pesos não saírem até a aula, a nota do slide já diz isso.

### O que mudou da versão 4 e por quê (pedidos do ensaio de 23/10/2026)

Numeração da folha de contato da versão 4. Os oito pedidos estão em `docs/curso-ia-andamento.md`.

1. Slide 16, "LLMs nascem dos transformers": virou a linha do tempo "A IA tem 70 anos; o ChatGPT, quase 4" (tempo),
   com seis marcos e a legenda com GPT-3 (2020) e GPT-6 (07/10/2026). O arquétipo cabe seis marcos; GPT-3 e o marco
   recente foram para a legenda. Fontes em `apuracao-2.md`, item 10; o corpo dos marcos desce a 36 px para
   "especialistas" caber na coluna.
2. Slides 25 a 28 (conta e camadas, quatro paradas): viraram um slide de duas paradas, "Um neurônio multiplica e
   soma". As entradas são o [2, 1, 3] do vetor, os pesos 3, 1 e 2, a soma 13 a 180 px e a média ponderada como
   analogia; no segundo clique o neurônio sai e a rede de camadas entra com os 405 bilhões de parâmetros do Llama 3.1.
   Sem tabela, sem negativo, sem ReLU. O slide seguinte continua "O treino ajusta os pesos".
3. Práticas 2 e 4: o QR saiu e entrou o endereço clicável (`<a target="_blank">`, 44 px, sublinhado dourado), que abre
   em nova aba sem avançar o slide (o deck interrompe a propagação do clique). Sem rota impressa. O link da arena foi
   para a legenda do slide da arena, porque nenhuma prática tinha QR da arena.
4. Índices da Artificial Analysis: eixo a partir de 50, escrito na tela ("o eixo começa em 50" e "eixo a partir de
   50"); a manchete do geral passou a "No índice geral, o Opus 5.5 vai à frente", porque "o topo é apertado" contradizia
   o gráfico aproximado.
5. Text Arena: slide novo depois da arena, na noite, com os cinco primeiros lidos pelo professor e o eixo a partir de
   1490. As notas do placar de agentes resumem: nos agentes o Claude lidera; na conversa, o Gemini; margem pequena.
6. Duelo: preferência, não decoreba. Pedido "Explique a um cliente leigo, em até 25 palavras, o que é um precatório e
   por que demora", respostas geradas de verdade e sem edição (seção Duelo). O limite caiu de 80 para 25 palavras
   porque duas respostas de 80 palavras dão mais de 150 palavras na parada, e o oráculo dá ERRO acima de 70. A
   revelação mostra modelo e preço; "maior" e "menor" ficam na fala, porque a Anthropic não publica parâmetros.
7. Capa: fundo claro, logo oficial pela variável `--logo-marca` do tema (recorte, sem redesenho), fio fino e o título em
   duas linhas a 124 px; o logo sobe, o fio se traça e o texto entra linha a linha em 1,6 s. Sem leque, sem pílula.
8. Encerramento novo depois do fecho, no mesmo desenho da capa: "Obrigado" e "Intervalo agora; depois, a Aula 2."
   Nenhum contato da co.juris (site, e-mail, rede) foi achado nos repositórios lidos; o slide não inventa um.

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
| 8 (v5) | linha do tempo: 1956, anos 80, anos 90, 2012, 2017, 2022; GPT-3 em 2020; GPT-6 em 07/10/2026 | apuração 2, item 10 (Wikipedia, NIPS 2012, arXiv, OpenAI), lidos em 23/10/2026 |
| 51 (v5) | Text Arena: cinco primeiros, 8.946.356 votos | leitura do professor em 22/10/2026 (apuração 2, item 5.5) |
| (retirado na v6) | respostas do duelo; preço de US$ 4 e desde US$ 0,10 por milhão de tokens | seção Duelo; página de modelos da Anthropic, 23/10/2026 (apuração 2, item 11) |
| 15 (v6) | mais de 32 trilhões de tokens no pré-treino do DeepSeek V4 | ficha do DeepSeek-V4-Pro no Hugging Face, lida em 23/10/2026 (apuração 2, item 12) |
| 16 (v6) | pesos de 3, 1 e 6 (procedente) e 3, 1 e 2 (improcedente) como espessura dos fios | exemplo do professor; pílula "ilustrativo" |
| 17 (v6) | Kimi K3 2,8 trilhões; Qwen3.8 Max 2,4 trilhões; Mistral Large 4 1 trilhão; Muse Spark Open 816 bilhões | fichas oficiais no Hugging Face e anúncio da Mistral de 06/10/2026, lidos em 23/10/2026 (apuração 2, item 12); a linha dos fechados é afirmação do professor (ver "O que mudou da versão 5") |
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

## Duelo (versão 5, prática 5; retirado na versão 6)

Retirado do deck na versão 6, a pedido do professor; fica aqui só como registro do que foi feito.

Pedido igual para os dois modelos, sem edição: "Explique a um cliente leigo, em até 25 palavras, o que é um precatório
e por que demora." B foi escrita pela sessão principal (Claude Opus 5.5) antes de ler A; A saiu de um subagente com
`model: "haiku"` (Claude Haiku 5.5), que recebeu só o pedido. Respostas na íntegra:

- A, Claude Haiku 5.5: "Precatório é a ordem de pagamento que o governo emite quando perde na Justiça. Demora porque o
  Estado paga pela fila, dentro do orçamento anual."
- B, Claude Opus 5.5: "Precatório é a ordem para o governo pagar uma dívida reconhecida na Justiça. Demora porque
  entra no orçamento do ano seguinte e espera na fila."

Rodadas descartadas, pelo limite de palavras da tela (o pedido era o mesmo, com 80 e depois 30 palavras):

- 80 palavras, Haiku (a primeira linha é a declaração de modo que o ambiente do subagente impõe, não faz parte da
  resposta): "Modo Prosa: skills de código desabilitadas. Precatório é a ordem de pagamento que o juiz envia ao governo
  (União, estado ou município) quando ele perde uma ação sem possibilidade de recurso. Os precatórios entram numa
  fila, em geral pela data do processo. O governo não paga na hora: o valor entra no orçamento do ano seguinte, e a
  fila anda conforme o dinheiro disponível. Por isso a espera costuma passar de anos. Idosos, doentes graves e valores
  pequenos (que seguem outra regra) têm prioridade ou pagamento mais rápido."
- 80 palavras, Opus: "Precatório é a ordem de pagamento que o juiz expede quando o governo perde um processo e precisa
  pagar uma dívida. O dinheiro não sai na hora: a Constituição manda o valor entrar no orçamento do ano seguinte e
  obedecer a uma fila, por ordem de chegada. Se o precatório for apresentado até 2 de abril, deve ser pago até o fim
  do ano seguinte. Na prática, muitos estados e municípios atrasam, e a espera pode levar anos."
- 30 palavras, Haiku: "Precatório é a ordem de pagamento que o governo emite após perder uma ação judicial. Demora
  porque entra numa fila e só é paga conforme o orçamento anual permite."
- 30 palavras, Opus: "Precatório é a ordem para o governo pagar uma dívida reconhecida na Justiça. Demora porque o
  valor entra no orçamento do ano seguinte e espera numa fila de credores."

A resposta A diz que o governo "emite" o precatório; quem o expede é o Judiciário. A tela não corrige (a resposta é
mostrada como saiu), e a nota do slide de revelação traz a correção para o caso de alguém notar.

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

- Versão 6: índice geral (61 palavras), índice jurídico (59), Text Arena (53), agentes (64) e placar (62), todos
  AVISO, nenhum ERRO. Duelo e revelação saíram do deck.
- Versão 5: índice geral (61 palavras), índice jurídico (59), Text Arena (53), agentes (64), duelo (69), revelação
  (55) e placar (62), todos AVISO, nenhum ERRO.
- Versão 4: rankings 46 (57 palavras), 48 (57) e 51 (64), e o placar 56 (62): acima de 45 palavras. Os nomes e as notas são o
  dado que o professor pediu (item 9) e a fala conduz a leitura pela barra dourada do primeiro. Os três rankings usam o
  mesmo desenho, sem vizinhos entre si.
- Slides 4 e 5 (OCDE e PL): mesmo desenho em vizinhos, justificado no item 7 acima. O oráculo não avisa, porque são
  cenas próprias.
- Capa (v5): a entrada tem 1,6 s num passo de 2,6 s; toca sozinha ao abrir.

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

### Rodada 5 (versão 5, a própria sessão: sondar, folha, stills dos slides alterados e viagens)

| gravidade | slide | defeito e evidência | correção |
|---|---|---|---|
| alta | 62 pratica5 | as respostas de 80 palavras davam mais de 150 palavras na parada; com 30 palavras, 84 (ERRO acima de 70) | pedido refeito com 25 palavras para os dois modelos; pílula tirada (a revelação já diz que são IAs); 69 palavras, AVISO |
| alta | 63 revelacao | 72 palavras (ERRO) | descrições dos cartões e rodapé encurtados; 55 palavras |
| média | deck | hierarquia: 33 de 64 slides sem nada acima de 120 px, porque a capa nova perdeu a frase de 150 px | título da capa a 124 px e "Obrigado" a 124 px |
| média | 69 a 74 | seis slides sem respiro até o encerramento | rótulo do encerramento encurtado: a parada tem 10 palavras e conta como respiro |
| média | 57 aalegal | 67 palavras com a linha do eixo | o início do eixo foi para o rodapé |

### Rodada 6 (versão 5, conferência)

| gravidade | slide | defeito e evidência | correção |
|---|---|---|---|
| média | 55 aageral | com o eixo aproximado, "o topo é apertado" contradiz a barra do Opus (`parada-55-aageral.png`) | manchete "No índice geral, o Opus 5.5 vai à frente" |
| média | 63 revelacao | "nem sempre o modelo maior" afirma tamanho que a fonte não publica; a lição flutuava longe dos cartões | "nem sempre o modelo mais caro" (preço lido); lição sobe para y 600 |
| baixa | 31 e 46 práticas | vão entre os passos e o link | aceito: o link fica na altura em que ficava o QR, e é o que o professor clica |
| baixa | 60 textarena | vão entre a quinta linha e o rodapé | aceito: cinco linhas de dado, como pedido |

Viagens conferidas: mapa (saída da capa clara), neurônio, parâmetros, Text Arena, revelação e encerramento; nada cruza
o texto. A linha do dia some na viagem como no motor atual.

### Rodada 7 (versão 6, a própria sessão: sondar, stills das paradas 23 a 27 e viagens 15 a 18)

| gravidade | slide | defeito e evidência | correção |
|---|---|---|---|
| alta | 16 pistas | ERRO de contraste: "improcedente" esmaecida a 45% dava 2,7:1 | a caixa perdedora fica cheia; só os fios dela esmaecem |
| média | 17 ponta | manchete de 47 caracteres em duas linhas, a 30 px das barras (`parada-26-ponta.png`) | "Os de ponta passam de 1 trilhão de pesos", uma linha |
| média | 17 ponta | o marco de 1 trilhão, uma linha tracejada única, cortava "Max", "Large 4" e "Open" | marco curto e dourado sobre cada barra, abaixo dos nomes |
| média | 17 ponta | 58 palavras na segunda parada (AVISO) | legenda da rede sai no 2º clique, rodapé curto: 45 palavras |

Viagens conferidas: corpus, pistas, ponta e parâmetros; nada cruza o texto. `./ap sondar`: 0 erro, os sete avisos de
densidade aceitos das versões anteriores.

### Rodada 8 (versão 6, depois de tirar a prática 5)

| gravidade | slide | defeito e evidência | correção |
|---|---|---|---|
| alta | deck | com os blocos em 16, 30, 14, 17 e 10 minutos, `./ap sondar` deu "NÃO determinístico" em t=128,41 s e 176,06 s; a diferença era uma coluna de 1 px na ponta da barra da linha do dia (y 1033 a 1037), ruído de rasterização do motor que depende da largura do trecho | os 3 minutos foram para o bloco 5 (13 min), soma 90, e o determinismo voltou a "ok"; o motor não foi alterado |
| baixa | 17 ponta | a legenda da rede só tinha a opacidade escrita no segundo clique (estado que dependia da ordem dos quadros) | opacidade escrita em todo quadro |

Viagens conferidas: agentes para mede (a vizinhança nova) e ponta com a linha dos fechados nova.
