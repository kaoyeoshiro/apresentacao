# Motor de palco

Apresentação ao vivo em que cada quadro é função pura do tempo, com paradas. O clique toca o trecho animado até a
parada seguinte; o mesmo arquivo vira vídeo, PDF e stills de revisão. A decisão de fazer motor próprio, em vez de
Slidev ou reveal.js, está em `docs/decisao.md`. O protocolo de produção de uma apresentação está na skill
`.claude/skills/apresentacao/SKILL.md`, o contrato dos temas em `docs/temas.md`; este documento é o contrato técnico.

## Estrutura de um deck

`decks/<slug>/deck.html`, com mídia em `decks/<slug>/midia/` e o crédito de cada arquivo em `midia/creditos.json`.
Saídas (`output/`, `storyboard/`, `pacote/`) e `cache/` ficam fora do git. A demonstração `decks/demo/` é o molde
(`./ap novo <slug> --tema <tema>`). Cor, fonte e logo vêm de `<link rel="stylesheet" href="../../temas/<tema>/tema.css">`
e o deck só usa os tokens do contrato.

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
| P | tela do apresentador (agora, próxima parada, notas, cronômetro, relógio) |
| ? | atalhos |

A posição fica no endereço (`#parada=N`), então recarregar a página não perde o lugar. A tela do apresentador
conversa com o palco por `postMessage` e funciona também no pacote aberto por arquivo.

## Ferramentas

```bash
./ap novo <slug> --tema noite|cojuris|pge
./ap abrir decks/<slug>
./ap sondar decks/<slug>
./ap paradas decks/<slug>
./ap pdf decks/<slug>
./ap video decks/<slug> --paginas 3
./ap empacotar decks/<slug>
```

`pdf` e `empacotar` recusam deck que ainda tem `[CONFERIR]` no `deck.html` (texto, comentário ou código) e listam
cada ocorrência com a linha; `--rascunho` gera assim mesmo, para ensaio, nunca para a plateia.
`paradas` grava um PNG por parada e a folha de contato em `storyboard/`. `pdf` gera uma página por slide, no estado
final (`--todas` para uma por parada), em 13,33 × 7,5 polegadas. `video` usa o renderizador (`./ap render`) com a linha de vídeo,
que segura cada parada `segura` segundos e toca os passos entre elas. `empacotar` gera `pacote/` com
`apresentacao.html`, o tema e as fontes locais, as do Google baixadas se o deck usar (só latin e latin-ext), a mídia,
o PDF de emergência e um LEIA-ME. Só entram arquivos da pasta do deck, de `temas/` e de `motor/`, nunca de `cache/`
nem ocultos; depois abre o pacote por `file://` com a rede bloqueada e falha se alguma fonte, imagem, vídeo, a seta → ou
a tela do apresentador não funcionar.

## Oráculo (`sondar`)

Mede o DOM e os pixels em cada parada e sai com código 1 se houver ERRO.

| medida | ERRO | AVISO |
|---|---|---|
| tamanho do texto na tela, com zoom | abaixo de 24 px | abaixo de 30 px |
| borda do quadro | texto cortado | dentro da margem de 4% |
| caixa do texto | o texto transborda (descontada a folga natural da fonte acima da entrelinha) | |
| topo das letras, medido pela tinta da primeira linha, contra o pai que corta (`overflow` diferente de `visible`) | o pai apaga o topo (acento de maiúscula em título justo dentro de `.corte`; a correção é `padding-top` no pai) | |
| opacidade numa parada | | entre 0,1 e 0,9 (animação que não terminou) |
| contraste com a mediana do anel em volta da caixa | abaixo de 3:1 | abaixo de 4,5:1 em texto menor que 40 px |
| sobreposição de blocos de texto | | mais de 10% do menor |
| palavras visíveis | acima de 70 | acima de 45 |
| movimento nos últimos 40 ms antes da parada, descontada a transição | | mais de 1,5 px |
| duração de um passo | | acima de 3,5 s |
| determinismo (até 8 paradas, em outra ordem e em página nova) | quadro diferente | |

O contraste é estimativa e pode errar sobre foto; o oráculo vê legibilidade, não beleza. Os limiares estão no
topo de `ferramentas/palco.py`, e o deck ruim de `tests/fixtures/palco_ruim/` prova que cada regra reprova.

## Mídia

Imagens e clipes vêm dos repositórios vizinhos e caem em `decks/<slug>/midia/`, cada um com o crédito em
`midia/creditos.json` (ferramenta, modelo, prompt, custo, origem, data). Originais e rascunhos ficam em
`midia/originais/`, que está no `.gitignore` por pesar demais: no git entram só os arquivos que o deck usa e o
`creditos.json`, e os originais precisam de cópia fora do repositório antes de apagar a pasta.

```bash
./ap imagem decks/<slug> mapa "prompt" --aspect 16:9 --resolucao 2K [--backend gemini] [--ref ref.png]
./ap video-ia decks/<slug> abertura "prompt" --segundos 8 --resolucao 720p [--imagem quadro.png]
./ap video-ia decks/<slug> abertura "prompt" ... --aprovado HASH
./ap trazer decks/<slug> ../claude_video_maker/videos/x/output/clipe.mp4 --origem "./cvm html, código próprio"
```

`imagem` usa o image-video-api pelo `./cvm imagem` do claude_video_maker (GPT Image por padrão, Gemini com
`--backend gemini`); cada `--ref` precisa ser PNG ou JPG, porque o image-video-api recusa WebP. `video-ia` usa o Gemini Omni pelo `./cvm veo`: sem `--aprovado` só imprime o orçamento e o
hash, e gerar exige o sim do usuário na conversa para aquele clipe e aquele custo. O clipe é gerado em
`claude_video_maker/videos/ap-<slug>/public/clipes/`, onde fica o orçamento, e copiado para o deck. `trazer`
copia um arquivo pronto (vídeo por código do `./cvm html`, Remotion ou Manim; foto com licença). O caminho do
claude_video_maker é a pasta vizinha, ou `CVM_PROJETO`.
