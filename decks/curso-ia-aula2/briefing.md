# Briefing: curso de IA da co.juris, dia 1, Aula 2. Do chat à pasta (versão 2, 23/10/2026)

Segunda de duas aulas de cerca de 90 minutos, na mesma tarde da Aula 1 (`decks/curso-ia-aula1`). Esta versão refaz a
primeira montagem (feita no Grok, 19 slides de rótulos soltos). O deck é um guia de uso diário do professor: cada
slide diz o que a sala vê, e o guia do apresentador (tecla P) diz o que falar, o que fazer e como passar ao próximo.
O deck é montado por `montar.py` a partir de `fonte/`; edite `fonte/`, nunca o `deck.html`.

## Para quem, onde e o que fica

- Curso pago, o primeiro do professor. Turma mista: advogados, uma desembargadora, servidores e assessores. Muitos sem
  plano pago. Exemplos neutros, que servem a escritório, gabinete e órgão público.
- Sala presencial, projetor e passador. Tema `cojuris`, plano contínuo, a mesma trilha dourada da Aula 1.
- Mensagem em uma frase: um pedido bom é um briefing; o processo se trabalha numa pasta, num Projeto que guarda o
  jeito de fazer; o agente propõe e a pessoa confere a fonte.
- No fim, cada um registra três coisas: a resposta, o arquivo e o trecho, e o que ainda precisa de conferência humana.
- Curso agnóstico: Claude e ChatGPT lado a lado. O Claude vai ao vivo na demonstração; o Codex entra gravado.
- Zero `[CONFERIR]` na tela. O que não foi lido em fonte nesta sessão sai do slide.
- Sem slide nem fala de sigilo (decisão do professor em 23/10/2026). Uma exceção, só nas notas do slide `pasta`: se
  alguém perguntar, pasta no computador não é offline; o que o agente lê vai ao provedor do modelo, como um anexo.
- Antes da aula, o professor manda pelo WhatsApp o pedido de instalar os apps do Claude e do ChatGPT e o link do material
  fictício: um `.zip` com contrato, aditivo e notificação, e um PDF único com os três (`material/`). Na sala não há papel.

## Decisões do professor nesta revisão

1. Os slides têm de guiar o professor na aula (passos na tela, cronômetro nas práticas, pedido exato para copiar).
2. Um slide muito claro sobre as diferenças entre Claude, ChatGPT Work, Claude Code e Codex, avisando que o Cowork
   não existe mais (virou o próprio Claude).
3. Projeto e pasta não são degraus: são duas escolhas independentes (onde moram as instruções e a memória; onde moram
   os documentos). Regra prática: processo, sempre com pasta. Code e Codex são para controle fino e volume.
4. Pedir bem usa a apresentação de engenharia de prompt do próprio professor (`engenharia-de-prompt-apresentacao.html`,
   17/03/2026): seis elementos, um por slide, com os exemplos dela, e a persona com peso próprio. A regra "se não souber,
   diga" é o fio da aula e volta na demonstração.
5. Lei: guardar (base fixa, com fonte e data) ou pesquisar (o que muda). Markdown em vez de PDF para contexto persistente.
6. Skills (Claude e ChatGPT/Codex usam o mesmo formato), plugin e MCP em um slide só; a prática fica para o dia 2.
7. Os exemplos jurídicos do professor (convênio de pavimentação, ofício do TCE, edital, ICMS) ficam como estão; leis e
   artigos citados na tela passam por conferência em fonte oficial antes de a versão final sair (ver Pendências).
8. Nenhuma versão de modelo (Claude 4.6, ChatGPT 5.4 etc.) aparece nos slides de pedir bem.

## Linha do dia (90 min; vale a da Revisão 2 abaixo: 23, 18, 8, 11, 27, 3)

| min | bloco (`bloco`) | slides |
|---|---|---|
| 25 | Pedir bem (`pedir`) | capa a relato |
| 22 | Duas escolhas (`escolhas`) | ponte a escolher |
| 8 | Skills (`skills`) | skills a liga (6 de aula e 2 de perguntas) |
| 16 | Na pasta (`pasta`) | papeis a limite |
| 15 | Mão na massa (`mao`) | codex a quem |
| 4 | Fecho (`fecho`) | registro e fecho |

## O caso fictício (fonte única para todos os blocos)

Pasta `caso-ficticio/` com três PDFs gerados por `material/gerar.py`. Tudo inventado; os nomes não existem.

- `contrato.pdf`: Contrato de prestação de serviços nº 07/2019, manutenção predial, entre o Município de Vila Serena
  (contratante) e Horizonte Manutenção Predial Ltda. (contratada). Cláusula terceira: "As partes firmam este contrato
  em 12/03/2019, com vigência de 36 (trinta e seis) meses, contados da assinatura." Cláusula segunda: R$ 48.000,00
  por mês. Cláusula quinta: relatório mensal até o dia 5. Cláusula nona: multa de 2% sobre o valor mensal por
  competência em atraso.
- `aditivo.pdf`: Primeiro termo aditivo, 01/04/2021. Cláusula primeira: prorroga por 12 meses, a contar do
  término da vigência original (12/03/2022), e a vigência passa a ir até 12/03/2023.
- `notificacao.pdf`: Notificação nº 031/2023, 20/02/2023. O relatório de janeiro de 2023 foi entregue em 14/02/2023,
  prazo 05/02/2023. Multa de 2% (cláusula nona) sobre R$ 48.000,00, total de R$ 960,00. Cinco dias úteis para defesa.
- A data do último pagamento NÃO consta de nenhum papel. É de propósito: mostra a regra "se não achar, diga que não
  achou".

Imagens prontas em `midia/`: `caso-contrato.webp`, `caso-aditivo.webp`, `caso-notificacao.webp` (primeira página de
cada papel, legível) e `caso-contrato-trecho.webp` (a página do contrato com a cláusula terceira marcada em amarelo;
o amarelo é cor do papel, não do tema, e só aparece nesta imagem).

Pedido da demonstração e da prática (texto exato, o mesmo nos dois):

> Monte a cronologia do caso com a data de cada fato. Para cada data, cite o arquivo e o trecho. Inclua a data do
> último pagamento. O que não estiver nos documentos, diga que não encontrou. Salve em cronologia.md.

Cronologia que o agente devolve (usada em `fonte`, `trecho` e nas notas):

| data | fato | fonte |
|---|---|---|
| 12/03/2019 | contrato assinado, vigência de 36 meses | contrato.pdf, cláusula terceira |
| 01/04/2021 | aditivo prorroga por 12 meses, até 12/03/2023 | aditivo.pdf, cláusula primeira |
| 14/02/2023 | relatório de janeiro entregue, com 9 dias de atraso | notificacao.pdf, segundo parágrafo |
| 20/02/2023 | multa de 2% notificada, R$ 960,00 | notificacao.pdf, terceiro parágrafo |
| (último pagamento) | não encontrei nos documentos | sem fonte |

`skill` da demonstração (arquivo `.claude/skills/cronologia-com-fonte/SKILL.md` no Claude, `.agents/skills/...` no
Codex), texto exato:

```
---
name: cronologia-com-fonte
description: Monta a cronologia de um caso com a data de cada fato e a fonte de cada data. Use quando o pedido for cronologia, datas ou prazos dos documentos da pasta.
---
Leia todos os documentos da pasta do caso.
Liste cada data com o fato correspondente, em ordem.
Para cada data, cite o arquivo e o trecho exato.
Se a informação não estiver nos documentos, escreva "não encontrei nos documentos". Não deduza.
Salve o resultado em cronologia.md.
```

`memoria.md` da pasta (contexto persistente, em Markdown), texto exato:

```
# Memória do caso
- Contrato nº 07/2019, manutenção predial: Município de Vila Serena e Horizonte Manutenção Predial Ltda.
- Os três documentos são fictícios, para a aula.
- Trate prazo e multa como pontos de conferência humana.
- Responda em português, em frases curtas.
```

## Fatos sobre as ferramentas (lidos em 23/10/2026; cite só o que está aqui)

Fontes: [Claude Cowork and chat are one Claude](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude),
[anúncio de 16/09/2026](https://claude.com/blog/cowork-is-now-claude), [preços do Claude](https://claude.com/pricing),
[visão geral do Claude Code](https://code.claude.com/docs/en/overview), [skills do Claude Code](https://code.claude.com/docs/en/skills),
[ChatGPT Work and Codex](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex),
[Codex no seu plano do ChatGPT](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan),
[Build skills (ChatGPT e Codex)](https://learn.chatgpt.com/docs/build-skills),
[envio de arquivos ao ChatGPT](https://help.openai.com/en/articles/8555545-uploading-files-and-audio-to-chatgpt),
[PDF no Claude](https://platform.claude.com/docs/en/build-with-claude/pdf-support).

- Cowork e chat viraram um só Claude, anunciado em 16/09/2026; chegou primeiro a Pro e Max, Team e Free depois. "Tudo o
  que o Cowork fazia está disponível em qualquer conversa." No app Claude Desktop o Claude lê, organiza e cria arquivos
  numa pasta liberada, mas só com o app aberto. Pedidos longos continuam na nuvem. Tem Projetos, memória, skills e plugins.
- Claude Code: lê a pasta, edita arquivos, roda comandos; no terminal, em editores, no app desktop (aba Code) e na web.
  Exige plano pago. Pro: US$ 20 por mês (US$ 17 no plano anual); Code incluído em Pro, Max e Team; o plano
  gratuito não tem Code.
- ChatGPT tem Chat, Work e Codex. Work: agente para trabalho de várias etapas e entregas (pesquisa, documento, planilha,
  apresentação). Na web e no celular roda na nuvem; no app desktop pode usar arquivos locais, com permissão. Work: planos
  pagos elegíveis. Codex: desenvolvimento de software e trabalho técnico; trabalha com pastas locais, repositórios e
  terminal no app desktop, e há Codex na nuvem. Codex está nos planos do ChatGPT, até no gratuito e no Go, só no app
  desktop e com limites; Plus e acima têm também web, linha de comando e editores.
- Skill é uma pasta com um arquivo `SKILL.md` (nome, descrição e instruções); segue um padrão aberto, então o mesmo
  arquivo serve ao Claude e ao ChatGPT/Codex. Claude: `.claude/skills/<nome>/SKILL.md`, chamada por `/nome`. Codex:
  `.agents/skills/<nome>/SKILL.md`, chamada por `$nome` (e `@` no ChatGPT). No app desktop do ChatGPT, o menu Skills
  lista as suas. O modelo vê só o nome e a descrição até decidir usar a skill, então ela custa pouco contexto.
- Plugin é um pacote com skills e, se quiser, conexões (servidores MCP). MCP é um padrão aberto para ligar o agente a
  ferramentas e sistemas externos.
- Limites do anexo no app do Claude (central de ajuda, "Upload files to Claude", lida em 23/10/2026): até 20 arquivos por
  conversa; PDF de até 1000 páginas; em PDF de até 100 páginas o Claude lê texto e elementos visuais (imagens, gráficos),
  de 101 a 1000 páginas lê só o texto. Arquivos de projeto: 30 MB cada, sem limite de quantidade, mas o conteúdo total tem
  de caber na janela de contexto do Claude. (O número "100 páginas por pedido" que apareceu antes era da API do Claude,
  não do app: não use.) ChatGPT: projeto com 5 arquivos no plano gratuito, 25 no Go e no Plus, 40 nos demais; o gratuito
  faz 3 envios por dia; arquivos de projeto são tratados diferente de anexos de chat, e imagens dentro do PDF podem não
  entrar.
- Conectores: o app do Claude liga a Drive, Gmail, Microsoft 365 e Slack em Customize > Connectors; o ChatGPT Work usa
  apps conectados e plugins, que podem trazer conexões MCP. Ou seja, conectar sistemas não é exclusivo de Claude Code e
  Codex.
- Skills: o ChatGPT Work cria skills com `@skill-creator` e o Codex com `$skill-creator`; o Codex detecta mudança em
  skills sozinho e, se a atualização não aparecer, basta reiniciar. No Claude, a skill se cria pedindo ao Claude ou
  escrevendo o `SKILL.md`.
- Word: o app do Claude cria documentos, planilhas e apresentações como arquivos editáveis, e o ChatGPT Work cria
  documento, planilha e apresentação; por isso o exercício pede o `.docx` ao próprio agente, sem instalar conversor.
  Conversor de linha de comando (pandoc) não está instalado nesta máquina e o aluno não o terá: fica só como opção
  avançada nas notas.
- No Claude, o Projeto agrega instruções, memória, contexto (arquivos) e pasta numa tela só.

## O teste do processo fictício (feito em 23/10/2026, `/tmp/teste_processo`, reproduzível)

Processo inventado com 7 PDFs de texto digital: 348 páginas, 1,5 MB, 129.226 palavras (cerca de 190 mil tokens, estimativa
de 1,5 token por palavra). Cabeçalho e rodapé repetidos em cada página somam 8.700 palavras (6,7%). Ao converter para
Markdown e remover o ruído, 120.540 palavras. Achar "12/03/2019" na pasta de arquivos Markdown levou 6 milissegundos e
o agente lê só o trecho, cerca de 300 palavras (0,2% do processo). No chat, as 348 páginas entram inteiras na conversa e passam do limite de 5 arquivos por projeto do ChatGPT gratuito (no app do Claude, ver a Revisão 2: o número de 4 pedidos de 100 páginas era da API e foi retirado). Limites do teste: texto
repetitivo e PDFs com texto digital; em PDF escaneado o texto sai vazio sem reconhecimento de caracteres. Marcar na tela
como "teste com processo fictício".

## Mudanças depois da primeira montagem (23/10/2026)

O deck final tem 56 slides (ver a Revisão 2). Em relação à lista abaixo: entraram `agente` ("O chat responde. O agente age.") e `confere`
("O agente propõe; você confere") logo depois de `reenvio`, porque faltava explicar a diferença entre chat e agente;
entrou `skills` (respiro que abre o bloco); `ponte` virou cena própria (papéis caindo sobre a caixa do pedido);
`limite` virou respiro ("A conclusão jurídica fica com você"), com os três pontos nas notas. Skills ganhou 8 minutos
(6 de aula, 2 de perguntas), que também mantém a linha do dia estável no oráculo. A tela de "quem tem" diz Pro e Max
para o Claude novo, Team e Free depois. Citações de lei conferidas no Planalto em 23/10/2026: Lei 14.133/2021, art. 67
(o §1º limita atestados às parcelas de maior relevância, 4% ou mais do valor) e LC 101/2000 existem como citadas; o
caput do art. 67 fala em obra "semelhante" e serviço "similar".

## Revisão 2 (23/10/2026, depois de o professor ver a primeira montagem)

Decisões do professor e correções, a seguir. Quem constrói cada bloco segue esta seção e vence o que estiver abaixo.

1. **Contexto é prompt.** Em Pedir bem, no elemento 2, e no slide que abre o bloco "Duas escolhas", dizer que o contexto
   normalmente vem de documentos anexados, não digitado no pedido, e que tudo o que a IA lê (pedido, anexos,
   instruções, memória, conversa anterior) é prompt. Correção ao professor, a dizer nas notas: digitar quem você é e o
   caso também é contexto e vale; o grosso do material pesado é que costuma vir por anexo, instruções e memória.
2. **`ponte`** (abre Duas escolhas) vira "Tudo o que a IA lê é prompt": uma caixa grande "o que a IA lê" onde entram, um
   por clique de onda, "seu pedido" (pequeno), "anexos", "instruções", "memória" e "conversa anterior". Legenda: "O contexto
   costuma chegar por anexos, instruções e memória." Sem a frase "o contexto não cabe mais no pedido".
3. **`pasta` (cinco motivos), motivo 1 e `teste`:** o número "o Claude aceita 100 páginas por pedido" está errado para o
   app (era limite da API). Use os fatos corrigidos acima. Motivo 1: "No anexo, o processo entra inteiro na conversa e
   ocupa a mesa; na pasta, o agente abre só o que precisa." `teste` mostra, à esquerda, 348 páginas e 129 mil palavras
   e a busca de 12/03/2019 em 6 milissegundos; à direita, duas barras que comparam "Anexado no chat: o processo inteiro
   entra na conversa" com "Na pasta: o agente lê cerca de 300 palavras (0,2%)". Sem os "4 pedidos de 100 páginas".
4. **`lei`:** guarde as leis que você usa sempre e a jurisprudência favorável que você sempre cita, em `.md`, com a fonte
   e a data da conferência. Pesquise o que muda: jurisprudência nova e alterações de lei.
5. **`codigo`, `escolher`, `matriz`, `travou`:** Claude Code e Codex são ferramentas avançadas para quem quer integrações,
   raspagem (scrapers), automação e controle fino, não "o que tem plano gratuito". Conectar sistemas (MCP, conectores)
   também se faz no Claude e no ChatGPT Work; a diferença é que Code e Codex programam e rodam o que for preciso. Sai
   de toda a aula a recomendação "sem plano pago, use o Codex" (continua só o fato, na grade de planos).
   `codigo`: título "Claude Code e Codex são para quem constrói"; quatro cartões: Integrações (ligam o agente a
   sistemas por MCP e APIs), Raspagem (baixam e organizam dados de sites e tribunais, em lote), Automação (rotinas e
   scripts para centenas de arquivos), Controle (plano, permissões e cada mudança à vista). Rodapé: "Claude e ChatGPT
   Work também têm conectores. Code e Codex programam e rodam o que for preciso."
   `escolher`: 1 "Um arquivo só?" chat com anexo; 2 "Quer o documento pronto, em Word ou planilha?" Claude ou ChatGPT Work;
   3 "É processo, ou vai reusar?" Projeto com pasta; 4 "Precisa integrar sistemas, raspar dados ou automatizar?"
   Claude Code ou Codex. `matriz`, linha de baixo: "Para integrar sistemas, raspar dados e automatizar: Claude Code e
   Codex."
6. **Mão na massa fica mais complexa (24 min).** Duas práticas: (a) a cronologia (10 min, como estava); (b) o desafio de
   criar uma **skill que entrega a cronologia em Word no padrão do escritório fictício** (15 min). O escritório é
   **Dias & Moura Advocacia**; o logo é um emblema gerado por IA (GPT Image, pelo `./ap imagem`, em 23/10/2026) com o nome
   composto em texto; as cores do padrão (verde `#064A45` e cobre `#B87548`) foram amostradas do emblema. Arquivos já
   prontos: `midia/logo-escritorio.webp` (logo, com selo de IA), `midia/caso-parecer-exemplo.webp` (como o Word deve
   ficar), e no zip do aluno `padrao-do-escritorio.md`, `logo-escritorio.png` e `cronologia-exemplo.md` (rede de
   segurança para quem não terminou a prática a). Padrão (texto exato, 8 regras): fonte Georgia corpo 11; títulos em
   verde com filete cobre; cabeçalho com o logo e "Documento de trabalho"; título em caixa alta, centralizado, corpo 14,
   negrito; datas dd/mm/aaaa e valores com duas casas; tabela com cabeçalho verde e linhas alternadas; rodapé com o nome e
   a página; termina com "Pontos para conferência humana". Celular: cole o padrão no pedido e peça o Word.
   Pedido do desafio (texto exato): "Crie uma skill chamada parecer-no-padrao. Ela lê o cronologia.md e o
   padrao-do-escritorio.md da pasta e gera o cronologia.docx no padrão do escritório, com o logo no cabeçalho e a seção
   Pontos para conferência humana. Depois rode a skill e salve o Word na pasta."
   Slides do bloco E, nesta ordem: `codex`, `material` (acrescente a linha "No zip: padrão do escritório, logo e
   cronologia pronta"), `pratica2` (renomeie na tela para "Prática 1: a cronologia", 10 min), `escritorio` (o logo e o
   padrão em poucas linhas), `desafio` (a missão em três passos e como criar a skill em cada ferramenta: Claude, peça "crie
   uma skill"; ChatGPT Work, `@skill-creator`; Codex, `$skill-creator`), `alvo` (a imagem `caso-parecer-exemplo.webp`
   grande, com três legendas: logo no cabeçalho, tabela no padrão, seção de conferência), `pratica3` ("Prática 2: a
   skill em Word", 15 min, com o pedido exato e cinco passos curtos), `travou` (revisto: sem cronologia.md, use
   cronologia-exemplo.md do zip; o app não gerou Word, peça o `.docx` explicitamente; a skill não aparece, reinicie o
   app; celular, cole o padrão no pedido), `mostrar` (respiro: "Mostre o seu Word."). O slide `quem` ("Quem trouxe a
   fonte?") sai.
7. **Fecho melhor (3 min).** Slides do bloco F: `levar` (tempo, seis marcos, "O que você leva hoje": pedido com seis
   elementos; diga que não achou; projeto com pasta; skill escrita uma vez; confira a fonte; Word no padrão), `dia2` ("No
   dia 2": MCP e plugins, rotinas, raspagem de jurisprudência do TJMS e do STF, casos práticos, artefatos e
   apresentações, devolutiva), `fecho` (a mensagem "Trabalhe no caso, não no chat", o logo oficial da co.juris e
   "Obrigado"; veja o encerramento da Aula 1). O slide `registro` sai (a ideia de registrar resposta, fonte e o que
   conferir vai para as notas das duas práticas).
8. **Linha do dia:** pedir 23, escolhas 18, skills 8, pasta 11, mão na massa 27, fecho 3 (90 min). As duas práticas somam 25 min dentro dos 27 do bloco. Os arquivos `cronologia-exemplo.md` do zip ficam na pasta `reserva/`, para não aparecer na Prática 1.

## Os slides

Convenções: `noite` marca o clima (as noites ficam nos respiros, nas aberturas e na demonstração). `cena` = cena própria
(não há arquétipo). Densidade: até 45 palavras visíveis por parada, de preferência menos de 20. Texto de tela abaixo de
30 px não vale. Toda parte que o professor faz tem `pratica` (minutos) ou `faca` nas notas.

### Bloco A, pedir bem (25 min), arquivos `fonte/a-pedir.*`

Origem dos exemplos: `engenharia-de-prompt-apresentacao.html` do professor (texto na pasta da Aula 2 do OneDrive, em
`Curso de IA`). Os exemplos jurídicos entram com as palavras dele, encurtados só para caber.

1. `capa` (abertura, noite): "Do chat à pasta" (palavra `.sinal`: pasta), subtítulo "Como pedir bem e trabalhar nos documentos do caso." Imagem `heroi-aula2.webp` com selo de IA. `linhaDia: false`, abre sozinha.
2. `mapa` (tempo, seis marcos): "A tarde em seis etapas": pedir bem (25 min), duas escolhas (22), skills (6), na pasta (16), mão na massa (15), fecho (4). `agora` no primeiro. Legenda: "Cada etapa termina numa tarefa sua."
3. `tentativas` (cena): "Na terceira tentativa chega perto". Três cartões em fila, cada um com o pedido e uma barra de "distância do que você queria" que encolhe: 1) "Resume esse parecer." 2) "Resume em 10 linhas." 3) "Resume só o que muda o prazo." Rodapé: "O problema não é a IA. É o pedido." (frase do professor).
4. `colega` (comparacao com texto): "Prompt é briefing para colega novo". A: "Resume esse acórdão." B: "Objetivo: o que muda o prazo. Contexto: o contrato e o aditivo. Regra: cite o trecho." Pílula "exemplo de pedido". Notas: se o colega responderia "mas o que exatamente você quer?", o pedido precisa de mais contexto. "Por favor" e gorjeta não funcionam; gaste tokens com informação útil.
5. `seis` (tempo, seis marcos): "Seis elementos, nem todos obrigatórios": objetivo, contexto, persona, saída, exemplos, regras. Legenda: "Pergunta simples pede só o objetivo." Cada clique não; um clique só, marcos acendem em onda.
6. `objetivo` (cena `par`): rótulo "Elemento 1" manchete "Objetivo: o que você quer". Errado: "Escreve sobre inteligência artificial." Certo: "Escreva um parágrafo de 100 palavras sobre como a IA é usada no Judiciário brasileiro, com 2 aplicações concretas." Destacar: 100 palavras, 2 aplicações. Clique 1: errado; clique 2: certo com destaques.
7. `contexto` (cena `par`): "Contexto: o que a IA precisa saber". Errado: "Me ajuda a redigir um parecer." Certo (encurtado): "Sou procurador do Estado e preciso de um parecer sobre a legalidade de um convênio entre o Estado de MS e um município, repasse de R$ 2 milhões, à luz da Lei 14.133/2021 e da LC 101/2000." Dica na tela: "O mais importante vai no começo ou no fim." (o professor: modelos aproveitam menos o meio).
8. `persona` (cena `par`): "Persona: quem a IA deve ser". Errado: "Me explica o que é precatório." Certo: "Você é professor de direito financeiro explicando a servidores que não são da área jurídica. Explique o que é precatório, como o pagamento funciona e por que demora. Sem jargão."
9. `personas` (cena): "A mesma pergunta, três papéis". Pergunta fixa em cima: "O que é precatório?" Três colunas: "Professor para leigos" / "Consultor sênior" / "Procurador do Estado", cada uma com 2 ou 3 linhas de resposta no registro dela, mostrando só vocabulário e profundidade. As respostas são exemplo ilustrativo (pílula "respostas ilustrativas, escritas para a aula"). Frase: "A persona muda o registro da resposta inteira."
10. `saida` (cena `par`): "Estrutura de saída: o formato da resposta". Errado: "Me dá argumentos para contestar essa tese." Certo: "Liste 5 argumentos para contestar a prescrição intercorrente. Para cada um: o fundamento legal, a explicação em 2 frases, e um precedente do STJ ou STF, se houver." Lista de formatos possíveis em linha: tabela, lista numerada, passo a passo, prós e contras.
11. `exemplos` (cartoes, 3 cartões): "Exemplos: mostre o que você quer". zero-shot "tarefa simples e clara, só a instrução"; one-shot "tom ou formato específico, 1 exemplo resolvido"; few-shot "tarefa ambígua ou subjetiva, 2 a 5 exemplos". Rodapé: "Exemplos continuam muito poderosos."
12. `regras` (cena `par`): "Regras: o que a IA não deve fazer". Errado: "Analisa essa cláusula contratual." Certo: "Analise a cláusula 7ª. Só legalidade, não conveniência. Aponte o que for ambíguo. Cite os artigos. Sem jurisprudência clara, diga." Destaque grande: "Se não souber, diga que não sabe." Notas: a IA inventa jurisprudência com total confiança; as regras são a linha de defesa. FIO DA AULA: este "diga que não sabe" volta na demonstração.
13. `junta` (cena): "Juntando tudo". O prompt do edital (do professor), seis linhas com o rótulo de cada elemento à esquerda (Persona, Objetivo, Contexto, Saída, Exemplo, Regras), acendendo uma por clique dentro de um clique só (em onda). Texto: persona "procurador do Estado com experiência em licitações"; objetivo "Analise o edital abaixo e aponte irregularidades jurídicas"; contexto "Concorrência para uma escola estadual, R$ 5 milhões, impugnação em 5 dias úteis"; saída "Tabela: cláusula, irregularidade, fundamento legal, risco"; exemplo "atestado de obra idêntica, art. 67, §1º, Lei 14.133/2021, risco alto"; regras "Não invente artigos. Na dúvida, escreva 'verificar manualmente'." Rodapé: "Não é prompt longo. É a informação certa."
14. `tce` (cena `par`, com destaque no contexto): "O contexto muda tudo". Errado: "Escreve uma resposta para o Tribunal de Contas." Certo (essencial): "Responda ao ofício do TCE-MS sobre o convênio de pavimentação. O TCE diz que falta o plano de trabalho. O plano existe e foi juntado em apenso. Tom formal, não defensivo, até 250 palavras." Destaque: "O plano existe e foi juntado em apenso." Notas: sem essa informação a IA não tem como produzir resposta útil.
15. `pratica1` (cena guia, `pratica: 4`): "Sua vez: reescreva um pedido seu". Três passos na tela: 1 Pegue um pedido que você faz hoje. 2 Reescreva com objetivo, contexto e uma regra. 3 Cole no seu app e compare. À direita, o checklist de seis itens. Cronômetro 4 min nas notas e no palco.
16. `relato` (respiro, noite): "O que mudou na resposta?" Para duas pessoas lerem em voz alta, com consentimento. Notas guiam o debrief (qual elemento mais pesou).

### Bloco B, duas escolhas (22 min), arquivos `fonte/b-escolhas.*`

17. `ponte` (respiro, noite): "O contexto não cabe mais no pedido." Notas: do "prompt" para a "engenharia de contexto" (2025 e 2026 no fecho da apresentação dele): o sistema de informação em volta do pedido. Abre o bloco.
18. `reenvio` (cena): "No chat, você sobe tudo de novo". Três conversas lado a lado (conversa 1, 2, 3), em cada uma os mesmos três papéis (miniaturas de `caso-*.webp`) sobem de novo; rótulo "de novo" a cada uma. Rodapé: "Conversa nova, upload novo."
19. `matriz` (cena): "Duas escolhas, não uma escada". Dois eixos: instruções e memória (na conversa solta | no Projeto) e documentos (anexados | numa pasta). As quatro células preenchem em onda: conversa+anexo "Chat"; Projeto+anexo "Projeto"; conversa+pasta "Tarefa com pasta"; Projeto+pasta "Projeto com pasta" (destacada: "processo: sempre aqui"). Abaixo, uma linha: "Mais controle e volume: Claude Code e Codex".
20. `projeto` (cena): "O Projeto guarda o seu jeito". Desenho por código da tela de Projeto do Claude (instruções, memória, contexto, pasta, programado), com conteúdo do caso fictício; nunca o print do professor (tem número de processo real). Anotações: "visível e editável com um clique". Rodapé: "No ChatGPT, Projeto também guarda instruções e arquivos."
21. `pasta` (cena, lista que acende): "Processo? Trabalhe com pasta". Cinco motivos: 1 volume (um processo passa de 300 páginas), 2 lê só o trecho (busca e abre o que precisa), 3 sem reenviar, 4 a entrega fica ao lado da fonte, 5 você libera só a pasta. Notas: a correção do sigilo (ver "Para quem"); funciona no computador, com o app aberto, não no celular.
22. `teste` (cena de números): "O teste: 348 páginas, 0,2% lidas". Contadores: 348 páginas, 129 mil palavras, achar a data em 6 milissegundos, 0,2% do processo lido. Ao lado, duas barras: "Anexado no chat: o processo inteiro" e "Na pasta: 0,2%". Pílula "teste com processo fictício".
23. `lei` (cena): "Lei: guardar ou pesquisar?". Duas colunas. Guarde: as leis que você usa sempre, com a fonte oficial e a data da conferência. Pesquise: jurisprudência, alteração recente, "esta lei mudou?". Faixa embaixo: "Use o arquivo. Para confirmar alteração, consulte o site oficial e diga a data."
24. `mdpdf` (cena): "PDF ou Markdown?". Mesma página, lado a lado: à esquerda, o PDF (a "foto da página", com cabeçalho e rodapé repetidos marcados em tracejado dourado); à direita, o Markdown limpo (`## Cláusula terceira`). Três legendas: "gasta menos", "erra menos", "acha o artigo certo". Dois clicks: o PDF (com o ruído marcado), depois o Markdown.
25. `converter` (cartoes, 3 cartões): "Converter tudo? Não". "Converta o que você vai reusar", "Pergunta única: suba o PDF como está", "Escaneado: precisa de reconhecimento de texto antes". Rodapé: "Guarde o PDF como prova e o Markdown como cópia de trabalho."
26. `codigo` (cartoes, 4 cartões): "Quando ir além: Claude Code e Codex". 1 Plano e mudanças à vista: mostra o que fará e o que mudou, arquivo por arquivo. 2 Volume e repetição: dezenas de arquivos, a mesma tarefa de novo. 3 Conexões: liga a sistemas (MCP, dia 2). 4 Custo: o Codex funciona até no plano gratuito, no app desktop.
27. `ferramentas` (cena): "Quatro nomes, dois pares". Dois pares em colunas: "Pedir uma entrega": Claude (o antigo Cowork) e ChatGPT Work; "Trabalhar na pasta como um desenvolvedor": Claude Code e Codex. Faixa destacada: "Cowork não existe mais: virou o próprio Claude (16/09/2026)."
28. `diferenca` (cena de grade): "O que muda de um para o outro". Grade 4 colunas x 3 linhas (para que serve, onde roda, quem tem), uma linha por clique em onda. Conteúdo (ver Fatos): Claude / Work / Code / Codex. Linha "quem tem": Claude Pro, Max e Team (Free depois); Work planos pagos elegíveis; Code planos pagos (Pro US$ 20 por mês); Codex todos os planos, até o gratuito, no app desktop.
29. `escolher` (cena): "Como escolher em 10 segundos". Quatro perguntas em sequência, cada uma com a resposta ao lado: "Um arquivo só?" chat com anexo. "É processo, ou vai reusar?" Projeto com pasta. "Precisa ver o plano e o que mudou, ou tem volume?" Code ou Codex. "Sem plano pago?" Codex no app desktop.

### Bloco C, skills (6 min), arquivos `fonte/c-skills.*`

30. `skill` (cena): "Skill é o seu jeito de fazer, escrito uma vez". O `SKILL.md` da demonstração (texto exato, acima) num painel de arquivo, com três anotações: nome, descrição ("diz quando usar"), instruções. Rodapé: "O modelo só lê o nome e a descrição até decidir usar."
31. `onde` (cena de grade): "O mesmo arquivo nos dois". Linhas: onde mora e como chamar. Claude: `.claude/skills/nome/SKILL.md`, `/nome`. ChatGPT e Codex: `.agents/skills/nome/SKILL.md`, `@nome` no ChatGPT e `$nome` no Codex. Rodapé: "Padrão aberto de skills: escreva uma vez, use nas duas."
32. `liga` (cena de diagrama): "O que liga o agente ao mundo". Agente no centro, à esquerda skill ("o jeito"), à direita MCP ("a tomada para sistemas"), em cima plugin ("o pacote com os dois"). Legenda: "Prática de plugin e MCP: dia 2."

### Bloco D, na pasta (16 min), arquivos `fonte/d-pasta.*`

33. `papeis` (viagem): "Três papéis na pasta do caso". Os três papéis (`caso-*.webp`, ids `ob-contrato`, `ob-aditivo`, `ob-notificacao`) voam para a árvore `caso-ficticio/`. Foto `pasta-aberta.webp` com selo de IA.
34. `estrutura` (cena, árvore): "O que está na pasta". Árvore: contrato.pdf, aditivo.pdf, notificacao.pdf, memoria.md, skills/cronologia-com-fonte/SKILL.md; e `cronologia.md` aparece vazio, tracejado, "o agente vai criar". Legenda: "Pronto antes da aula. Nada é criado ao vivo, só a cronologia."
35. `memoria` (cena): "A memória do caso, em Markdown". O `memoria.md` (texto exato, acima). Rodapé: "Contexto persistente: texto limpo, que qualquer agente lê."
36. `agora` (respiro, noite): "Agora, funcionando." Notas: abrir o app na pasta do caso.
37. `pedido` (cena guia): "O pedido e os cinco passos". À esquerda, o pedido exato (acima), que se digita. À direita, cinco passos numerados: 1 abrir a pasta, 2 colar o pedido, 3 ler o plano e autorizar, 4 abrir o cronologia.md, 5 conferir um trecho no papel.
38. `demo` (cena, noite): "Ao vivo no Claude, na pasta". Simulação por código de uma sessão: o pedido, "lendo contrato.pdf, aditivo.pdf, notificacao.pdf", o plano, a escrita do `cronologia.md`. Rótulo "simulação por código; a gravação da aula substitui". Notas: se a rede falhar, deixar esta cena rodar.
39. `fonte` (fios, noite): "Cada data aponta para o papel". Fontes: contrato.pdf, aditivo.pdf, notificacao.pdf. Minuta `cronologia.md` com quatro linhas: "12/03/2019: contrato assinado" (contrato, `.marca` na data), "01/04/2021: aditivo prorroga 12 meses" (aditivo), "20/02/2023: multa de 2% notificada" (notificacao), "Último pagamento" sem fonte, `.sem-fonte`: "não consta dos papéis". S.T.A.R. da aula: o fio do contrato chega e a data acende; a linha sem fonte mostra a regra do slide `regras`.
40. `trecho` (cena): "Confira o trecho no papel". À esquerda a linha da cronologia ("12/03/2019, contrato.pdf, cláusula terceira"); à direita `caso-contrato-trecho.webp` com a cláusula marcada; um fio liga as duas. Notas: peça a alguém da sala que aponte o trecho.
41. `limite` (cartoes, 3): "O que o agente não decide". "A data: você confere no papel." "A tese: é sua." "A minuta: você revisa." Rodapé: "Conclusão jurídica fica com a pessoa."

### Bloco E, mão na massa (15 min), arquivos `fonte/e-mao.*`

42. `codex` (comparacao, noite): "O mesmo pedido no Codex". A: "Claude, na pasta, ao vivo." B: "Codex, o mesmo pedido, gravado." Pílula "gravação do professor". Notas: o professor grava o mesmo pedido no Codex antes da aula e põe a data da gravação na tela (campo `[data da gravação]` só no HTML do arquivo de vídeo quando existir; sem a gravação, o slide diz "gravação no ensaio" como hoje e o professor decide).
43. `material` (objetos): "O material está no link". Pedido digitado ("Peça a cronologia com arquivo e trecho. Inclua o último pagamento. (O texto completo do pedido está em `pratica2`.)") e os três papéis (`caso-*.webp`) como no WhatsApp. Selo de IA não (imagens são código, não IA).
44. `pratica2` (cena guia, `pratica: 12`): "Sua vez no caso". Duas colunas: Notebook (1 extraia o zip, 2 abra a pasta no app, 3 cole o pedido, 4 confira um trecho) e Celular (1 abra o PDF único, 2 suba no chat, 3 cole o pedido, 4 confira um trecho). Embaixo, o pedido para copiar. Cronômetro 12 min.
45. `travou` (cartoes, 3): "Travou? Três saídas". "Sem plano pago: Codex no app desktop." "Sem notebook: o PDF no celular." "Resposta sem fonte: peça arquivo e trecho de novo." 
46. `quem` (respiro, noite): "Quem trouxe a fonte?" Notas: ouvir duas ou três pessoas; a data sozinha não basta.

### Bloco F, fecho (4 min), arquivos `fonte/f-fecho.*`

47. `registro` (tempo, três marcos): "Resposta, fonte e o que conferir": 1 a resposta, 2 arquivo e trecho, `agora` 3 o que conferir. Legenda: "A mesma entrega nas duas rotas."
48. `fecho` (fecho, claro, logo): "Trabalhe no caso, não no chat." Três passos: reescreva o pedido, abra a pasta, confira a fonte. Notas: no dia 2, MCP, plugins, rotinas, raspagem de jurisprudência do TJMS e do STF, casos práticos, artefatos e devolutiva.

## Pendências e a conferir antes da versão final

- Citações de lei: conferidas (ver acima). O conteúdo jurídico dos demais cases (TCE, ICMS) é do professor.
- Gravação do Codex e link do WhatsApp: só o professor faz.
- Vídeo de reserva: o slide `demo` é simulação por código; a gravação real da aula o substitui.
- Gasto de imagem: US$ 0 nesta versão (documentos e cenas por código); o `heroi-aula2.webp` é da prévia.
