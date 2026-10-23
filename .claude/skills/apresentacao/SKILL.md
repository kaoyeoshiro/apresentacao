---
name: apresentacao
description: Produz apresentações ao vivo de alto impacto feitas por código (motor de palco), para projetar com passador de slides, no nível da prévia aprovada do curso de IA. Plano contínuo por padrão, montado com a biblioteca de arquétipos (a câmera viaja por uma trilha dourada, um clique por slide abre tudo com animação), imagens geradas em série e tratadas nas cores do tema, vídeo dentro do slide, tela do apresentador, PDF de contingência e pacote que roda sem internet. Use para "faz uma apresentação", "slides para minha palestra", "deck para a aula", "apresentação animada", "transforma isso em slides", "palestra sobre X", ou para revisar por que um deck parece PowerPoint de modelo. Não use para .pptx editável nem para vídeo narrado.
---

# apresentacao

A sessão é diretora de arte, roteirista, programadora e revisora. O deck é código em `decks/<slug>/deck.html`, e a
apresentação existe para alguém falar na frente dela: a tela carrega imagem, número e frase curta, a fala carrega o
argumento. A régua de qualidade é a prévia que o usuário aprovou, `decks/previa-curso-ia/` (14 slides, um clique cada,
trilha dourada contínua, partitura de claro e escuro, imagens em série, vídeo dentro do slide).

O modo padrão é o plano contínuo, montado a partir do catálogo `decks/catalogo/` com a biblioteca `motor/cenas.js` e
`motor/cenas.css`. A biblioteca já faz o mundo, a trilha, as zonas noite, as viagens de câmera, a duração de cada
clique e doze arquétipos de slide; o deck escreve só o conteúdo. Use a biblioteca antes de escrever qualquer maquinário
próprio, e comece cada slide escolhendo o arquétipo no roteiro.

Leia cada referência no passo em que ela entra: `roteiro.md` (passo 4), `midia.md` (passo 6) e `critica.md` (passo 7),
nesta pasta. Os contratos técnicos ficam em `docs/cenas.md` (arquétipos, andamentos, peças), `docs/palco.md` (motor,
ferramentas, oráculo, mídia) e `docs/temas.md` (tema e série de imagens).

## O que perguntar e o que decidir sozinha

Pergunte com a ferramenta de perguntas, no máximo três por vez, a opção recomendada primeiro e com o motivo:

- tema: um de `temas/` (`ls temas | grep -v '^_'`), nunca herdado do deck anterior; tema novo se cria antes de tudo,
  pela seção "Criar um tema novo" de `docs/temas.md`;
- modo: "Plano contínuo (Recomendado)", em que a câmera viaja por uma trilha entre os slides, ou "Slides com
  transições", mais simples, para deck curto ou conteúdo sem fio entre os slides;
- público, duração e a mensagem que a plateia leva em uma frase, se o pedido não disser.

Depois disso, só três coisas voltam ao usuário: o roteiro, porque é texto que o público vê; a escolha entre os
rascunhos de imagem; e qualquer custo acima do teto do `./ap imagens` (US$ 2,00 por execução) ou clipe de vídeo pago.
O resto a sessão decide e anota no briefing: arquétipo, andamento, ordem dos cliques, enquadramento, tratamento de
imagem, correções da crítica e dúvidas técnicas.

## Passos

Cada passo termina num critério que se confere. Não avance com o critério em aberto.

### 1. Perguntar e ver a régua

Faça as perguntas acima. Gere e abra o storyboard da prévia (fica fora do git), para calibrar o olho:

```bash
./ap paradas decks/previa-curso-ia --viagens
```

Abra com a ferramenta Read `decks/previa-curso-ia/storyboard/folha.png` e `viagens.png`. Se `./ap` reclamar do
ambiente Python, rode `./ap sync` uma vez.

Passa quando: tema, modo, público, duração e mensagem estão respondidos, e as duas folhas da prévia foram abertas.

### 2. Criar o deck

```bash
./ap novo <slug> --tema <tema>                  # plano contínuo: copia decks/catalogo
./ap novo <slug> --tema <tema> --modo slides    # só se o usuário escolheu slides com transições
./ap sondar decks/<slug>
```

O deck novo traz os 13 slides do catálogo (um por arquétipo e um mergulho), o `briefing.md` do catálogo e a
mídia-marcador dele, com crédito. No modo slides, o molde é `decks/demo/` e vale `docs/palco.md` no lugar de
`docs/cenas.md`; os passos 3 a 9 são os mesmos.

Passa quando: `./ap sondar decks/<slug>` termina com "0 erro(s)" antes de qualquer mudança, o que prova o ambiente e o
tema.

### 3. Briefing e apuração

Reescreva `decks/<slug>/briefing.md`, que ainda fala do catálogo: público, duração, ocasião, a mensagem em uma frase,
o que a plateia faz ou decide no fim, tema, modo e prazo. Leia `temas/<tema>/regras.md` antes de escrever qualquer
texto, porque ele manda em voz, grafia de nomes e cargos, avisos obrigatórios e no que a marca nunca diz.

Cada número, nome, lei, data e caso vem de fonte lida nesta sessão e fica anotado no briefing ao lado do slide que o
usa. O que não tiver fonte sai do deck; o que ficou por confirmar aparece na tela com `[CONFERIR]` numa `.pilula`; o
exemplo ilustrativo leva a pílula "ilustrativo". Material do usuário que não abrir: diga onde tentou e não invente o
conteúdo. Telas de sistema real só entram por captura mascarada (`midia.md`).

Passa quando: o briefing não menciona mais o catálogo, e todo dado previsto tem fonte, `[CONFERIR]` ou "ilustrativo"
anotado ao lado.

### 4. Roteiro com um arquétipo por slide

Leia `roteiro.md`. Escreva no briefing o arco e a tabela do roteiro (slide, manchete, o que a tela prova, clima e
densidade, arquétipo, mídia e custo). O arquétipo de cada slide sai da função dele no arco, pela seção Arquétipos de
`docs/cenas.md`, que diz também a densidade máxima de cada um. Mostre o roteiro ao usuário e espere o sim antes de
construir.

Passa quando: a lista de conferência do fim de `roteiro.md` fecha (o que ficar de fora tem motivo escrito no
briefing), cada linha da tabela cabe na sua faixa de densidade (respiro até 12 palavras, nenhuma parada acima de 45)
e o usuário aprovou o roteiro.

### 5. Montar a partir do catálogo

Trabalhe sobre o deck copiado, nunca do zero. Para cada linha do roteiro, use a section do catálogo com aquele
arquétipo: troque o texto e os `data-*` (o contrato de cada um está em `docs/cenas.md`), o `data-slide` e a linha da
lista `slides` no fim do arquivo. Arquétipo repetido no roteiro: copie a section e dê outro id. Slide do catálogo que o
roteiro não usa: apague a section e a linha; ao apagar a demonstração, apague também a linha do mergulho dela.

- A ordem dos slides é a da lista. `class="noite"` segue a coluna clima do roteiro.
- `andamento` só se escreve para mudar o sentido de uma passagem: `corte` quando o assunto muda, `capitulo` no
  respiro que fecha uma parte. O resto sai do padrão da biblioteca.
- Cada slide tem `notas` para leitura de relance e `titulo` curto; `segura: 3` ou 4 na abertura e no fecho.
- Aula com blocos: `blocos` e `bloco` dão a linha do dia e o ritmo na tela do apresentador, `notas: {diga, faca, transicao}` o guia, `pratica: N` o cronômetro e `autoplay: true` a abertura sozinha (`docs/palco.md`, Blocos da aula).
- Texto sempre no HTML (o oráculo mede o HTML), dados em `data-*`, cor só por `var()` do tema. Reescreva também o
  comentário do topo do arquivo e o `<title>`.
- Monte primeiro a abertura, o slide mais denso e um slide com dado; rode `./ap sondar` e `./ap paradas` neles e
  corrija o sistema visual antes de seguir. Erro de sistema achado no fim custa o deck inteiro.

Cena própria só quando nenhum arquétipo conta aquilo (na prévia, um slide em 14: o pedido que vira arquivo). A
section vai sem `data-arquetipo` (um nome fora da biblioteca para o deck com erro), e a cena entra por
`m.cenas({id: (t, c) => {...}})`, com `conteudo`, `titulo` e `fim` de `motor/cenas.js` para o mesmo ritmo dos
arquétipos e os ajudantes de `docs/palco.md`; o exemplo está em `docs/cenas.md`, seção Cena própria. Trilha, câmera,
zonas noite e viagens continuam com a biblioteca; nunca reescreva esse maquinário no deck.

Passa quando: `./ap lint decks/<slug>` diz "lint: tudo certo"; `./ap sondar decks/<slug>` termina sem ERRO; e
`grep -o "titulo: '[^']*'" decks/<slug>/deck.html` lista exatamente os slides do roteiro, na ordem dele.

### 6. Mídia

Leia `midia.md` e suba a escada de mídia do mais barato ao mais caro. Imagem gerada sai do `./ap imagens`, a partir de
`decks/<slug>/imagens.toml`:

```bash
./ap imagens decks/<slug>                          # situação e custo, sem gastar
./ap imagens decks/<slug> --rascunhos -n 3         # rascunhos e storyboard/candidatos.png
./ap imagens decks/<slug> --final nome=2 outra=1   # com a escolha do usuário na folha de candidatos
./ap midia conferir decks/<slug>
```

Todo tema de `temas/` tem a série em `imagem/` (bíblia, lista anticlichê e `padroes.toml`, com os geradores
liberados), mas `noite` e `pge` ainda não têm a mestra. Sem ela o comando gera com aviso; não aceite isso: a mestra
entra como primeira linha do `imagens.toml` (`docs/temas.md`, seção Imagem), com o custo dela na coluna mídia e custo
do roteiro, e é escolhida na mesma folha de candidatos. Depois de copiada para `temas/<tema>/imagem/refs/`, a entrada
e os arquivos dela saem do deck. Tema novo copia `temas/_modelo/imagem/` antes da primeira imagem.

Mostre `storyboard/candidatos.png` ao usuário e gere o final com a escolha dele. Vídeo por código vem do
claude_video_maker por `./ap trazer` e entra no arquétipo demonstracao. Cada marcador do catálogo é trocado pela mídia
do deck ou sai com o slide, e a entrada dele sai do `midia/creditos.json`.

Passa quando: `./ap imagens decks/<slug>` termina em "N de N prontas" sem nenhuma linha AVISO (se o deck tem imagem
gerada); `./ap midia conferir decks/<slug>` dá "0 erro(s)"; `grep -c marcador decks/<slug>/midia/creditos.json` dá 0;
e todo slide com imagem gerada tem `.selo-ia`.

### 7. Crítica, no mínimo três rodadas

Leia `critica.md` e siga o procedimento de lá a cada rodada:

```bash
./ap sondar decks/<slug>
./ap paradas decks/<slug> --viagens
```

Abra com Read a folha de contato (`storyboard/folha.png`), cada still (`storyboard/parada-NN-<id>.png`) e a folha das
viagens (`storyboard/viagens.png`), e o PNG inteiro do quadro de viagem onde algo parecer errado. Responda a rubrica,
nomeie os piores defeitos e corrija os três maiores. Registre cada rodada numa seção "Crítica" do briefing (defeito,
evidência, correção). Quando a sessão puder despachar um subagente, use o prompt pronto de `critica.md`, que olha o deck
sem o viés de quem o fez; senão, a própria sessão aplica a rubrica, na mesma ordem.

Passa quando: há pelo menos três rodadas registradas e a última não achou defeito de gravidade alta ou média;
`./ap sondar` termina sem ERRO; e cada AVISO restante foi corrigido, isento no HTML com motivo (`data-contraste-ok`,
`data-ritmo-ok`, `ritmoOk`) ou justificado no briefing.

### 8. Ensaio ao vivo com o usuário

```bash
./ap abrir decks/<slug>
```

Abre no Chrome. Peça ao usuário que passe o deck inteiro pelo passador ou pelas setas, com a tela do apresentador
aberta (P), e que diga o que muda. Pedido de mudança volta ao passo 5 ou 6 e passa de novo por uma rodada do passo 7.

Passa quando: o usuário aprovou o deck ao vivo.

### 9. Entrega

```bash
./ap empacotar decks/<slug>   # pacote/ que abre sem internet, com o PDF de emergência
./ap pdf decks/<slug>         # se o usuário quiser o PDF à parte
./ap video decks/<slug>       # só se pedido
```

`pdf` e `empacotar` recusam deck com `[CONFERIR]` e listam cada ocorrência; `--rascunho` gera assim mesmo, só para
ensaio. Diga ao usuário onde está o pacote e como abrir: dois cliques em `apresentacao.html` no Chrome, F tela cheia,
P tela do apresentador, o passador funciona como as setas. Peça um ensaio no computador e no projetor do evento, com a
luz da sala acesa, porque o projetor lava o marinho. Liste as pendências: `[CONFERIR]` restantes, fonte provisória do
tema, avisos aceitos e o gasto de mídia somado do `midia/creditos.json`.

Passa quando: `./ap empacotar decks/<slug>` termina em "pacote: ok, abre sem internet".

## Proibido

- Fato sem fonte; logo redesenhado ou gerado por IA; pessoa real, foto de banco genérica ou ícone como decoração.
- Texto dentro de imagem ou vídeo, lista de tópicos como layout, parágrafo em slide, texto abaixo de 30 px.
- Cor, fonte ou logo escritos no deck: só `var()` do tema.
- Animação fora do tempo: `setTimeout`, `Date.now()`, `Math.random()` sem semente, CSS transition (o lint barra).
- Paralaxe, câmera inclinada, pulsos correndo pela trilha, `mix-blend-mode` ou `will-change` no `#mundo`, filtro SVG
  de duotone ao vivo, notebook ou celular ilustrado como moldura, rabisco à mão em toda parada, número ilustrativo
  gigante (`docs/cenas.md`, "O que a biblioteca não faz").
- Recurso da internet em tempo de palco: fonte, vídeo, imagem e iframe ficam locais no pacote.
- Gerar clipe pago (Omni, Veo) sem o sim do usuário para aquele clipe e aquele custo; subir o `--teto` do
  `./ap imagens` sem o sim dele; gerador que o `padroes.toml` do tema não libera.
- Copiar código ou texto do onetake (PolyForm Noncommercial).
