# Ficha: agentes de uma peça do quatilex (harness), para a Aula 4

Fonte única: print da aba "Detalhes" de uma peça gerada no quatilex, enviado pelo professor na conversa de 05/11/2026,
guardado em `dia2-harness-print-2026-11-05.png`. Não há dado de processo no print. Os números valem para essa peça,
não para a média do sistema.

| Agente | Modelo | Tokens in | Cache read | Cache write | Tokens out | US$ |
|---|---|---|---|---|---|---|
| classificador | openai.gpt-6-luna | 4 | 52.738 | 64.197 | 4.980 | 0,0121 |
| mm_arg_flash | gemini-3.8-flash | 84.810 | 591.054 | 0 | 7.548 | 0,1362 |
| mm_arg_luna | openai.gpt-6-luna | 12 | 415.152 | 122.425 | 25.832 | 0,0356 |
| doutrina | gemini-embedding-2 | 129 | 0 | 0 | 0 | 0,0000 |
| doutrina | typesafe-jev | 40.786 | 0 | 0 | 0 | 0,0017 |
| acervo_jurisprudencia | gemini-embedding-2 | 195 | 0 | 0 | 0 | 0,0000 |
| acervo_jurisprudencia | typesafe-jev | 79.140 | 0 | 0 | 0 | 0,0033 |
| mm_agrupador | claude-haiku-5-5 | 7.428 | 0 | 1.797 | 10.681 | 0,0063 |
| redator | claude-opus-5-5 | 10 | 490.845 | 189.212 | 12.172 | 1,3859 |
| validador_jurisprudencia | openai.gpt-6-luna | 6 | 23.639 | 13.968 | 3.276 | 0,0040 |
| validador_legislacao | openai.gpt-6-luna | 4 | 11.082 | 21.408 | 7.660 | 0,0073 |
| afirmacao_oficio | openai.gpt-6-luna | 2 | 0 | 2.661 | 17 | 0,0004 |

Totais calculados nesta sessão: 10 agentes, 6 modelos, US$ 1,5928, 72.166 tokens gerados; o redator responde por
US$ 1,3859, 87,0% do custo.

Presunções a resolver na leitura do código (`/Volumes/Projetos/Automacao_Agent`, só leitura): a ordem real do fluxo e o
papel de `mm_agrupador` e `afirmacao_oficio`. O professor confirmou em 05/11/2026 que a tabela termina em
`afirmacao_oficio`, então os totais acima são os da peça. A versão anterior da animação (`claude_video_maker/videos/agentes-peca`, 07/10/2026)
usava outro print: 8 agentes, 5 modelos, US$ 0,7527.

## Papéis e ordem (lidos no código em 05/11/2026)

Caminhos relativos a `Automacao_Agent/`. O pré-passo dos leitores só roda quando a opção multiagente do lote está ligada e não há rota por assunto (`src/services/orchestrator.py:2049-2090`; padrão desligado em `src/domain/orchestration.py:40`). A peça do print passou por esse caminho, pois traz `mm_arg_*` e `mm_agrupador`.

| Ordem | Agente | Papel em linguagem simples | Onde no código |
|---|---|---|---|
| 1 | classificador | Lê os autos e decide o tipo do caso e a saída recomendada (peça ou não). | `src/agents/classification_graph.py:18`; chamado em `src/services/orchestrator.py:3729-3746` |
| 2 | mm_arg_luna | Leitor barato: lê os autos e monta lista de argumentos e fatos com fonte. | `src/composition.py:294`; `src/services/contexto_multiagente.py:148,397` |
| 2 | mm_arg_flash | Segundo leitor barato, do mesmo trabalho; os dois rodam juntos. | `src/composition.py:297`; `src/services/contexto_multiagente.py:148,397` |
| 3 | mm_agrupador | Compara os argumentos dos dois leitores e junta os que dizem a mesma coisa. | `src/services/mm_agrupador.py:1-5,47`; chamado em `src/services/contexto_multiagente.py:421` |
| 4 | redator | Escreve a peça, com ferramentas para conferir nos autos o que os leitores disseram. | `src/composition.py:247`; geração em `src/services/orchestrator.py:4356` |
| sob demanda | doutrina | Ferramenta de busca de doutrina que leitores e redator chamam; usa embeddings e filtro, não escreve. | `src/agents/tools_doutrina.py:27`; registro em `src/agents/producers/peca_producer.py:736`; custo em `src/adapters/embeddings/google_embeddings.py:29` e `src/adapters/jev/filtro_jev.py:39` |
| sob demanda | acervo_jurisprudencia | Ferramenta de busca no acervo de súmulas e temas oficiais; não escreve. | `src/agents/tools_acervo_jurisprudencia.py:13`; registro em `src/agents/producers/peca_producer.py:742`; custo em `src/composition.py:1053,1059` |
| 5 | validador_jurisprudencia | Confere se cada julgado citado na peça existe e diz o que a peça afirma. | `src/agents/validador_jurisprudencia_agent.py:1`; chamado em `src/services/orchestrator.py:4790` |
| 5 | validador_legislacao | Confere se cada artigo de lei citado existe e está bem descrito. | `src/agents/validador_legislacao_agent.py:1`; chamado em `src/services/orchestrator.py:4794` |
| 6 | afirmacao_oficio | Lê a peça pronta e confere se ela afirma um ofício que não foi expedido; se afirmar, manda gerar o rascunho do ofício. | `master:docs/ARQUITETURA.md:148` (pergunta 173, 03/11/2026: GPT 6 Luna, sem ferramentas, em `_finalizar_resultado`, depois da peça); `master:src/services/afirmacao_oficio.py` |

Os dois leitores rodam em paralelo entre si (`rodar_analistas_paralelo`, `src/services/contexto_multiagente.py:397`), e os dois validadores rodam em paralelo entre si, num pool de duas tarefas (`src/services/orchestrator.py:4749-4796`). Fora isso a ordem é em fila: classificador, leitores, agrupador, redator, validadores. Doutrina e acervo não são etapa própria, são ferramentas chamadas dentro dos leitores e do redator (`src/services/contexto_multiagente.py:370`).

Correção do coordenador (05/11/2026): a leitura acima foi feita na pasta de trabalho do quatilex, que estava no ramo
`knowledge/ec136-tres-intervalos`, anterior ao agente `afirmacao_oficio`. No `master` (commits 83cb6be59 e 91da193c0)
ele existe e é o último passo da peça, como na linha 6 da tabela. As linhas de código citadas nas demais linhas são do
ramo lido e podem ter mudado de número no `master`; papéis e ordem foram conferidos pela `docs/ARQUITETURA.md` do
`master` só para o `afirmacao_oficio`.

Não consegui confirmar:
- Se a chamada logo depois dos validadores (nova rodada do redator, `_auto_resolver_fontes`, `src/services/orchestrator.py:4866`) aparece no print com o nome `redator`: o código a manda ao mesmo redator, mas não vi onde o nome é gravado na trilha.
- A ordem entre ofício e classificador no print: no código o ofício vem depois do classificador e antes da geração, mas não sei se `afirmacao_oficio` é esse passo.
- Se o `langgraph.json` dá a ordem: ele só registra o grafo de teste `ping`; a ordem real está no `orchestrator.py`, e `generation_graph.py` tem um único nó.
