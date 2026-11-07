# Futuro da IA e assistentes pessoais: dados para a Aula 4

Pesquisa de apoio para a Aula 4 do Dia 2 do curso co.juris, feita em 06/11/2026; todas as URLs foram acessadas nessa data. O grau de confiança segue a regra das outras notas desta pasta. É **alto** quando o dado foi lido na fonte primária (registro na SEC, página oficial da empresa, central de ajuda, relatório original). É **médio** quando vem de veículo jornalístico que cita a fonte primária, ou quando a fonte primária só sustenta o dado por inferência. É **baixo** quando há uma única fonte secundária, números conflitantes ou agregador de qualidade incerta. O que não se confirmou vai marcado "não confirmado", com o lugar onde se procurou.

## 1. Custo de computação da Anthropic no S-1/A

O documento é a Emenda nº 1 ao Formulário S-1 da Anthropic, PBC, "As filed with the Securities and Exchange Commission on November 2, 2026" (índice do EDGAR: data de protocolo 2026-11-02). O arquivo foi baixado inteiro e lido por busca textual.

| Afirmação | Dado ou citação curta | Data | URL | Confiança |
|---|---|---|---|---|
| A métrica do slide existe e se chama "Compute and infrastructure" como porcentagem da receita | 1.056% (2023), 653% (2024), 160% (2025), 172% (jan-set/2025), 57% (jan-set/2026) | S-1/A, 02/11/2026 | https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm | alto |
| Valores absolutos da linha | US$ 433 mi (2023), US$ 2.522 mi (2024), US$ 7.326 mi (2025), US$ 18.808 mi (jan-set/2026), sobre receita de US$ 33.242 mi | S-1/A, 02/11/2026 | mesma URL | alto |
| Definição: inclui todas as cargas de trabalho, treino incluído | "supports the full range of workloads for our models, including research, model development, serving customers, and internal usage of Claude" | S-1/A, 02/11/2026 (MD&A e nota de políticas contábeis) | mesma URL | alto |
| A empresa não separa o gasto por carga de trabalho na linha principal | "plan, incur, and assess it on a total basis rather than by individual workload" | S-1/A, 02/11/2026 | mesma URL | alto |
| Desde 2025 a demonstração de resultados é por natureza; custo da receita e P&D deixaram de ser linhas próprias | "cost of revenue, gross profit (loss), research and development ... are no longer presented as separate line items" | S-1/A, 02/11/2026 (Nota 2) | mesma URL | alto |
| Visão funcional, só em nota: custo da receita (quase todo computação para servir clientes) | US$ 26 mi (2023), US$ 752 mi (2024), US$ 2.773 mi (2025), US$ 4.812 mi (jan-set/2026); "Substantially all of cost of revenue consists of compute and infrastructure costs associated with customer-serving workloads" | S-1/A, 02/11/2026 (Nota 8, Supplemental Operating Expense Information) | mesma URL | alto |
| Visão funcional: P&D, onde fica a computação de treino | US$ 422 mi (2023), US$ 2.275 mi (2024), US$ 6.338 mi (2025), US$ 19.240 mi (jan-set/2026); P&D "primarily consist of compute and infrastructure costs associated with model development, research, and internal usage workloads, personnel-related costs ..." | S-1/A, 02/11/2026 (Nota 8) | mesma URL | alto |
| Computação do plano gratuito fica em vendas e marketing | S&M inclui "compute and infrastructure costs associated with providing free access" | S-1/A, 02/11/2026 (Nota 8) | mesma URL | alto |
| Custo da receita como fração da receita (cálculo próprio a partir da Nota 8) | cerca de 195% (2024), 60% (2025), 14,5% (jan-set/2026) | cálculo sobre o S-1/A | mesma URL | alto (aritmética) |
| Trimestres de 2026 | computação e infraestrutura caiu de 251% da receita (1º tri/2025) para 48% (2º tri/2026) e subiu para 58% (3º tri/2026), incluindo US$ 5,0 bi de computação de curto prazo, mais cara | S-1/A, 02/11/2026 | mesma URL | alto |

A resposta direta é que os 57% **incluem o treino**. A linha "Compute and infrastructure" soma toda a computação da empresa (pesquisa, desenvolvimento de modelos, atendimento a clientes e uso interno do Claude), e o prospecto diz expressamente que a Anthropic não a separa por carga de trabalho. O valor isolado do treino não aparece em lugar nenhum do documento. O mais perto disso é a nota 8, que reapresenta as despesas por função: ali a computação de treino e pesquisa está dentro de P&D (US$ 19,24 bi em jan-set/2026), misturada com pessoal, software e rateio de despesas gerais, enquanto a computação de servir clientes pagantes está no custo da receita (US$ 4,81 bi, ou cerca de 14,5% da receita no mesmo período). Isso muda a leitura do slide. Se a turma ouvir "custo de computação" como custo de responder perguntas, o número engana pela metade, porque o atendimento custa bem menos que 57% e o grosso do gasto vai para os próximos modelos. A nota anterior desta pasta (`dia2-economia-subsidio-bolha.md`) dizia que o subsídio estava "no treino dos modelos seguintes"; o S-1/A confirma a direção, mas o treino já está dentro dos 57%, e não fora deles. Sugestão de rótulo para o slide: "computação total (treino, pesquisa e atendimento) sobre a receita".

## 2. Assistentes pessoais de IA (retrato de novembro de 2026)

### 2.1. Os cinco do slide e o OpenClaw

| Afirmação | Dado ou citação curta | Data | URL | Confiança |
|---|---|---|---|---|
| Claude Duet: prévia de pesquisa, Pro, Max e Ultra, só EUA | "We're starting today with Pro, Max, and Ultra users in the US"; app para iOS, Android e claude.ai; feito em torno do Claude Opus 5.5 | 21/10/2026 (atualizado 23/10) | https://claude.com/resources/articles/claude-duet | alto |
| Claude Duet: restrição geográfica | "available in the US only during the research preview"; Team e Enterprise depois; acesso por lista de espera | sem data na página | https://support.claude.com/en/articles/17631495-get-started-with-claude-duet | alto |
| dots (OpenAI): lançamento e modelo | "always-on agents in ChatGPT", com GPT-6 Astra e computador próprio na nuvem | 29/09/2026 | https://help.openai.com/en/articles/6825453-chatgpt-release-notes | médio (página devolveu 403; texto lido no trecho do buscador) |
| dots: quem tem acesso | no Pro, maiores de 18 anos fora do Espaço Econômico Europeu, Suíça e Reino Unido; Business Premium nas regiões do ChatGPT; Enterprise/Edu por prévia do administrador, padrão a partir de 18/11 | 2026 | https://help.openai.com/en/articles/20001530-getting-started-with-your-dot | médio (403; trecho do buscador) |
| dots no Brasil | o Brasil não está na lista de exclusões, logo entra no Pro; nenhuma página oficial lida cita o Brasil pelo nome | 2026 | mesma URL | médio |
| dots: mensagens de texto | iMessage/RCS em beta só para Pro nos EUA | 28/10/2026 | https://help.openai.com/en/articles/6825453-chatgpt-release-notes | médio |
| Muse (Meta): lançamento | "rolling out in the US"; iOS, Android, muse.ai e mensagens "directly in WhatsApp"; gratuito para a maior parte do uso, com planos pagos | 08/09/2026 (atualizado 30/09) | https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/ | alto |
| Muse em Singapura | disponível "from today" em iOS, Android e muse.ai; o comunicado não menciona WhatsApp | 27/10/2026 | https://about.fb.com/news/2026/10/muse-is-now-available-in-singapore-the-worlds-first-personal-ai-agent-built-for-everyone/ | alto |
| Grok Bot (xAI): lançamento | "Today we're launching Grok Bot", em beta, para SuperGrok, SuperGrok Plus, SuperGrok Heavy, Cursor Pro, Pro+, Ultra e Teams; desktop e iOS | 11/08/2026 | https://x.ai/news/introducing-grok-bot | alto |
| Grok Bot no Brasil | app "Grok Bot" na App Store brasileira, versão 1.0 de 11/08, em português, compras em reais (Pro R$ 179,90; Pro+ R$ 499,90; Ultra R$ 1.799,90) | consultado 06/11/2026 | https://apps.apple.com/br/app/grok-bot/id6794501026 | médio |
| Grok Bot: única restrição geográfica oficial encontrada | marcar @bot no X "is not yet available for accounts based in Australia, the United Kingdom, the European Union", Islândia, Liechtenstein e Noruega; o Brasil não está na lista | sem data | https://docs.x.ai/grok-bot/tag-on-x | alto |
| Hermes Agent (Nous Research): lançamento | "An autonomous agent that lives on your server, remembers what it learns" | 25/02/2026 | https://nousresearch.com/releases | alto |
| Hermes Agent: código aberto | licença MIT; roda em Linux, macOS, WSL2, Windows nativo e Android via Termux; cerca de 261 mil estrelas no GitHub | consultado 06/11/2026 | https://github.com/NousResearch/hermes-agent | alto |
| OpenClaw: o que é | "Your assistant, on your devices, in your chats"; licença MIT; roda em macOS, Linux e Windows (WSL2 ou PowerShell), com apps para iOS e Android; conversa por WhatsApp, Telegram, Discord, iMessage, Slack, Teams e mais de 20 outros; cerca de 394 mil estrelas | consultado 06/11/2026 | https://github.com/openclaw/openclaw | alto |
| OpenClaw: autor e histórico de nomes | Peter Steinberger (austríaco, fundador da PSPDFKit); Warelay (24/11/2025), CLAWDIS (03/12/2025), Clawdbot (02/01/2026), Moltbot (27/01/2026, após queixa de marca da Anthropic), OpenClaw (30/01/2026) | 2025-2026 | https://en.wikipedia.org/wiki/OpenClaw | médio |
| OpenClaw: governança | OpenClaw Foundation, entidade sem fins lucrativos, anunciada em 14/02/2026, mesmo dia em que Steinberger anunciou ida para a OpenAI | 14/02/2026 | mesma URL | médio |
| OpenClaw: restrição de país | nenhuma; é software que o usuário instala e paga só a API do modelo escolhido. A única restrição achada é da China, que em mar/2026 vetou o uso em órgãos e estatais | mar/2026 | mesma URL | médio |

Dos quatro dados que o slide já trazia, três se mantêm e um precisa de ajuste. O Claude Duet está certo (21/10/2026, prévia, Pro, Max e Ultra, só EUA); parte da imprensa fala só em Pro e Max, mas o texto da própria Anthropic inclui o Ultra. Os dots estão certos quanto à data e ao Brasil no plano Pro, com a ressalva de que a OpenAI define o acesso por exclusão (fica de fora a Europa), e não por uma lista que nomeie o Brasil. O Muse precisa de ajuste: lançou nos EUA em 08/09/2026 com WhatsApp e chegou a Singapura em 27/10/2026 (e não 28/10, data de uma declaração à imprensa local), mas o comunicado de Singapura fala em iOS, Android e site, sem WhatsApp. O Hermes Agent é mesmo de código aberto (MIT). Sobre o Grok Bot, a afirmação do professor se sustenta pela via indireta: o app está na App Store brasileira desde a versão 1.0 de 11/08/2026, com preços em reais, e a única restrição geográfica publicada pela xAI exclui Europa e Austrália, não o Brasil. Nenhuma página da xAI diz "Brasil" com todas as letras, daí a confiança média.

### 2.2. O que o professor pode querer dizer com "openbot"

Há quatro candidatos reais com esse nome em 2026, e um quinto que não se chama assim mas é a hipótese mais provável de troca de nome.

| Candidato | Dado | Data | URL | Confiança |
|---|---|---|---|---|
| OpenClaw (troca de nome) | o assistente pessoal de código aberto mais conhecido de 2026, que passou por "Clawdbot" e "Moltbot"; "open" + "bot" é a mistura natural dos nomes | jan/2026 | https://github.com/openclaw/openclaw | médio (é inferência sobre a intenção) |
| OpenBot da CopilotKit | "Open-source AI coworkers that each get a computer of their own"; MIT; desktop para Mac e Windows, Docker ou Kubernetes; conversa por Slack, Teams e SMS; cerca de 10,3 mil estrelas; vendido como alternativa aberta ao Grok Bot | post de 23/10/2026; lançamento em ago/2026 segundo terceiros | https://github.com/CopilotKit/OpenBot ; https://www.copilotkit.ai/blog/openbot-vs-grok-bot | alto (produto); baixo (data de lançamento) |
| OpenBot da Synthetify Labs (Polônia) | "a local-first workspace where the AI models you already use can work as a team of agents"; macOS, Windows, Linux, apps para iOS e Android; licença PolyForm Noncommercial (grátis para uso pessoal) | 14/09/2026 | https://openbot.run/news/introducing-openbot ; https://openbot.run/ | alto |
| meetopenbot/openbot | "local-first harness for running AI agents", instalado por npm; MIT; cerca de 350 estrelas | sem data | https://github.com/meetopenbot/openbot | alto (produto), mas é projeto pequeno |
| openbot-ai (PyPI) | assistente leve derivado do nanobot | sem data | https://pypi.org/project/openbot-ai/ | baixo |

A leitura mais provável é que o professor esteja pensando no OpenClaw, que foi o fenômeno do começo do ano (Clawdbot, depois Moltbot) e que muita gente ainda chama de "o bot aberto". Se a ideia for um produto chamado literalmente OpenBot, o candidato com mais tração é o da CopilotKit, que se apresenta como versão aberta do Grok Bot e combina com o slide por isso. Vale perguntar ao professor antes de fechar o slide; o assunto é de nomes parecidos e a turma pode procurar o errado.

### 2.3. Linhas prontas para o slide

| Nome | Empresa | Data | Onde funciona |
|---|---|---|---|
| Claude Duet | Anthropic | 21/10/2026 (prévia) | só EUA; Pro, Max e Ultra; lista de espera |
| dots | OpenAI | 29/09/2026 | Pro fora da Europa (Brasil incluído); Business Premium |
| Muse | Meta | 08/09/2026 | EUA (app, web e WhatsApp); Singapura desde 27/10/2026 (app e web) |
| Grok Bot | xAI | 11/08/2026 (beta) | planos SuperGrok e Cursor; app na loja brasileira |
| Hermes Agent | Nous Research | 25/02/2026 | código aberto (MIT), roda no computador ou servidor do usuário |
| OpenClaw | Peter Steinberger / OpenClaw Foundation | nov/2025 (nome atual em 30/01/2026) | código aberto (MIT), roda no computador do usuário, conversa por WhatsApp e Telegram |

## 3. Visões sobre o futuro da IA e do trabalho

### 3.1. Otimistas

| Quem, cargo | Data | O que diz | Horizonte | URL | Confiança |
|---|---|---|---|---|---|
| Dario Amodei, CEO da Anthropic | out/2024 | IA poderosa "could come as early as 2026"; comprimir 50 a 100 anos de biologia "into 5-10 years"; "country of geniuses in a datacenter" | 2 e 5-10 anos | https://www.darioamodei.com/essay/machines-of-loving-grace | alto |
| Sam Altman, CEO da OpenAI, "The Gentle Singularity" | 10/06/2025 | "2026 will likely see the arrival of systems that can figure out novel insights"; robôs em 2027; "the 2030s are likely going to be wildly different"; admite "whole classes of jobs going away" | 1, 2 e 5-10 anos | https://blog.samaltman.com/the-gentle-singularity | alto (texto); médio (data, pela imprensa) |
| Sam Altman, entrevista a Matt Comyn (Commonwealth Bank) | mai/2026 | recua do alarme sobre empregos: "I'm delighted to be wrong about this"; esperava "more impact on entry-level white-collar jobs being eliminated by now" | presente | https://fortune.com/2026/05/26/sam-altman-dario-amodei-walking-back-ai-jobs-apocalypse-prophecies-ipo/ | médio |
| Demis Hassabis, CEO do Google DeepMind | 11/02/2026 | "In 10, 15 years' time, we'll be in a kind of new golden era of discovery"; "radical abundance" | 10-15 anos | https://fortune.com/2026/02/11/demis-hassabis-nobel-google-deepmind-predicts-ai-renaissance-radical-abundance/ | médio |
| Goldman Sachs, relatório econômico | mar/2023 | IA generativa poderia elevar o PIB global em 7% em dez anos, embora exponha o equivalente a 300 milhões de empregos em tempo integral | 10 anos | https://www.goldmansachs.com/insights/articles/generative-ai-could-raise-global-gdp-by-7-percent | médio (página devolveu 403; números consistentes na imprensa) |

### 3.2. Pessimistas

| Quem, cargo | Data | O que diz | Horizonte | URL | Confiança |
|---|---|---|---|---|---|
| Dario Amodei, à Axios | 28/05/2025 | IA pode eliminar metade dos empregos de entrada de escritório e levar o desemprego nos EUA a 10-20%; direito entre os setores mais expostos | 1-5 anos | https://axios.com/2025/05/28/ai-jobs-white-collar-unemployment-anthropic | médio (Axios não abriu; números iguais em várias fontes) |
| Dario Amodei, "The Adolescence of Technology" | jan/2026 | "AI will disrupt 50% of entry-level white-collar jobs over 1–5 years"; IA poderosa "could be as little as 1–2 years away" | 1-2 e 1-5 anos | https://www.darioamodei.com/essay/the-adolescence-of-technology | alto |
| Geoffrey Hinton, Nobel de Física 2024, na CNN | 28/12/2025 | sobre 2026: "We're going to see it having the capabilities to replace many, many jobs"; poucos engenheiros de software por projeto | 1 ano | https://fortune.com/2025/12/28/geoffrey-hinton-godfather-of-ai-2026-prediction-human-worker-replacement/ | médio |
| Yoshua Bengio, presidente do Relatório Internacional de Segurança da IA, ao WSJ | out/2025 (republicado mai/2026) | riscos graves em cinco a dez anos; sobre extinção, "even if there was only a 1% chance it could happen, it's not acceptable" | 5-10 anos | https://fortune.com/2025/10/01/ai-godfather-yoshua-bengio-ai-extinction-risks-openai-google-xai-anthropic/ | médio |
| Yoshua Bengio, Montreal | 19/09/2026 | pede que governos e pessoas "wake up" para o risco existencial | sem horizonte | https://www.ctvnews.ca/sci-tech/article/time-for-people-governments-to-wake-up-to-ai-existential-threat-bengio/ | médio |
| Daniel Kokotajlo e outros, "AI 2027" e atualizações | abr/2025; atualizações em 31/12/2025, 02/04/2026 e 16/08/2026 | o cenário punha um programador autônomo em 2027; a equipe adiou e voltou a adiantar: em ago/2026 Kokotajlo fala em "mid-2027" para esse marco, e Eli Lifland em 2030 | 1-4 anos | https://blog.aifutures.org/archive ; https://www.lesswrong.com/posts/ZPSsmRH5oMwLPXys4/q2-5-2026-timelines-update-uplift-and-revenue | médio (medianas exatas estão em gráficos não lidos) |
| Brynjolfsson, Chandar e Chen, Stanford Digital Economy Lab | 12/08/2026 | jovens de 22 a 25 anos nas ocupações mais expostas têm emprego 19% abaixo do esperado (eram 15% em jul/2025); efeito vem de menos contratação | presente | https://digitaleconomy.stanford.edu/news/canariesaug26/ | alto |
| Thomson Reuters, Future of Professionals 2026 (direito) | dados de mar-abr/2026 | profissionais esperam menos vagas de júnior; 78% dizem que advogados iniciantes dependem de mentoria para aprender o que a IA está tirando deles; iniciantes levariam cerca de um ano a mais para chegar ao julgamento independente | 1 ano | https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report-legal | alto |

### 3.3. Céticos e moderados

| Quem, cargo | Data | O que diz | Horizonte | URL | Confiança |
|---|---|---|---|---|---|
| Daron Acemoglu, MIT, Nobel de Economia 2024 | mai/2024 (publicado em Economic Policy, 2025) | ganho de produtividade total dos fatores de "no more than a 0.66%" em dez anos, talvez "less than 0.53%" | 10 anos | https://www.nber.org/papers/w32487 | alto |
| Yann LeCun, ex-cientista-chefe de IA da Meta, fundador da AMI Labs | mar/2026 | modelos de linguagem são beco sem saída para inteligência humana; AMI levantou US$ 1,03 bi e mira sistemas "fairly universal" em três a cinco anos | 3-5 anos | https://thenextweb.com/news/yann-lecun-ami-labs-world-models-billion | médio (sem citação literal de LeCun na fonte) |
| Yale Budget Lab | abr/2026 (dados até mar/2026) | a mudança na composição das ocupações "is not a large difference and predates the widespread introduction of AI" | presente | https://budgetlab.yale.edu/node/1495/pdf | médio (lido pelo buscador) |
| Stanford, mesmo estudo de ago/2026 | 12/08/2026 | "We do not see widespread, economy-wide job displacement associated with AI" | presente | https://digitaleconomy.stanford.edu/news/canariesaug26/ | alto |

### 3.4. Exposição de empregos

| Fonte | Dado | Data | URL | Confiança |
|---|---|---|---|---|
| FMI, Kristalina Georgieva | "almost 40 percent of global employment is exposed to AI"; cerca de 60% nas economias avançadas, 40% nas emergentes, 26% nas de baixa renda | 14/01/2024 | https://www.imf.org/en/Blogs/Articles/2024/01/14/ai-will-transform-the-global-economy-lets-make-sure-it-benefits-humanity | alto |
| OIT e NASK, índice refinado | 24% dos empregos do mundo com alguma exposição à IA generativa; 34% nos países de alta renda, 11% nos de baixa renda; 3,3% na faixa mais exposta; a maioria seria transformada, não eliminada | 20/05/2025 | https://www.ilo.org/resource/news/one-four-jobs-risk-being-transformed-genai-new-ilo%E2%80%93nask-global-index-shows | alto |
| Goldman Sachs, setor jurídico | 44% das tarefas jurídicas automatizáveis nos EUA | mar/2023 | https://www.goldmansachs.com/insights/articles/generative-ai-could-raise-global-gdp-by-7-percent | médio (403; número repetido pela imprensa) |
| Relatório Internacional de Segurança da IA 2026 | economistas divergem: uns preveem efeito macroeconômico modesto, outros queda de salários e emprego se a IA superar humanos em quase tudo; estudos nos EUA e na Dinamarca não acham relação entre exposição e emprego total, mas vários acham queda para iniciantes | 03/02/2026 | https://arxiv.org/pdf/2602.21012 | alto |

A evidência de 2026 favorece uma posição intermediária, que é a mais útil para uma turma com vinte anos de carreira pela frente. No agregado, o emprego ainda não caiu (Yale, Stanford, o próprio Relatório Internacional), e Altman admitiu em maio que errou ao esperar mais demissões a esta altura. No começo da carreira, porém, o sinal é claro e cresce: a diferença medida por Stanford passou de 15% para 19% em um ano, e a pesquisa da Thomson Reuters com escritórios de advocacia prevê menos vagas de júnior e um aprendizado mais lento. O ponto em aberto é se isso é uma onda de reorganização, como a do computador pessoal, ou o começo da substituição que Amodei e Hinton anunciam; os dados disponíveis são descritivos e não permitem separar a IA de juros altos e contratação fraca. Para o debate, os horizontes ficam assim: em dois anos, a disputa é sobre empregos de entrada (Amodei, Hinton, Stanford); em cinco, sobre agentes que fazem trabalho de vários dias (AI 2027, OCDE); em dez, sobre produtividade (Acemoglu contra Goldman e Hassabis); em vinte, só há visões, como a "era de ouro" de Hassabis e o risco existencial de Bengio, e nenhuma fonte séria arrisca número.

## 4. O slide "De ganho modesto a salto rápido"

O relatório foi lido na versão integral em PDF (arXiv 2602.21012; a página oficial confirma a publicação em 03/02/2026 e a presidência de Yoshua Bengio). As citações abaixo são da Seção 1.3, "Capabilities by 2030", páginas 31 a 39.

| Pedaço do slide | O que a fonte diz | Onde | URL | Confiança |
|---|---|---|---|---|
| "O Relatório Internacional de Segurança da IA (03/02/2026)" | data e nome corretos | página oficial | https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026 | alto |
| "cita a OCDE" | a OCDE desenvolveu os cenários e colaborou com o relatório para integrá-los; documento-base: Hobbs, Docherty, Aranda, Sugimoto, Perset e Kierzenkowski, "Exploring Possible AI Trajectories through 2030" (OCDE, 2026), doi 10.1787/cb41117a-en, publicado em 03/02/2026 | Seção 1.3, quadro "What could progress through 2030 look like: OECD progress scenarios", e referência 241 | https://oecd.ai/en/ai-publications/exploring-possible-ai-trajectories-through-2030 | alto |
| "até 2030, de melhoras modestas a ganhos rápidos" | o relatório diz "from stagnation to an acceleration in the rate of capability improvements" e, no fim do quadro, "from stagnation to rapid improvement to levels that exceed human cognitive performance". O ponto de partida é estagnação, não melhora modesta | introdução do Capítulo 1 e fecho do quadro da OCDE | https://arxiv.org/pdf/2602.21012 | alto |
| "se a tendência se mantiver, os sistemas completariam com confiança tarefas de software bem especificadas que levam vários dias" | o texto existe, mas não vem da OCDE: "If capabilities continue to improve at their current rate, by 2030 AI systems will be able to complete well-scoped software engineering tasks that would take human engineers multiple days to complete". A base é o estudo do METR (Kwa e outros, "Measuring AI Ability to Complete Long Tasks", 2025): tarefas de 30 minutos com 80% de acerto, duração dobrando a cada sete meses, "several hours by 2027 and ... several days by 2030". O "com confiança" do slide não está no texto | Seção 1.3, "Key information" e "Drivers of progress", referência 98 | https://arxiv.org/pdf/2602.21012 | alto |
| "gargalos: dados, chips, dinheiro e energia" | também não é da OCDE e se refere a depois de 2030: "Beyond 2030 ... some experts expect it will be harder to obtain data, chips, capital, and energy". Para até 2030, o relatório diz que o crescimento dos insumos é tecnicamente viável "without hitting hard limits in energy, chips, or data" | Seção 1.3, "Key information" | https://arxiv.org/pdf/2602.21012 | alto |
| Nomes oficiais dos cenários da OCDE | não confirmado no PDF da OCDE (oecd.org devolveu 403); no relatório os quatro se chamam "Progress stalls", "Progress slows", "Progress continues" e "Progress accelerates" | quadro da OCDE na Seção 1.3 | https://arxiv.org/pdf/2602.21012 | alto (nomes no relatório) |
| Série e número da publicação da OCDE | "OECD Artificial Intelligence Papers No. 55", segundo resumo do buscador; não confirmado na página da OCDE | buscador | https://www.oecd.org/en/publications/exploring-possible-ai-trajectories-through-2030_cb41117a-en.html | baixo |

Os quatro cenários, tal como o relatório os resume, são os seguintes. No primeiro, **o progresso estanca**: em 2030 a IA faz rápido tarefas que tomariam horas de uma pessoa, mas alucina, depende de instrução detalhada e revisão humanas e não aprende habilidades novas nem guarda memória; o caminho seria retorno decrescente do treino, falta de computação, queda de investimento ou ausência de avanço algorítmico, e a analogia é a velocidade dos aviões de passageiros, que parou em 500 nós. No segundo, **o progresso desacelera**: a IA é "comparable to useful assistants", usa o computador e a web, guarda memórias e corrige erros em tarefas mais longas, mas não aprende sozinha e só faz trabalho físico em ambiente controlado; os gargalos citados são "hardware, infrastructure, natural resources, data supply, and energy", e a analogia é a descoberta de antibióticos depois da era de ouro. No terceiro, **o progresso continua**: a IA é "comparable to expert collaborators", faz tarefas profissionais digitais que levariam um mês, trabalha com alta autonomia e aprende no serviço em alguma medida, como na lei de Moore. No quarto, **o progresso acelera**: a IA é "comparable to human-level remote workers", iguala ou supera pessoas em tarefas cognitivas e persegue objetivos amplos, com a IA ajudando a desenvolver a própria IA, como no sequenciamento de DNA entre 2000 e 2020.

O slide junta três coisas que o relatório mantém separadas. A faixa de cenários é da OCDE; a projeção de tarefas de vários dias é do METR e vale só "se a tendência atual continuar"; e a lista de gargalos é uma opinião de "alguns especialistas" sobre o período depois de 2030, que o próprio relatório contrabalança dizendo que até 2030 não há limite duro em energia, chips ou dados. Um texto fiel ficaria assim: "O Relatório Internacional de Segurança da IA (03/02/2026) traz quatro cenários da OCDE para 2030, da estagnação à aceleração. Se a tendência atual continuar, em 2030 a IA fará tarefas de software bem delimitadas que levam vários dias de um engenheiro (estudo do METR). Depois de 2030, dados, chips, capital e energia podem virar gargalo." O que segue sem resposta, e o relatório diz isso, é qual cenário é o mais provável: "There is little expert consensus on which trajectory is most likely."

## 5. O que ficou sem confirmar

- Texto integral das páginas da OpenAI sobre dots (openai.com e help.openai.com devolveram 403); os dados vieram dos trechos que o buscador exibe dessas mesmas páginas.
- Menção expressa ao Brasil na documentação do Grok Bot (procurado em x.ai/news, docs.x.ai/grok-bot, docs.x.ai/grok-bot/tag-on-x e no changelog, que devolveu 403); a disponibilidade foi inferida da App Store brasileira.
- WhatsApp do Muse em Singapura (o comunicado de 27/10/2026 não menciona).
- Data exata de lançamento do OpenBot da CopilotKit (o repositório não mostra datas; agosto de 2026 vem de agregador).
- Medianas atuais de Kokotajlo e Lifland para o programador autônomo (estão em gráficos externos em aifuturesmodel.com, não lidos).
- Texto da Axios de 28/05/2025 e da página do Goldman Sachs (bloqueados); números conferidos em várias fontes secundárias e, no caso de Amodei, repetidos por ele no ensaio de jan/2026.
- Série e número da publicação da OCDE e nomes dos cenários no PDF original da OCDE (oecd.org devolveu 403).
- Estimativa de risco de extinção atribuída a Hinton (10-20%): só achada em agregador, por isso fora das tabelas.
- Dados específicos da advocacia brasileira: não pesquisados nesta rodada.
