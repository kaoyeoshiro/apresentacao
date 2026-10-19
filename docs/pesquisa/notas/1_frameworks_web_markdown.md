# Frameworks web e Markdown para apresentações

Notas de pesquisa para relatório em português. Coleta de métricas do GitHub em 19/10/2026, entre 13:20 e 13:45 UTC, pela API `api.github.com` com autenticação (`gh api`). Contagens de downloads do npm referentes ao período 19/09/2026 a 18/10/2026.

## 1. Resumo executivo

O campo se divide em três camadas. A primeira é a de frameworks de runtime, representada por reveal.js, impress.js e Shower, em que o autor controla HTML, CSS e JavaScript e o limite visual depende do seu domínio de front-end. A segunda é a de ferramentas Markdown com exportação, representada por Marp, Slidev, remark, reveal-md e backslide, em que o custo de entrada é baixo e o resultado visual depende do tema escolhido. A terceira é a de bibliotecas de componente, representada por Spectacle, mdx-deck e Eagle.js, em que a apresentação é uma aplicação React ou Vue e o layout é código.

Em outubro de 2026, quatro projetos combinam maturidade e atividade real: reveal.js (72,4 mil estrelas, versão 6.0.2), Slidev (49,1 mil estrelas, versão 53.0.0), Quarto (6,1 mil estrelas, versão 1.10.19) e Marp (12,7 mil estrelas no repositório de entrada, CLI 4.5.1). Spectacle e Shower também estão ativos, mas ocupam nichos mais específicos, React e HTML acessível, respectivamente.

O maior impacto visual por esforço está em Slidev, WebSlides e Spectacle, por razões diferentes. Slidev entrega tipografia, código, animações e componentes Vue sem sair do Markdown. WebSlides entrega um sistema editorial pronto, com 40+ componentes e 120+ slides, mas exige HTML manual e está parado desde 2020. Spectacle entrega liberdade total de React, porém sem galeria de temas prontos e com exportação limitada a PDF.

A maior armadilha da lista é confundir estrelas com saúde. mdx-deck tem 11,5 mil estrelas e o último commit é de agosto de 2021. nodeppt tem 10,3 mil estrelas e está arquivado. Fusuma tem 5,4 mil estrelas e está arquivado. WebSlides tem 6,3 mil estrelas e o último commit é de setembro de 2020. Para um relatório de 2026, esses projetos entram como alternativa histórica ou como alerta, não como recomendação padrão.

## 2. Método e confiabilidade dos números

As métricas de repositório vêm de `GET /repos/{owner}/{repo}`, `GET /repos/{owner}/{repo}/releases/latest`, `GET /repos/{owner}/{repo}/commits?per_page=1` e `GET /repos/{owner}/{repo}/license`. As datas de última publicação no npm vêm do registro público `registry.npmjs.org`. As contagens de download vêm de `api.npmjs.org/downloads/point/last-month/{pacote}`.

Três ressalvas valem para toda a tabela.

- O campo `open_issues_count` do GitHub soma issues e pull requests abertos. Ele não é o número de bugs abertos. Em projetos grandes, como Quarto, o valor de 1.905 é dominado por volume de trabalho, não por falhas críticas.
- Estrelas e forks são cumulativos e não decaem. Um projeto arquivado mantém a contagem alta. A data do último commit e o estado `archived` dizem mais sobre manutenção do que a popularidade.
- O repositório `marp-team/marp` é o repositório de entrada do ecossistema, não o motor. As estrelas de 12.656 não devem ser somadas às de `marp-cli` (3.874) e `marp-core` (1.159), porque são públicos diferentes do mesmo projeto.

Classificação de atividade usada nas fichas:

- Ativo: commit ou release nos últimos 12 meses.
- Manutenção lenta: última atividade entre 12 e 24 meses.
- Estagnado: última atividade há mais de 24 meses, sem arquivamento.
- Arquivado: campo `archived` verdadeiro na API.

## 3. Panorama comparativo

### 3.1. Métricas verificadas

| Projeto | Repositório | Estrelas | Forks | Issues + PRs | Último commit | Último release | Licença | Status |
|---|---:|---:|---:|---:|---|---|---|---|
| Slidev | slidevjs/slidev | 49.127 | 2.229 | 237 | 2026-10-02 | v53.0.0, 2026-09-16 | MIT | Ativo |
| reveal.js | hakimel/reveal.js | 72.441 | 17.023 | 928 | 2026-09-30 | 6.0.2, 2026-09-10 | MIT | Ativo |
| Marp (entrada) | marp-team/marp | 12.656 | 302 | 1 | push 2026-07-29 | sem release no repo de entrada | MIT | Ativo |
| Marp CLI | marp-team/marp-cli | 3.874 | 204 | 20 | 2026-09-08 | v4.5.1, 2026-09-06 | MIT | Ativo |
| Marp Core | marp-team/marp-core | 1.159 | 165 | 10 | 2026-09-04 | v4.4.0, 2026-07-17 | MIT | Ativo |
| Quarto | quarto-dev/quarto-cli | 6.099 | 471 | 1.905 | 2026-10-19 | v1.10.19, 2026-10-06 | MIT | Ativo |
| remark | gnab/remark | 13.005 | 861 | 181 | 2023-06-27 | v0.15.0, 2020-01-18 | MIT | Estagnado |
| reveal-md | webpro/reveal-md | 3.912 | 414 | 12 | 2024-11-27 | 6.1.4, 2024-11-27 | MIT | Arquivado |
| Spectacle | FormidableLabs/spectacle | 10.181 | 701 | 83 | 2026-09-24 | 10.2.3, 2025-10-10 | MIT | Ativo |
| mdx-deck | jxnblk/mdx-deck | 11.500 | 594 | 141 | 2021-08-03 | 4.1.1, 2020-03-12 (npm) | MIT | Estagnado |
| WebSlides | webslides/WebSlides | 6.327 | 585 | 82 | 2020-09-05 | 1.5.0, 2017-09-16 | MIT | Estagnado |
| Shower | shower/shower | 4.876 | 853 | 40 | 2026-10-14 | npm @shower/core 3.6.0, 2026-07-07 | MIT | Ativo |
| impress.js | impress/impress.js | 38.155 | 6.567 | 61 | 2026-07-23 | v2.0.0, 2022-07-22 | MIT | Ativo |
| Fusuma | hiroppy/fusuma | 5.356 | 190 | 85 | 2021-12-01 | npm 2.8.4, 2021-05-15 | MIT no package.json, sem LICENSE | Arquivado |
| backslide | sinedied/backslide | 777 | 50 | 15 | 2022-03-15 | 3.1.0, 2022-03-15 | MIT | Estagnado |
| nodeppt | ksky521/nodeppt | 10.328 | 2.021 | 27 | 2021-01-25 | npm 2.2.2, 2020-06-28 | MIT | Arquivado |
| Eagle.js | Zulko/eagle.js | 4.047 | 214 | 13 | 2022-07-10 | npm 0.6.1, 2019-10-23 | ISC | Estagnado |
| Bespoke.js | bespokejs/bespoke | 4.793 | 446 | 6 | 2020-09-08 | 1.1.0, 2015-09-24 (npm) | MIT | Estagnado |
| DeckDeckGo | deckgo/deckdeckgo | 1.674 | 188 | 117 | 2024-02-06 | v7.1.0, 2022-10-31 | Nenhuma detectada | Arquivado |
| MkSlides | MartenBE/mkslides | 481 | 21 | 1 | 2026-10-11 | 2.0.23, 2026-09-30 | MIT | Ativo |

### 3.2. Matriz de recursos

Legenda: S = suporte nativo documentado; P = via plugin ou extensão; N = não documentado no núcleo; traço = não se aplica.

| Projeto | Autor principal | Markdown | HTML | PDF | PPTX | Notas | Apresentador | Temas | Math | Diagramas | Build |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Slidev | Markdown + Vue | S | S | S | S | S | S | S (npm) | S | S | Node |
| reveal.js | HTML | P | S | S | N | S | S | S (12) | S | P | Nenhum |
| Marp | Markdown | S | S | S | S | S | S | S (3) | S | P (v5 RC) | Node/CLI |
| Quarto | Markdown + Pandoc | S | S | S | S | S | S | S | S | S | Instalador |
| remark | Markdown | S | P | S (print) | N | S | S | N | N | N | Nenhum |
| reveal-md | Markdown | S | P | S | N | S | S | S (reveal) | P | P | Node |
| Spectacle | React/TS | S | S | S | N | S | S | S (custom) | P | P | Node |
| mdx-deck | MDX/React | S | S | N | N | S | S | S | P | P | Node |
| WebSlides | HTML/CSS | N | S | N | N | N | P | S (sistema próprio) | N | N | Nenhum |
| Shower | HTML/CSS | N | S | S (print) | N | N | N | S (2) | N | N | Nenhum/CLI |
| impress.js | HTML/CSS | N | S | N | N | N | N | N | N | N | Nenhum |
| Fusuma | Markdown/MDX | S | S | S | N | S | S | S (5) | S | S | Node |
| backslide | Markdown/Remark | S | P | S | N | S | S | S (Remark) | P | P | Node |
| nodeppt | Markdown | S | S | N | N | S | S | S (WebSlides) | S | S | Node |
| Eagle.js | Vue 2 | N | S | N | N | N | N | S | P | P | Node |
| Bespoke.js | HTML/CSS | N | S | N | N | N | N | P | N | N | Node |
| DeckDeckGo | editor web | P | S | N | N | N | N | S | N | N | Editor |
| MkSlides | Markdown | S | P | S | N | S | S | S (reveal) | P | P | Python |

As células "N" indicam ausência de documentação oficial encontrada, não necessariamente impossibilidade técnica. Em projetos arquivados, a ausência de documentação costuma significar ausência de suporte, não uma lacuna contornável.

## 4. Fichas por projeto

### 4.1. Slidev

Repositório: https://github.com/slidevjs/slidev
Site e documentação: https://sli.dev
Showcases: https://sli.dev/resources/showcases

Métricas em 19/10/2026: 49.127 estrelas, 2.229 forks, 237 issues + PRs, último commit em 02/10/2026, release v53.0.0 em 16/09/2026, licença MIT. npm `@slidev/cli`: 393.213 downloads no último mês.

O que é. Ferramenta de apresentações para desenvolvedores, escrita em Markdown estendido, construída sobre Vue 3 e Vite. O deck inteiro cabe em um `slides.md`, com frontmatter por slide, layouts prontos, componentes Vue embutidos e UnoCSS para estilos pontuais. O diferencial é tratar a apresentação como aplicação web moderna, com hot reload, componentes reutilizáveis e ecossistema npm de temas e addons. O README exige Node.js 22.12 ou superior.

Qualidade visual. É o conjunto mais completo para palestras técnicas. O código usa Shiki, com Magic Move e integração TwoSlash, e o Monaco permite edição ao vivo. Há KaTeX nativo, Mermaid nativo, ícones via Iconify, animações por `v-click`, `v-clicks` e `v-motion`, além de transições de slide. A galeria oficial de temas e a instalação via npm elevam o teto visual, mas o resultado padrão é limpo e discreto, não espetacular. Para impacto, o autor precisa escolher um tema bom ou montar o próprio.

Exportação e apresentação. Exporta PDF, PPTX, PNG e Markdown de imagens pelo CLI, com Playwright Chromium. O PPTX padrão transforma cada slide em imagem, então o texto não é selecionável; as notas são preservadas. Existe um modo `pptx-editable`, que reconstrói formas nativas, mas SVG, canvas, iframe, vídeo, fórmulas KaTeX, gradientes e filtros continuam como imagem. O modo apresentador tem três layouts, notas, editor de notas em lote, espelhamento de tela, desenho e gravação com câmera. O build gera uma SPA estática para GitHub Pages, Netlify ou Vercel.

Curva e manutenção. Markdown básico é imediato. Layouts, componentes Vue e configuração de Vite exigem familiaridade com o ecossistema. O projeto está muito ativo, com release mensal e comunidade grande. O risco é o acoplamento ao Node e ao Vue: um deck com componentes customizados vira um pequeno projeto de software.

Casos ideais. Palestras de engenharia, workshops, aulas com código, live coding, demonstrações interativas e talks que precisam de vídeo, câmera ou gravação. É a escolha padrão quando o palestrante é desenvolvedor e quer Markdown sem abrir mão de Vue.

Limitações. Exige Node e build. O PPTX padrão não é editável. Recursos interativos não sobrevivem à exportação. A estética depende do tema escolhido e o excesso de componentes pode deixar o arquivo mais próximo de código do que de texto.

Showcases oficiais. A página de showcases lista talks de 2023 a 2026, incluindo "Reverse Engineering Denuvo in Hogwarts Legacy" (Navaja Negra 2025), "Taming Dependency Chaos for LLM in K8s" (KubeCon China 2025) e "Composable Vue" (VueDay 2021, de Anthony Fu). https://talks.antfu.me/2021/composable-vue/

### 4.2. reveal.js

Repositório: https://github.com/hakimel/reveal.js
Site e documentação: https://revealjs.com
Demo: https://revealjs.com/demo/

Métricas em 19/10/2026: 72.441 estrelas, 17.023 forks, 928 issues + PRs, último commit em 30/09/2026, release 6.0.2 em 10/09/2026, licença MIT. npm `reveal.js`: 571.757 downloads no último mês.

O que é. O framework HTML de apresentações mais antigo e difundido da lista, criado em 2011. Cada slide é um `<section>`; a navegação, as transições e os plugins são JavaScript e CSS. Markdown é suportado por plugin, e há um wrapper React oficial. O diferencial é a portabilidade: um deck é um conjunto de arquivos estáticos que roda em qualquer navegador, sem build obrigatório, e pode ser embutido em outra página ou aplicação.

Qualidade visual. A documentação lista 12 temas oficiais (black, white, league, beige, night, serif, simple, solarized, moon, dracula, sky e blood). O teto é alto porque todo o CSS é acessível, mas o piso é o tema padrão. Os recursos visuais incluem slides verticais aninhados, transições none/fade/slide/convex/concave/zoom, fragmentos com estilos variados, Auto-Animate para morfar elementos entre slides, fundos com imagem, vídeo, iframe e parallax, código com highlight.js, matemática com plugin oficial e visualização em overview. É a base do Slides.com, editor visual comercial do mesmo autor.

Exportação e apresentação. A exportação oficial é PDF, pelo modo de impressão do navegador ou pelo DeckTape. Não há exportador PPTX ou PNG no núcleo documentado. O modo apresentador mostra slide atual, próximo slide, timer e notas; há multiplex para sincronizar a audiência, scroll view, overview e atalhos de teclado. O deck é HTML estático e pode ser hospedado em qualquer servidor.

Curva e manutenção. Começar é trivial: um HTML, um CSS e um script. Fazer bonito é trabalho de front-end. O projeto está ativo após 15 anos, com versão 6 e comunidade ampla. O risco é a liberdade: sem um sistema de layout, cada slide especial vira CSS manual.

Casos ideais. Apresentações institucionais, aulas, decks embutidos em sites, demos que precisam de iframe ou JavaScript customizado, projetos que exigem arquivo estático de longo prazo e situações em que o autor quer controle total do HTML.

Limitações. Exige HTML e CSS para resultados acima do tema padrão. O PDF é o único formato oficial de exportação. A acessibilidade e a responsividade dependem do CSS do autor. A quantidade de issues abertas reflete a idade e a superfície do projeto.

Showcase. A demo oficial cobre vertical slides, Auto-Animate, fragmentos, speaker view, fundos e exportação PDF. https://revealjs.com/demo/

### 4.3. Marp

Repositório de entrada: https://github.com/marp-team/marp
Site: https://marp.app
CLI: https://github.com/marp-team/marp-cli
Core: https://github.com/marp-team/marp-core

Métricas em 19/10/2026. Repositório de entrada: 12.656 estrelas, 302 forks, 1 issue + PR, push em 29/07/2026. CLI: 3.874 estrelas, 204 forks, 20 issues + PRs, último commit em 08/09/2026, release v4.5.1 em 06/09/2026. Core: 1.159 estrelas, 165 forks, 10 issues + PRs, último commit em 04/09/2026, release v4.4.0 em 17/07/2026. Todos MIT. npm `@marp-team/marp-cli`: 235.700 downloads; `@marp-team/marp-core`: 405.311.

O que é. Ecossistema Markdown para slides, baseado em CommonMark, com separação de páginas por `---`. A arquitetura tem três peças: Marpit, o framework de conversão; Marp Core, o motor com temas e extensões; e Marp CLI, a ferramenta de linha de comando. Há extensão oficial para VS Code. O diferencial é a portabilidade: o mesmo Markdown vira HTML, PDF, PPTX ou imagem, com sintaxe de imagem e diretivas que resolvem layouts comuns sem HTML.

Qualidade visual. Três temas oficiais, default, gaia e uncover, com a possibilidade de criar temas em CSS puro. A tipografia é boa e o sistema de imagens de fundo é poderoso, com `![bg left:40%]`, múltiplas imagens e auto-scaling. O visual é mais sóbrio e previsível do que Slidev, e menos expressivo do que WebSlides. Código, tabelas, citações e matemática funcionam bem. O Marp Core v5, ainda release candidate, separa plugins opcionais de Shiki, Mermaid e KaTeX/MathJax; a última release estável é a 4.4.0, e as ferramentas atuais ainda podem usar a linha v4.

Exportação e apresentação. Converte para HTML estático, PDF, PPTX e imagens (PNG/JPEG). O PDF aceita anotações de notas com `--pdf-notes` e marcadores com `--pdf-outlines`. O PPTX carrega as notas do apresentador; o modo `--pptx-editable` é experimental e não suporta notas. As notas são comentários HTML no Markdown e podem ser exportadas como TXT com `--notes`. O template bespoke do CLI inclui uma visão do apresentador com slide atual, próximo, notas e timer. A conversão para PDF, PPTX e imagem exige Chrome, Edge ou Firefox instalado. Node.js 18 ou superior para o CLI.

Curva e manutenção. É a curva mais baixa da lista para quem só quer Markdown. Diretivas e temas CSS exigem algum estudo, mas o núcleo é pequeno. O ecossistema está ativo, com releases regulares do CLI e do Core, embora o repositório de entrada esteja mais quieto. O risco é o oposto de Slidev: quando o deck precisa de interação ou layout fora do padrão, a simplicidade vira limite.

Casos ideais. Aulas, relatórios, decks corporativos, documentação apresentada, PDFs para distribuição e qualquer situação em que o conteúdo precise ser versionado em Markdown e exportado para PowerPoint. É a melhor opção quando o destinatário final pede PPTX.

Limitações. Não tem o poder de componentes de Slidev. O layout é mais rígido. Mermaid só entra como plugin opcional na v5 RC. Não confirmei visão do apresentador na extensão do VS Code; a visão documentada está no template do Marp CLI. A exportação depende de um navegador externo.

Showcase. A própria home https://marp.app é um deck gerado pelo Marp Core, com tema gaia e imagens de fundo. É a demonstração oficial mais direta do resultado possível.

### 4.4. Quarto

Repositório: https://github.com/quarto-dev/quarto-cli
Site e documentação: https://quarto.org
Demo de apresentação: https://quarto.org/docs/presentations/revealjs/demo/

Métricas em 19/10/2026: 6.099 estrelas, 471 forks, 1.905 issues + PRs, último commit em 19/10/2026, release v1.10.19 em 06/10/2026, licença MIT (arquivo COPYING.md). Não é um pacote npm; a distribuição é um instalador próprio.

O que é. Sistema de publicação científica e técnica construído sobre Pandoc. Para apresentações, aceita três formatos: `revealjs` (HTML), `pptx` (PowerPoint) e `beamer` (LaTeX/PDF). A documentação afirma que `revealjs` é o formato mais capaz e o recomenda, e que a apresentação pode ser exibida como HTML ou impressa em PDF. O diferencial é a reprodutibilidade: o mesmo documento executa código Python, R, Julia ou Observable JS, gera gráficos, tabelas, citações, referências cruzadas e múltiplas saídas.

Qualidade visual. Herda o reveal.js e acrescenta camadas de tema, tipografia e layout do Quarto. O resultado é acadêmico e consistente, com boa Tipografia para texto e dados, mas menos "palco" do que Slidev ou WebSlides. Inclui diagramas Mermaid e Graphviz nativos, código com destaque, matemática, imagens, vídeo, chalkboard para desenhar, multiplex, auto-slide, preview de links, tom de slide para acessibilidade e modo apresentador com notas e timer.

Exportação e apresentação. Gera HTML autocontido com `embed-resources`, PDF por impressão, PPTX nativo e Beamer em PDF. O modo apresentador do reveal.js mostra slide atual, próximo, timer e notas; as notas são uma `div` com classe `.notes`. Há publicação para Quarto Pub, GitHub Pages, Posit Connect, Netlify e outros.

Curva e manutenção. A curva é moderada. Markdown e YAML bastam para começar, mas o sistema tem uma superfície grande: execução de código, ambientes, temas, extensões e formatos. É o projeto mais ativo da lista em commits, com versão 1.10.19 e quase 2 mil itens abertos. O risco é o peso: para um deck simples, o Quarto é mais instalação e configuração do que o necessário.

Casos ideais. Aulas e palestras com dados, relatórios científicos, apresentações que precisam citar fontes, dashboards estáticos, materiais que viram artigo, PDF e PPTX a partir da mesma fonte, e equipes que já usam R, Python ou Julia.

Limitações. Não é uma biblioteca de componentes JavaScript. O design fica dentro do universo reveal.js e dos temas do Quarto. A instalação é maior e o tempo de renderização pode ser alto em documentos com código. O volume de issues + PRs abertos é grande.

Showcase. A demo oficial de apresentação reveljs do Quarto, com opções de navegação, speaker view, scroll view e impressão. https://quarto.org/docs/presentations/revealjs/demo/

### 4.5. remark

Repositório: https://github.com/gnab/remark
Site e demo: https://remarkjs.com

Métricas em 19/10/2026: 13.005 estrelas, 861 forks, 181 issues + PRs, último commit em 27/06/2023, release v0.15.0 em 18/01/2020, licença MIT.

O que é. Ferramenta minimalista que roda no navegador e transforma Markdown em slides. O Markdown fica dentro de um `<textarea>` na própria página HTML, e o `remark.create()` monta a apresentação. Não exige build, servidor ou Node. O diferencial é a simplicidade radical e o modo apresentador com espelhamento de tela.

Qualidade visual. O visual é o mais datado do grupo. A apresentação depende de CSS escrito à mão; não há galeria de temas, sistema de layout ou componentes. O README destaca escala de slide, syntax highlighting, templates Markdown simples, suporte a toque e modo apresentador com notas e clone da tela. Para um deck bonito, o autor precisa construir o CSS.

Exportação e apresentação. O PDF é feito pela impressão do Chrome. O modo apresentador é acionado com `C` para clonar a tela e `P` para entrar no modo de apresentação. As notas são Markdown dentro dos slides.

Curva e manutenção. Baixa para começar, alta para estilizar. O projeto está estagnado: última release em 2020 e último commit em 2023. A comunidade migrou para Slidev, Marp e reveal.js. Não é uma escolha para projeto novo em 2026.

Casos ideais. Decks simples, offline, de uma pessoa, que precisam de um único HTML e não exigem design elaborado. Também serve como base histórica para entender a linhagem Markdown-to-slides.

Limitações. Sem temas, sem componentes, sem math ou diagramas documentados no README, sem exportação PPTX e sem manutenção ativa. O CSS é responsabilidade total do autor.

Showcase. A própria apresentação oficial em https://remarkjs.com demonstra o padrão visual e o modo apresentador.

### 4.6. reveal-md

Repositório: https://github.com/webpro/reveal-md
Documentação: README do repositório

Métricas em 19/10/2026: 3.912 estrelas, 414 forks, 12 issues + PRs, último commit e release 6.1.4 em 27/11/2024, licença MIT, repositório arquivado.

O que é. CLI que transforma arquivos Markdown em apresentações reveal.js, com servidor local, live reload, temas, highlight themes, atributos de slide, frontmatter YAML e scripts customizados. O diferencial é o zero-config sobre o reveal.js: um comando abre o Markdown como deck.

Qualidade visual. Herda os temas do reveal.js e permite CSS customizado e tema remoto. A qualidade depende inteiramente do tema e do CSS escolhidos. O recurso de destaque de linhas de código (` ```python [1|3-6] `) é útil para palestras técnicas.

Exportação e apresentação. PDF via Puppeteer ou via Docker com DeckTape, site estático, notas do apresentador e live reload. O README documenta todas essas opções.

Curva e manutenção. Baixa. O projeto, porém, está arquivado e o próprio README declara que não está mais em desenvolvimento ativo. A recomendação oficial é migrar para MkSlides ou Slidev.

Casos ideais. Manutenção de decks antigos que já usam reveal-md. Para novos projetos, não é recomendável.

Limitações. Sem desenvolvimento ativo, sem novos recursos e com dependências antigas. O README recomenda explicitamente alternativas.

Showcase. Não há galeria oficial; a referência é o README e os decks de exemplo do repositório.

### 4.7. Spectacle

Repositório: https://github.com/FormidableLabs/spectacle
Site e documentação: https://commerce.nearform.com/open-source/spectacle/

Métricas em 19/10/2026: 10.181 estrelas, 701 forks, 83 issues + PRs, último commit em 24/09/2026, release 10.2.3 em 10/10/2025, licença MIT. npm `spectacle`: 425.103 downloads no último mês.

O que é. Biblioteca React/TypeScript para apresentações em JSX ou Markdown. O `create-spectacle` oferece quatro modelos: one page em HTML único com htm, app Markdown, app React com Vite e app React com webpack. O diferencial é a liberdade de React: qualquer componente, biblioteca ou estado da aplicação pode entrar no slide.

Qualidade visual. O sistema de temas é um objeto de duas camadas baseado em styled-system, com chaves para cores, fontes, espaçamentos, bordas, sombras e z-index. Não há uma galeria de temas prontos como em Slidev ou Marp; há um tema default e um sistema de template para overlays. O resultado pode ser sofisticado, mas exige designer ou bom gosto de front-end. Recursos incluem transições por slide, autoPlay, `CodePane` com syntax highlighting e faixas de código destacadas, `Appear` para animações e componentes de layout.

Exportação e apresentação. A FAQ documenta exportação para PDF com `?exportMode=true` e impressão pelo navegador; há também `printMode=true` para preto e branco. Não há PPTX documentado. O modo apresentador abre uma segunda janela com slides e notas.

Curva e manutenção. Exige React, build e noções de TypeScript. É mais pesado do que Marp ou Slidev para um deck simples, mas mais flexível do que ambos quando o slide precisa de comportamento de aplicação. O projeto está ativo, com commits recentes e versão 10.

Casos ideais. Apresentações de produto, demos de bibliotecas React, slides que precisam de estado, gráficos interativos, componentes da própria empresa e talks em que o deck é parte do produto.

Limitações. Sem galeria de temas prontos. Exportação apenas em PDF. Exige build React. O posicionamento do repositório fala em "live demo your code", mas o `CodePane` documentado é exibição com highlight, não execução de código; não confirmei execução dentro do slide.

Showcase. O site oficial mostra o deck default e a documentação; não localizei uma galeria pública de showcases de terceiros.

### 4.8. mdx-deck

Repositório: https://github.com/jxnblk/mdx-deck
Site: https://mdx-deck.jxnblk.com (não respondeu em 19/10/2026)

Métricas em 19/10/2026: 11.500 estrelas, 594 forks, 141 issues + PRs, último commit em 03/08/2021, última publicação npm 4.1.1 em 12/03/2020, licença MIT. npm `mdx-deck`: 2.649 downloads no último mês. O demo oficial retornou erro de conexão na verificação.

O que é. Ferramenta React baseada em MDX, com CLI zero-config: cada slide é um trecho de Markdown que aceita JSX e componentes React. O diferencial foi popularizar a ideia de deck como aplicação React com MDX, tema via Theme UI e componentes reutilizáveis.

Qualidade visual. Temas embutidos (a documentação mostra future, comic e yellow), Theme UI e Emotion para estilização, componentes `Notes`, `Head`, `Header`, `Footer` e `Steps`, layouts customizados e integração com CodeSurfer para código animado. O visual pode ser muito bom, mas o padrão é datado em relação a Slidev.

Exportação e apresentação. O README documenta modo apresentador com `Option + P`, timer, próximo slide e notas, além de duas janelas sincronizadas. Não encontrei exportação oficial para PDF ou PPTX no README.

Curva e manutenção. Exige React e MDX. O projeto está efetivamente abandonado: último commit em 2021 e última publicação em 2020. Um comentário no Hacker News em 2024 diz que "mdx-deck não é mais desenvolvido" e que o autor migrou para Marp CLI para a tarefa. https://news.ycombinator.com/item?id=41709690

Casos ideais. Manutenção de decks antigos em MDX/React. Para novos projetos, Slidev ou Spectacle cobrem o mesmo terreno com manutenção ativa.

Limitações. Abandono, demo offline, sem exportação documentada, dependências antigas e risco de incompatibilidade com React atual.

Showcase. O demo em https://mdx-deck.jxnblk.com não respondeu; a referência visual restante é o GIF e as imagens do README.

### 4.9. WebSlides

Repositório: https://github.com/webslides/WebSlides
Site e demos: https://webslides.tv
Demos: https://webslides.tv/demos

Métricas em 19/10/2026: 6.327 estrelas, 585 forks, 82 issues + PRs, último commit em 05/09/2020, release 1.5.0 em 16/09/2017, licença MIT.

O que é. Sistema de apresentações em HTML e CSS puro, sem build e sem Markdown. Cada `<section>` dentro de `#webslides` é um slide. O diferencial é o design editorial: componentes prontos, tipografia cuidada e uma estética de revista que raramente aparece em frameworks de slides.

Qualidade visual. É o projeto com maior impacto visual pronto da lista. O site promete 40+ componentes (capas, cards, citações, métricas, backgrounds), 500+ ícones SVG, 120+ slides premium e ritmo vertical de 8 px. As fontes documentadas são Roboto, Maitree (serifada) e San Francisco. Há navegação horizontal e vertical, permalinks, contador, autoslide, suporte a toque e apresentadores remotos. A integração com animate.css e particles.js é possível, mas externa.

Exportação e apresentação. A saída é HTML estático. O README não documenta exportação para PDF ou PPTX; a impressão depende do CSS. Há navegação por teclado e permalinks, mas não encontrei notas do apresentador documentadas.

Curva e manutenção. Baixa para HTML/CSS, média para manter consistência visual. O projeto está estagnado desde 2020 e a última release é de 2017. O código é simples e legível, o que ajuda a manter, mas não há correções de segurança ou compatibilidade com navegadores recentes.

Casos ideais. Decks de marketing, apresentações editoriais, portfólios, landing pages de evento, stories e materiais em que o visual vale mais do que a interatividade ou o PDF.

Limitações. Sem Markdown, sem build, sem notas, sem exportação oficial, sem manutenção ativa. O HTML manual fica verboso em decks longos.

Showcase. A galeria oficial inclui "Netflix's Culture", "Landings", "Portfolios" e "Keynote", todos navegáveis em https://webslides.tv/demos.

### 4.10. Shower

Repositório: https://github.com/shower/shower
Site e demo: https://shwr.me

Métricas em 19/10/2026: 4.876 estrelas, 853 forks, 40 issues + PRs, último commit em 14/10/2026, npm `@shower/core` 3.6.0 em 07/07/2026, licença MIT.

O que é. Motor de apresentações em HTML, CSS e JavaScript vanilla, com temas separados do motor. Cada slide é uma `<section class="slide">`. Há dois temas oficiais, Ribbon e Material, e um CLI para criar, servir, empacotar e publicar. O diferencial é a acessibilidade: navegação completa por teclado, foco visível e estrutura semântica.

Qualidade visual. O visual é limpo, tipográfico e discreto. Ribbon é o tema clássico; Material segue o Material Design. O motor oferece gerenciamento de slides, navegação, barra de progresso, timer e navegação interna para revelar itens. Não é um sistema de design rico como WebSlides, mas o resultado é elegante e consistente.

Exportação e apresentação. Imprime para PDF pelo navegador, funciona como HTML estático e pode ser publicado pelo CLI. Não há modo apresentador com notas documentado; o timer e a barra de progresso são os recursos de palco.

Curva e manutenção. Baixa para quem conhece HTML/CSS. O projeto está ativo, com release de 2026 e commits recentes. A comunidade é menor e concentrada no público de língua russa, mas o código é estável.

Casos ideais. Apresentações corporativas ou técnicas que precisam de acessibilidade, decks leves sem build, materiais que serão impressos em PDF e situações em que o autor quer HTML semântico e controle de CSS.

Limitações. Apenas dois temas oficiais. Sem Markdown, sem notas de apresentador documentadas, sem PPTX. O visual não tem o impacto de WebSlides ou Slidev por padrão.

Showcase. A home https://shwr.me é o próprio deck de demonstração, com os dois temas e os recursos do motor.

### 4.11. impress.js

Repositório: https://github.com/impress/impress.js
Site e demo: https://impress.github.io/impress.js/

Métricas em 19/10/2026: 38.155 estrelas, 6.567 forks, 61 issues + PRs, último commit em 23/07/2026, release v2.0.0 em 22/07/2022, licença MIT.

O que é. Framework de apresentações baseado em transformações CSS3 3D, inspirado no Prezi. Cada slide é um elemento posicionado em um plano 3D com `data-x`, `data-y`, `data-z`, `data-rotate` e `data-scale`. O diferencial é a navegação espacial: a câmera voa entre pontos do canvas em vez de avançar páginas.

Qualidade visual. O impacto é único quando bem usado. Não há temas, componentes ou sistema tipográfico: o autor define todo o CSS. O resultado pode ser memorável ou desorientador. A demo oficial e a "Classic Slides" mostram que é possível fazer um deck tradicional, mas o valor está justamente no layout não linear.

Exportação e apresentação. A saída é HTML estático. Não há exportação PDF, PPTX ou modo apresentador com notas documentados. A navegação é por teclado e a API é JavaScript.

Curva e manutenção. Alta. Posicionar slides em 3D e manter legibilidade exige experimentação. O projeto está ativo em commits, mas a última release é de 2022. A base de 38 mil estrelas reflete a fama histórica, não adoção recente.

Casos ideais. Keynotes de alto impacto, visualizações espaciais, storytelling não linear, demos de produto e peças de portfólio em que a navegação é parte da mensagem.

Limitações. Não serve para decks densos de conteúdo. Não tem temas, notas ou exportação. Pode causar desconforto visual e tem desafios de acessibilidade e responsividade.

Showcase. A demo oficial em https://impress.github.io/impress.js/ e o exemplo "Classic Slides" em http://impress.github.io/impress.js/examples/classic-slides/.

### 4.12. Fusuma

Repositório: https://github.com/hiroppy/fusuma
Site e demos: https://hiroppy.github.io/fusuma/

Métricas em 19/10/2026: 5.356 estrelas, 190 forks, 85 issues + PRs, último commit em 01/12/2021, npm 2.8.4 em 15/05/2021, release GitHub v2.8.3 em 30/03/2021. Licença MIT declarada no `package.json`, sem arquivo LICENSE no repositório. Repositório arquivado.

O que é. CLI Node para criar slides em Markdown ou MDX com React, configuração zero, temas, build otimizado, PDF, deploy para GitHub Pages, modo apresentador com notas, timer e gravação de ações e voz. O README também promete SEO/OGP e checagem de acessibilidade.

Qualidade visual. Cinco temas documentados (default, pop, webpack, babel, node), syntax highlight, MathJax, diagramas e fluxogramas, sidebar com agenda e CSS customizável. O resultado é bom e a proposta era sofisticada para 2021. Hoje o visual está datado em relação a Slidev.

Exportação e apresentação. PDF, build HTML, deploy GitHub Pages, modo apresentador com notas, timer e gravação. O build gera imagem de capa para `og:image`.

Curva e manutenção. Exige Node e React/MDX para recursos avançados. O projeto está arquivado e sem manutenção desde 2021. npm registra 201 downloads no último mês, sinal de uso residual.

Casos ideais. Manutenção de decks antigos. Para novos projetos, não é recomendável por risco de dependências e segurança.

Limitações. Arquivado, dependências antigas, documentação congelada, sem correções. A licença está no manifesto, mas não há arquivo LICENSE, o que pode complicar revisão jurídica.

Showcase. A demo "Introducing Fusuma" em https://hiroppy.github.io/fusuma/intro e a galeria de temas em https://hiroppy.github.io/fusuma/themes/.

### 4.13. backslide

Repositório: https://github.com/sinedied/backslide
Site e demo: https://sinedied.github.io/backslide

Métricas em 19/10/2026: 777 estrelas, 50 forks, 15 issues + PRs, último commit e release 3.1.0 em 15/03/2022, licença MIT. npm `backslide`: 168 downloads no último mês.

O que é. CLI para criar apresentações HTML com Remark.js a partir de Markdown. O fluxo é `bs init`, `bs serve` e `bs export`/`bs pdf`. O diferencial é o template com Sass, o HTML autocontido e a exportação de PDF via DeckTape.

Qualidade visual. O visual vem do Remark.js e do template Sass do projeto. É limpo e funcional, mas não tem a riqueza de temas ou componentes de ferramentas mais novas. A customização é toda via `style.scss`.

Exportação e apresentação. HTML autocontido, PDF via DeckTape, modo website, remoção de notas para handout e remoção de fragmentos. As notas do apresentador vêm do Remark.js.

Curva e manutenção. Baixa para Markdown e Sass. O projeto está estagnado desde 2022 e depende do Remark.js, que também está parado.

Casos ideais. Decks simples baseados em Remark.js, materiais que precisam de um único HTML e PDF, e manutenção de projetos existentes.

Limitações. Sem manutenção, sem PPTX, dependência de Remark.js legado e ecossistema pequeno.

Showcase. A apresentação de exemplo em https://sinedied.github.io/backslide.

### 4.14. nodeppt

Repositório: https://github.com/ksky521/nodeppt
Site e demo: https://nodeppt.js.org

Métricas em 19/10/2026: 10.328 estrelas, 2.021 forks, 27 issues + PRs, último commit em 25/01/2021, npm 2.2.2 em 28/06/2020, licença MIT. Repositório arquivado.

O que é. Ferramenta chinesa de apresentações Markdown, reconstruída na versão 2.0 sobre WebSlides, webpack, markdown-it e posthtml. O Markdown é dividido por tags `<slide>`, com YAML no topo para configuração. O diferencial é o pacote de plugins: ECharts para gráficos, Mermaid para diagramas e KaTeX para matemática, além de modo apresentador com `?mode=speaker`.

Qualidade visual. A base WebSlides garante um visual editorial acima da média, e os plugins de gráficos e diagramas ampliam o repertório. A documentação é em chinês, o que limita a adoção fora desse público. O resultado pode ser sofisticado, mas o código e o webpack são de outra época.

Exportação e apresentação. O README documenta `nodeppt build` para gerar o site estático e `?mode=speaker` para o modo apresentador com duas telas sincronizadas. Não encontrei exportação PDF ou PPTX documentada.

Curva e manutenção. Exige Node e webpack. O projeto está arquivado desde 2021 e sem release desde 2020. Não é opção para 2026.

Casos ideais. Manutenção de decks chineses existentes e estudo de uma abordagem inicial de Markdown com plugins.

Limitações. Arquivado, documentação em chinês, webpack legado, sem exportação PDF/PPTX documentada, dependências antigas.

Showcase. https://nodeppt.js.org exibe o resultado do nodeppt 2.0.

### 4.15. Eagle.js

Repositório: https://github.com/Zulko/eagle.js
Site e demo: https://zulko.github.io/eaglejs-demo/

Métricas em 19/10/2026: 4.047 estrelas, 214 forks, 13 issues + PRs, último commit em 10/07/2022, npm 0.6.1 em 23/10/2019, licença ISC. npm `eagle.js`: 99 downloads no último mês.

O que é. Framework de slides para Vue 2, com componentes `slideshow` e `slide`, widgets interativos, animações via animate.css, temas e API pública para hackear. O diferencial é a organização em componentes Vue e a facilidade de reutilizar slides e estilos entre apresentações.

Qualidade visual. Bom para demos interativos e slides com componentes Vue. As transições vêm do animate.css e os widgets permitem conteúdo manipulável. Não há um sistema de temas tão rico quanto o de concorrentes atuais.

Exportação e apresentação. O README não documenta exportação PDF/PPTX nem modo apresentador com notas. O foco é a apresentação no navegador.

Curva e manutenção. Exige Vue 2 e Node. O projeto se declara "feature-completed" e recomenda Slidev para Vue 3. O último commit é de 2022 e a última publicação npm é de 2019. Está efetivamente morto.

Casos ideais. Manutenção de decks Vue 2 existentes. Para novos projetos, Slidev é o sucessor natural.

Limitações. Vue 2 fora de suporte, sem manutenção, sem exportação documentada, dependências antigas.

Showcase. A demo "Introducing Eagle" em https://zulko.github.io/eaglejs-demo/#/introducing-eagle.

### 4.16. Bespoke.js

Repositório: https://github.com/bespokejs/bespoke
Site: http://markdalgleish.com/projects/bespoke.js/ (histórico)

Métricas em 19/10/2026: 4.793 estrelas, 446 forks, 6 issues + PRs, último commit em 08/09/2020, npm 1.1.0 em 24/09/2015, licença MIT. npm `bespoke`: 1.226 downloads no último mês.

O que é. Micro-framework de apresentações com 1 KB minificado e gzipado. O núcleo só monta o deck, oferece API de controle e eventos; tudo o mais é plugin: teclado, toque, classes, bullets, escala, hash, backdrop, estado. O diferencial é o tamanho e a modularidade extrema.

Qualidade visual. O núcleo não tem visual. O autor escolhe ou gera um tema com o gerador Yeoman. O resultado depende inteiramente dos plugins e do CSS. Não há um sistema de design pronto.

Exportação e apresentação. A saída é HTML estático. Não há exportação PDF/PPTX nem modo apresentador com notas no núcleo; qualquer recurso precisa de plugin ou código próprio.

Curva e manutenção. Baixa para montar, alta para chegar a um deck completo. O projeto está parado desde 2020 e a última release é de 2015.

Casos ideais. Apresentações embutidas em páginas existentes, widgets de slides em produtos e experimentos que precisam de um motor mínimo.

Limitações. Sem manutenção, sem temas prontos, sem notas, sem exportação. É uma base, não uma solução.

Showcase. Não há galeria oficial ativa; a referência é a documentação e os geradores do ecossistema.

### 4.17. Outros projetos com tração

DeckDeckGo. https://github.com/deckgo/deckdeckgo. 1.674 estrelas, 188 forks, 117 issues + PRs, último commit em 06/02/2024, release v7.1.0 em 31/10/2022, repositório arquivado. Era um editor web open source de apresentações, com abordagem de app e PWA. Está arquivado, sem licença detectada pela API. Não é opção para 2026.

MkSlides. https://github.com/MartenBE/mkslides. 481 estrelas, 21 forks, 1 issue + PR, último commit em 11/10/2026, release 2.0.23 em 30/09/2026, licença MIT. É o sucessor indicado pelo próprio reveal-md: transforma Markdown em slides reveal.js, com foco em simplicidade e manutenção ativa. Vale acompanhar como substituto direto do reveal-md, embora a base de usuários ainda seja pequena.

## 5. Comparações e sinais de comunidade

### 5.1. Hacker News

O lançamento do Slidev em 05/05/2021 teve 125 pontos e 23 comentários. A discussão mostra a comparação imediata com reveal.js e Marp e a percepção de que o Slidev reduzia o atrito de formatação e deploy. https://news.ycombinator.com/item?id=27050687

Em outubro de 2024, uma pergunta sobre ferramentas Markdown para slides trouxe três sinais úteis: mdx-deck "não é mais desenvolvido"; Marp CLI "fez o trabalho" para quem testou; e Slidev foi recomendado por permitir componentes Vue e plugins. https://news.ycombinator.com/item?id=41709690

Em 2026, uma discussão sobre fluxo com Claude Code mencionou Quarto para PPTX, Beamer e revealjs e Slidev para apresentações sobre software. A distinção feita na thread é que Slidev é desenhado para conteúdo de desenvolvimento, enquanto Quarto é mais geral. https://news.ycombinator.com/item?id=47112673

### 5.2. Comparativos secundários

Três comparativos recentes convergem na mesma divisão: Slidev para talks técnicos com Markdown e código; reveal.js para controle de HTML e portabilidade; Marp para simplicidade e PDF. Os textos são de 2026 e batem com as métricas de estrelas coletadas.

- PaneFlow, "Slidev vs Reveal.js: Which Should You Use? (2026)", 22/09/2026. https://paneflow.com/compare/slidev-vs-reveal-js
- Variant, "Reveal.js vs Slidev", 27/08/2026. https://www.variant.art/blog/reveal-js-vs-slidev
- Deckary, "HTML Presentations: Reveal.js, Slidev, Marp & AI", 09/08/2026. https://deckary.com/blog/html-presentations

Ressalva de fonte: PaneFlow vende uma alternativa aos dois frameworks, e Deckary e Variant também comercializam produtos de apresentação. Os textos servem para mapear recursos e objeções, não como benchmark neutro. As afirmações de recursos foram conferidas na documentação oficial quando possível.

### 5.3. Adoção no npm

Downloads no último mês, coletados em 19/10/2026:

| Pacote | Downloads |
|---|---:|
| reveal.js | 571.757 |
| spectacle | 425.103 |
| @marp-team/marp-core | 405.311 |
| @slidev/cli | 393.213 |
| @marp-team/marp-cli | 235.700 |
| mdx-deck | 2.649 |
| nodeppt | 1.546 |
| bespoke | 1.226 |
| fusuma | 201 |
| backslide | 168 |
| eagle.js | 99 |

Os números de reveal.js, Spectacle, Marp e Slidev são da mesma ordem de grandeza. mdx-deck, nodeppt, bespoke, fusuma, backslide e Eagle.js estão abaixo de 3 mil downloads mensais, apesar de somarem mais de 35 mil estrelas. Estrelas medem interesse histórico; downloads medem uso corrente.

## 6. Recomendações por cenário

| Cenário | Primeira escolha | Alternativa | Evitar |
|---|---|---|---|
| Palestra técnica com código e live coding | Slidev | Spectacle | WebSlides, Shower |
| Deck HTML sob controle total, sem build | reveal.js | Shower | Slidev, Quarto |
| Markdown para PDF e PPTX | Marp | Quarto | remark, backslide |
| Aula ou relatório com dados reprodutíveis | Quarto | Marp | WebSlides |
| Slide como aplicação React | Spectacle | mdx-deck (só legado) | Marp, WebSlides |
| Impacto editorial com pouco código | WebSlides | Shower | Slidev, Quarto |
| Acessibilidade e HTML semântico | Shower | reveal.js | impress.js |
| Navegação 3D e storytelling espacial | impress.js | reveal.js com transições | Marp, Quarto |
| Compatibilidade com decks antigos | reveal.js ou o framework original | MkSlides para reveal-md | Fusuma, nodeppt, Eagle.js |
| Migração de reveal-md | MkSlides | Slidev | reveal-md |

## 7. Lacunas e o que não foi confirmado

- Não foi possível testar visualmente todos os frameworks em ambiente controlado. As avaliações de qualidade visual são inferências a partir de temas, componentes, documentação e demos oficiais, não de um teste cego com designers.
- O demo oficial do mdx-deck não respondeu em 19/10/2026. A avaliação visual desse projeto se apoia no README e nas imagens de tema.
- Não confirmei se a extensão Marp para VS Code oferece visão de apresentador com notas. A visão do apresentador está documentada no template do Marp CLI.
- Não encontrei documentação oficial de exportação PDF/PPTX para Eagle.js, Bespoke.js, WebSlides, Shower, impress.js e nodeppt. A ausência foi registrada como "não documentado", não como impossibilidade técnica.
- Não localizei uma galeria oficial de showcases do Spectacle. O site oficial mostra o deck default e a documentação.
- Não foram encontrados threads relevantes no Reddit nem benchmarks quantitativos de qualidade visual. A cobertura de comunidade se concentra no Hacker News e em comparativos de fornecedores.
- As contagens de estrelas, forks e issues mudam ao longo do dia. Os valores valem para a janela de coleta de 19/10/2026, 13:20 a 13:45 UTC.
- A contagem de issues do GitHub inclui pull requests. Para projetos grandes, ela superestima a quantidade de problemas abertos.
- Quarto não é um framework de slides no mesmo sentido dos demais. Ele foi incluído porque a saída `revealjs` é uma das formas mais usadas de fazer apresentações científicas em HTML e porque o pedido o listou explicitamente.

## 8. Fontes primárias consultadas

Repositórios e APIs:

- https://api.github.com/repos/slidevjs/slidev
- https://api.github.com/repos/hakimel/reveal.js
- https://api.github.com/repos/marp-team/marp
- https://api.github.com/repos/marp-team/marp-cli
- https://api.github.com/repos/marp-team/marp-core
- https://api.github.com/repos/quarto-dev/quarto-cli
- https://api.github.com/repos/gnab/remark
- https://api.github.com/repos/webpro/reveal-md
- https://api.github.com/repos/FormidableLabs/spectacle
- https://api.github.com/repos/jxnblk/mdx-deck
- https://api.github.com/repos/webslides/WebSlides
- https://api.github.com/repos/shower/shower
- https://api.github.com/repos/impress/impress.js
- https://api.github.com/repos/hiroppy/fusuma
- https://api.github.com/repos/sinedied/backslide
- https://api.github.com/repos/ksky521/nodeppt
- https://api.github.com/repos/Zulko/eagle.js
- https://api.github.com/repos/bespokejs/bespoke
- https://api.github.com/repos/deckgo/deckdeckgo
- https://api.github.com/repos/MartenBE/mkslides

Documentação e demos:

- https://sli.dev/guide/why
- https://sli.dev/guide/ui
- https://sli.dev/guide/exporting
- https://sli.dev/resources/showcases
- https://revealjs.com/
- https://revealjs.com/themes/
- https://revealjs.com/demo/
- https://marp.app/
- https://marpit.marp.app/usage?id=presenter-notes
- https://github.com/marp-team/marp-cli
- https://github.com/marp-team/marp-core
- https://quarto.org/docs/presentations/
- https://quarto.org/docs/presentations/revealjs/presenting.html
- https://quarto.org/docs/presentations/revealjs/demo/
- https://quarto.org/docs/authoring/diagrams.html
- https://remarkjs.com/
- https://github.com/webpro/reveal-md
- https://commerce.nearform.com/open-source/spectacle/docs/
- https://commerce.nearform.com/open-source/spectacle/docs/faq
- https://commerce.nearform.com/open-source/spectacle/docs/themes
- https://commerce.nearform.com/open-source/spectacle/docs/api-reference
- https://github.com/jxnblk/mdx-deck
- https://webslides.tv/
- https://webslides.tv/demos
- https://shwr.me/
- https://impress.github.io/impress.js/
- https://hiroppy.github.io/fusuma/
- https://sinedied.github.io/backslide
- https://nodeppt.js.org
- https://zulko.github.io/eaglejs-demo/
- https://github.com/bespokejs/bespoke
- https://deckdeckgo.com

Comunidade e comparativos:

- https://news.ycombinator.com/item?id=27050687
- https://news.ycombinator.com/item?id=41709690
- https://news.ycombinator.com/item?id=47112673
- https://paneflow.com/compare/slidev-vs-reveal-js
- https://www.variant.art/blog/reveal-js-vs-slidev
- https://deckary.com/blog/html-presentations
- https://api.npmjs.org/downloads/point/last-month/reveal.js
- https://api.npmjs.org/downloads/point/last-month/@slidev/cli
- https://api.npmjs.org/downloads/point/last-month/@marp-team/marp-cli
- https://api.npmjs.org/downloads/point/last-month/@marp-team/marp-core
- https://api.npmjs.org/downloads/point/last-month/spectacle
