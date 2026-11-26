# Estilo cinema: cena 3D atrás do texto

O terceiro estilo do repositório, ao lado do plano contínuo (`docs/cenas.md`) e dos slides com transições
(`docs/palco.md`). A apresentação acontece num mundo 3D desenhado em tempo real, com luz, névoa, reflexo no chão e
brilho, e a câmera viaja por ele a cada clique, como num plano de cinema. O texto continua no HTML, por cima, em
poucas palavras. A referência de nível é uma palestra que o usuário mostrou em 26/11/2026, em que o gráfico sai do
slide e vira uma torre de papel; a régua deste repositório é `decks/cojuris-cinema/`, prévia de cinco paradas na
marca co.juris.

Use quando o pedido falar em estilo cinema, cinematográfico, 3D, "nesse nível" de uma referência desse tipo, ou
quando a apresentação for curta e de impacto (abertura de aula, lançamento, palestra de 5 a 15 minutos). Para aula
longa com conteúdo denso, o plano contínuo continua sendo o padrão, e o cinema entra só nos momentos de abertura,
virada e fecho. Cada parada de cinema custa horas de ajuste de luz e câmera, e por isso a prévia tem cinco.

## A ideia vem antes do código

O que separa este estilo de um fundo 3D decorativo é uma metáfora visual única que atravessa a apresentação e se
transforma a cada clique. Na prévia da co.juris, um ponto dourado vira traço de circuito, sobe pelo sulco de uma
coluna clássica e acende a coluna inteira, que é o grafismo do próprio logo da marca. Antes de modelar qualquer
coisa, escreva no `briefing.md` a metáfora em uma frase e o que ela vira em cada parada; se a frase não existe, o
deck vira vitrine de efeitos. Não copie cena de referência (a torre de papel, o barco): a metáfora sai do assunto e
da marca do deck.

## Contrato

O deck é um deck comum do motor (`palco()` com `slides`, `cenas` e `desenhar`), sem `#mundo` e sem a biblioteca de
cenas. O 3D entra por `motor/cinema.js`, que usa o three.js r186 copiado em `motor/vendor/three/` (licença MIT ao
lado, com os complementos de pós-processamento e o espelho do chão, cujo `import 'three'` foi trocado pelo caminho
relativo para funcionar sem internet e no pacote).

```js
import {palco, surgir, molaAR, faixa, entradaSaida} from '../../motor/palco.js';
import {cinema, corDoTema, trajeto, respirar, fio, halo, ceu, poeira, lajes, Reflector, THREE} from '../../motor/cinema.js';

const C = cinema({fov: 38, brilho: {forca: 0.6, raio: 0.45, limiar: 0.9}});
const posar = trajeto([{pos: [..], alvo: [..], fov: 34}, ...]);   // uma pose a mais que slides: a do escuro inicial
function desenhar(t, ctx) {
  posar(C.camera, ctx.slide.i + entradaSaida(ctx.p(0)));         // o slide i viaja da pose i à pose i + 1
  respirar(C.camera, ctx.ocioso);
  // ... revelar fios, trocar cores e luzes em função de ctx.k('slide') ...
  C.desenhar();
}
palco({slides, cenas, desenhar, autoplay: true});
```

| peça | o que faz |
|---|---|
| `cinema({fov, exposicao, brilho, amostras})` | canvas `#cinema` de 1920×1080 no fundo do `#palco`, cena, câmera, brilho (bloom) e saída; devolve `{cena, camera, renderer, bloom, desenhar}` |
| `corDoTema('--token')` | a cor de um token do tema como `THREE.Color`, resolvida pelo navegador (inclusive `color-mix`) |
| `trajeto(poses)` | câmera por poses `{pos, alvo, fov}`, ligadas por Catmull-Rom centrípeta; recebe `u` de 0 a poses − 1 |
| `respirar(camera, ocioso, {amp})` | deriva lenta de câmera parada, de ruído com semente, que entra em 1,5 s |
| `fio(pontos, {raio, cor, intensidade})` | traço de luz por segmentos retos, com `userData.revelar(k, de)` e `userData.ponta(k)` |
| `halo(cor, {tamanho, intensidade})` | brilho aditivo, sem teste de profundidade, para a ponta de um fio ou uma lâmpada |
| `ceu({topo, horizonte})` | esfera em gradiente; as cores são uniforms que o deck troca em t |
| `poeira({n, caixa, semente, cor})` | grãos de luz que flutuam; `userData.desenhar(t + ocioso)` |
| `lajes({lado, semente})` | textura de piso em lajes, em tons de cinza (a cor vem do material) |
| `Reflector`, `THREE` | o espelho de chão do three.js e o próprio three.js, para o resto |

## Regras

- O quadro é função do tempo, como no resto do motor. A cena é montada uma vez no carregamento, e o `desenhar(t, ctx)`
  só move, revela e troca cor. Nada de `Clock`, `AnimationMixer`, `requestAnimationFrame` próprio ou `Math.random`; a
  geração procedural usa `aleatorio(semente)`. Movimento parado usa `ctx.ocioso`, que o palco faz andar ao vivo.
- Texto nunca vai para dentro do 3D. Fica no HTML, medido pelo oráculo, com uma sombra local (gradiente da tinta do
  tema) que entra junto com ele. Manchete de até seis palavras em Montserrat caixa alta, no canto que a câmera deixa
  vazio; o enquadramento de cada pose é escolhido para isso.
- Cor só de token do tema, por `corDoTema`. Tons de noite e de aurora saem de misturas desses tokens. O molde
  escurece a `--cor-tinta` para fazer a noite e usa a `--cor-fundo` como o dia, então pede tema de fundo claro e
  tinta escura (cojuris, pge); num tema escuro como `noite`, troque os papéis dos dois tokens no deck.
- Logo continua sendo o recorte oficial no HTML, sobre fundo claro, nunca modelado em 3D.
- O passo longo é a viagem da câmera e pode ir a 5,5 s. Declare `data-ritmo-ok="motivo"` na seção; o oráculo aceita
  a isenção porque o canvas `#cinema` está no quadro (`docs/palco.md`, Oráculo).
- Tone mapping neutro (`THREE.NeutralToneMapping`) quando o deck termina no claro da marca: o ACES puxa o off-white
  para o cinza.
- Transição de noite para dia passa por uma cor intermediária quente; a mistura direta de marinho e off-white dá um
  cinza morto no meio da viagem.

## Conferir

Os comandos são os mesmos de todo deck, e o 3D sai nos stills, no PDF, no vídeo e no pacote porque o renderizador
headless tem WebGL.

```bash
./ap lint decks/<slug>
./ap sondar decks/<slug>              # o canvas conta como imagem do quadro inteiro
./ap paradas decks/<slug> --viagens   # olhe o meio das viagens: é onde o cinema erra (cinza, corte, câmera dentro de objeto)
./ap empacotar decks/<slug>           # 17 módulos e cerca de 4 MB, abre sem internet
./ap video decks/<slug>               # a melhor forma de mostrar a prévia a quem não está na frente do projetor
```

O que a revisão olha, além da rubrica de `critica.md`: brilho estourado (o bloom acima de 0,7 lava a cena), linha
dura no horizonte (a cor do horizonte do céu precisa ser a da névoa), ação escondida atrás da manchete, objeto
cortado na borda do quadro na parada final, e o quadro do meio de cada viagem.

## Limites

O deck pesa na placa de vídeo: espelho do chão e brilho renderizam a cena mais de uma vez por quadro. Num Mac com
chip M o ao vivo roda liso; num notebook antigo de sala de aula, ensaie antes e, se engasgar, baixe `amostras` e a
resolução do espelho. O PDF de emergência do pacote tem as paradas como imagem. O oráculo não vê dentro do 3D: ele
mede o texto e o contraste sobre o quadro renderizado, e a beleza da cena fica com a folha de contato e o vídeo.
