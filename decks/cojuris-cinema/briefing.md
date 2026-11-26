# co.juris em cinema: prévia do estilo

Prévia curta, pedida em 26/11/2026, para mostrar o estilo cinema (`docs/cinema.md`) na marca co.juris. Serve também
de molde do `./ap novo <slug> --modo cinema`. Não é ainda uma apresentação de evento: as frases são provisórias e
passam pelo usuário antes de qualquer uso público.

- Público: abertura de curso ou de palestra da co.juris.
- Duração: cerca de 40 segundos, cinco paradas, a primeira tocada sozinha ao abrir.
- Mensagem: a IA entra no Direito pela tradição dele, e a co.juris ensina esse caminho.
- Tema: `cojuris`. Estilo: cinema.

## Metáfora

A coluna clássica com trilhas de circuito douradas, que é o grafismo do logo (`temas/cojuris/regras.md`, "trilhas de
circuito douradas e coluna clássica"). Um ponto dourado no escuro vira traço de circuito no chão, chega à base da
coluna, sobe por um sulco, acende todos os sulcos e a rede do chão, e o dia clareia até o papel da marca, onde entra o
logo oficial.

## Roteiro

| parada | manchete | o que a tela mostra | clima |
|---|---|---|---|
| ponto | IA NA PRÁTICA JURÍDICA (rótulo) | um ponto dourado no chão escuro, a coluna ao fundo | noite |
| fio | Achar o fio da meada. | o traço corre pelo chão até a base da coluna | noite |
| coluna | A tradição segura o peso. | contra-plongée: o traço sobe por um sulco até o capitel | noite |
| circuito | A IA sobe pela tradição. | todos os sulcos e a rede do chão acesos, a coluna inteira | noite |
| fecho | logo e "Curso presencial de IA aplicada ao Direito" | o dia clareia; logo sobre o papel da marca | dia |

## Fontes

- "IA na Prática Jurídica": nome do curso, no site da co.juris (`public/obrigado.html` e `public/apostila.html`,
  descrições das páginas), lido em 26/11/2026.
- "Curso presencial de IA aplicada ao Direito": descrição da página inicial do site da co.juris, lida em 26/11/2026.
- Logo: `temas/cojuris/marca/logo-vertical.png`, recorte oficial, sobre fundo claro.
- As manchetes são frase de marca, sem dado, número ou norma.

## Oráculo

`./ap sondar decks/cojuris-cinema`: 0 erro e 1 aviso. As quatro viagens passam de 3,5 s e estão isentas por
`data-ritmo-ok`, porque a viagem da câmera é o conteúdo. O aviso que fica é a sequência de quatro slides escuros com
poucas palavras: o arco inteiro é uma noite que vira dia num clique só, e acender a cena antes quebraria a metáfora.

## Crítica

1. Primeira renderização: brilho estourado (bloom 0,95 e luz da ponta 10), linha dura no horizonte e ação escondida
   atrás da manchete. Brilho caiu para 0,6, a luz da ponta para 2, o horizonte do céu passou a ter a cor da névoa e
   a manchete do fio foi para o alto, com a câmera recuada para mostrar o traço inteiro.
2. Halo da ponta cortado ao meio pelo chão, "dentes" na base da coluna (trilhas apagadas dos sulcos) e chão sem
   escala. O halo deixou de testar profundidade, as trilhas apagadas dos sulcos saíram e o chão ganhou lajes.
3. Coluna cortada no alto da parada 4 e texto sobre a rede do chão; meio do amanhecer num cinza morto. A câmera da
   parada 4 recuou, a manchete foi para o alto, e o amanhecer passa por uma aurora dourada.
