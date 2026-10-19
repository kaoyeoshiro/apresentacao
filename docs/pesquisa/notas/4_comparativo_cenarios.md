# Repositórios para apresentações: evidência comparativa e matriz por cenário

## 1. Escopo, método e data de coleta

Estas notas comparam ferramentas de apresentação com repositório público no GitHub, com foco em evidência de uso, maturidade, risco e critério de escolha, não em descrição de recursos. A data de referência é 19/10/2026.

Os números do GitHub foram coletados diretamente na API em 19/10/2026, às 13h24 UTC. Usei `GET /repos/{owner}/{repo}`, `GET /repos/{owner}/{repo}/releases`, `GET /repos/{owner}/{repo}/contributors`, `GET /repos/{owner}/{repo}/stats/participation` e a API GraphQL para separar issues de pull requests. Estrelas, forks, issues e releases são, portanto, valores observados, não estimativas.

Três ressalvas metodológicas valem para todas as tabelas. Primeiro, `open_issues_count` do endpoint REST soma issues e pull requests; nas tabelas abaixo os dois aparecem separados, obtidos por GraphQL. Segundo, a contagem de contribuidores é limitada a 100 pelo tamanho da página, então "100+" significa "pelo menos 100", e a fatia do principal contribuidor é calculada sobre esses 100, o que subestima levemente a concentração em projetos muito grandes. Terceiro, estrelas e forks medem atenção, não uso: forks são inflados por cópias de template e estrelas por divulgação.

Para adoção relativa usei downloads de pacotes como proxy, com janela de 19/09/2026 a 18/10/2026 (npm) e último mês fechado (PyPI). Downloads também não distinguem uso direto de instalação transitiva, então entram apenas como sinal secundário.

## 2. Métricas verificadas

### 2.1. Candidatos principais

| Projeto | Stars | Forks | Issues abertas (PRs) | Último release | Licença |
|---|---:|---:|---:|---|---|
| Slidev | 49.127 | 2.229 | 192 (45) | v53.0.0, 16/09/2026 | MIT |
| reveal.js | 72.441 | 17.023 | 810 (118) | 6.0.2, 10/09/2026 | MIT |
| Marp (CLI / repo de entrada) | 3.874 / 12.656 | 204 / 302 | 18 (2) | v4.5.1, 06/09/2026 | MIT |
| Quarto | 6.099 | 471 | 1.824 (81) | 1.10.19, 06/10/2026 | MIT |
| Pandoc | 46.629 | 6.984 | 961 (86) | 3.12.1, 08/10/2026 | GPL-2.0 |
| Beamer | 1.722 | 165 | 120 (0) | v3.78, 20/08/2026 | GPL-2.0+ ou LPPL-1.3c |
| Touying | 2.392 | 93 | 28 (5) | 0.8.0, 17/09/2026 | MIT |
| presenterm | 8.927 | 219 | 57 (27) | v0.16.1, 20/02/2026 | BSD-2-Clause |
| patat | 2.747 | 66 | 20 (3) | v0.15.2.0, 06/08/2025 | GPL-2.0 |
| PPTist | 9.409 | 1.772 | 18 (3) | nenhum release | AGPL-3.0 |
| Presenton | 11.212 | 1.707 | 19 (12) | v0.9.11-beta, 21/09/2026 | Apache-2.0 |
| Spectacle | 10.181 | 701 | 75 (8) | 10.2.3, 10/10/2025 | MIT |
| Excalidraw | 134.161 | 15.731 | 2.133 (1.206) | v0.18.1, 21/04/2026 | MIT |
| Remotion | 65.213 | 5.185 | 166 (25) | v4.0.536, 16/10/2026 | licença própria, ver 9.2 |
| Manim (Community) | 41.677 | 3.209 | 394 (105) | v0.22.0, 08/10/2026 | MIT |

O repositório `marp-team/marp` é apenas a porta de entrada do projeto; o desenvolvimento real está em `marp-cli` e `marp-core`. Por isso as duas contagens aparecem juntas. O mesmo vale para Beamer, cuja distribuição canônica é o TeX Live, não o GitHub: 1.722 estrelas subestimam bastante a base instalada.

### 2.2. Complementares, legado e casos específicos

| Projeto | Stars | Forks | Issues abertas (PRs) | Último release | Licença |
|---|---:|---:|---:|---|---|
| 3b1b/manim | 95.341 | 7.815 | 464 (41) | v1.7.2, 13/12/2024 | MIT |
| Mermaid | 90.748 | 9.363 | 1.499 (421) | 12.2.0, 13/10/2026 | MIT |
| tldraw | 50.984 | 3.573 | 443 (122) | v5.5.2, 02/10/2026 | licença própria, ver 9.2 |
| impress.js | 38.155 | 6.567 | 51 (10) | v2.0.0, 22/07/2022 | MIT |
| Motion Canvas | 19.391 | 848 | 151 (24) | v3.17.2, 14/12/2024 | MIT |
| remark | 13.005 | 861 | 172 (9) | v0.15.0, 18/01/2020 | MIT |
| mdx-deck | 11.500 | 594 | 95 (46) | nenhum release | MIT |
| slides (maaslalani) | 11.690 | 318 | 52 (27) | v0.9.0, 13/09/2022 | MIT |
| Metropolis (tema Beamer) | 6.906 | 859 | 84 (7) | v1.2, 23/01/2017 | "free license not otherwise listed" |
| WebSlides | 6.327 | 585 | 68 (14) | 1.5.0, 16/09/2017 | MIT |
| Shower | 4.876 | 853 | 40 (0) | nenhum release | MIT |
| Polylux | 1.609 | 70 | 83 (14) | v0.4.0, 27/01/2025 | MIT |

### 2.3. Adoção como proxy de download

| Pacote | Downloads no último mês | Janela |
|---|---:|---|
| Remotion (`remotion`) | 8.052.542 | 19/09 a 18/10/2026 |
| Remotion CLI (`@remotion/cli`) | 5.567.739 | idem |
| reveal.js | 571.757 | idem |
| Spectacle | 425.103 | idem |
| Slidev (`@slidev/cli`) | 393.213 | idem |
| Marp CLI | 235.700 | idem |
| Motion Canvas (`@motion-canvas/core`) | 22.648 | idem |
| mdx-deck | 2.649 | idem |
| Manim (PyPI) | 132.683 | último mês fechado |
| Quarto CLI (PyPI) | 61.331 | último mês fechado |

A distância entre estrelas e downloads conta uma história. Spectacle tem 10 mil estrelas e 425 mil downloads mensais, mas um único commit nas últimas 12 semanas. Remotion tem 8 milhões de downloads mensais porque é dependência de pipelines de vídeo, não porque todo esse volume produza apresentações. Já mdx-deck, com 11,5 mil estrelas, marca 2,6 mil downloads, o retrato de um projeto morto que continua instalado por dependências antigas.

## 3. Saúde do projeto e risco de manutenção

| Projeto | Releases 12m | Commits 12s | Contribuidores | Top-1 | Issues >18m | Issues sem comentário | Leitura |
|---|---:|---:|---:|---:|---:|---:|---|
| Slidev | 36 | 66 | 100+ | antfu, 70% | 87 de 192 | 76 | ativo, núcleo concentrado |
| reveal.js | 3 | 11 | 100+ | hakimel, 84% | 756 de 810 | 419 | maduro, backlog antigo |
| Marp CLI | 6 | 19 | 27 | yhatt, 96% | 12 de 18 | 0 | ativo, autor único |
| Quarto | 7 | 172 | 100+ | dragonstyle, 30% | 1.336 de 1.824 | 436 | muito ativo, backlog grande |
| Pandoc | 11 | 514 | 100+ | jgm, 82% | 855 de 961 | 155 | muito ativo, autor central |
| Beamer | 2 | 6 | 31 | josephwright, 41% | 117 de 120 | 21 | estável, baixo volume |
| Touying | 7 | 15 | 44 | OrangeX4, 75% | 5 de 28 | 7 | ativo, jovem |
| presenterm | 2 | 0 | 57 | mfontanini, 87% | 8 de 57 | 18 | desacelerou em 2026 |
| patat | 0 | 0 | 23 | jaspervdj, 92% | 13 de 20 | 5 | baixa atividade |
| PPTist | 0 | 8 | 14 | pipipi-pikachu, 62% | 9 de 18 | 12 | sem releases |
| Presenton | 43 | 483 | 22 | sauravniraula, 31% | 0 de 19 | 8 | ritmo altíssimo, v0.x |
| Spectacle | 0 | 1 | 100+ | kenwheeler, 27% | 69 de 75 | 31 | praticamente parado |
| Excalidraw | 1 | 78 | 100+ | dwelle, 24% | 1.441 de 2.133 | 717 | ativo, backlog enorme |
| Remotion | ≥100 | 4.702 | 100+ | JonnyBurger, 86% | 5 de 166 | 128 | muito ativo, autor central |
| Manim CE | 6 | 86 | 100+ | 3b1b, 40% | 319 de 394 | 111 | ativo |
| Motion Canvas | 0 | 0 | 96 | aarthificial, 67% | 129 de 151 | 55 | parado desde 2024 |
| remark | 0 | 0 | 75 | gnab, 77% | 168 de 172 | 50 | morto |
| mdx-deck | 0 | 0 | 59 | jxnblk, 72% | 95 de 95 | 37 | morto |
| WebSlides | 0 | 0 | 13 | Antonio-Laguna, 45% | 61 de 68 | 36 | morto |
| impress.js | 0 | 0 | 85 | bartaz, 50% | 49 de 51 | 6 | manutenção mínima |
| slides | 0 | 0 | 38 | maaslalani, 55% | 48 de 52 | 18 | dormente |
| Polylux | 0 | 0 | 17 | andreasKroepelin, 70% | 75 de 83 | 18 | dormente |
| Metropolis | 0 | 0 | 31 | matze, 53% | 82 de 84 | 28 | congelado desde 2017 |
| Shower | 0 | 13 | 32 | pepelsbey, 33% | 40 de 40 | 8 | ativo sem releases |

Quatro leituras saem dessa tabela. A primeira é que maturidade e manutenção não caminham juntas. reveal.js é o projeto mais antigo e mais forkado da lista, mas 93% das issues abertas têm mais de 18 meses e 52% nunca receberam comentário. A segunda é que projetos de autor único dominam a categoria: Marp CLI tem 96% dos commits de yhatt, patat 92%, presenterm 87%, Remotion 86%, reveal.js 84%, Pandoc 82%. Isso não é defeito por si, mas define o risco: férias, burnout ou mudança de emprego de uma pessoa param o projeto.

A terceira é a existência de dois regimes distintos de saúde. Projetos com triagem rápida (Touying com 5 de 28 issues antigas, PPTist com 9 de 18, Presenton com 0 de 19, tldraw com 4 de 443) resolvem ou fecham o que não vão fazer. Projetos com backlog histórico (reveal.js, Pandoc, Quarto, Excalidraw, Mermaid) acumulam issues como registro público, sem que isso signifique abandono.

A quarta é o sinal de parada. Motion Canvas não tem release desde dezembro de 2024 e nenhum commit nas últimas 12 semanas, com 151 issues abertas. slides não lança versão desde 2022. Polylux está parado e o próprio README avisa que não há garantia de compatibilidade futura. Metropolis está congelado em 2017. Esses quatro entram na conversa apenas com ressalva explícita.

## 4. Evidência de uso real

### 4.1. Slidev

A página oficial de showcases lista palestras em KubeCon China (2024 e 2025), FOSSASIA Summit 2024, LASCON 2024 (HD Moore), Vue.js Nation 2023 e JSConf Korea 2022, além de cursos e meetups ([sli.dev](https://sli.dev/resources/showcases)). É a evidência mais forte de uso em conferência técnica entre os candidatos, ainda que a lista seja curada pelo próprio projeto e não auditada.

Fora do circuito de divulgação, o blog da Datum descreve em junho de 2026 o uso de Slidev em produção para decks comerciais, de conselho e de comunidade, com tema próprio, conteúdo compartilhado por symlink e geração automatizada de slides a partir de dados internos ([Datum](https://www.datum.net/blog/automagic-presentations-with-claude)). É um relato corporativo verificável, não um depoimento anônimo.

O projeto apareceu no Hacker News em abril de 2025 com 273 pontos e 91 comentários ([HN 43816634](https://news.ycombinator.com/item?id=43816634)). Nos comentários, a crítica recorrente é o controle de layout: quem vem de PowerPoint sente falta de posicionamento pixel a pixel.

### 4.2. reveal.js

A thread de 2020 no Hacker News, com o criador presente, reúne relatos de uso em aulas na Bournemouth University, em apresentações internas na Microsoft, em talks da RubyConf e em dezenas de palestras desde 2013 ([HN 25233136](https://news.ycombinator.com/item?id=25233136)). Um dos relatos descreve o uso em concertos e instalações, o que mostra a elasticidade do formato HTML.

O modelo de sustentação é explícito: o criador mantém o reveal.js aberto e financia o desenvolvimento com o editor proprietário Slides.com ([HN 25235766](https://news.ycombinator.com/item?id=25235766)). Isso reduz o risco de abandono, mas cria dependência de um único mantenedor e de um produto comercial.

Com 17.023 forks, é o projeto mais replicado da categoria. A maior parte desses forks, porém, é cópia de deck ou de template, não contribuição.

### 4.3. Marp

Não encontrei showcase oficial com nome de empresa ou evento. A evidência disponível é indireta e consistente: 235.700 downloads mensais do CLI, extensão de VS Code mantida pela mesma equipe e relatos no Hacker News de uso em aulas e apresentações rápidas ([HN 43303752](https://news.ycombinator.com/item?id=43303752), [HN 45842777](https://news.ycombinator.com/item?id=45842777)). Um instrutor descreve ter abandonado presenterm e adotado Marp por controle de tamanho de fonte e previsibilidade.

O ponto fraco é a ausência de casos públicos de grande porte. Marp parece forte em adoção difusa, fraca em vitrine.

### 4.4. Quarto

A adoção acadêmica é documentada por fontes primárias. O site "Teaching (with) Quarto" reúne materiais da sessão da JSM 2023 e cursos em Duke, com slides e repositórios públicos ([teach-with-quarto](https://mine-cetinkaya-rundel.github.io/teach-with-quarto/)). Um artigo de 2025 na *Teaching Statistics* relata uso em laboratório de estatística na Swansea University, com pesquisa com 13 alunos: todos concordaram que o site é fácil de navegar e bem apresentado, e 11 de 13 consideraram a busca útil ([doi 10.1111/test.12409](https://doi.org/10.1111/test.12409)).

O patrocinador é a Posit, e o Quarto é o sucessor declarado do R Markdown. Isso dá previsibilidade de manutenção que nenhum projeto de autor único oferece, ao custo de um backlog de 1.824 issues e de uma superfície de configuração grande.

### 4.5. Beamer, Touying e o circuito acadêmico

Beamer não precisa de vitrine: está no TeX Live e no MiKTeX, é padrão de fato em várias áreas e tem 11 releases registrados no GitHub, dois nos últimos 12 meses ([CTAN](https://ctan.org/pkg/beamer)). O repositório GitHub é um espelho de desenvolvimento, não a via de distribuição.

Touying foi promovido a pacote em destaque no Typst Universe em setembro de 2024, e a discussão no fórum do Typst recomenda Touying sobre Polylux por manutenção e sintaxe ([Typst Forum](https://forum.typst.app/t/touying-vs-polylux/1703), [anúncio](https://forum.typst.app/t/new-featured-packages-on-universe/524)). No Reddit, a recomendação se repete em novembro de 2025 ([r/typst](https://www.reddit.com/r/typst/comments/1oubl2y/need_slides_libraries_suggestions/)). É adoção de comunidade, não corporativa.

Polylux foi o precursor e aparece nas mesmas recomendações, mas o repositório está sem commits desde fevereiro de 2026 e sem release desde janeiro de 2025.

Metropolis tem 6.906 estrelas e é o tema Beamer mais reconhecido, mas a última versão no CTAN é de 23/01/2017 e o último commit é de agosto de 2018 ([CTAN](https://ctan.org/pkg/beamertheme-metropolis)). Continua funcionando e continua sendo baixado, o que é exatamente o perfil de dependência congelada.

### 4.6. Terminal: presenterm, patat e slides

presenterm chegou ao topo do Hacker News em março de 2025 com 306 pontos e 45 comentários ([HN 43303752](https://news.ycombinator.com/item?id=43303752)). O autor mantém uma lista de oito talks que usaram a ferramenta, incluindo palestras de Orhun Parmaksız sobre Ratatui ([README](https://github.com/mfontanini/presenterm)). Há relato de uso em apresentação de trabalho com transição direta para o Vim, que é o caso de uso que justifica a categoria.

patat aparece na mesma thread como ferramenta de longa data, com a vantagem de executar snippets durante a palestra. slides, de maaslalani, tem 11,7 mil estrelas mas nenhum release desde setembro de 2022 e nenhum commit nas últimas 12 semanas.

### 4.7. PPTist e Presenton

PPTist tem 1.772 forks e é usado como base para editores de slides web, segundo a própria documentação. Não encontrei caso público independente de empresa ou evento. O README é incomum por ser honesto: diz que o projeto não é uma ferramenta pronta, que a importação de PPTX tem fidelidade de cerca de 85% e a exportação cerca de 95%, e que perda de detalhes é inevitável ([README](https://github.com/pipipi-pikachu/PPTist)).

Presenton tem 11,2 mil estrelas em cerca de 17 meses de vida, 43 releases em 12 meses e versão corrente 0.9.11-beta. O README promete exportação PPTX totalmente editável e execução local com modelos próprios ([README](https://github.com/presenton/presenton)). O volume de estrelas em pouco tempo é sinal de divulgação, não de maturidade: não há release 1.0, e o ritmo de 43 versões por ano indica instabilidade de API.

### 4.8. Excalidraw, Mermaid, Remotion e Manim

Excalidraw e Mermaid não são ferramentas de apresentação, são fornecedores de diagramas. Excalidraw tem 134 mil estrelas e exporta PNG e SVG com facilidade; Mermaid tem 90,7 mil e é renderizado nativamente por ferramentas como Slidev, Quarto e GitHub. Nos dois casos, o uso em apresentação é como componente, não como runtime.

Remotion tem 8 milhões de downloads mensais e 4.702 commits nas últimas 12 semanas, o maior volume da lista. É infraestrutura de vídeo programático, usada em pipelines, não um concorrente de Slidev.

Manim tem 41,7 mil estrelas na versão da comunidade e 132 mil downloads mensais no PyPI. A versão 3b1b/manim, com 95,3 mil estrelas, é o motor dos vídeos do canal 3Blue1Brown. Nenhuma das duas é ferramenta de slide; são motores de animação explicativa.

## 5. Limitações relatadas por usuários

### 5.1. Exportação

Slidev exporta PPTX com cada slide como imagem, portanto sem texto selecionável; o próprio guia oficial diz isso ([docs](https://github.com/slidevjs/docs/blob/main/guide/exporting.md)). PDF, PPTX e PNG dependem de Playwright com Chromium instalado, o que adiciona peso e um ponto de falha em CI.

reveal.js não tem exportação PPTX. O PDF sai pela impressão do navegador em `?print-pdf`, e a discussão de acessibilidade do projeto documenta que esses PDFs não têm metadados de idioma nem estrutura de cabeçalhos, o que os torna incompatíveis com PDF/UA ([Discussion 3733](https://github.com/hakimel/reveal.js/discussions/3733)). Um usuário relata ter migrado para Quarto com reveal.js e continuado com PDFs inacessíveis.

Marp é o inverso: `--pdf` e `--pptx` em um comando, com renderização previsível, segundo teste independente de setembro de 2026 ([lecture.studio](https://lecture.studio/blog/marp-vs-slidev-vs-revealjs/)). A limitação está no outro lado, pouca animação e pouco controle fino de layout.

Quarto herda a exportação do reveal.js quando usa esse formato. Uma issue de janeiro de 2026 mostra imagens grandes desaparecendo em viewport móvel por causa do cálculo de `r-stretch` ([Quarto #13943](https://github.com/quarto-dev/quarto-cli/issues/13943)).

PPTist declara perda de fidelidade na importação e exportação de PPTX. Slidev e Presenton prometem PPTX, mas com naturezas diferentes: Slidev achata em imagens, Presenton promete editável e depende do modelo de IA para gerar conteúdo.

### 5.2. Acessibilidade

reveal.js tem uma issue aberta desde junho de 2024 pedindo navegação por teclado, suporte a leitor de tela e controle de contraste ([#3637](https://github.com/hakimel/reveal.js/issues/3637)). Em fevereiro de 2025, um usuário descreveu que a navegação funciona razoavelmente com NVDA e JAWS, com falhas em alt text e títulos de iframe, o que mostra que o problema é parcial e dependente de configuração.

Quarto acumula issues de acessibilidade no menu de slides que ele empacota, incluindo violação de nome acessível em axe-core e menu navegável por leitor de tela quando está fechado ([#14249](https://github.com/quarto-dev/quarto-cli/issues/14249)). A resposta do mantenedor foi rápida, o que é um bom sinal.

Marp e presenterm têm menos relatos de acessibilidade, em parte porque geram documentos mais simples: Marp produz PDF com texto selecionável (não verifiquei conformidade com PDF/UA), e presenterm produz terminal, acessível pelo leitor de tela do próprio terminal, não pelo navegador.

### 5.3. Layout, mobile e fontes

A queixa mais repetida em todas as ferramentas markdown é a falta de controle fino de layout. No Hacker News, um professor descreve que Slidev e similares não dão posicionamento pixel a pixel como PowerPoint ([HN 43816634](https://news.ycombinator.com/item?id=43816634)). Em presenterm, um palestrante de KubeCon relata ter desistido depois de duas horas tentando acertar colunas e alinhamento ([HN 43303752](https://news.ycombinator.com/item?id=43303752)). O autor respondeu pedindo o arquivo, o que indica que parte disso é falta de documentação, não limitação técnica.

Fontes são um risco silencioso. Temas que carregam fontes da web quebram em ambiente offline ou atrás de proxy; Slidev, Marp e reveal.js dependem de CSS e, em alguns temas, de Google Fonts. presenterm depende de fontes instaladas no terminal e de suporte a imagens em kitty, iTerm2, WezTerm, Ghostty ou foot.

### 5.4. Colaboração

Nenhuma das ferramentas de código aberto da lista oferece edição colaborativa em tempo real comparável a Google Slides. Slidev tem servidor de desenvolvimento e hot reload, não multiplayer. Excalidraw e tldraw têm colaboração, mas são quadros brancos, não fluxos de slide. Para um time em que várias pessoas editam o mesmo deck, o custo de coordenação em Git é real.

## 6. Curva de aprendizado e custo de manutenção

As estimativas abaixo são julgamento a partir da documentação e dos relatos citados, não medições. Servem para ordenar esforço, não para prometer horas exatas.

| Ferramenta | Tempo até o primeiro deck | Custo recorrente | Principal fonte de custo |
|---|---|---|---|
| Marp | 30 min | baixo | CSS para fugir do padrão |
| patat | 30 min | baixo | sintaxe Haskell-like do Pandoc |
| presenterm | 1 h | baixo | layout e fontes do terminal |
| reveal.js | 1 a 2 h | baixo | HTML, CSS e plugins |
| Slidev | 1 a 3 h | médio | projeto Node, Vue para customizar |
| Quarto | 2 a 4 h | médio | YAML, R ou Python, LaTeX para PDF |
| Touying | 2 a 4 h | médio | Typst e API de animação |
| PPTist | imediato na UI | médio | Vue para estender, AGPL |
| Presenton | minutos para rascunho | médio a alto | Docker, chaves de API, correção manual |
| Spectacle | 2 a 4 h | baixo | React e JSX |
| Beamer | 1 a 2 dias | baixo | LaTeX e overlays |
| Remotion | 2 a 5 dias | alto | React, Chromium, FFmpeg, licença |
| Manim | 2 a 5 dias | alto | Python e geometria de cena |

Manutenção de deck é o critério que menos aparece nas comparações e o que mais pesa no ano seguinte. Marp e reveal.js vendored são os mais baratos: um arquivo markdown ou uma pasta de HTML que abre em qualquer navegador. Slidev exige que o `node_modules` ou o lockfile sobreviva a três anos de atualizações; o guia de exportação depende de Playwright, que muda com frequência. Quarto exige a versão do CLI e, para PDF, uma instalação TeX. PPTist e Presenton exigem um serviço rodando, o que muda o problema de "arquivo" para "operação".

## 7. Matriz de decisão

Notas de 1 a 5 são julgamento fundamentado nas seções anteriores, não métricas da API. "Atividade" resume releases e commits das últimas 12 semanas. "Licença" mede liberdade de uso comercial, não preferência ideológica.

| Projeto | Visual | Facilidade | Exportação | Animação | Ecossistema | Atividade | Licença | Melhor uso |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Slidev | 5 | 3 | 4 | 5 | 5 | 5 | 5 | Palestra técnica, demo de código |
| reveal.js | 4 | 3 | 3 | 4 | 5 | 4 | 5 | Deck web customizado, evento ao vivo |
| Marp | 3 | 5 | 5 | 2 | 4 | 4 | 5 | Aula, relatório, PDF/PPTX rápido |
| Quarto | 4 | 3 | 4 | 3 | 5 | 5 | 5 | Academia, dados e código executável |
| Pandoc | 2 | 2 | 5 | 1 | 5 | 5 | 4 | Conversão, pipeline, Beamer via markdown |
| Beamer | 4 | 2 | 5 | 3 | 5 | 4 | 5 | Academia formal, matemática densa |
| Touying | 5 | 3 | 4 | 4 | 3 | 4 | 5 | Academia em Typst, visual tipográfico |
| presenterm | 3 | 4 | 4 | 4 | 3 | 3 | 5 | Terminal, SSH, live demo |
| patat | 2 | 4 | 2 | 2 | 2 | 2 | 4 | Terminal minimalista |
| PPTist | 4 | 4 | 4 | 2 | 2 | 3 | 2 | Editor PPTX web, produto interno |
| Presenton | 4 | 5 | 4 | 2 | 3 | 5 | 5 | Rascunho de pitch deck com IA |
| Spectacle | 4 | 3 | 3 | 4 | 3 | 2 | 5 | Time React, deck como componente |
| Excalidraw | 4 | 4 | 4 | 1 | 4 | 4 | 5 | Diagramas e quadros, não slides |
| Remotion | 5 | 2 | 5 | 5 | 4 | 5 | 2 | Vídeo programático, motion graphics |
| Manim | 5 | 2 | 4 | 5 | 3 | 5 | 5 | Animação matemática explicativa |

Duas notas exigem explicação. A licença do Remotion recebe 2 porque o uso é gratuito apenas para indivíduos, empresas de até três funcionários e organizações sem fins lucrativos; acima disso, é preciso comprar licença ([LICENSE](https://github.com/remotion-dev/remotion/blob/main/LICENSE.md)). A do PPTist recebe 2 porque é AGPL-3.0, o que obriga a abrir o código de serviços derivados que rodem na rede, um problema real para quem quer embutir o editor num produto.

## 8. Ranking por cenário

### 8.1. Palestra técnica ou conferência

1. **Slidev.** Melhor combinação de código, animação e aparência para talks de engenharia, com showcases verificáveis em KubeCon, FOSSASIA e LASCON. O custo é o projeto Node e a exportação via Playwright.
2. **reveal.js.** Mais controle sobre HTML e plugins, melhor para quem quer embedar demo interativo ou iframe. O custo é o backlog e a acessibilidade do PDF.
3. **presenterm.** Se a palestra é sobre terminal, infraestrutura ou CLI, a transição entre slide e shell ao vivo é imbatível.

Evitar: PPTist e Presenton. São geradores ou editores, não runtimes de palestra ao vivo. Spectacle só se o time já for React e o deck for parte do produto.

### 8.2. Pitch deck de startup

1. **Presenton**, como rascunho rápido a partir de um prompt, com a ressalva de que a saída exige revisão manual e o produto está em 0.x.
2. **PPTist**, se o objetivo é editar e exportar PPTX dentro de uma ferramenta web própria.
3. **Marp**, se o pitch é para uma audiência técnica e o conteúdo muda toda semana.

Evitar: Slidev e reveal.js para investidores. O visual é bom, mas o ciclo de ajuste fino de uma página por rodada de feedback é caro, e o arquivo final não é o PPTX que o sócio ou o banco espera. Na prática, PowerPoint, Keynote ou Google Slides continuam vencendo esse cenário; entre os repositórios, nenhum resolve a colaboração e a revisão visual que um pitch exige.

### 8.3. Aula e academia

1. **Quarto.** Integra código executável, citação, PDF e site de curso, com adoção documentada em Duke e Swansea. É a escolha de menor risco institucional.
2. **Beamer.** Se o curso já vive em LaTeX, nada substitui a estabilidade e o PDF final. Metropolis continua bonito, mas está congelado desde 2017.
3. **Touying.** Para quem já usa Typst, entrega visual melhor que Beamer com compilação em milissegundos e temas prontos.

Evitar: Marp para material que depende de equações e referências cruzadas complexas; ele dá conta, mas o fluxo acadêmico fica melhor no Quarto ou no Beamer. Polylux, pelo estado dormente.

### 8.4. Relatório corporativo

1. **Marp.** Um arquivo markdown, PDF e PPTX em um comando, sem projeto Node. É o melhor custo-benefício para relatórios recorrentes.
2. **Quarto.** Quando o relatório tem dados, gráficos e código reprodutível.
3. **PPTist.** Quando o destino final é um PPTX editável por outras áreas.

Evitar: Slidev para relatório mensal. O custo de manter um projeto por deck não se paga quando o conteúdo é tabular e repetitivo.

### 8.5. Evento ao vivo

1. **reveal.js.** É o mais previsível em palco: HTML estático, funciona offline, permite embedar demo, iframe e vídeo, e tem modo apresentador.
2. **Slidev.** Melhor para live coding com destaque de linhas e componentes, desde que o notebook esteja com o ambiente buildado e testado.
3. **presenterm.** Para talks de terminal, com a ressalva de que o layout exige ensaio.

Evitar: Presenton, que depende de geração por IA e não foi feito para operar ao vivo. Qualquer ferramenta cujo export dependa de rede no momento da palestra.

### 8.6. Vídeo e animação

1. **Remotion.** Melhor para vídeo programático em React, com render em lote e integração a pipeline. Cuidado com a licença acima de três funcionários.
2. **Manim.** Melhor para animação matemática e explicativa, com a comunidade mais ativa que o fork do 3b1b.
3. **Motion Canvas.** Boa IDE e bom resultado, mas parado desde dezembro de 2024; usar só com fork próprio.

Evitar: Slidev e Marp para vídeo. Nenhum dos dois foi desenhado para render frame a frame com áudio.

### 8.7. Apresentação offline ou sem internet

1. **Marp com PDF.** O PDF é o formato mais portátil que existe; o HTML exportado só depende de fontes externas se o tema as carregar.
2. **reveal.js com a pasta do framework vendorizada.** Abre de qualquer navegador, sem servidor.
3. **presenterm.** Um binário e um arquivo markdown, sem rede.

Evitar: Slidev sem build prévio. O deck depende de `node_modules` e de um servidor de desenvolvimento; o build estático existe, mas exige teste antecipado. Evitar também temas que baixam fontes do Google.

### 8.8. Terminal e SSH

1. **presenterm.** O mais completo: imagens, colunas, Mermaid, LaTeX, notas e export para PDF e HTML, com 8,9 mil estrelas e uso documentado em talks.
2. **patat.** Mais antigo e mais simples, com execução de snippets, mas GPL-2.0 e atividade baixa.
3. **slides.** Só se o apelo for o binário Go e a simplicidade; o projeto está dormente desde 2022 em termos de release.

Evitar: qualquer ferramenta que exija navegador. Em SSH puro, a única saída real é terminal.

## 9. Riscos e armadilhas

### 9.1. Projetos abandonados ou congelados

remark não tem release desde janeiro de 2020 e nenhum commit desde 2023. mdx-deck não tem release e está sem commits desde 2021. WebSlides parou em 2020, com último release em 2017. Metropolis está congelado em 2017. Motion Canvas parou em dezembro de 2024. slides não lança versão desde 2022. Polylux não tem commit desde fevereiro de 2026 e avisa no README que não garante compatibilidade.

Esses projetos continuam instaláveis e muitos continuam funcionando. O problema imediato não é o software deixar de rodar, e sim a ausência de correção de segurança, de suporte a navegador novo e de resposta quando o Node ou o Python da máquina mudar.

### 9.2. Licenças que mudam o cálculo

tldraw não é open source no sentido usual: a licença proíbe uso em produção sem chave e acordo comercial, inclui verificação técnica de licença e coleta de dados de uso ([LICENSE](https://github.com/tldraw/tldraw/blob/main/LICENSE.md)). É excelente para protótipo e para desenvolvimento, impróprio para colocar num produto sem contrato.

Remotion é gratuito para indivíduos, empresas de até três funcionários e organizações sem fins lucrativos; acima disso exige licença comercial ([LICENSE](https://github.com/remotion-dev/remotion/blob/main/LICENSE.md)). O código é aberto, mas a licença não é OSI.

PPTist é AGPL-3.0. Usar como base de um serviço web interno já levanta obrigação de disponibilizar o código derivado a quem interage pela rede; para produto comercial, é preciso avaliar com jurídico.

Pandoc e patat são GPL-2.0. Isso não afeta o PDF ou o deck gerado, mas afeta a redistribuição do software junto com um produto.

Beamer é dual GPL-2.0+ ou LPPL-1.3c, o que na prática é permissivo para uso acadêmico.

### 9.3. Dependências pesadas

Slidev carrega um projeto Vite/Vue e, para exportar, Playwright com Chromium. Quarto carrega Pandoc, Deno e, para PDF, uma distribuição TeX. Remotion carrega Chromium e FFmpeg. Presenton carrega Docker, modelo de linguagem e chaves de API. PPTist carrega Node 20 ou superior e um build Vue.

O custo aparece em três lugares: tempo de instalação em máquina nova, tamanho da imagem de CI e fragilidade de versão em dois ou três anos. Marp e reveal.js vendorizado são os únicos que praticamente não têm esse problema.

### 9.4. Dependência de uma pessoa

Marp CLI (96% de yhatt), patat (92%), presenterm (87%), Remotion (86%), reveal.js (84%), Pandoc (82%) e 3b1b/manim (79%) são projetos de autor central. Convém manter um plano B, mesmo sem descartá-los. O caso do reveal.js é o mais confortável, porque o autor tem receita do Slides.com e mantém o projeto há 15 anos. O caso do Metropolis mostra o que acontece quando o autor para.

### 9.5. Armadilhas de avaliação

Estrelas não medem uso. Spectacle tem 10 mil estrelas e um commit em 12 semanas; mdx-deck tem 11,5 mil e está morto. Presenton tem 11,2 mil em 17 meses, número compatível com divulgação.

Forks não medem contribuição. reveal.js tem 17 mil forks, quase todos cópias de deck.

Backlog não mede abandono. Quarto tem 1.824 issues abertas e 172 commits em 12 semanas; Excalidraw tem 2.133 e 78 commits. O que mede abandono é a combinação de zero commits, zero releases e issues antigas sem triagem.

Showcase não mede adequação. A lista do Slidev é curada pelo projeto e favorece talks de tecnologia. Não encontrei vitrine equivalente para Marp ou Quarto, o que não significa ausência de uso.

## 10. Recomendação final

**Melhor geral: Slidev.** É a melhor combinação de visual, animação, código e comunidade para o caso mais comum, que é palestra técnica. A ressalva é operacional: trate o deck como projeto Node, fixe versões e teste a exportação antes do evento.

**Melhor para impacto visual: Slidev**, com **Touying** como alternativa para quem quer qualidade tipográfica de impressão e não se importa de aprender Typst. Touying produz o resultado mais bonito por linha de código, mas o ecossistema é jovem e a exportação PPTX é experimental.

**Melhor para simplicidade: Marp.** Um arquivo markdown, um comando, PDF e PPTX. É a escolha certa quando o deck precisa existir e o tempo é curto, e a que sobrevive melhor a uma troca de máquina sem reinstalar um projeto.

**Melhor para academia: Quarto**, com Beamer como escolha para quem já vive em LaTeX e Touying para quem já vive em Typst. Quarto ganha por integrar análise, citação e PDF no mesmo fluxo, não por ser mais bonito.

**Melhor para terminal: presenterm.** É o mais completo da categoria, com imagens, colunas, notas, Mermaid, LaTeX e export, e tem uso documentado em talks reais.

**Para pitch deck e relatório corporativo**, a resposta honesta é que nenhum repositório desta lista supera PowerPoint, Keynote ou Google Slides em colaboração e revisão. Entre os candidatos, Presenton serve para rascunho e PPTist para edição web; Marp serve para o relatório técnico recorrente.

**Para vídeo**, Remotion se o time é React e a licença se encaixa; Manim se o conteúdo é matemática. Motion Canvas só com fork, dado o estado parado.

## 11. Lacunas e o que não foi confirmado

Não encontrei dados públicos de "quem usa" por empresa além dos showcases oficiais e de relatos isolados. As listas de showcase são curadas pelos próprios projetos e não passam por auditoria independente.

Não há série histórica pública de tempo de resposta a issues. Usei idade e ausência de comentário como proxy, mas uma issue antiga sem comentário pode ter sido triada por outro canal, como Discord.

Não consegui medir uso corporativo real de PPTist e Presenton. O volume de estrelas e o ritmo de releases são compatíveis com adoção, mas não provam implantação em produção.

Não verifiquei preços atuais de licença comercial do tldraw nem do Remotion além do que está nos arquivos de licença. Para decisão de compra, é preciso consultar a página comercial.

Não testei as ferramentas em primeira mão. As limitações relatadas vêm de issues, discussões e relatos de usuários, com a fonte indicada em cada caso; onde não há fonte, a afirmação foi marcada como julgamento.

Os tempos de aprendizado da seção 6 são estimativas ordinais, não medições. Servem para comparar esforço relativo, não para dimensionar prazo.

As contagens de contribuidores estão limitadas a 100 por página da API. Projetos marcados como "100+" têm pelo menos 100 contribuidores, possivelmente muitos mais.
