# Como construir um bloco da Aula 2

Leia antes, nesta ordem: `decks/curso-ia-aula2/briefing.md` (o roteiro, o caso fictício, os fatos e os textos exatos),
`docs/cenas.md` (a biblioteca de cenas), `docs/palco.md` (ajudantes, oráculo, blocos da aula) e, como exemplo vivo de
cenas próprias, `decks/curso-ia-aula1/deck.html` (cenas `partes`, `queda`, `memoria`, `ranking`, `cartoes`, `legal`,
`placar`; procure o CSS e o JS de cada uma). Regras do projeto em `CLAUDE.md` e `temas/cojuris/regras.md`.

## Arquivos do seu bloco (só estes; não edite `base.*`, nem outro bloco, nem `deck.html`)

Para o bloco `X` (por exemplo `a-pedir`), em `decks/curso-ia-aula2/fonte/`:

- `X.css`: só classes com o prefixo do bloco (`a-`, `b-`, `c-`, `d-`, `e-`, `f-`) e seletores `[data-slide="id"]`.
  Cor, fonte e logo só por `var()` do tema (`--cor-tinta`, `--cor-destaque`, `--cor-linha`, `--sobre-noite`...). Cor
  literal reprova no `./ap lint`. Texto nunca abaixo de 30 px.
- `X.html`: as `<section data-slide="id" data-arquetipo="...">` do bloco, na ordem. Cena própria: section sem
  `data-arquetipo`. Slide de noite: `class="noite"`. O texto fica no HTML, não no script.
- `X.slides.js`: `SLIDES.push({...}, {...})` com uma entrada por slide: `id`, `titulo` (a manchete), `notas`
  `{diga, faca: [...], transicao}`, e quando couber `pratica` (minutos), `linhaDia: false`, `segura`, `andamento`. A
  primeira entrada do bloco leva `bloco: '<id do bloco em base.topo.js>'` (pedir, escolhas, skills, pasta, mao, fecho).
- `X.cenas.js`: o código das cenas, que usa `m` e preenche `CENAS.<id> = (t, c) => {...}`. Já estão no escopo (vêm da
  base): `palco, revelar, surgir, tracar, contar, digitar, voar, anotar, caixa, kenburns, escalonar, molaAR, faixa,
  saida, entradaSaida, clamp, lerp, mundo, conteudo, titulo, fim, m, CENAS, $$, vis, NS, traco, cartoes(id),
  partes(id)`. Não faça `import` nem declare `const m`. Dê nomes de variável com o prefixo do bloco para não colidir
  com outro bloco (o script é um só).

Arquétipo sem cena própria (comparacao, tempo, respiro, fios, viagem, objetos, abertura, fecho) não precisa de linha em
`CENAS`; a biblioteca cuida. Cena própria exige `CENAS.<id>`; use `titulo(sec, x, c)` e `fim(sec, x, t0)` como a Aula 1.

## Como ensaiar o seu bloco

```bash
python3 decks/curso-ia-aula2/montar.py X          # gera decks/_p-X/deck.html (só o seu bloco)
./ap sondar decks/_p-X                             # oráculo; precisa sair sem ERRO
./ap paradas decks/_p-X [--viagens]                # um PNG por parada em decks/_p-X/storyboard/ e a folha de contato
./ap lint decks/_p-X
```

Abra a folha de contato (`storyboard/folha.png`) e cada PNG com a ferramenta Read e olhe de verdade: texto cortado,
sobreposição, elemento escondido, slide vazio, hierarquia. Corrija até ficar bom. Avisos do oráculo: resolva, ou
justifique no relatório final se for efeito de o bloco estar isolado (por exemplo "três claros seguidos" ou "primeiro
slide sem abertura"). Rode `./ap sondar` e `./ap paradas` uma de cada vez (o Chrome é pesado).

O ensaio isolado não tem o resto do deck: a linha do dia mostra todos os blocos, e o primeiro slide do seu bloco chega
por corte. Isso é esperado.

## O que fazer bem

- O deck é um guia de uso diário do professor. Cada slide tem de dizer, na tela, o que a sala precisa ver, e nas notas
  o que ele fala, faz e como passa ao próximo. Notas `diga` em voz de aula, frases curtas, fatos só dos que estão em
  `briefing.md`. `faca` lista ações reais (abrir, colar, cronômetro, pedir mão levantada).
- Uma coisa se mexe por vez, de 0,5 a 1,5 s por passo; cada slide termina parado. Animação é função do tempo (`c`,
  `t`); nada de `setTimeout`, `Date.now`, `Math.random` sem semente, nem CSS transition.
- Até 45 palavras visíveis por parada, de preferência menos de 20. Slide que é só texto precisa de forma: tamanho,
  posição, desenho por código que mostre a ideia (barras, setas, caixas, telas de app desenhadas por código).
- Os papéis do caso (`midia/caso-*.webp`) e as figuras de tela de aplicativo são desenhados por código; nunca use o
  print do professor (tem número de processo real) nem dado pessoal.
- Texto de tela sob as normas de escrita do professor: sem travessão, sem "não é X, mas Y", sem dois-pontos como
  anúncio, sem jargão de IA sem explicar, frases curtas, voz ativa. Exemplos jurídicos entram com as palavras do
  professor (briefing), encurtados só se não couberem. Nada de `[CONFERIR]` na tela.
- Não invente fato, número, lei, data ou preço. Só o que está em `briefing.md`.
- Slides vizinhos não repetem o mesmo arquétipo. Alterne claro e noite como a Aula 1.

## Relatório final (curto)

O que construiu (slides e cenas), comandos rodados com a saída resumida do `sondar` (ERROS e AVISOS que sobraram e por
quê), o que ficou frágil ou fora do contrato do briefing, e qualquer mudança que você gostaria na base. Não ponha
conteúdo extenso no relatório: o código é a entrega.
