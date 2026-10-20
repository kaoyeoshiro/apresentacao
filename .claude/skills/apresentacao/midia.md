# Mídia

Imagem, foto e vídeo entram quando provam ou mostram o que o código não desenha bem, nunca para enfeitar. Todo
arquivo fica em `decks/<slug>/midia/`, com o crédito em `midia/creditos.json`, e o custo previsto vai na coluna mídia e
custo do roteiro. O contrato técnico está em `docs/palco.md`, seção Mídia, e a série de imagens em `docs/temas.md`,
seção Imagem.

## A escada, do mais barato ao mais caro

Suba um degrau só quando o de baixo não prova a ideia.

1. Código vivo no deck, sem custo. Os arquétipos já desenham leque, grade, placar, ramos, árvore, fios e moldura de
   vídeo; um gráfico próprio é SVG com `tracar` e número com `contar` (`docs/palco.md`, Ajudantes).
2. Imagem gerada e tratada nas cores do tema, pelo `./ap imagens`. Rascunho Gemini 1K a US$ 0,0336; final 2K a
   US$ 0,0504 e 4K a US$ 0,113 (tabela de `ferramentas/imagens.py`, lida em 19/10/2026 e não reconferida).
3. Captura de tela de sistema, sem custo, feita no claude_video_maker com os dados pessoais mascarados
   (`./cvm capturar <url ou arquivo> --saida <png> --mascarar-pii`, ou `--mascarar-processos`, `--tarjar SELETOR`; o
   comando reconfere e apaga o PNG se achar dado pessoal) e trazida com `./ap trazer`.
4. Vídeo feito por código no claude_video_maker, sem custo, trazido com `./ap trazer` (seção Vídeo, abaixo).
5. Clipe pago do Gemini Omni (`./ap video-ia`): só com o sim do usuário na conversa para aquele clipe e aquele custo.

## Regras de imagem

- Texto nunca vai dentro de imagem ou vídeo. Título, legenda e rótulo ficam no HTML, onde o oráculo mede e o tema dá a
  fonte; os modelos escrevem letra falsa, por isso todo prompt pede papel sem texto legível.
- Uma heroica por bloco, na abertura, sob o véu. No conteúdo, a imagem entra como objeto recortado com transparência
  sobre o papel (papel `objeto`, que o tema trata com `alfa`), nunca dentro de cartão ou moldura de interface.
- As imagens são uma série: mesma luz, mesma lente, mesmo grão, mesmas cores do tema. O mesmo objeto que aparece em
  dois slides (a pasta da abertura e a do conteúdo, na prévia) sai com a imagem do outro como ref de objeto.
- Todo slide com imagem gerada leva `<p class="selo-ia">imagem gerada por IA</p>` (no plural quando houver várias).
- Nunca logo (o logo é recorte do arquivo oficial, `var(--logo-marca)`), pessoa, rosto ou mão, foto de banco genérica
  nem item do `temas/<tema>/imagem/proibidos.txt`.
- Na heroica, a área do título fica vazia: o prompt pede a zona lisa ("keep the left 50% of the frame completely
  empty") e a entrada declara `zona_texto`, que o comando mede depois do final.

## A série do tema

`temas/<tema>/imagem/` guarda a bíblia de estilo (`estilo.txt`, em inglês, prefixada a todo prompt), a lista
anticlichê (`proibidos.txt`), os geradores liberados e o tratamento por papel (`padroes.toml`) e a placa-mestra
(`refs/mestra.png` ou `.jpg`, a Image 1 de toda geração). `cojuris`, `noite` e `pge` têm a pasta; só a `cojuris`
tem a mestra. Os geradores já estão no `padroes.toml` (nos temas novos, só o `gemini`, o único com preço na tabela) e
não se pergunta por eles: outro gerador entra só se o usuário pedir. Tema sem mestra: a mestra é a primeira linha do
`imagens.toml` do deck, gerada como em `docs/temas.md` (seção Imagem), com custo na coluna mídia e custo do roteiro e
escolha do usuário na folha de candidatos; o original vai para `temas/<tema>/imagem/refs/` e a entrada sai do deck.
Sem mestra o comando gera com aviso e a série perde a âncora; não aceite isso. Tema novo copia
`temas/_modelo/imagem/` e escreve a bíblia pelas seis decisões de `docs/temas.md`; num tema escuro, tire a `gama` do
tratamento de objeto, que acinzenta o papel sobre o fundo escuro. A heroica num tema escuro fica escura como na
prévia: o tratamento leva o preto da foto ao fundo e o branco à tinta, e o véu da abertura usa a cor da zona noite.

## Imagens do deck: `imagens.toml` e `./ap imagens`

Escreva uma entrada por imagem em `decks/<slug>/imagens.toml`. O prompt descreve só o objeto e a cena: o estilo do
tema, a frase da mestra e o tratamento entram sozinhos, e repetir o estilo é erro. Dê nomes novos às imagens do deck;
um nome igual ao de um marcador do catálogo (`heroi-aula1`, `doc-contrato`) funciona, porque o comando sabe que o
marcador não vale como final, mas nome próprio deixa o crédito mais claro.

```toml
[[imagem]]
nome = "heroi-abertura"   # vira midia/heroi-abertura.webp; original em midia/originais/heroi-abertura.png
slide = "abertura"        # data-slide em que a imagem entra
papel = "heroica"         # heroica (tela cheia sob o título), objeto (recortado) ou textura (fundo)
prompt = """Title-slide photograph, low-key. Subject: an open wooden index-card drawer full of blank cards, seen from \
a low three-quarter angle; one blank card is lifted slightly above the others and catches the light. Subject in the \
right third of the frame. Keep the left 50% of the frame completely empty: only the smooth dark background, no \
objects, no lines, no texture. All cards blank."""
resolucao = "4K"                 # 1K, 2K ou 4K (padrão 2K); aspect padrão "16:9"; backend padrão "gemini"
zona_texto = [0, 0, 0.42, 1]     # onde vai o título, em frações x0, y0, x1, y1

[[imagem]]
nome = "doc-pedido"
slide = "material"
papel = "objeto"
prompt = """A single A4 page with a faded round ink stamp made only of concentric rings, no letters, seen from \
straight above, isolated on a perfectly flat, evenly lit warm off-white seamless backdrop, only a very soft contact \
shadow. The page shows only faint grey lines, never legible text. The paper is bright white, clearly lighter than the \
backdrop."""
aspect = "3:4"
# refs = ["midia/originais/pasta.png"]   ref de objeto (PNG ou JPG, a partir do deck): o mesmo objeto de outro slide
# tratamento = { gama = 1.4 }            só o que foge do padroes.toml do tema
```

O fluxo, sempre nesta ordem:

```bash
./ap imagens decks/<slug>                          # situação de cada imagem e custo do que falta; não gasta
./ap imagens decks/<slug> --rascunhos -n 3         # três rascunhos 1K por imagem sem final e storyboard/candidatos.png
./ap imagens decks/<slug> --final heroi-abertura=2 doc-pedido=1   # final com o rascunho escolhido como composição
./ap imagens decks/<slug>                          # confira: tratada "sim", zona "ok", "N de N prontas"
```

Mostre `storyboard/candidatos.png` ao usuário: cada linha é uma imagem e cada quadro se chama `<nome>-<i>`, e quem
escolhe é ele. O `--final` gera na resolução do toml, trata nas cores do tema, grava `midia/<nome>.webp` e escreve o
crédito com prompt, refs, custo e tratamento. Aviso de zona de texto se resolve com outro rascunho ou pedindo a zona
vazia no prompt. Para mudar só o tratamento, edite o toml e rode `--tratar <nome>`, sem custo.

O comando soma o custo de cada execução e recusa tudo acima de `--teto` (US$ 2,00). Subir o teto exige mostrar o custo
ao usuário e ter o sim dele na conversa. Backend sem preço na tabela (GPT Image, FLUX, Ideogram) só gera com
`preco_usd` na entrada e a fonte do preço anotada no briefing. `midia/originais/` fica fora do git: num checkout novo,
os WebP com crédito já são os finais, e não se rascunha de novo o que está pronto.

`./ap imagem` e `./ap tratar` avulsos chamam o gerador ou tratam um arquivo sem estilo, mestra nem trava de custo;
ficam para exceção declarada ao usuário.

## Os marcadores do catálogo

O deck criado por `./ap novo` traz a mídia do catálogo, copiada da prévia e tratada para o cojuris:
`heroi-aula1.webp`, `doc-peticao.webp`, `doc-contrato.webp`, `doc-modelo.webp`, `pasta-aberta.webp`, `demo.mp4` e
`demo-capa.webp`, cada uma com a nota "marcador: substitua por mídia do deck" no crédito. Nenhuma pode ficar no deck
entregue, nem mesmo no tema cojuris, porque o assunto é outro. Para cada uma: troque pelo arquivo do deck e mude o
`src`, ou apague o slide; depois apague o arquivo-marcador e a entrada dele no `midia/creditos.json`. Sem custo, uma
imagem do mesmo tema já gerada para outro deck pode entrar, com o crédito copiado e a origem anotada.

Passa quando `grep -c marcador decks/<slug>/midia/creditos.json` dá 0 e este laço, rodado na pasta do deck, não
imprime nada além de "fim":

```bash
for f in midia/*; do case "$f" in */._*|*/creditos.json|*/originais) continue;; esac; grep -q "$f" deck.html || echo "sem uso: $f"; done; echo fim
```

## Vídeo

O vídeo entra no arquétipo `demonstracao`: toca numa moldura de navegador neutra, começa no clique e para sozinho em
cada parada, no mesmo quadro que sai no PDF. Mergulhos são linhas da lista sem section, depois da demonstração, que
levam a câmera para dentro do vídeo e acendem um holofote nos `furos`; a legenda de cada mergulho é uma `.legenda`
dentro da `.tela`, no HTML (`docs/cenas.md`, demonstracao).

Vídeo por código, sem custo:

1. No claude_video_maker (pasta vizinha, fora deste repositório: escrever lá pede o sim do usuário na conversa),
   escreva uma composição HTML em `videos/ap-<slug>/` pelo contrato do motor HTML de lá (`docs/motores.md`, seção
   HTML, com `engines/html/exemplos/ondas.html` de exemplo): a interface imitada, com dado fictício, em 2560 px de
   largura para o zoom do mergulho ficar nítido.
2. Renderize: `./cvm html videos/ap-<slug>/comp.html --saida videos/ap-<slug>/output/demo.mp4`.
3. Traga para o deck: `./ap trazer decks/<slug> <caminho do mp4> --origem "./cvm html, código próprio, caso fictício"
   --perfil demo --capa 0`, que prepara o vídeo para o palco (H.264, quadro-chave a cada 0,5 s, sem áudio) e grava a
   capa para o `poster`.
4. `./ap midia conferir decks/<slug>` sem ERRO.
5. Na lista de slides, `video: [de, dur]` diz que trecho cada clique toca. Passo acima de 3,5 s com o vídeo tocando
   leva `ritmoOk: 'motivo'` na linha do mergulho ou `data-ritmo-ok="motivo"` na section; digitação lenta no vídeo
   cansa a sala, e a prévia acelerou esses trechos em 2x com ffmpeg, registrando a aceleração no crédito.

Clipe pago, só com aprovação:

```bash
./ap video-ia decks/<slug> <nome> "prompt" --segundos 8 --resolucao 720p          # só orça e imprime o HASH
./ap video-ia decks/<slug> <nome> "prompt" --segundos 8 --resolucao 720p --aprovado HASH
```

Mostre ao usuário o custo e o que o clipe mostra, e rode com `--aprovado` só depois do sim dele para aquele clipe.

## Custo e créditos no briefing

O briefing tem uma tabela de mídia (arquivo, gerador, custo estimado) e a soma do que foi gasto, rascunhos incluídos,
como a da prévia. O `midia/creditos.json` guarda o resto: prompt integral, refs, parâmetros, tratamento e origem de
cada arquivo.
