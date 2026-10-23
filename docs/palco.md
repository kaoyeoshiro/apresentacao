# Motor de palco

Apresentação ao vivo em que cada quadro é função pura do tempo, com paradas. O clique toca o trecho animado até a
parada seguinte; o mesmo arquivo vira vídeo, PDF e stills de revisão. A decisão de fazer motor próprio, em vez de
Slidev ou reveal.js, está em `docs/decisao.md`. O protocolo de produção de uma apresentação está na skill
`.claude/skills/apresentacao/SKILL.md`, o contrato dos temas em `docs/temas.md`; este documento é o contrato técnico.

## Estrutura de um deck

`decks/<slug>/deck.html`, com mídia em `decks/<slug>/midia/` e o crédito de cada arquivo em `midia/creditos.json`.
Saídas (`output/`, `storyboard/`, `pacote/`) e `cache/` ficam fora do git. Há dois moldes: `./ap novo <slug> --tema
<tema>` copia o catálogo do plano contínuo, `decks/catalogo/`, que é o padrão, e `--modo slides` copia a demonstração
`decks/demo/`, de slides com transições. Cor, fonte e logo vêm de `<link rel="stylesheet"
href="../../temas/<tema>/tema.css">` e o deck só usa os tokens do contrato.

```html
<div id="palco">
  <section data-slide="abertura"> ... </section>
  <section data-slide="problema"> ... </section>
</div>
<script type="module">
import {palco, entrar, revelar, surgir} from '../../motor/palco.js';
palco({
  slides: [
    {id: 'abertura', titulo: 'Abertura', passos: [1.4, 0.8], notas: 'O que dizer.', segura: 3},
    {id: 'problema', passos: [1.1], transicao: 'empurrar'},
  ],
  cenas: {
    abertura: (t, c) => { revelar(document.getElementById('titulo'), entrar(c.desde(0))); },
  },
  desenhar: (t, ctx) => { /* elementos globais, como um fio de progresso */ },
});
</script>
```

O palco tem 1920×1080 e o tocador escala para a janela. Cada `section[data-slide]` ocupa o quadro inteiro, com
posição absoluta.

O plano contínuo tem biblioteca pronta. Com `motor/cenas.css` ligado depois do tema e `mundo(slides)` de
`motor/cenas.js`, o deck escreve só o conteúdo, em sections com `data-arquetipo`, e uma linha por slide; posição no
mundo, trilha dourada, zonas noite, viagens, duração dos cliques e cenas saem da biblioteca, e apagar ou reordenar um
slide é mexer na section e na lista. O contrato de cada arquétipo (abertura, escolha, numero, comparacao, ramos,
objetos, viagem, fios, demonstracao, respiro, fecho), os andamentos e a partitura de luz estão em `docs/cenas.md`; o
molde, com um slide por arquétipo, é `decks/catalogo/`. O resto deste documento é o motor por baixo, que a biblioteca
usa e que um slide fora dos arquétipos usa direto.

## Linha do tempo

A parada 0 é t = 0, antes de qualquer passo: o palco antes do primeiro clique. Se o título deve estar na tela
enquanto a plateia chega, desenhe-o já visível em t = 0. Cada slide tem `passos`, durações em segundos, e cada
passo termina numa parada. O primeiro passo de um slide contém a entrada dele e a transição a partir do anterior.

| campo do slide | efeito |
|---|---|
| `id` | casa com `data-slide` e com a chave em `cenas` |
| `titulo` | índice (tecla G) e tela do apresentador; padrão é o id |
| `passos` | durações dos trechos animados; um clique por passo |
| `notas` | texto da tela do apresentador |
| `segura` | segundos que a linha de vídeo fica em cada parada deste slide (padrão 2,5) |
| `transicao` | `corte` (padrão), `fade` ou `empurrar`, aplicada às seções durante o primeiro passo |
| `camera` | `true` (enquadra a própria seção) ou `{x, y, w, h}` no mundo; exige `<div id="mundo">` dentro do palco e liga o modo mundo, em que todas as seções ficam visíveis e a câmera viaja entre elas no primeiro passo |
| `viagem` | segundos que a câmera leva para chegar, contados do início do primeiro passo (padrão: o passo inteiro); o resto do passo fica para a entrada do conteúdo, e um slide pode abrir inteiro num clique só |
| `recuo` | de 0 a 1: quanto a câmera se afasta no meio da viagem (0,15 mostra os vizinhos e o caminho entre eles); só em slide com `camera` |

## Contexto das cenas

`cenas[id](t, c)` é chamada para o slide atual e, durante a entrada dele, também para o anterior; no modo mundo,
para todos. Como cada cena desenha a partir de t, pular para qualquer instante dá sempre o mesmo quadro.

| `c.` | valor |
|---|---|
| `p(n)` | progresso linear do passo n, de 0 a 1 |
| `desde(n)` | segundos desde o início do passo n (negativo antes); é a entrada das molas |
| `local` | segundos desde o início do slide |
| `entrada` | progresso suavizado do primeiro passo |
| `ocioso` | segundos parado na parada atual (só no slide atual); para movimento ambiente discreto |
| `passo`, `atual`, `slide`, `i`, `modo` | passo corrente, se é o slide atual, o slide, o índice e `vivo` ou `render` |
| `camera` | pose da câmera em t, `{cx, cy, z, rot}` (centro no mundo, zoom e giro); fora do modo mundo, a pose neutra `{cx: 960, cy: 540, z: 1, rot: 0}` |
| `kCamera` | progresso suavizado da viagem da câmera até este slide, de 0 a 1; vale 1 no primeiro slide, em slide sem `camera` e fora do modo mundo, e com `viagem: 0` (corte seco) vira degrau |

O `desenhar` global recebe também `k(id, n)` e `de(id)`, para elementos que atravessam slides. Antes do primeiro
quadro, ao vivo e no render, o palco carrega todas as fontes do documento, porque medidas feitas com a fonte de
reserva erram a caixa; no render, também decodifica as imagens e espera um quadro de cada vídeo.

## Ajudantes

| função | uso |
|---|---|
| `entrar(dt)` | mola de entrada com ~3% de excesso que assenta em 1 exato; use com `c.desde(n)` |
| `revelar(el, k, {de})` | sobe de trás de uma linha de corte (`baixo`, `cima`, `esquerda`); a entrada padrão de texto |
| `surgir(el, k, {dy, dx, escala})` | opacidade e deslocamento curtos, para blocos e cartões |
| `palavras(el, k)` | revela palavra por palavra |
| `contar(el, k, de, ate, {casas, prefixo, sufixo})` | número que conta, em formato pt-BR; só reescreve quando o texto muda |
| `tracar(path, k)` | traço SVG que se desenha |
| `video(el, seg, {fps})` | vídeo local no quadro exato no render; ao vivo, toca e corrige acima de 0,25 s, e parado corrige acima de meio quadro (`fps`, padrão 30), para a parada mostrar o quadro do PDF |
| `digitar(el, k, {cursor, semente})` | texto simples que se digita, com ritmo fixado pela semente e pausa depois de vírgula e ponto; o que falta fica escondido no lugar final, então a linha não muda de quebra; `cursor: true` mostra a barra, um span com fundo `var(--cor-destaque)` (nunca o glifo ▌) |
| `voar(el, de, para, k, {arco})` | FLIP: o elemento fica no lugar dele no layout e é levado por `translate` e `scale` da caixa `de` (k = 0) à caixa `para` (k = 1); caixas são elementos (medidos uma vez) ou `{x, y, w, h}` de `caixa()`; `para` nulo é o próprio lugar, e em k = 1 o transform fica vazio; `arco` levanta o meio do voo em px |
| `anotar(alvo, k, {forma, semente, folga})` | traço à mão firme que se desenha: `'circulo'` (1,05 volta, raio modulado em 1,5% por `ruido`) ou `'sublinhado'`, 6 px em `var(--cor-destaque)`; alvo HTML ganha uma camada SVG no `offsetParent` dele (se esse pai corta, anote o contêiner); alvo `<svg>` (viewBox em px) ou `<path>` recebe o traço na própria caixa e o estilo do deck |
| `kenburns(el, k, {escala, origem})` | aproximação lenta de foto: começa em `escala` (padrão 1,06) e assenta em `scale(1)` exato em k = 1; `origem` é o ponto que fica parado |
| `caixa(el)` | `{x, y, w, h}` do elemento HTML no mundo (ou no palco, fora do modo mundo), pela soma de `offsetLeft` e `offsetTop`; meça com ela, nunca com `getBoundingClientRect`, que inclui a escala do tocador e o zoom da câmera (o `./ap lint` avisa) |
| `transformar`, `enquadrar` | um elemento que vira outro e a pose de câmera que mostra uma caixa (`motor/camera.js`) |

De `motor/tempo.js`, também exportadas pelo palco:

| função | uso |
|---|---|
| `faixa(t, t0, t1)` | de 0 em t0 a 1 em t1; com t1 <= t0 vira degrau em t0 (viagem 0 não dá NaN) |
| `molaAR(dt, {resposta, amortecimento})` | mola dita por período em segundos e razão ζ, que assenta em 1 exato como `entrar`; `entrar` equivale a resposta 0,41 s e ζ 0,77, e o tom sóbrio do cojuris é 0,5 s e ζ 0,9 (o padrão) |
| `saida`, `entradaSaida`, `sair`, `chegar` | curvas: `saida` desacelera, `entradaSaida` é simétrica, `sair` arranca devagar (o que deixa a tela) e `chegar` pousa longo (o que chega) |
| `escalonar(itens, {de, quantidade, curva})` | atrasos de uma onda, em segundos: `itens` é um número (fila) ou caixas medidas uma vez; `de` é `'inicio'`, `'centro'`, `'bordas'` ou `{x, y}`; atraso = `quantidade` (padrão 0,4) × curva(distância / maior distância) |

Numa cena, os ajudantes novos se combinam assim (a peça e a frase existem no HTML desde o carregamento):

```js
let atrasos;                                                   // medidos no primeiro quadro, com as fontes prontas
const cenas = {
  palavra: (t, c) => {
    const d = c.desde(0) - (c.slide.viagem ?? 0) + 0.5;      // conteúdo começa 0,5 s antes do pouso
    digitar($('frase'), faixa(d, 0, 1.6), {cursor: true});
    voar($('vencedora'), $('candidata'), null, molaAR(d - 1.8), {arco: 60});
    anotar($('voto'), saida(faixa(d, 2.2, 2.8)), {semente: 4});
    const itens = [...$('grade').children];
    atrasos ??= escalonar(itens.map(caixa), {de: {x: 120, y: 975}});
    itens.forEach((el, n) => surgir(el, molaAR(d - atrasos[n])));
    $('rotulo').style.opacity = c.kCamera;                    // acompanha a câmera durante a viagem
  },
  aula1: (t, c) => kenburns($('heroi'), faixa(c.local, 0, 2.4), {escala: 1.06, origem: '70% 55%'}),
};
```

Animação é função do tempo: nada de relógio, timer, `Math.random()` sem semente (`aleatorio` e `ruido` de
`motor/tempo.js` têm semente) nem CSS transition, e o `./ap lint` barra. Cores do tema podem vir de `color-mix`,
que o oráculo lê como o navegador calcula. Dados entram no próprio HTML, porque `fetch()` não funciona no pacote
aberto por arquivo.

## Blocos da aula

Três recursos opcionais, ligados pelo deck e sem efeito nenhum em quem não os usa. O deck de teste é
`tests/fixtures/palco_guia/`, e o catálogo usa os três.

```js
palco({
  autoplay: true,
  blocos: [
    {id: 'o-que-e', rotulo: 'O que é IA', minutos: 15},
    {id: 'como-funciona', rotulo: 'Como funciona', minutos: 20},
    {id: 'fechados-abertos', rotulo: 'Fechados e abertos', minutos: 10},   // pode ser da aula seguinte
  ],
  slides: [
    {id: 'capa', passos: [1.4], linhaDia: false},
    {id: 'definicao', bloco: 'o-que-e', passos: [1.2]},
    {id: 'exemplo', passos: [1.0]},                                       // herda 'o-que-e'
    {id: 'pratica', bloco: 'como-funciona', passos: [1.0], pratica: 3,
     notas: {diga: 'Agora é com vocês.', faca: ['abrir o app', 'pedir mão levantada'], transicao: 'Quem terminou mostra.'}},
  ],
  ...
});
```

A abertura automática (`autoplay: true`) toca a entrada do primeiro slide sozinha ao abrir o deck ao vivo, assim que
as fontes carregam, e para na parada 1 como se alguém tivesse clicado. Só vale na parada 0: recarregar a página no
meio da aula (`#parada=N`) não toca nada. Render, vídeo, PDF, stills, prévias e a tela do apresentador não passam pelo
tocador e continuam idênticos.

A linha do dia é uma faixa fina embaixo da trilha, de 120 a 1800 px e de y 993 a 1037, dentro da margem de 4%. Cada
bloco de `blocos` é um rótulo de 30 px com um trilho de 4 px por baixo; a largura de cada um cresce na proporção dos
`minutos`, sem cortar o rótulo. O bloco atual vem na tinta cheia, os outros na tinta suave, e o trilho do atual enche
de dourado com o tempo do deck (do começo do primeiro slide do bloco ao fim do último); os passados ficam cheios na
tinta suave e os futuros vazios. O `bloco` de um slide vale para os seguintes até outro `bloco`, e `linhaDia: false`
a esconde naquele slide (capa, aberturas, respiro). Ela entra e sai em 0,4 s no começo do slide, troca para as cores
da noite (`.noite` na section) no meio da viagem da câmera e fica fora do `#mundo`, então não anda com a câmera. Tudo
é função de t, e por isso aparece nos stills do `./ap paradas`, no PDF e no vídeo. Ficam só `var()` do tema
(`--cor-tinta`, `--cor-tinta-suave`, `--cor-linha`, `--cor-destaque` e as da noite). O oráculo mede a legibilidade
dela (corpo, borda, contraste, sobreposição), mas não a conta como conteúdo do slide nas palavras, na hierarquia, na
escala e no respiro, porque ela é marcada com `data-sinalizacao`. Bloco sem slide neste deck aparece sempre: futuro
se vem depois do atual, cheio se vem antes, para a aula 2 mostrar o dia inteiro.

A tela do apresentador (P) mostra, além do que já mostrava, o bloco atual ("bloco 2 de 5 · Como funciona · 07:12 de
20:00"), com o ritmo: o tempo no bloco contra os minutos previstos para a fração dele que já passou (parada a parada),
e "adiantado" ou "atrasado" acima de meio minuto de diferença. O relógio do bloco começa quando a tela vê o bloco pela
primeira vez. Embaixo da próxima parada vai o título dela, o passo e o aviso de bloco novo. `notas` aceita texto ou o
guia `{diga, faca, transicao}`: `diga` é a fala, `faca` uma ação ou uma lista delas (abrir o app, pedir mão levantada,
cronômetro de prática) e `transicao` a ponte para o próximo slide. Com `pratica: 3` (minutos), a tela do apresentador
conta 3 minutos para trás desde a chegada ao slide, em dourado, e depois do zero conta o excesso (`+00:12`) em
vermelho; no palco aparece o mesmo número, pequeno no canto, fora do `#palco` (não sai em still, PDF nem vídeo).

## Ao vivo

| tecla | ação |
|---|---|
| → espaço Page Down Enter, clique | avança (clique no meio de uma animação toca o resto dela em 3x e segue para o próximo trecho; um segundo clique completa na hora) |
| ← Page Up | volta para a parada anterior, sem animação |
| número + Enter | vai ao slide |
| Home End | início e fim |
| B ou . | tela preta |
| F | tela cheia |
| G | índice de slides |
| P | tela do apresentador (agora, próxima parada, notas ou guia, bloco e ritmo, prática, cronômetro, relógio) |
| ? | atalhos |

A posição fica no endereço (`#parada=N`), então recarregar a página não perde o lugar. A tela do apresentador
conversa com o palco por `postMessage` e funciona também no pacote aberto por arquivo.

## Ferramentas

```bash
./ap novo <slug> --tema noite|cojuris|pge [--modo continuo|slides]
./ap abrir decks/<slug>
./ap sondar decks/<slug>
./ap paradas decks/<slug> --viagens
./ap pdf decks/<slug>
./ap video decks/<slug> --paginas 3
./ap empacotar decks/<slug>
./ap lint decks/<slug>
./ap lint motor/cenas.css
```

`novo` copia o molde do modo para `decks/<slug>/` e troca o link do tema: `continuo` (padrão) parte de
`decks/catalogo/`, com o `briefing.md` a reescrever e a mídia-marcador de `midia/` com o crédito dela, e `slides` parte
de `decks/demo/`. Saídas do molde (`storyboard/`, `output/`, `pacote/`, `cache/`) não vão junto.

`pdf` e `empacotar` recusam deck que ainda tem `[CONFERIR]` no `deck.html` (texto, comentário ou código) e listam
cada ocorrência com a linha; `--rascunho` gera assim mesmo, para ensaio, nunca para a plateia.
`paradas` grava um PNG por parada e a folha de contato em `storyboard/`. Com `--viagens`, grava também os quadros de
dentro de cada viagem, onde a crítica da prévia achou a maior parte dos defeitos (papel vazio no meio do caminho,
foto com borda dura, elemento que some): a 35% e a 70% da viagem da câmera e 0,3 s depois do pouso, quando o
conteúdo ainda está entrando. Fora do modo mundo, os dois primeiros quadros caem na entrada do slide; com `viagem: 0`
(corte seco) só há o do pouso. Cada quadro vai para `storyboard/viagem-NN-<id>-<35|70|pouso>.png` (NN é o número do slide), e a folha
`storyboard/viagens.png` tem uma linha por slide, nas colunas 35%, 70% e pouso, rotulada "slide · instante". Abra a
folha e, onde algo parecer errado, o PNG inteiro. Sem `--viagens`, os quadros de viagem de uma rodada anterior são
apagados, para a folha velha não passar por atual.
`pdf` gera uma página por slide, no estado final (`--todas` para uma por parada), em 13,33 × 7,5 polegadas. `video`
usa o renderizador (`./ap render`) com a linha de vídeo, que segura cada parada `segura` segundos e toca os passos
entre elas. `empacotar` gera `pacote/` com `apresentacao.html`, o tema e as fontes locais, as do Google baixadas se o
deck usar (só latin e latin-ext), a mídia, o PDF de emergência e um LEIA-ME. Só entram arquivos da pasta do deck, de
`temas/` e de `motor/`, nunca de `cache/` nem ocultos; depois abre o pacote por `file://` com a rede bloqueada e falha
se alguma fonte, imagem, vídeo, a seta → ou a tela do apresentador não funcionar.

`lint` roda no `sondar` e antes do render de vídeo (`./ap video`, `./ap render`), e aceita a pasta do deck, o
`deck.html` ou uma folha `.css`. Além das regras do deck (relógio, timer, aleatório sem semente, CSS transition, id
repetido), recusa cor literal (hex, nome de cor como `white` ou `black`, `rgb()`, `hsl()` e afins, fora de comentário
e de texto entre aspas) numa folha de `motor/`, como `motor/cenas.css`: ali a cor vem só de `var()` do tema, misturada
por `color-mix` se preciso. Vale para `./ap lint motor/cenas.css` e para a folha de `motor/` que o deck liga por
`<link rel="stylesheet">`. A folha do tema (`temas/<nome>/tema.css`) é onde a cor literal mora, e o lint não a olha.
Seletor com cara de hex (`#fade`), `url(#id)`, `transparent`, `currentColor` e palavra composta (`white-space`,
`--cor-red`) não contam; numa máscara, use `var(--cor-tinta)` no lugar de `#000` ou `black`.

## Oráculo (`sondar`)

Mede o DOM e os pixels em cada parada e sai com código 1 se houver ERRO. As regras de hierarquia, escala e sequência
olham a parada final de cada slide e o deck inteiro; os limiares delas foram calibrados na prévia do curso
(`decks/previa-curso-ia`) e na primeira versão dela (commit a04455e), toda clara e sem nada grande, que reprova.
Deck que lança erro ao abrir (arquétipo ou andamento que não existe, lista de slides inválida) para `sondar`,
`paradas` e as outras ferramentas na hora, com a mensagem do deck, em vez de esperar o limite de 180 s.

| medida | ERRO | AVISO |
|---|---|---|
| tamanho do texto na tela, com zoom | abaixo de 24 px | abaixo de 30 px |
| borda do quadro | texto cortado | dentro da margem de 4% |
| caixa do texto | o texto transborda (descontada a folga natural da fonte acima da entrelinha) | |
| topo das letras, medido pela tinta da primeira linha, contra o pai que corta (`overflow` diferente de `visible`) | o pai apaga o topo (acento de maiúscula em título justo dentro de `.corte`; a correção é `padding-top` no pai) | |
| opacidade numa parada | | entre 0,1 e 0,9 (animação que não terminou) |
| contraste com a mediana do anel em volta da caixa | abaixo de 3:1 | abaixo de 4,5:1 em texto menor que 40 px |
| sobreposição de blocos de texto, na vertical pela faixa da tinta (título empilhado pela tinta não conta) | | mais de 10% do menor |
| palavras visíveis | acima de 70 | acima de 45 |
| movimento nos últimos 40 ms antes da parada, descontada a transição | | mais de 1,5 px |
| duração de um passo | | acima de 3,5 s |
| foto (`<img>`) na tela, com o encaixe (`object-fit`), o zoom da câmera e os transforms, contra o tamanho natural | | ampliada acima de 1,05x (uma vez por imagem e slide; SVG não conta) |
| hierarquia na parada final: o maior texto contra a mediana dos outros (as linhas do próprio maior texto não contam) | | menos de 1,5x |
| escala do deck: o maior elemento da parada final, texto pelo tamanho ou foto e vídeo pelo lado menor visível | | nada acima de 120 px em mais da metade dos slides |
| sequência pela parada final: clima (luminância média do still, claro a partir de 0,5) e faixa de palavras (até 12, 13 a 24, 25 a 45, mais de 45) | | três ou mais slides seguidos com o mesmo clima e a mesma faixa |
| respiro: parada com até 12 palavras ou com um texto de 200 px ou mais | | mais de cinco slides seguidos sem respiro |
| `data-arquetipo` da seção | | dois slides vizinhos com o mesmo arquétipo |
| determinismo (até 8 paradas, em outra ordem e em página nova, com o Chromium sem raster parcial) | quadro diferente em mais de 24 níveis num canal de algum pixel (abaixo disso é ruído de rasterização) | |

O contraste é estimativa e pode errar sobre foto; o oráculo vê legibilidade, não beleza, e não substitui abrir a
folha de contato e a de viagens. Os limiares estão no topo de `ferramentas/palco.py`. O deck ruim de
`tests/fixtures/palco_ruim/` prova que cada regra de legibilidade reprova; o monótono de
`tests/fixtures/palco_monotono/` dispara hierarquia, escala, sequência, respiro e arquétipo; o de
`tests/fixtures/palco_isencoes/` mostra a foto ampliada e as isenções; e o de `tests/fixtures/palco_estado/`, que
guarda estado entre quadros, prova que a folga do determinismo não o esconde. A folga existe porque o Chromium
rasteriza o mesmo instante revisitado com até 5 níveis de diferença (canto arredondado, transform de identidade),
enquanto estado escondido de verdade (objeto que some, quadro de vídeo errado) passa de 200; o limiar é
`TOLERANCIA`, em `ferramentas/render.py`.

Duas exceções se declaram no HTML, sempre com o motivo, e o relatório as lista como `ISENTO`, com o motivo, sem
contar como aviso (a última linha diz quantas houve):

- `data-contraste-ok="motivo"` no texto ou num ancestral dele isenta o contraste baixo em texto de 48 px ou mais,
  como o dourado oficial cheio num título grande sobre o claro (`temas/cojuris/regras.md`). Em texto menor, ou sem
  motivo, o achado continua, com a explicação.
- `data-ritmo-ok="motivo"` na seção do slide isenta o passo longo em que um vídeo visível no quadro toca mais de meio
  segundo. O slide que é só uma pose de câmera sobre o vídeo, sem seção própria, declara `ritmoOk: 'motivo'` na
  lista de slides. Sem vídeo tocando, o aviso continua, com a explicação.

## Mídia

Imagens e clipes caem em `decks/<slug>/midia/`, cada arquivo com o crédito em `midia/creditos.json` (ferramenta,
modelo, prompt, refs, parâmetros, custo estimado, origem, data). Originais e rascunhos ficam em `midia/originais/` e a
folha de candidatos em `storyboard/`, ambos fora do git por pesarem demais; no git entram só os arquivos que o deck
usa e o `creditos.json`, e os originais precisam de cópia fora do repositório antes de apagar a pasta.

### Imagens

Imagem gerada para o deck pertence à série do tema e sai do `./ap imagens`, que lê `decks/<slug>/imagens.toml` (uma
entrada por imagem, com prompt só do objeto e da cena) e `temas/<tema>/imagem/`. O contrato inteiro, com o formato do
toml, a trava de custo, o aviso de zona de texto e o que vale num checkout sem `midia/originais/`, está em
`docs/temas.md`, seção Imagem.

```bash
./ap imagens decks/<slug>                                # situação e custo do que falta, sem gastar
./ap imagens decks/<slug> --rascunhos [nome ...] [-n 3]  # Gemini 1K e a folha storyboard/candidatos.png
./ap imagens decks/<slug> --final nome=i [...]           # final na resolução do toml, tratado e creditado
./ap imagens decks/<slug> --tratar [nome ...]            # refaz só o tratamento, sem custo
```

Fora da série, `./ap imagem decks/<slug> nome "prompt" [--backend gemini] [--ref ref.png]` chama o gerador uma vez
(GPT Image por padrão), sem estilo, mestra nem trava de custo, e `./ap tratar decks/<slug> arquivo [--tom
duotone|tritone] [--alfa] [--niveis auto|claro|fundo] [--gama G] [--largura L]` trata um arquivo avulso. Os dois ficam
para exceção declarada ao usuário. Cada `--ref` é PNG ou JPG, porque o image-video-api recusa WebP.

### Vídeo

```bash
./ap video-ia decks/<slug> abertura "prompt" --segundos 8 --resolucao 720p [--imagem quadro.png]
./ap video-ia decks/<slug> abertura "prompt" ... --aprovado HASH
./ap trazer decks/<slug> ../claude_video_maker/videos/x/output/clipe.mp4 --origem "./cvm html, código próprio" \
  [--perfil tela|demo] [--ate SEG] [--capa SEG] [--com-audio]
./ap midia conferir decks/<slug>
```

`video-ia` usa o Gemini Omni pelo `./cvm veo`, e sem `--aprovado` só imprime o orçamento e o hash; gerar exige o sim
do usuário na conversa para aquele clipe e aquele custo. O clipe é gerado em
`claude_video_maker/videos/ap-<slug>/public/clipes/`, onde fica o orçamento, e copiado para o deck. `trazer` copia um
arquivo pronto (vídeo por código do `./cvm html`, Remotion ou Manim, ou foto com licença) e prepara o vídeo para o
palco em H.264 high e yuv420p, com quadro-chave a cada 0,5 s, índice no começo (faststart), sem áudio salvo
`--com-audio` e largura até 1920 px (`tela`) ou 2560 px (`demo`). A opção `--capa` grava `<nome>-capa.webp` daquele
instante, para o `poster`. `midia conferir` passa o ffprobe em cada vídeo de `midia/` e sai 1 com ERRO para HEVC ou
ProRes, que o Chromium não toca, e para mais de 8 bits ou croma 4:2:2 e 4:4:4. Os avisos cobrem AV1 (toca, mas pode
decodificar em software no notebook do palco), quadro-chave acima de 1 s, índice no fim do arquivo e largura acima do
perfil registrado no crédito.

O claude_video_maker é a pasta vizinha, procurada também acima do repositório (o que vale num worktree), ou a
indicada em `CVM_PROJETO`.
