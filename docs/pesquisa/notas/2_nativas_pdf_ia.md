# Repositórios para apresentações: terminal, PDF/Typst/LaTeX e geração por IA

## 0. Método e síntese

### 0.1. Coleta

Os números foram coletados em 19/10/2026, entre 13h20 e 13h45 UTC, com a API do GitHub autenticada. Estrelas, forks, issues e licença vêm do endpoint `repos/{owner}/{repo}`; o último commit vem de `commits?per_page=1` no branch padrão; o release vem de `releases/latest`. A contagem de issues é `open_issues_count`, que soma issues e pull requests abertos. Tudo é um retrato do momento e envelhece rápido.

Para os projetos sem release, a API retorna 404 e a nota registra "nenhum". No Metropolis, a API não identifica um SPDX; a licença vem do README. Em RISE, xaringan e Quarto, a API retorna NOASSERTION; a nota usa o arquivo LICENSE e o DESCRIPTION. Os links de site e de demonstração foram verificados por requisição HTTP em 19/10/2026. O link de galeria de temas do Touying presente no README retorna 404 e não é usado como referência.

### 0.2. Síntese

Para terminal, o presenterm é a opção com mais recursos verificáveis (imagens, Mermaid, fórmulas, PDF/HTML e notas), enquanto o slides tem mais estrelas e a instalação mais simples, mas não publica release desde 2022. O patat é a escolha de quem já vive em Pandoc e quer notas em segunda janela; o lookatme está parado desde 2023.

Em PDF moderno, o Typst oferece o melhor equilíbrio entre velocidade e tipografia. O Touying traz temas e animações prontos; o Polylux é mais minimalista e depende de templates. PPTX nativo ainda é experimental nos dois.

O Beamer continua imbatível em matemática e TikZ, mas o Metropolis está congelado desde 2018; Focus, Auriga, Arguelles e SimplePlus são alternativas mantidas. Pandoc e Quarto são *pipelines*, não sistemas de design.

Entre os geradores com IA, o Presenton tem a tração mais clara e exporta PPTX editável; o PPTAgent é pesquisa aplicada, com resultado dependente de referência e modelo; o allweonedev é um clone de Gamma com stack pesada. O RISE clássico está extinto; o jupyterlab-rise é o sucessor.

O teto visual varia muito. Terminal limita a texto e imagens protocolares; Typst e Beamer têm teto alto; PPTX gerado por IA ainda pede revisão humana. As avaliações desta nota olham documentação, GIFs e PDFs de demonstração, não testes de renderização.

### 0.3. Como ler as avaliações

As notas de qualidade visual são julgamentos baseados em GIFs, PDFs de demonstração e documentação, não em testes de renderização. Onde o recurso é uma afirmação do fornecedor, o texto diz isso. Não instalei, não compilei e não cronometrei nenhum projeto. A ausência de um recurso na documentação é registrada como "não documentado", não como ausência comprovada.

## 1. Métricas verificadas

Tabela 1. Métricas da API do GitHub em 19/10/2026, 13h20 a 13h45 UTC.

| Projeto | Repositório | Site | Estrelas | Forks | Issues | Último commit | Último release | Licença |
|---|---|---:|---:|---:|---:|---|---|---|
| presenterm | [mfontanini/presenterm](https://github.com/mfontanini/presenterm) | [docs](https://mfontanini.github.io/presenterm/) | 8.927 | 219 | 84 | 22/05/2026 | v0.16.1 (20/02/2026) | BSD-2-Clause |
| slides | [maaslalani/slides](https://github.com/maaslalani/slides) | [site](http://maaslalani.com/slides/) | 11.690 | 318 | 79 | 08/07/2026 | v0.9.0 (13/09/2022) | MIT |
| patat | [jaspervdj/patat](https://github.com/jaspervdj/patat) | [Hackage](https://hackage.haskell.org/package/patat) | 2.747 | 66 | 23 | 25/06/2026 | v0.15.2.0 (06/08/2025) | GPL-2.0 |
| lookatme | [d0c-s4vage/lookatme](https://github.com/d0c-s4vage/lookatme) | [docs](https://lookatme.readthedocs.io/en/latest/) | 2.333 | 66 | 38 | 24/01/2023 | v2.5.0 (27/10/2022); PyPI 2.5.5 | MIT |
| Touying | [touying-typ/touying](https://github.com/touying-typ/touying) | [docs](https://touying-typ.github.io/) | 2.392 | 93 | 33 | 28/09/2026 | 0.8.0 (17/09/2026) | MIT |
| Polylux | [polylux-typ/polylux](https://github.com/polylux-typ/polylux) | [book](https://polylux.dev/book) | 1.609 | 70 | 97 | 28/02/2026 | v0.4.0 (27/01/2025) | MIT |
| Metropolis | [matze/mtheme](https://github.com/matze/mtheme) | [CTAN](https://ctan.org/pkg/beamertheme-metropolis) | 6.907 | 859 | 91 | 01/08/2018 | v1.2 (23/01/2017) | CC-BY-SA 4.0 (README) |
| Pandoc | [jgm/pandoc](https://github.com/jgm/pandoc) | [site](https://pandoc.org) | 46.629 | 6.986 | 1.047 | 19/10/2026 | 3.12.1 (08/10/2026) | GPL-2.0 |
| Quarto | [quarto-dev/quarto-cli](https://github.com/quarto-dev/quarto-cli) | [site](https://quarto.org) | 6.099 | 471 | 1.907 | 19/10/2026 | v1.10.19 (06/10/2026) | MIT |
| Marp CLI | [marp-team/marp-cli](https://github.com/marp-team/marp-cli) | [marp.app](https://marp.app/) | 3.874 | 204 | 20 | 08/09/2026 | v4.5.1 (06/09/2026) | MIT |
| xaringan | [yihui/xaringan](https://github.com/yihui/xaringan) | [demo](https://slides.yihui.org/xaringan/) | 1.523 | 273 | 45 | 18/08/2025 | v0.31 (18/08/2025) | MIT (DESCRIPTION) |
| PPTist | [pipipi-pikachu/PPTist](https://github.com/pipipi-pikachu/PPTist) | [demo](https://pipipi-pikachu.github.io/PPTist/) | 9.409 | 1.772 | 21 | 10/10/2026 | nenhum | AGPL-3.0 |
| Presenton | [presenton/presenton](https://github.com/presenton/presenton) | [site](https://presenton.ai) | 11.212 | 1.707 | 31 | 19/10/2026 | v0.9.11-beta (21/09/2026) | Apache-2.0 |
| PPTAgent | [icip-cas/PPTAgent](https://github.com/icip-cas/PPTAgent) | [arXiv](https://arxiv.org/abs/2501.03936) | 5.130 | 600 | 18 | 20/09/2026 | v2.0.0 (16/12/2025) | MIT |
| presentation-ai | [allweonedev/presentation-ai](https://github.com/allweonedev/presentation-ai) | [demo](https://presentation.allweone.com) | 3.050 | 529 | 0 | 05/06/2026 | nenhum | MIT |
| RISE | [damianavila/RISE](https://github.com/damianavila/RISE) | [docs](https://rise.readthedocs.io) | 3.736 | 408 | 162 | 29/10/2023 | nenhum estável (tags 5.7.2.dev2) | BSD-3-Clause (LICENSE) |
| jupyterlab-rise | [jupyterlab-contrib/rise](https://github.com/jupyterlab-contrib/rise) | [repo](https://github.com/jupyterlab-contrib/rise) | 254 | 31 | 54 | 17/04/2026 | v0.43.1 (31/12/2024) | BSD-3-Clause |
| pdfpc | [pdfpc/pdfpc](https://github.com/pdfpc/pdfpc) | [site](https://pdfpc.github.io/) | 1.881 | 126 | 32 | 23/04/2026 | v4.7.0 (17/12/2024) | GPL-3.0 |
| Kami | [tw93/Kami](https://github.com/tw93/Kami) | [site](https://kami.tw93.fun) | 12.002 | 557 | 0 | 18/10/2026 | V1.18.0 (15/10/2026) | MIT |
| GenOffice | [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice) | [site](https://genoffice.ai/) | 10.016 | 1.273 | 70 | 19/10/2026 | v0.11.829 (15/10/2026) | Apache-2.0 |
| slydst | [glambrechts/slydst](https://github.com/glambrechts/slydst) | [Typst Universe](https://typst.app/universe/package/slydst) | 141 | 5 | 1 | 30/01/2026 | nenhum | MIT |
| Focus | [pcafrica/focus-beamertheme](https://github.com/pcafrica/focus-beamertheme) | [CTAN](https://ctan.org/pkg/beamertheme-focus) | 546 | 47 | 0 | 07/02/2024 | v3.4.0 (07/02/2024) | GPL-3.0 |
| Auriga | [anishathalye/auriga](https://github.com/anishathalye/auriga) | [repo](https://github.com/anishathalye/auriga) | 405 | 38 | 0 | 01/02/2025 | nenhum | MIT |
| Arguelles | [piazzai/arguelles](https://github.com/piazzai/arguelles) | [CTAN](https://ctan.org/pkg/beamertheme-arguelles) | 283 | 25 | 0 | 26/04/2026 | v2.6.0 (26/04/2026) | MIT |
| SimplePlus | [pm25/SimplePlus-BeamerTheme](https://github.com/pm25/SimplePlus-BeamerTheme) | [CTAN](https://ctan.org/pkg/beamertheme-simpleplus) | 279 | 26 | 0 | 12/01/2025 | v1.1 (07/01/2025) | Unlicense |
| Ultimate list | [martinbjeldbak/ultimate-beamer-theme-list](https://github.com/martinbjeldbak/ultimate-beamer-theme-list) | [repo](https://github.com/martinbjeldbak/ultimate-beamer-theme-list) | 1.824 | 138 | 2 | 13/10/2026 | nenhum | nenhuma declarada |

### 1.1. Capacidades

Tabela 2. Recursos documentados. "Parcial" indica suporte limitado ou dependente de extensão; "n/d" indica que a documentação consultada não cobre o item; "n/a" indica item que não se aplica. "Código" se refere a bloco de código com realce.

| Projeto | Código | Matemática | Diagramas | Imagens | Animação | Notas | Exportação |
|---|---|---|---|---|---|---|---|
| presenterm | sim | sim | sim | sim | sim | sim | PDF, HTML |
| slides | sim | não | não | n/d | não | não | nenhuma documentada |
| patat | sim | n/d | não | experimental | sim | sim | nenhuma (dump) |
| lookatme | sim | n/d | via extensão | via ueberzug (Linux) | parcial | não | nenhuma |
| Touying | sim | sim | sim | sim | sim | sim | PDF, PPTX experimental, HTML |
| Polylux | sim | sim | sim | sim | sim | sim | PDF |
| Beamer/Metropolis | sim | sim | sim | sim | sim | sim | PDF |
| Pandoc | sim | sim | via LaTeX/TikZ | sim | limitada | sim | PDF, PPTX, HTML |
| Quarto | sim | sim | sim | sim | sim | sim | HTML, PDF, PPTX |
| Marp CLI | sim | sim | sim | sim | sim | sim | HTML, PDF, PPTX |
| xaringan | sim | sim | via widgets | sim | sim | sim | HTML |
| PPTist | não | sim | gráficos | sim | sim | sim | PPTX, PDF, imagens, JSON |
| Presenton | n/d | n/d | parcial | parcial | n/d | n/d | PPTX, PDF |
| PPTAgent | não | n/d | parcial | sim | não | não | PPTX, HTML |
| RISE | sim | sim | via libs | sim | sim | sim | PDF via nbconvert/decktape |
| pdfpc | n/a | n/a | n/a | n/a | n/a | sim | apresenta PDF |

### 1.2. Leitura das métricas

Estrelas medem atenção, não qualidade. O PPTist tem 9,4 mil estrelas e nenhum release; o Metropolis tem 6,9 mil e está congelado desde 2018; o slides tem 11,7 mil e não publica release desde 2022. O contrário também aparece: o Presenton chegou a 11,2 mil estrelas em menos de 18 meses, com commits diários.

Issues e pull requests abertos entram no mesmo número. Uma fila baixa pode significar estabilidade ou abandono, e uma fila alta pode significar uso intenso. Para separar os casos, a nota olha a data do último commit, a cadência de releases e o volume de forks. Forks altos em temas (Metropolis, PPTist) costumam indicar uso como base, não contribuição.

## 2. Terminal

### 2.1. presenterm

**O que é.** Uma ferramenta de linha de comando em Rust que lê Markdown e apresenta no terminal. Aceita um ou vários arquivos, temas em YAML, layout em colunas, títulos de slide e slide de introdução. O diferencial é tratar o terminal como superfície gráfica: imagens e GIFs em kitty, iTerm2, WezTerm, Ghostty e foot, gráficos Mermaid e D2, fórmulas LaTeX e Typst, realce seletivo de código e execução de snippets.

**Visual e recursos.** Tem realce para muitas linguagens, tamanhos de fonte, transições, pausas, recarga automática e atalhos configuráveis. O teto é o terminal: não há antialiasing vetorial nem posicionamento absoluto, e imagens dependem do protocolo do emulador. Para live coding e demonstrações de CLI, o resultado é o mais convincente da categoria.

**Exportação e notas.** Exporta PDF via weasyprint e HTML autocontido. As notas do apresentador usam duas instâncias, uma publicando e outra ouvindo por UDP em localhost; no Mac, só um listener funciona por vez. Não exporta PPTX.

**Aprendizado e manutenção.** Markdown mais comentários HTML; o binário único instala por brew, cargo, nix, scoop ou winget. O release v0.16.1 é de fevereiro de 2026 e o último commit de maio de 2026, cinco meses antes da coleta. Há 84 issues abertas. O projeto está ativo.

**Uso e limites.** Serve para palestras de programação, demos de terminal, acesso remoto por SSH e eventos em que a estética de terminal é parte do conteúdo. Limita quando a plateia está longe, quando a fonte do terminal é pequena e quando o emulador não suporta imagens. Também não serve para material que precisa ser editado por não técnicos.

**Showcase.** O GIF de demonstração e o `examples/demo.md` do repositório mostram imagens, colunas e código; o README lista palestras de Orhun Parmaksız sobre Ratatui e TUI.

**Fontes.** [README](https://github.com/mfontanini/presenterm), [exportação](https://mfontanini.github.io/presenterm/features/exports.html), [notas](https://mfontanini.github.io/presenterm/features/speaker-notes.html), [API](https://api.github.com/repos/mfontanini/presenterm).

### 2.2. slides

**O que é.** Um apresentador de terminal em Go, com Markdown, temas JSON no formato do glamour, paginação, autor e data. O diferencial é a simplicidade: um binário, um arquivo e nenhum build. Também executa blocos de código com Ctrl+E, pré-processa blocos com comandos externos e aceita entrada por stdin.

**Visual e recursos.** A saída é ANSI bem cuidada, com temas prontos e busca por expressão regular. O README não documenta imagens, matemática nem diagramas. Para texto e código, o resultado é limpo; para gráficos, fica atrás do presenterm.

**Exportação e notas.** Não documenta exportação para PDF, PPTX ou HTML, nem notas do apresentador. O comando `slides serve` permite assistir por SSH, o que resolve apresentação remota sem instalar nada na máquina do espectador.

**Aprendizado e manutenção.** A curva é a mais baixa da categoria. O último release é v0.9.0, de setembro de 2022, embora existam commits até julho de 2026. São 79 issues abertas. A ausência de release por quatro anos é o principal sinal de risco: correções podem existir no branch principal sem chegar a um pacote.

**Uso e limites.** Serve para talks rápidas, aulas de terminal e apresentações remotas. Limita por não ter exportação, notas ou imagens documentadas, e por ter um conjunto de recursos congelado na prática.

**Showcase.** O GIF `assets/slides-1.gif` e o diretório `examples` mostram o fluxo básico, incluindo execução e pré-processamento.

**Fontes.** [README](https://github.com/maaslalani/slides), [API](https://api.github.com/repos/maaslalani/slides), [release](https://api.github.com/repos/maaslalani/slides/releases/latest).

### 2.3. patat

**O que é.** Um apresentador de terminal em Haskell construído sobre Pandoc. Aceita Markdown, reStructuredText, Org e outros formatos que o Pandoc lê, o que o torna a opção natural para quem já mantém documentos nesses formatos. Tem realce com sintaxe do Kate, slides incrementais, transições, avanço automático, temas com 24 bits e imagens experimentais.

**Visual e recursos.** O cuidado com tipografia de terminal aparece na centralização, na reescrita de linhas e nas margens. Imagens são experimentais e matemática não é documentada. O resultado é elegante para texto corrido, menos expressivo para conteúdo visual.

**Exportação e notas.** Não exporta PDF nem PPTX; `--dump` despeja os slides em texto. As notas do apresentador podem ser gravadas em arquivo a cada mudança de slide e exibidas em outro terminal ou em uma segunda instância do patat, o que funciona bem em dois monitores.

**Aprendizado e manutenção.** A curva é baixa para quem conhece Markdown e Pandoc. A instalação vem por Homebrew, Cabal ou pacotes Linux. O release v0.15.2.0 é de agosto de 2025 e o último commit de junho de 2026; há 23 issues abertas. É um projeto pequeno, com manutenção constante.

**Uso e limites.** Serve para palestras textuais, aulas e quem quer notas em segunda janela sem sair do terminal. Limita por não ter exportação, por tratar imagens como experimentais e por não documentar matemática.

**Showcase.** O GIF `extra/demo.gif` mostra o fluxo de slides e o realce de código.

**Fontes.** [README](https://github.com/jaspervdj/patat), [Hackage](https://hackage.haskell.org/package/patat), [API](https://api.github.com/repos/jaspervdj/patat).

### 2.4. lookatme

**O que é.** Um apresentador de terminal em Python, com Markdown, realce via Pygments, terminais interativos embutidos, carregamento de arquivos externos e extensões contributivas. Entre elas estão QR code, imagens com ueberzug (só Linux) e renderização de Graphviz e Mermaid por programa externo. Os slides progressivos usam comentários `<!-- stop -->`.

**Visual e recursos.** A saída é funcional e personalizável por estilos do Pygments. Imagens dependem de extensão e de ueberzug no Linux; matemática não é documentada. O recurso mais distintivo é embutir um terminal vivo dentro do slide, útil para demonstrar ferramentas de linha de comando.

**Exportação e notas.** Não documenta exportação para PDF, PPTX ou HTML, nem notas do apresentador. O foco é a execução ao vivo.

**Aprendizado e manutenção.** A curva é baixa para quem usa Python e pip. O último commit é de janeiro de 2023 e o último release do GitHub é v2.5.0, de outubro de 2022, embora o PyPI tenha 2.5.5. São 38 issues abertas. O README ainda diz que a versão 3.0 está próxima, mas o sinal de atividade é fraco.

**Uso e limites.** Serve para demos de terminal, aulas de Python e apresentações legadas. Limita por estar parado, por imagens só funcionarem no Linux com ueberzug e por não ter exportação.

**Showcase.** Os GIFs de tour, terminal embutido e carregamento de arquivos externos no repositório mostram o que a ferramenta faz de melhor.

**Fontes.** [README](https://github.com/d0c-s4vage/lookatme), [docs](https://lookatme.readthedocs.io/en/latest/), [PyPI](https://pypi.org/project/lookatme/), [API](https://api.github.com/repos/d0c-s4vage/lookatme).

## 3. Typst

### 3.1. Touying

**O que é.** Um pacote de slides para Typst, com slides baseados em headings, seis temas embutidos (Simple, Metropolis, Dewdrop, University, Aqua e Stargazer), animações com `#pause` e `#meanwhile`, animação de equações e integração com CeTZ e Fletcher. O modo artigo compila o mesmo arquivo como slides ou como prosa, com as animações colapsadas no estado final.

**Visual e recursos.** A tipografia é a do Typst, com compilação em milissegundos e preview ao vivo. O resultado é o mais pronto da categoria: temas, capa, bookmarks de PDF, notas e animações vêm no pacote. A versão 0.8.0 exige Typst 0.15 e trouxe mudanças de API.

**Exportação e notas.** Exporta PDF nativo. PPTX editável ou com fidelidade visual é experimental, via Tylina ou `touying-exporter`; o mesmo exportador gera HTML. As notas do apresentador funcionam em segunda tela com pdfpc, pympress, PowerPoint ou HTML, e o bundle pode gravar arquivos `.pdfpc`.

**Aprendizado e manutenção.** A curva é média: é preciso conhecer Typst e a API de temas. A documentação é em inglês e chinês. O release 0.8.0 é de setembro de 2026 e o último commit é do mesmo mês; há 33 issues abertas. O projeto é muito ativo.

**Uso e limites.** Serve para talks acadêmicas, aulas, matemática e diagramas com CeTZ/Fletcher. Limita porque o PPTX ainda é experimental, as notas dependem de ferramenta externa e a API mudou na 0.8.0. A página de temas citada no README retorna 404; a galeria que funciona é a wiki do repositório.

**Showcase.** A galeria da wiki, o exemplo `examples/simple.typ` aberto no Tylina e as capturas de animação de equações e CeTZ/Fletcher no README.

**Fontes.** [README](https://github.com/touying-typ/touying), [docs](https://touying-typ.github.io/), [wiki](https://github.com/touying-typ/touying/wiki), [Typst Universe](https://typst.app/universe/package/touying), [API](https://api.github.com/repos/touying-typ/touying).

### 3.2. Polylux

**O que é.** Um pacote minimalista de slides para Typst. O usuário cria slides com `#slide`, controla conteúdo dinâmico com `#uncover`, `#only`, `#alternatives` e `#pause`, e monta o design com funções do próprio Typst. Não traz temas próprios; parte de templates da Typst Universe, sendo o "basic" o mais simples.

**Visual e recursos.** O padrão é cru, sem identidade visual. O teto é alto porque tudo é Typst, mas o resultado depende inteiramente do template escolhido. A API de overlays é mais direta que a de pacotes opinativos, o que agrada quem quer controle fino.

**Exportação e notas.** Exporta PDF. O suporte a pdfpc cobre notas, ocultação de slides e configuração de timer, o que resolve o modo apresentador fora do Typst.

**Aprendizado e manutenção.** A curva é média, com a documentação em livro. O release v0.4.0 é de janeiro de 2025 e o último commit de fevereiro de 2026; há 97 issues abertas. O README avisa que não há garantia de compatibilidade retroativa, o que é um custo real para projetos longos.

**Uso e limites.** Serve para quem quer design próprio, matemática e controle de overlays em Typst. Limita por não ter temas, pela API em movimento e pela dependência de pdfpc para notas.

**Showcase.** O `demo.pdf` publicado no release e o exemplo mínimo `examples/minimal.png` mostram o contraste entre o padrão cru e o que os templates entregam.

**Fontes.** [README](https://github.com/polylux-typ/polylux), [book](https://polylux.dev/book), [demo.pdf](https://github.com/andreasKroepelin/polylux/releases/latest/download/demo.pdf), [API](https://api.github.com/repos/polylux-typ/polylux).

### 3.3. slydst

**O que é.** Um pacote de slides estáticos simples em Typst, com 141 estrelas, licença MIT e último commit em janeiro de 2026. Não tem release publicado e a documentação é a da Typst Universe.

**Visual e recursos.** O foco é o mínimo: páginas de slide, tipografia e pouco mais. Não compete com Touying ou Polylux em temas, animações ou notas.

**Uso e limites.** Serve para quem quer um arquivo Typst curto e sem dependências conceituais. Limita pela baixa tração, pela ausência de release e pelo conjunto de recursos reduzido.

**Fontes.** [Repositório](https://github.com/glambrechts/slydst), [Typst Universe](https://typst.app/universe/package/slydst), [API](https://api.github.com/repos/glambrechts/slydst).

## 4. LaTeX Beamer

### 4.1. Beamer e Metropolis

**Beamer.** É a referência para slides acadêmicos em PDF. Entrega overlays, matemática, TikZ, notas do apresentador, temas e uma base de pacotes madura. O custo é a curva do LaTeX e o peso da instalação, mas para conteúdo matemático denso continua sendo o caminho mais previsível. A documentação central está no CTAN.

**Metropolis.** Um tema minimalista para Beamer, com Fira Sans, barra de progresso opcional e blocos limpos. Está no CTAN desde dezembro de 2014 e é distribuído em MiKTeX e TeX Live. O desenho é de 2014 e ainda aparece em conferências, mas o último commit é de agosto de 2018 e o último release é v1.2, de janeiro de 2017; há 91 issues abertas. Na prática, é um tema congelado.

**Visual e recursos.** O resultado é sóbrio e legível, com boa hierarquia tipográfica. A licença é CC-BY-SA 4.0, conforme o README; modificações do tema precisam manter a mesma licença, mas as apresentações geradas não são afetadas. A API do GitHub não detecta um SPDX para o repositório.

**Exportação e notas.** PDF. Notas do apresentador via recursos do Beamer ou pdfpc. O modo apresentador depende do leitor de PDF escolhido.

**Uso e limites.** Serve para conferências, defesas, aulas e qualquer talk com matemática ou TikZ. Limita pelo congelamento, pelo visual datado em relação a temas mais novos e pela dependência de Fira Sans para o resultado pretendido.

**Showcase.** O PDF de demonstração no CTAN mostra capa, seções, blocos e barras.

**Fontes.** [README](https://github.com/matze/mtheme), [CTAN](https://ctan.org/pkg/beamertheme-metropolis), [demo.pdf](https://mirrors.ctan.org/macros/latex/contrib/beamer-contrib/themes/metropolis/demo/demo.pdf), [API](https://api.github.com/repos/matze/mtheme).

### 4.2. Alternativas mantidas

Tabela 3. Temas de Beamer com atividade posterior ao Metropolis.

| Tema | Estrelas | Issues | Último commit | Release | Licença | Traço |
|---|---:|---:|---|---|---|---|
| Focus | 546 | 0 | 07/02/2024 | v3.4.0 | GPL-3.0 | Minimalista, Fira, CTAN, requer PGF/TikZ e appendixnumberbeamer |
| Auriga | 405 | 0 | 01/02/2025 | nenhum | MIT | Enxuto, LuaTeX, Raleway/Lato/Hack, gera PDF de notas |
| Arguelles | 283 | 0 | 26/04/2026 | v2.6.0 | MIT | Tipográfico, Alegreya/Euler, CTAN |
| SimplePlus | 279 | 0 | 12/01/2025 | v1.1 | Unlicense | Acadêmico, CTAN e Overleaf |
| Ultimate list | 1.824 | 2 | 19/10/2026 | nenhum | nenhuma | Catálogo de temas, não um tema |

O Focus é a alternativa mantida mais próxima do espírito do Metropolis. O Auriga é o mais enxuto e tem um detalhe útil: o Makefile gera `p.pdf` e `p-notes.pdf`, este último com notas do apresentador. O Arguelles é o mais tipográfico, com Alegreya e Euler, e permite remover as fontes com a opção `noalegre`. O SimplePlus é o mais simples de adotar, com CTAN e Overleaf.

Nenhum desses temas tem a tração do Metropolis, mas todos têm commits ou releases mais recentes. O Ultimate Beamer Theme List serve para descobrir outras opções, não para escolher um design pronto; a API não declara licença, então a reutilização pede contato com o autor.

**Showcase.** O Focus traz um demo no diretório [focus-demo](https://github.com/pcafrica/focus-beamertheme/tree/main/focus-demo); o Auriga publica o [auriga.pdf](https://raw.githubusercontent.com/anishathalye/assets/master/auriga/auriga.pdf); o Arguelles publica o [demo-arguelles.pdf](https://github.com/piazzai/arguelles/raw/master/demo-arguelles.pdf); o SimplePlus publica [sample.pdf](https://github.com/pm25/SimplePlus-BeamerTheme/blob/master/sample.pdf) e previews no diretório `preview`.

**Fontes.** [Focus](https://github.com/pcafrica/focus-beamertheme), [Auriga](https://github.com/anishathalye/auriga), [Arguelles](https://github.com/piazzai/arguelles), [SimplePlus](https://github.com/pm25/SimplePlus-BeamerTheme), [Ultimate list](https://github.com/martinbjeldbak/ultimate-beamer-theme-list).

## 5. Pipelines Markdown

### 5.1. Pandoc

**O que é.** Um conversor universal escrito em Haskell. Para apresentações, aceita Markdown e outros formatos e gera Beamer, PowerPoint, reveal.js, Slidy, DZSlides e Typst, entre outros. PDF sai por pdflatex, lualatex, xelatex, tectonic, typst, weasyprint ou outros motores.

**Diferencial.** A fonte única é o argumento principal: o mesmo Markdown vira artigo, slides e handout. O Pandoc oferece notas do apresentador em Beamer, PPTX e reveal.js, listas incrementais, colunas, `--slide-level`, filtros Lua e `--reference-doc` para PPTX. Para Beamer, variáveis como `theme`, `aspectratio` e `colortheme` passam direto ao template.

**Visual e recursos.** O Pandoc não tem design próprio. O resultado é tão bom quanto o tema Beamer ou o documento de referência do PPTX. No PPTX, ele escolhe layouts predefinidos (Title Slide, Section Header, Two Content) e não documenta animações de elemento. Layouts complexos exigem LaTeX ou HTML bruto.

**Exportação e notas.** PDF, PPTX e HTML. As notas usam o bloco `::: notes` e aparecem no PowerPoint, no Beamer e no reveal.js.

**Aprendizado e manutenção.** A linha de comando é simples; a customização é avançada. A instalação é um binário Haskell, mas PDF exige TeX ou outro motor. O release 3.12.1 é de outubro de 2026 e o último commit é do mesmo mês; há 1.047 issues abertas. O projeto é muito ativo.

**Uso e limites.** Serve para documentos que viram slides, automação de apresentações e fluxos acadêmicos. Limita no PPTX, que tem estilo limitado, e em layouts que precisam de posicionamento fino.

**Showcase.** Não há showcase visual próprio; o resultado depende do tema.

**Fontes.** [Manual](https://pandoc.org/MANUAL.html), [site](https://pandoc.org), [API](https://api.github.com/repos/jgm/pandoc).

### 5.2. Quarto

**O que é.** Um sistema de publicação científica construído sobre o Pandoc. Para apresentações, oferece `revealjs` (HTML), `pptx` e `beamer` (PDF). O mesmo projeto pode executar código Python, R ou Julia, o que o torna popular em ciência de dados e ensino.

**Visual e recursos.** O reveal.js é o formato mais capaz e o recomendado pela própria documentação. O PPTX e o Beamer dependem de tema ou documento de referência. O Quarto adiciona listas incrementais, colunas, notas e preview ao vivo.

**Exportação e notas.** HTML, PDF e PPTX. Notas do apresentador no reveal.js e, via Pandoc, nos formatos que suportam notes.

**Aprendizado e manutenção.** A curva é média: é preciso entender o CLI do Quarto, o Pandoc e, para Beamer, o LaTeX. O release v1.10.19 é de outubro de 2026 e o último commit é do mesmo dia; há 1.907 issues abertas. A atividade é alta e a fila também.

**Uso e limites.** Serve para talks reprodutíveis, aulas com código e relatórios que viram slides. Limita pelo peso da instalação e pela necessidade de conhecer o formato de saída escolhido.

**Showcase.** A galeria do Quarto reúne apresentações e documentos; a documentação de apresentações mostra o fluxo mínimo.

**Fontes.** [Apresentações](https://quarto.org/docs/presentations/), [Beamer](https://quarto.org/docs/presentations/beamer.html), [PowerPoint](https://quarto.org/docs/presentations/powerpoint.html), [galeria](https://quarto.org/docs/gallery/), [API](https://api.github.com/repos/quarto-dev/quarto-cli).

### 5.3. Marp CLI

**O que é.** Uma ferramenta de linha de comando em Node para converter Markdown no formato Marp/Marpit em HTML, PDF, PPTX e imagens. Os temas são CSS, o que facilita alinhar a palestra à identidade visual de uma marca. Tem modo watch e servidor.

**Visual e recursos.** O resultado é web, com tipografia CSS. O Marp Core traz plugins de KaTeX, MathJax e Mermaid, então matemática e diagramas são possíveis. O PPTX padrão é rasterizado: cada slide vira imagem, o que preserva a aparência mas não permite editar o conteúdo.

**Exportação e notas.** HTML, PDF, PPTX e imagens. As notas do Marpit podem ser exportadas em TXT (`--notes`), anotadas no PDF (`--pdf-notes`) e incluídas no PPTX. O modo `--pptx-editable` é experimental, exige LibreOffice, tem fidelidade menor e não suporta notas.

**Aprendizado e manutenção.** A curva é baixa para Markdown e média para CSS. A instalação é via npx; PDF, PPTX e imagens exigem Chrome, Edge ou Firefox. O release v4.5.1 é de setembro de 2026 e o último commit é de dois dias depois; há 20 issues abertas. O projeto é ativo.

**Uso e limites.** Serve para talks de desenvolvedor, decks de marca e PDFs de distribuição. Limita porque o PPTX padrão não é editável, o modo editável perde fidelidade e o HTML gerado não teve um console de apresentador confirmado nesta coleta.

**Showcase.** O site do Marp e os exemplos do repositório mostram temas e o fluxo de conversão.

**Fontes.** [README](https://github.com/marp-team/marp-cli), [Marp](https://marp.app/), [Marp Core](https://github.com/marp-team/marp-core), [API](https://api.github.com/repos/marp-team/marp-cli).

### 5.4. xaringan

**O que é.** Uma extensão de R Markdown para slides em HTML, baseada no remark.js. Usa a sintaxe de Markdown do R Markdown, temas em CSS, slides incrementais, notas do apresentador e MathJax. Diagramas entram por widgets HTML.

**Visual e recursos.** O resultado é web e depende do tema CSS. Para R e biostatística, há temas prontos e integração com gráficos; sem customização, fica menos polido que Quarto ou reveal.js.

**Exportação e notas.** O formato nativo é HTML. PDF depende de impressão do navegador ou de ferramenta externa; não testei esse fluxo. As notas usam `???`, a convenção do remark.js.

**Aprendizado e manutenção.** A curva é média para quem já usa R Markdown. O release v0.31 é de agosto de 2025 e o último commit é do mesmo mês; há 45 issues abertas. O DESCRIPTION indica versão 0.31.1 e licença MIT, embora a API retorne "Other".

**Uso e limites.** Serve para aulas de R, relatórios com código e quem já tem um fluxo R Markdown. Limita pela dependência de R, pela ausência de PDF/PPTX nativos e pela necessidade de CSS para um resultado autoral.

**Showcase.** O site de demonstração do xaringan mostra temas, código e notas.

**Fontes.** [Repositório](https://github.com/yihui/xaringan), [demo](https://slides.yihui.org/xaringan/), [livro do R Markdown](https://bookdown.org/yihui/rmarkdown/xaringan.html), [API](https://api.github.com/repos/yihui/xaringan).

## 6. Editor e suíte

### 6.1. PPTist

**O que é.** Uma aplicação web de edição e apresentação de slides, escrita em Vue 3 e TypeScript, sem biblioteca de UI. Replica os elementos mais usados do PowerPoint: texto rico, imagens, formas, linhas, gráficos, tabelas, vídeo, áudio e fórmulas. Também oferece AIPPT baseado em templates e um esquema de dados para a IA gerar páginas diretamente.

**Visual e recursos.** O controle é alto e a experiência se aproxima de um aplicativo de desktop, com menus de contexto, atalhos, alinhamento magnético, camadas, animações de transição e de elemento, notas ricas e visualização do apresentador. A importação de PPTX tem fidelidade declarada de cerca de 85% e a exportação, de cerca de 95%, segundo o README. São números do fornecedor, não medições independentes.

**Exportação e notas.** PPTX, PDF por impressão, imagens, JSON e o formato próprio `.pptist`. As notas do apresentador são rich text e há "speaker view" no modo de apresentação. O AIPPT é baseado em templates e depende de modelo, prompt e ativos.

**Aprendizado e manutenção.** Como usuário, a curva é baixa; como desenvolvedor, é alta, porque o projeto é uma base Vue para construir um produto. Requer Node 20 ou superior. A licença é AGPL-3.0, com obrigações fortes para quem oferece o serviço pela rede. Não há releases, mas há commits até outubro de 2026 e 21 issues abertas.

**Uso e limites.** Serve para construir um editor de slides web, um produto vertical ou uma ferramenta de pré-visualização de PPTX. Não é um produto pronto, e o próprio README desaconselha usá-lo como ferramenta acabada. A fidelidade de PPTX não é total, e o AIPPT não é um gerador autônomo de qualidade garantida.

**Showcase.** A demonstração online cobre edição, apresentação e AIPPT.

**Fontes.** [README](https://github.com/pipipi-pikachu/PPTist), [demo](https://pipipi-pikachu.github.io/PPTist/), [API](https://api.github.com/repos/pipipi-pikachu/PPTist).

## 7. Geração por IA

### 7.1. Presenton

**O que é.** Um gerador de apresentações com IA, auto-hospedado, com API e aplicativo desktop. Cria slides a partir de um prompt, de um documento ou de um template PPTX. Funciona com Ollama, LM Studio, OpenAI, Gemini, Vertex AI, Azure OpenAI, Bedrock, Fireworks, Together, Anthropic e qualquer provedor compatível com OpenAI. Tem edição por arrastar, templates embutidos e exportação para PPTX totalmente editável.

**Visual e recursos.** A qualidade visual é a de templates de negócio, com layouts para pitch, relatórios, atualizações executivas e educação. O resultado depende do modelo, do template e dos ativos. O diferencial é o controle: modelo, dados e design ficam na máquina ou na infraestrutura do usuário, sem assinatura obrigatória.

**Exportação e notas.** PPTX editável e PDF, segundo o README. A API permite geração programática. Não encontrei documentação de notas do apresentador ou de um modo apresentador próprio.

**Aprendizado e manutenção.** A curva é média: Docker ou app desktop, chave de modelo e configuração de template. O projeto foi criado em maio de 2025 e chegou a 11,2 mil estrelas em menos de 18 meses, com commits no dia da coleta e 31 issues abertas. A licença é Apache-2.0. O release mais recente é v0.9.11-beta, de setembro de 2026, ou seja, o trem de releases ainda é beta.

**Uso e limites.** Serve para equipes que querem auto-hospedar, proteger dados, gerar muitos decks e integrar via API. Limita pelo custo e pela variabilidade do modelo, pela dependência de templates e pela ausência de teste independente da fidelidade do PPTX. A exportação editável é uma afirmação do fornecedor.

**Showcase.** A galeria de templates do Presenton mostra Momentum, Dynamic, Executive, General, Modern e Standard.

**Fontes.** [README](https://github.com/presenton/presenton), [site](https://presenton.ai), [templates](https://presenton.ai/explore), [API](https://api.github.com/repos/presenton/presenton).

### 7.2. PPTAgent

**O que é.** Um framework agêntico de pesquisa para gerar PowerPoint. O método é de duas etapas e baseado em edição: primeiro analisa apresentações de referência para extrair tipos funcionais de slide e esquemas de conteúdo; depois monta um outline e gera ações de edição sobre slides de referência. O artigo foi aceito na EMNLP 2025, e o DeepPresenter, com pesquisa profunda, design livre e criação de ativos, foi aceito na ACL 2026.

**Visual e recursos.** O resultado é editável e guiado por referência, o que costuma ser mais coerente do que a geração livre. O projeto inclui avaliação PPTEval em conteúdo, design e coerência, servidor MCP, skill para Claude Code, Codex e OpenCode, e revisão visual com modelo multimodal. A qualidade depende da deck de referência, do modelo e dos ativos.

**Exportação e notas.** PPTX, fontes HTML e previews. Não documenta notas do apresentador nem modo apresentador.

**Aprendizado e manutenção.** A curva é alta: Python 3.12, uv, LibreOffice, Chrome, chaves de modelo e dependências de conversão. O release v2.0.0 é de dezembro de 2025 e o último commit de setembro de 2026; há 18 issues abertas. A licença é MIT. É pesquisa aplicada com manutenção ativa, não um produto de prateleira.

**Uso e limites.** Serve para geração de decks a partir de documentos, pesquisa em geração de slides e fluxos de agentes. Limita pelo peso das dependências, pelo custo de tokens, pela complexidade de instalação e pela variância do resultado.

**Showcase.** O GIF de demonstração no repositório e os artigos no arXiv mostram o pipeline e os resultados.

**Fontes.** [README](https://github.com/icip-cas/PPTAgent), [paper](https://arxiv.org/abs/2501.03936), [API](https://api.github.com/repos/icip-cas/PPTAgent).

### 7.3. allweonedev/presentation-ai

**O que é.** Um clone open source de Gamma, em Next.js, React, TypeScript e PostgreSQL. O fluxo é outline-first: gera um outline, permite editar, depois transforma em slides. Tem 38 temas embutidos, criação de temas, importação de tema de PPTX, geração de imagens, modo de apresentação, link público, gravação e exportação para PPTX.

**Visual e recursos.** A proposta é uma experiência web de produto, com temas e edição por arrastar. A qualidade depende do modelo e do tema. A stack é pesada para auto-hospedagem: Next.js, Prisma, NextAuth, UploadThing e PostgreSQL.

**Exportação e notas.** PPTX. PDF não é documentado. O modo de apresentação acontece dentro do app.

**Aprendizado e manutenção.** A curva é média-alta para self-host, por causa do banco, autenticação, armazenamento e chaves de modelo. O projeto tem 3.050 estrelas, licença MIT, nenhum release e último commit em junho de 2026; as issues abertas aparecem como zero. Esse conjunto sugere menos atividade recente que Presenton e PPTAgent.

**Uso e limites.** Serve para quem quer uma alternativa a Gamma com código aberto e controle do modelo. Limita pela ausência de PDF, pela stack pesada e pela falta de releases.

**Showcase.** A demonstração pública em presentation.allweone.com.

**Fontes.** [README](https://github.com/allweonedev/presentation-ai), [demo](https://presentation.allweone.com), [API](https://api.github.com/repos/allweonedev/presentation-ai).

### 7.4. Fronteira: Kami e GenOffice

**Kami.** Um sistema de regras de layout e templates para agentes de IA exportarem PDF, PNG e PowerPoint editável. Tem 12.002 estrelas, licença MIT, release v1.18.0 em outubro de 2026 e oito templates de documento, entre eles um de keynote com oito slides. Não é um editor de slides; é uma camada de layout para agentes.

**GenOffice.** Uma suíte de escritório com IA, com Docs, Sheets, Slides, PDF, Markdown e HTML, além de CLI e skill para agentes. Abre e salva `.docx`, `.xlsx` e `.pptx` nativos. Tem 10.016 estrelas, Apache-2.0, release v0.11.829 em outubro de 2026 e 70 issues abertas. É uma suíte, não um gerador dedicado de apresentações.

Os dois mostram que a fronteira de "apresentação" está se movendo para agentes e suítes. Para um relatório sobre slides, servem como contexto e como sinal de tração, não como substitutos de Presenton ou PPTAgent.

**Fontes.** [Kami](https://github.com/tw93/Kami), [site do Kami](https://kami.tw93.fun), [GenOffice](https://github.com/genspark-ai/genoffice), [site do GenOffice](https://genoffice.ai/).

## 8. Jupyter e apresentação de PDF

### 8.1. RISE

**O que é.** Uma extensão do notebook clássico do Jupyter que transforma o notebook em uma apresentação reveal.js ao vivo, sem conversão. Tem notas do apresentador, temas, transições e exportação para PDF via nbconvert ou decktape.

**Status.** O próprio changelog declara "END OF LIFE": o RISE só suporta o notebook clássico, que está obsoleto, e não será mais mantido. O último commit é de outubro de 2023, há 162 issues abertas e a API não lista release estável, apenas tags 5.7.2.dev2.

**Uso e limites.** Serve apenas para notebooks clássicos legados. Para JupyterLab e Notebook 7, o caminho é o jupyterlab-rise. Não é uma escolha para projeto novo.

**Showcase.** O notebook de demonstração no Binder, linkado no README.

**Fontes.** [README](https://github.com/damianavila/RISE), [docs](https://rise.readthedocs.io), [changelog](https://rise.readthedocs.io/en/latest/changelog.html), [API](https://api.github.com/repos/damianavila/RISE).

### 8.2. jupyterlab-rise

**O que é.** O sucessor do RISE para JupyterLab e Notebook 7, com a mesma proposta de transformar o notebook em slides reveal.js ao vivo. Tem 254 estrelas, licença BSD-3-Clause, release v0.43.1 em dezembro de 2024 e último commit em abril de 2026; há 54 issues abertas.

**Uso e limites.** Serve para quem trabalha em JupyterLab e quer apresentar notebooks sem converter. A tração é menor que a do RISE clássico, e a manutenção é de comunidade.

**Fontes.** [Repositório](https://github.com/jupyterlab-contrib/rise), [API](https://api.github.com/repos/jupyterlab-contrib/rise).

### 8.3. pdfpc

**O que é.** Um console de apresentador para PDF, com saída multi-monitor no estilo Keynote. Mostra slide atual e próximo, notas, tempo restante, visão geral, overlays, congelamento da tela e reprodução de vídeo. Processa PDFs gerados por quase todas as ferramentas modernas.

**Por que entra.** É o complemento natural para Beamer, Polylux, Touying e presenterm quando o resultado é PDF. O apresentador ganha notas e timer sem depender do leitor de PDF padrão.

**Números e limites.** 1.881 estrelas, 126 forks, 32 issues, GPL-3.0, release v4.7.0 em dezembro de 2024 e último commit em abril de 2026. Exige GTK e um ambiente gráfico; não é uma solução de terminal puro.

**Showcase.** A página oficial mostra o presenter view com slide atual, próximo, notas e tempo.

**Fontes.** [Site](https://pdfpc.github.io/), [repositório](https://github.com/pdfpc/pdfpc), [API](https://api.github.com/repos/pdfpc/pdfpc).

## 9. Comparação e critérios de escolha

### 9.1. Por objetivo

Para live coding e demos de terminal, o presenterm tem o conjunto mais completo; o slides é o mais simples; o patat é o melhor para quem já usa Pandoc; o lookatme só se justifica em fluxos legados.

Para PDF acadêmico com matemática, o Beamer com Metropolis ou com Focus/Auriga/Arguelles/SimplePlus é o caminho conservador. O Touying é a alternativa moderna em Typst, com mais recursos prontos; o Polylux é para quem quer controle fino e aceita montar o design.

Para fonte única em Markdown, o Pandoc é a base e o Quarto é a camada de produtividade. Para times que querem HTML/PDF/PPTX com temas CSS, o Marp CLI é o mais direto.

Para editar slides como no PowerPoint, o PPTist é a base mais próxima, com a ressalva da AGPL e da fidelidade de importação/exportação. Para gerar decks com IA, o Presenton é a opção com mais tração e PPTX editável; o PPTAgent é a opção de pesquisa e fluxo agêntico; o allweonedev é um clone de Gamma com stack pesada.

Para Jupyter, o jupyterlab-rise é o único caminho novo. Para apresentar PDF com notas, o pdfpc resolve.

### 9.2. Custos e riscos

Projetos congelados: Metropolis (2018), lookatme (2023), RISE (2023) e slides (sem release desde 2022). Projetos com PPTX de fidelidade não comprovada: Touying (experimental), Marp no modo editável, Presenton e PPTAgent (afirmações de fornecedor). Projetos com licença de copyleft forte: PPTist (AGPL-3.0), patat e Focus (GPL), pdfpc (GPL). Projetos com licença de documentação: Metropolis (CC-BY-SA 4.0).

Peso de dependência: PPTAgent é o mais pesado; Quarto e Beamer exigem instalações grandes; os apresentadores de terminal são binários leves. Atividade e estrelas não andam juntos: slides e Metropolis têm muitas estrelas e pouca manutenção; Presenton e Touying têm menos estrelas e releases recentes.

### 9.3. Lacunas da pesquisa

Não renderizei, instalei ou cronometrei nenhum projeto, então as notas de qualidade visual são julgamentos sobre documentação, GIFs e PDFs de demonstração. Não fiz varredura sistemática de Hacker News, Reddit ou blogs; a tração foi inferida de estrelas, forks, releases e showcases oficiais. A contagem de issues inclui pull requests.

Alguns pontos ficaram sem confirmação: o console de apresentador do HTML gerado pelo Marp CLI; a exportação de PDF do xaringan sem ferramenta externa; a fidelidade real do PPTX do Presenton, do PPTAgent e do PPTist; e a profundidade do suporte a slides do Kami e do GenOffice. O release do Presenton é declarado beta, o que pode não representar a maturidade do produto. O link de temas do Touying no README retorna 404. As contagens de estrelas e issues são um retrato de 19/10/2026 e mudam com o tempo.
