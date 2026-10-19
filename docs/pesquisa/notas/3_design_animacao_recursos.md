# Design, diagramas, animação e recursos visuais para apresentações

## 1. Método, coleta e limites

### Takeaway

A coleta principal reuniu 58 repositórios ligados a diagramas, animação, ícones, tipografia, captura de tela, mockups e temas de slides; um fork comunitário do Motion Canvas foi verificado à parte. Todos os números de estrelas, forks, issues e atividade vieram da API REST do GitHub em 19/10/2026, entre 13h23 e 13h34 UTC; estrelas e forks mudam ao longo do dia, então a leitura vale para esse horário. O retrato é um instantâneo, não uma medida de qualidade: estrelas acumulam história e favorecem projetos antigos, enquanto repositórios-espelho, como o do draw.io, aparecem muito abaixo da adoção real.

### Cited Findings

- A coleta usou `GET https://api.github.com/repos/{owner}/{repo}`, `GET /releases/latest` e `GET /tags?per_page=1`, com autenticação via `gh api`; os campos registrados foram `stargazers_count`, `forks_count`, `open_issues_count`, `pushed_at`, `license.spdx_id` e `archived` ([API do GitHub](https://docs.github.com/en/rest/repos/repos)).
- `open_issues_count` soma issues e pull requests abertos, portanto os números de "issues" nas fichas são, na prática, issues mais PRs ([documentação do campo](https://docs.github.com/en/rest/repos/repos#get-a-repository)).
- `pushed_at` indica o último push em qualquer branch, não necessariamente o último commit no branch principal nem uma nova release; por isso a ficha separa "último push" de "último release" ([documentação do campo](https://docs.github.com/en/rest/repos/repos#get-a-repository)).
- Quando o campo de licença voltou `NOASSERTION`, a licença foi conferida no arquivo `LICENSE` do repositório ou na página oficial do projeto; os casos mistos estão explicados na ficha ([exemplo: tldraw](https://github.com/tldraw/tldraw/blob/main/LICENSE.md); [exemplo: Remotion](https://github.com/remotion-dev/remotion/blob/main/LICENSE.md)).
- Projetos sem release no GitHub foram registrados com a última tag disponível ou com a indicação explícita de ausência; não houve conversão de tag em release ([exemplo: GSAP, tag 3.15.0](https://github.com/greensock/GSAP/tags)).
- As páginas oficiais citadas foram abertas em 19/10/2026; links de demonstração e galeria só entraram quando responderam HTTP 200 na verificação ([exemplo: galeria do Remotion](https://www.remotion.dev/showcase)).
- Os links `api.github.com` usados como fonte podem retornar 403 em acesso anônimo por limite de taxa; os valores foram coletados com autenticação e permanecem válidos para o horário registrado.

### Inferences

- Comparar estrelas entre categorias diferentes é enganoso. Excalidraw, Manim e reveal.js acumulam público muito maior que ferramentas de nicho com qualidade equivalente, como D2 ou VHS.
- O número de issues abertas isolado não mede saúde. Mermaid, Excalidraw e reveal.js têm milhares de issues e PRs abertos e, ao mesmo tempo, releases recentes e atividade diária; já projetos pequenos podem ter poucas issues por baixa exposição, não por estabilidade.
- A proximidade entre `pushed_at` e a data da coleta é o sinal mais simples de atividade, mas não distingue manutenção de correção pontual. Releases e tags ajudam a separar os dois casos.

### Gaps

- Não foi possível obter números confiáveis de downloads, instalações ou uso real para todos os projetos. O npm não foi consultado de forma sistemática, e vários projetos são usados por CDN ou cópia direta.
- Não foi encontrado um comparativo quantitativo recente e independente sobre essas ferramentas em Hacker News, Reddit ou blogs de design. A evidência usada é primária (repositórios, documentação e sites oficiais), com uma exceção: o fork comunitário do Motion Canvas, que documenta o estado do projeto original.
- Preços de licenças comerciais de tldraw e Remotion não foram cotados; as fichas registram apenas o critério de elegibilidade publicado pelos projetos.
- O draw.io no GitHub é uma versão de teste do produto, não o repositório de desenvolvimento principal; as estrelas não representam a base instalada ([README do draw.io](https://github.com/jgraph/drawio#readme)).

## 2. Fichas por projeto

### 2.1. Diagramas e whiteboards

#### Excalidraw

[Repositório](https://github.com/excalidraw/excalidraw) · [Site](https://excalidraw.com) · [Bibliotecas de formas](https://libraries.excalidraw.com)

134.161 estrelas, 15.731 forks, 3.339 issues/PRs abertos, licença MIT, release v0.18.1 em 21/04/2026, último push em 19/10/2026 ([API](https://api.github.com/repos/excalidraw/excalidraw)).

Um whiteboard infinito de código aberto com estética de desenho à mão, o Excalidraw tem versão web que aceita colaboração em tempo real com criptografia ponta a ponta, links somente leitura e salvamento local; o pacote npm `@excalidraw/excalidraw` embute o editor em aplicações React, mas o README avisa que colaboração e links compartilháveis ainda não acompanham o pacote por padrão ([README](https://github.com/excalidraw/excalidraw#readme)). Para uma apresentação, serve para diagramas de arquitetura, wireframes, mapas mentais e anotações sobre screenshots, com exportação em PNG, SVG, área de transferência ou JSON `.excalidraw` ([README](https://github.com/excalidraw/excalidraw#readme)).

O impacto visual vem do traço irregular e das cores chapadas, que diferenciam o slide de um diagrama corporativo genérico. A biblioteca de formas e a possibilidade de importar desenhos prontos reduzem o tempo de produção. A curva de aprendizado é baixa para desenhar e média para embutir o editor em um produto, porque a integração exige React e controle do estado do canvas.

A limitação concreta é a precisão: não é um editor vetorial, não tem o rigor de alinhamento do draw.io e pode ficar visualmente poluído em diagramas grandes. O projeto é muito ativo, com comunidade ampla, mas o volume de issues e PRs abertos indica fila de manutenção. Ideal para rascunhos e diagramas explicativos com personalidade; menos indicado para diagramas normativos ou densos.

#### tldraw

[Repositório](https://github.com/tldraw/tldraw) · [Site](https://tldraw.dev) · [Aplicativo](https://tldraw.com) · [Galeria](https://tldraw.dev/showcase)

50.984 estrelas, 3.573 forks, 565 issues/PRs abertos, licença própria (source-available), release v5.5.2 em 02/10/2026, último push em 19/10/2026 ([API](https://api.github.com/repos/tldraw/tldraw)).

O tldraw entrega um SDK de canvas infinito para React, não apenas um whiteboard. A biblioteca entrega formas geométricas, texto rico, setas com snap, caneta sensível à pressão, imagens, vídeo, embeds de sites e exportação de imagens; a camada de colaboração `@tldraw/sync` é auto-hospedável, e o SDK permite criar formas, ferramentas, bindings e componentes de interface próprios ([README](https://github.com/tldraw/tldraw#readme)). Em uma apresentação, o uso mais direto é o aplicativo de whiteboard; o uso mais ambicioso é construir uma ferramenta de diagramação ou um canvas interativo para acompanhar a fala.

O acabamento é o principal diferencial: o tldraw tem interações mais polidas que a maioria dos whiteboards abertos e um modelo de dados pensado para aplicações, não só para desenhar. Isso permite diagramas com embeds, conteúdo multimídia e comportamento customizado, algo difícil de replicar no Excalidraw.

A licença é a limitação decisiva. O código é disponibilizado, mas o uso em produção exige uma chave de licença: o modo padrão permite apenas desenvolvimento; há trial de 100 dias, licença comercial paga e licença hobby para projetos não comerciais, esta última mantendo a marca "made with tldraw" no canvas ([página de licença](https://tldraw.dev/community/license)). Para um deck público ou um produto comercial, isso precisa entrar no orçamento. A curva é média a alta, por causa dos conceitos de editor, shapes e bindings. O projeto é muito ativo, com releases frequentes e clientes grandes citados no README. Ideal para quem vai construir um produto sobre o canvas; para uma apresentação isolada, o Excalidraw resolve com licença MIT e menos cerimônia.

#### Mermaid

[Repositório](https://github.com/mermaid-js/mermaid) · [Site e documentação](https://mermaid.js.org) · [Editor](https://mermaid.live)

90.748 estrelas, 9.363 forks, 1.920 issues/PRs abertos, licença MIT, versão 12.2.0 em 13/10/2026, último push em 19/10/2026 ([API](https://api.github.com/repos/mermaid-js/mermaid)).

Uma ferramenta JavaScript que transforma texto em diagramas e gráficos, o Mermaid usa sintaxe inspirada em Markdown e renderiza em SVG ([documentação](https://mermaid.js.org/intro/)). A versão atual cobre mais de vinte tipos, entre fluxograma, sequência, classes, estados, entidade-relacionamento, Gantt, linha do tempo, mapa mental, quadrantes, Sankey, gráfico XY, blocos, pacotes, kanban, arquitetura, radar, treemap, Venn, Ishikawa, Wardley, Cynefin e TreeView ([índice de sintaxe](https://mermaid.js.org/intro/)).

Em slides, o ganho está na combinação de versionamento e consistência: o diagrama fica no Markdown, evolui com o código e é renderizado no tema da apresentação. Slidev, GitHub, GitLab e vários editores já integram Mermaid, o que reduz o atrito ([integrações](https://mermaid.js.org/ecosystem/integrations-community.html)). O impacto visual é bom para diagramas limpos e técnicos, mas o layout automático impõe limites: diagramas complexos exigem ajuste de direção, subgrafos e temas, e às vezes o resultado nunca fica exatamente como o autor imaginou.

A curva é baixa para o básico e média para temas, ícones e layouts. A manutenção é intensa, com releases frequentes e quase duas mil issues/PRs abertas. Há uma limitação de segurança relevante: conteúdo fornecido por terceiros deve ser sanitizado ou renderizado em iframe sandbox, porque a sintaxe aceita muitos caracteres de HTML ([segurança](https://mermaid.js.org/intro/#security-and-safe-diagrams)). Ideal para arquitetura, processos, sequências e cronogramas em decks técnicos; pouco indicado para diagramas com posicionamento milimétrico.

#### draw.io / diagrams.net

[Repositório](https://github.com/jgraph/drawio) · [Site](https://www.drawio.com) · [Aplicativo](https://app.diagrams.net)

8.866 estrelas, 1.327 forks, 31 issues/PRs abertos, licença Apache-2.0 com restrições para bibliotecas de ícones, release v32.5.5 em 18/10/2026, último push em 18/10/2026 ([API](https://api.github.com/repos/jgraph/drawio)).

O draw.io é um aplicativo de diagramação e whiteboard configurável, com versões web e desktop, além de integrações corporativas. O repositório é explicitamente uma versão de teste para avaliação, o produto de produção é pago, pull requests não são aceitos e esta versão não tem edição colaborativa em tempo real ([README](https://github.com/jgraph/drawio#readme)). A base de formas é enorme: UML, BPMN, redes, AWS, Azure, GCP, Kubernetes, fluxogramas e ícones diversos, com exportação em PNG e SVG.

Para apresentações, é a opção mais madura quando o diagrama precisa ser preciso e denso, com conectores que não se cruzam e alinhamento fino. O impacto é o de um diagrama profissional, não de um rascunho. O custo está na interface pesada e na ausência de colaboração em tempo real, o que obriga a trabalhar com arquivos e versões. A curva é média para quem já usou ferramentas de diagramação e alta para dominar atalhos e estilos.

A licença Apache-2.0 vale para o código, mas o README acrescenta uma restrição às bibliotecas de ícones e stencils: elas não podem ser usadas como ativos em produtos Atlassian nem distribuídas no marketplace sem permissão escrita ([README](https://github.com/jgraph/drawio#readme)). Para um deck, isso não afeta o diagrama exportado; para um produto, afeta. As 8,8 mil estrelas não representam a adoção real, porque o repositório é espelho de teste. Ideal para diagramas técnicos complexos e apresentações corporativas; menos indicado para colaboração ao vivo.

#### D2

[Repositório](https://github.com/d2lang/d2) · [Site](https://d2lang.com) · [Playground](https://play.d2lang.com)

25.654 estrelas, 769 forks, 537 issues/PRs abertos, licença MPL-2.0, release v0.9.0 em 07/09/2026, último push em 11/10/2026 ([API](https://api.github.com/repos/d2lang/d2)).

Uma linguagem de script de diagramas, o D2 converte texto em diagramas e oferece temas, fontes, motores de layout e ferramentas de linguagem ([README](https://github.com/d2lang/d2#readme)). O diferencial em relação ao Mermaid é o esforço explícito em estética: temas prontos, controle de estilo por elemento e layouts alternativos, incluindo Dagre, ELK e TALA. Em uma apresentação, produz diagramas de arquitetura e fluxo com aparência mais autoral que o padrão do Graphviz ou do Mermaid.

O impacto visual é alto para quem aceita aprender a linguagem e ajustar layout. O custo é a imaturidade relativa: versão 0.9.0, ecossistema menor e menos integrações prontas que Mermaid. A curva é média, com sintaxe simples mas muitas opções de estilo. Ideal para diagramas de arquitetura e sistemas em que a aparência importa; menos indicado para quem precisa de edição visual imediata.

#### PlantUML

[Repositório](https://github.com/plantuml/plantuml) · [Site](https://plantuml.com)

13.373 estrelas, 1.238 forks, 591 issues/PRs abertos, licença LGPL-3.0, release v1.2026.9 em 17/10/2026, último push em 18/10/2026 ([API](https://api.github.com/repos/plantuml/plantuml)).

Um gerador de diagramas baseado em texto, escrito em Java, o PlantUML tem um catálogo muito amplo: UML, sequência, atividade, componentes, implantação, estados, tempo, mapas mentais, WBS, ArchiMate, C4, redes e interfaces. Para slides de engenharia, resolve diagramas de sequência e UML com precisão e sintaxe compacta.

O impacto visual é funcional, não sofisticado: o padrão é reconhecível e um pouco datado, embora temas e estilos possam melhorar o resultado. A curva é média, com dependência de Java e particularidades de sintaxe. É a escolha certa quando o conteúdo é UML e a prioridade é clareza normativa; menos indicada quando o slide precisa de aparência editorial.

#### diagrams (mingrammer)

[Repositório](https://github.com/mingrammer/diagrams) · [Site](https://diagrams.mingrammer.com)

42.742 estrelas, 2.734 forks, 399 issues/PRs abertos, licença MIT, release v0.25.1 em 22/11/2025, último push em 17/10/2026 ([API](https://api.github.com/repos/mingrammer/diagrams)).

Uma DSL em Python para desenhar arquiteturas de sistemas e nuvem, o diagrams usa ícones de provedores e Graphviz por baixo ([documentação](https://diagrams.mingrammer.com)). Em apresentações técnicas, permite gerar diagramas de AWS, Azure, GCP, Kubernetes e on-premise a partir de código, com consistência entre slides e documentação.

O impacto é profissional e imediatamente reconhecível para plateias de infraestrutura. A limitação é o Graphviz: o layout às vezes resiste, e o diagrama pode ficar denso demais. A curva é média, com Python e noções de Graphviz. Ideal para talks de arquitetura e cloud; menos indicado para diagramas conceituais leves.

#### nomnoml

[Repositório](https://github.com/skanaar/nomnoml) · [Site](https://www.nomnoml.com)

2.837 estrelas, 210 forks, 16 issues/PRs abertos, licença MIT, release v1.7.0 em 14/12/2024, último push em 19/08/2026 ([API](https://api.github.com/repos/skanaar/nomnoml)).

Um editor de diagramas por texto com estilo limpo e levemente desenhado à mão, o nomnoml serve para UML e fluxos rápidos, com exportação SVG. O impacto visual é modesto, mas agradável para rascunhos em slides. A limitação é o ecossistema pequeno e a atividade baixa; não é uma aposta para integrações críticas.

### 2.2. Animação e vídeo

#### Motion Canvas

[Repositório](https://github.com/motion-canvas/motion-canvas) · [Site](https://motion-canvas.io) · [Exemplos](https://github.com/motion-canvas/examples)

19.391 estrelas, 848 forks, 175 issues/PRs abertos, licença MIT, release estável v3.17.2 em 14/12/2024, último push em 02/07/2026 ([API](https://api.github.com/repos/motion-canvas/motion-canvas)).

Uma biblioteca TypeScript com editor, o Motion Canvas usa funções geradoras para descrever animações quadro a quadro, com pré-visualização em tempo real e sincronização com narração ([README](https://github.com/motion-canvas/motion-canvas#readme)). Em apresentações, serve para explicadores técnicos, diagramas animados, aberturas e sequências de código, com timing definido por código em vez de keyframes.

O impacto visual é alto para animação vetorial precisa: o autor controla duração, velocidade e aceleração de cada etapa, e o resultado tem aparência de motion graphics, não de slide animado. A curva é média a alta, porque exige TypeScript, geradores e o modelo de cenas.

O sinal de manutenção é o ponto crítico. A última release estável é de dezembro de 2024; houve apenas uma alpha 3.18.0 em fevereiro de 2025. Um fork comunitário, Canvas Commons, declara que o Motion Canvas "hasn't had updates in a while" (não recebe atualizações há um tempo) e que os mantenedores atuais não têm permissão de push nem de release no repositório original ([README do fork](https://github.com/canvas-commons/.github)). O fork tem 260 estrelas, licença MIT e atividade em outubro de 2026 ([API](https://api.github.com/repos/canvas-commons/canvas-commons)). Para trabalho novo, o Motion Canvas é um protótipo de alto potencial, não uma base sem risco; acompanhar o Canvas Commons é a alternativa.

#### Remotion

[Repositório](https://github.com/remotion-dev/remotion) · [Site](https://www.remotion.dev) · [Galeria](https://www.remotion.dev/showcase)

65.213 estrelas, 5.185 forks, 191 issues/PRs abertos, licença própria (Remotion License), release v4.0.536 em 16/10/2026, último push em 19/10/2026 ([API](https://api.github.com/repos/remotion-dev/remotion)).

Com Remotion, o vídeo é uma composição React e TypeScript. O preview roda no Player/Studio e a renderização gera MP4; a biblioteca cobre renderização em lote, Lambda, renderização no cliente e aplicações de edição ([README](https://github.com/remotion-dev/remotion#readme)). O pacote `@remotion/transitions` traz apresentações prontas para transições entre cenas, incluindo fade, slide, wipe, flip, clockWipe, iris, zoomBlur, ripple, crosswarp, crossZoom, cube e outras, além de transições customizadas ([documentação](https://www.remotion.dev/docs/transitions/presentations)).

Para slides, o uso mais produtivo é video-first: abertura, cortes animados, gráficos data-driven, versões em vídeo de um deck e sequências para redes sociais. Também é possível construir o deck inteiro como composição React e exportar vídeo, mas isso troca a interatividade de um reveal.js ou Slidev por um arquivo renderizado. O impacto é alto: pixel perfect, reproduzível, com CSS, SVG e WebGL disponíveis.

A licença não é OSI. O uso é gratuito para indivíduos, organizações com até três funcionários, organizações sem fins lucrativos e avaliação; empresas maiores precisam de licença comercial ([LICENSE](https://github.com/remotion-dev/remotion/blob/main/LICENSE.md)). A curva é média a alta, com React, timing em frames e pipeline de render. A manutenção é intensa, com releases muito frequentes. Ideal para vídeo e motion design programático; menos indicado para uma palestra ao vivo.

#### Manim (3b1b)

[Repositório](https://github.com/3b1b/manim) · [Documentação](https://3b1b.github.io/manim/) · [Vídeos do 3Blue1Brown](https://www.3blue1brown.com)

95.341 estrelas, 7.815 forks, 505 issues/PRs abertos, licença MIT, release v1.7.2 em 13/12/2024, último push em 09/09/2026 ([API](https://api.github.com/repos/3b1b/manim)).

Criado por Grant Sanderson, do 3Blue1Brown, o Manim é um motor de animação programática para vídeos explicativos de matemática. O pacote é o ManimGL, instalado como `manimgl`, e exige Python 3.10 ou superior, FFmpeg, OpenGL e, opcionalmente, LaTeX ([README](https://github.com/3b1b/manim#readme)). Em slides, produz transformações geométricas, provas visuais, algoritmos e animações de equações com precisão matemática.

O impacto é difícil de igualar em conteúdo matemático: as transformações são suaves, o LaTeX é nativo e o resultado tem a assinatura visual do 3Blue1Brown. A curva é alta, com cenas, mobjects, updaters e renderização. A manutenção é irregular: o último release é de 2024, embora haja pushes em 2026. A limitação é ser um projeto pessoal, com documentação menos amigável que a da versão comunitária. Ideal para divulgação científica e aulas; menos indicado para quem quer começar hoje sem apoio da comunidade.

#### Manim Community

[Repositório](https://github.com/ManimCommunity/manim) · [Site](https://www.manim.community) · [Galeria de exemplos](https://docs.manim.community/en/stable/examples.html)

41.677 estrelas, 3.209 forks, 499 issues/PRs abertos, licença MIT, release v0.22.0 em 08/10/2026, último push em 16/10/2026 ([API](https://api.github.com/repos/ManimCommunity/manim)).

O Manim Community é o fork comunitário do Manim, mantido com foco em estabilidade, testes, documentação e resposta a contribuições. O próprio README recomenda esta versão para desenvolvimento continuado e para quem está começando, reservando o repositório do 3b1b para estudar como os vídeos originais são feitos ([README](https://github.com/ManimCommunity/manim#readme)). A galeria oficial mostra o tipo de resultado: geometria, cálculo, álgebra linear, gráficos e animações de código.

O impacto visual é o mesmo universo do Manim, com onboarding melhor. A curva continua alta, porque o autor precisa pensar em cenas, objetos e transformações, e o ambiente exige FFmpeg, LaTeX e dependências de sistema. A manutenção é a mais saudável das duas versões, com release em outubro de 2026 e atividade semanal. Ideal para aulas, vídeos de matemática e visualizações científicas; menos indicado para animações de marketing.

#### GSAP

[Repositório](https://github.com/greensock/GSAP) · [Site](https://gsap.com) · [Galeria](https://gsap.com/showcase)

29.467 estrelas, 2.275 forks, 7 issues/PRs abertos, licença própria (GSAP Standard License), tag 3.15.0, sem release no GitHub, último push em 13/04/2026 ([API](https://api.github.com/repos/greensock/GSAP)).

Uma biblioteca JavaScript de animação independente de framework, o GSAP tem timeline, easing e plugins para SVG, canvas, WebGL, texto e scroll. Os plugins incluem ScrollTrigger, SplitText, MorphSVG, Flip, MotionPath, Draggable e Observer ([README](https://github.com/greensock/GSAP#readme)). Em slides web, serve para tipografia cinética, revelações por etapa, morphing de SVG e animações disparadas pela navegação, integrando com reveal.js e Slidev.

O impacto é de padrão de mercado: o motor é rápido, o controle de timeline é preciso e o resultado é fluido em navegadores. A curva é média, com o modelo de timeline e o registro de plugins. A licença mudou o jogo: desde 30/04/2025, o GSAP é gratuito para uso comercial, incluindo os antigos plugins pagos, sob a licença padrão da Webflow ([anúncio](https://webflow.com/blog/gsap-becomes-free); [licença](https://gsap.com/licensing)). A limitação é não ser um framework de slides e o risco de excesso de movimento. A atividade no GitHub é baixa em comparação com a importância, mas o projeto é mantido pela equipe original dentro da Webflow. Ideal para decks web com motion design autoral.

#### anime.js

[Repositório](https://github.com/juliangarnier/anime) · [Site](https://animejs.com)

73.704 estrelas, 4.979 forks, 124 issues/PRs abertos, licença MIT, release v4.5.0 em 22/06/2026, último push em 21/08/2026 ([API](https://api.github.com/repos/juliangarnier/anime)).

Um motor de animação JavaScript leve, o anime.js chegou à versão 4 com a API reorganizada e recursos como timeline, stagger, animação de layout, SVG com morph e desenho, divisão e scramble de texto, sincronização com a Web Animations API, draggable e adaptador para Three.js ([documentação](https://animejs.com/documentation/)). Em slides, funciona bem para microinterações, revelação de texto, diagramas SVG e gráficos animados sem a complexidade de uma timeline de vídeo.

O impacto é elegante e econômico: poucas linhas produzem movimento com boa sensação, e a licença MIT elimina preocupação comercial. A curva é baixa a média. A limitação é o ecossistema menor que o do GSAP e menos recursos para sequências muito longas ou efeitos dependentes de plugins. A documentação da v4 ainda está amadurecendo. Ideal para decks web enxutos e para quem quer animar sem carregar um framework grande.

#### Motion (Framer Motion)

[Repositório](https://github.com/motiondivision/motion) · [Site](https://motion.dev)

34.348 estrelas, 1.444 forks, 42 issues/PRs abertos, licença MIT, tag v14.4.0, sem release no GitHub, último push em 19/10/2026 ([API](https://api.github.com/repos/motiondivision/motion)).

Pensado para React, o Motion é uma das bibliotecas de animação de interface mais usadas, com animações de layout, gestos, molas e transições de entrada e saída. Em um deck React, resolve transições entre componentes e microinterações com pouco código. O impacto é o de interface polida, não de motion graphics. A limitação é o foco em React e em UI, com menos controle de timeline que GSAP ou anime.js.

#### Lottie

[Repositório](https://github.com/airbnb/lottie-web) · [Site](https://airbnb.io/lottie)

32.251 estrelas, 2.948 forks, 858 issues/PRs abertos, licença MIT, tag v5.13.0, sem release no GitHub, último push em 01/09/2025 ([API](https://api.github.com/repos/airbnb/lottie-web)).

Um player de animações exportadas do After Effects em JSON, o Lottie permite usar animações vetoriais feitas por designers sem vídeo pesado, com boa qualidade em diferentes resoluções. O impacto depende do arquivo de origem: bem feito, parece motion design; mal feito, vira enfeite. A limitação é a dependência do After Effects e das diferenças de renderização entre players. A atividade está em manutenção, com último push em 2025.

#### three.js

[Repositório](https://github.com/mrdoob/three.js) · [Site](https://threejs.org)

116.621 estrelas, 36.688 forks, 392 issues/PRs abertos, licença MIT, release r186 em 24/09/2026, último push em 19/10/2026 ([API](https://api.github.com/repos/mrdoob/three.js)).

Para 3D no navegador, three.js é a biblioteca de referência. Em slides, permite cenas 3D, produtos, dados espaciais e fundos animados com impacto alto. O custo é alto: WebGL, shaders, performance e acessibilidade. A curva é alta e o peso no deck é grande. Ideal para uma abertura ou um momento específico, não para o deck inteiro.

#### p5.js

[Repositório](https://github.com/processing/p5.js) · [Site](https://p5js.org)

24.142 estrelas, 3.873 forks, 541 issues/PRs abertos, licença LGPL-2.1, release v2.3.4 em 25/09/2026, último push em 17/10/2026 ([API](https://api.github.com/repos/processing/p5.js)).

Programação criativa em canvas, com sintaxe acessível e foco em arte generativa, é a proposta do p5.js. Em apresentações, serve para visualizações generativas, fundos e demonstrações ao vivo. O impacto é experimental e visualmente distinto. A limitação é a licença LGPL e o fato de exigir código para produzir o visual; não é uma ferramenta de layout.

#### rough-notation

[Repositório](https://github.com/rough-stuff/rough-notation) · [Site](https://roughnotation.com)

9.715 estrelas, 239 forks, 33 issues/PRs abertos, licença MIT, sem release no GitHub, último push em 18/03/2024 ([API](https://api.github.com/repos/rough-stuff/rough-notation)).

Uma biblioteca pequena, rough-notation desenha círculos, sublinhados, caixas e riscos à mão sobre texto e elementos HTML, com animação de entrada. Em slides, é excelente para destacar uma frase ou um número com humor visual, sem editar imagem. O impacto é o de anotação feita na hora. A limitação é o escopo estreito e a falta de atividade recente; para um efeito simples, continua útil.

#### tsParticles

[Repositório](https://github.com/tsparticles/tsparticles) · [Site](https://particles.js.org)

8.994 estrelas, 945 forks, 23 issues/PRs abertos, licença MIT, release v4.4.0 em 31/08/2026, último push em 19/10/2026 ([API](https://api.github.com/repos/tsparticles/tsparticles)).

Um motor de partículas para fundos e efeitos, tsParticles pode criar um fundo animado para uma capa ou uma transição, mas o uso indiscriminado distrai e pesa. A curva é baixa; a limitação é estética e de performance. Serve como tempero, não como estrutura.

### 2.3. Frameworks de slides, temas e coleções

Os frameworks web e Markdown são tratados em profundidade na nota 1 desta série. Aqui o recorte é o que cada um oferece em recursos visuais, temas e animação.

#### Slidev

[Repositório](https://github.com/slidevjs/slidev) · [Site](https://sli.dev) · [Galeria de temas](https://sli.dev/resources/theme-gallery)

49.127 estrelas, 2.229 forks, 237 issues/PRs abertos, licença MIT, release v53.0.0 em 16/09/2026, último push em 18/10/2026 ([API](https://api.github.com/repos/slidevjs/slidev)).

Feito para quem programa: Markdown, componentes Vue, UnoCSS, destaque de código, LaTeX, Mermaid, ícones, modo apresentador, desenho sobre os slides, gravação e exportação para PDF, PNG e PPTX ([README](https://github.com/slidevjs/slidev#readme)). O impacto visual vem dos temas npm e da liberdade de embutir componentes Vue, o que permite animações sob medida com GSAP, anime.js ou Motion. A curva é média, com Node 22.12 ou superior e noções de Vue. A limitação é o ecossistema Node e a exportação para PPTX não ser pixel perfect. A galeria oficial de temas é o melhor ponto de partida para um visual de alto padrão.

#### reveal.js

[Repositório](https://github.com/hakimel/reveal.js) · [Site](https://revealjs.com) · [Demo](https://revealjs.com/demo/)

72.441 estrelas, 17.023 forks, 928 issues/PRs abertos, licença MIT, release 6.0.2 em 10/09/2026, último push em 30/09/2026 ([API](https://api.github.com/repos/hakimel/reveal.js)).

O reveal.js é o framework HTML de apresentações mais conhecido, com slides aninhados, Markdown, Auto-Animate, exportação para PDF, notas do apresentador, LaTeX, destaque de código e API ([README](https://github.com/hakimel/reveal.js#readme)). O impacto visual é totalmente controlável por CSS, e o Auto-Animate permite transições suaves entre layouts sem código de animação. Os temas embutidos mudam o visual sem CSS adicional, e o catálogo oficial fica em [revealjs.com/themes](https://revealjs.com/themes/). A curva é média para HTML/CSS e alta para temas realmente autorais. A limitação é a idade do modelo: não há editor visual embutido, e a customização exige disciplina de CSS. A demo oficial mostra o potencial e também o estilo padrão que muita gente reconhece.

#### Marp

[Repositório](https://github.com/marp-team/marp) · [Site](https://marp.app) · [CLI](https://github.com/marp-team/marp-cli)

12.656 estrelas, 302 forks, 1 issue/PR aberto, licença MIT, sem release no repositório principal, CLI v4.5.1 em 06/09/2026, último push em 29/07/2026 ([API](https://api.github.com/repos/marp-team/marp)).

Um ecossistema Markdown para slides, o Marp tem CLI que converte para HTML, PDF, PPTX e imagens, além da extensão de VS Code ([README](https://github.com/marp-team/marp#readme)). O visual é mais simples que o de Slidev ou reveal.js, com temas embutidos e CSS customizável. O impacto é a velocidade de produção e a consistência, não o motion design. A limitação é o repositório principal ser uma porta de entrada, com o desenvolvimento distribuído em vários pacotes; para temas e recursos, é preciso olhar o Marp Core e a lista oficial.

#### Quarto

[Repositório](https://github.com/quarto-dev/quarto-cli) · [Site](https://quarto.org) · [Apresentações](https://quarto.org/docs/presentations/)

6.099 estrelas, 471 forks, 1.905 issues/PRs abertos, licença MIT, release v1.10.19 em 06/10/2026, último push em 19/10/2026 ([API](https://api.github.com/repos/quarto-dev/quarto-cli)).

Baseado em Pandoc, o Quarto é um sistema de publicação científica com apresentações em reveal.js, Beamer e PowerPoint, execução de código Python, R, Julia e JavaScript, referências cruzadas, painéis e callouts ([README](https://github.com/quarto-dev/quarto-cli#readme)). O impacto visual depende do formato escolhido: reveal.js para web, Beamer para PDF acadêmico. A curva é média, com Markdown e YAML, mas o toolchain é pesado e a fila de issues é grande. Ideal para talks com dados e código reproduzível; menos indicado para design autoral.

#### Beamer e Metropolis (mtheme)

[Repositório](https://github.com/matze/mtheme) · [Página no CTAN](https://ctan.org/pkg/beamertheme-metropolis)

6.906 estrelas, 859 forks, 91 issues/PRs abertos, licença CC BY-SA 4.0, release v1.2 em 23/01/2017, último push em 23/11/2022 ([API](https://api.github.com/repos/matze/mtheme)).

O Metropolis é um tema Beamer minimalista, com tipografia limpa, bastante espaço em branco e uma barra de progresso opcional ([README](https://github.com/matze/mtheme#readme)). Em apresentações acadêmicas em PDF, resolve o visual com elegância e é fácil de instalar via CTAN. O impacto é o de um deck sóbrio e legível, sem os enfeites do Beamer padrão. A limitação é a idade: últimos release em 2017 e push em 2022, sem desenvolvimento ativo. A licença CC BY-SA 4.0 exige compartilhar adaptações sob a mesma licença. Para um visual mais atual em PDF, vale comparar com Touying/Polylux no Typst, cobertos na nota 2.

#### PPTist

[Repositório](https://github.com/pipipi-pikachu/PPTist) · [Demo](https://pipipi-pikachu.github.io/PPTist/)

9.409 estrelas, 1.772 forks, 21 issues/PRs abertos, licença AGPL-3.0, sem releases ou tags no GitHub, último push em 10/10/2026 ([API](https://api.github.com/repos/pipipi-pikachu/PPTist)).

Um editor de apresentações web, o PPTist replica boa parte do PowerPoint: texto, imagens, formas, linhas, gráficos, tabelas, vídeo, áudio e fórmulas, com importação e exportação de PPTX ([README](https://github.com/pipipi-pikachu/PPTist#readme)). O próprio projeto é honesto sobre o escopo: a fidelidade de importação de PPTX fica em torno de 85%, e a recomendação principal é usar o PPTist como base para um produto de edição web, não como ferramenta pronta ([README](https://github.com/pipipi-pikachu/PPTist#readme)). Para uma apresentação, o valor está em templates e na edição visual; para um produto, a AGPL-3.0 impõe obrigações fortes. A curva é média para usar e alta para estender.

#### impress.js, Spectacle e WebSlides

[impress.js](https://github.com/impress/impress.js) tem 38.155 estrelas, 6.567 forks, 61 issues/PRs, licença MIT, release v2.0.0 em 22/07/2022 e push em 23/07/2026; é conhecido pelas transições 3D em CSS, com impacto alto e manutenção estagnada ([API](https://api.github.com/repos/impress/impress.js)). [Spectacle](https://github.com/FormidableLabs/spectacle) tem 10.181 estrelas, 701 forks, 83 issues/PRs, licença MIT, release 10.2.3 em 10/10/2025 e push em 17/10/2026; é uma biblioteca React com temas e modo apresentador ([API](https://api.github.com/repos/FormidableLabs/spectacle)). [WebSlides](https://github.com/webslides/WebSlides) tem 6.327 estrelas, 585 forks, 82 issues/PRs, licença MIT, release 1.5.0 em 16/09/2017 e push em 10/12/2022; é um framework HTML/CSS semântico, visualmente correto e sem manutenção relevante ([API](https://api.github.com/repos/webslides/WebSlides)). Nenhum dos três é a primeira escolha em 2026, mas o Spectacle ainda serve para decks React e o impress.js continua útil para um efeito 3D específico.

#### Listas e coleções

[matteofigus/awesome-speaking](https://github.com/matteofigus/awesome-speaking) reúne 1.997 estrelas, 615 forks e 6 issues/PRs, licença MIT, último push em 11/09/2026; cobre técnica de fala e preparação, não templates ([API](https://api.github.com/repos/matteofigus/awesome-speaking)).

[martinbjeldbak/ultimate-beamer-theme-list](https://github.com/martinbjeldbak/ultimate-beamer-theme-list) tem 1.824 estrelas, 138 forks e 2 issues/PRs, sem licença declarada, último push em 19/10/2026; é a lista mais ampla de temas Beamer da comunidade, mas a ausência de licença impede reutilização do conteúdo sem contato com o autor ([API](https://api.github.com/repos/martinbjeldbak/ultimate-beamer-theme-list)).

[favourhong/Awesome-Marp](https://github.com/favourhong/Awesome-Marp) tem 1.053 estrelas, 116 forks e 41 issues/PRs, sem licença declarada, último push em 21/08/2026; é um ecossistema de temas Marp, com boa variedade visual, mas o mesmo problema de licença ([API](https://api.github.com/repos/favourhong/Awesome-Marp)).

[marp-team/awesome-marp](https://github.com/marp-team/awesome-marp) tem 523 estrelas, 15 forks e nenhuma issue/PR, licença CC0-1.0, último push em 25/04/2026; é a lista oficial e a mais segura para descobrir recursos Marp ([API](https://api.github.com/repos/marp-team/awesome-marp)).

[slidevjs/themes](https://github.com/slidevjs/themes) tem 221 estrelas, 122 forks e 5 issues/PRs, licença MIT, último push em 29/07/2025; reúne os temas oficiais do Slidev e é o caminho mais direto para um deck com aparência profissional ([API](https://api.github.com/repos/slidevjs/themes)).

[xinychen/awesome-beamer](https://github.com/xinychen/awesome-beamer) tem 123 estrelas, 25 forks e nenhuma issue/PR, licença MIT, último push em 27/09/2023; está parado e serve apenas como arquivo ([API](https://api.github.com/repos/xinychen/awesome-beamer)).

[pmichaillat/latex-presentation](https://github.com/pmichaillat/latex-presentation) tem 299 estrelas, 78 forks e nenhuma issue/PR, licença MIT, último push em 14/10/2026; é um template acadêmico minimalista, ativo e fácil de adaptar ([API](https://api.github.com/repos/pmichaillat/latex-presentation)).

A busca não encontrou uma lista "awesome presentations" com a mesma autoridade das listas de outras áreas. A curadoria mais útil está dentro dos ecossistemas: temas oficiais do Slidev, lista oficial do Marp e a lista de temas Beamer. Para templates de alto padrão, o caminho é combinar um framework (Slidev ou reveal.js), um tema bem mantido e recursos visuais próprios, em vez de procurar um repositório único com "os melhores slides".

### 2.4. Ícones e tipografia

#### Lucide

[Repositório](https://github.com/lucide-icons/lucide) · [Site](https://lucide.dev) · [Ícones](https://lucide.dev/icons)

25.143 estrelas, 1.649 forks, 423 issues/PRs abertos, licença ISC, release 1.59.0 em 17/10/2026, último push em 19/10/2026 ([API](https://api.github.com/repos/lucide-icons/lucide)).

Uma biblioteca de mais de 1.600 ícones SVG, o Lucide é fork do Feather e mantém traço consistente e pacotes oficiais para React, Vue, Svelte, Angular, Solid e outras stacks, além de plugin para Figma ([README](https://github.com/lucide-icons/lucide#readme)). Em slides, resolve ícones de interface, listas de features e diagramas com um estilo uniforme. O impacto é a coerência: todos os ícones compartilham grid e espessura, o que evita o visual misturado de bibliotecas diferentes.

A curva é baixa, a licença ISC é permissiva e a manutenção é muito ativa. A limitação é o estilo de traço único, que não cobre ícones de marca nem ilustrações; para isso, Simple Icons ou Font Awesome. O catálogo é menor que o do Tabler, mas suficiente para a maioria dos decks.

#### Tabler Icons

[Repositório](https://github.com/tabler/tabler-icons) · [Site](https://tabler.io/icons)

22.369 estrelas, 1.242 forks, 84 issues/PRs abertos, licença MIT, release 3.49.0 em 05/10/2026, último push em 15/10/2026 ([API](https://api.github.com/repos/tabler/tabler-icons)).

Um conjunto de 6.238 ícones SVG, sendo 5.184 em outline e 1.054 em filled, o Tabler é desenhado em grid 24x24 com traço de 2 px ([README](https://github.com/tabler/tabler-icons#readme)). Em apresentações, é a opção mais generosa para grids de features, diagramas técnicos e listas com muitos ícones. O impacto é a variedade com consistência, e a possibilidade de alternar outline e filled no mesmo slide.

A curva é baixa e a licença MIT é simples. A limitação é o estilo: o traço de 2 px e o grid 24x24 impõem uma linguagem visual específica, que pode não combinar com ícones de marca. O conjunto filled é menor que o outline. A manutenção é ativa, com releases frequentes.

#### Font Awesome

[Repositório](https://github.com/FortAwesome/Font-Awesome) · [Site](https://fontawesome.com) · [Ícones](https://fontawesome.com/icons)

76.967 estrelas, 12.157 forks, 322 issues/PRs abertos, licença mista, release 7.3.1 em 15/07/2026, último push em 15/07/2026 ([API](https://api.github.com/repos/FortAwesome/Font-Awesome)).

Uma das bibliotecas de ícones mais conhecidas da web, o Font Awesome tem versão Free e Pro. A licença Free separa três camadas: ícones em SVG e JS sob CC BY 4.0, fontes sob SIL OFL 1.1 e código sob MIT ([LICENSE](https://github.com/FortAwesome/Font-Awesome/blob/master/LICENSE.txt)). Em slides, resolve ícones de marca, redes sociais e símbolos universalmente reconhecíveis. O impacto é a familiaridade, não a sofisticação.

A limitação é a atribuição: os ícones CC BY 4.0 exigem crédito, e muitos ícones e estilos adicionais ficam no Pro. O kit completo é pesado para uma apresentação simples. A curva é baixa. A manutenção é ativa, com release em julho de 2026.

#### Google Fonts

[Repositório](https://github.com/google/fonts) · [Site](https://fonts.google.com)

20.647 estrelas, 2.932 forks, 1.448 issues/PRs abertos, licença por família (majoritariamente OFL 1.1), sem releases, último push em 19/10/2026 ([API](https://api.github.com/repos/google/fonts)).

O Google Fonts é o catálogo de fontes binárias servidas pelo serviço. Cada família tem seu próprio arquivo de licença; a maioria usa SIL Open Font License 1.1, algumas usam Apache 2.0 e as fontes Ubuntu usam a Ubuntu Font License 1.0 ([README](https://github.com/google/fonts#readme)). Em apresentações, é a fonte primária para escolher tipografia sem custo e com ampla cobertura de idiomas.

O impacto depende da curadoria: uma boa dupla de fontes resolve metade da qualidade percebida de um deck. A limitação é a variação de qualidade e a necessidade de conferir a licença de cada família, além do volume de issues, que reflete o tamanho do catálogo, não a saúde de um produto único. Para uso offline e consistente, o Fontsource empacota essas fontes em npm.

#### Simple Icons

[Repositório](https://github.com/simple-icons/simple-icons) · [Site](https://simpleicons.org)

26.036 estrelas, 3.185 forks, 996 issues/PRs abertos, licença CC0-1.0, release 16.35.0 em 11/10/2026, último push em 19/10/2026 ([API](https://api.github.com/repos/simple-icons/simple-icons)).

Reúne logotipos de marcas em SVG, com nomes padronizados. Em slides técnicos, resolve a fileira de logos de tecnologias e produtos com consistência de tamanho e cor. O impacto é a limpeza visual. A limitação é jurídica: a licença CC0 cobre o arquivo do projeto, mas as marcas continuam protegidas por direitos de seus titulares, e o uso deve respeitar as políticas de cada empresa. A manutenção é ativa.

#### Phosphor

[Repositório](https://github.com/phosphor-icons/core) · [Site](https://phosphoricons.com)

393 estrelas no repositório core, 55 forks, 5 issues/PRs, licença MIT, release v2.0.8 em 01/02/2024, último push em 06/01/2026 ([API](https://api.github.com/repos/phosphor-icons/core)).

Uma família de ícones com múltiplos pesos (thin, light, regular, bold, fill e duotone), o Phosphor permite variar a intensidade visual sem trocar de biblioteca. Em slides, funciona bem para ícones grandes e composições com hierarquia. O número de estrelas do repositório core subestima o uso, porque a distribuição principal acontece pelos pacotes web e pelo site. A limitação é a atividade baixa e o catálogo menor que Tabler.

#### Feather

[Repositório](https://github.com/feathericons/feather) · [Site](https://feathericons.com)

26.016 estrelas, 1.283 forks, 507 issues/PRs abertos, licença MIT, release v4.29.2 em 01/05/2024, último push em 11/03/2025 ([API](https://api.github.com/repos/feathericons/feather)).

O Feather é o conjunto minimalista que inspirou o Lucide. Ainda serve para ícones de traço fino, mas está parado desde 2024 e foi superado pelo fork em cobertura e manutenção. Para trabalho novo, o Lucide é a escolha mais direta; o Feather fica como referência histórica ou para projetos legados.

#### Material Icons

[Repositório](https://github.com/google/material-design-icons) · [Site](https://fonts.google.com/icons)

54.130 estrelas, 9.750 forks, 429 issues/PRs abertos, licença Apache-2.0, release 4.0.0 em 31/08/2020, último push em 09/10/2026 ([API](https://api.github.com/repos/google/material-design-icons)).

É a biblioteca oficial do Google Material Design, com milhares de ícones em estilos filled, outlined, rounded, sharp e two-tone. Em slides, é uma opção segura para ícones de produto e interface, com a estética Google. A limitação é o release parado em 2020 e o visual marcadamente Material, que pode não combinar com um deck editorial. A manutenção do repositório continua com pushes em 2026, mas sem release novo.

#### Inter

[Repositório](https://github.com/rsms/inter) · [Site](https://rsms.me/inter)

19.978 estrelas, 487 forks, 148 issues/PRs abertos, licença OFL-1.1, release v4.1 em 16/11/2024, último push em 19/11/2024 ([API](https://api.github.com/repos/rsms/inter)).

É uma fonte sans-serif desenhada para interfaces, com altura-x generosa, bom desempenho em telas e variantes ópticas. Em slides, funciona bem para texto de interface, tabelas e gráficos, e a legibilidade em projeção é boa. O impacto é neutralidade e clareza, não personalidade. A limitação é a baixa atividade do repositório e o fato de ser uma fonte de UI, não uma display para títulos enormes. Para títulos, vale combinar com uma serifada ou uma grotesca de contraste.

#### IBM Plex

[Repositório](https://github.com/IBM/plex) · [Site](https://www.ibm.com/plex)

11.710 estrelas, 627 forks, 85 issues/PRs abertos, licença OFL-1.1, último release em 13/11/2024, último push em 16/10/2026 ([API](https://api.github.com/repos/IBM/plex)).

É uma família corporativa com Sans, Serif, Mono, Condensed e variantes, desenhada para consistência entre produto e comunicação. Em apresentações técnicas, o Plex Sans e o Plex Mono resolvem texto e código com uma identidade sóbria. O impacto é o de um sistema tipográfico completo. A limitação é a associação com a IBM e o tamanho da família, que exige escolha disciplinada.

#### Fontsource

[Repositório](https://github.com/fontsource/fontsource) · [Site](https://fontsource.org)

6.220 estrelas, 195 forks, 41 issues/PRs abertos, licença MIT, release core v0.6.1 em 12/10/2026, último push em 14/10/2026 ([API](https://api.github.com/repos/fontsource/fontsource)).

Empacota fontes open source, incluindo as do Google Fonts, como pacotes npm auto-hospedados. Em apresentações web, garante que a fonte carregue offline e sem depender do CDN do Google, o que evita variação de layout em eventos com rede ruim. O impacto é a consistência tipográfica. A limitação é exigir tooling JavaScript e não ser um recurso de design por si.

### 2.5. Captura, mockup e gravação

#### Carbon

[Repositório](https://github.com/carbon-app/carbon) · [Site](https://carbon.now.sh)

36.117 estrelas, 1.973 forks, 86 issues/PRs abertos, licença MIT, release 4.9.10 em 13/06/2022, último push em 10/02/2026 ([API](https://api.github.com/repos/carbon-app/carbon)).

Transforma trechos de código em imagens com tema, padding, sombra e controles de janela. Em slides técnicos, é a forma mais rápida de exibir código legível sem capturar a tela inteira do editor. O impacto é alto para quem mostra código, com estética limpa e exportação PNG/SVG. A limitação é o release parado em 2022 e o fato de ser uma aplicação web, não uma biblioteca de layout; trechos longos exigem ajuste manual. A manutenção é mínima, mas o produto continua funcionando.

#### VHS

[Repositório](https://github.com/charmbracelet/vhs) · [Site](https://charm.sh/vhs)

21.149 estrelas, 569 forks, 178 issues/PRs abertos, licença MIT, release v0.12.1 em 24/09/2026, último push em 01/10/2026 ([API](https://api.github.com/repos/charmbracelet/vhs)).

Gera GIFs e MP4 de sessões de terminal a partir de um script `.tape`, com controle de digitação, pausas e janela. Em apresentações de CLI, é a maneira reproduzível de mostrar um comando sem gravar a tela e sem depender de velocidade de digitação. O impacto é o de uma demo limpa e repetível. A limitação é o escopo de terminal e as dependências de FFmpeg e ttyd. A manutenção é ativa.

#### shot-scraper

[Repositório](https://github.com/simonw/shot-scraper) · [Site](https://shot-scraper.datasette.io)

2.596 estrelas, 133 forks, 60 issues/PRs abertos, licença Apache-2.0, release 1.12 em 13/09/2026, último push em 14/10/2026 ([API](https://api.github.com/repos/simonw/shot-scraper)).

É uma CLI de captura de páginas web baseada em Playwright, com seletores, página inteira, execução de JavaScript e espera por elementos. Em slides, serve para gerar screenshots consistentes de sites e produtos em viewports definidos. O impacto é a padronização: todas as imagens saem no mesmo tamanho e resolução. A limitação é ser uma ferramenta de linha de comando, não um editor de mockup.

#### Playwright

[Repositório](https://github.com/microsoft/playwright) · [Site](https://playwright.dev)

98.067 estrelas, 6.651 forks, 211 issues/PRs abertos, licença Apache-2.0, release v1.64.1 em 14/10/2026, último push em 19/10/2026 ([API](https://api.github.com/repos/microsoft/playwright)).

É uma das suítes de automação de navegadores mais usadas, com screenshots, emulação de dispositivos, PDF e testes. Em apresentações, resolve capturas de UI em resoluções exatas e em lote, além de permitir roteiros de demo. O impacto é a precisão e a repetibilidade. A limitação é o peso: exige código, navegadores instalados e tempo de execução. Para uma única captura, o shot-scraper é mais direto; para um pipeline, o Playwright é a base.

#### html-to-image

[Repositório](https://github.com/bubkoo/html-to-image) · [Documentação](https://github.com/bubkoo/html-to-image#readme)

7.255 estrelas, 675 forks, 208 issues/PRs abertos, licença MIT, release v1.11.13 em 14/02/2025, último push em 28/05/2026 ([API](https://api.github.com/repos/bubkoo/html-to-image)).

Converte nós DOM em PNG, SVG ou JPEG no navegador. Em um deck web, permite transformar um componente ou gráfico em imagem para exportação, sem passar por servidor. O impacto é a integração com o próprio slide. A limitação é a fidelidade: fontes, imagens externas e CSS complexo podem falhar por CORS ou diferenças de renderização. A manutenção é moderada.

#### Pencil

[Repositório](https://github.com/evolus/pencil) · [Site](https://pencil.evolus.vn)

9.880 estrelas, 792 forks, 531 issues/PRs abertos, licença GPL-2.0, release v3.1.1 em 01/01/2023, último push em 16/10/2026 ([API](https://api.github.com/repos/evolus/pencil)).

É uma ferramenta de wireframe e mockup de código aberto, com stencils e exportação de imagens. Em slides, serve para mostrar telas e fluxos de produto sem abrir o Figma. O impacto é funcional, com aparência de protótipo. A limitação é a idade, a interface datada e a licença GPL-2.0, que pode ser um problema para incorporar em produtos. Para mockups rápidos, o Penpot é mais moderno.

#### Penpot

[Repositório](https://github.com/penpot/penpot) · [Site](https://penpot.app)

61.365 estrelas, 4.254 forks, 861 issues/PRs abertos, licença MPL-2.0, release 2.18.3 em 06/10/2026, último push em 19/10/2026 ([API](https://api.github.com/repos/penpot/penpot)).

É uma ferramenta de design e prototipagem open source, baseada em web, com SVG nativo, componentes, design tokens e auto-hospedagem. Em apresentações, permite criar mockups de alta fidelidade e exportar telas com controle de qualidade. O impacto é o de uma suíte de design profissional sem assinatura. A limitação é o peso: para uma única imagem, é exagero; para um sistema de design, é uma base sólida. A manutenção é ativa, com releases frequentes.

#### OBS Studio

[Repositório](https://github.com/obsproject/obs-studio) · [Site](https://obsproject.com)

77.767 estrelas, 10.741 forks, 1.162 issues/PRs abertos, licença GPL-2.0, release 32.2.2 em 14/08/2026, último push em 16/10/2026 ([API](https://api.github.com/repos/obsproject/obs-studio)).

É uma referência para gravação e transmissão de tela, com cenas, fontes, câmera e mixagem de áudio. Em apresentações, serve para gravar a palestra, capturar uma demo com picture-in-picture e produzir vídeos de divulgação. O impacto é a qualidade de produção. A limitação é a configuração e o fato de não ser um editor; a edição fica para outro programa.

#### Kap

[Repositório](https://github.com/wulkano/Kap) · [Site](https://getkap.co)

19.402 estrelas, 901 forks, 260 issues/PRs abertos, licença MIT, release v3.6.0 em 27/10/2022, último push em 12/11/2024 ([API](https://api.github.com/repos/wulkano/Kap)).

É um gravador de tela para macOS, com exportação em GIF e MP4 e interface simples. Em slides, serve para demos curtas de interface. O impacto é a praticidade. A limitação é séria: macOS apenas e sem atividade desde 2024. Para trabalho novo, OBS ou a gravação nativa do sistema são mais seguros.

#### ScreenToGif

[Repositório](https://github.com/NickeManarin/ScreenToGif) · [Site](https://www.screentogif.com)

27.817 estrelas, 2.377 forks, 338 issues/PRs abertos, licença MS-PL, release 2.43.2 em 28/07/2026, último push em 14/10/2026 ([API](https://api.github.com/repos/NickeManarin/ScreenToGif)).

É um gravador e editor de GIF para Windows, com edição quadro a quadro, remoção de quadros e exportação para vídeo. Em apresentações, resolve demos curtas de software com controle fino. O impacto é a clareza do GIF. A limitação é ser Windows apenas. A manutenção é ativa.

## 3. Síntese, armadilhas de licença e lacunas

### Takeaway

Para elevar o impacto visual de uma apresentação em 2026, a combinação de melhor retorno, na avaliação desta nota, é: um framework de slides com tema bem cuidado (Slidev ou reveal.js), diagramas versionáveis (Mermaid ou Excalidraw, com draw.io para precisão), uma biblioteca de ícones consistente (Lucide ou Tabler), tipografia com Inter ou IBM Plex, e motion pontual (GSAP ou anime.js). Manim e Remotion entram quando o conteúdo é matemática ou vídeo, não como substitutos de um deck ao vivo. tldraw e Remotion exigem atenção contratual; draw.io exige atenção de escopo antes de entrar em produção.

### Cited Findings

| Projeto | Papel no deck | Estrelas | Licença | Sinal em 19/10/2026 |
|---|---|---:|---|---|
| [Excalidraw](https://github.com/excalidraw/excalidraw) | Diagramas e rascunhos | 134.161 | MIT | Muito ativo |
| [Mermaid](https://github.com/mermaid-js/mermaid) | Diagramas versionáveis | 90.748 | MIT | Muito ativo |
| [draw.io](https://github.com/jgraph/drawio) | Diagramas técnicos precisos | 8.866 | Apache-2.0 com restrições | Ativo, repositório de teste |
| [tldraw](https://github.com/tldraw/tldraw) | Canvas/SDK | 50.984 | Proprietária, produção paga | Muito ativo |
| [D2](https://github.com/d2lang/d2) | Diagramas com estética | 25.654 | MPL-2.0 | Ativo, v0.x |
| [Manim CE](https://github.com/ManimCommunity/manim) | Matemática animada | 41.677 | MIT | Muito ativo |
| [Remotion](https://github.com/remotion-dev/remotion) | Vídeo programático | 65.213 | Proprietária, limite de 3 funcionários | Muito ativo |
| [Motion Canvas](https://github.com/motion-canvas/motion-canvas) | Motion graphics em TS | 19.391 | MIT | Sem release estável desde 2024 |
| [GSAP](https://github.com/greensock/GSAP) | Animação web | 29.467 | Gratuita desde 2025 | Mantido, repo pouco movimentado |
| [anime.js](https://github.com/juliangarnier/anime) | Animação web leve | 73.704 | MIT | Ativo |
| [Slidev](https://github.com/slidevjs/slidev) | Deck para devs | 49.127 | MIT | Muito ativo |
| [reveal.js](https://github.com/hakimel/reveal.js) | Deck HTML | 72.441 | MIT | Ativo, fila grande |
| [Lucide](https://github.com/lucide-icons/lucide) | Ícones de interface | 25.143 | ISC | Muito ativo |
| [Tabler](https://github.com/tabler/tabler-icons) | Ícones em massa | 22.369 | MIT | Muito ativo |
| [Playwright](https://github.com/microsoft/playwright) | Screenshots e demos | 98.067 | Apache-2.0 | Muito ativo |

As armadilhas de licença que mais afetam um projeto de apresentação são:

- tldraw não é MIT. O uso em produção exige chave e licença; sem chave, o editor para de renderizar após cinco segundos em produção ([licença](https://tldraw.dev/community/license)).
- Remotion é gratuito para indivíduos e empresas com até três funcionários; acima disso, exige licença comercial ([LICENSE](https://github.com/remotion-dev/remotion/blob/main/LICENSE.md)).
- GSAP é gratuito para uso comercial desde 30/04/2025, mas a licença é própria, não MIT ([anúncio](https://webflow.com/blog/gsap-becomes-free)).
- draw.io é Apache-2.0, com restrição adicional para bibliotecas de ícones em produtos Atlassian ([README](https://github.com/jgraph/drawio#readme)).
- Font Awesome Free separa ícones CC BY 4.0, fontes OFL 1.1 e código MIT; o crédito é obrigatório para os ícones ([LICENSE](https://github.com/FortAwesome/Font-Awesome/blob/master/LICENSE.txt)).
- Simple Icons é CC0, mas as marcas continuam protegidas por seus titulares; a licença do arquivo não autoriza uso indevido de marca.
- PPTist é AGPL-3.0, com obrigações fortes para quem oferece o software como serviço ([LICENSE](https://github.com/pipipi-pikachu/PPTist/blob/master/LICENSE)).
- mtheme é CC BY-SA 4.0, o que exige compartilhar adaptações sob a mesma licença ([README](https://github.com/matze/mtheme#readme)).

### Inferences

Por cenário, a escolha mais simples e segura fica assim:

- Palestra para público técnico, com código e diagramas: Slidev, Mermaid, Lucide e GSAP ou anime.js para um ou dois momentos de motion.
- Deck com identidade visual própria e controle total de HTML/CSS: reveal.js, com Auto-Animate e GSAP.
- Artigo acadêmico em PDF: Beamer com Metropolis ou Quarto com Beamer, aceitando a estagnação do mtheme.
- Aula ou vídeo de matemática: Manim Community, não o ManimGL, salvo se o objetivo for replicar o estilo do 3Blue1Brown.
- Vídeo promocional ou versão em vídeo do deck: Remotion, com atenção ao limite de funcionários da licença.
- Diagrama de arquitetura: Mermaid para documentação e fluxo, Excalidraw para rascunho com personalidade, draw.io para precisão e stencils, D2 para estética.
- Ícones: Lucide ou Tabler para interface; Font Awesome para marcas e símbolos conhecidos; Simple Icons para logos de tecnologias.
- Tipografia: Inter para texto e interface, IBM Plex para um sistema completo, Google Fonts para exploração e Fontsource para entrega offline.
- Screenshots e demos: Playwright ou shot-scraper para captura em escala, Carbon para código, VHS para terminal, OBS para gravação.
- Mockups: Penpot para alta fidelidade, Pencil apenas para wireframe legado.

A leitura de atividade sugere três faixas. Muito ativos e com releases recentes: Excalidraw, tldraw, Mermaid, Remotion, Manim CE, Slidev, reveal.js, D2, PlantUML, Penpot e Playwright. Estáveis ou em manutenção: draw.io, GSAP, anime.js, Lucide, Tabler, Inter, Carbon e VHS. Com risco de manutenção: Motion Canvas, mtheme, WebSlides, Kap, Pencil e Feather. A faixa de risco não significa que o software parou de funcionar; significa que novas necessidades podem não ser atendidas.

### Gaps

- Não há benchmark independente de qualidade visual. As avaliações de "impacto" nesta nota são julgamentos baseados em recursos documentados, não em testes cegos com plateias.
- Não foi possível medir o custo real de renderização de Remotion ou Manim em máquinas diferentes; os tempos variam com o projeto e o hardware.
- A licença do Remotion pode mudar na versão 5.0, conforme aviso no próprio LICENSE; a nota registra o estado de outubro de 2026.
- O número de estrelas do draw.io, do Phosphor core e do Marp principal não representa a adoção real, por serem repositórios-espelho, monorepos parciais ou portas de entrada.
- Não foi feita uma revisão sistemática de Hacker News ou Reddit; a única evidência comunitária usada foi o README do fork Canvas Commons, por documentar um fato de manutenção que o repositório original não expõe.
