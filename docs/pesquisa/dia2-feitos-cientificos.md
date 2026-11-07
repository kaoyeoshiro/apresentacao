# Feitos recentes da IA nas ciências (2024 a novembro de 2026)

Pesquisa feita em 07/11/2026 com páginas lidas na sessão. Onde a página primária bloqueou a leitura (openai.com, nobelprize.org, nature.com, theguardian.com, newscientist.com retornaram 403 ou recusa), a informação veio de fonte secundária indicada na tabela, e isso pesa no grau de confiança.

## Resumo

1. A IA não "resolveu um problema do milênio" no sentido que o Clay Institute reconhece: a OpenAI anunciou em 08/09/2026 uma prova de explosão (singularidade) para Navier-Stokes com força externa, ainda sem verificação independente e sem chancela do Clay.
2. Em matemática de competição o patamar foi atingido: ouro oficial do Gemini Deep Think na IMO 2025 (35/42) e nota máxima de dois sistemas chineses, corrigidos pela organização, na IMO 2026.
3. Em pesquisa, a IA passou a produzir resultados que matemáticos de primeira linha conferem e assinam, como o contraexemplo da OpenAI à conjectura das distâncias unitárias de Erdős (maio de 2026), verificado por Alon, Gowers e outros sete.
4. Em computação, o AlphaEvolve (2025) achou algoritmo melhor que o de Strassen para matrizes 4x4 complexas e recupera 0,7% da capacidade de computação mundial do Google; no ICPC 2025 a OpenAI fez 12 de 12 e o Gemini 10 de 12.
5. Em biologia, o Nobel de Química de 2024 premiou o AlphaFold; em 2025 vieram antibióticos desenhados por IA eficazes em camundongos e o primeiro fármaco descoberto por IA com resultado de fase 2a publicado.
6. A ressalva comum a tudo é a mesma: a máquina gera, mas a validação continua humana e lenta, e prova formal em Lean só garante o que foi formalizado, que pode não ser o problema original.

## O "problema do milênio": o que é fato e o que é exagero

Em 08/09/2026 a OpenAI anunciou que um modelo interno não lançado, operando como enxame de cerca de 10 mil agentes por 88 horas (mais 17 horas para formalizar em Lean), construiu uma solução das equações de Navier-Stokes em três dimensões, com força externa suave, que desenvolve singularidade em tempo finito. É a alternativa (C) do enunciado oficial de Charles Fefferman para o Clay, a da quebra (*breakdown*), e não a prova de que as soluções são sempre suaves. A empresa disse que não reclamará o prêmio de US$ 1 milhão. O trabalho se apoia no programa de Diego Córdoba e Luis Martínez-Zoroa (arXiv 2309.08495, 2023), e Fefferman disse à Quanta estar feliz com a solução, atribuindo o mérito central a esses dois matemáticos (Quanta, 08/09/2026).

O exagero está em três pontos. Primeiro, ninguém de fora verificou a prova até onde esta pesquisa alcançou: a Wikipedia registra que em 18/09/2026 a afirmação (C) não tinha verificação independente, e o presidente do Clay, Martin Bridson, disse que a avaliação será "deliberadamente sem pressa" e rigorosa; a página oficial do Clay segue classificando Navier-Stokes como problema "ativo", sem menção à IA. Segundo, a formalização em Lean foi contestada: Bastounis, Circelli e Hansen (arXiv 2610.08144, 06/10/2026) sustentam que o enunciado em Lean não corresponde à prova em linguagem natural, de modo que a checagem da máquina não dá confiança sobre o argumento original, embora não afirmem que a prova matemática esteja errada. Terceiro, o caso sem força externa, que é o que os especialistas consideram o coração do problema, continua aberto: Constantin, Ignatova e Vicol (arXiv 2609.20803, 17/09/2026) provaram que o método da OpenAI não se estende a forças analíticas, e portanto não alcança a força nula; Luis Silvestre (Chicago) resumiu à Scientific American que "o problema mais importante não está resolvido" (21/09/2026).

Há ainda uma disputa de crédito. Tristan Buckmaster (NYU) e Levent Alpöge (Anthropic) publicaram horas antes um resultado de explosão para as equações de Euler, e Buckmaster acusou a OpenAI de ter aproveitado seus métodos; a empresa nega e diz que as provas "diferem significativamente". Dias depois a OpenAI disse ao New York Times ter feito "progresso substancial" num segundo problema do milênio, sem nomeá-lo nem mostrar nada (Decrypt, 17/09/2026); isso não é verificável.

Veredito: é verdade que um sistema de IA produziu, em quatro dias, um argumento que, se resistir à revisão, responde a uma das formulações oficiais do problema de Navier-Stokes, com elogio do autor do enunciado. É exagero dizer que "a IA resolveu um problema do milênio": não há verificação independente publicada, o Clay não reconheceu nada (e suas regras exigem publicação e prazo de espera), a prova em Lean foi questionada e a versão sem força, a que interessa aos matemáticos, segue aberta. A formulação honesta para a aula é "a IA apresentou uma solução candidata para uma versão do problema, ainda em verificação". O prazo de dois anos após publicação mencionado pela imprensa não foi conferido no regulamento do Clay (a página só remete a um PDF) e fica [CONFERIR].

## Tabela de feitos

A tabela reúne os itens confirmados, com o grau de confiança atribuído à fonte efetivamente lida.

| Área | Feito | Data | Quem | Fonte lida | Confiança | Ressalva |
|---|---|---|---|---|---|---|
| Matemática | Solução candidata de Navier-Stokes com força externa (explosão em tempo finito) | 08/09/2026 | OpenAI (modelo interno, ~10 mil agentes) | quantamagazine.org/ai-has-solved-one-of-maths-1-million-millennium-prize-problems-20260908/; arxiv.org/abs/2609.20803; arxiv.org/abs/2610.08144; claymath.org/millennium/navier-stokes-equation/ | Alta quanto ao anúncio; baixa quanto à validade | Sem verificação independente; Lean contestado; caso sem força segue aberto; post da OpenAI não pôde ser lido (403) |
| Matemática | Ouro oficial na IMO 2025, 35/42, em linguagem natural e dentro das 4,5 h | 21/07/2025 | Google DeepMind (Gemini Deep Think) | deepmind.google/discover/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/ | Alta | Corrigido pelos coordenadores da IMO; a OpenAI também anunciou 35/42, mas autoavaliado |
| Matemática | 42/42 na IMO 2026 (Xangai), corrigidos pela organização | 23/07/2026 | Huawei (Celia) e Xiaohongshu (dots-note-3.0) | standardmedia.co.ke (despacho AFP); digitalapplied.com/blog/imo-2026-perfect-scores-ai-benchmark-saturation | Média | Sem página oficial da IMO lida; notas máximas de OpenAI, Anthropic e Kimi vieram de teste privado com corretores automáticos, não oficial |
| Matemática | Contraexemplo à conjectura das distâncias unitárias de Erdős (1946) | 20/05/2026 | OpenAI (modelo interno); verificação por Alon, Gowers, Litt, Sawin e outros | arxiv.org/abs/2605.20695 | Alta | Verificado e reescrito por nove matemáticos; ganho no expoente é pequeno (cerca de n^1,014 após melhoria humana) |
| Matemática | Soluções completas de problemas de Erdős 205 e 652 | jan/2026 | GPT-5.2 Thinking e Pro, registrados na base de Terence Tao | renyi.hu/en/news/we-are-midst-historic-moment-erdos-problems-solved-chatgpt | Média | Vários "resolvidos" anteriores já estavam na literatura; Tao critica a legibilidade das provas |
| Matemática | AlphaProof: medalha de prata na IMO 2024 (4 de 6, com AlphaGeometry 2), em Lean | jul/2024; artigo na Nature em 12/11/2025 | Google DeepMind | deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/ (via busca); research.google/pubs/olympiad-level-formal-mathematical-reasoning-with-reinforcement-learning/ | Média-alta | Problemas traduzidos para Lean por humanos; dias de computação, não 4,5 h |
| Matemática | FrontierMath Tier 4 (pesquisa) perto de 100% | set-out/2026 | GPT-6 Astra (97,6%, informado pela OpenAI) e outros | agregadores (benchlm.ai, wikidocs) | Baixa | Página da Epoch não mostrou os números; não confirmado na fonte primária |
| Computação | Algoritmo de 48 multiplicações para matrizes 4x4 complexas, melhor que Strassen (1969); 0,7% da computação do Google recuperada; kernel do Gemini 23% mais rápido | 14/05/2025 | Google DeepMind (AlphaEvolve) | deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/ | Alta (fonte da empresa) | Resultados verificados por avaliadores automáticos; em 50+ problemas abertos, melhorou 20% e igualou 75% |
| Computação | ICPC 2025: 12/12 (OpenAI) e 10/12 com ouro, segundo lugar virtual (Gemini) | 04/09/2025 | OpenAI; Google DeepMind | deepmind.google/discover/blog/gemini-achieves-gold-level-performance-at-the-international-collegiate-programming-contest-world-finals/ | Alta para o Gemini; média para OpenAI (só imprensa) | Participação remota; o ICPC aceitou as soluções mas não validou o sistema |
| Computação | Tarefas longas: horizonte de 50% de acerto de ao menos 16 h (Claude Mythos Preview) | mar-mai/2026 | METR | en.wikipedia.org/wiki/METR; metr.org/time-horizons/ | Média | A própria METR diz que medidas acima de 16 h não são confiáveis e que a página não é mais atualizada |
| Física | Previsão do tempo por IA mais precisa que o ENS do ECMWF em 97,2% dos alvos, até 15 dias, em 8 min num TPU | 04/12/2024 | Google DeepMind (GenCast, Nature) | deepmind.google/discover/blog/gencast-predicts-weather-and-the-risks-of-extreme-conditions-with-sota-accuracy/ | Alta | Comparação feita pela própria empresa, publicada com revisão por pares |
| Física | Fusão: simulador TORAX usado no dia a dia do tokamak SPARC | 16/10/2025 | Google DeepMind e Commonwealth Fusion Systems | deepmind.google/discover/blog/bringing-ai-to-the-next-generation-of-fusion-energy/ | Alta | Quase tudo é plano; o SPARC ainda não opera |
| Materiais | 2,2 milhões de cristais previstos, 736 sintetizados por terceiros | 29/11/2023 | Google DeepMind (GNoME, Nature) | deepmind.google/discover/blog/millions-of-new-materials-discovered-with-deep-learning/ | Alta | Fora da janela 2024-2026; utilidade de muitos materiais foi questionada por químicos (crítica não lida nesta sessão) |
| Biologia | Nobel de Química: metade a Baker (desenho de proteínas), metade a Hassabis e Jumper (AlphaFold) | 09/10/2024 | Academia Real Sueca | sciencenews.org/article/nobel-prize-chemistry-2024-proteins (via busca) | Alta | nobelprize.org bloqueou a leitura |
| Biologia | AlphaFold 3 prevê complexos de proteína com DNA, RNA e fármacos, 50% mais preciso que métodos anteriores | 08/05/2024 | Google DeepMind e Isomorphic Labs (Nature) | blog.google/technology/ai/google-deepmind-isomorphic-alphafold-3-ai-model/ | Alta | Código liberado só para uso acadêmico (nov/2024) |
| Química | Antibióticos desenhados por IA generativa (NG1 contra gonorreia, DN1 contra MRSA) eficazes em camundongos | 14/08/2025 | MIT, Broad Institute, James Collins (Cell) | broadinstitute.org/news/using-ai-researchers-design-new-compounds-kill-antibiotic-resistant-bacteria | Alta | Pré-clínico; de 80 moléculas escolhidas para gonorreia, só 2 foram sintetizáveis |
| Biologia | Fármaco descoberto por IA (rentosertib) com fase 2a publicada em fibrose pulmonar | 03-04/06/2025 | Insilico Medicine (Nature Medicine) | news-medical.net/news/20250604/AI-designed-drug-shows-early-promise-for-lung-fibrosis-patients-in-clinical-trial.aspx | Média-alta | 71 pacientes, 12 semanas, eficácia exploratória, mais efeitos adversos que placebo |
| Biologia | "AI co-scientist" propôs alvos e fármacos validados em laboratório (leucemia, fibrose hepática) e reproduziu hipótese já confirmada sobre resistência bacteriana | 19/02/2025 | Google Research | research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/ | Média | Avaliação pequena (15 metas), com especialistas no circuito; publicação na Nature em 2026 só vista em material do Google |
| Biologia | Miniproteínas desenhadas que ligam e desligam receptores GPCR, comparáveis a fármaco em camundongos | 21/05/2026 | Institute for Protein Design (Univ. Washington), Nature | resultado de busca (eurekalert.org/news-releases/1129114) | Baixa-média | Página não lida por inteiro; pré-clínico |

Não confirmados: os resultados oficiais de OpenAI e Anthropic na IMO 2026 (só teste privado), o placar atual do FrontierMath na página da Epoch, um feito relevante de IA em física de partículas ou astronomia em 2026 (não pesquisado a fundo por falta de tempo), e a citação exata de Terence Tao sobre Navier-Stokes (as postagens em mathstodon.xyz não foram abertas; a única fala dele lida, via mathscholar.org, de agosto de 2026, defende que matemáticos se organizem diante da IA).

## Proposta de dois slides

### Slide A: o que a IA já fez

Título: "IA na ciência"

| Área | Ano | Feito |
|---|---|---|
| Biologia | 2024 | Nobel de Química pelo AlphaFold |
| Matemática | 2025 | Ouro oficial na Olimpíada Internacional |
| Computação | 2025 | Bate Strassen em matrizes 4x4 complexas |
| Meteorologia | 2024 | Previsão de 15 dias melhor que europeia |
| Química | 2025 | Antibióticos novos curam infecção em camundongos |
| Matemática | 2026 | Derrubou conjectura de Erdős de 1946 |

Cerca de 45 palavras visíveis. Fala sugerida: a IA gera depressa e conferir leva tempo (AlphaEvolve e GenCast foram conferidos por avaliadores automáticos e pela própria empresa; na matemática, por matemáticos).

### Slide B: "a IA resolveu um problema do milênio?"

Título: "Navier-Stokes: fato e exagero"

Fato: em set/2026 a OpenAI apresentou prova candidata, com força externa.

Exagero: "resolvido". Ninguém verificou ainda; o Clay não reconheceu; a versão sem força segue aberta.

Rodapé: "Gerar é rápido. Verificar é humano."

Cerca de 34 palavras visíveis. Fala sugerida: liga direto à rotina do advogado, que recebe da IA uma peça plausível e ainda precisa conferir cada citação.
