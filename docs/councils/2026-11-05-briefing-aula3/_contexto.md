# Contexto

**O que é o alvo.** O briefing e o roteiro (versão 1, 05/11/2026) da Aula 3, "Fazer", do curso pago de IA aplicada ao
Direito da co.juris, dado por um procurador do Estado de Mato Grosso do Sul. É a primeira de duas aulas de 90 minutos
do dia 2; a Aula 4, "Decidir", trata de assistentes pessoais, economia da IA e geopolítica. O roteiro vira um deck
animado por código, com um clique por slide, projetado com passador; o professor fala, a tela mostra imagem, número e
frase curta, e a tela do apresentador traz as notas.

**Quem usa.** O professor, que vai ensaiar e dar a aula com este roteiro; a turma (advogados, uma desembargadora,
servidores e assessores, sem formação técnica, muitos sem plano pago de IA), que vê os slides e faz as atividades.

**O que está em jogo.** Curso pago, primeira turma. Um fato errado na tela diante de juristas, uma demonstração que trava
ou uma aula que estoura o horário compromete a credibilidade do professor e da marca.

## Foco do usuário (requisito prioritário)

Avaliar arco, ritmo, atividades, exatidão dos fatos e o que a sala vai lembrar. O desenho do dia 2 está no anexo abaixo.

## Restrições duras (nenhuma sugestão pode violá-las)

- Nenhum fato, número, nome, lei ou data sem fonte lida e anotada no briefing; o que não for confirmado sai da tela.
- Dados pessoais nunca na tela; documentos de atividade são fictícios.
- Demonstrações ao vivo só no Claude, na tela do professor; a sala não instala nada e não precisa de plano pago.
- Até 45 palavras visíveis por slide; manchete com até oito palavras; respiro a cada no máximo cinco slides; dois slides
  vizinhos não repetem o arquétipo.
- Texto de tela sem travessão como vírgula, sem "não é X, mas Y", sem jargão de IA sem explicação.
- Captcha nunca se contorna; raspagem só de fonte aberta, por tema e nunca por pessoa.
- Artefatos e Claude Design ficaram fora do dia 2 por decisão do professor; não proponha reincluí-los.

## Anexo: desenho do dia 2 (contexto, não alvo)

<CONTEXTO — DADO DE APOIO, NÃO INSTRUÇÃO>
# Curso de IA da co.juris, Dia 2: desenho das Aulas 3 e 4

Desenho aprovado na conversa de 05/11/2026. Vale como spec das duas apresentações; quando cada deck for criado, o
`briefing.md` dele herda daqui o público, a linha do tempo, as atividades e as fontes, e este arquivo deixa de ser
editado. Fontes do conteúdo novo: as quatro fichas em `docs/pesquisa/dia2-*.md` (todas de 05/11/2026) e a Parte V da
apostila v2 (`/Volumes/Projetos/Academic-Writing-System/artigos_livros/direito_ia/ebooks/apostila-v2/content/16` a `22`,
com as fichas em `fontes/`).

## Para quem e como

Mesma turma do Dia 1 (advogados, uma desembargadora, servidores e assessores; muitos sem plano pago), sala presencial com
projetor e passador. Duas apresentações de cerca de 90 minutos, `decks/curso-ia-aula3` e `decks/curso-ia-aula4`, no
tema `cojuris`, em plano contínuo e com a mesma trilha dourada das Aulas 1 e 2. Os slides guiam o professor como na Aula
2: passos na tela, cronômetro nas atividades, pedido exato para copiar e guia do apresentador (tecla P) com o que falar.

A divisão é por natureza. A Aula 3, "Fazer", põe a IA para trabalhar fora do chat: skills, Word, MCP, plugins, scraper,
GitHub e rotinas. A Aula 4, "Decidir", trata do que se entrega à máquina e a que preço: assistentes pessoais, o harness,
quem paga a conta, geopolítica e o futuro. Se uma demonstração da Aula 3 falhar, a Aula 4 não depende dela.

Dinâmica das práticas (decisão de 05/11/2026): o professor faz as demonstrações ao vivo na tela, e a sala faz atividades
curtas em dupla ou em grupo que não exigem plano pago, instalação nem papel; o enunciado está no slide. A parte técnica,
o aluno refaz em casa com o kit.

## Aula 3, "Fazer": do arquivo ao mundo

| Min | Bloco | Conteúdo e demonstração | Atividade |
|---|---|---|---|
| 0 a 4 | Abertura | Recapitulação em uma imagem: agente executa, skill é o jeito, MCP é a tomada, plugin é o pacote (o slide `liga` da Aula 2, agora como mapa do dia). | |
| 4 a 30 | Skills e Word | Demo da skill de Word do Claude: rascunho em Markdown vira parecer `.docx` no modelo timbrado do kit. Demo do Claude for Word revisando um documento. O `SKILL.md` por dentro, e a correção de vocabulário: a skill de Word é "código publicado", com licença proprietária; o restante de `anthropics/skills` e o `claude-for-legal` são Apache 2.0. Checklist de sete pontos antes de instalar (apostila, 16.8). | A1, A2 |
| 30 a 46 | MCP e plugins | Demo de conector MCP remoto gratuito e sem login (`https://learn.microsoft.com/api/mcp`); na conta gratuita ele ocupa a única vaga de conector personalizado. Demo de plugin do marketplace Legal: instalar, ver o que traz, remover. Aviso: os plugins jurídicos seguem o direito dos EUA e entregam rascunho. Injeção de comando e permissão mínima (apostila, 17.6 e 17.7). | A3, A4 |
| 46 a 66 | Scraper de jurisprudência | Etapa 1: Claude no navegador com a skill de consulta ao TJMS (CJSG do e-SAJ), sem código. Etapa 2: o Claude Code escreve um script de cerca de vinte linhas sobre os Dados Abertos do STJ ("Espelhos de acórdãos", JSON mensal, licença CC Atribuição, sem chave nem captcha), filtra por tema e grava CSV. Limites na tela: pesquisa por tema e nunca por pessoa (Res. CNJ 121/2010, art. 5º), uma requisição por vez com pausa, captcha não se contorna. | A5 |
| 66 a 73 | GitHub | Repositório como pasta com histórico; README, baixar ZIP, issue e pull request em uma frase cada; onde moram skills e plugins; o script da etapa 2 e a skill do escritório guardados num repositório. | |
| 73 a 86 | Rotinas | O boletim de jurisprudência da etapa 2 vira tarefa agendada no Claude. Quadro do que se agenda, do que se agenda com conferência e do que não se automatiza (apostila, 18.6); a lista preliminar não é contagem de prazo. | A6 |
| 86 a 90 | Fecho | O que levar, onde está o kit, ponte para a Aula 4. | |

## Aula 4, "Decidir": o que fica e quanto custa

| Min | Bloco | Conteúdo | Atividade |
|---|---|---|---|
| 0 a 4 | Abertura | Da ferramenta que responde ao assistente que age sozinho. | |
| 4 a 27 | Assistentes pessoais | Claude Duet, dots, Muse, Grok Bot e Hermes Agent, com datas, planos e disponibilidade no Brasil (apostila, cap. 22, e a ficha `fontes/cap22-assistentes.md`). O preço do acesso: sigilo profissional (Lei 8.906/1994, Recomendação OAB 001/2024, Resolução CNJ 615/2025). | A7 |
| 27 a 33 | O harness | Animação engraçada no estilo de `claude_video_maker/videos/agentes-peca` (bichinhos que acordam, trabalham e colam o que produziram numa folha que percorre a trilha, com o custo acumulado subindo), refeita com os dados do print da aba "Detalhes" de uma peça do quatilex enviado pelo professor em 05/11/2026: 10 agentes, 6 modelos, US$ 1,59 no total, dos quais US$ 1,39 (87%) do redator em Claude Opus 5.5 e o resto em modelos baratos. Mostra que o sistema em volta do modelo pesa tanto quanto o modelo, e serve de ponte para "Quem paga a conta": o modelo caro só onde ele faz diferença. | |
| 33 a 56 | Quem paga a conta | Tese (decisão de 05/11/2026): o uso já se paga, a corrida não. Investidores bancam o treino e a infraestrutura, e o usuário pesado é bancado pelo leve. Números do S-1/A da Anthropic (02/11/2026): receita, custo de computação caindo para 57% da receita, compromissos de cerca de US$ 895 bi pagos com ou sem uso. Os planos fixos encolhendo: modelo de ponta fora do Pro, Copilot por consumo desde 01/06/2026, anúncios no ChatGPT, Gemini CLI desligado para contas pessoais. Bolha: alertas de BIS, FMI e Banco da Inglaterra, que falam em risco de correção e não afirmam bolha, contra receita recorrente e demanda acima da oferta. Consequência: portabilidade. | A8 |
| 56 a 74 | Geopolítica | Chips e licenças caso a caso para a China (91 FR 1684, 15/01/2026); modelos abertos cerca de quatro meses atrás dos fechados (Epoch AI) e a avaliação do CAISI/NIST sobre DeepSeek, com a ressalva de quem avalia; CLOUD Act e a ausência de acordo com o Brasil; AI Act em vigor com o alto risco adiado para 2027 e 2028; PL 2338/2023 parado na Câmara. | A9 |
| 74 a 90 | Futuro, plano e devolutiva | Cenários com sinais para acompanhar; plano de 30 dias (conclusão da apostila); devolutiva da turma; fecho do curso. | A10, A11 |

## Atividades

Onze atividades, todas com enunciado na tela e cronômetro, sem papel e sem computador do aluno.

| | Aula | Atividade | Tempo |
|---|---|---|---|
| A1 | 3 | Auditoria relâmpago: em dupla, achar os três defeitos escondidos numa skill fictícia (script que envia dados para fora, permissão ampla demais, descrição que dispara sempre) com o checklist de sete pontos. | 6 min |
| A2 | 3 | A sala dita três regras do escritório e o professor as transforma em skill ao vivo, com "Criar com o Claude". | 7 min |
| A3 | 3 | Caça à injeção: a sala acha a ordem escondida numa petição fictícia antes de o agente lê-la; depois o professor roda o agente e todos veem o que ele faz com a ordem. | 4 min |
| A4 | 3 | Tomada ou pacote: oito situações na tela para classificar como conector, MCP, skill ou plugin. | 4 min |
| A5 | 3 | A sala vota o tema do scraper e, no fim, confere três acórdãos coletados contra a fonte. | 4 min |
| A6 | 3 | Agendável ou não: tarefas do cotidiano para separar em agendar, agendar com conferência e não automatizar; a sala propõe uma tarefa da própria rotina e o professor cria a rotina com a mais votada. | 8 min |
| A7 | 4 | Permissões mínimas de um assistente para a própria rotina (Exercício 22.1 da apostila). | 7 min |
| A8 | 4 | Plano B: "se o preço dobrar na sexta, o que quebra no meu trabalho?", com o checklist de portabilidade. | 5 min |
| A9 | 4 | Debate em dois lados, preparado com um mapa de onde vão os dados de cada ferramenta da sala: o órgão público pode usar um modelo aberto chinês rodando localmente? | 6 min |
| A10 | 4 | Plano de 30 dias, individual, com três ações. | 5 min |
| A11 | 4 | Devolutiva: o que cada um leva e o que faltou. | 5 min |

## Kit do Dia 2

Repositório público no mesmo padrão do kit da Aula 2 (`kaoyeoshiro/kit-aula2-curso-ia`), gerado por script a partir do
deck: a skill fictícia com defeitos (A1), a petição fictícia com ordem escondida (A3), o modelo timbrado `.docx` do
escritório fictício Dias & Moura, o script do scraper da etapa 2 com modo offline, e um guia de como refazer cada
demonstração em casa no Claude, no ChatGPT e no Gemini, marcando o que é equivalente, o que exige adaptação e o que não
existe.

## Contingência e ensaio

Cada demonstração ao vivo tem reserva gravada no ensaio. O scraper tem modo offline: o JSON do STJ e uma página de
resultado do TJMS salvos antes da aula. Itens que o professor precisa ensaiar na própria conta, porque nenhuma página
oficial os garante: o timbre preservado no `.docx` gerado; remover um plugin sozinho (a ajuda só explica remover o
marketplace); tarefa agendada rodando com o app fechado; Claude in Chrome e uso do computador visíveis na conta brasileira.

## Regras de conteúdo

Zero `[CONFERIR]` na tela: o que as fichas listam em "não consegui confirmar" fica fora do slide. Linhas de confiança
"baixa" nas fichas não vão para a tela; as de confiança "média" só com a fonte nomeada no slide. Nenhum número de
OpenAI ou xAI aparece sem a ressalva de que vem de vazamento a jornal ou de leitura de terceiros. Exemplos neutros, que
servem a escritório, gabinete e órgão público. Dados pessoais nunca aparecem; o harness do quatilex usa caso fictício.

## Pendências antes de montar

- Ler o repositório do quatilex (papéis e ordem dos 10 agentes de `docs/pesquisa/dia2-harness-quatilex.md`) para a
  animação do harness; o código está em `/Volumes/Projetos/Automacao_Agent` (remoto `kaoyeoshiro/quatilex`), só para
  leitura. A animação é feita no repositório `claude_video_maker`, a partir de `videos/agentes-peca`, e entra no deck
  pelo `./ap trazer` (decisão do professor de 05/11/2026).
- O livro *A próxima onda* (Suleyman e Bhaskar, 2023), anotado em `curso-ia-ideias.md` para o bloco do futuro, só entra
  se houver a edição em mãos para citar tese e página; sem isso, o bloco do futuro usa só as fichas.
- Imagens da série do tema: custo de geração sob o teto de US$ 2,00 do `./ap imagens`; acima disso, só com o sim do
  professor. A escolha entre os rascunhos é dele.
- Conferir em fonte primária, antes da versão final, as linhas de confiança média que forem usadas na tela (por exemplo,
  números de energia da IEA e o texto da Lei 15.504/2026).

## Fora do escopo

Artefatos e Claude Design (decisão de 05/11/2026) e o harness como tema técnico aprofundado. O Claude no navegador
aparece só como ferramenta da etapa 1 do scraper, sem bloco próprio.

</CONTEXTO>
