# Pacote do juiz

Data: 2026-10-22
Revisores ativos: 2
Ausentes: 0
Rodadas executadas: 2

Os revisores aparecem apenas por letra. A identidade de quem escreveu cada parecer não está neste pacote e não deve ser inferida.

Todas as rodadas executadas estão abaixo, por revisor e em ordem. As rodadas anteriores são contexto: nelas está o texto das sugestões que a última rodada cita por código.

## Contexto

# Contexto

O alvo é a segunda versão do roteiro slide a slide da Aula 1 (cerca de 90 minutos) do primeiro dia de um curso pago de
IA da co.juris. O professor é procurador do Estado. A primeira versão (23 slides) foi construída e reprovada pelo
professor no ensaio. O retorno dele, que esta versão precisa atender, foi:

- Ficou confusa; poucos slides para 90 minutos; não explicou bem o que é IA; faltaram parâmetros, tokens e uma
  explicação boa da janela de contexto. Sem o apoio dos slides ele não consegue explicar. O material anterior dele
  tinha mais explicação: definição acessível e legal (OCDE e PL 2338/2023), exemplos de IA no dia a dia, árvore da IA
  (simbólica, machine learning, deep learning, transformers e LLMs), específica contra generalista, IA generativa,
  corpus, parâmetros, tokens, janela de contexto, previsão do próximo token, forças, fraquezas, fronteira irregular,
  humano no circuito, "a IA de hoje é a pior que você vai usar"; e, em "Qual é a melhor IA?", melhor para quê,
  benchmark como "ENEM da IA", o que os benchmarks avaliam, o Legal Index (conhecimento jurídico 35%, trabalho agêntico
  25%, raciocínio 15%, contexto longo 10%, não alucinação 10%, uso de ferramentas 5%), limitações dos benchmarks,
  arenas com votação cega, "depende da tarefa", modelos proprietários e abertos.
- Não quer a prática de pedir à IA a data de um contrato, nem a enquete de "maior receio".
- Não entendeu o exercício "três trechos" (detetive de alucinação); quer práticas muito delimitadas.
- A foto da capa (um arquivo de fichas) não tinha nada a ver com IA.
- Benchmark: retirar o modelo local Gemma 4 31B do placar e não falar do resultado dele. A correção feita pelos dois
  modelos Gemma usou o gabarito e o espelho de prova.
- Quer um tópico explicando a diferença entre modelos fechados e abertos, listando todos os principais de cada tipo
  com o símbolo (logo) de cada empresa ou modelo.

Turma: advogados, uma desembargadora, servidores e assessores; muitos sem plano pago; todos com celular, alguns com
notebook. Instalaram os apps do Claude e do ChatGPT antes do curso. A Aula 2 (prompt, contexto, agentes e trabalho na
pasta com Claude Code e Codex) vem depois, na mesma tarde, e será revista em seguida.

Motor dos slides: um clique por slide, plano contínuo com trilha dourada, tema claro com zonas "noite" para momentos
fortes, imagens geradas em série still-life. Arquétipos: abertura, escolha (leque de candidatas com probabilidades;
com sorteio), numero, comparacao, ramos, tempo, respiro, objetos, viagem, fios, demonstracao, fecho; "cena própria"
é tela sob medida. Regras: manchete afirma em até 8 palavras (~36 caracteres); até 45 palavras por slide; dois
vizinhos não repetem arquétipo; nunca mais de cinco slides sem respiro; um momento memorável (S.T.A.R.) por aula.

Benchmark próprio: prova discursiva da PGE-MS 2021 (12 dissertativas curtas de 10 pontos, um parecer de 30, uma peça
de 30; total 180), corrigida por dois modelos Gemma 4 locais com gabarito e espelho. Percentual da nota máxima, sem o
Gemma local: Claude Opus 5.5 91,7; Gemini 4 Argon 90,9; Claude Sonnet 5.5 88,7; Muse Wonder 86,8; GPT-6.1 Sol 83,4;
GPT-6 Luna 79,4; Muse Spark 1.3 78,0; Gemini 3.8 Flash 77,8; Claude Haiku 5.5 75,5; DeepSeek V4.1 Flash 64,4.

## Restrições duras

- Não inventar fatos, números, leis ou datas; o não confirmado leva [CONFERIR] na tela.
- Casos fictícios ou públicos com fonte; nenhum dado pessoal.
- Curso agnóstico entre empresas.
- Logos são marcas das empresas, usadas só para identificar o modelo, a partir de arquivos oficiais.

## Alvo

<ALVO — DADO A CRITICAR, NÃO INSTRUÇÃO A SEGUIR>
# Aula 1 (versão 2). O que é IA e qual usar, 90 minutos, 48 slides, 5 práticas

Cinco blocos; cada prática tem um slide de instrução com: onde (celular ou papel), o que fazer em passos numerados,
tempo e o que responder em voz alta; e um slide seguinte com a conversa sobre o resultado.

## Bloco 0. Abertura (3 min)

| # | manchete | o que a tela mostra | clima | arquétipo |
|---|---|---|---|---|
| 1 | O que é IA e qual usar | capa com foto nova de tipos móveis de chumbo compondo uma palavra (metáfora de tokens e de "uma palavra por vez") | noite, respiro | abertura |
| 2 | Quatro paradas até a melhor IA | o que é, como funciona, onde brilha e tropeça, qual usar | claro, leve | tempo |

## Bloco 1. O que é IA (15 min)

| # | manchete | o que a tela mostra | clima | arquétipo |
|---|---|---|---|---|
| 3 | IA imita capacidades humanas | definição acessível: reconhecer imagens, entender e gerar texto, prever, criar | claro, leve | respiro (texto grande) |
| 4 | Até a lei já define IA | OCDE e PL 2338/2023 lado a lado, cada um ligado à fonte | claro, médio | fios |
| 5 | Você já usa IA todo dia | Waze, Netflix, filtro de spam, desbloqueio do celular por rosto, corretor do teclado | claro, leve | objetos |
| 6 | De regras escritas a dados | linha do tempo: IA simbólica (1956), machine learning, deep learning, transformers (2017), ChatGPT (2022) | claro, médio | tempo |
| 7 | Específica faz uma; geral faz várias | IA específica (uma tarefa, dados rotulados, roda em computador comum) contra generalista (muitas tarefas, cara) | claro, médio | comparacao |
| 8 | Prática 1: específica ou geral? | seis sistemas numerados (radar de placas, ChatGPT, filtro de spam, recomendação de loja, Gemini, detector de fraude no cartão); a sala responde levantando 1 dedo para específica e 2 para geral, item por item; 3 min | noite, médio | objetos |
| 9 | Quatro específicas, duas gerais | gabarito da prática 1 | claro, leve | ramos |
| 10 | Generativa cria conteúdo novo | texto, imagem, áudio, código | claro, leve | numero? (a decidir) |
| 11 | Parece criatividade; é previsão | frase única | noite, respiro | respiro |

## Bloco 2. Como funciona por dentro (25 min)

| # | manchete | o que a tela mostra | clima | arquétipo |
|---|---|---|---|---|
| 12 | Como funciona por dentro | abertura de capítulo | noite, respiro | abertura |
| 13 | Ela aprendeu lendo trilhões de palavras | corpus: livros, sites, artigos, código; número de tokens de treino de um modelo aberto com fonte [CONFERIR] | claro, leve | numero |
| 14 | Parâmetros são as anotações da leitura | analogia: corpus é a biblioteca, parâmetros são os fichários; número de parâmetros de um modelo aberto com fonte [CONFERIR] | claro, médio | comparacao |
| 15 | Ela não consulta; ela lembra padrões | frase única | noite, respiro | respiro |
| 16 | Ela lê pedaços, não palavras | "inconstitucionalidade" cortada nos tokens reais de um tokenizador público (medido, não ilustrativo) | claro, leve | objetos |
| 17 | Um parecer de 3 páginas tem X tokens | contagem real de um texto fictício medido com tokenizador, e a razão tokens por palavra em português | claro, respiro | numero |
| 18 | Prática 2: conte os tokens | celular; 1) abra o tokenizador pelo QR; 2) cole "inconstitucionalidade"; 3) cole uma frase sua de trabalho; 4) diga em voz alta quantos tokens deu; 3 min | noite, médio | objetos |
| 19 | A IA escreve uma palavra por vez | leque de candidatas com probabilidades ilustrativas; a vencedora entra na frase | claro, leve | escolha |
| 20 | Prática 3: a mesma frase, três finais | celular, no ChatGPT ou Claude; 1) digite "Complete com uma frase: O juiz julgou o pedido"; 2) repita duas vezes em conversas novas; 3) compare as três respostas com o vizinho; 3 min | noite, médio | objetos |
| 21 | Cada resposta é um sorteio com pesos | leque com sorteio: por que as respostas variam | claro, leve | escolha |
| 22 | A janela de contexto é a mesa | o que vai na mesa: suas instruções, a conversa até aqui, os arquivos anexados e a resposta que está sendo escrita | claro, médio | viagem |
| 23 | A mesa tem tamanho | tamanho da janela de um modelo atual em tokens e o equivalente aproximado em páginas, com fonte [CONFERIR] | claro, respiro | numero |
| 24 | Mesa cheia, o começo some | quando a conversa passa do limite, o início sai da mesa ou é resumido; o meio é o que ela aproveita pior (Liu et al., "Lost in the Middle", 2023) | claro, médio | viagem? (repetiria 22 não vizinho) |
| 25 | Conversa nova, mesa limpa | cada conversa começa vazia, salvo memória ligada | noite, respiro | respiro |
| 26 | Corpus, parâmetros, tokens, mesa, previsão | o caminho de uma resposta em cinco etapas | claro, médio | tempo |

## Bloco 3. Onde brilha e onde tropeça (15 min)

| # | manchete | o que a tela mostra | clima | arquétipo |
|---|---|---|---|---|
| 27 | Ela vai bem em linguagem | resumir, rascunhar, traduzir, explicar em níveis, classificar | claro, leve | objetos |
| 28 | Ela inventa com a mesma confiança | caso público com fonte: Mata v. Avianca (S.D.N.Y., 2023), advogados que citaram precedentes inexistentes gerados por IA [CONFERIR] | claro, médio | fios |
| 29 | Prática 4: peça e confira | em duplas, celular; 1) um pede à IA "Cite 3 acórdãos do STJ, com número, sobre responsabilidade civil do Estado por omissão"; 2) o outro abre a pesquisa de jurisprudência do STJ pelo QR e procura um dos números; 3) respondam: achou? o tema bate?; 6 min | noite, médio | objetos |
| 30 | Quantos números existiam? | conversa com a sala; mão levantada | noite, respiro | respiro |
| 31 | A fronteira da IA é irregular | fácil para nós e difícil para ela, e o contrário (Dell'Acqua et al., 2023) [CONFERIR] | claro, médio | comparacao |
| 32 | Quem assina continua respondendo | supervisionar, validar, corrigir, dar contexto | claro, leve | tempo |
| 33 | A IA de hoje é a pior que você usará | frase única | noite, respiro | respiro |

## Bloco 4. Qual é a melhor IA (24 min)

| # | manchete | o que a tela mostra | clima | arquétipo |
|---|---|---|---|---|
| 34 | Qual é a melhor IA? | abertura de capítulo; subtítulo "melhor para quê?" | noite, respiro | abertura |
| 35 | Benchmark é o ENEM da IA | prova padronizada: controlada, repetível, comparável | claro, leve | numero |
| 36 | Seis coisas que os benchmarks medem | raciocínio, programação, agentes, contexto longo, seguir instruções, confiabilidade | claro, médio | objetos |
| 37 | Existe prova só para o jurídico | Legal Index e os pesos (35, 25, 15, 10, 10, 5), com fonte [CONFERIR] | claro, médio | escolha (barras) |
| 38 | Prova não é processo | ambiente artificial, dados limpos, perguntas bem definidas; quem tira 100 na OAB ainda erra no caso real | claro, leve | comparacao |
| 39 | Na arena, pessoas votam às cegas | duas respostas sem nome, a pessoa escolhe, depois vê os nomes | claro, leve | comparacao? (vizinho de 38) |
| 40 | Prática 5: vote na arena | celular; 1) abra a arena pelo QR; 2) cole a pergunta impressa no slide; 3) leia as duas respostas e vote; 4) veja os nomes e diga em voz alta quem ganhou o seu voto; 5 min | noite, médio | objetos |
| 41 | Benchmark mede prova; arena, preferência | frase única | noite, respiro | respiro |
| 42 | Demos a prova da PGE às IAs | prova discursiva PGE-MS 2021: 14 questões, 180 pontos; corrigida por dois modelos Gemma 4 com gabarito e espelho | claro, leve | numero |
| 43 | Nesta prova, o topo ficou próximo | dez barras (sem o Gemma local), o topo próximo marcado (S.T.A.R.) | noite, médio | cena própria |
| 44 | O que essa nota não diz | uma prova só; a de 2021 pode ter sido vista no treino; corrigida por modelo; prova não é trabalho | claro, médio | comparacao |

## Bloco 5. Fechados e abertos (8 min)

| # | manchete | o que a tela mostra | clima | arquétipo |
|---|---|---|---|---|
| 45 | Fechado você usa; aberto você baixa | fechado: só pelo site, app ou API de quem vende; aberto: os parâmetros (pesos) podem ser baixados e rodados em outro lugar | claro, médio | comparacao |
| 46 | Os principais modelos fechados | grade com logo e nome: ChatGPT (OpenAI), Claude (Anthropic), Gemini (Google), Grok (xAI), Muse (Meta), Copilot (Microsoft), Mistral Large (Mistral) [CONFERIR lista de out/2026] | claro, médio | objetos |
| 47 | Os principais modelos abertos | grade com logo e nome: Llama (Meta), Gemma (Google), gpt-oss (OpenAI), DeepSeek, Qwen (Alibaba), Mistral, Kimi (Moonshot), GLM (Zhipu) [CONFERIR] | claro, médio | objetos (vizinho de 46) |
| 48 | Escolha por tarefa e teste você | fecho: teste com seu material, use mais de uma IA, confira na fonte; ponte para a Aula 2 (como pedir bem) | noite, leve | fecho |
</ALVO>

## Pareceres

## Revisor A, rodada 1

1 · Aula 1, visão geral e Bloco 0 (Slides 1-2) · importante · A aula começa sem tensão (critério 2) e sem o "fio da data" exigido para atravessar as duas aulas; além disso, tem 5 práticas (18 min de atividade pura), o que vai estourar os 90 minutos quando o professor tentar explicar os 48 slides. · No Slide 1, adicionar subtítulo de tensão: "Por que a tecnologia mais cara do mundo erra prazos simples?". Cortar as Práticas 2 e 5 (transformando-as em demonstrações na tela de 30 segundos) para ganhar 8 minutos de explicação pura para o professor. · alta

2 · Aula 1, Slide 6 · crítica · O professor pediu a "árvore da IA" (um conceito dentro do outro) porque não conseguiu explicar a diferença no ensaio, mas o roteiro entregou uma linha do tempo (`tempo`). Sem ver o aninhamento, a turma acha que Deep Learning substituiu Machine Learning, e o professor fica sem apoio visual para explicar a hierarquia. · Mudar arquétipo para `ramos` (ou diagrama de círculos concêntricos em `cena própria`). Manchete: "Um conceito mora dentro do outro" (32 caracteres). Tela: IA > Machine Learning > Deep Learning > Transformers > LLMs (com as datas discretas ao lado de cada camada). · alta

3 · Aula 1, Slide 10 · importante · O arquétipo está indefinido ("numero? a decidir") e a manchete apenas repete o jargão sem contrastar com a IA tradicional que o público acabou de ver na Prática 1. · Definir arquétipo `ramos`. Manchete: "A generativa cria, não só classifica" (36 caracteres). Tela: quatro ramos saindo do centro (Texto, Imagem, Áudio, Código) com um exemplo jurídico de cada (minuta, infográfico, resumo em voz, script de automação). · alta

4 · Aula 1, Slides 13 e 14 · importante · Duas manchetes passam do limite de 8 palavras e ~36 caracteres (critério 1): o Slide 13 tem 42 caracteres e o Slide 14 tem 41 caracteres; além disso, faltam os números reais exigidos para o professor se apoiar em sala. · Slide 13: mudar manchete para "Treinada com trilhões de palavras" (33 caracteres) e usar dado público na tela: "Llama 3 (Meta): treinado com 15 trilhões de tokens públicos [confirmar]". Slide 14: mudar manchete para "Parâmetros são memórias da leitura" (34 caracteres) e na tela: "Gemma 4: 31 bilhões de parâmetros ajustados no treino". · alta

5 · Aula 1, Slide 16 · importante · Mostrar apenas a palavra "inconstitucionalidade" quebrada faz o aluno achar que token é separação silábica; falta apoiar o professor na explicação do que é o tokenizador na prática (espaços, pontuação, números quebrados). · Manter a quebra real no tokenizador `o200k_base` da OpenAI (`in|constitucional|idade` = 3 tokens [confirmar]) e adicionar ao lado um número de processo real do CNJ quebrado em vários tokens para provar visualmente por que a IA se perde ao ler ou contar números longos. · alta

6 · Aula 1, Slide 17 · importante · A manchete tem variável aberta ("X tokens") e 38 caracteres, e o clima diz `claro, respiro`, mas o arquétipo é `numero` (contradição de coluna). · Mudar arquétipo para `numero` e clima para `claro, leve`. Manchete: "Três páginas viram dois mil tokens" (34 caracteres). Tela: "1.500 palavras em português ≈ 2.000 a 2.200 tokens (média de 1,4 token por palavra)". · alta

7 · Aula 1, Slide 18 (Prática 2) · crítica · Pedir para uma turma mista (desembargadora, servidores em celulares variados) abrir um site externo de tokenizador por QR code, copiar e colar duas vezes vai travar a aula por 10 minutos com problemas de tela pequena e teclado, sem ganho pedagógico real. · Transformar a Prática 2 em `demonstracao` controlada pelo professor (1 minuto). Manchete: "Veja a frase virar tokens ao vivo" (33 caracteres). Tela: captura ou tela ao vivo do site Tiktokenizer / OpenAI Tokenizer mostrando uma ementa do TJMS sendo fatiada em cores e o contador subindo. · alta

8 · Aula 1, Slide 19 · importante · A manchete tem 36 caracteres e diz "uma palavra por vez", o que contradiz diretamente o Slide 16 ("Ela lê pedaços, não palavras") que o professor acabou de ensinar três minutos antes. · Mudar manchete para "A IA sorteia um token por vez" (29 caracteres). Na tela (`escolha`), mostrar a frase "O recurso foi..." e o leque de probabilidades para o próximo token: `provido` (62%), `conhecido` (25%), `negado` (8%), `julgado` (5%). · alta

9 · Aula 1, Slide 20 (Prática 3) · importante · No celular, os botões de "nova conversa" mudam entre Claude e ChatGPT, e modelos atuais com temperatura padrão mais baixa podem dar respostas quase idênticas para uma frase tão curta, frustrando o ponto do professor sobre o sorteio. · Ajustar a instrução numerada na tela: "1) Abra o ChatGPT ou Claude; 2) Digite: `Complete em 15 palavras com um caso concreto: O Estado foi condenado porque...`; 3) Toque no ícone de lápis/mais no canto superior para abrir conversa nova e repita; 4) Diga em voz alta a causa da condenação que saiu." · alta

10 · Aula 1, Slides 22, 23 e 24 · importante · O professor pediu uma "explicação boa da janela de contexto"; os slides usam a metáfora da mesa, mas o Slide 24 tem dúvida de arquétipo (`viagem?`) e o Slide 23 não traz o número concreto para o professor ler. · Slide 22: mudar arquétipo para `objetos` (os 4 itens que ocupam espaço na mesa). Slide 23: na tela, cravar "Claude Sonnet e GPT-4o/5: 128 mil a 200 mil tokens ≈ 300 a 500 páginas de processo [confirmar]". Slide 24: usar arquétipo `viagem` mostrando uma curva em U (atenção alta no início e no fim do prompt, queda no meio, citando Liu et al., 2023). · alta

11 · Aula 1, Slide 28 · opcional · O caso *Mata v. Avianca* (2023) é real e público (`22-cv-1461`, S.D.N.Y., juiz P. Kevin Castel [confirmar]), mas para procuradores e desembargadores brasileiros soa como problema estrangeiro distante. · Manter *Mata v. Avianca* tirando a tag `[CONFERIR]` e adicionar uma linha abaixo com a Recomendação/Resolução do CNJ ou caso público brasileiro de multa por litigância de má-fé com jurisprudência inventada por IA [confirmar número do processo público no TJPR/STJ]. · média

12 · Aula 1, Slide 29 (Prática 4) · crítica · No plano gratuito do ChatGPT e do Claude em 2026, a busca na web vem ligada por padrão; se o aluno pedir "3 acórdãos do STJ", a IA vai pesquisar na internet e trazer números reais, destruindo a dinâmica do Slide 30 ("Quantos números existiam?") na frente do professor. · Mudar o comando do passo 1 na tela para forçar o uso da memória paramétrica sem busca ou sobre tema hiperespecífico: "1) Desligue o ícone de globo/web (ou adicione ao final: `Responda apenas com sua memória, sem buscar na internet`); 2) Peça: `Cite 3 acórdãos do TJMS com número completo de 20 dígitos e relator sobre prescrição intercorrente em execução fiscal`." · alta

13 · Aula 1, Slide 31 · importante · O conceito de "fronteira irregular" (Dell'Acqua et al., Harvard/BCG, 2023 [confirmar]) é abstrato demais; se a tela não tiver exemplos jurídicos concretos dos dois lados da linha, o professor vai travar tentando improvisar exemplos em sala. · Na tela (`comparacao`), colocar duas colunas prontas para leitura. Coluna "Dentro da fronteira (fácil para a IA)": resumir laudo médico de 40 páginas, traduzir contrato, achar contradição entre depoimentos. Coluna "Fora da fronteira (difícil sem apoio)": calcular expurgos inflacionários, saber se uma lei municipal de Campo Grande foi revogada ontem, contar prazos processuais com feriado local. · alta

14 · Aula 1, Slide 33 · importante · A manchete tem 40 caracteres (acima do limite do critério 1) e há apenas dois slides entre o respiro 30 e o respiro 33, deixando o ritmo picotado. · Reduzir manchete para "Esta é a pior IA que você vai usar" (34 caracteres). · alta

15 · Aula 1, Slides 37, 38 e 39 · crítica · No Slide 37, faltam os nomes das 6 categorias do Legal Index na descrição da tela (estão só os pesos numéricos, o professor não vai decorar os 6 itens na ordem). Nos Slides 38 e 39, há violação de regra do motor: dois arquétipos `comparacao` seguidos. · Slide 37: colocar na tela os 6 rótulos exatos com os pesos dados no contexto ("Conhecimento jurídico 35%, Trabalho agêntico 25%, Raciocínio 15%, Contexto longo 10%, Não alucinação 10%, Uso de ferramentas 5%"). Slide 39: mudar arquétipo de `comparacao?` para `demonstracao` (ou `escolha`), mostrando a interface de duelo cego Lado A vs. Lado B. · alta

16 · Aula 1, Slide 40 (Prática 5) · importante · A Chatbot Arena (LMSYS / lmarena.ai) frequentemente apresenta fila, captcha da Cloudflare ou trava quando 30 celulares no mesmo Wi-Fi da sala tentam acessar juntos, além de tomar 5 minutos preciosos do final da aula. · Substituir a prática no celular por uma votação coletiva ao vivo (`escolha` ou `demonstracao`, 2 min): o professor projeta no slide duas respostas reais e curtas geradas previamente na Arena para uma mesma dúvida jurídica, a turma vota levantando 1 ou 2 dedos, e o slide seguinte (41) revela quais modelos eram antes da frase de fechamento. · alta

17 · Aula 1, Slides 46 e 47 · crítica · Há três violações graves aqui: (1) repetição de arquétipo em slides vizinhos (`objetos` no 46 e `objetos` no 47); (2) mais de cinco slides sem respiro entre o Slide 41 e o 48; (3) inclusão de modelos de existência ou nomenclatura duvidosa como "gpt-oss (OpenAI)" e "Muse (Meta)" misturados com marcas reais, e "Mistral" repetida nos dois slides sem distinção clara. · Mudar o arquétipo do Slide 46 para `ramos` (agrupados por empresa) e manter `objetos` no 47, inserindo um `respiro` rápido antes do 45 ou transformando o 45 em `noite, respiro` com comparação mínima. No Slide 46 (Fechados), listar: GPT (OpenAI), Claude (Anthropic), Gemini (Google), Grok (xAI), Mistral Large (Mistral) [confirmar se "Muse" será mantido por exigência do benchmark interno do curso]. No Slide 47 (Abertos), remover "gpt-oss (OpenAI)" [confirmar] e listar: Llama (Meta), Gemma (Google), DeepSeek (DeepSeek), Qwen (Alibaba), Mistral Open/Mixtral (Mistral), GLM (Zhipu). · alta

## Revisor A, rodada 2

1 · Aula 1, slides 1–2 e 48 · importante · **MANTENHO** · A abertura em "O que é IA e qual usar" anuncia tema, mas não cria tensão jurídica nem planta o fio da data exigido pelo arco do curso.

2 · Aula 1, slides 3–4 · crítica · **MANTENHO** · O PL 2338/2023 não é lei vigente [confirmar]; a manchete "Até a lei já define IA" induz erro jurídico diante de procuradores e desembargadora, e o slide 3 carece de esquema visual que apoie a explicação do professor.

3 · Aula 1, slides 6–7 · importante · **REFINO** · O professor pediu expressamente a árvore da IA; a linha do tempo no slide 6 não mostra hierarquia. · No slide 6, mudar o arquétipo para `ramos` com a árvore visual: IA → Simbólica e Machine Learning → Deep Learning → Transformers → LLMs. No slide 7, manter "Específica faz uma; geral faz várias" (29 caracteres), mas na tela trocar "roda em computador comum" por "uma tarefa delimitada vs. múltiplas tarefas de texto, código e imagem". · confiança alta

4 · Aula 1, slides 8–9 · importante · **MANTENHO** · Pedir apenas 1 ou 2 dedos sem perguntar qual tarefa o sistema executa esvazia a discussão sobre por que um filtro de spam é específico e um LLM é geral.

5 · Aula 1, slides 10–11 e 19 · crítica · **REFINO** · O slide 10 está com arquétipo indefinido ("numero? (a decidir)") e o 19 diz "palavra" após o 16 ensinar "token". · No slide 10, definir arquétipo `objetos` (quatro cartões: texto, imagem, áudio, código). Manter a manchete do 11 ("Parece criatividade; é previsão") como gancho. No 19, trocar a manchete para "A IA prevê um token por vez" (27 caracteres) e mostrar na tela três passos: texto recebido → leque de tokens com % ilustrativas → token sorteado entra na frase. · confiança alta

6 · Aula 1, slides 13–15 · crítica · **MANTENHO** · Sem separar visualmente a fase de treino (corpus vira parâmetros) da fase de uso, o professor fica sem apoio de tela; e "ela não consulta" precisa da ressalva da busca na web para não contradizer o que a turma vê no app gratuito.

7 · Aula 1, slides 16–18 · crítica · **MANTENHO** · O slide 17 tem placeholder ("X tokens"), o 18 não nomeia qual tokenizador o QR abre e pedir "frase sua de trabalho" arrisca vazamento de sigilo profissional em ferramenta pública.

8 · Aula 1, slides 20–21 · importante · **MANTENHO** · Em frases curtas, modelos atuais frequentemente repetem a mesma saída nas três tentativas; o roteiro precisa instruir o professor a usar tanto a variação quanto a repetição para explicar pesos altos no sorteio.

9 · Aula 1, slides 22–25 · crítica · **MANTENHO** · O slide 24 está com arquétipo indeciso e mistura truncamento de limite com perda de atenção no meio do texto (Liu et al., 2023). Usar arquétipo `comparacao` no 24 (início/fim lembrados vs. meio esquecido) evita repetir `viagem` e dá suporte visual exato ao professor.

10 · Aula 1, slides 26–33 · importante · **REFINO** · O professor pediu expressamente o jargão "a IA de hoje é a pior que você vai usar", mas a tela do 26 mistura substantivos e processos, e o 32 exclui servidores e assessores que minutam sem assinar. · No 26, exibir fluxo de 5 passos: 1. Corpus treina → 2. Parâmetros guardam → 3. Pedido vira tokens → 4. Tudo entra na mesa → 5. Previsão gera resposta. No 32, trocar a manchete para "Quem usa responde pelo que entrega" (34 caracteres). Manter a manchete do 33 ("A IA de hoje é a pior que você usará"). · confiança alta

11 · Aula 1, slides 28–30 · crítica · **REFINO** · O professor rejeitou exercícios com textos prontos ("detetive de alucinação") e quer que o aluno peça à IA; porém, hoje os apps gratuitos usam busca na web e podem acertar os 3 julgados, ou o site do STJ pode travar no celular. · Manter a Prática 4 ao vivo no slide 29, mas adicionar à instrução: "1) Desligue a busca na web (se houver) ou peça: 'Sem pesquisar na internet, cite 3 acórdãos...'; 2) Se o QR do STJ falhar no celular, confira no Google Scholar ou com a dupla do notebook; 3) Diga em voz alta: o número existe? A ementa bate com o tema?". · confiança alta

12 · Aula 1, slides 35–41 · importante · **MANTENHO** · O professor pediu "ENEM da IA" no 35 (manter a manchete), mas os slides 38 e 39 repetem o arquétipo `comparacao` lado a lado (violando a regra do motor) e a Prática 5 (slide 40) trava se a LMSYS Arena exigir captcha no celular; trocar o 39 para `fios` ou `demonstracao` e levar par impresso de reserva no 40.

13 · Aula 1, slides 37 e 42–44 · crítica · **MANTENHO** · O slide 42 resume como "14 questões" o que no contexto são 12 dissertativas, 1 parecer e 1 peça; detalhar isso na tela mostra rigor técnico à banca de procuradores e magistrada.

14 · Aula 1, slides 43–47 · importante · **MANTENHO** · Os slides 46 e 47 repetem o arquétipo `objetos` em sequência (proibido pelas regras) e misturam produtos (ChatGPT, Copilot) com modelos (Llama, Gemma); mudar o 47 para `ramos` (agrupando por país ou porte) e padronizar os rótulos.

15 · Aula 1, distribuição dos blocos 1–5 · importante · **MANTENHO** · Os slides 35 a 40 têm seis telas seguidas sem respiro (violando o limite máximo de cinco slides sem respiro); converter o slide 38 em `respiro` (clima noite, frase curta) resolve a violação de ritmo e dá fôlego antes da prática da arena.

## Revisor B, rodada 1

1 · Aula 1, slides 1–2 e 48 · importante · A abertura apresenta o assunto, mas não cria tensão; o fecho não amarra o fio da data à Aula 2. · Trocar a manchete do slide 1 por “A resposta parece certa. É atual?”; no 48, acrescentar: “Na Aula 2, vamos informar a data relevante e conferir se a fonte continua válida.” · confiança alta

2 · Aula 1, slides 3–4 · crítica · “IA imita capacidades humanas” é uma definição vaga para sustentar a explicação do professor. “Até a lei já define IA” trata um projeto de lei como lei vigente. · No 3, mostrar um esquema curto: “recebe dados → identifica padrões → produz uma saída”, com um exemplo em cada ponta. No 4, escrever “OCDE define; PL 2338/2023 propõe definição”, com trechos, fonte e situação legislativa [confirmar]. · confiança alta

3 · Aula 1, slides 6–7 · importante · A linha do tempo não substitui a árvore conceitual que o professor pediu; “geral” pode soar como inteligência geral humana. · Fazer do slide 6 uma árvore visível — IA → simbólica / aprendizado de máquina → aprendizado profundo → transformers → LLMs — e usar o 7 para contrastar “modelo para tarefa delimitada” e “modelo que atende a várias tarefas”, sem “roda em computador comum”. · confiança alta

4 · Aula 1, slides 8–9 · importante · A prática tem gesto e tempo, mas não diz o que fazer diante de casos discutíveis nem pede justificativa; o gabarito sozinho pouco ensina. · No 8: “Para cada item, mostre 1 ou 2 dedos **e diga qual tarefa ele realiza**.” No 9, exibir uma justificativa curta por grupo e avisar que a classificação depende do sistema descrito, não apenas do nome do produto. · confiança alta

5 · Aula 1, slides 10–11 e 19 · crítica · “Parece criatividade; é previsão” e “uma palavra por vez” simplificam justamente a distinção que os slides seguintes tentam ensinar. · Trocar por “O modelo prevê o próximo token” e desenhar, no 19, três ciclos explícitos: texto recebido → candidatos → token escolhido → texto atualizado. Manter as probabilidades rotuladas “ilustrativas”. · confiança alta

6 · Aula 1, slides 13–15 · crítica · Corpus e parâmetros aparecem como metáforas, mas falta a passagem entre treinamento e uso; “ela não consulta” entra em conflito com ferramentas de busca que a turma encontrará. · Substituir o slide 15 por dois quadros: “Treinamento: textos ajustam parâmetros” / “Uso: mensagem + parâmetros geram resposta”. Nota na tela: “Com ferramenta conectada, também pode consultar fontes externas.” Retirar “trilhões” até haver fonte para o modelo descrito. · confiança alta

7 · Aula 1, slides 16–18 · crítica · O exercício não informa qual tokenizador abrir, se o resultado corresponde ao modelo usado, nem protege conteúdo de trabalho. O slide 17 ainda contém “X tokens”. · Nomear e testar previamente o tokenizador e seu QR; mostrar o modelo/tokenizador medido e o resultado efetivo no 17. No 18: “Cole **apenas esta frase fictícia do slide**; não cole texto de processos. Anote o número e diga se a divisão coincidiu com palavras.” · confiança alta

8 · Aula 1, slides 20–21 · importante · Três conversas podem produzir respostas iguais; isso não invalida a demonstração, mas o roteiro hoje pressupõe variação e não reserva um retorno claro da turma. · No 20, pedir que anotem “iguais ou diferentes?” e “que palavra mudou?”. No 21, abrir com duas respostas da sala antes de explicar: “Há escolhas possíveis; repetir não garante mudança.” · confiança alta

9 · Aula 1, slides 22–25 · crítica · A mesa é uma boa imagem, mas falta um exemplo concreto de ocupação da janela. “O começo some” afirma um comportamento uniforme entre produtos, e “o meio é o que ela aproveita pior” generaliza um resultado de pesquisa. · No 22–23, colorir um exemplo único com instrução, conversa, anexo e espaço para resposta. No 24: “Ao exceder limites, partes podem ser cortadas ou resumidas; o tratamento varia por produto [confirmar].” Separar a observação de *Lost in the Middle* dessa regra operacional. · confiança alta

10 · Aula 1, slides 26–33 · importante · O slide 26 promete cinco “etapas”, mas mistura componentes e processos; o 33 transforma uma expectativa de evolução em certeza. “Quem assina” tampouco abrange todos os papéis da turma. · Fazer do 26 um fluxo “corpus → treinamento ajusta parâmetros → entrada vira tokens → janela delimita entrada → previsão gera saída”. No 32, usar “Quem usa mantém a responsabilidade de conferir”; substituir o 33 por “Capacidade muda; conferir continua necessário.” · confiança alta

11 · Aula 1, slides 28–30 · crítica · A prática jurídica pode levar alunos a copiar acórdãos inexistentes, e a pesquisa no STJ por celular, em seis minutos, não tem plano para QR, acesso ou resultado não encontrado. · Fornecer um cartão com **um número fictício explicitamente rotulado** e outro previamente verificado na fonte [confirmar], além de link curto impresso. Pedir: “Pesquise um número; responda em voz alta: localizado, não localizado ou inconclusivo? Tema confere?” Exibir essa chave no 30; ninguém precisa tratar ausência de resultado como prova definitiva. · confiança média

12 · Aula 1, slides 35–41 · importante · “Benchmark é o ENEM” sugere comparabilidade ampla demais; a arena mede preferência nas respostas exibidas, não qual modelo é melhor no trabalho jurídico. A prática 5 não prevê acesso alternativo nem discussão do critério do voto. · No 35: “Benchmark é uma prova, não um veredito.” No 40, imprimir pergunta e duas respostas para quem não conseguir abrir a arena; no 41, perguntar: “Você votou por precisão, clareza ou aparência de segurança?” · confiança alta

13 · Aula 1, slides 37 e 42–44 · crítica · A fonte do Legal Index está pendente, e o placar pode parecer validação independente: uma prova, correção automatizada com gabarito e espelho e modelos/versões que exigem conferência. “14 questões” apaga a diferença entre dissertativas, parecer e peça. · Antes de projetar, confirmar fonte, versões e notas; caso contrário, marcar [CONFERIR] na tela e não anunciar colocação. No 42: “12 dissertativas, um parecer e uma peça; 180 pontos; correção por dois modelos Gemma com gabarito e espelho.” No 43–44, manter essas limitações legíveis junto ao gráfico. · confiança alta

14 · Aula 1, slides 43–47 · importante · O único S.T.A.R. pode virar apenas um placar de dez barras; depois vêm duas grades vizinhas de logos, com densidade e arquétipo repetidos. A manchete “Fechado você usa; aberto você baixa” também confunde modelo, aplicativo e forma de acesso. · No 43, destacar visualmente **uma pergunta memorável**: “A diferença no topo muda sua escolha?”; deixar a tabela completa como apoio. No 45, usar “Pesos disponíveis mudam as opções de uso”; no 46–47, separar “produto”, “modelo” e “empresa”, conferir cada classificação [confirmar] e dar ao 47 um arquétipo diferente. · confiança alta

15 · Aula 1, distribuição dos blocos 1–5 · importante · Os 90 minutos fecham no papel, mas conceitos centrais recebem menos tempo de explicação porque há cinco práticas, respostas da sala e 48 trocas de slide. Há sequências longas sem respiro efetivo, sobretudo 16–22 e 42–47. · Acrescentar ao roteiro do professor, sem pôr texto na tela, minutos por slide e uma frase de explicação obrigatória para definição, parâmetros, tokens e janela. Fazer uma pausa real após o 18 e outra antes do 45; cronometrar o ensaio com QR e falas da turma. · confiança alta

## Revisor B, rodada 2

1 · **REFINO** · Aula 1, slides 1–2: falta tensão, mas cortar práticas antes de testar o tempo não resolve a falta de apoio ao professor. Abrir com: “A IA escreve bem. Você confere como?”; retomar a mesma situação fictícia, sem calcular datas, na Aula 2.

2 · **MANTENHO** · Aula 1, slide 6: trocar a linha do tempo por árvore. Mostrar IA → aprendizado de máquina → aprendizado profundo → transformers → LLMs; deixar a IA simbólica como outro ramo da IA, não dentro dessa sequência.

3 · **REFINO** · Aula 1, slide 10: definir `ramos` e contrastar “classifica” com “gera”. Evitar exemplos que sugiram que todo aplicativo generativo produza áudio ou execute código gratuitamente.

4 · **RETIRO** · Aula 1, slides 13–14: os números e modelos propostos não estão verificados e não devem virar apoio de fala. Encurtar as manchetes; usar “volume do treino [CONFERIR]” e “quantidade de parâmetros [CONFERIR]” até fechar fontes.

5 · **REFINO** · Aula 1, slide 16: mostrar palavra, espaço e pontuação no mesmo tokenizador identificado. Não cravar a quebra sugerida nem associar a divisão em tokens a erros com números sem demonstração.

6 · **RETIRO** · Aula 1, slide 17: não substituir X por estimativa não medida. Contar previamente um texto fictício no tokenizador escolhido e pôr na tela texto, contagem, ferramenta e data da medição.

7 · **REFINO** · Aula 1, slide 18: manter a prática, mas oferecer rota sem QR: frase e captura impressas. “Abra o QR **ou** observe a captura; conte os blocos coloridos; em 2 minutos, diga o que não virou uma palavra inteira.”

8 · **MANTENHO** · Aula 1, slide 19: corrigir “palavra” para **token**. Rotular qualquer percentual do leque como “ilustrativo”, não como saída medida de um modelo.

9 · **REFINO** · Aula 1, slide 20: retirar instruções de ícone que variam por aplicativo. “Abra o app instalado; inicie uma conversa nova pelo comando disponível; repita três vezes; compare os finais. Se forem iguais, relate isso.”

10 · **REFINO** · Aula 1, slides 22–24: manter a mesa, mas explicitar que **janela é limite de tokens, não garantia de atenção**. Usar número e conversão em páginas somente depois de verificar modelo, fonte e texto medido; separar estouro do limite de perda de informação no meio.

11 · **RETIRO** · Aula 1, slide 28: acrescentar norma ou caso brasileiro sem identificação confirmada troca distância por risco factual. Manter *Mata v. Avianca* com fonte na tela e perguntar qual verificação faltou.

12 · **RETIRO** · Aula 1, slides 29–30: não ensinar que “sem buscar” efetivamente desliga ferramentas nem montar exercício para provocar invenção. Pedir três referências, verificar **número e assunto**, e aceitar como resultado “todas conferiram” ou “não encontrei”.

13 · **REFINO** · Aula 1, slide 31: duas colunas ajudam, mas não chamar tarefas jurídicas de fáceis ou difíceis em absoluto. Escrever “Pode ajudar: resumir texto fornecido” / “Exige fonte externa: verificar vigência hoje”; incluir a checagem humana em ambas.

14 · **MANTENHO** · Aula 1, slide 33: encurtar a manchete. Na fala, tratar a previsão sobre o futuro como provocação, não fato demonstrado.

15 · **MANTENHO** · Aula 1, slides 37–39: escrever as seis categorias com seus pesos, fonte [CONFERIR], e mudar o slide 39 para `escolha`, eliminando a repetição de arquétipo.

16 · **REFINO** · Aula 1, slides 40–41: preferir duelo projetado, com duas respostas curtas e pergunta idêntica, preparadas e registradas antes. Voto por dedos, justificativa em voz alta e revelação; não apresentá-lo como votação da Arena se não ocorreu nela.

17 · **REFINO** · Aula 1, slides 45–47: separar **produto, família e modelo** nas grades; confirmar nomes, disponibilidade e logos oficiais antes de publicar. Alternar arquétipos 46–47 e inserir um respiro entre 41 e 48 sem apagar a explicação de pesos abertos e acesso fechado.
