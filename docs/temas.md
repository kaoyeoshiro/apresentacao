# Temas: o contrato de um design system

Um tema é uma pasta `temas/<nome>/`, e trocar de cliente é trocar de pasta. O deck liga o tema por
`<link rel="stylesheet" href="../../temas/<nome>/tema.css">` e só usa os tokens abaixo, de modo que nenhum deck tem
hex de marca, nome de fonte ou caminho de logo. O contrato veio do repositório antigo `apresentacoes` e vale sem
mudança para os temas trazidos de lá (co.juris, PGE e o `_modelo`); o tema `noite`, escuro e sem marca, é o da
demonstração. Os testes `test_demo_com_tema_de_marca_passa_no_oraculo` (a demonstração com co.juris e PGE) e
`test_catalogo_passa_com_outros_temas` (o catálogo com noite e PGE) reprovam o tema ou o deck que quebrar
legibilidade.

## Arquivos

```
temas/<nome>/
  tema.css     tokens e @font-face; o único CSS que sabe de cor, fonte e logo
  marca/       logos oficiais, sempre recortados do arquivo original, fundo transparente
  fonts/       fontes com licença que permite redistribuir (OFL), woff2 ou ttf variável, com a licença ao lado
  regras.md    identidade, voz, o que precisa de fonte, pessoas e cargos, contraste medido
  imagem/      opcional: a série de imagens geradas (estilo.txt, proibidos.txt, padroes.toml, refs/mestra.png)
```

## Tokens obrigatórios em `:root`

| token | o que é |
|---|---|
| `--cor-fundo` | fundo dos slides |
| `--cor-tinta` | texto e títulos; também o fundo de bloco invertido |
| `--cor-destaque` | cor de marca para régua, ponto, número, o que chama o olho |
| `--cor-papel` | cartões e folhas, um degrau acima do fundo |
| `--cor-tinta-suave` | texto secundário sobre o fundo |
| `--cor-linha` | linhas finas e trilhos sobre o fundo |
| `--cor-destaque-fraca` | destaque diluído, para caixas e etiquetas |
| `--cor-sobre-tinta` | texto sobre `--cor-tinta` |
| `--cor-suave-sobre-tinta` | texto secundário sobre `--cor-tinta` |
| `--cor-linha-sobre-tinta` | linhas finas sobre `--cor-tinta` |
| `--fonte-titulo` | pilha de fontes dos títulos |
| `--fonte-texto` | pilha de fontes do texto |
| `--logo-marca` | `url(marca/...)` do logo principal; `url('data:,')` se o tema não tiver logo |
| `--logo-marca-proporcao` | largura / altura do logo, por exemplo `950 / 815` |

Opcionais que o deck deve respeitar quando existirem: `--titulo-caixa` (`none` na PGE, que só admite caixa alta em
rótulo curto; o deck aplica com `text-transform: var(--titulo-caixa, none)`), `--cor-destaque-texto` (destaque com
pelo menos 3:1 sobre o fundo, para texto grande; se faltar, vale `--cor-destaque`) e `--fonte-mono` (rótulos curtos;
se faltar, o deck cai em `--fonte-titulo`). Outros extras (`--logo-simbolo` da co.juris) são livres, e só os decks
daquele cliente os usam.

Toda variável com `url()` precisa ser registrada como `<url>` antes do `:root`, ou o navegador resolve o endereço
em relação à folha que usa a variável (o deck) e o logo dá 404:

```css
@property --logo-marca { syntax: '<url>'; inherits: true; initial-value: url('data:,'); }
```

## Cores derivadas

Num tema claro, cada derivada sai de `color-mix` a partir das três de marca, como na co.juris:
`--cor-tinta-suave` é `color-mix(in srgb, var(--cor-tinta) 72%, var(--cor-fundo))`, `--cor-linha` é
`color-mix(in srgb, var(--cor-tinta) 16%, transparent)` e assim por diante (ver `temas/_modelo/tema.css`). Num tema
escuro a mistura com o fundo sai lavada, e o `noite` escreve o suave e a linha em hex. O oráculo lê as cores como o
navegador as calcula, então qualquer das duas formas é medida.

## Contraste mínimo

Conferido com número, nunca a olho, e registrado em `regras.md`: tinta sobre fundo, 7:1; tinta suave sobre fundo,
4,5:1; sobre-tinta e suave-sobre-tinta sobre a tinta, 4,5:1; destaque sobre a tinta, 3:1, e só em elemento grande.
Cor de marca que não passa vira exceção escrita em `regras.md`, e o deck evita aquele uso. O `./ap sondar` mede o
contraste real de cada texto em cada parada (ERRO abaixo de 3:1, AVISO abaixo de 4,5:1 em texto menor que 40 px).

## Fontes e logos

Fontes locais, com licença que permite redistribuir, em `fonts/`, com `font-display: swap`. Se a fonte oficial da
marca não estiver confirmada ou licenciada, use uma parecida e registre em `regras.md` que é provisória (a
Montserrat da co.juris é). O logo é recorte do arquivo oficial com fundo transparente, nunca redesenhado nem gerado
por IA; `regras.md` diz sobre que fundos ele pode entrar, porque logo de tinta escura some em fundo escuro.

## Imagem

A pasta `imagem/` faz das imagens geradas uma série da marca, e o `./ap imagens` (o lado do deck vem no fim desta
seção) lê tudo dela, de modo que nenhum deck escreve estilo, mestra ou tratamento à mão. São quatro peças:

```
temas/<nome>/imagem/
  estilo.txt     bíblia da série, em inglês, prefixada a todo prompt; linha começando por # é comentário
  proibidos.txt  lista anticlichê da marca, um item por linha, com o termo do prompt entre parênteses
  padroes.toml   geradores que a marca permite e tratamento por papel (heroica, objeto, textura)
  refs/mestra.png  placa-mestra, a Image 1 de toda geração (PNG ou JPG: o image-video-api recusa WebP)
```

A bíblia descreve a série e nunca a cena, porque a cena vem do `imagens.toml` de cada deck. A da co.juris funciona
por seis decisões que o modelo em `temas/_modelo/imagem/estilo.txt` pede, na ordem. Primeiro o gênero numa frase
("quiet editorial still-life photography of everyday legal work"). Depois o tom em preto e branco com meios-tons
abertos, porque o tratamento descarta a cor do original e mapeia só a luminância na paleta do tema. Em seguida uma
luz só, com direção e queda ("one soft directional window light from the upper left"), que é o que mais costura
imagens diferentes, e a lente e a câmera sem inclinação. O quinto item é o vocabulário de materiais do mundo do
cliente (papel A4, pasta parda, elástico, grampo, carimbo, caneta, mesa de carvalho claro), objetos e não símbolos.
Por fim, o acabamento e as negativas: grão fino, nada de HDR, flare ou bokeh, nenhum texto, letra, número ou logo
(os modelos escrevem texto falso), nenhuma pessoa e a lista do `proibidos.txt`.

A mestra sai da própria bíblia. Uma entrada `mestra` no `imagens.toml` de um deck qualquer, com papel `textura` e
os materiais arrumados sob a luz da série, gera seis rascunhos (`--rascunhos mestra -n 6`); o usuário escolhe na
folha de candidatos, o `--final mestra=i` gera em 2K, e o `midia/originais/mestra.png` é copiado para
`temas/<nome>/imagem/refs/`. Sem mestra o comando gera, com aviso, e a série perde a âncora de luz e grão. Trocar a
mestra depois obriga a refazer as imagens derivadas.

No `padroes.toml`, `geradores` lista os backends do image-video-api que o usuário liberou para a marca (`gemini`,
`azure-gpt-image`, `azure-flux`, `ideogram-4-5`); entrada com outro backend é recusada. As tabelas
`[tratamento.<papel>]` aceitam as opções do `./ap tratar` (`tom`, `intensidade`, `largura`, `alfa`, `grao`,
`semente`, `niveis`, `gama`), e a entrada do deck sobrepõe só o que muda. Na co.juris, calibrados na prévia, a
heroica é duotone 0,8 com 2048 px e o objeto é duotone 0,8, recortado (`alfa`), com 900 px e gama 1,8, que põe o
papel em L* perto de 90 contra 98 do `--cor-fundo`. Papel sem tabela fica com o padrão do `./ap tratar`.

### O deck: `imagens.toml` e `./ap imagens`

Cada imagem do deck é uma entrada de `decks/<slug>/imagens.toml`, cujo prompt descreve só o objeto e a cena; repetir
a bíblia é erro, como também é erro a chave desconhecida. O comando monta o prompt enviado nesta ordem: a bíblia, a
mestra como Image 1 (com a frase que pede dela só a luz, o grão e a lente), uma frase por ref da entrada, o prompt e,
no final feito a partir de um rascunho, a frase do rascunho aprovado como última imagem. Ref escrita como texto é
referência de objeto, que o modelo copia em forma, cor e material; para outro uso, `{ arquivo = "...", uso = "..." }`,
em que `uso` completa a frase "Image N is". Toda ref é PNG ou JPG, com caminho a partir da pasta do deck.

```toml
[[imagem]]
nome = "heroi-aula2"     # obrigatório; vira midia/heroi-aula2.webp, com original em midia/originais/heroi-aula2.png
slide = "aula2"          # obrigatório; data-slide em que a imagem entra
papel = "heroica"        # obrigatório; heroica (tela cheia sob texto), objeto (recortado) ou textura (fundo)
prompt = """The same thin kraft cardboard case folder as the object reference, here closed, with the camera pointing
straight down ... the left half of the frame is one even dark tone. No text, no labels."""
refs = ["midia/originais/pasta-aberta.png"]   # opcional; texto é ref de objeto
zona_texto = [0, 0, 0.5, 1]   # opcional; onde vai o título, em frações x0, y0, x1, y1
tratamento = { gama = 1.4 }   # opcional; só o que foge de [tratamento.heroica] do padroes.toml
# backend = "gemini"    padrão; precisa estar em geradores do padroes.toml
# aspect = "16:9"       padrão; largura:altura
# resolucao = "2K"      padrão; 1K, 2K ou 4K
# preco_usd = 0.07      US$ por imagem, obrigatório para backend sem preço na tabela de ferramentas/imagens.py
```

```bash
./ap imagens decks/<slug>                                # situação e custo do que falta, sem gastar
./ap imagens decks/<slug> --rascunhos [nome ...] [-n 3]  # Gemini 1K e a folha storyboard/candidatos.png
./ap imagens decks/<slug> --final heroi-aula2=3 doc      # final na resolução do toml, tratado e creditado
./ap imagens decks/<slug> --tratar [nome ...]            # refaz só o tratamento, sem custo
```

A situação mostra, por imagem, os rascunhos, o original, o tratamento (`sim`, `não` ou `refazer`, quando o toml mudou
depois do último tratamento), a zona de texto e o custo do que falta. Os rascunhos custam US$ 0,0336 cada, caem em
`midia/originais/rascunhos/<nome>-<i>.png` em numeração contínua e entram na folha de candidatos, uma linha por imagem
e cada quadro rotulado `<nome>-<i>`; quem escolhe é o usuário. Sem nomes, `--rascunhos` só pega as imagens que ainda
não têm final. O `--final nome=i` gera na resolução do toml com o rascunho `i` como ref de composição, grava
`midia/originais/<nome>.png` (o anterior vai para `rascunhos/<nome>-antes-<k>.png`, com o crédito), trata, escreve
`midia/<nome>.webp` e registra prompt, refs, custo e tratamento no `creditos.json`.

Como `midia/originais/` fica fora do git, um checkout novo (outro worktree, ou o principal depois do merge) recebe só
os WebP e o `creditos.json`. O final de uma imagem é, portanto, o `midia/<nome>.webp`, e a situação conta como pronta
a imagem cujo WebP tem o tratamento pedido, com o original marcado `fora do git` e custo zero; o `--rascunhos` sem
nomes pula essas imagens. O original só faz falta ao `--tratar`, que lê o arquivo apontado pelo crédito do WebP e
assim refaz a prévia byte a byte, e às refs que apontam para `midia/originais/`. Nos dois casos o comando avisa e
pede a cópia de segurança, sem propor geração paga. A exceção é o marcador: o deck criado do catálogo traz WebPs
copiados da prévia com a nota "marcador: substitua por mídia do deck" no crédito, e uma entrada com o mesmo nome não
conta como pronta (a coluna `tratada` mostra `marcador`, o custo entra na conta e o `--final` substitui o crédito).

Antes de chamar o gerador, o comando soma o custo estimado pela tabela de `ferramentas/imagens.py` (Gemini 1K a
US$ 0,0336, 2K a 0,0504 e 4K a 0,113, lidos na página de preços do Google em 19/10/2026 e não reconferidos) e recusa
a execução inteira acima de `--teto`, que por padrão é US$ 2,00. Subir o teto exige mostrar o custo ao usuário e ter o
sim dele na conversa, e backend sem preço na tabela só gera com `preco_usd` na entrada e a fonte anotada no briefing.
As chamadas saem uma por vez, a pelo menos 6 s uma da outra; no limite de taxa (429) o comando espera o que a ponte
pedir, ou 30 s, em até três novas tentativas.

Com `zona_texto`, a imagem tratada é medida na área do título, reduzida a 640 px de largura para o grão sumir, e o
comando avisa acima de 0,08 de desvio de luminância ou de 0,3% de pixels de borda (gradiente acima de 6 níveis por
pixel). Na calibração, as heroicas da prévia mediram desvio de 0,050 e 0,019 na zona livre, com 0,04% e 0,02% de
bordas, enquanto o rascunho recusado pelo veio de madeira deu 0,63% e o da quina de mesa, 0,64%. O aviso se resolve
com outro rascunho ou pedindo a zona vazia no prompt.

Fora da série, `./ap imagem` chama o gerador uma vez, sem estilo, mestra nem trava de custo, e `./ap tratar` trata um
arquivo avulso. Os dois ficam para exceção declarada ao usuário, e imagem da série passa sempre pelo `./ap imagens`.

## Criar um tema novo

1. Pedir ao usuário o logo em arquivo original, as cores da marca (ou extraí-las do logo), as fontes oficiais e o
   que a marca nunca diz.
2. Copiar `temas/_modelo/` para `temas/<nome>/`, recortar o logo e conferir sobre fundo claro e escuro.
3. Escrever `tema.css`, derivar as cores e medir os contrastes; escrever `regras.md`.
4. Rodar o catálogo com o tema (`./ap novo _teste --tema <nome>`, `./ap sondar decks/_teste`, `./ap paradas
   decks/_teste`), repetir com `--modo slides` para a demonstração, olhar os stills e apagar as pastas de teste.
5. Se a marca vai ter imagem gerada, copiar `temas/_modelo/imagem/`, escrever a bíblia e a lista anticlichê,
   perguntar ao usuário quais geradores ele libera e gerar a mestra como descrito em Imagem.
