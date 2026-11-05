# Geopolítica da IA e futuro: levantamento para a Aula 4 do Dia 2

Pesquisa de apoio para o curso co.juris (advogados e procuradores, com foco no setor público). Todas as fontes foram acessadas em 05/11/2026. Há dois graus de leitura, e a coluna de confiança os distingue. "Lida" quer dizer que a página primária foi aberta e o trecho conferido nesta sessão; "busca" quer dizer que o dado veio do resumo de mecanismo de busca sobre a página indicada, sem abertura direta (por bloqueio do site ou falta de tempo). Nenhum dado de "busca" deve ir para a tela sem nova conferência ou sem o selo `[CONFERIR]`.

Três páginas primárias recusaram a leitura automática (HTTP 403): o sumário executivo da IEA, o comunicado da IEA de 2026 e o anúncio do gpt-oss pela OpenAI. Para elas, os números vêm do resumo da busca e ficam com confiança média no máximo.

## 1. Tabela de afirmações

### 1.1. EUA x China: chips e Taiwan

| Afirmação | Número | Data | URL | Confiança |
|---|---|---|---|---|
| O BIS trocou a "presunção de negação" por análise caso a caso nas licenças de chips avançados para China e Macau (abrange H200 e MI325X) | limiar: TPP < 21.000 e banda DRAM < 6.500 GB/s | vigência 15/01/2026 (91 FR 1684, doc. 2026-00789) | https://www.govinfo.gov/content/pkg/FR-2026-01-15/html/2026-00789.htm | alto (lida) |
| Teto de volume na regra: o envio à China não pode passar de metade do que vai a clientes nos EUA; texto: "no more than 50% of the total product shipped to customers for end use in the United States" | 50% | 15/01/2026 | mesma URL acima | alto (lida) |
| Cada lote exportado passa por laboratório terceiro nos EUA, que pode testar por amostragem | n/a | 15/01/2026 | mesma URL acima | alto (lida) |
| A liberação veio acompanhada de tarifa de 25% sobre a importação desses chips nos EUA (proclamação de 14/01/2026), mecanismo pelo qual o governo fica com parte da receita | 25% | 14/01/2026 | https://www.cov.com/news-and-insights/insights/2026/01/us-commerce-department-revises-license-review-policy-for-exports-of-certain-advanced-computing-commodities-to-china-and-macau | médio (busca, escritório de advocacia) |
| A receita da Nvidia ligada à China, incluindo H200, ficou abaixo de 1% no trimestre encerrado em 26/07/2026, com provisão de US$ 400 milhões por estoque excedente de H200 | < 1%; US$ 400 mi | ago/2026 | https://www.mlex.com/mlex/articles/2480408 | baixo (busca, cobertura secundária; conferir no 10-Q na SEC) |
| A Huawei anunciou o roteiro Ascend 950 (2026), 960 (2027) e 970 (2028), com o supernó Atlas 950 SuperPoD de até 8.192 chips previsto para o 4º tri de 2026 | 8.192 chips | 18/09/2025 (Huawei Connect) | https://www.trendforce.com/news/2025/09/18/news-huawei-unveils-ascend-950-with-in-house-hbm-in-2026-touts-superpod-to-rival-nvidia/ | médio (busca) |
| O AI Index registra que a TSMC fabrica "quase todo" chip de IA de ponta e que os EUA têm 5.427 data centers, mais de dez vezes qualquer outro país | 5.427 | abr/2026 (AI Index 2026) | https://hai.stanford.edu/ai-index/2026-ai-index-report | alto (lida) |
| Relatório do Pentágono sobre o poder militar chinês: o ELP refina opções contra Taiwan, "most dangerously, an amphibious invasion", com meta de capacidade para 2027 | 2027 | dez/2025 | https://www.airandspaceforces.com/china-military-power-report-highlights-concern-over-taiwan-contingency/ | médio (busca; relatório do DoD não aberto) |
| Avaliação Anual de Ameaças da comunidade de inteligência dos EUA: líderes chineses "do not currently plan to execute an invasion of Taiwan in 2027" | 2027 | 18-19/03/2026 | https://www.aljazeera.com/news/2026/3/19/us-intelligence-agencies-not-expecting-china-to-invade-taiwan-in-2027 | médio (busca; texto em dni.gov não aberto) |

### 1.2. Modelos de pesos abertos

| Afirmação | Número | Data | URL | Confiança |
|---|---|---|---|---|
| Desde janeiro de 2026, os melhores modelos abertos ficam atrás dos fechados de fronteira cerca de quatro meses no Epoch Capabilities Index | 4 meses; 8 pontos de ECI | 29/05/2026 (Edwards e Emberson) | https://epoch.ai/data-insights/open-closed-eci-gap | alto (lida) |
| Na medição anterior da Epoch, a defasagem média era de cerca de três meses | 3 meses | out/2025 | https://epoch.ai/data-insights/open-weights-vs-closed-weights-models | médio (busca) |
| AI Index 2026: em março de 2026, o melhor modelo americano (da Anthropic) liderava o melhor chinês por 2,7%; no Arena, 1.503 contra 1.464 | 2,7% | mar/2026 | https://hai.stanford.edu/ai-index/2026-ai-index-report | alto (lida) |
| AI Index 2026, segundo cobertura: o melhor fechado supera o melhor aberto em 3,3%, contra 0,5% em agosto de 2024 | 3,3% | abr/2026 | https://thenextweb.com/news/stanford-ai-index-2026-china-us-performance-gap | baixo (busca; a página de destaques do Index não traz o número) |
| Estudo OpenRouter/a16z com 100 trilhões de tokens: modelos abertos chineses saíram de ~1,2% da fatia semanal no fim de 2024 para picos perto de 30% em 2025, média ~13% | 1,2% → ~30% (pico) | dez/2025 (arXiv 2601.10088) | https://arxiv.org/abs/2601.10088 | médio (busca; PDF não aberto) |
| CAISI/NIST avaliou DeepSeek R1, R1-0528 e V3.1 contra modelos americanos em 19 benchmarks; o melhor americano venceu em quase todos | 19 benchmarks | 30/09/2025 (atualizado 20/11/2025) | https://www.nist.gov/node/1898176 | alto (lida) |
| Mesmo relatório: agentes sobre R1-0528 foram 12 vezes mais propensos a seguir instruções maliciosas; com jailbreak comum, responderam a 94% dos pedidos maliciosos, contra 8% dos americanos | 12x; 94% x 8% | 30/09/2025 | https://www.nist.gov/node/1898176 | alto (lida) |
| Mesmo relatório: modelos DeepSeek repetiram narrativas do PCCh imprecisas quatro vezes mais que os americanos; downloads subiram quase 1.000% desde jan/2025 | 4x; ~1.000% | 30/09/2025 | https://www.nist.gov/node/1898176 | alto (lida) |
| CAISI sobre o Kimi K2 Thinking (Moonshot): era o modelo chinês mais capaz no lançamento, mas "only a modest improvement on DeepSeek V3.1"; SWE-Bench Verified 56,2 contra 63,0 do GPT-5 | 56,2 x 63,0 | 12/12/2025 | https://www.nist.gov/node/1900996 | alto (lida) |
| Mesmo relatório: alinhamento a pontos do PCCh de ~26% em chinês e ~7% em inglês | 26% / 7% | 12/12/2025 | https://www.nist.gov/node/1900996 | médio (lida, mas número lido da descrição de gráfico) |
| A Meta desenvolve um modelo fechado (codinome "Avocado"), afastando-se da linha Llama aberta | n/a | dez/2025 a abr/2026 | https://the-decoder.com/meta-is-reportedly-ditching-open-llama-models-for-avocado-a-closed-model-built-for-direct-sales/ | baixo (imprensa com fontes anônimas) |

### 1.3. Energia e data centers

| Afirmação | Número | Data | URL | Confiança |
|---|---|---|---|---|
| IEA, cenário base: consumo elétrico de data centers mais que dobra até ~945 TWh em 2030 | ~945 TWh | abr/2025 (Energy and AI) | https://www.iea.org/reports/energy-and-ai/executive-summary | médio (busca; site recusou leitura) |
| IEA: a demanda de data centers cresceu 17% em 2025, contra 3% da demanda elétrica global | 17% x 3% | 2026 | https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions | médio (busca; site recusou leitura) |
| Faixa da IEA para 2035 entre os cenários | 700 a 1.700 TWh | abr/2025 | https://www.iea.org/reports/energy-and-ai/executive-summary | médio (busca) |
| Brasil: Lei 15.504/2026 institui o Redata (regime especial de tributação para serviços de data center), oriunda do PL 278/2026, sancionada sem vetos | n/a | 15/09/2026 | https://www.planalto.gov.br/ccivil_03/_Ato2023-2026/2026/Lei/l15504.htm | médio (busca; texto no Planalto não aberto) |
| Contrapartidas do Redata (segundo o Senado): investir 2% do valor dos produtos adquiridos com benefício e reservar 10% da capacidade ao mercado interno; renúncia estimada de R$ 5,2 bi em 2026 | 2%; 10%; R$ 5,2 bi | 01/09/2026 | https://www12.senado.leg.br/noticias/materias/2026/09/01/incentivo-para-instalacao-de-data-centers-no-brasil-e-aprovado-pelo-senado | médio (busca) |
| O Redata nasceu na MP 1.318/2025, que perdeu validade sem votação | n/a | fev/2026 | https://www.camara.leg.br/noticias/1247282-camara-aprova-incentivo-fiscal-para-investimentos-em-centros-de-processamento-de-dados | médio (busca) |
| EPE: projetos em processo de conexão à rede básica somavam 26,2 GW no fim de 2025, quase todos data centers | 26,2 GW | 03/09/2026 (notícia) | https://cenarioenergia.com.br/2026/09/03/data-centers-262-gw-conexao-capacidade-rede-eletrica-brasileira/ | baixo (imprensa setorial) |
| ONS concedeu 228 MW da rede básica a três data centers em São Paulo por processo competitivo | 228 MW | 2026 | https://datacenterdynamics.com/br/not%C3%ADcias/ons-destina-228-mw-da-rede-b%C3%A1sica-a-tr%C3%AAs-projetos-de-data-centers-em-s%C3%A3o-paulo | baixo (imprensa setorial) |
| Projeto TikTok/ByteDance no Pecém (CE): anúncio de mais de R$ 200 bilhões, outras fontes falam em R$ 50 bilhões | R$ 50 a 200 bi | 03/12/2025 | https://www.infomoney.com.br/business/tiktok-anuncia-investimento-de-r-200-bilhoes-em-data-center-no-brasil/ | baixo (valores divergentes) |

### 1.4. Regulação

| Afirmação | Número | Data | URL | Confiança |
|---|---|---|---|---|
| AI Act: proibições e letramento em IA aplicam-se desde 02/02/2025; regras de modelos de propósito geral desde 02/08/2025 | n/a | | https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act | alto (lida) |
| AI Act: em 02/08/2026 começou a fiscalização da maior parte das regras, incluindo transparência do art. 50 | n/a | 02/08/2026 | mesma URL | alto (lida) |
| Omnibus Digital de IA adiou alto risco do Anexo III para 02/12/2027 e do Anexo I (produtos regulados) para 02/08/2028 | 2027 / 2028 | | mesma URL | alto (lida) |
| Omnibus: proibição de deepfakes sexuais não consentidos e material de abuso infantil a partir de 02/12/2026; mesma data é o fim da transição do art. 50(2) para sistemas já no mercado | 02/12/2026 | | mesma URL | alto (lida) |
| O Omnibus é o Regulamento (UE) 2026/1744, publicado no JO em 24/07/2026, em vigor desde 27/07/2026 | 2026/1744 | jul/2026 | https://www.aiacto.eu/en/blog/digital-omnibus-ai-act-report-2027 | baixo (busca; número não confirmado em EUR-Lex) |
| EUA: Ordem Executiva 14365, "Ensuring a National Policy Framework for Artificial Intelligence", mandou o Procurador-Geral criar uma força-tarefa para litigar contra leis estaduais de IA | 30 dias | 11/12/2025 | https://www.ropesgray.com/en/insights/alerts/2025/12/trump-attempts-to-preempt-state-ai-regulation-through-executive-order | médio (busca, escritório) |
| EUA: o Senado retirou a moratória de dez anos a leis estaduais de IA do projeto de reconciliação por 99 a 1 | 99-1 | jul/2025 | https://www.joneswalker.com/en/insights/blogs/ai-law-blog/us-house-of-representatives-advance-unprecedented-10-year-moratorium-on-state-ai.html | médio (busca) |
| China: emenda à Lei de Cibersegurança com primeira cláusula sobre IA em lei nacional, em vigor em 01/01/2026 | n/a | aprov. 28/10/2025 | https://www.caixinglobal.com/2025-10-29/china-amends-cybersecurity-law-to-add-first-ever-ai-clause-102376988.html | médio (busca) |
| China: medidas de rotulagem de conteúdo gerado por IA e norma GB 45438-2025 exigíveis desde 01/09/2025 | n/a | 01/09/2025 | https://www.china-briefing.com/news/china-ai-regulation-2026-enforcement-guidance-compliance/ | médio (busca; datas divergem entre fontes) |
| Brasil: PL 2338/2023 está "Aguardando Parecer do(a) Relator(a)" na Comissão Especial da Câmara; relator Aguinaldo Ribeiro (PP-PB), designado em 20/05/2025; comissão criada em 29/04/2025 | n/a | situação em 05/11/2026; último ato 27/10/2026 (apensação) | https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2487262 | alto (lida) |
| Brasil: PBIA ("IA para o Bem de Todos") prevê R$ 23,03 bilhões em 54 ações entre 2024 e 2028 | R$ 23,03 bi | jul/2024 | https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/cct/documentacao/23072024.pdf | médio (busca; documento oficial não aberto) |
| PBIA: supercomputador previsto para o RN, valor caiu de R$ 1,8 bi (mar/2026) para ~R$ 1 bi (ago/2026); edital atrasado | R$ 1 a 1,8 bi | 2026 | https://www.poder360.com.br/poder-tech/governo-atrasa-edital-para-compra-do-supercomputador-do-plano-de-ia/ | baixo (imprensa) |
| LGPD: Resolução CD/ANPD 19/2024 aprovou o Regulamento de Transferência Internacional e as cláusulas-padrão; prazo de 12 meses para adequação venceu em 23/08/2025 | 12 meses | 23/08/2024 | https://www.mattosfilho.com.br/?p=115485 | médio (busca; DOU não aberto) |
| Resolução CNJ 615/2025: diretrizes para desenvolvimento, uso e governança de IA no Judiciário, substitui a Res. 332/2020, cria o Comitê Nacional de IA do Judiciário; o art. 19 trata de modelos de linguagem | n/a | 11/03/2025 | https://atos.cnj.jus.br/atos/detalhar/6001 | médio (busca; página consta como "Alterado") |
| Portaria SGD/MGI 5.950/2023: dados tratados em nuvem pelos órgãos do Sisp devem ficar em data centers no território brasileiro | n/a | out/2023 | https://agenciagov.ebc.com.br/noticias/202310/gestao-define-novo-modelo-de-contratacao-de-softwares-e-servicos-de-computacao-em-nuvem | médio (busca) |

### 1.5. Soberania e jurisdição dos dados

| Afirmação | Número | Data | URL | Confiança |
|---|---|---|---|---|
| CLOUD Act, 18 U.S.C. § 2713: o provedor americano deve preservar ou entregar dados sob sua "possession, custody, or control", esteja o dado dentro ou fora dos EUA | n/a | 23/03/2018 (Pub. L. 115-141) | https://www.law.cornell.edu/uscode/text/18/2713 | alto (lida) |
| O DOJ lista acordos executivos do CLOUD Act só com Reino Unido (2019) e Austrália (2021); Canadá e UE em negociação; o Brasil não aparece | 2 acordos | consultado 05/11/2026 | https://www.justice.gov/criminal/cloud-act-resources | alto (lida) |
| A Nuvem de Governo do Serpro tem ambientes homologados com AWS Outposts, Google Distributed Cloud e Huawei Cloud Stack, isto é, infraestrutura física no Brasil operada com tecnologia estrangeira | 3 provedores | out/2026 | https://capitaldigital.com.br/55773-2/ | baixo (imprensa) |
| Segundo a ministra Esther Dweck, Serpro e Dataprev já destinaram mais de R$ 1,8 bilhão a infraestrutura de nuvem soberana | R$ 1,8 bi | out/2026 | https://fenati.org.br/serpro-dataprev-infraestrutura-nuvem-soberana/ | baixo (imprensa sindical) |
| TCU, Acórdão 1380/2026-Plenário, auditou o modelo de nuvem de governo e os acordos com Serpro e Dataprev | n/a | jun/2026 | https://static.poder360.com.br/uploads/2026/06/Acordao-1380-de-2026-Plenario.pdf | baixo (busca; conteúdo não lido) |

### 1.6. Cenários e sinais

| Afirmação | Número | Data | URL | Confiança |
|---|---|---|---|---|
| Relatório Internacional de Segurança da IA 2026 (presidido por Yoshua Bengio): o cômputo de treino dos modelos líderes cresce ~5x ao ano e a eficiência algorítmica 2 a 6x ao ano | 5x; 2-6x | 03/02/2026 | https://internationalaisafetyreport.org/publication/2026-report-extended-summary-policymakers | alto (lida) |
| Mesmo relatório, citando a OCDE: até 2030 os resultados "could range from modest improvements to rapid gains" | n/a | 03/02/2026 | mesma URL | alto (lida) |
| Mesmo relatório: mantida a tendência, em 2030 sistemas "could reliably complete well-specified software engineering tasks" de vários dias; gargalos possíveis são dados, chips, financiamento e energia | duplicação ~7 meses | 03/02/2026 | mesma URL | alto (lida) |
| AI Index 2026: incidentes documentados com IA subiram de 233 (2024) para 362 (2025) | 233 → 362 | abr/2026 | https://hai.stanford.edu/ai-index/2026-ai-index-report | alto (lida) |
| AI Index 2026: investimento privado em IA nos EUA de US$ 285,9 bi em 2025, mais de 23 vezes o da China (US$ 12,4 bi), com a ressalva de que o dado privado subestima o gasto chinês | US$ 285,9 bi x 12,4 bi | abr/2026 | mesma URL | alto (lida) |
| AI Index 2026: confiança no governo para regular IA é de 31% nos EUA e 91% em Singapura | 31% / 91% | abr/2026 | mesma URL | alto (lida) |

## 2. Leitura para o profissional do Direito público

O núcleo da aula pode ser a distância entre onde o dado mora e quem manda nele. A Portaria SGD/MGI 5.950/2023 exige que dados de órgãos federais em nuvem fiquem em data centers no Brasil, mas o § 2713 do CLOUD Act alcança o que estiver sob controle de provedor americano "wherever" esteja armazenado. Localização física, portanto, não afasta a jurisdição americana sobre a empresa; quem resolve esse conflito é um acordo executivo, e o Brasil não tem nenhum na lista do DOJ. A Nuvem de Governo do Serpro, ao operar com AWS Outposts, Google Distributed Cloud e Huawei Cloud Stack, aposta na operação por estatal brasileira como barreira, e se essa barreira resiste a uma ordem judicial estrangeira dirigida ao fornecedor da tecnologia é pergunta que nenhuma fonte lida nesta sessão responde.

A escolha entre modelo americano e chinês costuma ser apresentada como escolha de país, e as fontes sugerem outro recorte. Um modelo de pesos abertos (aquele cujo arquivo de parâmetros pode ser baixado e rodado em servidor próprio) executado dentro da infraestrutura do órgão não envia dado a ninguém; o risco passa a ser o comportamento do modelo, e é isso que a CAISI mediu (vulnerabilidade a sequestro de agente, viés em temas políticos). Usar o mesmo modelo pela API do fabricante chinês, ao contrário, leva o dado à jurisdição chinesa. O par relevante, então, é "rodar em casa ou mandar para fora", e a nacionalidade entra como segundo critério. A ressalva é que a CAISI é órgão do governo americano avaliando concorrentes chineses, o que não invalida os números, mas pede leitura com isso em mente.

No Brasil, a lacuna regulatória é concreta: o PL 2338/2023, aprovado no Senado, segue sem parecer na Comissão Especial da Câmara em 05/11/2026, e a movimentação de 2026 na ficha se resume a apensações. Enquanto isso, o Judiciário já tem a Resolução CNJ 615/2025, a ANPD já tem regra de transferência internacional em vigor e o Executivo federal regula nuvem por portaria. O procurador trabalha, hoje, com normas setoriais e infralegais, e não com um marco geral.

## 3. Sinais para acompanhar

A lista abaixo traz indicadores com fonte pública e data previsível, para que a aula não dependa de previsão de consultoria.

1. Parecer do relator na Comissão Especial do PL 2338/2023 (ficha da Câmara, link da seção 1.4). Notícias de agosto de 2026 indicavam votação só depois das eleições de outubro; não confirmado em fonte primária.
2. Regulamentação do Redata pela Receita Federal, sem a qual o benefício da Lei 15.504/2026 não se aplica, e a próxima janela de acesso à rede básica do ONS, prevista para janeiro de 2027.
3. Edital da "Nuvem Brasileira" (ABDI, MGI, Serpro, BNDES), previsto para o fim de 2026, e o desfecho do Acórdão TCU 1380/2026.
4. 02/12/2026 na UE: fim da transição do art. 50(2) do AI Act e início das novas proibições sobre deepfakes sexuais.
5. Próxima medição da Epoch AI sobre a defasagem entre modelos abertos e fechados (estava em quatro meses em maio de 2026).
6. Novas licenças ou revogações do BIS para H200 e eventual regra sobre Blackwell para a China; entregas efetivas do Atlas 950 SuperPoD da Huawei (prometido para o 4º tri de 2026).
7. Próxima edição do relatório da IEA sobre energia e IA e do AI Index (abril de 2027, se mantido o calendário).

## 4. O que não consegui confirmar

- O texto das páginas da IEA (403). Os números de 945 TWh em 2030 e crescimento de 17% em 2025 vieram de resumo da busca; uma fonte secundária cita revisão para 950 TWh na edição de 2026, sem confirmação no site da IEA.
- O número do Regulamento do Omnibus (2026/1744) e as datas de publicação no Jornal Oficial; a página oficial do AI Act Service Desk confirma as datas de aplicação, mas não traz o número.
- O texto da Lei 15.504/2026 no Planalto (só o resumo da busca e de escritórios). Há divergência sobre se os benefícios de PIS/Cofins/IPI valem só até 31/12/2026 por causa da reforma tributária.
- Se houve embarques relevantes de H200 para a China. As fontes se contradizem (bloqueio aduaneiro chinês, "very few" segundo autoridade do Commerce ao Congresso em julho, embarques limitados à ByteDance e Tencent em agosto). O 10-Q da Nvidia não foi aberto.
- O texto primário da Avaliação Anual de Ameaças (dni.gov) e do relatório do Pentágono sobre a China; as citações vêm da imprensa.
- Os números exatos do estudo OpenRouter/a16z (PDF não lido) e o número de 3,3% de diferença aberto x fechado atribuído ao AI Index (não aparece na página de destaques).
- Norma específica do GSI/PR sobre nuvem para informação classificada em 2025-2026; a busca só achou a IN GSI/PR nº 5/2021 citada em planos de órgãos.
- O conteúdo do Acórdão TCU 1380/2026 e o teor da alteração da Resolução CNJ 615/2025 (a página do CNJ a marca como "Alterado").
- Desfecho das ações da força-tarefa do DOJ contra leis estaduais (Colorado foi citado como alvo, sem processo identificado) e se a FTC e o Commerce cumpriram os prazos de março de 2026 da EO 14365.
- Situação atual da linha Llama da Meta; só há imprensa com fontes anônimas. O anúncio do gpt-oss pela OpenAI (agosto de 2025, licença Apache 2.0, segundo memória própria) não pôde ser lido (403) e não entra na tabela.
- Valor do projeto TikTok no Pecém (R$ 50 bi ou R$ 200 bi) e capacidade (200 ou 300 MW).

## 5. Pontos em disputa

**Se o controle de chips funciona.** A regra de janeiro de 2026 liberou o H200 sob condições, o que leitores críticos tratam como afrouxamento (https://www.iaps.ai/research/bis-licensing-policy-for-h200s, título: "Tough Guidelines, Weak Enforcement"). O Council on Foreign Relations defende manter os controles e estima que, mesmo produzindo milhões de Ascend, a Huawei teria cerca de 4% do poder computacional agregado que a Nvidia produz (https://www.cfr.org/articles/chinas-ai-chip-deficit-why-huawei-cant-catch-nvidia-and-us-export-controls-should-remain, dado de busca; a página retornou 404 na leitura direta). Do lado chinês, há relatos de bloqueio aduaneiro ao H200 para proteger a Huawei. Nenhuma fonte lida mede o efeito líquido.

**Se a China alcançou os EUA.** O AI Index 2026 fala em diferença de 2,7% entre os melhores modelos de cada país em março de 2026. A CAISI, órgão americano, afirma que o melhor modelo americano venceu o DeepSeek V3.1 em quase todos os 19 testes e que o Kimi K2 Thinking foi "only a modest improvement". As duas leituras convivem porque medem coisas diferentes (preferência humana no Arena contra benchmarks técnicos de engenharia e cibersegurança) e em datas diferentes.

**Se modelos abertos estão perdendo terreno.** A Epoch mediu a defasagem subindo de três para quatro meses; ao mesmo tempo, o uso de modelos abertos chineses cresceu no OpenRouter. Parte da explicação aventada em comentários (não no Index) é que laboratórios chineses passaram a fechar suas versões de ponta, e a Meta pode estar fazendo o mesmo. É hipótese, não achado.

**Risco de Taiwan em 2027.** O relatório do Pentágono de dezembro de 2025 enfatiza capacidade para 2027; a avaliação de inteligência de março de 2026 afirma que não há plano de invasão nesse ano. Críticos citados pelo Washington Times (26/03/2026) consideraram a conclusão simplista. A divergência é entre capacidade e intenção, e as duas fontes podem estar certas ao mesmo tempo.

**Execução do PBIA.** Em março de 2026, o MCTI falou em 30% a 35% das metas em execução; em agosto, a ministra Luciana Santos falou em 64% executado. Não há metodologia pública que concilie os números nas fontes lidas.

**Preempção federal nos EUA.** A EO 14365 manda litigar contra leis estaduais, mas ordem executiva não revoga lei estadual; o Congresso recusou a moratória duas vezes (99 a 1 no Senado em julho de 2025; fora do NDAA em dezembro de 2025). A minuta bipartidária de 2026 (Obernolte e Trahan), com congelamento de três anos, estava parada em setembro segundo editorial da CASRAI, fonte de confiança baixa.
