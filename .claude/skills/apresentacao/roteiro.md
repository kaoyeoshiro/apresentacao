# Roteiro

O roteiro decide o deck antes de qualquer código: o arco, uma linha por slide e o arquétipo de cada uma. Fica no
`briefing.md`, e o usuário aprova antes do passo 5, porque manchete e texto da tela são o que o público vê.

## Arco

A abertura cria tensão (uma pergunta, um problema, um contraste com o que a plateia acha que sabe), três a cinco
movimentos desenvolvem a resposta, e o fecho entrega a mensagem e o pedido: o que a plateia faz agora. Num curso, cada
aula é um bloco com abertura própria, e a abertura de bloco vira capítulo (`andamento: 'capitulo'`, viagem de 2,2 s).

Cada bloco tem um S.T.A.R. e o resto fica quieto. S.T.A.R. é o momento que a plateia vai lembrar ("something they'll
always remember", na expressão de Nancy Duarte em *Resonate*, 2010), e ele explica a tese do bloco em vez de enfeitar.
Na prévia, o da Aula 1 é a data inventada (a IA escolhe uma data plausível sem o contrato), e o da Aula 2 são os papéis
que viram skill e pasta, até o fio da minuta responder à pergunta da Aula 1. Dois momentos fortes no mesmo bloco
disputam a memória; o segundo vira slide quieto.

Um slide por minuto e meio a dois de fala é o ponto de partida. No plano contínuo, cada clique abre um slide inteiro.

## Partitura de luz

O claro é a base e a noite marca o momento forte: abertura de capítulo, respiro, S.T.A.R. quando couber, demonstração
e fecho vão na noite (`class="noite"`); explicação, número e fonte ficam no claro. A densidade se mede em palavras da
parada final, nas faixas do oráculo: respiro (até 12 palavras), leve (13 a 24), médio (25 a 45). Acima de 45 o
oráculo avisa, e acima de 70 dá ERRO.

- Nunca três slides seguidos com o mesmo clima e a mesma faixa de palavras.
- Respiro depois de denso, e nunca mais de cinco slides seguidos sem respiro (parada de até 12 palavras ou um texto de
  200 px ou mais).
- Dois vizinhos nunca repetem o arquétipo.

As três regras são avisos do `./ap sondar`; resolvê-las no roteiro sai mais barato que no deck.

## Texto da tela

- Manchete afirma, em até oito palavras e uns 36 caracteres, para caber numa linha a 68 px: "A IA escreve uma palavra
  por vez", e não "Funcionamento da IA". O `.rotulo` acima dela nomeia o assunto ("Como funciona").
- No máximo 20 palavras por parada, contando tudo que está na tela.
- O dourado aponta uma coisa por parada: a palavra `.sinal`, a `.marca` do fio ou a barra que vence. Sobre o claro, o
  dourado entra como preenchimento (barra, faixa atrás da palavra), nunca como cor de texto miúdo.
- O ilustrativo leva a pílula "ilustrativo"; o que falta confirmar, `[CONFERIR]` na pílula. Número ilustrativo nunca
  vira número gigante: a escala de 320 px é para número apurado e datado.
- Um termo que a tela não apresentou não aparece na legenda (na prévia, "pesos abertos" virou "também rodam no
  escritório").
- Dados de slides diferentes conversam: na prévia, uma candidata do leque era a data verdadeira do contrato e
  desmentia a manchete "sem o contrato, a data é inventada". Releia o roteiro procurando contradições assim.

## Escolher o arquétipo

O arquétipo sai da função do slide no arco. O contrato de cada um, com a densidade máxima e um exemplo de HTML, está
na seção Arquétipos de `docs/cenas.md`; não duplique aqui.

| função no arco | arquétipo |
|---|---|
| abrir o deck ou um bloco | `abertura` (foto heroica sob véu e palavra-chave dourada) |
| mostrar que uma escolha sai de opções com peso | `escolha` (leque; com `data-sorteio`, o sorteio raso) |
| um número que a plateia deve lembrar | `numero` (grade corrigida a caneta, placar e barra) |
| duas versões lado a lado, antes e depois, teste cego | `comparacao` |
| o assunto se divide em dois caminhos | `ramos` (a trilha se divide) |
| pausa, frase que fecha uma parte | `respiro` |
| o pedido ao lado do material | `objetos` (recortes que podem viajar ao slide seguinte) |
| coisas que vão para um lugar | `viagem` (os objetos voam para uma árvore) |
| cada afirmação aponta para a sua fonte | `fios` |
| mostrar funcionando | `demonstracao`, com mergulhos no vídeo |
| a mensagem e o que fazer agora | `fecho` |

Quando nenhum serve, reescreva a função do slide antes de pensar em cena própria; quase sempre o slide estava tentando
provar duas coisas. A cena própria é exceção para o S.T.A.R. que nenhum arquétipo conta (passo 5 da skill).

## Modelo da tabela

Uma linha por slide, no `briefing.md`. As linhas abaixo são da prévia, com o arquétipo da biblioteca que faz cada uma
(o slide 9, skill, é cena própria e ficou de fora):

| # | slide | manchete | o que a tela prova | clima e densidade | arquétipo | mídia e custo |
|---|---|---|---|---|---|---|
| 1 | aula1 | O que é IA | abertura da Aula 1 | noite, respiro | abertura | heroica gerada 4K, US$ 0,113, mais rascunhos |
| 2 | palavra | A IA escreve uma palavra por vez | a frase cresce em duas rodadas de leque; a vencedora voa para a frase | claro, leve | escolha | código, US$ 0 |
| 3 | data | Sem o contrato, a data é inventada | leque raso, sorteio, data plausível sublinhada (S.T.A.R. da Aula 1) | noite, leve | escolha com `data-sorteio` | código |
| 4 | benchmark | Benchmark, a mesma prova com gabarito | a caneta corrige dez itens, 8 de 10 (ilustrativo) | claro, respiro | numero, `andamento: 'corte'` | código |
| 5 | arena | Arena, pessoas votam sem saber qual IA | A e B sem nome, B circulada | claro, leve | comparacao | código |
| 6 | mercado | Onde fica o dado do cliente | a trilha se divide entre o servidor de quem vende e o do escritório | claro, médio | ramos | código |
| 7 | aula2 | Prompt, contexto e skill | abertura da Aula 2 | noite, respiro | abertura (capítulo) | heroica 2K, US$ 0,0504 |
| 8 | prompt | Prompt é o pedido; contexto é o material | o pedido se digita ao lado de três papéis | claro, médio | objetos | três recortes 2K, US$ 0,15 |
| 10 | pasta | Os autos vão para a pasta do caso | os papéis voam para a árvore do caso | claro, médio | viagem | foto 2K, US$ 0,0504 |
| 11 | fonte | Cada linha aponta para um documento | os fios ligam a minuta às fontes; a data acende quando o fio chega | claro, médio | fios | código |
| 12 | demo | Funcionando, num caso fictício | o vídeo toca na moldura; dois mergulhos com holofote | noite, leve | demonstracao + 2 mergulhos | vídeo por código, US$ 0 |

Dois pontos dessa tabela ensinam. Palavra e data repetem o arquétipo escolha, e o oráculo avisa quando as sections
levam `data-arquetipo`; a repetição se defende porque a data é o S.T.A.R. e muda de clima, e um deck que a mantiver
escreve esse motivo no briefing. Prompt, skill, pasta e fonte são quatro telas claras e médias seguidas, e o oráculo
avisa também; num deck novo, uma delas iria para a noite ou viraria respiro.

## Lista de conferência

Antes de mostrar o roteiro ao usuário, confira:

1. O arco tem abertura com tensão, três a cinco movimentos e fecho com pedido.
2. Cada bloco tem um S.T.A.R. marcado na tabela, e só um.
3. Nenhum trecho de três slides tem o mesmo clima e a mesma densidade; nenhum trecho de seis slides fica sem respiro.
4. Nenhum par de vizinhos repete o arquétipo.
5. Cada manchete afirma, com até oito palavras e uns 36 caracteres.
6. Cada parada fica em até 20 palavras e respeita a densidade máxima do arquétipo em `docs/cenas.md`.
7. Metade dos slides ou mais tem imagem, número, diagrama ou vídeo como elemento dominante.
8. Cada dado tem fonte no briefing, `[CONFERIR]` ou pílula "ilustrativo".
9. A coluna mídia e custo soma o gasto previsto, e o que passa do teto do `./ap imagens` está marcado para perguntar.

O item que ficar de fora leva o motivo escrito no briefing, como o par palavra e data teria de levar.
