# Apuração 2 da Aula 1 (curso de IA)

Segunda rodada, feita em 22 e 23/10/2026 sobre a base de `apuracao.md`. Cada item traz texto para a tela, fonte, data da fonte e data de leitura. Leituras de 22/10/2026, salvo quando indicado. Os itens 1, 2, 3, 4, 5 e 7 foram apurados por subagentes, que leram as páginas e devolveram os trechos citados; o coordenador desta apuração releu pessoalmente os itens 6 e 8 e a página de agentes da arena.ai (item 5.4). Onde o texto diz "ilustrativo" ou "proposta", a frase é do professor, não da fonte.

## 0. Cada [CONFERIR] do deck e o destino

Ocorrências encontradas com `grep -n CONFERIR` em `deck.html` (linhas 202, 386, 397, 577, 656, 674, 722, 757, 759, 795, 810, 812) e `briefing.md` (linhas 49, 66, 67, 84, 91, 92, 186 e a seção "Pendências", linha 201). São seis pendências, cada uma com a pílula na tela e o eco nas notas e no briefing.

| slide (id) | linhas | pendência | destino |
|---|---|---|---|
| 7 (llms) | deck 202, 722; briefing 49, 186 | ChatGPT lançado em 2022 | Resolvido com o post oficial da OpenAI de 30/11/2022, lido na cópia do Internet Archive (item 1.1). Tirar a pílula; nas notas, trocar "[CONFERIR data]" por "30/11/2022 (post oficial da OpenAI)". |
| 24 (tamanho) | deck 386, 757; briefing 66 | limite da janela no app | Resolvido com a central de ajuda do Claude: nos planos pagos, Opus 5.5 tem 1 milhão de tokens também no app (item 1.2). Reformular o rodapé para "Claude Opus 5.5, planos pagos (central de ajuda da Anthropic, out/2026)." e tirar a pílula. Não pôr número do ChatGPT nem do plano gratuito do Claude. |
| 25 (limite) | deck 397, 759; briefing 67 | como cada produto corta ou resume | Reformular. Texto da coluna "Não cabe": "O começo é resumido ou deixado de fora." Nas notas, citar só o caso documentado: "O Claude resume as mensagens antigas quando a conversa chega perto do limite (central de ajuda da Anthropic); os outros produtos não documentam o método." Tirar a pílula. |
| 42 (pratica5) | deck 577, 795; briefing 84 | respostas do duelo | Não é fato a apurar, é conteúdo a escrever. Proposta pronta no item 0.1, com base legal lida; com ela, tirar a pílula. Se o professor preferir as próprias respostas, ele as escreve e a pílula sai do mesmo jeito. |
| 49 (fechados) | deck 656, 810; briefing 91 | versões nos apps | Reformular para "família mais recente de cada empresa", que está confirmada, em vez de "modelo padrão do app", que não está (item 1.4). Corrigir o cartão da OpenAI: "GPT-6" (o system card fala em GPT-6 Sol e Luna no ChatGPT; o 6.1 Sol não está confirmado no ChatGPT comum). Rodapé: "Família mais recente de cada empresa em 22/10/2026; o modelo usado varia por plano." Tirar a pílula. |
| 50 (abertos) | deck 674, 812; briefing 92 | família Mistral | Resolvido com reformulação (item 1.5). O carro-chefe anunciado é o Mistral Large 4, mas em prévia e ainda sem pesos publicados; num slide de pesos abertos, o cartão deve ser "Mistral Large 3" (pesos publicados, Apache 2.0). Na fala: "o Large 4 está em prévia, com pesos prometidos para o fim de outubro". Tirar a pílula. |

Pendências de `apuracao.md` que não estão no deck, mas que esta rodada fechou: o nome da plataforma ("LMArena is now Arena", post oficial de 28/01/2026, item 5); "19% menos" em Dell'Acqua et al. é, no original, 19 pontos percentuais (item 7.1); a referência de Liu et al. no TACL é vol. 12 (2024), pp. 157–173 (item 2.1). Ficam abertas, sem efeito na tela, a ordem de extinção em Mata v. Avianca (não lida; não citar) e os termos de marca da Microsoft, da Moonshot e da Z.ai.

Duas mudanças fora da lista de CONFERIR decorrem desta apuração. O slide 26 (meio) deve trocar de tese (item 2.6). O cartão da OpenAI no slide 49 deve perder o "6.1" (item 1.4).

### 0.1. Proposta para o duelo do slide 42

Pergunta: "Qual é o prazo para o Estado contestar no procedimento comum?"

- Resposta A: "30 dias úteis: os 15 dias do art. 335 do CPC contam em dobro para a Fazenda Pública (art. 183), e só os dias úteis entram na contagem (art. 219)."
- Resposta B: "15 dias, conforme o art. 335 do CPC."

A resposta B soa segura e está incompleta, porque esquece o prazo em dobro; é o erro que o curso quer mostrar, o da resposta convincente que só a conferência denuncia. Fonte da base legal: Lei 13.105/2015 (CPC), texto compilado no Planalto, https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm, lido em 22/10/2026. Trechos: art. 335, "no prazo de 15 (quinze) dias"; art. 183, "gozarão de prazo em dobro para todas as suas manifestações processuais, cuja contagem terá início a partir da intimação pessoal"; art. 219, "computar-se-ão somente os dias úteis". As duas respostas são redação do professor, apresentadas como respostas de duas IAs anônimas só para o exercício; convém dizer isso na revelação.

## 1. Datas, apps e modelos

### 1.1. Lançamento do ChatGPT

Para a tela: "ChatGPT: lançado pela OpenAI em 30/11/2022."

- Fonte: OpenAI, "ChatGPT: Optimizing Language Models for Dialogue", post oficial datado de 30/11/2022, lido na cópia do Internet Archive, https://web.archive.org/web/2022/https://openai.com/blog/chatgpt/ (endereço atual https://openai.com/index/chatgpt/, que devolve 403 a robô). Trecho: "November 30, 2022 … We've trained a model called ChatGPT which interacts in a conversational way." Lido em 22/10/2026.

### 1.2. Janela de contexto dentro dos apps

Claude, confirmado para os planos pagos. Para a tela: "Claude, planos pagos: 1 milhão de tokens nos modelos 5.5 e no Fable 5.1."

- Fonte: Anthropic, central de ajuda, "How large is the context window on paid Claude plans?", https://support.claude.com/en/articles/8606394, atualizada "over 2 weeks ago" (sem data exata). A tabela dá 1M tokens para Opus 5.5, Sonnet 5.5, Haiku 5.5 e Fable 5.1, e "200K+ tokens (about 500 pages of text or more)" para os demais. Não há número para o plano gratuito nem separado para Team ou Enterprise.

Gemini, confirmado (só para a fala). Fonte: Google, ajuda do app Gemini, https://support.google.com/gemini/answer/16275805, sem data. Trecho: "Without an AI plan 32k tokens · AI Plus 128k tokens · AI Pro & AI Ultra 1 million tokens".

ChatGPT, sem fonte oficial lida. As páginas help.openai.com/en/articles/12003714, openai.com/chatgpt/pricing e chatgpt.com/pricing deram 403, inclusive no navegador do subagente. Só há fonte secundária e anterior ao GPT-6 (ai-toolbox.co, 15/09/2026), que não serve para a tela. Recomendação: não pôr número do ChatGPT. Frase segura: "No ChatGPT, o limite depende do plano e do modo." Para confirmar, a sessão principal pode abrir no navegador https://help.openai.com/en/articles/12003714.

### 1.3. O que acontece com histórico longo

Claude, confirmado. Para as notas: "Perto do limite, o Claude resume as mensagens antigas e segue a conversa."

- Fonte: Anthropic, central de ajuda, "How usage and length limits work", https://support.claude.com/en/articles/11647753-how-usage-and-length-limits-work, atualizada "over a week ago". Trechos: "When your conversation approaches the context window limit, Claude summarizes earlier messages to continue the conversation seamlessly"; "Code execution must be enabled for automatic context management."

Gemini: a ajuda (mesma página do item 1.2) diz só que passar da janela pode levar a respostas que não consideram tudo; não descreve resumo. ChatGPT: nenhuma página oficial lida; a única fonte é jornalística (PCWorld, 18/06/2026, https://www.pcworld.com/article/3168543/chatgpt-forgets-things-in-long-threads-heres-the-fix.html), que diz que os três produtos compactam conversas longas, mas sem método público.

Recomendação para o slide 25: texto genérico, que não depende de método por produto. "Não cabe: o começo é resumido ou deixado de fora." Conselho prático para a fala, que não precisa de fonte: em tarefa longa, pedir um resumo e abrir conversa nova.

### 1.4. Famílias e modelos nos apps (slide 49)

| empresa | cartão proposto | fonte lida | o que não foi confirmado |
|---|---|---|---|
| OpenAI | "GPT-6", ChatGPT | System card, https://deploymentsafety.openai.com/gpt-6-october, 07/10/2026: "We're launching GPT-6 to everyone in ChatGPT, across free and paid plans globally. These models will replace GPT-5.6 Sol and GPT-5.6 Luna in ChatGPT." O documento trata de GPT-6 Sol e GPT-6 Luna. | Qual modelo cada plano recebe. O GPT-6.1 Sol no ChatGPT só aparece em imprensa (Crypto Briefing, 11/10/2026, "ChatGPT Work"); tirar o "6.1" do cartão. |
| Anthropic | "Claude 5.5", Claude | Tabela da apuração anterior, item 4; ajuda do item 1.2. | Nada pendente. |
| Google | "Gemini 4", Gemini | Apuração anterior, item 11. | Nada pendente. |
| xAI (SpaceXSI) | "Grok 4.7", Grok | x.ai/news/grok-4-7, 21/09/2026: "Grok 4.7 is available today in Cursor and Grok Build. It is also available through the Grok API". | O anúncio não fala do app; por isso o rodapé diz "família mais recente", não "modelo do app". |
| Meta | "Muse Spark", Meta AI | about.fb.com, 08/04/2026 (https://about.fb.com/ltam/news/2026/04/presentamos-muse-spark-el-primer-modelo-de-lenguaje-a-gran-escala-disenado-para-priorizar-a-las-personas/): "Muse Spark ahora impulsa el asistente Meta AI en la app Meta AI y en meta.ai". https://dev.meta.ai/docs/models (sem data): Spark 1.3 é "the latest version"; "Muse Wonder is in preview". | Que a versão no app seja a 1.3; não pôr número de versão. |
| Microsoft | "GPT e Claude", Copilot | Microsoft Tech Community, 30/09/2026, https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/available-today-openais-gpt-6-1-sol-and-claude-sonnet-5-5-in-microsoft-copilot/4560801: "Earlier this month, Anthropic's Claude Opus 5.5 and OpenAI's GPT-6 Sol joined model choice in Microsoft Copilot. Now … GPT-6.1 Sol and Claude Sonnet 5.5"; chegada em fases a Word, Excel, PowerPoint e Chat; modo padrão "Auto". | A oferta varia por licença; dizer na fala. |

Notas do slide 49, versão proposta: "OpenAI: GPT-6 (Sol e Luna) no ChatGPT desde 07/10/2026. Anthropic: Claude 5.5 e Fable 5.1. Google: Gemini 4 Argon. xAI, hoje SpaceXSI: Grok 4.7, o mais recente. Meta: Muse Spark no Meta AI; Muse Wonder em prévia. Microsoft: Copilot com GPT-6 Sol, GPT-6.1 Sol, Claude Opus 5.5 e Sonnet 5.5, além do modo Auto. O modelo exato varia por plano."

### 1.5. Mistral (slide 50)

- Fonte: Mistral AI, "Mistral Large 4", https://mistral.ai/news/mistral-large-4, 06/10/2026. Trechos: "public preview of Mistral Large 4"; "1 trillion-parameter natively multimodal model with 52 billion active parameters. It is our largest and most capable model to date"; "We will release the weights by the end of the month." A documentação (https://docs.mistral.ai/getting-started/models/models_overview/) o destaca como "A state-of-the-art, open-weight, general-purpose multimodal model."
- Licença do Large 4: não anunciada; não há repositório dele no Hugging Face em 22/10/2026. O Mistral Large 3 está no Hugging Face sob `apache-2.0` (https://huggingface.co/mistralai).

Para o cartão: "Large 3", subtítulo "Mistral". Para a fala: "O Large 4, o maior da Mistral, está em prévia desde 06/10/2026, com pesos prometidos para o fim do mês." Se os pesos saírem antes da aula, trocar o cartão para "Large 4" e conferir a licença.

## 2. Contexto longo: o que vale em 2026

### 2.1. Liu et al., referência completa

"Lost in the Middle: How Language Models Use Long Contexts", Transactions of the Association for Computational Linguistics, vol. 12 (2024), pp. 157–173, DOI 10.1162/tacl_a_00638, https://aclanthology.org/2024.tacl-1.9/. Mede modelos de 2023.

### 2.2. RULER (Hsieh et al., 2024)

arXiv 2404.06654, v1 de 09/04/2024, v3 de 06/08/2024 (COLM 2024), https://arxiv.org/abs/2404.06654. Passar no teste simples da agulha (achar uma frase escondida num texto longo) não garante uso real do contexto: dos 17 modelos testados, todos anunciando 32 mil tokens ou mais, "only half of them can maintain satisfactory performance at the length of 32K". Modelos de 2024 (Gemini 1.5 Pro, GPT-4, Llama 3.1, Qwen2 e outros).

### 2.3. NoLiMa (Modarressi et al., 2025)

arXiv 2502.05167, v1 de 07/02/2025, v3 de 09/07/2025 (ICML 2025), https://arxiv.org/abs/2502.05167. A pergunta e o trecho com a resposta quase não têm palavras em comum, o que obriga o modelo a inferir a ligação. Com 13 modelos de 128 mil tokens ou mais, em 32 mil tokens 11 deles "drop below 50% of their strong short-length baselines"; o GPT-4o caiu de 99,3% para 69,7%.

### 2.4. Context Rot (Chroma, 2025)

Kelly Hong, Anton Troynikov e Jeff Huber, Chroma, 14/07/2025, https://www.trychroma.com/research/context-rot (o endereço research.trychroma.com/context-rot redireciona para cá). Testa 18 modelos, entre eles Claude Opus 4 e Sonnet 4, o3, GPT-4.1, Gemini 2.5 Pro e Qwen3. O desempenho cai com o tamanho da entrada mesmo em tarefas simples, e cai mais quando a pergunta se parece pouco com o trecho certo ou quando há distratores ("even a single distractor reduces performance"). Sobre posição, as 11 posições testadas deram "no notable variation in performance" na tarefa da agulha. Blogs que atribuem à Chroma a reconfirmação do "lost in the middle" não encontram apoio no texto dela.

### 2.5. Testes recentes

- LongPiBench (Tian et al., ACL Findings 2025, arXiv 2410.14641, v3 de 28/05/2025, https://arxiv.org/abs/2410.14641): com 11 modelos, "most current models are robust against the 'lost in the middle' issue"; persiste um viés ligado à distância entre as várias informações relevantes.
- Fiction.LiveBench (https://fiction.live, tabela datada de 04/04/2026, lida no navegador): compreensão de enredo em histórias longas. Em 192 mil tokens, os modelos de ponta ficam perto do teto (gemini-3-flash-preview 100,0; gpt-5.2 96,9), enquanto modelos médios despencam (glm-4.7 com 15,6 em 120 mil). Modelos de 2026 mais novos que esses não estão na tabela lida.
- Anthropic, lançamento do Claude Opus 4.6, 05/02/2026, https://www.anthropic.com/news/claude-opus-4-6: no MRCR v2 com 8 agulhas e 1 milhão de tokens, Opus 4.6 fez 76% e Sonnet 4.5, 18,5%; a empresa usa a expressão "context rot".
- LongBench v2 (arXiv 2412.15204, 19/12/2024): especialistas humanos acertaram 53,7%, o melhor modelo sem raciocínio 50,1%, o o1-preview 57,7%.
- OpenAI, GPT-5.5 (23/04/2026): a página oficial deu 403 e os números do MRCR por faixa não foram lidos. Não usar.

### 2.6. Veredito e frase para a tela

A tese "o meio se perde" não se sustenta mais como regra geral: o LongPiBench registra que a maioria dos modelos atuais resiste ao efeito, e a Chroma não viu variação por posição na tarefa da agulha. O que se mantém, em estudos de 2024 a 2026 e nos testes dos próprios fabricantes, é a queda com o tamanho, mais forte quando a resposta exige ligar informações em vez de localizar uma frase, e muito desigual entre modelos.

Para o slide 26, título proposto: "Quanto maior o texto, mais o acerto cai". Achado: "Achar uma frase solta já é fácil; ligar dados espalhados num texto longo ainda falha (NoLiMa, 2025; Chroma, 2025)." As três imagens (início, meio, fim) podem virar três documentos de tamanho crescente, ou o professor mantém a imagem e troca só o achado. Liu et al. pode ficar na fala como origem histórica do tema, sempre com "2023".

## 3. Memória nos chats

Fontes oficiais lidas no navegador em 22/10/2026 (help.openai.com bloqueia robô, mas abriu no navegador).

### 3.1. ChatGPT

- Memória: OpenAI, "Memory in ChatGPT", https://help.openai.com/en/articles/8590148-memory-in-chatgpt, atualizada por volta de 21/10/2026 (a página mostrava "há 19 horas"). Pode usar "past chats, saved memories, custom instructions, files in Library, content from connected apps", conforme plano e região. Como entra na conversa: "ChatGPT decides which available information is relevant to a response"; podem aparecer "Sources" abaixo da resposta, indicando a memória ou conversa usada. As memórias salvas ficam "stored separately from chat history". Caminho: Settings > Personalization > Memory, com opções de corrigir, "Don't mention this again" e "Delete and turn off memory", que "does not delete past chats". Desligar a referência ao histórico agenda o apagamento do que foi lembrado "within 30 days"; "The original chats remain in your history".
- Apagar não é simétrico: "Deleting a chat alone does not necessarily delete a separate saved memory created from that chat"; apagar uma memória salva "does not remove mentions of that information from past conversations"; "OpenAI may retain logs of deleted saved memories for up to 30 days". Dado sensível: "Sensitive information can appear in Memory if you share it with ChatGPT."
- Treino: "For personal ChatGPT accounts, OpenAI may use chats and remembered information to improve models when Improve the model for everyone is on"; por padrão, não usa conteúdo de Business, Enterprise e Edu.
- Conversa temporária: https://help.openai.com/en/articles/8914046-temporary-chat-in-chatgpt, atualizada por volta de 19/10/2026. Fica fora do histórico, não treina o modelo enquanto for temporária e "Neither option creates or updates memories"; a opção "Personalized" ainda pode usar memórias já existentes. "OpenAI may keep a copy of a temporary chat for up to 30 days for safety purposes."
- Projetos: https://help.openai.com/en/articles/10169521-projects-in-chatgpt, atualizada por volta de 21/10/2026. Memória padrão ou "Project-only memory"; projetos compartilhados usam só a memória do projeto.

### 3.2. Claude

- Memória e busca: Anthropic, https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context, atualizada em 21/10/2026. "Claude saves memory as a set of individual topics as you chat"; também guarda o que se pede com "remember this". Ligada por padrão nos planos Free, Pro e Max; no Team e no Enterprise, depende do administrador. A busca em conversas anteriores existe nos planos pagos e aparece na tela como chamada de ferramenta. Cada projeto tem memória própria. Ver e editar em Settings > Memory (lista de "Topics"); "Pause memory" suspende; "Reset memory" "Permanently deletes all memories including project memories". Dá para desligar numa conversa só, antes da primeira mensagem (menu "+" > Memory).
- Apagar não é simétrico: "When a conversation expires or is deleted, related memory entries generated from it won't be removed, but you can delete individual memories at any time."
- O que não vira memória: "government ID numbers, criminal history, financial account numbers, and immigration status", mesmo a pedido.
- Conversa anônima: https://support.claude.com/en/articles/12260368-use-incognito-chats, atualizada "over 3 weeks ago". Não entra no histórico nem na memória; não é usada para treino; fica guardada por 30 dias, ou mais se a organização definir.
- Treino: https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training (16/03/2026) e https://www.anthropic.com/news/updates-to-our-consumer-terms (28/08/2025). Nos planos Free, Pro e Max, o treino depende da escolha do usuário; quem permite tem retenção de cinco anos, quem não permite fica com 30 dias. Não vale para os planos de trabalho nem para a API.

### 3.3. Texto para três slides

Slide A, o que é: "Memória é um caderno de anotações sobre você que o app consulta quando acha útil e põe na conversa nova." Linha de apoio: "ChatGPT: memórias salvas e conversas anteriores. Claude: memória por tópicos e busca nas conversas passadas."

Slide B, como controlar: "Ver, corrigir e apagar: Configurações > Memória." "Conversa temporária (ChatGPT) ou anônima (Claude): não cria memória nem entra no histórico."

Slide C, sigilo: "Dado de processo digitado numa conversa comum pode virar memória e voltar em outra conversa." "Apagar a conversa não apaga a memória que saiu dela, e vice-versa." "Temporária não é sigilo absoluto: a cópia fica até 30 dias."

A palavra "contexto" no slide A é do professor (é o que liga este tema à mesa da aula); as páginas oficiais não dizem "injetado no contexto", dizem que o app escolhe o que é relevante para a resposta. O slide 27 atual ("Salvo memória ligada: veja as configurações.") continua correto.

## 4. Artificial Analysis

As tabelas só aparecem com JavaScript e foram lidas no navegador em 22/10/2026. Cada nível de esforço de um mesmo modelo ("max", "xhigh", "high") é uma linha separada; empates seguem a ordem da tabela.

### 4.1. Intelligence Index (v4.3.2)

O que é: nota de 0 a 100 que resume dez provas aplicadas pela própria Artificial Analysis (AA-Briefcase v1.1, GDPval-AA v2.1, AutomationBench-AA, Terminal-Bench 4.0, SciCode, Humanity's Last Exam, GDP.pdf, CritPt, AA-Omniscience e AA-LCR v1.1), com pesos de 30% para tarefas de agente, 30% gerais, 20% programação e 20% raciocínio científico; quase tudo em texto e em inglês.

| posição | modelo | nota |
|---|---|---|
| 1 | Claude Opus 5.5 (max with fallback) | 58 |
| 2 | Claude Sonnet 5.5 (max with fallback) | 56 |
| 3 | Claude Opus 5.5 (xhigh with fallback) | 56 |
| 4 | Muse Wonder Full (max), Meta | 56 |
| 5 | Claude Opus 5.5 (high with fallback) | 54 |
| 6 | Claude Fable 5.1 (max with fallback) | 53 |
| 7 | Claude Fable 5.1 (xhigh with fallback) | 53 |
| 8 | GPT-6 Astra (max), OpenAI | 53 |
| 9 | Gemini 4 Argon (high), Google | 53 |
| 10 | Muse Wonder (max), Meta | 52 |

- Fonte: https://artificialanalysis.ai/leaderboards/models e https://artificialanalysis.ai/ ; metodologia em https://artificialanalysis.ai/methodology/intelligence-benchmarking. A tabela não traz data; o registro de mudanças da página inicial mostra a última avaliação em "22 Oct". Lido em 22/10/2026.
- Para a tela, uma linha por modelo (sem repetir variantes): Claude Opus 5.5, 58; Claude Sonnet 5.5, 56; Muse Wonder Full, 56; Claude Fable 5.1, 53; GPT-6 Astra, 53; Gemini 4 Argon, 53. Rodapé: "Artificial Analysis Intelligence Index v4.3.2, lido em 22/10/2026; melhor variante de cada modelo."

### 4.2. Legal Index

O que é: média ponderada de sete medidas de trabalho jurídico (conhecimento, trabalho de agente, raciocínio, contexto longo, não alucinação e uso de ferramentas), com tarefas de direito americano e europeu, não brasileiro. Os pesos de `apuracao.md`, item 9, conferem com a tabela de metodologia e com o FAQ da própria página: 35% AA-Omniscience Law Accuracy; 25% GDPval-AA v2.1 e AA-Briefcase v1.1; 15% HLE; 10% LCR e GDP.pdf; 10% AA-Omniscience Law Non-Hallucination; 5% AutomationBench-AA Support and Operations.

| posição | modelo | nota |
|---|---|---|
| 1 | Claude Opus 5.5 (max with fallback) | 63 |
| 2 | Claude Fable 5.1 (max with fallback) | 60 |
| 3 | Gemini 4 Argon (high) | 60 |
| 4 | GPT-6 Astra (max) | 59 |
| 5 | GPT-6.1 Sol (max) | 58 |
| 6 | Claude Sonnet 5.5 (max with fallback) | 56 |
| 7 | Muse Wonder Full (max) | 55 |
| 8 | Grok 4.7 (xhigh) | 54 |
| 9 | Muse Wonder (max) | 52 |
| 10 | Gemini 3.8 Flash (high) | 52 |

- Fonte: https://artificialanalysis.ai/models/capabilities/legal, que redireciona para https://artificialanalysis.ai/indexes/legal. Página sem data; lida em 22/10/2026. O gráfico mostra uma variante por modelo (27 de 226). O FAQ da página informa que Claude Fable 5.1 (xhigh) e Claude Opus 5.5 (xhigh) também têm 61; contadas todas as variantes, o segundo lugar seria 61, não 60. Para a tela, usar a tabela acima e o rodapé "uma variante por modelo, como no gráfico da página".

## 5. arena.ai

O nome mudou de LMArena para Arena: "LMArena is now Arena", post oficial assinado por "Arena Team", 28/01/2026, https://arena.ai/blog/lmarena-is-now-arena.

### 5.1. Como a nota da arena de texto é calculada

Pessoas comparam às cegas duas respostas e votam na melhor; um modelo estatístico de comparações em pares (Bradley-Terry), "similar to the Elo rating system", transforma os votos em pontos. Fontes: FAQ, https://arena.ai/faq (sem data); "Does Style Matter?", https://arena.ai/blog/style-control, 29/08/2024, atualizado em 13/06/2025 (regressão logística sobre os votos, com controle de estilo como variável extra); política do placar, https://arena.ai/blog/policy/, atualizada em 01/09/2026 (exige "at least 1,000" votos para a nota se estabilizar). O ajuste "Style Control" estava ativo ao abrir a página, mas nenhuma página lida diz que é o padrão.

### 5.2. Arena de texto, geral

| posição | faixa de posição | modelo | nota | votos |
|---|---|---|---|---|
| 1 | 1–3 | Gemini 4 Argon (High) | 1524 ±9 | 4.900 |
| 2 | 1–8 | Muse Wonder (Max) | 1510 ±9 | 5.099 |
| 3 | 1–7 | Claude Opus 5.5 (High) | 1509 ±7 | 9.496 |
| 4 | 2–10 | Claude Fable 5 (High) | 1504 ±4 | 43.399 |
| 5 | 2–10 | Claude Opus 4.6 (High) | 1503 ±3 | 82.619 |
| 6 | 2–12 | Claude Fable 5.1 (Max) | 1503 ±6 | 15.623 |
| 7 | 2–12 | Claude Opus 4.7 (High) | 1501 ±4 | 65.131 |
| 8 | 4–17 | Claude Opus 4.6 | 1497 ±3 | 87.372 |
| 9 | 3–18 | Gemini 3.8 Flash (High) | 1496 ±5 | 41.423 |
| 10 | 4–19 | Muse Spark 1.3 (Max) | 1495 ±5 | 19.323 |

Fonte: https://arena.ai/leaderboard/text (redireciona para https://arena.ai/leaderboard/chat/text). Data mostrada: 20/10/2026; 8.900.458 votos no total; 418 modelos. Lido em 22/10/2026.

### 5.3. Categoria jurídica ("Legal & Government")

Existe, dentro de "Occupational": https://arena.ai/leaderboard/chat/text/industry-legal-and-government. Data mostrada: 20/10/2026; 597.033 votos; 391 modelos. Lido em 22/10/2026.

| posição | faixa de posição | modelo | nota | votos |
|---|---|---|---|---|
| 1 | 1–23 | Gemini 4 Argon (High) | 1536 ±30 | 399 |
| 2 | 1–24 | Muse Spark 1.2 (xHigh) | 1527 ±22 | 757 |
| 3 | 1–32 | Claude Fable 5 (High) | 1511 ±11 | 3.627 |
| 4 | 1–28 | Claude Opus 4.7 (High) | 1511 ±9 | 5.261 |
| 5 | 1–34 | Kimi K3 (Max) | 1510 ±12 | 2.682 |
| 6 | 1–28 | Claude Opus 4.6 (High) | 1510 ±8 | 6.744 |
| 7 | 1–69 | Muse Wonder (Max) | 1508 ±29 | 441 |
| 8 | 1–33 | Claude Opus 4.6 | 1507 ±8 | 7.001 |
| 9 | 1–58 | Claude Opus 5.5 (High) | 1505 ±22 | 821 |
| 10 | 1–42 | Claude Opus 5 (Max) | 1504 ±12 | 2.901 |

Todas as faixas de posição começam em 1: os dez podem estar em primeiro lugar, o que é empate estatístico. Se for à tela, dizer isso.

### 5.4. Ranking de agentes (escolhido pelo professor)

Lido pelo coordenador desta apuração no navegador em 23/10/2026, em https://arena.ai/leaderboard/agent ("Agent Arena | Capabilities", categoria "Overall"). Os percentuais da lista que o professor trouxe da página inicial ("Top 10 Agents · Best Overall") são idênticos aos da coluna "Net Improvement" desta página: Claude Opus 5.5 20,92%; GPT-6 Astra 14,70%; Claude Fable 5.1 14,17%; GPT-6.1 Sol 13,55%; Claude Sonnet 5.5 12,67%; Gemini 4 Argon 12,03%; Muse Wonder Full 11,26%; GPT-6 Sol 9,36%; Claude Fable 5 8,31%; Claude Opus 5 8,09% (todos na versão "Max", salvo Fable 5, "High"). A página inicial em si não mostrou esse bloco no navegador desta sessão.

O que o percentual significa, segundo o FAQ da própria página: o modo agente manda cada sessão real para um modelo sorteado e observa como ele trabalha como orquestrador (o modelo que decide quais ferramentas usar). Para cada sinal (sucesso confirmado pelo usuário, elogio contra reclamação, obediência a correções, confiabilidade dos comandos, ferramentas inventadas), a nota é a diferença, em pontos percentuais, entre o modelo e a média de todos ("net improvement: how much better or worse a behavior becomes when substituting in a particular model. Positive means above average"). O número principal é a média ponderada desses sinais, com intervalo de confiança de 95%; não há votação entre duas respostas nem Bradley-Terry.

Para a tela: "Agentes na arena: quanto cada modelo melhora o resultado de tarefas reais em relação ao modelo médio." Rodapé: "arena.ai, Agent Arena, Overall, 20/10/2026."

Divergência a resolver antes de projetar: o professor anotou 367.936.358 sessões; a página do placar de agentes mostra "Oct 20, 2026 · 2,731,078 sessions · 57 models". O número maior provavelmente é o total da plataforma exibido na página inicial, que esta sessão não conseguiu ver. Recomendação: usar "2,7 milhões de sessões" com a data de 20/10/2026, que é o número que o próprio placar mostra, ou abrir a página inicial no navegador e conferir a legenda do número maior.

Metodologia detalhada, não lida nesta sessão: https://arena.ai/blog/agent-arena-methodology/.

## 6. Definição de IA: OCDE e PL 2338/2023 (slide 4)

### 6.1. OCDE

Texto integral vigente, relido no PDF oficial em 22/10/2026:

> "An AI system is a machine-based system that, for explicit or implicit objectives, infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments. Different AI systems vary in their levels of autonomy and adaptiveness after deployment."

Tradução livre: "Sistema de IA é um sistema baseado em máquina que, para objetivos explícitos ou implícitos, infere, a partir da entrada que recebe, como gerar saídas, como previsões, conteúdos, recomendações ou decisões, que podem influenciar ambientes físicos ou virtuais. Os sistemas de IA variam em seu grau de autonomia e de capacidade de adaptação depois de implantados."

- Fonte: OCDE, Recommendation of the Council on Artificial Intelligence, OECD/LEGAL/0449, https://legalinstruments.oecd.org/public/doc/648/648.en.pdf. Definição revista pelo Conselho em 8/11/2023; Recomendação revista em 3/5/2024. Lido em 22/10/2026 (texto extraído do PDF baixado, idêntico ao da apuração anterior).

Decomposição didática (explicações são do professor, não da OCDE):

| parte | trecho | para leigo |
|---|---|---|
| 1 | "sistema baseado em máquina" | É programa rodando em computador, não pessoa nem regra escrita em papel. |
| 2 | "para objetivos explícitos ou implícitos" | Persegue um alvo, que pode ter sido dado por alguém ou ter ficado embutido no treino. |
| 3 | "infere, a partir da entrada que recebe, como gerar saídas" | Não segue um passo a passo fixo: deduz do que recebe qual resposta dar. |
| 4 | "previsões, conteúdos, recomendações ou decisões que podem influenciar ambientes físicos ou virtuais" | O que sai dele tem efeito no mundo, de um texto na tela a uma porta que se abre. |
| 5 | "variam em autonomia e capacidade de adaptação depois de implantados" | Uns precisam de comando a cada passo, outros agem sozinhos; uns continuam mudando com o uso, outros não. |

### 6.2. PL 2338/2023

Texto integral do art. 4º, I, na versão aprovada pelo Senado e recebida pela Câmara, relido no inteiro teor em 22/10/2026:

> "I – sistema de inteligência artificial (IA): sistema baseado em máquina que, com graus diferentes de autonomia e para objetivos explícitos ou implícitos, infere, a partir de um conjunto de dados ou informações que recebe, como gerar resultados, em especial previsão, conteúdo, recomendação ou decisão que possa influenciar o ambiente virtual, físico ou real;"

- Fonte: Câmara dos Deputados, inteiro teor do PL 2338/2023 (apresentação em 17/03/2025), https://www.camara.leg.br/proposicoesWeb/prop_mostrarintegra?codteor=2868197 (PDF de 36 páginas). Lido em 22/10/2026.

Situação na Câmara, relida na API de dados abertos em 22/10/2026 (https://dadosabertos.camara.leg.br/api/v2/proposicoes/2487262 e /tramitacoes): situação "Aguardando Parecer"; regime "Prioridade (Art. 151, II, RICD)"; "Proposição Sujeita à Apreciação do Plenário"; último andamento em 02/09/2026, notificação de apensação (PL 3060/2026 apensado em 01/09/2026). Nada mudou desde a apuração anterior.

Para a tela: "PL 2338/2023: aprovado no Senado em 10/12/2024; na Câmara, aguardando parecer (situação em 22/10/2026). Ainda não é lei."

Decomposição didática:

| parte | trecho | para leigo |
|---|---|---|
| 1 | "sistema baseado em máquina" | Mesmo ponto de partida da OCDE: é programa de computador. |
| 2 | "com graus diferentes de autonomia" | O PL traz a autonomia para dentro da definição; a OCDE a deixa numa frase à parte. |
| 3 | "para objetivos explícitos ou implícitos" | Persegue um alvo, declarado ou embutido. |
| 4 | "infere, a partir de um conjunto de dados ou informações que recebe, como gerar resultados" | Deduz a resposta do que recebe; o PL troca "entrada" por "dados ou informações" e "saídas" por "resultados". |
| 5 | "previsão, conteúdo, recomendação ou decisão que possa influenciar o ambiente virtual, físico ou real" | Mesmos quatro tipos de saída da OCDE, com "real" acrescentado aos ambientes. |

Diferenças que valem uma frase na fala, lidas nos dois textos: o PL não menciona a "capacidade de adaptação depois de implantados" e acrescenta o ambiente "real". O AI Act europeu (art. 3(1)) não foi lido nesta sessão; não citar na tela.


## 7. Fronteira irregular (Dell'Acqua et al., 2023)

### 7.1. Números e versões

- Versão original: Working Paper 24-013 da HBS, resumo no SSRN postado em 18/09/2023 (lido na cópia do Internet Archive; o mesmo texto está no arquivo de 10/01/2024 da página da HBS). Com 758 consultores do BCG, dentro da fronteira quem usou GPT-4 fez "12.2% more tasks", "25.1% more quickly" e com "more than 40% higher quality"; fora dela, foi "19 percentage points less likely to produce correct solutions". A página atual da HBS (https://www.hbs.edu/faculty/Pages/item.aspx?num=64700) diz "19% less likely"; a formulação do original é em pontos percentuais.
- Versão publicada: Organization Science, vol. 37, n. 2, pp. 403–423, março-abril de 2026, DOI 10.1287/orsc.2025.21838. Segundo o resumo do HBS AI Institute (09/04/2026, https://aiinstitute.hbs.edu/back-to-the-beginnings-of-ai-at-work/), a qualidade subiu "about 32%" e, fora da fronteira, o acerto foi de 84,5% sem IA, 70,6% com GPT-4 e 60,0% com GPT-4 e curso de prompt. O PDF completo não foi lido (a HBS pede verificação humana).
- Para a tela, ajuste da frase de `apuracao.md`, item 8: "…na tarefa fora dela, acertaram 19 pontos percentuais menos (Dell'Acqua et al., 2023)."
- Ethan Mollick, coautor, difundiu o termo no post "Centaurs and Cyborgs on the Jagged Frontier", 16/09/2023, https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged ("what we call the 'Jagged Frontier'"). Fica confirmado que ele divulgou o termo; não que o tenha cunhado sozinho.

### 7.2. As tarefas do estudo

Fontes: BCG, "How People Can Create, and Destroy, Value with Generative AI", 21/09/2023, https://www.bcg.com/publications/2023/how-people-create-and-destroy-value-with-gen-ai, e o post de Mollick acima.

- Dentro da fronteira: desenvolver um calçado novo, em 18 subtarefas criativas e de escrita, como "Propose at least 10 ideas for a new shoe targeting an underserved market or sport", "Segment the footwear industry market based on users", criar slogans e propor como testá-los, "Draft a press release marketing copy" e escrever um memorando aos funcionários.
- Fora da fronteira: a empresa fictícia "Kleding". Com notas de entrevistas com executivos e uma planilha financeira por marca, o consultor devia dizer em qual marca o CEO deveria investir e justificar com dados. A resposta certa dependia de conciliar a planilha "with subtle clues embedded in interview notes" (resumo da HBS). Era a tarefa feita para a IA errar de modo convincente.

### 7.3. Seis exemplos jurídicos (ilustrativos do professor, não do estudo)

Dentro da fronteira:

1. Primeira versão de ofício ou minuta de rotina. Análoga ao press release e ao memorando, escrita persuasiva a partir de briefing, onde a IA mais elevou a qualidade.
2. Resumo de uma petição longa entregue ao modelo. Organizar e condensar texto que está na própria conversa é análogo à segmentação do mercado: nada depende de fonte externa.
3. Lista de teses e argumentos possíveis para um caso. Corresponde às "10 ideas" de calçado: gerar alternativas, que o advogado depois filtra.

Fora da fronteira:

4. Dizer se um precedente existe e se diz o que se afirma. Como na Kleding, a resposta vem plausível e só a conferência na fonte mostra o erro (é o caso Avianca do slide 30).
5. Contar um prazo que depende de feriado local ou de suspensão de expediente do tribunal. O detalhe decisivo está fora do texto dado, como a pista escondida nas entrevistas.
6. Concluir algo que exige cruzar um documento dos autos com um detalhe escondido em outro (a data numa certidão, a ressalva num laudo). É a estrutura exata da tarefa Kleding, em que confiar na IA derrubou o acerto.

Para a tela, uma linha por coluna: "Dentro: minutar, resumir, listar argumentos." "Fora: conferir precedente, contar prazo com feriado local, cruzar documentos dos autos." Pílula: "exemplos do professor".

## 8. Pesos e multiplicação de matrizes (roteiro para não técnicos)

Roteiro em seis passos, com exemplo verificado (conta refeita em Python em 22/10/2026). Os nomes "vetor" e "matriz" podem ficar só na fala.

1. A palavra vira uma lista de números. Cada token entra no modelo como uma lista fixa de números; no exemplo, três: [2, 1, 3]. Nos modelos reais, a lista tem milhares de números.
2. Cada número é multiplicado por um peso. Peso é um número que o modelo aprendeu e guarda. Para formar a primeira saída, os pesos são 1, 0 e 1: 2×1 + 1×0 + 3×1.
3. Soma. Os produtos se somam: 2 + 0 + 3 = 5. Para a segunda saída, outra coluna de pesos (0, 2 e −1): 2×0 + 1×2 + 3×(−1) = 0 + 2 − 3 = −1. Três números entraram, dois saíram: [5, −1].
4. Um filtro simples. Antes de seguir, valores negativos viram zero (é a função que os técnicos chamam de ReLU): [5, −1] vira [5, 0].
5. Passa à camada seguinte. A lista [5, 0] é a entrada da próxima camada, que repete o processo com seus próprios pesos.
6. Muitas camadas. Um modelo grande empilha muitas camadas e tem bilhões de pesos (o Llama 3.1 405B tem 405 bilhões, item 3 da apuração anterior); a conta de cada peso continua sendo multiplicar e somar.
7. O treino ajusta os pesos. No começo os pesos são aleatórios; o treino compara a resposta com o texto real e corrige um pouco cada peso, repetidas vezes, até a previsão da próxima palavra melhorar.

Tabela do exemplo para a tela (a matriz 3×2, cada coluna é um conjunto de pesos):

| entrada | pesos da saída 1 | pesos da saída 2 |
|---|---|---|
| 2 | 1 | 0 |
| 1 | 0 | 2 |
| 3 | 1 | −1 |
| soma | 5 | −1 |
| depois do filtro | 5 | 0 |

Referências de estilo, para consulta e não para cópia:

- 3Blue1Brown (Grant Sanderson), "But what is a GPT? Visual intro to Transformers", Deep Learning, capítulo 5, 01/04/2024; página da lição: https://www.3blue1brown.com/lessons/gpt (título na página: "Transformers, the tech behind LLMs"). Lido em 22/10/2026: a lição diz que os parâmetros se chamam pesos porque interagem com os dados "through weighted sums" e que esses pesos ficam empacotados em matrizes, multiplicadas por vetores; cita os 175 bilhões de pesos do GPT-3 em "just under 28,000" matrizes.
- Financial Times, Visual Storytelling Team e Madhumita Murgia, "Generative AI exists because of the transformer", 12/09/2023, https://ig.ft.com/generative-ai/. Título e data lidos no HTML da página em 22/10/2026 (metadado "2023-09-12T05:00:00"); o corpo é interativo e não foi lido por robô. O que se aproveita é o estilo: uma frase por tela, a palavra se transformando em números diante do leitor.
- Ressalva: o exemplo é deliberadamente minúsculo e não reproduz figuras das duas fontes. A ordem real dentro de um transformer (atenção, camadas de neurônios, normalização) é mais complexa; o roteiro descreve a camada de neurônios, que é a parte "multiplica e soma".

## 9. O que ficou sem fonte

- Limite de contexto do ChatGPT por plano e do plano gratuito do Claude: sem página oficial lida (help.openai.com/en/articles/12003714 e chatgpt.com/pricing deram 403). O deck fica sem esses números.
- Método do ChatGPT e do Gemini para resumir conversa longa: não documentado em página oficial lida. O slide 25 usa frase genérica.
- Modelo padrão por plano no ChatGPT, modelo do app Grok e versão do Muse no Meta AI: não confirmados. O slide 49 passa a falar em "família mais recente".
- Licença do Mistral Large 4: não anunciada.
- Números de contexto longo do GPT-5.5 (página da OpenAI com 403): não usados.
- Página inicial da arena.ai: o bloco "Top 10 Agents" e o total de 367.936.358 sessões não apareceram no navegador desta sessão; os percentuais foram conferidos no placar de agentes, cujo total é 2.731.078 sessões.
- PDF completo de Dell'Acqua et al. (HBS exige verificação humana) e metodologia do placar de agentes (https://arena.ai/blog/agent-arena-methodology/): não lidos; nada do deck depende deles.
