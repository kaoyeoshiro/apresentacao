# Temas: o contrato de um design system

Um tema é uma pasta `temas/<nome>/`, e trocar de cliente é trocar de pasta. O deck liga o tema por
`<link rel="stylesheet" href="../../temas/<nome>/tema.css">` e só usa os tokens abaixo, de modo que nenhum deck tem
hex de marca, nome de fonte ou caminho de logo. O contrato veio do repositório antigo `apresentacoes` e vale sem
mudança para os temas trazidos de lá (co.juris, PGE e o `_modelo`); o tema `noite`, escuro e sem marca, é o da
demonstração. O teste `test_demo_com_tema_de_marca_passa_no_oraculo` roda a demonstração com co.juris e PGE e
reprova o tema ou o deck que quebrar legibilidade.

## Arquivos

```
temas/<nome>/
  tema.css     tokens e @font-face; o único CSS que sabe de cor, fonte e logo
  marca/       logos oficiais, sempre recortados do arquivo original, fundo transparente
  fonts/       fontes com licença que permite redistribuir (OFL), woff2 ou ttf variável, com a licença ao lado
  regras.md    identidade, voz, o que precisa de fonte, pessoas e cargos, contraste medido
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

## Criar um tema novo

1. Pedir ao usuário o logo em arquivo original, as cores da marca (ou extraí-las do logo), as fontes oficiais e o
   que a marca nunca diz.
2. Copiar `temas/_modelo/` para `temas/<nome>/`, recortar o logo e conferir sobre fundo claro e escuro.
3. Escrever `tema.css`, derivar as cores e medir os contrastes; escrever `regras.md`.
4. Rodar a demonstração com o tema (`./ap novo _teste --tema <nome>`, `./ap sondar decks/_teste`, `./ap paradas
   decks/_teste`), olhar os stills e apagar a pasta de teste.
