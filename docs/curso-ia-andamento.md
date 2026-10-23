# Curso de IA da co.juris: andamento (passagem para o próximo agente)

Atualizado em 23/10/2026. Branch `claude/briefing-dia-1`, no worktree
`/Volumes/Projetos/apresentacao/.claude/worktrees/ia-course-presentations-c2018d`. Nada foi juntado ao `main` nem
publicado. Ideias para depois ficam em `docs/curso-ia-ideias.md`.

## O que é

Dia 1 de um curso pago de IA (turma mista: advogados, uma desembargadora, servidores, assessores; muitos sem plano
pago). Duas aulas de ~90 min na mesma tarde, tema `cojuris`, plano contínuo. Siga a skill
`.claude/skills/apresentacao/SKILL.md`.

- Aula 1, "O que é IA e qual usar": `decks/curso-ia-aula1/` (briefing, deck de 63 slides da versão 4, `apuracao.md` e
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

1. Ensaio do professor com `./ap abrir decks/curso-ia-aula1` (tela do apresentador com P); pedidos voltam ao passo 5
   da skill.
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

## Pedidos do ensaio da versão 4 (23/10/2026)

Versão 4 da Aula 1: commit `37a7245` mais a correção do motor `effee7c` (linha do dia some na viagem). Ajustes pedidos
pelo professor, em execução por um subagente quando esta nota foi escrita (versão 5); se o commit da versão 5 não
estiver no branch, refazer a partir daqui, pela numeração da folha `decks/curso-ia-aula1/storyboard/folha.png` da v4:

1. Slide 16 (ramos simbólica/máquina/profundo/transformers): virar linha do tempo com períodos e marcos até os LLMs
   (Dartmouth 1956, sistemas especialistas, aprendizado de máquina, AlexNet 2012, transformers 2017, GPT-3 2020,
   ChatGPT 30/11/2022), cada data com fonte.
2. Slides 25 e 26 (conta da matriz): difíceis; trocar por um neurônio com três entradas, três pesos e a soma, com
   analogia do cotidiano (nota ponderada), sem tabela.
3. Slide 33: sem folha impressa; QR vira link clicável (o professor testa ao vivo). Idem nas outras práticas.
4. Slides 57 e 59 (Artificial Analysis geral e jurídico): escala aproximada, não 0 a 100, com o início do eixo escrito,
   para a vantagem do Claude aparecer.
5. Slide 61: acrescentar a Text Arena, em que o Gemini 4 Argon lidera (captura do professor de arena.ai/leaderboard/text,
   22/10/2026, 8.946.356 votos, 418 modelos: Gemini 4 Argon 1517 ±7 preliminar; Claude Opus 5.5 1509 ±7; Muse Wonder
   1509 ±8; Claude Fable 5 1503 ±4; Claude Fable 5.1 1503 ±6). Agentes: Claude lidera; conversa: Gemini.
6. Slide 63 (duelo do prazo em dobro): a plateia sabe de cor. Trocar por duelo de preferência (explicar precatório a um
   leigo), com respostas reais do Claude Opus 5.5 e do Claude Haiku 5.5, sem nome, e revelação no slide seguinte.
7. Capa mais simples, com o logo da co.juris (`temas/cojuris/marca/`, só sobre fundo claro), abrindo sozinha.
8. Slide de encerramento com o logo da co.juris.

Depois da versão 5: novo ensaio do professor; em seguida a Aula 2 (rever o briefing, que ainda usa o fio da data).
