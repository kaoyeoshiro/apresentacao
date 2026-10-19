# Escolha a ferramenta certa para cada apresentação

Em 19/10/2026, a melhor escolha geral para apresentações de alta qualidade é o Slidev: 49.127 estrelas, licença MIT, release v53.0.0 em setembro de 2026 e atividade mensal. Ele combina Markdown (texto com marcações simples), componentes Vue, código com destaque, diagramas e animação sem exigir que o autor monte um site do zero. O custo é tratar o deck como um pequeno projeto Node (ambiente JavaScript), o que se paga em palestras técnicas e aulas com código.

Para PDF e PowerPoint em um comando, o Marp é a via mais curta. Para academia com dados e citação, o Quarto tem o fluxo mais completo. Para terminal, o presenterm tem o conjunto mais amplo. O Touying entrega o PDF tipograficamente mais bonito quando o autor aceita aprender Typst. Estrelas, porém, não medem saúde: o mdx-deck tem 11.500 e está sem commits desde 2021, o WebSlides tem 6.327 e parou em 2020, e o Metropolis tem 6.907 e está congelado desde 2018. Os números vêm da API do GitHub, entre 13h20 e 13h45 UTC de 19/10/2026.

## 1. Recomendação prática

A melhor escolha geral é o Slidev, pela combinação de visual, animação, código e comunidade para palestra técnica. Para impacto visual, a mesma ferramenta lidera, com o Touying como resposta quando o impacto vem da tipografia e do PDF; o WebSlides tem o visual editorial mais pronto, mas está parado desde 2020.

Para simplicidade, o Marp resolve com um arquivo Markdown, um comando e saída em HTML, PDF, PPTX ou imagem. Para academia, o Quarto é a primeira escolha, com Beamer para quem já vive em LaTeX e Touying para quem já usa Typst. Para terminal, o presenterm oferece imagens, colunas, Mermaid, fórmulas, notas e exportação para PDF e HTML. Para pitch deck e relatório corporativo, nenhum projeto aberto supera PowerPoint, Keynote ou Google Slides em colaboração; entre os repositórios, o Presenton serve para rascunho com IA e o PPTist para edição web.

## 2. Como a pesquisa foi feita

As métricas vieram da API REST do GitHub, pelos endpoints `GET /repos/{owner}/{repo}`, `GET /releases/latest` e `GET /commits?per_page=1`, com autenticação. A coleta ocorreu em 19/10/2026, entre 13h20 e 13h45 UTC. A contagem de issues usa `open_issues_count`, que soma issues e pull requests e superestima bugs em projetos grandes. Downloads do npm cobrem 19/09/2026 a 18/10/2026; os do PyPI usam o último mês fechado.

Há três níveis de confiança. O primeiro reúne estrelas, forks, issues mais PRs, último commit, último release, licença e downloads. O segundo é julgamento sobre qualidade visual, curva de aprendizado e melhor uso, com base em documentação, GIFs, PDFs de demonstração e demos oficiais, sem teste cego com designers. O terceiro é o que não foi confirmado: fidelidade real de PPTX, desempenho na máquina do leitor, preços de licença comercial e uso corporativo.

A atividade é classificada como ativa, com commit ou release em 12 meses; lenta, entre 12 e 24 meses; estagnada, acima de 24 meses; ou arquivada, pelo campo `archived`. Não instalei, compilei, cronometrei ou renderizei os projetos.

## 3. O mapa que evita a escolha errada

A escolha envolve três camadas técnicas. Na primeira camada estão os frameworks de runtime, como reveal.js, Shower e impress.js: o autor controla HTML, CSS e JavaScript, e o limite visual depende do front-end. Na segunda estão as ferramentas Markdown com exportação, como Slidev, Marp, Quarto e presenterm: o custo de entrada é baixo, o resultado depende do tema e a saída pode ser PDF, PPTX, HTML ou imagem. Na terceira estão componentes e recursos, como Excalidraw, Mermaid e Remotion: eles não substituem o framework, mas elevam um slide específico.

As métricas de popularidade não acompanham a adequação. O reveal.js tem 72.441 estrelas e 571.757 downloads mensais, mas exporta apenas PDF no núcleo. O Slidev tem 49.127 estrelas e 393.213 downloads, com PPTX e componentes Vue. O Marp CLI tem 3.874 estrelas e 235.700 downloads. O Spectacle tem 425.103 downloads e um único commit em 12 semanas. A contagem de downloads também não é sinal de atividade.

## 4. Frameworks web e Markdown

### 4.1. Slidev

O Slidev escreve Markdown sobre Vue 3 e Vite, com componentes Vue, Shiki, KaTeX, Mermaid, ícones e animações ([Slidev](https://github.com/slidevjs/slidev)). O resultado padrão é limpo e sobe com um bom tema. Exporta PDF, PPTX, PNG e site estático. O PPTX padrão rasteriza cada slide; o modo editável reconstrói formas, mas SVG, canvas, vídeo e fórmulas continuam imagem ([guia](https://sli.dev/guide/exporting)). A curva é de 1 a 3 horas. Tem 49.127 estrelas, MIT, release v53.0.0 em setembro de 2026 e 70% dos commits de antfu. Os showcases listam talks em KubeCon, FOSSASIA e LASCON ([showcases](https://sli.dev/resources/showcases)).

### 4.2. reveal.js

O reveal.js é o framework HTML de 2011. Cada slide é uma `<section>`, com plugins em JavaScript e CSS; Markdown entra por plugin ([reveal.js](https://github.com/hakimel/reveal.js)). Tem 12 temas e teto visual alto, com Auto-Animate, fundos com vídeo e iframe e matemática. Exporta PDF, sem PPTX, e roda offline. A curva é de 1 a 2 horas, mais para um visual autoral. Tem 72.441 estrelas, MIT, release 6.0.2 em setembro de 2026, mas 93% das issues abertas têm mais de 18 meses e 84% dos commits são de hakimel. O PDF não tem metadados de idioma nem cabeçalhos, o que inviabiliza PDF/UA (padrão de acessibilidade) ([discussão 3733](https://github.com/hakimel/reveal.js/discussions/3733)).

### 4.3. Marp

O Marp é a via mais curta entre Markdown e um arquivo que outra pessoa abre. O conjunto de ferramentas tem Marpit, Marp Core e Marp CLI ([Marp](https://github.com/marp-team/marp)). Exporta HTML, PDF, PPTX e imagens. O PPTX padrão é rasterizado; o modo `--pptx-editable` é experimental, exige LibreOffice, perde fidelidade e não suporta notas ([CLI](https://github.com/marp-team/marp-cli)). A curva é de 30 minutos. O CLI tem 3.874 estrelas, MIT, v4.5.1 em setembro de 2026 e 235.700 downloads, mas 96% dos commits são de yhatt; o repositório de entrada tem 12.656. Interação e layout fora do padrão são o limite.

### 4.4. Spectacle, Shower e impress.js

O Spectacle trata o deck como app React, tem 10.181 estrelas, MIT, exporta PDF e tem manutenção mínima ([Spectacle](https://github.com/FormidableLabs/spectacle)). O Shower é um motor vanilla com foco em acessibilidade, 4.876 estrelas, MIT e atividade recente; exporta HTML e PDF, sem notas documentadas ([Shower](https://github.com/shower/shower)). O impress.js posiciona slides em 3D, com 38.155 estrelas, MIT e release de 2022 ([impress.js](https://github.com/impress/impress.js)).

## 5. Terminal

O presenterm lê Markdown e apresenta no terminal. É escrito em Rust e trata o terminal como superfície gráfica: imagens em kitty, iTerm2, WezTerm, Ghostty e foot, Mermaid, D2, fórmulas LaTeX e Typst, realce de código, colunas e execução de snippets ([presenterm](https://github.com/mfontanini/presenterm)). É o mais convincente para live coding e demos de CLI. Exporta PDF via weasyprint e HTML, sem PPTX. As notas usam duas instâncias por UDP; no Mac, só um listener funciona por vez. A curva é de cerca de 1 hora. Tem 8.927 estrelas, BSD-2-Clause, release v0.16.1 em fevereiro de 2026 e último commit em maio de 2026. Está ativo, mas desacelerou.

O slides é um binário Go com Markdown, curva baixíssima e `slides serve` por SSH ([slides](https://github.com/maaslalani/slides)). Tem 11.690 estrelas e MIT, mas o último release é de 2022 e não há commits nas 12 semanas anteriores à coleta; não documenta imagens, exportação ou notas. O patat usa Pandoc, tem notas em segunda janela, 2.747 estrelas, GPL-2.0 e atividade baixa ([patat](https://github.com/jaspervdj/patat)). O lookatme embute um terminal vivo, mas está parado desde 2023 ([lookatme](https://github.com/d0c-s4vage/lookatme)). Para projeto novo, presenterm.

## 6. PDF, LaTeX, Typst e academia

### 6.1. Quarto

O Quarto é um sistema de publicação científica sobre Pandoc. Aceita `revealjs` em HTML, `pptx` e `beamer` em LaTeX/PDF; a documentação recomenda `revealjs` ([Quarto](https://quarto.org/docs/presentations/)). O mesmo documento executa Python, R, Julia ou Observable JS, gera gráficos, citações e referências cruzadas, e pode virar artigo, site e slide. O visual herda o reveal.js. Exporta HTML autocontido, PDF, PPTX e Beamer. A curva é de 2 a 4 horas. Tem 6.099 estrelas, MIT, release v1.10.19 em outubro de 2026 e 1.824 issues abertas, com atividade diária. É a escolha de menor risco institucional para aulas e dados ([Teaching with Quarto](https://mine-cetinkaya-rundel.github.io/teach-with-quarto/)).

### 6.2. Beamer e os temas

O Beamer é a referência para slides acadêmicos em PDF, com overlays, matemática, TikZ, notas e pacotes maduros. Está no TeX Live e no MiKTeX, e o repositório no GitHub é espelho ([CTAN](https://ctan.org/pkg/beamer)). A curva é de 1 a 2 dias para quem não vive em LaTeX. O Metropolis tem 6.907 estrelas e CC-BY-SA 4.0, mas o último release é de 2017 e o último commit de 2018 ([Metropolis](https://github.com/matze/mtheme)). Os temas mantidos são Focus (546, GPL-3.0), Auriga (405, MIT), Arguelles (283, MIT) e SimplePlus (279, Unlicense). O Focus é o mais próximo do Metropolis e o Arguelles é o mais tipográfico.

### 6.3. Touying e Polylux

O Touying é um pacote de slides para Typst com seis temas, animações por `#pause` e `#meanwhile`, animação de equações e integração com CeTZ e Fletcher ([Touying](https://github.com/touying-typ/touying)). O PDF é nativo; PPTX é experimental via Tylina ou `touying-exporter`; notas dependem de pdfpc, pympress, PowerPoint ou HTML. A curva é de 2 a 4 horas para quem já conhece Typst. Tem 2.392 estrelas, MIT, release 0.8.0 em setembro de 2026 e 75% dos commits de OrangeX4. Está ativo, mas é jovem e a API mudou na 0.8.0. O Polylux é o precursor minimalista, com 1.609 estrelas e MIT, sem temas; está dormente desde fevereiro de 2026 ([Polylux](https://github.com/polylux-typ/polylux)).

### 6.4. Pandoc e pdfpc

O Pandoc gera Beamer, PowerPoint, reveal.js e Typst a partir de Markdown ([Pandoc](https://github.com/jgm/pandoc)). Tem 46.629 estrelas, GPL-2.0, release 3.12.1 em outubro de 2026 e atividade intensa. O resultado depende do tema Beamer ou do documento de referência do PPTX. O pdfpc resolve notas, timer e visão geral para qualquer PDF, com 1.881 estrelas, GPL-3.0 e release v4.7.0 em dezembro de 2024 ([pdfpc](https://github.com/pdfpc/pdfpc)).

## 7. Geração por IA

O Presenton é um gerador auto-hospedado com API e aplicativo desktop. Cria slides a partir de prompt, documento ou template PPTX e funciona com Ollama, LM Studio, OpenAI, Gemini, Anthropic e provedores compatíveis ([Presenton](https://github.com/presenton/presenton)). Tem edição por arrastar, templates e exportação para PPTX editável e PDF. O diferencial é o controle: modelo, dados e design ficam na infraestrutura do usuário. A curva é de minutos para um rascunho e média para Docker, chave e template. Tem 11.212 estrelas, Apache-2.0, 43 releases em 12 meses e versão v0.9.11-beta. A fidelidade do PPTX é afirmação do fornecedor, sem teste independente.

O PPTAgent é um framework agêntico de pesquisa. Analisa apresentações de referência, extrai tipos de slide e esquemas, monta um outline e aplica ações de edição sobre slides de referência. O artigo foi aceito na EMNLP 2025, e o DeepPresenter, na ACL 2026 ([PPTAgent](https://github.com/icip-cas/PPTAgent), [arXiv](https://arxiv.org/abs/2501.03936)). Exporta PPTX, fontes HTML e previews. A qualidade depende do deck de referência, do modelo e dos ativos. A curva é alta: Python 3.12, uv, LibreOffice, Chrome e chaves de modelo. Tem 5.130 estrelas, MIT, release v2.0.0 em dezembro de 2025 e manutenção ativa.

O presentation-ai é um clone open source de Gamma, com fluxo outline-first, 38 temas, importação de tema PPTX e exportação PPTX ([presentation-ai](https://github.com/allweonedev/presentation-ai)). Tem 3.050 estrelas, MIT, nenhum release e último commit em junho de 2026. A stack é pesada e não documenta PDF. O PPTist é um editor web em Vue 3 com texto rico, formas, gráficos, tabelas, vídeo e AIPPT por templates ([PPTist](https://github.com/pipipi-pikachu/PPTist)). Declara 85% de fidelidade na importação e 95% na exportação de PPTX, números do README. Exporta PPTX, PDF por impressão, imagens, JSON e `.pptist`. Tem 9.409 estrelas, AGPL-3.0, nenhum release e commits até outubro de 2026. O README desaconselha usá-lo como ferramenta acabada.

## 8. Design, diagramas e animação

O Excalidraw é um whiteboard infinito com estética de desenho à mão, colaboração na versão web e exportação em PNG, SVG e JSON ([Excalidraw](https://github.com/excalidraw/excalidraw)). Tem 134.161 estrelas, MIT e atividade diária. É a melhor opção para rascunhos e anotações sobre screenshots. O Mermaid transforma texto em SVG, com mais de vinte tipos de diagrama ([Mermaid](https://mermaid.js.org/intro/)). Tem 90.748 estrelas, MIT e 1.499 issues mais PRs. O ganho é versionar o diagrama no Markdown; o layout automático impõe limites. O draw.io é a opção mais madura para diagramas densos, mas o repositório é uma versão de teste ([draw.io](https://github.com/jgraph/drawio)). A licença é Apache-2.0 com restrição para bibliotecas de ícones em produtos Atlassian.

O D2 foca em estética, com temas e layouts alternativos; tem 25.654 estrelas, MPL-2.0 e ainda está em v0.x ([D2](https://github.com/d2lang/d2)). O diagrams tem 42.742 estrelas, MIT e DSL Python para nuvem, com as limitações do Graphviz ([diagrams](https://github.com/mingrammer/diagrams)). O tldraw tem 50.984 estrelas e um SDK de canvas muito polido, mas a licença é própria e o uso em produção exige chave ([licença](https://tldraw.dev/community/license)).

O Remotion transforma vídeo em composição React e TypeScript, com render em MP4, Lambda e cliente ([Remotion](https://github.com/remotion-dev/remotion)). Tem 65.213 estrelas, release v4.0.536 em outubro de 2026, 8.052.542 downloads mensais e 4.702 commits em 12 semanas. É a melhor opção para abertura, gráficos data-driven e versão em vídeo do deck, com curva de 2 a 5 dias. A licença é própria: gratuito para indivíduos, organizações com até três funcionários, sem fins lucrativos e avaliação; acima disso, exige licença comercial. O Manim Community é o fork comunitário do motor do 3Blue1Brown, com 41.677 estrelas, MIT, release v0.22.0 em outubro de 2026 e 132.683 downloads mensais no PyPI ([Manim CE](https://github.com/ManimCommunity/manim)). É a melhor opção para matemática animada, com curva de 2 a 5 dias. O Motion Canvas tem 19.391 estrelas e MIT, mas está sem release estável desde dezembro de 2024 e sem commits em 12 semanas ([Canvas Commons](https://github.com/canvas-commons/.github)).

O GSAP tem 29.467 estrelas, licença própria e é gratuito para uso comercial desde 30/04/2025 ([GSAP](https://github.com/greensock/GSAP)). O anime.js tem 73.704 estrelas, MIT e release v4.5.0 em junho de 2026 ([anime.js](https://github.com/juliangarnier/anime)). Escolha um dos dois e use em poucos momentos. O [Carbon](https://github.com/carbon-app/carbon) e o VHS capturam código e terminal; o Playwright e o Penpot cobrem telas e mockups.

## 9. Temas e recursos visuais

Temas, tipografia e recursos visuais determinam a qualidade percebida. No Slidev, a galeria oficial e o repositório de temas são o caminho mais direto para um deck profissional; o repositório tem 221 estrelas, MIT e último push em julho de 2025 ([temas](https://github.com/slidevjs/themes)). No Marp, a lista oficial `awesome-marp` tem 523 estrelas e CC0-1.0 ([awesome-marp](https://github.com/marp-team/awesome-marp)). A lista comunitária `Awesome-Marp` tem 1.053 estrelas, mas não declara licença. No Beamer, a `ultimate-beamer-theme-list` tem 1.824 estrelas e nenhuma licença, então serve para descoberta ([lista](https://github.com/martinbjeldbak/ultimate-beamer-theme-list)).

O Lucide tem 25.143 estrelas, ISC e mais de 1.600 ícones ([Lucide](https://github.com/lucide-icons/lucide)). O Tabler tem 22.369 estrelas, MIT e 6.238 ícones ([Tabler](https://github.com/tabler/tabler-icons)). O Simple Icons tem 26.036 estrelas, CC0 e logotipos de marcas; a licença cobre o arquivo, mas as marcas continuam protegidas ([Simple Icons](https://github.com/simple-icons/simple-icons)). A Inter tem 19.978 estrelas e OFL-1.1, boa para texto e gráficos ([Inter](https://github.com/rsms/inter)).

## 10. Matriz comparativa

Estrelas e atividade em 19/10/2026, entre 13h20 e 13h45 UTC. "Atividade" resume commits e releases; "mínima", "beta" e "pesquisa" são julgamentos.

| Projeto | Estrelas | Licença | Atividade | Melhor uso |
|---|---:|---|---|---|
| Slidev | 49.127 | MIT | Muito ativa | Palestra técnica, código, demo |
| reveal.js | 72.441 | MIT | Ativa, fila antiga | Deck HTML sob controle total, offline |
| Marp | 12.656 entrada / 3.874 CLI | MIT | Ativa | PDF e PPTX rápidos, aula, relatório |
| Quarto | 6.099 | MIT | Muito ativa | Academia com dados, código e citação |
| Touying | 2.392 | MIT | Ativa, jovem | PDF tipográfico em Typst, matemática |
| Beamer | 1.722 | GPL-2.0+ / LPPL-1.3c | Estável, baixo volume | Academia formal em LaTeX |
| presenterm | 8.927 | BSD-2-Clause | Ativa, desacelerou | Terminal, SSH, live demo |
| PPTist | 9.409 | AGPL-3.0 | Ativa, sem releases | Editor PPTX web, produto interno |
| Presenton | 11.212 | Apache-2.0 | Beta intensa | Rascunho de pitch deck com IA |
| Spectacle | 10.181 | MIT | Mínima | Deck como aplicação React |
| Excalidraw | 134.161 | MIT | Muito ativa | Diagramas e rascunhos, não slides |
| Remotion | 65.213 | Própria, limite de 3 funcionários | Muito ativa | Vídeo programático, motion graphics |
| Manim Community | 41.677 | MIT | Muito ativa | Animação matemática explicativa |
| Pandoc | 46.629 | GPL-2.0 | Muito ativa | Conversão e pipeline, não design |

## 11. Escolha por cenário

| Cenário | Primeira escolha | Alternativa | Evitar |
|---|---|---|---|
| Palestra técnica com código | Slidev | presenterm, se o tema for terminal | PPTist, Presenton |
| Evento ao vivo, HTML e offline | reveal.js | Shower | Slidev sem build testado |
| Aula ou relatório com PPTX | Marp | Quarto | Slidev para relatório mensal |
| Academia com dados e citação | Quarto | Beamer | Marp para equações complexas |
| Academia formal em LaTeX | Beamer com Focus ou Arguelles | Metropolis, com ressalva | Temas sem licença |
| PDF tipográfico em Typst | Touying | Polylux | Polylux para temas prontos |
| Terminal e SSH | presenterm | patat | slides para projeto novo |
| Pitch deck com IA | Presenton | PPTist para edição | Slidev para revisão com investidores |
| Vídeo e matemática animada | Remotion ou Manim CE | Motion Canvas só com fork | Slidev e Marp para vídeo |
| Diagramas técnicos | Excalidraw ou Mermaid | draw.io, D2 | tldraw sem licença comercial |

## 12. Combinações práticas

### 12.1. Slidev com Mermaid ou Excalidraw e Lucide

O Markdown guarda o conteúdo, o Slidev renderiza código e animação, o Mermaid cobre fluxos versionáveis, o Excalidraw cobre o diagrama autoral e o Lucide mantém os ícones coerentes. Um momento de anime.js ou GSAP resolve a abertura. Serve para palestra técnica com tempo de testar o build, não para relatório mensal.

### 12.2. Marp com tema CSS e Carbon

Um arquivo Markdown, um tema alinhado à marca e imagens de código resolvem a maior parte dos decks corporativos. O PDF sai previsível e o PPTX sai rasterizado, o que serve para apresentar, não para editar. Serve para aula e relatório recorrente, não para deck dependente de animação.

### 12.3. Quarto com reveal.js, código e citação

O mesmo documento executa Python, R ou Julia, gera gráficos, cita fontes e publica HTML, PDF ou PPTX. Mermaid e Graphviz entram nativamente. Serve para aulas, relatórios com dados e material que vira artigo, não para marketing, porque a instalação é pesada.

### 12.4. Typst com Touying, CeTZ ou Fletcher e pdfpc

Entrega o PDF mais bonito por linha de código entre as opções mantidas. O CeTZ e o Fletcher resolvem diagramas vetoriais, e o pdfpc resolve notas e timer. Serve para matemática, física e conferências, não para quem exige PPTX editável.

### 12.5. presenterm com VHS

Para palestra sobre CLI, infraestrutura ou terminal, o presenterm alterna entre slide e shell ao vivo. O VHS grava a demo com digitação controlada e evita depender da rede no palco. Faz sentido em evento técnico e apresentação por SSH; não faz sentido para plateia distante.

### 12.6. Presenton ou PPTAgent com PPTist

A pilha de IA começa com um rascunho no Presenton, que é auto-hospedável e exporta PPTX editável, ou no PPTAgent, mais adequado a fluxos agênticos. O PPTist entra para edição visual no navegador. Faz sentido para quem gera muitos decks e revisa manualmente; não faz sentido para palestra ao vivo.

## 13. Riscos

### 13.1. Projetos abandonados

O mdx-deck tem 11.500 estrelas e está sem commits desde 2021; o WebSlides tem 6.327 e parou em 2020; o remark tem 13.005 e não tem release desde 2020; o reveal-md tem 3.912 e está arquivado. Fusuma, nodeppt, Eagle.js e Bespoke estão arquivados ou parados. O Metropolis está congelado desde 2018 e o slides não publica release desde 2022. Esses projetos continuam instaláveis, mas não recebem correção quando o Node, o Python ou o navegador muda.

### 13.2. Licenças

O tldraw não é open source no sentido usual: o uso em produção exige chave, e sem chave o editor pode parar de renderizar após cinco segundos. Há trial de 100 dias, licença comercial e licença hobby ([licença](https://tldraw.dev/community/license)). O Remotion é gratuito para indivíduos, empresas com até três funcionários, sem fins lucrativos e avaliação; acima disso, exige licença comercial, e a licença pode mudar na versão 5.0. O PPTist é AGPL-3.0, com obrigação de abrir o código derivado de serviços na rede. Pandoc e patat são GPL-2.0, o que afeta a redistribuição do software, não o PDF gerado.

### 13.3. Concentração de mantenedor

O Marp CLI tem 96% dos commits de yhatt, o patat 92%, o presenterm 87%, o Remotion 86%, o reveal.js 84%, o Pandoc 82% e o Manim do 3b1b 79%. O Slidev tem 70% de antfu, o Touying 75% de OrangeX4 e o PPTist 62% de pipipi-pikachu. Isso não é defeito por si, mas férias, burnout ou mudança de emprego param o projeto.

### 13.4. Exportação PPTX

Nenhuma ferramenta aberta entrega PPTX perfeitamente editável em todos os casos. Slidev rasteriza cada slide no modo padrão; o modo editável deixa SVG, canvas, iframe, vídeo, fórmulas e filtros como imagem. Marp rasteriza por padrão; o modo editável é experimental, exige LibreOffice e não suporta notas. Quarto e Pandoc usam layouts predefinidos e estilo limitado. Touying tem PPTX experimental. Presenton promete PPTX editável, mas a fidelidade é afirmação do fornecedor. PPTist declara 85% na importação e 95% na exportação. Se o destinatário vai editar, teste antes e leve um PDF.

### 13.5. Acessibilidade, colaboração e fontes

O Shower é a opção mais atenta à acessibilidade, com teclado, foco visível e HTML semântico. O reveal.js tem issue aberta desde 2024 pedindo navegação por teclado, leitor de tela e contraste, e o PDF não tem metadados de idioma nem cabeçalhos, o que inviabiliza PDF/UA ([issue 3637](https://github.com/hakimel/reveal.js/issues/3637)). O Quarto tem issues de acessibilidade no menu de slides. Nenhuma ferramenta aberta oferece edição colaborativa em tempo real comparável a Google Slides; Excalidraw e tldraw colaboram, mas são quadros brancos. Fontes carregadas da web quebram offline ou atrás de proxy.

## 14. Roteiro de decisão em cinco passos

1. Defina a saída e o palco. Projeção ao vivo pede runtime e modo apresentador; envio pede PDF ou PPTX; vídeo pede motor de render, não framework de slides.
2. Meça as restrições. Verifique Node, LaTeX, Typst, Docker, internet no evento e prazo. Marp com PDF sobrevive a quase tudo; Slidev exige build e Playwright; Quarto exige CLI e, para PDF, TeX.
3. Escolha a família. Slidev para palestra técnica; Marp para simplicidade e PPTX; Quarto para academia com dados; Beamer para LaTeX; Touying para Typst; presenterm para terminal; reveal.js para HTML sob controle total; Remotion ou Manim para vídeo.
4. Escolha o visual. Um tema, duas fontes e um conjunto de ícones. Mermaid ou Excalidraw para diagramas, Carbon ou VHS para código e terminal, animação em poucos momentos.
5. Teste a exportação e ensaie. Gere PDF e PPTX no equipamento do evento, abra offline, confira fontes, vídeos, notas e modo apresentador. Congele versões e leve um PDF de emergência.

## 15. Fontes

### 15.1. Repositórios e documentação

- Slidev: https://github.com/slidevjs/slidev
- Exportação do Slidev: https://sli.dev/guide/exporting
- Showcases do Slidev: https://sli.dev/resources/showcases
- reveal.js: https://github.com/hakimel/reveal.js
- Marp: https://github.com/marp-team/marp
- Marp CLI: https://github.com/marp-team/marp-cli
- Quarto: https://quarto.org/docs/presentations/
- Spectacle: https://github.com/FormidableLabs/spectacle
- Shower: https://github.com/shower/shower
- presenterm: https://github.com/mfontanini/presenterm
- slides: https://github.com/maaslalani/slides
- patat: https://github.com/jaspervdj/patat
- Touying: https://github.com/touying-typ/touying
- Beamer no CTAN: https://ctan.org/pkg/beamer
- Metropolis: https://github.com/matze/mtheme
- Focus: https://github.com/pcafrica/focus-beamertheme
- Auriga: https://github.com/anishathalye/auriga
- Arguelles: https://github.com/piazzai/arguelles
- SimplePlus: https://github.com/pm25/SimplePlus-BeamerTheme
- Polylux: https://github.com/polylux-typ/polylux
- pdfpc: https://github.com/pdfpc/pdfpc
- Pandoc: https://github.com/jgm/pandoc
- PPTist: https://github.com/pipipi-pikachu/PPTist
- Presenton: https://github.com/presenton/presenton
- PPTAgent: https://github.com/icip-cas/PPTAgent
- Excalidraw: https://github.com/excalidraw/excalidraw
- tldraw: https://github.com/tldraw/tldraw
- Remotion: https://github.com/remotion-dev/remotion
- Manim Community: https://github.com/ManimCommunity/manim
- GSAP: https://github.com/greensock/GSAP
- Lucide: https://github.com/lucide-icons/lucide
- VHS: https://github.com/charmbracelet/vhs
- Licença do tldraw: https://tldraw.dev/community/license
- Mermaid: https://mermaid.js.org/intro/

### 15.2. Dados de uso e método

- API de repositórios do GitHub: https://docs.github.com/en/rest/repos/repos

### 15.3. Relatos, estudos e comparativos

- Discussão sobre Slidev no Hacker News: https://news.ycombinator.com/item?id=43816634
- Teaching with Quarto: https://mine-cetinkaya-rundel.github.io/teach-with-quarto/
- Estudo do Quarto na Swansea University: https://doi.org/10.1111/test.12409
