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
