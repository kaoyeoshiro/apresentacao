# Motor de palco: apresentações ao vivo feitas por código

Design de 19/10/2026, a partir dos relatórios de pesquisa em `docs/pesquisa/` (síntese do Opus 5.5, relatório
consolidado e quatro notas de pesquisa com métricas do GitHub coletadas no mesmo dia).
Respostas do usuário: uso principal é o palco ao vivo, PDF basta como arquivo (sem PowerPoint editável), e o
piloto real é uma palestra sobre IA no Direito.

## 1. Decisão

Os relatórios comparam ferramentas prontas para quem vai escrever slides à mão. O Slidev venceu por
equilíbrio entre Markdown, componentes Vue e comunidade (49.127 estrelas, MIT, v53.0.0 em setembro de 2026);
o Motion Canvas, indicado como parceiro pelo relatório do Opus, aparece no levantamento do GitHub sem release
estável desde dezembro de 2024 e sem commits em 12 semanas, o que basta para descartá-lo. Nenhum dos
relatórios avaliou o caso deste repositório, em que o Claude dirige a peça e precisa conferir cada quadro.

O motor de palco é próprio e nasceu do motor HTML do claude_video_maker. Cada apresentação é uma composição em que o quadro é função
pura do tempo, com pontos de parada; o clique avança até a parada seguinte. Dessa escolha saem quatro produtos
do mesmo arquivo, sem conversão: o deck ao vivo, o vídeo (pelo renderizador quadro a quadro), o PDF com o estado
de cada parada e os stills da revisão visual. O Slidev ficou de fora porque as animações dele são transições
CSS controladas pelo navegador, que não se deixam renderizar quadro a quadro nem medir por um oráculo; o
reveal.js tem o mesmo limite. Deles vêm ideias, não código: tela do apresentador, movimento que leva um
elemento de um slide ao seguinte (o Auto-Animate do reveal.js) e o atalho de tela preta.

O custo é escrever o tocador e a tela do apresentador, que os frameworks dão prontos. São poucas centenas de
linhas e ficam sob o mesmo contrato de determinismo do resto do motor.

## 2. Contrato da composição

```js
import {palco} from '../../motor/palco.js';
palco({
  titulo: 'Nome da palestra',
  slides: [
    {id: 'abertura', passos: [1.4, 0.9], notas: 'O que dizer aqui.', segura: 3},
    {id: 'problema', passos: [1.2], camera: {x: 2400, y: 0, w: 1920, h: 1080}},
  ],
  desenhar: (t, ctx) => { /* posiciona o DOM no instante t */ },
});
```

A linha do tempo começa parada em t = 0. Cada slide tem `passos`, durações em segundos de trechos animados, e
cada passo termina numa parada. O primeiro passo de um slide inclui a entrada dele, inclusive o movimento de
câmera quando há `camera` (caixa do mundo que o slide enquadra, como no take único). `ctx` traz o slide atual,
o progresso de cada passo (`ctx.p(n)`, de 0 a 1), o tempo local do slide e `ocioso`, segundos desde a chegada
à parada, para movimento ambiente discreto. Nada de relógio, timer, aleatório sem semente ou CSS transition
na composição; o `./ap lint` barra.

## 3. Os quatro modos

No navegador comum, o tocador escala o palco de 1920×1080 para a janela, com tarjas pretas, e responde a seta,
espaço, Page Down e Page Up (é o que os passadores enviam), clique, B para tela preta, F para tela cheia, G
para o índice de slides e P para a tela do apresentador. Voltar pula para a parada anterior sem animação, como
no reveal.js. A tela do apresentador abre numa segunda janela e conversa pela `postMessage` (funciona até
abrindo o arquivo direto do disco), com slide atual, prévia da próxima parada, notas, cronômetro e relógio.

No renderizador (Chromium controlado), o tocador expõe `window.__seek` sobre uma linha de vídeo que segura
cada parada por `segura` segundos (padrão 2,5) e toca os passos entre elas; o `./ap video` gera o MP4
sem mudança no renderizador. `window.__palco` expõe as paradas para as ferramentas.

## 4. Ferramenta `./ap`

- `novo <slug> --tema <tema>`: cria `decks/<slug>/deck.html` a partir da demonstração.
- `paradas <deck>`: um PNG por parada e uma folha de contato, para a revisão visual.
- `sondar <deck>`: o oráculo do palco, que mede o DOM e os pixels em cada parada (seção 5).
- `pdf <deck>`: PDF com uma página por parada, para distribuição e contingência.
- `video <deck>`: atalho para o render pelo motor HTML, com desfoque opcional.
- `empacotar <deck> --saida <pasta>`: pasta autossuficiente para o palco, que abre com dois cliques e sem
  internet. Os módulos entram no HTML como mapa de importação com URLs `data:`, as fontes do Google são
  baixadas (todas OFL) e as imagens e vídeos referenciados são copiados. O pacote é conferido ao final, aberto
  por `file://` com a rede bloqueada, e leva junto o PDF de emergência.

## 5. Oráculo do palco

O oráculo do take único mede continuidade; o do palco mede legibilidade em projeção, que é onde decks gerados
por IA costumam falhar (slide cheio, texto pequeno, contraste fraco). Em cada parada, com ERRO e AVISO:

| Medida | Reprova |
|---|---|
| tamanho do texto na tela, já com zoom de câmera | ERRO abaixo de 24 px em 1080p; AVISO abaixo de 30 px |
| texto cortado pela borda do quadro | ERRO; AVISO quando invade a margem de segurança de 4% |
| texto que transborda a própria caixa | ERRO |
| blocos de texto sobrepostos | AVISO |
| palavras visíveis na parada | AVISO acima de 45; ERRO acima de 70 |
| contraste estimado entre a cor do texto e a mediana dos pixels da caixa | ERRO abaixo de 3:1; AVISO abaixo de 4,5:1 |
| passo longo demais, plateia esperando | AVISO acima de 3,5 s |

O contraste é estimativa: a mediana da caixa aproxima o fundo quando o texto ocupa menos da metade dela. O
oráculo vê regras de legibilidade, não beleza; a folha de contato e o olho continuam obrigatórios.

## 6. Fora desta primeira versão

Vídeo narrado com voz e trilha (a linha de vídeo já existe; falta ligar a narração do claude_video_maker),
PowerPoint, edição colaborativa e controle pelo celular. A palestra-piloto sobre IA no Direito começa depois do
motor, com briefing próprio (público, duração, mensagem, fontes), porque fatos e números só entram com fonte
lida na sessão.

## 7. Critério de pronto

O deck de demonstração passa no `sondar` sem erro, sai idêntico em renders repetidos, gera PDF e vídeo, e o
pacote abre por `file://` sem rede com fontes carregadas e sem requisição falha. Testes em
`tests/test_palco.py` cobrem a linha do tempo, os modos, o oráculo contra um deck ruim de propósito e o pacote.

## 8. Repositório próprio

O motor nasceu dentro do claude_video_maker e saiu dele no mesmo dia, para `/Volumes/Projetos/apresentacao`, que
absorve o repositório antigo `/Volumes/Projetos/apresentacoes` (GSAP, one take por atos). Do antigo vieram os temas
co.juris, PGE e o modelo, com o contrato de tokens, e as regras que custaram retrabalho: perguntar o tema e o modo,
ler `regras.md` antes de escrever, logo só recortado do arquivo oficial, `[CONFERIR]` no que não foi confirmado,
ato que termina parado. O antigo ficou intacto e parado. O claude_video_maker continua sendo a fábrica de
matéria-prima (vídeo por código, Omni, imagem pelo image-video-api), chamada pelas pontes `./ap imagem`,
`./ap video-ia` e `./ap trazer`.
