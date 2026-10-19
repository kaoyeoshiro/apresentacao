# Regras de conteúdo: PGE-MS

A skill lê este arquivo antes de escrever qualquer texto de apresentação nesta marca. Fonte: `CLAUDE.md`, `tokens.css` e `GUIA-TIPOGRAFIA.md` do design system das peças jurídicas da PGE-MS (repositório de visual law, pasta `pge-ms`). O que aquelas fontes não declaram aparece marcado com `[CONFERIR com o usuário]`; nada foi presumido em silêncio. O design system nasceu para peça processual em papel, e a apresentação em tela é um meio novo para ele. Onde a regra de papel não se traduz sozinha, isso é dito.

## Identidade

- Nunca misturar com a co.juris. O `CLAUDE.md` da PGE-MS é explícito: nenhum elemento da co.juris entra em material com a identidade da PGE, e o logo da PGE não entra em material da co.juris (o exemplo dado é post de Instagram). Esta pasta serve só a apresentações da PGE-MS.
- Cores (tabela oficial da PGE-MS, coluna central): `--cor-tinta` é o marinho institucional, usado em títulos, tarjas, cabeçalhos e nos atos escuros; `--cor-destaque` é o laranja; `--cor-fundo` é o azul quase branco que o design system usa como fundo de quadro; `--cor-papel` é o branco das folhas e cartões. `--cor-destaque-escuro` é o laranja escuro da mesma tabela, extra deste tema.
- Mapeamento escolhido para o contrato: o design system tem texto de leitura em preto puro, regra tirada de tipografia para papel ("documentos impressos para leitura devem sempre ser compostos em tipo preto"). Em tela e em ato escuro, `--cor-tinta` fica no marinho, que é a cor de moldura institucional. `--cor-fundo` vem do papel de cor de fundo de quadro do design system, e não de um off-white próprio, porque a tabela oficial não traz um. `[CONFERIR com o usuário]` se o fundo padrão dos atos deve ser esse azul quase branco ou branco puro.
- O laranja é destaque, e só isso. O design system proíbe usá-lo como cor de estrutura: entra quando um número, uma barra ou uma linha precisa saltar da página, e perde a função se aparecer em mais de dois ou três lugares por peça. Numa apresentação, o mesmo limite vale por ato. O verde-água da tabela oficial (eixo de precedentes) e o azul médio (numeração e filetes) não foram levados ao tema por não fazerem parte do contrato; se um ato precisar, buscar no `tokens.css` do design system.
- Tipografia: Montserrat variável nos títulos (é a família do documento institucional da PGE-MS) e Source Serif 4 no texto e nas citações (é a família do corpo das peças). Ambas são OFL e viajam em `fonts/` com as licenças (`OFL.txt` para a Montserrat, `OFL-source.txt` para a Source Serif 4). O design system as escolheu para não depender de fonte instalada no computador. Se a fonte original dos documentos oficiais da PGE-MS (a do cabeçalho do `.docx` institucional) for outra, o design system não a declara com clareza: `[CONFERIR com o usuário]`.
- Caixa alta só em rótulo curto (menos de uma linha), com entreletra positiva. O design system proíbe caixa alta em frase, em título de mais de uma linha e em parágrafo. O contrato dos temas fala em títulos em caixa alta e negrito; para esta marca, a apresentação deve pôr caixa alta apenas em título de uma linha e escrever os demais em caixa normal. O design system também nota que sans com entreletra larga puxa a página para cara de slide, então a entreletra dos títulos fica moderada. `[CONFERIR com o usuário]` se ele prefere manter caixa alta em todo título de ato.
- Nunca sublinhar. Ênfase é negrito, e o itálico fica para estrangeirismo, título de obra e nome de julgado. Negrito no corpo tem a cor do texto ao redor.
- Sem marca d'água, sem fundo cinza médio, sem moldura grossa. Antes de traçar filete, tentar mais branco.
- Uso do nome: PGE-MS para a sigla; o logo escreve "Procuradoria-Geral do Estado" e "Mato Grosso do Sul". Como o nome completo aparece no texto corrido ("Procuradoria-Geral do Estado de Mato Grosso do Sul") não está declarado nas fontes lidas: `[CONFERIR com o usuário]`.

### Logo

- Arquivo: `marca/logo-pge.png`, recortado de `logo-pge.png` do design system (que o `CLAUDE.md` diz ter sido extraído do cabeçalho oficial do `.docx` da PGE). O fundo branco virou transparência e as margens foram cortadas. O desenho não foi alterado: as duas tintas do logo (azul e laranja) foram mantidas com valor exato e só o alfa das bordas suaves foi recalculado. Sobre branco, o recorte reproduz o original com diferença máxima de 4 em 255 por canal. O logo tem 607 por 186 pixels e não deve passar de uns 600 pixels de largura na tela, sob pena de perder nitidez.
- Um efeito do recorte: as áreas brancas dentro do brasão (a onça, o miolo do escudo) ficaram transparentes e mostram o fundo do ato. Sobre `--cor-fundo` e `--cor-papel` isso é imperceptível.
- Pode entrar sobre `--cor-fundo`, `--cor-papel` e `--cor-destaque-fraca`. O azul do logo tem 10,5:1 sobre o fundo claro.
- Não pode entrar sobre `--cor-tinta`: o azul do logo é quase o mesmo marinho e o contraste é 1,3:1, o logo some. Também não entra sobre `--cor-destaque`, porque o filete laranja do próprio logo desaparece, nem sobre foto ou textura. Em ato escuro, omitir o logo ou usar uma faixa clara atrás dele. Versão negativa (branca) do logo não existe nos arquivos lidos e não deve ser improvisada: `[CONFERIR com o usuário]` se a PGE-MS tem uma oficial.
- Nunca redesenhar nem gerar o logo por IA.

## Voz

O `CLAUDE.md` e o guia tratam de composição e de conteúdo de peças, e não definem um tom de voz de apresentação. O que decorre do que está declarado:

- O título diz o argumento em vez de rotular a seção ("O adicional não incide no período vedado", não "Do mérito"). Título é substantivo ou tese, e no máximo três níveis, dois de preferência.
- Numeração arábica, com o segundo nível em `1.1`. Sem numeral romano nem letra para seção.
- Texto em português do Brasil (`lang="pt-BR"`). Aspas curvas, reticência `…` (não três pontos), meia-risca `–` em intervalo (`fls. 12–19`), ordinal `º`/`ª`, e `n.` em vez de `nº`. Espaço não separável depois de `art.`, `n.`, `§`, `inc.`, `fls.`, `R$`, `Lei`, `Tema` e `Súmula`, para a linha não quebrar entre o marcador e o número.
- Um espaço entre palavras, nunca dois. Travessão é um caractere diferente de meia-risca e de hífen; o guia trata os três como coisas distintas.
- Tom institucional: sério, técnico e sem hype. `[CONFERIR com o usuário]`: o registro desejado (formal de peça ou mais didático), a pessoa gramatical e se a apresentação fala em nome da PGE-MS ou como servidor apresentando experiência própria.

## Conteúdo

- A peça processual é assinada e vai a protocolo. Por analogia, apresentação com o timbre da PGE-MS merece o mesmo rigor. O `CLAUDE.md` da PGE-MS é taxativo: não inventar número de processo, tese, ementa, data de julgamento, valor ou estatística; sem fonte confirmada, deixar `[CONFERIR]` no texto. Isso inclui jurisprudência.
- Todo número que aparece em tabela, gráfico ou destaque tem de constar do material de origem. Gráfico não é lugar de estimativa nova.
- Blocos autorais que não existem no texto de origem (resumo, síntese, rótulos de linha do tempo) são redação nova e precisam de leitura do procurador responsável antes de a apresentação sair. Sinalizar isso na entrega.
- Nomes de partes e de signatários: conferir a grafia, com acentuação, contra o documento de origem.
- Dado ilustrativo aparece marcado como tal na tela. O que não foi confirmado leva `[CONFERIR]`.
- Consultoria e opinião jurídica: as fontes lidas não dizem se uma apresentação da PGE-MS pode expressar tese do órgão. `[CONFERIR com o usuário]` quem valida o conteúdo antes de sair (chefia, Procuradoria-Geral) e se há aviso obrigatório de que a fala é pessoal.
- Dados pessoais, sigilo e LGPD: nenhuma regra específica nas fontes lidas para apresentação. `[CONFERIR com o usuário]`.

## Pessoas e cargos

As fontes lidas da PGE-MS não trazem lista de pessoas nem de cargos. Não presumir grafia de nome, cargo ou lotação. Antes de qualquer nome aparecer em ato, a grafia exata (com acentuação) e o cargo vêm do usuário: `[CONFERIR com o usuário]`. O tema da co.juris tem nomes e cargos de sócias e sócios, mas ele pertence a outra identidade e não deve ser copiado para cá.

## Contraste medido

Cálculo WCAG 2.x (luminância relativa, sRGB) em script Python; as derivadas de `color-mix` foram calculadas com a mesma fórmula da spec (mistura linear em sRGB) e conferidas no Chromium, que devolveu os mesmos valores. Os nomes abaixo são os tokens de `tema.css`, onde estão os valores.

| Par (texto sobre fundo) | Razão | Mínimo | Resultado |
|---|---|---|---|
| `--cor-tinta` sobre `--cor-fundo` | 13,48:1 | 7:1 | passa |
| `--cor-tinta-suave` sobre `--cor-fundo` | 5,66:1 | 4,5:1 | passa |
| `--cor-sobre-tinta` sobre `--cor-tinta` | 13,48:1 | 4,5:1 | passa |
| `--cor-suave-sobre-tinta` sobre `--cor-tinta` | 8,04:1 | 4,5:1 | passa |
| `--cor-destaque` sobre `--cor-tinta` | 5,76:1 | 3:1 | passa |

Pares extras, medidos para orientar o uso:

| Par | Razão | Referência | Resultado |
|---|---|---|---|
| `--cor-tinta` sobre `--cor-papel` | 14,49:1 | 7:1 | passa |
| `--cor-tinta` sobre `--cor-destaque-fraca` | 11,98:1 | 7:1 | passa |
| `--cor-tinta-suave` sobre `--cor-papel` | 6,09:1 | 4,5:1 | passa |
| `--cor-tinta` sobre `--cor-destaque` | 5,76:1 | 4,5:1 | passa |
| `--cor-destaque` sobre `--cor-fundo` | 2,34:1 | 3:1 | falha |
| `--cor-destaque` sobre `--cor-papel` | 2,52:1 | 3:1 | falha |
| `--cor-destaque-escuro` sobre `--cor-fundo` | 3,58:1 | 3:1 | passa (só texto grande) |
| `--cor-destaque-escuro` sobre `--cor-papel` | 3,85:1 | 3:1 | passa (só texto grande) |
| azul do logo sobre `--cor-fundo` | 10,54:1 | 3:1 | passa |
| azul do logo sobre `--cor-tinta` | 1,28:1 | 3:1 | falha |
| azul do logo sobre `--cor-destaque` | 4,50:1 | 3:1 | passa (mas o filete do logo some) |

Todos os pares do contrato passam. Exceções e restrições de uso registradas:

- `--cor-destaque` sobre fundo claro (`--cor-fundo` ou `--cor-papel`) fica abaixo de 3:1. O laranja cheio serve como preenchimento (filete, barra, marcador, etiqueta), nunca como cor de texto sobre claro. Número ou texto grande em destaque sobre claro usa `--cor-destaque-escuro`, que passa de 3:1 mas não de 4,5:1, e por isso só vale para corpo grande (a partir de 24 px, ou 19 px em negrito). Texto pequeno em laranja não existe nesta marca.
- `--cor-destaque` sobre `--cor-tinta` passa (5,76:1), então o laranja em número grande ou filete sobre ato escuro está liberado. Texto pequeno em destaque sobre tinta continua fora, como manda o contrato.
- O logo não entra sobre `--cor-tinta` (ver a seção do logo).
