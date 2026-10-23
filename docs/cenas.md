# Biblioteca de cenas: o plano contínuo pronto

`motor/cenas.js` e `motor/cenas.css` generalizam o que a prévia do curso de IA (`decks/previa-curso-ia`) escreveu à
mão. Os slides moram num mundo só, ligados por uma trilha dourada de circuito; a câmera viaja de um ao outro, cada
clique abre o slide inteiro com animação, e os traços de cada abertura descem até a trilha na viagem seguinte. O
deck escreve só o conteúdo, em sections com `data-arquetipo`, e uma linha por slide numa lista; posições, trilha,
zonas noite, durações e cenas saem da biblioteca. O molde é `decks/catalogo/`, com um slide por arquétipo, e o
contrato do motor por baixo está em `docs/palco.md`.

## Montar o mundo

O tema vem antes da folha da biblioteca, e o texto fica no HTML (o oráculo mede o HTML). Os dados de cada cena vão
em atributos `data-*`, nunca no script.

```html
<link rel="stylesheet" href="../../temas/cojuris/tema.css">
<link rel="stylesheet" href="../../motor/cenas.css">
...
<div id="palco"><div id="mundo">
  <section data-slide="aula1" data-arquetipo="abertura" class="noite"> ... </section>
  <section data-slide="palavra" data-arquetipo="escolha"> ... </section>
</div></div>
<script type="module">
import {palco} from '../../motor/palco.js';
import {mundo} from '../../motor/cenas.js';
const slides = [
  {id: 'aula1', titulo: 'Aula 1', segura: 3, notas: 'O que dizer.'},
  {id: 'palavra', titulo: 'Uma palavra por vez', notas: 'O que dizer.'},
];
const m = mundo(slides);
palco({slides: m.slides, cenas: m.cenas(), desenhar: m.desenhar});
</script>
```

A entrada do slide aceita os campos do palco (`id`, `titulo`, `notas`, `segura`, `passos`, `viagem`, `recuo`,
`camera`) e mais estes, todos opcionais:

| campo | efeito |
|---|---|
| `andamento` | `corte`, `curta`, `media`, `longa`, `capitulo` ou `mergulho` (tabela abaixo; `capítulo`, com acento, também vale); `viagem` e `recuo` explícitos vencem |
| `passos` | duração do clique em segundos; o padrão é a espera da viagem mais a duração do arquétipo, nunca menos que a viagem mais 0,4 s nem que o fim do vídeo |
| `dy`, `vao` | degrau vertical e vão horizontal até o slide anterior, em px do mundo |
| `x`, `y` | posição absoluta no mundo, quando a regra automática não serve |
| `video: [de, dur]` | o slide toca `dur` segundos do vídeo da `.tela` a partir de `de` segundos do seu início |
| `mergulho: {em, x, y, f, furos}` | slide sem section: a câmera entra na `.tela` do slide `em` (canto em frações `x`, `y`, largura `f` da tela) e acende um holofote com os `furos`, cada um `[x, y, w, h]` em frações do quadro do vídeo |

Cada slide fica depois do anterior, com 1920 px de largura mais o vão: 400 px em regra, 1100 depois de uma abertura e
1000 antes de um capítulo. A altura segue um ciclo de degraus (240, −300, 0, 260, −300, 280, −180 px), que vira as
curvas de 45° da trilha; depois de uma abertura o degrau é zero, para os traços dela descerem paralelos até a trilha.
A trilha corre em y 975 de cada slide, de x 120 a 1800, com um pad em cada ponta (o da esquerda fica oco até a
câmera chegar) e um anel no fim do último slide. Slides com `class="noite"` ganham uma zona marinha atrás deles,
com 400 px de anoitecer de cada lado; vizinhos noite dividem a mesma zona.

`mundo(slides)` devolve `m` com `m.slides` (a lista pronta para o palco), `m.cenas(ajustes)`, `m.desenhar`, e as peças
para cenas próprias: `m.secao(id)`, `m.T0[id]` e `m.V[id]` (início e duração da viagem), `m.kCam(t, id)`,
`m.proximo(id)`, `m.depois(f)` (desenho que atravessa slides, roda depois de todas as cenas) e `m[arquetipo](id,
opções)`. Em `m.cenas(ajustes)`, `ajustes[id]` é um objeto de opções do arquétipo ou uma cena inteira `(t, c) =>
{...}`, que substitui a da biblioteca (seção Cena própria, abaixo). O script mede uma vez, no primeiro quadro, e põe
no `#palco` as variáveis que o tema não tem: `--sinal-noite` (o dourado como texto na zona noite, puxado para a cor
do texto quando não dá 3:1 ali), `--sobre-destaque` (texto sobre o dourado), `--cor-sombra` (a mais escura entre
tinta e fundo) e, no tema escuro, as quatro da zona noite (seção Partitura de luz).
`m.cenas()` monta o DOM das peças (células, barras, ícones) e se chama uma vez só, na chamada do `palco`.

Trocar, apagar e reordenar não mexem em script. Para apagar, tire a section e a linha da lista; ao apagar uma
demonstração, apague também as linhas dos mergulhos dela (`mergulho.em` com o id dela), senão o deck para com erro.
Para reordenar, mude a ordem das linhas (a das sections não importa). Section sem linha na lista fica escondida, com
aviso no console, e linha sem section, ou arquétipo que não existe, para o deck com erro claro. `tests/test_cenas.py`
prova que o catálogo passa no oráculo com cojuris, noite e PGE e também depois de apagar um slide do meio.

## Andamentos

O andamento é a duração e o recuo da viagem da câmera. O padrão sai do arquétipo e do vizinho, e só se escreve
`andamento` para mudar o sentido da passagem, como o corte seco que avisa que o assunto mudou.

| nome | viagem | recuo | padrão para |
|---|---|---|---|
| `corte` | 0 | 0 | o primeiro slide; escolha explícita quando o assunto muda (o título já está na tela no clique) |
| `curta` | 0,8 s | 0,06 | vizinho no mesmo capítulo |
| `media` | 1,0 s | 0,12 | o slide depois de uma abertura (os traços descem) e o arquétipo viagem (os objetos atravessam) |
| `longa` | 1,5 s | 0,15 | a demonstração e o slide depois de um mergulho |
| `capitulo` | 2,2 s | 0,22 | toda abertura que não é a primeira; escolha explícita no respiro que fecha um capítulo |
| `mergulho` | 1,4 s | 0 | slide com `mergulho` |

## Partitura de luz

O claro é a base e a noite marca o momento forte. Abertura de capítulo, respiro, demonstração e fecho vão na noite;
explicação, número e fonte ficam no claro. O oráculo avisa quando três slides seguidos têm o mesmo clima e a mesma
faixa de palavras, e quando passam mais de cinco sem respiro (até 12 palavras ou um texto de 200 px), de modo que a
alternância é regra e não gosto. O dourado tem cinco usos, a trilha, a palavra `.sinal`, a `.marca` do fio, a barra
que vence e o marco de agora do tempo, e cada slide acende no máximo uma coisa dourada além da trilha; a exceção é a viagem, em que cada nome que
recebe um objeto acende depois do pouso, um de cada vez, e por isso dois ou três objetos bastam.

A zona noite tem quatro variáveis da biblioteca, que o CSS usa em tudo o que mora nela (fundo da zona, véu da
abertura, holofote e legenda do mergulho, moldura do vídeo, textos e linhas): `--noite`, `--sobre-noite`,
`--suave-sobre-noite` e `--linha-sobre-noite`. No tema claro valem a tinta e as cores "sobre tinta" do tema, como na
prévia. No tema escuro (tinta mais clara que o fundo, como o `noite`), inverter para a tinta poria um bloco creme no
meio da palestra; a zona fica então num tom abaixo do fundo, puxado 6% para o dourado, com a tinta clara por cima, e
o holofote escurece em vez de clarear. A diferença para os slides claros (que no tema escuro também são escuros) é
de temperatura e não de luz, por isso o capítulo se marca também pela foto e pelo título grande da abertura. Um
tema escuro que queira outro tom define `--cor-noite` no `tema.css`.

## Peças comuns

A linha do dia (`blocos` no `palco()` e `bloco` nos slides, contrato em `docs/palco.md`, Blocos da aula) corre numa
faixa fina logo abaixo da trilha, sem cruzar com ela nem com a pílula e o selo, e passa à cor da noite junto com a
zona; nas aberturas e no respiro, `linhaDia: false`.

A escala é `--esc-1` a `--esc-6` (30, 44, 68, 110, 180 e 320 px), com margem de 120 px. `.rotulo` (em cima, caixa
alta) e `.manchete` entram juntos; a manchete é uma linha só, de até uns 36 caracteres a 68 px, e se passar disso o
corpo desce até 56 px e, abaixo disso, ela quebra em duas linhas, aperta o conteúdo e o console avisa para encurtar.
`.pilula` (canto inferior direito) diz "ilustrativo" ou `[CONFERIR]`; `.selo-ia` marca imagem gerada por IA; os dois
entram por último, e qualquer elemento com `data-entra="1.2"` surge naquele segundo do conteúdo (o número não alonga o
clique: acima da duração do arquétipo o elemento não chega a aparecer na parada). Num slide claro com os dois, o
cenas.js põe o selo à esquerda da pílula, na mesma faixa, porque acima dela ficam as legendas dos objetos e abaixo
corre a trilha; na noite o selo já mora no canto de cima, e na viagem, embaixo da foto. `.display` é o texto grande em
caixa alta da fonte de título, `.etiqueta` o rótulo pequeno solto e `.sinal` a palavra dourada.

## Cena própria

Só quando nenhum arquétipo conta aquilo (skill, passo 5). A section vai sem `data-arquetipo`, e a cena entra em
`m.cenas({id: (t, c) => {...}})`; trilha, câmera, zona noite e viagem continuam com a biblioteca. Para o mesmo ritmo
dos arquétipos, `motor/cenas.js` exporta o acabamento: `conteudo(c)` dá os segundos do conteúdo, que começa antes de
a câmera pousar (0,5 s nas viagens de até 1 s, a metade nas mais longas); `titulo(sec, x, c)` faz o rótulo e a
manchete entrarem juntos, com o encaixe numa linha (`encaixar(el)`, também exportado) e prontos no clique de um
corte; e `fim(sec, x, t0)` traz pílula e selo por último, a partir de `t0`, e cada `data-entra` no seu segundo. O
resto vem dos ajudantes de `docs/palco.md` (`surgir`, `revelar`, `tracar`, `molaAR`, `faixa`...). Sem `passos` na
entrada, o clique dura a espera da viagem mais 2 s.

```html
<section data-slide="carimbo" class="noite">
  <p class="rotulo">Revisão</p>
  <h2 class="manchete">A minuta sai carimbada</h2>
  <p class="display carimbo">Aprovado</p>
  <p class="pilula">ilustrativo</p>
</section>
```

```js
import {mundo, conteudo, titulo, fim} from '../../motor/cenas.js';
import {palco, surgir, molaAR} from '../../motor/palco.js';
const m = mundo(slides);
palco({slides: m.slides, desenhar: m.desenhar, cenas: m.cenas({
  carimbo: (t, c) => {
    const sec = m.secao('carimbo'), x = conteudo(c);
    titulo(sec, x, c);
    surgir(sec.querySelector('.carimbo'), molaAR(x - 0.4), {dy: 0, escala: 1.4});
    fim(sec, x, 1.0);
  },
})});
```

A posição e o corpo do `.carimbo` vão no `<style>` do deck, só com `var()` do tema.

## Arquétipos

Cada arquétipo é uma section com `data-arquetipo`; a chamada padrão é `m.cenas()`, e as opções vão em
`m.cenas({id: {...}})`. A mídia que custa dinheiro só se gera com o "sim" do usuário para aquele custo (skill,
regra de vídeo), e cada arquétipo tem uma alternativa sem custo. Vizinhos com o mesmo arquétipo levam aviso do
oráculo.

### abertura

Abre o deck ou um capítulo: rótulo, duas ou três linhas de título com uma palavra-chave dourada, subtítulo de uma
frase (até 20 palavras) e foto heroica sob véu. A palavra `.sinal` cresce até 760 px de largura (opção `largura`) e as
linhas se empilham pela tinta, assentadas acima da trilha. Mídia: foto 16:9 tratada no tema (`./ap imagens`, papel
heroica); sem custo, uma foto do mesmo tema já gerada para outro deck, com o crédito copiado, ou nenhuma (tire a
`.heroi-caixa`, e o título fica sobre o marinho). Foto que não pode ocupar a tela até a borda (objeto pequeno, fundo
que briga com os traços do circuito) vai sem caixa, como `<img class="heroi recorte" style="left: 540px; top: 272px;
width: 1209px">`, com as quatro bordas dissolvidas no marinho. Com foto gerada, o `.selo-ia` é obrigatório. Os traços
do circuito nascem pela borda direita e descem até a trilha na viagem seguinte, sem nada no HTML. As caixas das linhas
se cruzam no empilhamento justo, mas o oráculo mede a sobreposição pela tinta e não avisa; se avisar, as letras se
tocam de fato.

```html
<section data-slide="aula1" data-arquetipo="abertura" class="noite">
  <div class="heroi-caixa"><img class="heroi" src="midia/heroi.webp" alt=""><div class="veu"></div></div>
  <p class="rotulo">Curso de IA · aula 1</p>
  <div class="display ab-linha">O que é</div>
  <div class="display ab-linha sinal">IA</div>
  <p class="ab-sub">Como funciona, como se mede e quem está no mercado.</p>
  <p class="selo-ia">imagem gerada por IA</p>
</section>
```

### escolha

Mostra que uma escolha sai de opções com peso (a próxima palavra, um voto, uma data inventada). A frase cabe numa
linha (uns 33 caracteres a 96 px); cada `.leque` é uma rodada de três ou quatro candidatas, no máximo duas rodadas,
e a vencedora (`li.vence`, ou a primeira) voa para a palavra `data-alvo` da frase. Com `data-sorteio`, uma rodada
só: as barras ficam rasas (`data-escala` é o % que enche o trilho, padrão 60), um anel sorteia, a palavra sai
sublinhada e a `.frase-leg` aparece embaixo dela. Sem mídia. Valores que não vêm de fonte levam a pílula.

```html
<section data-slide="palavra" data-arquetipo="escolha">
  <p class="rotulo">Como funciona</p>
  <h2 class="manchete">A IA escreve uma palavra por vez</h2>
  <div class="frase"><span>O juiz julgou o pedido</span> <span id="pl-w">procedente</span></div>
  <ol class="leque" data-alvo="pl-w"><li data-pct="46">procedente</li><li data-pct="38">improcedente</li><li data-pct="9">extinto</li></ol>
  <p class="pilula">valores ilustrativos</p>
</section>
```

### numero

Um número que a plateia deve lembrar, construído item a item: a caneta corrige a grade (até 10 células, cinco por
linha, `data-colunas` muda), o placar conta os acertos e a barra sobe. Placar curto ("8 de 10") e legenda de até
seis palavras. Sem mídia. Número de fonte real vai anotado no `briefing.md`; o ilustrativo leva a pílula e nunca
vira número gigante.

```html
<section data-slide="prova" data-arquetipo="numero">
  <p class="rotulo">Como se mede</p>
  <h2 class="manchete">Benchmark, a mesma prova com gabarito</h2>
  <div class="grade" data-marcas="1101111011"></div>
  <p class="display numero"><span class="conta">0</span> de 10</p>
  <div class="numero-trilho"><div class="numero-barra"></div></div>
  <p class="numero-leg">acertos na prova</p>
  <p class="pilula">ilustrativo</p>
</section>
```

### comparacao

Duas versões lado a lado sem nome (teste cego, antes e depois), separadas por um fio; o texto de cada uma é
desenhado em linhas cinza (`data-linhas`, largura de cada linha em %, até seis) e a `.janela.escolhida` ganha o
círculo na letra. Sem mídia. Se a comparação for de texto, troque as linhas cinza por uma frase real curta (até 15
palavras) em `<p class="janela-txt">` dentro de cada janela, sem `data-linhas`; ela entra com a janela.

```html
<section data-slide="arena" data-arquetipo="comparacao">
  <p class="rotulo">Como se mede</p>
  <h2 class="manchete">Arena, pessoas votam sem saber qual IA</h2>
  <div class="janela" data-linhas="92 80 88 64"><p class="display letra">A</p><p class="etiqueta">modelo oculto</p></div>
  <div class="fio-v"></div>
  <div class="janela escolhida" data-linhas="86 94 72 90"><p class="display letra">B</p><p class="etiqueta">modelo oculto</p></div>
</section>
```

### ramos

A trilha se divide quando o assunto se divide (classificação, dois caminhos, quem faz o quê). Dois ramos
(`data-y` 450 e 720), até três estações por ramo (nome e subtítulo de até 12 caracteres cada), uma caixa de destino
de até quatro palavras em duas linhas e uma legenda de até dez palavras. Os ramos saem do pad esquerdo da trilha.
Sem mídia.

```html
<section data-slide="mercado" data-arquetipo="ramos">
  <p class="rotulo">Mercado</p>
  <h2 class="manchete">Onde fica o dado do cliente</h2>
  <div class="ramo" data-y="450">
    <div class="estacao"><b>ChatGPT</b><small>OpenAI</small></div>
    <p class="caixa-txt">roda no servidor<br>de quem vende</p>
  </div>
  <div class="ramo" data-y="720">
    <div class="estacao"><b>Llama</b><small>Meta</small></div>
    <p class="caixa-txt">pode rodar no<br>escritório</p>
  </div>
  <p class="ramos-leg">Legenda curta.</p>
</section>
```

### tempo

Agenda, cronograma, linha do tempo ou etapas: o que acontece em que ordem (a semana de estudo, as fases de um
processo, os passos de um método). Até seis marcos numa linha horizontal; cada `li` de `.etapas` tem a data, a hora
ou o número do passo num `<b>` de até 8 caracteres, em cima da linha, e um texto de até quatro palavras embaixo. A
linha se traça da esquerda, cada marco surge quando ela passa, e o `li.agora` (um só, o marco que importa: hoje, a
fase atual, o prazo) enche de dourado depois de todos. Legenda `.tempo-leg` opcional, de até dez palavras. Densidade:
até uns 40 palavras com a legenda. Sem mídia.

```html
<section data-slide="semana" data-arquetipo="tempo">
  <p class="rotulo">Rotina</p>
  <h2 class="manchete">A semana tem um ritmo fixo</h2>
  <ol class="etapas">
    <li><b>seg</b>lei seca</li>
    <li><b>ter</b>questões</li>
    <li class="agora"><b>qua</b>simulado</li>
    <li><b>qui</b>revisão dos erros</li>
    <li><b>sex</b>descanso</li>
  </ol>
  <p class="tempo-leg">O simulado de quarta mede a semana.</p>
</section>
```

### respiro

Pausa: uma frase de até 12 palavras, uma linha por span, que cresce até a linha mais larga ocupar 1680 px (de 110 a
180 px) e fica centrada na altura. Vai na noite; quando fecha um capítulo, a entrada dele leva `andamento:
'capitulo'`. Sem mídia.

```html
<section data-slide="pausa" data-arquetipo="respiro" class="noite">
  <p class="rotulo">Respiro</p>
  <p class="respiro"><span>Uma ideia por tela.</span><span>O resto é <span class="sinal">fala</span>.</span></p>
</section>
```

### objetos

O pedido se digita numa caixa ao lado do material, até três objetos recortados com legenda de uma ou duas palavras;
pedido de até 15 palavras. Mídia: recortes com transparência (`./ap imagens`, papel objeto, com custo); sem custo,
os recortes de outro deck do mesmo tema, com o crédito copiado. Dê `id` às imagens que vão viajar para o slide
seguinte.

```html
<section data-slide="prompt" data-arquetipo="objetos">
  <p class="rotulo">Prompt e contexto</p>
  <h2 class="manchete">Prompt é o pedido, contexto o material</h2>
  <p class="etiqueta">Pedido</p>
  <div class="entrada"></div>
  <p class="pedido">Redija a contestação. Ataque a prescrição.</p>
  <p class="etiqueta">Contexto</p>
  <div class="objetos">
    <figure><img class="objeto" id="ob-contrato" src="midia/doc-contrato.webp" alt=""><figcaption class="doc-leg">contrato</figcaption></figure>
  </div>
  <p class="selo-ia">imagens geradas por IA</p>
</section>
```

### viagem

Os objetos de um slide anterior atravessam o mundo grandes, encolhem perto de uma árvore de arquivos e entram no
ícone; a folha surge no pouso e o nome acende depois. Árvore de até sete nós (`data-nivel` 0 a 2, `data-arquivo`
põe o ícone, `data-de` é o id do objeto que chega), nomes de até 18 caracteres. Mídia: foto à esquerda
(`.viagem-foto`), opcional; sem ela, a árvore pode ir para a esquerda com `style="left: 120px"`.

```html
<section data-slide="pasta" data-arquetipo="viagem">
  <p class="rotulo">Pasta do caso</p>
  <h2 class="manchete">Os autos vão para a pasta do caso</h2>
  <img class="viagem-foto" src="midia/pasta.webp" alt="">
  <div class="arvore">
    <p class="no" data-nivel="0">caso-ficticio/</p>
    <p class="no" data-nivel="1" data-arquivo data-de="ob-contrato">contrato.pdf</p>
  </div>
  <p class="selo-ia">imagem gerada por IA</p>
</section>
```

### fios

Cada afirmação aponta para a sua fonte: até três fontes à esquerda e até quatro linhas na minuta, de até oito
palavras cada. Só o fio da linha com `.marca` é dourado, e a marca acende quando ele chega; ponha a marca no começo
da linha, porque o fio chega pela esquerda na altura dela. A linha sem `data-fonte` é sublinhada e a `.sem-fonte`
aparece. Sem mídia.

```html
<section data-slide="fonte" data-arquetipo="fios">
  <p class="rotulo">Revisão</p>
  <h2 class="manchete">Cada linha aponta para um documento</h2>
  <div class="fontes">
    <p class="no" data-arquivo id="fn-contrato">contrato.pdf</p>
  </div>
  <div class="minuta">
    <p class="cab">minuta.md</p>
    <p class="linha" data-fonte="fn-contrato"><span><span class="marca">12/03/2019</span> é a data do contrato.</span></p>
    <p class="linha"><span>O tribunal decide assim.</span></p>
    <p class="sem-fonte">sem fonte: conferir</p>
  </div>
</section>
```

### demonstracao

O vídeo toca numa moldura de navegador neutra, ao lado de uma nota de até 20 palavras, e para sozinho em cada
parada. Mergulhos são linhas da lista sem section, depois da demonstração; a legenda de cada um fica dentro da
`.tela` (`data-mergulho` é o id do mergulho, `data-x` e `data-y` em frações). Cada holofote novo chega cheio antes
de o anterior sair, e o último sai com a viagem ao slide seguinte. Mídia: gravação de tela feita no
claude_video_maker, com máscara e sem custo; vídeo do Gemini Omni custa e só com aprovação. Um mergulho com vídeo
longo pode passar de 3,5 s: declare `ritmoOk: 'motivo'` na linha dele (docs/palco.md, Oráculo).

```html
<section data-slide="demo" data-arquetipo="demonstracao" class="noite">
  <p class="rotulo">Demonstração</p>
  <h2 class="manchete">Funcionando, num caso fictício</h2>
  <div class="moldura">
    <div class="barra-nav"><i></i><i></i><i></i><u></u></div>
    <div class="tela">
      <video src="midia/demo.mp4" poster="midia/demo-capa.webp" muted playsinline preload="auto"></video>
      <p class="legenda" data-mergulho="demo-skill" data-x="0.27" data-y="0.40">o pedido curto abriu a skill</p>
    </div>
  </div>
  <p class="nota-lateral">Vídeo de exemplo, sobre um caso fictício.</p>
</section>
```

```js
{id: 'demo', titulo: 'Demonstração', video: [1.0, 2.4]},
{id: 'demo-skill', titulo: 'A skill', video: [0, 1.6],
 mergulho: {em: 'demo', x: 0, y: 0.03, f: 0.56, furos: [[0.03, 0.254, 0.208, 0.035]]}},
```

### fecho

A mensagem em duas linhas (spans) e até três passos do que a plateia faz agora; a trilha termina no anel do último
slide. A mensagem cresce até 150 px. Vai na noite. Sem mídia.

```html
<section data-slide="fim" data-arquetipo="fecho" class="noite">
  <p class="rotulo">Para levar</p>
  <h2 class="display fecho-msg"><span>Pedido claro,</span><span>material <span class="sinal">certo</span></span></h2>
  <ol class="fecho-passos"><li><b>1</b>Escreva o pedido.</li><li><b>2</b>Junte o material.</li></ol>
</section>
```

## O que a biblioteca não faz

Paralaxe, câmera inclinada, pulsos correndo pela trilha, `mix-blend-mode` ou `will-change` no `#mundo`, duotone por
filtro SVG ao vivo (a imagem já chega tratada pelo `./ap imagens`), notebook ou celular ilustrado como moldura,
rabisco à mão em toda parada e número ilustrativo gigante ficaram de fora de propósito: pesam no ensaio, cansam a
plateia ou fingem dado. O `will-change` também não entra nas peças do mundo, nem na foto da abertura, porque a camada
própria guarda a rasterização de quadros anteriores e o mesmo instante, revisitado, sai com outros pixels, o que
reprova o determinismo do `./ap sondar`. Animação continua função do tempo, e a cor só vem de `var()` do tema
(`./ap lint motor/cenas.css`).
