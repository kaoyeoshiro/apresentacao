# Curso de IA da co.juris: andamento (passagem para o próximo agente)

Atualizado em 23/10/2026. Branch `claude/briefing-dia-1`, no worktree
`/Volumes/Projetos/apresentacao/.claude/worktrees/ia-course-presentations-c2018d`. Nada foi juntado ao `main` nem
publicado. Ideias para depois ficam em `docs/curso-ia-ideias.md`.

## O que é

Dia 1 de um curso pago de IA (turma mista: advogados, uma desembargadora, servidores, assessores; muitos sem plano
pago). Duas aulas de ~90 min na mesma tarde, tema `cojuris`, plano contínuo. Siga a skill
`.claude/skills/apresentacao/SKILL.md`.

- Aula 1, "O que é IA e qual usar": `decks/curso-ia-aula1/` (briefing, deck de 61 slides da versão 7, `apuracao.md` e
  `apuracao-2.md`).
- Aula 2, "Do chat à pasta": `decks/curso-ia-aula2/briefing.md` aprovado em 22/10, mas ainda com o fio da data do
  contrato, que o professor rejeitou na Aula 1; rever antes de montar. O deck ainda é a cópia do catálogo.

## Decisões do professor que valem

- Curso agnóstico (Claude e ChatGPT/Codex); levar a turma a trabalhar num agente na pasta; Claude ao vivo na demo.
- Sem a prática da data do contrato, sem enquete de "maior receio".
- Benchmark da PGE-MS 2021: dez barras, sem o Gemma 4 31B local; a correção foi por dois Gemma 4 com gabarito e
  espelho de prova.
- Zero `[CONFERIR]` na tela: confirmar em fonte ou reescrever o trecho.
- Conselhos (`/council`): rodar direto, sem pedir sim, só com Gemini 4 Argon e GPT-6 Sol; juiz Opus.
- Imagens só pelo `./ap imagens`, teto US$ 2,00; quem escolhe o rascunho é o professor. Gasto até aqui: US$ 0,25.

## Pedidos do ensaio da versão 3 (22/10): feitos na versão 4 (23/10)

Todos os 11 entraram em `decks/curso-ia-aula1/deck.html` (63 slides); o que mudou em cada um está no `briefing.md`
do deck, seção "O que mudou da versão 3".

1. [feito] Pesos e matrizes: slides 16 a 18 (vetor, conta em dois cliques, filtro e camadas) e 19 (o treino ajusta).
2. [feito] Capa por código, com `autoplay: true`: a frase em 150 px, o leque grande e o título no fim.
3. [feito] Zero `[CONFERIR]` no deck e no briefing, pela seção 0 de `apuracao-2.md`.
4. [feito] Mesa desenhada por código; "meio se perde" trocado por "Quanto maior o texto, mais o acerto cai" (NoLiMa,
   Chroma, Anthropic). `mesa.webp` e os `doc-*.webp` saíram do deck e do crédito.
5. [feito] Notas `{diga, faca, transicao}` nos 63 slides; `pratica` nas cinco práticas.
6. [feito] Linha do dia com cinco blocos (16, 30, 14, 20 e 10 minutos).
7. [feito] OCDE e PL 2338/2023 em cinco partes cada, um clique por parte.
8. [feito] Fronteira serrilhada desenhada, seis exemplos do professor e o número do estudo publicado.
9. [feito] Índice geral, Legal Index refeito (barra única), ranking jurídico e ranking de agentes da arena.ai.
10. [feito] Duelo do prazo de contestação do Estado, com revelação pelo CPC; respostas escritas pelo professor (proposta
    de `apuracao-2.md`, item 0.1), sem gerar respostas por IA.
11. [feito] Três slides de memória depois de "Conversa nova, mesa limpa".

Pontos para o professor decidir no ensaio: o índice geral mostra 7 modelos (os distintos entre as 10 primeiras linhas
da tabela, que repete variantes do mesmo modelo); o rodapé dos agentes usa as 367.936.358 sessões da captura, enquanto
o placar de agentes mostra 2.731.078 sessões em 20/10/2026 (a nota do slide diz isso).

Pendência do motor, achada na crítica e fora do escopo do deck: durante as viagens de câmera, a trilha passa por
cima dos nomes da linha do dia por cerca de 0,3 s. Conserto proposto em `motor/palco.js`: esmaecer a linha do dia
durante a viagem ou descer os nomes para y ≥ 1015.

## Próximo passo

1. Ensaio da versão 5 com `./ap abrir decks/curso-ia-aula1` (tela do apresentador com P); conferir os links com
   internet; pedidos voltam ao passo 5 da skill.
2. Depois, a Aula 2 (`decks/curso-ia-aula2`): rever o briefing (tirar o fio da data do contrato) e montar com os
   mesmos recursos (blocos, guia, práticas).
3. Antes de juntar ao `main`: bateria completa (`./ap teste`), autorrevisão por subagente e o "posso juntar?".

## Decisão de 22/10/2026: ranking da arena na Aula 1

O professor mandou captura da página inicial da arena.ai, quadro "Top 10 Agents · Best Overall" (367.936.358 sessões
no total), e pediu para usar esse ranking geral, em que o Claude lidera:

| # | modelo | valor mostrado |
|---|---|---|
| 1 | Claude Opus 5.5 (Max) | 20,92% |
| 2 | GPT-6 Astra (Max) | 14,70% |
| 3 | Claude Fable 5.1 (Max) | 14,17% |
| 4 | GPT-6.1 Sol (Max) | 13,55% |
| 5 | Claude Sonnet 5.5 (Max) | 12,67% |
| 6 | Gemini 4 Argon (High) | 12,03% |
| 7 | Muse Wonder Full (Max) | 11,26% |
| 8 | GPT-6 Sol (Max) | 9,36% |
| 9 | Claude Fable 5 (High) | 8,31% |
| 10 | Claude Opus 5 (Max) | 8,09% |

Fonte: arena.ai, página inicial, captura do professor de 22/10/2026. Antes de pôr o percentual na tela, abrir a
página e ler o que ele significa (a captura não diz); se não houver explicação, mostrar só a ordem e escrever na tela
"ranking de agentes, arena.ai, 22/10/2026". É um ranking de agentes (tarefas reais), diferente da Text Arena de
conversa, em que o Gemini 4 Argon lidera; o slide deve dizer qual quadro é.

## Pedidos do ensaio da versão 4 (23/10/2026): feitos na versão 5 (23/10)

Todos os 8 entraram em `decks/curso-ia-aula1/deck.html` (64 slides, 74 paradas); o detalhe de cada um está no
`briefing.md`, seção "O que mudou da versão 4", e as fontes novas em `apuracao-2.md`, itens 5.5, 10 e 11.

1. [feito] Slide 16 virou a linha do tempo "A IA tem 70 anos; o ChatGPT, quase 4" (seis marcos; GPT-3 e GPT-6 na
   legenda, porque o arquétipo tempo cabe seis).
2. [feito] Conta e camadas (quatro paradas) viraram "Um neurônio multiplica e soma" (duas paradas): 2×3 + 1×1 + 3×2
   = 13, média ponderada, e no segundo clique a rede com os 405 bilhões de parâmetros.
3. [feito] Práticas 2 e 4 com link clicável (nova aba, sem avançar o slide); sem rota impressa; arena.ai clicável na
   legenda do slide da arena.
4. [feito] Índice geral e jurídico com eixo a partir de 50, escrito na tela; manchete do geral trocada para "o Opus
   5.5 vai à frente".
5. [feito] Slide novo "Na conversa, o Gemini 4 Argon lidera" (Text Arena, eixo a partir de 1490).
6. [feito] Duelo de preferência sobre precatório, respostas reais do Claude Haiku 5.5 (A) e do Claude Opus 5.5 (B), em
   até 25 palavras (com 80, a parada passava de 150 palavras e o oráculo dá ERRO acima de 70); revelação com modelo e
   preço.
7. [feito] Capa clara com o logo do tema, título em duas linhas e entrada discreta, abrindo sozinha.
8. [feito] Encerramento "Obrigado" com o logo; sem contato, porque nenhum foi achado nos repositórios.

Para o professor decidir no ensaio: o limite de 25 palavras do duelo; o contato a pôr no encerramento (site, e-mail ou
rede da co.juris), se quiser um.

Pendência do motor (não alterado): `palco.js` avança o slide em qualquer clique no palco, inclusive num link; o deck
contorna com `stopPropagation` nos links. Conserto proposto: ignorar cliques em `a[href]` no `palcoEl`.

## Pedidos de 23/10/2026, depois da versão 5

Pedido do professor, feito na versão 6 de `decks/curso-ia-aula1/deck.html` (62 slides, 72 paradas); detalhe no
`briefing.md`, seção "O que mudou da versão 5", e fontes em `apuracao-2.md`, item 12.

1. [feito] Trocar "A palavra vira uma lista de números" e "Um neurônio multiplica e soma" (paradas 23 a 25 da folha da versão
   5) por dois slides visuais, sem conta: (a) "Pesos dizem quanto cada pista importa", a frase "O juiz julgou o
   pedido…" com "juiz", "julgou" e "pedido" ligadas a "procedente" e "improcedente" por fios de espessuras diferentes,
   a candidata com mais força entra na frase (pílula "ilustrativo"); (b) "Os modelos de ponta passam de 1 trilhão de
   pesos", uma rede em camadas e os números oficiais dos abertos de ponta, com fonte e data, e a linha de que os
   fechados não divulgam.
2. [feito] Tirar do deck o Llama 3.1 como exemplo de tamanho e de volume de treino, trocando por modelo recente com fonte; sem
   fonte oficial de tokens de treino, reformular o slide do corpus sem número de modelo antigo, e registrar no briefing.

3. [feito] Tirar a prática 5 inteira: o duelo de preferência sobre precatório e a revelação "A custa até 40 vezes
   menos que B" (paradas 62 e 63 da folha da versão 5). A arena fica explicada pelos slides de ranking; o bloco "Qual
   a melhor" caiu de 20 para 17 minutos e o "Fechado e aberto" subiu de 10 para 13 (soma 90); a seção Duelo do briefing ficou marcada como
   retirada. O deck passa a 62 slides e 72 paradas.
4. [feito] Linha dos fechados no slide "Os de ponta passam de 1 trilhão de pesos": "Claude, GPT e Gemini não divulgam
   o tamanho", porque nenhuma fonte lida estima o número; a ordem de grandeza fica na fala, como opinião do professor.

Para o professor decidir no ensaio: a manchete pedida virou "Os de ponta passam de 1 trilhão de pesos" para caber numa
linha; o Muse Spark Open (816 bilhões) fica abaixo do marco de 1 trilhão, como os números mostram;
os 3 minutos da prática 5 foram para o bloco 5 e podem ir para outra parte, se ele preferir.

## Pedido de 23/10/2026, depois da versão 6

O slide "Pesos dizem quanto cada pista importa" (fios entre "juiz/julgou/pedido" e "procedente/improcedente") ficou
confuso até para o professor.

Feito na versão 7 (61 slides, 71 paradas); detalhe no `briefing.md`, seção "O que mudou da versão 6", e na rodada 9
da crítica.

1. [feito] Retirar o slide "Pesos dizem quanto cada pista importa".
2. [feito] Em "Os de ponta passam de 1 trilhão de pesos", trocar a primeira parada (rede com fios) por texto grande com a
   analogia "Uma rede neural é feita de bilhões de botões de ajuste: os pesos, ou parâmetros. Treinar é girar esses
   botões até as respostas ficarem boas.", com no máximo um desenho discreto de botões girando; a segunda parada
   (barras e linha dos fechados) continua. Ficou com nove botões discretos que giram; no segundo clique, frase e
   botões saem e as barras ocupam a largura toda.
3. [feito] Vizinhança de arquétipos, respiro, notas e transições dos vizinhos; soma dos blocos em 90 e determinismo
   conferido. Blocos em 16/29/14/18/13: o minuto do slide retirado saiu do bloco 2 e foi para o 4, porque
   16/30/14/17/13 com 61 slides reprovou o determinismo (o mesmo pixel da linha do dia).

## Pendência de motor (23/10/2026)

- O teste de determinismo do `./ap sondar` falha por um pixel na barra de progresso da linha do dia conforme a
  divisão de minutos dos blocos (ex.: 16/30/14/17/10). Contornado na Aula 1 com 16/30/14/17/13 (versão 6) e 16/29/14/18/13 (versão 7). Corrigir em
  `motor/palco.js` (arredondar o `scaleX` da barra ou o `faixa` do bloco) e cobrir com teste.
- `palco.js` avança o slide em qualquer clique, inclusive em link; a Aula 1 contorna nos próprios links. Corrigir no
  motor ignorando cliques em `<a>`.

## Aula 1, versão 8 (23/10/2026)

- "O treino ajusta os pesos" virou cena própria de quatro cliques: o texto real "O céu é azul" inteiro, a última palavra
  escondida, o palpite errado ("verde"), a revelação e os botões girando até acertar. Novo slide "Depois, o reforço: notas,
  não gabarito" (quatro cliques): uma pergunta, duas respostas, as notas 9 e 2 (inventadas, só para explicar) e os botões
  girando a favor da de nota alta. 62 slides, 78 paradas; sondar sem erro e determinismo ok com os blocos 16/29/14/18/13.
- Feito depois, a pedido do professor: slide "Cada token vira uma lista de números" (dois cliques; vetor e mapa
  ilustrativos, marcados no rodapé, porque ele aceitou valor inventado; mostra "banco" de sentar e "banco" do dinheiro
  em lugares diferentes) e slide "Parecer e lei: prefira Markdown", depois do sigilo da memória. Fonte do segundo: documentação
  de PDF da Anthropic (platform.claude.com, lida em 23/10/2026: página vira imagem e texto; 1.500 a 3.000 tokens de
  texto por página; 3 páginas, cerca de 1.000 tokens só com texto e 7.000 com imagens) e central de ajuda do Claude
  (projetos passam a buscar só os trechos quando o conhecimento chega perto do limite). A ideia do post, "o PDF entra
  inteiro", é verdadeira em parte: vale para o anexo direto; apps com busca já recuperam trechos. ChatGPT: página de
  ajuda deu 403, comportamento com PDF [CONFERIR]. Total: 64 slides.
