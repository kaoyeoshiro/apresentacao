# Apuração de fatos da Aula 1 (curso de IA)

Data de leitura de todas as fontes: 22/10/2026, salvo indicação. Cada item traz o texto que pode ir à tela, a fonte, a data da fonte e uma ressalva. O que não foi confirmado em fonte primária ou oficial leva `[CONFERIR]` com o motivo.

## 1. Definição de sistema de IA da OCDE (slide 4)

Texto vigente, em inglês, na Recomendação do Conselho sobre Inteligência Artificial (OECD/LEGAL/0449), lido no PDF oficial:

> "An AI system is a machine-based system that, for explicit or implicit objectives, infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments. Different AI systems vary in their levels of autonomy and adaptiveness after deployment."

Tradução livre para a tela: "Sistema de IA é um sistema baseado em máquina que, para objetivos explícitos ou implícitos, infere, a partir da entrada que recebe, como gerar saídas, como previsões, conteúdos, recomendações ou decisões, capazes de influenciar ambientes físicos ou virtuais. Os sistemas variam em autonomia e em capacidade de adaptação depois de implantados."

Versão curta: "Sistema de máquina que, a partir do que recebe, infere como gerar previsões, conteúdos, recomendações ou decisões (OCDE, 2024, tradução livre)."

- Fonte: OCDE, Recommendation of the Council on Artificial Intelligence, OECD/LEGAL/0449, PDF oficial em https://legalinstruments.oecd.org/public/doc/648/648.en.pdf (página do instrumento: https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449). Adotada em 2019; definição revista pelo Conselho em 8/11/2023; Recomendação revista em nível ministerial em 3/5/2024 (datas lidas no próprio PDF).
- Apoio: OECD.AI, "Updated OECD definition of an AI system", 29/11/2023, https://oecd.ai/en/wonk/ai-system-definition-update.
- Ressalva: não há versão oficial em português; a tradução é livre e deve ser rotulada assim. A definição do AI Act europeu (art. 3(1)) segue a mesma redação, mas não foi lida no texto oficial da UE nesta sessão.

## 2. PL 2338/2023: definição e situação legislativa (slide 4)

Texto do art. 4º, I, na versão aprovada pelo Senado e enviada à Câmara (lido no inteiro teor da Câmara):

> "sistema de inteligência artificial (IA): sistema baseado em máquina que, com graus diferentes de autonomia e para objetivos explícitos ou implícitos, infere, a partir de um conjunto de dados ou informações que recebe, como gerar resultados, em especial previsão, conteúdo, recomendação ou decisão que possa influenciar o ambiente virtual, físico ou real;"

Situação em 22/10/2026, para a tela: "PL 2338/2023: aprovado no Senado em 10/12/2024; na Câmara desde 17/03/2025, aguardando parecer da comissão especial. Ainda não é lei."

- Fontes: Câmara dos Deputados, inteiro teor do PL 2338/2023 apresentado em 17/03/2025, https://www.camara.leg.br/proposicoesWeb/prop_mostrarintegra?codteor=2868197; ficha da proposição (id 2487262) pela API de dados abertos, https://dadosabertos.camara.leg.br/api/v2/proposicoes/2487262 (página humana: https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2487262). Situação lida: "Aguardando Parecer", regime de prioridade (art. 151, II, RICD), sujeito à apreciação do Plenário, última tramitação em 02/09/2026 (apensação de outros projetos). Senado Federal, matéria 157233, https://www25.senado.leg.br/web/atividade/materias/-/materia/157233: "Aprovada pelo Plenário" em 10/12/2024, remetida à Câmara.
- Ressalva: como passou por emendas, o texto deve voltar ao Senado se a Câmara o alterar; isso é regra constitucional (art. 65, parágrafo único), não fato apurado do PL. Reconferir a ficha da Câmara na véspera da aula, porque a situação pode mudar.

## 3. Volume de treino e parâmetros de um modelo aberto (slides 13 e 14)

Para a tela: "Llama 3.1 405B (Meta, 2024): cerca de 15 trilhões de tokens no pré-treino e 405 bilhões de parâmetros."

- Fonte: Meta, Model Card do Llama 3.1, repositório oficial meta-llama/llama-models, https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md. Trechos lidos: "Llama 3.1 was pretrained on ~15 trillion tokens of data from publicly available sources"; tamanhos "8B, 70B and 405B"; data de lançamento 23/07/2024; corte dos dados de pré-treino em dezembro de 2023.
- Ressalva: é um modelo de 2024, escolhido porque o fabricante publicou os dois números; modelos mais recentes não foram buscados para este dado. "Token" não é palavra: 15 trilhões de tokens equivalem a menos palavras (ver item 5).

## 4. Janela de contexto de um modelo atual (slide 23)

Para a tela: "Claude Opus 5.5: janela de 1 milhão de tokens (documentação da Anthropic)."

- Fonte: Anthropic, Models overview, https://platform.claude.com/docs/en/about-claude/models/overview (redireciona de docs.claude.com). Tabela lida: Claude Fable 5.1, Opus 5.5, Sonnet 5.5 e Haiku 5.5, todos com "Context window: 1M tokens" e saída máxima de 128K tokens. A própria página diz que 1M tokens equivalem a "roughly 555k words" no tokenizador atual da Anthropic.
- Alternativa: OpenAI, página de modelos, https://developers.openai.com/api/docs/models: GPT-6 Astra, GPT-6.1 Sol e GPT-6 Luna com janela de "1.05M" tokens.
- Ressalva: o número vale para a API. O limite no app (claude.ai, ChatGPT) depende do plano e não foi conferido `[CONFERIR]` (procurar na central de ajuda de cada app). Página sem data de publicação; lida em 22/10/2026.

## 5. Medição de tokens (slides 16, 17, 18 e 23)

Ferramenta: biblioteca `tiktoken` 0.14.0 (OpenAI), codificação `o200k_base`, instalada em ambiente temporário; medido em 22/10/2026. O tokenizador web da OpenAI, aba "GPT-5.x & O1/3", devolveu os mesmos IDs de token para as mesmas frases (conferido no navegador), o que mostra que essa aba usa `o200k_base`.

(a) "inconstitucionalidade" vira 4 tokens: `in` | `constit` | `ucional` | `idade`. Com espaço antes (no meio de frase), o primeiro bloco passa a ser ` in`.

(b) "O réu agravou da decisão." vira 8 tokens: `O` | ` ré` | `u` | ` agrav` | `ou` | ` da` | ` decisão` | `.` (o espaço vai colado ao início da palavra seguinte; o ponto é um token à parte).

(c) Parecer fictício em `decks/curso-ia-aula1/apuracao-parecer-ficticio.md` (pedido de reequilíbrio em contrato de pavimentação de município inventado, sem dado real): 1.486 palavras (contagem por espaços, `wc -w`), 2.056 tokens em `o200k_base`, razão de 1,38 token por palavra. Para comparação, a codificação antiga `cl100k_base` (GPT-4) dá 2.589 tokens, 1,74 por palavra.

Para a tela do slide 17: "Um parecer de 3 páginas: cerca de 2.000 tokens (1.486 palavras; 1,4 token por palavra; tokenizador da OpenAI, o200k_base, medido em 22/10/2026)."

(d) Janela em páginas, a 500 palavras por página: 1.000.000 ÷ 1,384 ≈ 722.800 palavras ≈ 1.450 páginas. Pela taxa que a própria Anthropic publica (1M ≈ 555 mil palavras), dá cerca de 1.100 páginas. Para a tela: "1 milhão de tokens: mais de mil páginas de parecer".

- URL do tokenizador web para o QR: https://platform.openai.com/tokenizer. No ar em 22/10/2026 (aberto no navegador, sem login; o curl simples recebe 403 por proteção anti-robô, o navegador não).
- Ressalva: cada fabricante tem seu tokenizador; o Claude não usa `o200k_base`, e a OpenAI não diz na página de modelos se o GPT-6 usa essa codificação. A conversão em páginas é ordem de grandeza, por isso a faixa "mais de mil". Não prometer na prática os mesmos blocos para quem abrir outro tokenizador.

## 6. Mata v. Avianca, Inc. (slide 28)

Para a tela: "Mata v. Avianca (Tribunal Federal de Nova York, 2023): advogados citaram seis decisões inventadas pelo ChatGPT. Em 22/06/2023, o juiz P. Kevin Castel multou-os em US$ 5.000."

- Fonte primária: Opinion and Order on Sanctions, Mata v. Avianca, Inc., No. 22-cv-1461 (PKC), S.D.N.Y., Document 54, assinada em 22/06/2023, cópia do PACER no CourtListener, https://storage.courtlistener.com/recap/gov.uscourts.nysd.575368/gov.uscourts.nysd.575368.54.0.pdf. Lido: os advogados Peter LoDuca e Steven A. Schwartz e o escritório Levidow, Levidow & Oberman "submitted non-existent judicial opinions with fake quotes and citations created by the artificial intelligence tool ChatGPT, then continued to stand by the fake opinions after judicial orders called their existence into question"; sanções do item d: "A penalty of $5,000 is jointly and severally imposed on Respondents"; além disso, cartas ao cliente e a cada juiz falsamente apontado como autor das decisões inventadas ("Varghese", "Shaboon", "Petersen", "Martinez", "Durden", "Miller").
- Ressalva: a multa decorreu também de os advogados terem sustentado as citações depois de questionados, não só do uso da ferramenta (a própria decisão diz isso). A extinção da ação principal por prescrição na mesma data é ordem separada, não lida `[CONFERIR]`. Na tela, evitar nomes dos advogados.

## 7. Liu et al., "Lost in the Middle" (slide 24B)

Para a tela: "O desempenho costuma ser maior quando a informação relevante está no começo ou no fim do contexto e cai quando está no meio (Liu et al., 2023)."

- Fonte: Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, Percy Liang, arXiv:2307.03172, https://arxiv.org/abs/2307.03172 (v1 06/07/2023, v3 20/11/2023; referência do periódico: Transactions of the Association for Computational Linguistics). Trecho do resumo: "performance is often highest when relevant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle of long contexts".
- Ressalva: medido em modelos de 2023, em duas tarefas (perguntas sobre múltiplos documentos e recuperação chave-valor). Modelos posteriores podem ter reduzido o efeito; não apresentar como lei geral. O volume e as páginas do TACL 2024 não foram conferidos `[CONFERIR]`.

## 8. Dell'Acqua et al., "Jagged Technological Frontier" (slide 31)

Para a tela: "Em 758 consultores do BCG, quem usou GPT-4 em tarefas dentro da fronteira fez 12,2% mais tarefas e 25,1% mais rápido; na tarefa fora dela, acertou 19% menos (Dell'Acqua et al., 2023)."

Quem cunhou "jagged frontier": os próprios autores do artigo ("We introduce and study the concept of a 'jagged technology frontier'"); Ethan Mollick, coautor, popularizou a expressão.

- Fonte: Harvard Business School, Working Paper 24-013, setembro de 2023, página oficial https://www.hbs.edu/faculty/Pages/item.aspx?num=64700 (lida no navegador; acesso por robô dá 403). Autores: Fabrizio Dell'Acqua, Edward McFowland III, Ethan Mollick, Hila Lifshitz-Assaf, Katherine C. Kellogg, Saran Rajendran, Lisa Krayer, François Candelon, Karim R. Lakhani. A página registra publicação em Organization Science, março-abril de 2026.
- Ressalva: o resumo da HBS diz "19% less likely"; outras versões do artigo podem falar em pontos percentuais, e a versão publicada na Organization Science não foi lida `[CONFERIR]` se citar o número. A atribuição de popularização a Mollick é conhecimento geral, não lida em fonte nesta sessão `[CONFERIR]`; na tela, basta "Dell'Acqua et al., 2023".

## 9. Legal Index (slide 37)

É o Legal Index da Artificial Analysis, um índice composto que pondera capacidades conforme a frequência com que aparecem em tarefas jurídicas reais. Os pesos do slide do professor conferem.

Para a tela: "Legal Index (Artificial Analysis): conhecimento jurídico 35%, trabalho agêntico 25%, raciocínio 15%, contexto longo 10%, não alucinação 10%, uso de ferramentas 5%."

| peso | capacidade (original) | provas usadas |
|---|---|---|
| 35% | Legal Knowledge | AA-Omniscience |
| 25% | Agentic Knowledge Work | GDPval-AA v2.1, AA-Briefcase v1.1 |
| 15% | Reasoning | HLE |
| 10% | Long-Context | LCR, GDP.pdf |
| 10% | Non-Hallucination | AA-Omniscience |
| 5% | Agentic Tool Use | AutomationBench-AA |

- Fonte: Artificial Analysis, Capability Indexes Methodology, https://artificialanalysis.ai/methodology/capability-indices (seção Legal Index); placar em https://artificialanalysis.ai/models/capabilities/legal. Página sem data; lida em 22/10/2026.
- Ressalva: empresa privada, metodologia própria e versões de provas que mudam; registrar a data de leitura no rodapé. A maior parte das provas é em inglês e de direito estrangeiro (a descrição fala em "statutes, doctrines, and procedure across jurisdictions").

## 10. LMArena (slides 39 e 40)

URL para o QR: https://arena.ai (o endereço antigo https://lmarena.ai redireciona para ele; placar em https://arena.ai/leaderboard). No ar em 22/10/2026, aberto no navegador, com o modo "Battle".

Para a tela: "Na arena, a pessoa faz uma pergunta, recebe duas respostas de modelos anônimos, vota na melhor e só depois vê os nomes; os votos formam o placar (Chiang et al., 2024)."

- Fonte do mecanismo: Wei-Lin Chiang et al., "Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference", arXiv:2403.04132, 07/03/2024, https://arxiv.org/abs/2403.04132. O resumo descreve comparações em pares com votos coletados do público (mais de 240 mil votos à época) e concordância razoável com avaliadores especialistas.
- Ressalva: o nome da plataforma mudou ao longo do tempo (Chatbot Arena, LMArena, Arena); o redirecionamento foi observado, mas não li anúncio oficial da mudança de nome `[CONFERIR]` se o nome for à tela. Mede preferência, não acerto.

## 11. Modelos fechados e abertos em outubro de 2026 (slides 47 e 48)

Apuração feita por subagente em 22/10/2026 nas páginas oficiais indicadas; o coordenador não releu cada página. Algumas páginas oficiais recusaram leitura automática (openai.com, help.openai.com, x.ai/news, posts da Microsoft); nesses casos a fonte é outra página oficial do mesmo fabricante, ou o item fica `[CONFERIR]`.

Fechados (acesso só pelo serviço de quem vende):

| empresa | família atual | produto | fonte (data) | ressalva |
|---|---|---|---|---|
| OpenAI | GPT-6 (Astra, Luna) e GPT-6.1 Sol | ChatGPT | https://deploymentsafety.openai.com/gpt-6-october (07/10/2026); https://developers.openai.com/api/docs/models | Qual modelo cada plano do ChatGPT usa `[CONFERIR]` (help.openai.com deu 403) |
| Anthropic | Claude Opus 5.5, Sonnet 5.5, Haiku 5.5; Claude Fable 5.1 no topo | Claude (app e API) | https://www.anthropic.com/news (Fable 5.1 em 15/09, Opus 5.5 em 22/09, Sonnet 5.5 em 28/09, Haiku 5.5 em 07/10/2026); tabela do item 4 | Confirmado |
| Google | Gemini 4 Argon | app Gemini, API, AI Studio | https://deepmind.google/models/model-cards/gemini-4-argon (13/10/2026); blog.google (30/09/2026) | Google anuncia mais modelos da família Gemini 4 |
| xAI (hoje SpaceXSI) | Grok 4.7 | Grok | https://docs.x.ai/developers/release-notes (setembro de 2026); model card de 21/09/2026 | Mudança de nome da empresa vista em imprensa e na documentação; se o 4.7 é o padrão do app `[CONFERIR]` (x.ai/news deu 403) |
| Meta | Muse (Muse Spark 1.3; Muse Wonder 1.0 em prévia) | Meta AI (app, WhatsApp, Instagram) | https://dev.meta.ai/docs/models (sem data); about.fb.com (Muse Spark em 08/04/2026) | Qual Muse roda hoje no app Meta AI `[CONFERIR]` |
| Microsoft | sem família principal própria; usa GPT-6/6.1 Sol e Claude Opus/Sonnet 5.5, além dos modelos internos MAI | Microsoft 365 Copilot | techcommunity.microsoft.com, posts "More Models, One Copilot" e "Available today: GPT-6.1 Sol and Claude Sonnet 5.5" | Corpo das páginas não carregou; lista e datas `[CONFERIR]`; oferta varia por licença e região |

Abertos (pesos baixáveis; "aberto" aqui é pesos disponíveis, não necessariamente licença de código aberto):

| empresa | família atual | licença | fonte (data) | ressalva |
|---|---|---|---|---|
| Meta | Muse Spark Open; Muse Glimmer 30B | Muse Model License (Spark Open); Apache 2.0 (Glimmer) | https://huggingface.co/meta-models (licença de 15/10/2026); dev.meta.ai | A Muse Model License impõe condições a grandes revendedores |
| Meta | Llama 4 (Scout, Maverick) | Llama 4 Community License | https://huggingface.co/meta-llama (último em abril de 2025) | Linha sem lançamento novo; para o slide 48, Muse Spark Open é o aberto atual da Meta |
| Google | Gemma 4 (E2B a 31B) | Apache 2.0 | https://ai.google.dev/gemma/docs/releases (31/03/2026; 12B em 03/06/2026) | Gemma 3 usava os Gemma Terms of Use |
| OpenAI | gpt-oss-120b e gpt-oss-20b | Apache 2.0 | https://huggingface.co/openai (04/08/2025) | Licença confirma; sem versão nova |
| DeepSeek | V4-Pro, V4.1-Flash | MIT | https://huggingface.co/deepseek-ai (até 17/10/2026) | Confirmado |
| Alibaba | Qwen3.8 (27B; 2.4T-A95B) | Apache 2.0 (27B); Qwen3.8-Max License (2.4T) | https://huggingface.co/Qwen (05 e 08/08/2026) | Licença muda conforme o tamanho |
| Mistral | Mistral Medium 3.5, Small 4, Large 3 | Modified MIT (Medium 3.5); Apache 2.0 (Small 4, Large 3) | https://huggingface.co/mistralai (31/03/2026) | Carro-chefe atual `[CONFERIR]` em docs.mistral.ai |
| Moonshot | Kimi K3 | Kimi K3 License (base MIT com restrição a quem revende) | https://huggingface.co/moonshotai/Kimi-K3 (13/06/2026) | Confirmado |
| Z.ai (antiga Zhipu) | GLM-5.3, GLM-5.3-Flash | GLM-5.3 License (base MIT com restrição); Flash em MIT | https://huggingface.co/zai-org (25/08/2026) | Confirmado |

Opcionais, se couber: IBM Granite 4.2 (Apache 2.0) e NVIDIA Nemotron (licença NVIDIA), só listados nas contas oficiais do Hugging Face.

Para a tela, rodapé: "seleção verificada em 22/10/2026". Ressalva geral: a grade muda a cada mês; reconferir na véspera.

### Logos baixados (`midia/logos/`)

Checagem feita duas vezes (subagente e coordenador): `file` confirma SVG ou PNG em todos; nenhum SVG contém `<script`, atributo `on…=` ou `javascript:`. Cores e conteúdo originais. Todos são marcas registradas: uso só nominativo, para identificar empresa ou produto, sem sugerir patrocínio. A "licença" abaixo é a que a página de origem declara para o arquivo, não autorização de uso da marca.

| arquivo | empresa | origem | licença / termos |
|---|---|---|---|
| openai.svg | OpenAI (símbolo) | https://upload.wikimedia.org/wikipedia/commons/6/66/OpenAI_logo_2025_%28symbol%29.svg | Commons: domínio público; marca registrada |
| openai-wordmark.svg | OpenAI (nome) | https://upload.wikimedia.org/wikipedia/commons/a/af/OpenAI_logo_2025_%28wordmark%29.svg | Commons: domínio público; marca registrada |
| anthropic.svg | Anthropic | https://upload.wikimedia.org/wikipedia/commons/7/78/Anthropic_logo.svg | Commons: domínio público; marca registrada |
| claude.svg | Claude (símbolo) | https://upload.wikimedia.org/wikipedia/commons/b/b0/Claude_AI_symbol.svg | Commons: CC0; marca registrada |
| claude-wordmark.svg | Claude (nome) | https://upload.wikimedia.org/wikipedia/commons/8/8a/Claude_AI_logo.svg | Commons: domínio público; marca registrada |
| gemini.svg | Google Gemini (ícone) | https://upload.wikimedia.org/wikipedia/commons/1/1d/Google_Gemini_icon_2025.svg | Commons: domínio público; marca registrada |
| gemini-wordmark.svg | Google Gemini (nome) | https://upload.wikimedia.org/wikipedia/commons/d/d9/Google_Gemini_logo_2025.svg | Commons: domínio público; marca registrada |
| grok.svg | Grok | https://upload.wikimedia.org/wikipedia/commons/f/f7/Grok-feb-2025-logo.svg | Commons: domínio público; marca registrada; se ainda é o logo em uso `[CONFERIR]` em grok.com |
| xai.svg | xAI | https://upload.wikimedia.org/wikipedia/commons/5/57/XAI-Logo.svg | Commons: domínio público; desatualizado após a mudança para SpaceXSI, preferir o logo do Grok |
| meta.svg | Meta | https://upload.wikimedia.org/wikipedia/commons/7/7b/Meta_Platforms_Inc._logo.svg | Commons: domínio público; marca registrada |
| meta-ai.svg | Meta AI (usar para Muse) | https://upload.wikimedia.org/wikipedia/commons/2/2f/Meta_AI_Logo_%282026%29.svg | Commons: domínio público; marca registrada |
| copilot.svg | Microsoft Copilot | https://res.cdn.office.net/officehub/images/content/images/unauth/copilot-app-4b262e7e56.svg (servidor da Microsoft) | Arquivo da Microsoft; termos de marca `[CONFERIR]` na página de marcas da Microsoft |
| gemma.png | Google Gemma | https://upload.wikimedia.org/wikipedia/commons/6/6d/Gemma_icon.png (ícone do repositório google-deepmind/gemma) | Commons: Apache 2.0; marca registrada |
| deepseek.svg | DeepSeek | https://upload.wikimedia.org/wikipedia/commons/e/ec/DeepSeek_logo.svg | Commons: MIT; marca registrada |
| qwen.svg | Alibaba Qwen | https://upload.wikimedia.org/wikipedia/commons/6/65/Qwen_Logo.svg | Commons: Apache 2.0; marca registrada |
| mistral.svg | Mistral AI | https://upload.wikimedia.org/wikipedia/commons/e/e6/Mistral_AI_logo_%282025%E2%80%93%29.svg | Commons: domínio público; marca registrada |
| kimi.png | Moonshot Kimi | https://raw.githubusercontent.com/MoonshotAI/Kimi-K3/HEAD/assets/kimi-logo.png (repositório oficial) | Termos de marca não publicados `[CONFERIR]` |
| zai.svg | Z.ai / GLM | https://raw.githubusercontent.com/zai-org/GLM-5/HEAD/resources/logo.svg (repositório oficial) | Termos de marca não publicados `[CONFERIR]` |

Faltantes: Llama (a Meta não publica logo próprio; os candidatos do Commons eram de outros projetos e foram descartados) e Muse (sem logo próprio; usar `meta-ai.svg` ou `meta.svg`). Os créditos ainda não foram lançados em `midia/creditos.json`, porque esta tarefa só podia escrever na pasta de logos.

## 12. Busca de jurisprudência do STJ (slide 29)

URL para o QR: https://processo.stj.jus.br/SCON/ (página "Pesquisa de Jurisprudência do STJ", com opção de busca por número). No ar em 22/10/2026, aberta no navegador sem desafio.

- O endereço https://scon.stj.jus.br/SCON/ respondeu, mas abriu uma tela de "Verificação automática em andamento" (proteção anti-robô do STJ) que não foi contornada. Para o QR, usar o endereço processo.stj.jus.br, e o professor testa os dois no celular na véspera.
- Ressalva: com 30 ou mais celulares na mesma rede, a proteção anti-robô pode pedir desafio a alguns; manter a rota impressa.
