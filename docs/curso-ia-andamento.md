# Curso de IA da co.juris: andamento (passagem para o próximo agente)

Atualizado em 22/10/2026. Branch `claude/briefing-dia-1`, no worktree
`/Volumes/Projetos/apresentacao/.claude/worktrees/ia-course-presentations-c2018d`. Nada foi juntado ao `main` nem
publicado. Ideias para depois ficam em `docs/curso-ia-ideias.md`.

## O que é

Dia 1 de um curso pago de IA (turma mista: advogados, uma desembargadora, servidores, assessores; muitos sem plano
pago). Duas aulas de ~90 min na mesma tarde, tema `cojuris`, plano contínuo. Siga a skill
`.claude/skills/apresentacao/SKILL.md`.

- Aula 1, "O que é IA e qual usar": `decks/curso-ia-aula1/` (briefing, deck de 52 slides da versão 3, `apuracao.md`).
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

## Pedidos do ensaio da versão 3 (22/10), ainda por fazer na Aula 1

1. Animação explicativa de pesos e multiplicação de matrizes (por código, sequência de slides).
2. Capa mais impactante, que abre sozinha ao carregar (sem tecla).
3. Tirar todos os `[CONFERIR]`.
4. Trocar a foto da janela de contexto (ruim) por desenho; o "meio se perde" (Liu et al., 2023) só fica com estudo
   recente que sustente, senão sai.
5. Guiar o apresentador: notas estruturadas (diga, faça, transição), tempo por bloco, cronômetro nas práticas.
6. Linha do dia fixa embaixo, com os blocos da aula e o atual destacado.
7. Conceito de IA mais longo e claro: OCDE e PL 2338/2023 decompostos em partes.
8. Fronteira irregular com desenho e exemplos jurídicos bons.
9. "Qual a melhor IA": mostrar o ranking atual da Artificial Analysis (índice geral e jurídico) e da arena.ai;
   refazer o slide 39 (pesos do Legal Index), que ninguém entenderia.
10. Refazer a prática do duelo (slide 42) com instrução clara e duas respostas reais de IAs diferentes; o professor
    ainda não respondeu se as gero eu (Claude + Gemini, < US$ 0,05) ou ele.
11. Slides de memória (ChatGPT e Claude) logo depois de "Conversa nova, mesa limpa".

## Trabalho em andamento quando esta nota foi escrita

- Pesquisa para os itens 3, 4, 7, 8, 9 e 11 e o roteiro de pesos e matrizes: vai para
  `decks/curso-ia-aula1/apuracao-2.md`. A parte de memória já voltou (páginas oficiais de 21 e 22/10/2026): apagar
  a conversa não apaga a memória criada dela, nos dois produtos; conversa temporária ou anônima não cria memória,
  mas fica guardada até 30 dias.
- Motor (itens 2, 5 e 6): PRONTO no commit `9f41c10` (`./ap teste`: 99 passed). O deck liga com `autoplay: true`,
  `blocos: [{id, rotulo, minutos}]`, `bloco:` por slide (herdado pelos seguintes), `linhaDia: false` para esconder,
  `pratica: N` (cronômetro) e `notas: {diga, faca: [...], transicao}`. Contrato em `docs/palco.md`, seção "Blocos da
  aula"; o catálogo já usa os três.
- Pesquisa: os subagentes devolveram memória, rankings (Artificial Analysis geral e jurídico, arena.ai), contexto
  longo (trocar "o meio se perde" por "quanto maior o texto, mais cai a capacidade de cruzar e inferir", NoLiMa 2025,
  Chroma 2025, Anthropic 2026; Liu et al. 2023 sai) e fronteira irregular (seis exemplos jurídicos ilustrativos). O
  consolidado vai para `decks/curso-ia-aula1/apuracao-2.md`; se o arquivo não existir ou estiver incompleto, os
  relatórios estão resumidos nas mensagens desta sessão e precisam ser refeitos.

## Próximo passo

Com `apuracao-2.md` e o motor prontos, remontar a Aula 1 com os 11 itens, rodar lint, sondar, mídia e três rodadas de
crítica (passos 5 a 7 da skill), commitar e abrir `./ap abrir decks/curso-ia-aula1` para o professor ensaiar. Depois,
a Aula 2. Antes de juntar ao `main`: bateria completa (`./ap teste`), autorrevisão por subagente e o "posso juntar?".

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
