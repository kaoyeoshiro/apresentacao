# Guia do professor: Aulas 3 e 4 do curso de IA (Dia 2)

Versão de 06/11/2026. Cada aula tem 90 minutos. A Aula 3 está em `cojuris.com.br/apresentacao/aula-3/` e a Aula 4 em
`cojuris.com.br/apresentacao/aula-4/`; sem internet, as duas abrem do computador com `./ap abrir decks/curso-ia-aula3`
e `./ap abrir decks/curso-ia-aula4`.

## 1. Como usar este guia

O guia é o mapa das duas aulas, e não o roteiro de fala. O texto do que dizer em cada slide já está nas notas, que
aparecem na tela do apresentador, ao lado do slide atual, do próximo e do cronômetro das atividades (ele dispara
sozinho quando a atividade entra). Aqui ficam o que as notas não dão de uma vez: em que minuto você deveria estar,
quando a sala trabalha, qual arquivo abrir em cada demonstração e onde está cada material.

Com a apresentação aberta e projetada, a tecla P abre a tela do apresentador numa janela separada, que você arrasta para
o notebook. A seta para a direita, o espaço e o passador avançam; a seta para a esquerda volta. Para pular a um slide,
digite o número e aperte Enter. G abre o índice, B apaga a tela (bom para conversa longa) e F liga a tela cheia.

As atividades das duas aulas são feitas em dupla, com o enunciado no slide e sem computador, porque boa parte da turma
não tem plano pago. Quem mexe no Claude durante a aula é você, na tela projetada, e a sala decide junto: dita as regras
da skill, vota o tema da jurisprudência, confere as linhas da planilha. A prática no computador de cada um fica para
casa, com o kit do GitHub, que repete todas as demonstrações.

## 2. Antes da aula

A Aula 4 não pede preparo além de conferir que os vídeos dos slides 5 e 12 tocam, e que o som baixo dos dois sai na caixa da sala. A Aula 3 depende de cinco demonstrações ao
vivo, e cada uma precisa estar ensaiada e gravada, porque a regra da aula é uma tentativa só: sem resultado útil em 60
segundos (40 no TJMS), você para e toca a gravação do ensaio na moldura do slide. Hoje as molduras dos slides 5, 15, 27,
29 e 38 tocam uma gravação provisória, de outra aula, que mostra um pedido de contestação; sem as gravações novas, a
reserva não existe.

- Gravar o ensaio de cada demonstração da Aula 3 (Word, conector, TJMS, script e rotina) e mandar os vídeos para serem
  colocados nas molduras.
- Baixar o kit em `github.com/kaoyeoshiro/kit-dia2-curso-ia` (botão Code, Download ZIP) e extrair na Área de Trabalho.
  Todo arquivo que você abre na Aula 3 está nele, no mesmo lugar em que os alunos vão achar.
- Na conta do Claude da demonstração, em Settings > Capabilities, deixar ligado "Create and edit files". Em Customize >
  Connectors, deixar livre a vaga de conector próprio (no plano gratuito cabe um só).
- No Chrome, a extensão Claude in Chrome conectada e a skill de consulta ao TJMS ativa.
- O Claude Code aberto numa pasta vazia, para a etapa 2 do scraper.
- Na véspera, rodar os três temas da votação no script do kit, dentro da pasta `scraper`:
  `python3 stj_espelhos.py --tema "execução fiscal"`, depois `--tema improbidade` e `--tema ICMS`. Tema que vier vazio
  sai da votação.
- No ensaio da rotina, conferir se a tarefa agendada roda com o computador desligado. Se não rodar, a legenda do slide
  37 deixa de prometer isso (a nota do slide explica).

## 3. Onde está o material

Quase tudo está no kit público; duas reservas do scraper ficam só no repositório das apresentações, porque não podem
ser redistribuídas ou só servem a você. A tabela diz o caminho dentro do kit e, quando o arquivo não está nele, o
caminho no repositório.

| arquivo | para quê | onde |
|---|---|---|
| `modelo-timbrado.docx` | demonstração do Word (slide 5) e A2 (slide 12) | kit, `escritorio/` |
| `rascunho-parecer.md` | o rascunho que vira parecer, nas mesmas duas | kit, `escritorio/` |
| `padrao-do-escritorio.md` e `logo-escritorio.png` | o padrão do escritório fictício Dias & Moura | kit, `escritorio/` |
| `SKILL.md` da skill com defeitos | A1 (slide 9); não instalar | kit, `skill-defeituosa/` |
| `peticao-injecao.pdf` | A3 e slide 18 (selecionar tudo para revelar a ordem) | kit, `peticao/` |
| `stj_espelhos.py` e `amostra/20260930.json` | etapa 2 do scraper e o plano sem internet | kit, `scraper/` |
| `atividades.md` | gabarito da A1 e da A3 | kit, `gabarito/` |
| `execucao.csv`, `improbidade.csv`, `icms.csv` | planilha pronta de cada tema, reserva da etapa 2 | repositório, `decks/curso-ia-aula3/material/scraper/amostra/` |
| `tjms.html` | página salva do TJMS, reserva da etapa 1 | só no seu computador, na mesma pasta acima |

O PDF de emergência de cada aula, um quadro por clique, fica em
`cojuris.com.br/apresentacao/aula-3/apresentacao-emergencia.pdf` e no endereço equivalente da Aula 4.

## 4. Aula 3: A IA fora do chat

### 4.1. O que a aula quer

A mensagem cabe numa frase: a IA trabalha fora do chat quando você lhe dá o jeito (a skill), a tomada (o conector e o
plugin) e a agenda (a rotina), e você continua conferindo a fonte. São seis atividades da sala, de A1 a A6, e cinco
demonstrações suas.

A Aula 2 já explicou o que é uma skill, mostrou o SKILL.md por dentro e rodou a skill de conferir temas no caso, e
a Aula 3 não repete essa parte. A fala do slide 2 lembra em uma frase o jeito, a tomada e o pacote da Aula 2 e anuncia
a peça nova, a rotina. O que a Aula 3 acrescenta em skills são três coisas que a Aula 2 não fez: a skill de Word que já
vem no Claude, transformando um rascunho em parecer no papel timbrado (slides 4 a 6); ler uma skill de terceiro antes de
instalar, com os sete pontos e a auditoria da A1 (slides 8 a 11); e criar uma skill nova a partir das regras que a
própria sala dita, a A2 (slide 12). É ali que fica a prática de skills do dia.

### 4.2. O mapa, minuto a minuto

Os minutos são aproximados e respeitam o tamanho de cada bloco: abertura 4, skills 24, MCP e plugins 16, scraper 20,
GitHub 5 e rotinas 21. O ensaio cronometrado decide o resto.

| minuto | slides | o que acontece | quem trabalha |
|---|---|---|---|
| 0 a 4 | 1 e 2 | capa e roteiro, com o lembrete da Aula 2 | você |
| 4 a 8 | 3 e 4 | o rascunho sem timbre; "qual das duas vocês protocolariam?" | você pergunta |
| 8 a 12 | 5 e 6 | demonstração do Word, com o pedido para copiar | você, no Claude |
| 12 a 14 | 7 | Claude for Word, só os cartões | você |
| 14 a 18 | 8 | sete pontos antes de instalar | você |
| 18 a 23 | 9 a 11 | A1, os três defeitos; votação e gabarito | duplas |
| 23 a 28 | 12 | A2, a sala dita a skill | sala dita, você executa |
| 28 a 30 | 13 e 14 | a tomada: conector pronto ou próprio | você |
| 30 a 33 | 15 e 16 | demonstração do conector do Microsoft Learn | você, no Claude |
| 33 a 38 | 17 a 20 | A3, a ordem escondida; os casos do STF e do STJ | duplas |
| 38 a 40 | 21 e 22 | o plugin | você |
| 40 a 44 | 23 | A4, tomada ou pacote | duplas |
| 44 a 46 | 24 e 25 | dois jeitos de raspar | você |
| 46 a 48 | 26 | A5, votação do tema | sala |
| 48 a 52 | 27 | etapa 1, o Claude no navegador consulta o TJMS | você, no Chrome |
| 52 a 57 | 28 e 29 | etapa 2, o Claude Code escreve e roda o script | você |
| 57 a 62 | 30, 31 ou 32 | conferência de três linhas da planilha | duplas |
| 62 a 64 | 33 e 34 | regras para raspar; captcha | você |
| 64 a 69 | 35 | o repositório no GitHub | você |
| 69 a 72 | 36 e 37 | rotinas: o boletim de segunda | você |
| 72 a 75 | 38 | demonstração da tarefa agendada | você, no Claude |
| 75 a 77 | 39 | agendar, conferir ou não automatizar | você |
| 77 a 85 | 40 | A6, o que é agendável | duplas |
| 85 a 90 | 41 a 43 | o que levam, o kit, o fecho | você |

Os slides 30, 31 e 32 são a mesma conferência, um para cada tema da votação. Mostre só o do tema vencedor: execução
fiscal segue normalmente para o 30; improbidade, digite 31 e Enter; ICMS, digite 32 e Enter. Terminada a conferência,
digite 33 e Enter.

### 4.3. As demonstrações

Word (slides 5 e 6). Numa conversa nova, anexe `modelo-timbrado.docx` e `rascunho-parecer.md` e cole o pedido do slide
6. Abra o PDF que o Claude devolve e confira com a sala, página por página, o cabeçalho, os estilos e a numeração. O
pedido literal é este:

> Use o modelo do escritório anexo (modelo-timbrado.docx). Transforme este rascunho em parecer no padrão do modelo, com
> o mesmo cabeçalho, estilos e numeração. No fim, gere o PDF e me diga o que não coube no modelo.

A2 (slide 12), a skill que a sala dita. São três passos, um por clique, em sete minutos. Primeiro, anote no chat as três
regras do escritório exatamente como a sala disser (de formatação, de citação, de assinatura). Depois, peça ao Claude
que crie uma skill com essas três regras. Por último, rode a skill no mesmo rascunho da demonstração do Word e confira
cada regra no resultado. Para instalar uma skill própria, o caminho conferido em 05/11/2026 é Customize > Skills > "+" >
"+ Create skill" > "Upload a skill", com a pasta da skill compactada em ZIP; olhe a tela no ensaio, porque o menu muda.
O texto do segundo passo fica a seu critério; uma forma possível é "crie uma skill com estas três regras, para usar
quando eu transformar um rascunho em parecer no modelo timbrado".

Conector (slides 15 e 16). Em Customize > Connectors > "+ Add" > "Add custom connector", dê um nome e cole o endereço
`https://learn.microsoft.com/api/mcp`. Numa conversa nova, ligue o conector, pergunte algo sobre o Word e abra o link
que a resposta citar.

Scraper, etapa 1 (slide 27). No Chrome, com a skill do TJMS, cole o pedido trocando o tema pelo vencedor da A5. Se a
consulta não andar em 40 segundos, toque a gravação e diga à sala que é o ensaio, nunca coleta ao vivo.

> Pesquise no TJMS acórdãos de segundo grau sobre [tema votado], julgados nos últimos três meses. Leia as ementas,
> baixe só os pertinentes e me dê uma planilha com processo, relator, data e o motivo de cada escolha.

Scraper, etapa 2 (slides 28 e 29). No Claude Code, na pasta vazia, cole o pedido com o tema votado. Abra o CSV que o
script gravar e mostre as três primeiras linhas; o slide seguinte as põe lado a lado com o espelho de cada acórdão.

> Escreva um script em Python que baixe o arquivo de setembro de 2026 dos espelhos de acórdãos da Primeira Turma nos
> Dados Abertos do STJ, filtre as ementas por [tema votado] e grave um CSV com classe, processo, relator, órgão, data e
> ementa. Uma requisição por vez.

Rotina (slide 38). Em Scheduled > New task, crie a tarefa com o pedido abaixo e o tema votado. A tarefa roda na nuvem e
não lê arquivo do seu computador, por isso o pedido não cita pasta nenhuma.

> Toda segunda às 7h10, consulte os Dados Abertos do STJ, abra o arquivo mais recente de espelhos de acórdãos da
> Primeira Turma e liste os acórdãos sobre [tema votado], cada um com número, data e ementa resumida. Diga a data do
> arquivo consultado.

### 4.4. As atividades da sala

Todas têm o enunciado no slide e o cronômetro na tela do apresentador. A resposta também está nas notas de cada slide.

| atividade | slide | tempo | o que a sala faz | resposta |
|---|---|---|---|---|
| A1, três defeitos | 9, votação no 10, gabarito no 11 | 4 min | lê três trechos de uma skill e diz que ponto do checklist cada um fere | A fere permissões e dados acessados (dispara em qualquer pedido); B fere arquivos e scripts e comandos (manda a pasta para fora); C fere comandos (executa sem confirmar) |
| A2, a sala dita | 12 | 7 min | dita três regras do escritório | não há gabarito; confira cada regra no parecer gerado |
| A3, a ordem escondida | 17, revelação no 18 | 4 min | procura na petição a ordem dirigida à IA e conta quantas há | duas: uma no rodapé, em letra minúscula, e outra em texto branco no meio da página, que só aparece ao selecionar tudo |
| A4, tomada ou pacote | 23 | 4 min | classifica seis situações em skill, conector pronto, conector próprio ou plugin | 1 conector pronto; 2 conector próprio; 3 skill; 4 conector próprio; 5 plugin; 6 skill |
| A5, o tema | 26, conferência em 30 a 32 | 2 min mais a conferência | vota entre execução fiscal, improbidade e ICMS; depois cada dupla confere três linhas contra o espelho | não há gabarito; conta quem achou divergência |
| A6, o que é agendável | 40 | 8 min | classifica três tarefas e sugere outras | boletim do CNJ, agendar; resumo da pasta do caso, agendar com conferência; controle de prazos, não automatizar |

Na A6, se uma das sugestões da sala couber em "agendar", você pode criar essa rotina ao vivo; senão, crie a do boletim,
que já está pronta no slide 38.

## 5. Aula 4: Quem decide é você

### 5.1. O que a aula quer

A Aula 4 tem mais conversa que tela. Cada bloco termina numa decisão da sala: o acesso que se dá ao assistente, o que
quebra se o preço dobrar, se um modelo chinês pode rodar no órgão, o plano de 30 dias de cada um. Não há demonstração
ao vivo nem arquivo para abrir; os dois vídeos, nos slides 5 e 12, tocam sozinhos. As cinco atividades, de A7 a A11,
dispensam computador, e a última é a devolutiva do curso inteiro.

### 5.2. O mapa, minuto a minuto

Os blocos são assistentes 27 minutos, harness 6, quem paga 23, geopolítica 18 e futuro 16.

| minuto | slides | o que acontece | quem trabalha |
|---|---|---|---|
| 0 a 3 | 1 e 2 | capa e roteiro | você |
| 3 a 14 | 3 a 7 | o chat responde, o assistente age; os cinco do mercado; o vídeo do seu Grok Bot; o que ele lê; quem escreve para você | você narra o vídeo |
| 14 a 20 | 8 e 9 | o sigilo e o acesso; cortar o acesso não apaga a memória | você |
| 20 a 27 | 10 | A7, o acesso mínimo | duplas |
| 27 a 33 | 11 a 13 | o harness: o vídeo dos dez agentes e o custo de cada um | você narra o vídeo |
| 33 a 44 | 14 a 19 | o custo de cada uso, os US$ 895 bi, quem banca, o usuário pesado, o plano que encolhe | você |
| 44 a 48 | 20 e 21 | bolha ou não (mão levantada) e a tese | você pergunta |
| 48 a 56 | 22 e 23 | A8, e se o preço dobrar; o que vai com você | duplas |
| 56 a 66 | 24 a 29 | chips, os quatro meses, aberto não é seguro, CLOUD Act, as regras | você |
| 66 a 74 | 30 | A9, debate sobre o modelo chinês | sala dividida |
| 74 a 80 | 31 a 34 | 2030: o ritmo, os cenários, os sinais | você |
| 80 a 85 | 35 | A10, o plano de 30 dias | cada um |
| 85 a 90 | 36 a 38 | A11, a devolutiva; os quatro verbos; o fecho | roda e você |

No slide 5, o vídeo do Grok Bot tem 62 segundos e efeitos sonoros baixos, sem voz; você fala por cima, na ordem das
cenas: resumo de IA de manhã (5 a 13 s), WhatsApp e agenda (13 a 22), t3code com as quatro IAs (22 a 31), E-MS (31 a
38), PGE.Net (38 a 44), eventos e editais (44 a 50), compras (50 a 55) e todos ligados ao centro (55 a 62). Mensagens,
ofícios e compromissos do vídeo são fictícios.

No slide 12, o vídeo tem 40 segundos, também com efeitos sonoros baixos, e você fala por cima dele, na ordem em que os agentes aparecem: o classificador,
os dois leitores, o agrupador, o redator, os validadores e, por último, o agente que confere o ofício. O slide 11
lembra que a co.juris não fala em nome da PGE-MS; diga isso antes do vídeo.

### 5.3. As atividades da sala

| atividade | slide | tempo | o que a sala faz | resposta-modelo |
|---|---|---|---|---|
| A7, o acesso mínimo | 10 | 7 min | escolhe uma tarefa e preenche o que o assistente pode ler, o que pode escrever e o que nunca toca | para a agenda da manhã: lê a agenda e uma pasta de e-mails; escreve um rascunho salvo, nunca enviado; nunca toca a caixa inteira, o sistema do tribunal, pagamento ou apagar. Fecho: "Duas semanas, só lendo." |
| A8, o preço dobrou | 22, resposta no segundo clique | 5 min | diz o que quebra no trabalho se o plano dobrar de preço | quebra o que está preso ao app: instruções só na memória do chat, documentos só no projeto do fornecedor, nenhum segundo fornecedor testado. O slide 23 mostra o que vai com você |
| A9, debate | 30 | 6 min | metade defende que o modelo chinês pode rodar no órgão, metade que não; dois minutos de preparo, três de debate | seu fecho: rodar dentro da infraestrutura do órgão tira o dado do alcance de terceiros e desloca o risco para o comportamento do modelo, que é o que o CAISI mediu |
| A10, o plano de 30 dias | 35 | 5 min | cada um escreve três linhas no celular: uma skill, uma pasta de caso, uma rotina | não há gabarito; a quem travar na rotina, pergunte o que se perde se ela falhar em silêncio |
| A11, a devolutiva | 36 | 5 min | em roda, cada um diz uma coisa que leva e uma que faltou | anote as faltas para a próxima turma |

## 6. Quando algo der errado

A regra das demonstrações vale para todas: uma tentativa ao vivo, e sem resultado útil em 60 segundos (40 no TJMS) você
para e toca a gravação na moldura do slide. A sala avalia o resultado preparado do mesmo jeito, e a aula não perde o
ritmo. As notas de cada slide trazem a contingência específica; as mais prováveis estão abaixo.

Sem internet, a etapa 2 do scraper roda com a amostra do kit, dentro da pasta `scraper`:
`python3 stj_espelhos.py --tema "execução fiscal" --offline amostra/20260930.json`. A planilha pronta de cada tema
também está em `material/scraper/amostra/`, e a página salva do TJMS substitui a etapa 1, apresentada como gravação do
ensaio. Se aparecer captcha no TJMS, pare a automação, que é exatamente o que o slide 34 ensina, e toque a gravação.

Se o conector não entrar, quase sempre a vaga do plano gratuito está ocupada: desconecte o outro em Customize >
Connectors. Se o Word não sair, confira "Create and edit files" em Settings > Capabilities. Se o projetor falhar ou o
navegador travar, abra o PDF de emergência da aula, que tem um quadro por clique, e siga pelo passador.
