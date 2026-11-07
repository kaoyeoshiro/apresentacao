# Guia do professor: Aulas 3 e 4 do curso de IA (Dia 2)

Versão de 07/11/2026. Cada aula tem 90 minutos. A Aula 3 está em `cojuris.com.br/apresentacao/aula-3/` e a Aula 4 em
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
não tem plano pago. A exceção é a A3: quem puder abre o PDF da petição, do kit, no celular ou no notebook, e quem não
puder faz dupla com quem abriu. Quem mexe no Claude durante a aula é você, na tela projetada, e a sala decide junto:
vota o tema da jurisprudência, confere as linhas da planilha. A prática no computador de cada um fica para
casa, com o kit (o ZIP do site), que repete todas as demonstrações.

## 2. Antes da aula

A Aula 4 não pede preparo além de conferir que os vídeos dos slides 5 e 13 tocam, e que o som baixo dos dois sai na caixa da sala. A Aula 3 depende de cinco demonstrações ao
vivo, e a regra é uma tentativa só: sem resultado útil em 60 segundos (40 no TJMS), você para e usa a reserva. Não há
gravação de nenhuma delas. As molduras dos slides 7, 28 e 39 tocam um vídeo provisório, de outra aula, que mostra
um pedido de contestação; não deixe a sala assistir a ele. O slide 30, da etapa 2, não tem vídeo: desenha o caminho do
script. As reservas reais são o slide 6 e o `modelo-timbrado.docx` (Word), o próprio slide 16, que desenha o resultado
do teste de 06/11/2026 (conector), a página salva `tjms.html`
(etapa 1), o modo offline e as planilhas prontas (etapa 2) e a planilha da etapa 2 ou o pedido colado, sem salvar
(rotina).

- Ensaiar cada demonstração da Aula 3 (Word, conector, TJMS, script e rotina) na conta e no computador da aula.
- Baixar o kit em `https://www.cojuris.com.br/kit/kit-dia2-curso-ia.zip`, o endereço do slide 43, e extrair na Área de Trabalho. Todo arquivo que você abre na
  Aula 3 está nele, no mesmo lugar em que os alunos vão achar, já com a petição nova da A3 e o script que grava
  `.xlsx`; é também o endereço para a sala abrir o PDF na A3. O repositório `github.com/kaoyeoshiro/kit-dia2-curso-ia`
  é só referência: até ser atualizado, traz a versão anterior.
- Na conta do Claude da demonstração, em Settings > Capabilities, deixar ligado "Create and edit files". Em Customize >
  Connectors, deixar livre a vaga de conector por endereço (no plano gratuito cabe um só).
- No Chrome, a extensão Claude in Chrome conectada e a skill de consulta ao TJMS ativa.
- O Claude Code aberto numa pasta vazia, para a etapa 2 do scraper.
- Na véspera, rodar os três temas da votação no script do kit, dentro da pasta `scraper`:
  `python3 stj_espelhos.py --tema "execução fiscal" --arquivo 20260930.json`, depois `--tema improbidade` e `--tema ICMS`.
  Cada rodada grava `boletim-stj.xlsx` e `boletim-stj.csv` e confere as seis colunas; use `--saida` para não
  sobrescrever. Tema que vier vazio sai da votação. Abra uma vez a pesquisa de jurisprudência do STJ
  (`scon.stj.jus.br`) no computador da aula e cole um dos números da A5: o site pode pedir verificação do navegador.
- No ensaio da rotina, conferir se a tarefa agendada roda com o computador desligado. Se não rodar, a legenda do slide
  38 deixa de prometer isso (a nota do slide explica).

## 3. Onde está o material

Quase tudo está no kit público; duas reservas do scraper ficam só no repositório das apresentações, porque não podem
ser redistribuídas ou só servem a você. A tabela diz o caminho dentro do kit e, quando o arquivo não está nele, o
caminho no repositório.

| arquivo | para quê | onde |
|---|---|---|
| `modelo-timbrado.docx` | demonstração do Word (slide 7) | kit, `escritorio/` |
| `rascunho-parecer.md` | o rascunho que vira parecer, na mesma demonstração | kit, `escritorio/` |
| `padrao-do-escritorio.md` e `logo-escritorio.png` | o padrão do escritório fictício Dias & Moura | kit, `escritorio/` |
| `SKILL.md` da skill com defeitos | A1 (slide 11); não instalar | kit, `skill-defeituosa/` |
| `peticao-injecao.pdf` | A3 (slide 18) e slide 19, que revela as duas ordens | kit, `peticao/` |
| `stj_espelhos.py` e `amostra/20260930.json` | etapa 2 do scraper e o plano sem internet | kit, `scraper/` |
| `atividades.md` | gabarito da A1 e da A3 | kit, `gabarito/` |
| `execucao.xlsx`, `improbidade.xlsx`, `icms.xlsx` (com o `.csv` de mesmo nome ao lado) | planilha pronta de cada tema, reserva da etapa 2 | repositório, `decks/curso-ia-aula3/material/scraper/amostra/` |
| `tjms.html` | página salva do TJMS, reserva da etapa 1 | só no seu computador, na mesma pasta acima |

O PDF de emergência de cada aula, um quadro por clique, fica em
`cojuris.com.br/apresentacao/aula-3/apresentacao-emergencia.pdf` e no endereço equivalente da Aula 4.

## 4. Aula 3: A IA fora do chat

### 4.1. O que a aula quer

A mensagem cabe numa frase: a IA trabalha fora do chat quando você lhe dá o jeito (a skill), a tomada (o conector e o
plugin) e a agenda (a rotina), e você continua conferindo a fonte. São cinco atividades da sala (A1 e A3 a A6; a A2 saiu
em 07/11/2026, e os rótulos ficaram para casar com o kit) e cinco demonstrações suas.

A Aula 2 já explicou o que é uma skill, mostrou o SKILL.md por dentro e rodou a skill de conferir temas no caso, e
a Aula 3 não repete essa parte. A fala do slide 2 lembra em uma frase o jeito, a tomada e o pacote da Aula 2 e anuncia
a peça nova, a rotina. Logo depois, os slides 3 e 4 retomam na tela, em dois minutos, o jeito de organizar as pastas
que entrou na Aula 2 (`meu-jeito`): uma pasta por assunto, com o CLAUDE.md de cada nível (no Codex, AGENTS.md), e a
diferença entre o arquivo na pasta e o Projeto. Só o Claude Code aparece lendo o arquivo sozinho; o app Claude e o
Codex ficam nas notas. O que a Aula 3 acrescenta em skills são duas coisas que a Aula 2 não fez: a skill de Word que já
vem no Claude, transformando um rascunho em parecer no papel timbrado (slides 6 a 8), e ler uma skill de terceiro antes
de instalar, com os sete pontos e a auditoria da A1 (slides 10 a 13), que é a prática de skills do dia.

### 4.2. O mapa, minuto a minuto

Os minutos são aproximados e respeitam o tamanho de cada bloco: abertura 6, skills 17, MCP e plugins 18, scraper 22,
GitHub 5 e rotinas 22. O ensaio cronometrado decide o resto.

| minuto | slides | o que acontece | quem trabalha |
|---|---|---|---|
| 0 a 4 | 1 e 2 | capa e roteiro, com o lembrete da Aula 2 | você |
| 4 a 6 | 3 e 4 | retomada da Aula 2: uma pasta por assunto; arquivo na pasta ou Projeto | você |
| 6 a 9 | 5 e 6 | o rascunho sem timbre; "qual das duas vocês protocolariam?" | você pergunta |
| 9 a 13 | 7 e 8 | demonstração do Word, com o pedido para copiar | você, no Claude |
| 13 a 14 | 9 | Claude for Word, só os cartões | você |
| 14 a 18 | 10 | sete pontos antes de instalar | você |
| 18 a 23 | 11 a 13 | A1, os três defeitos; votação e gabarito | duplas |
| 23 a 25 | 14 e 15 | a tomada: conector da lista ou por endereço | você |
| 25 a 31 | 16 e 17 | demonstração do conector do Microsoft Learn | você, no Claude |
| 31 a 35 | 18 a 21 | A3, as ordens escondidas no PDF; a revelação, os casos do STF e do STJ, a regra | duplas |
| 35 a 37 | 22 e 23 | o plugin e o limite do aviso | você |
| 37 a 41 | 24 | A4, tomada ou pacote | duplas |
| 41 a 43 | 25 e 26 | dois jeitos de raspar | você |
| 43 a 45 | 27 | A5, votação do tema | sala |
| 45 a 49 | 28 | etapa 1, o Claude no navegador consulta o TJMS | você, no Chrome |
| 49 a 55 | 29 e 30 | etapa 2, o Claude Code escreve e roda o script | você |
| 55 a 60 | 31, 32 ou 33 | conferência de três linhas da planilha | duplas |
| 60 a 63 | 34 e 35 | regras para raspar; captcha | você |
| 63 a 68 | 36 | o repositório no GitHub | você |
| 68 a 71 | 37 e 38 | rotinas: o boletim de segunda | você |
| 71 a 74 | 39 | demonstração da tarefa agendada | você, no Claude |
| 74 a 76 | 40 | agendar, conferir ou aprovar antes | você |
| 76 a 84 | 41 | A6, o que é agendável | duplas |
| 84 a 90 | 42 a 44 | o que levam, o kit, o fecho | você |

Os slides 31, 32 e 33 são a mesma conferência, um para cada tema da votação. Mostre só o do tema vencedor: execução
fiscal segue normalmente para o 31; improbidade, digite 32 e Enter; ICMS, digite 33 e Enter. Terminada a conferência,
digite 34 e Enter.

### 4.3. As demonstrações

Word (slides 7 e 8). Numa conversa nova, anexe `modelo-timbrado.docx` e `rascunho-parecer.md` e cole o pedido do slide
8. Abra o PDF que o Claude devolve e confira com a sala, página por página, o cabeçalho, os estilos e a numeração. O
pedido literal é este:

> Use o modelo do escritório anexo (modelo-timbrado.docx). Transforme este rascunho em parecer no padrão do modelo, com
> o mesmo cabeçalho, estilos e numeração. No fim, gere o PDF, confira as páginas e me diga o que não coube no modelo e
> o que você decidiu sem eu ter pedido.

O modelo numera sozinho os títulos de seção (1., 2., 3.), como a versão B do slide 6. A última frase pede prestação de
contas; não garante nada, e por isso a conferência do arquivo continua sendo sua.

Conector (slides 16 e 17). Em Customize > Connectors > "+ Add" > "Add custom connector", dê um nome e cole o endereço
`https://learn.microsoft.com/api/mcp`. Numa conversa nova, ligue o conector, pergunte "Como coloco uma caixa do Exchange
Online em retenção para litígio?" e abra o link que a resposta citar. Evite perguntas de usuário do Word, que no teste
trouxeram fórum e página de programador; link que começa por `learn.microsoft.com/answers` é fórum de usuários.

Scraper, etapa 1 (slide 28). No Chrome, com a skill do TJMS, cole o pedido trocando o tema pelo vencedor da A5. Se a
consulta não andar em 40 segundos, abra a página salva `tjms.html` e diga à sala que é do ensaio, nunca coleta ao vivo.

> Pesquise no TJMS acórdãos de segundo grau sobre [tema votado], julgados nos últimos três meses. Leia as ementas,
> baixe só os pertinentes e me dê uma planilha com processo, relator, data e o motivo de cada escolha.

Scraper, etapa 2 (slides 29 e 30). No Claude Code, na pasta vazia, cole o pedido com o tema votado. O slide 30 desenha
o caminho que o script faz; não é gravação. Abra o `boletim-stj.xlsx` que o script gravar (dois cliques; no Mac, o
Numbers também abre) e mostre as três primeiras linhas; a conferência seguinte as põe lado a lado com o espelho de cada
acórdão. O pedido exige a planilha em `.xlsx` porque, no ensaio de 06/11/2026, o CSV abriu no Excel com tudo na coluna
A. Se precisar do `.csv`, não abra com dois cliques: no Excel, Dados > De Texto/CSV, origem UTF-8 e delimitador ponto
e vírgula. Se o script do Claude Code falhar, rode o do kit (`--offline amostra/20260930.json`) ou abra a planilha
pronta do tema.

> Escreva um script em Python que baixe, nos Dados Abertos do STJ, o arquivo JSON de setembro de 2026 (20260930.json)
> dos espelhos de acórdãos da Primeira Turma, com uma requisição por vez, e filtre as ementas por [tema votado]. Grave a
> planilha boletim-stj.xlsx com seis colunas separadas, nesta ordem: classe, processo, relator, orgao, data, ementa. O
> processo vai como texto, a data como data (dd/mm/aaaa) e a ementa inteira numa célula só. Grave também
> boletim-stj.csv para importar: UTF-8 com BOM, separador ponto e vírgula, todos os campos entre aspas. No fim, reabra
> os dois arquivos, confira seis colunas em cada linha e me diga quantas linhas gravou.

Conferência (slides 31 a 33). Ao lado de cada número de processo há um botão "copiar", que copia só o número; o toque
no botão não avança o slide. Cole na pesquisa de jurisprudência do STJ (`scon.stj.jus.br`): o número sozinho traz o
processo em qualquer classe, e a linha da planilha diz qual é a sua. Se a área de transferência recusar, o botão diz
"selecionado" e deixa o número selecionado para Ctrl+C (Cmd+C). Seta, Espaço e clique fora do botão continuam
avançando.

Rotina (slide 39). Em Scheduled > New task, crie a tarefa com o pedido abaixo e o tema votado. A tarefa roda na nuvem e
não lê arquivo do seu computador, por isso o pedido não cita pasta nenhuma. É a versão de aula: o arquivo do STJ é
mensal e sai em datas irregulares, e a janela de 7 dias mostra a ideia de checar a data. Ela depende do fuso e da hora
de corte, e uma execução que falha não recupera o arquivo; para uso real, a rotina guarda o que já processou e avisa
quando falhar.

> Toda segunda às 7h10, consulte os Dados Abertos do STJ e veja quais arquivos de espelhos de acórdãos da Primeira Turma
> foram publicados nos últimos 7 dias. Para cada um, liste os acórdãos sobre [tema votado], com número, data da decisão
> e as duas primeiras linhas da ementa, copiadas sem resumir. Se não houver arquivo novo, responda só "sem arquivo novo
> desde [data de publicação do mais recente]". Diga sempre o nome e a data de publicação de cada arquivo consultado.

### 4.4. As atividades da sala

Todas têm o enunciado no slide e o cronômetro na tela do apresentador. A resposta também está nas notas de cada slide.

| atividade | slide | tempo | o que a sala faz | resposta |
|---|---|---|---|---|
| A1, três defeitos | 11, votação no 12, gabarito no 13 | 4 min | lê três trechos de uma skill e diz que ponto do checklist cada um fere | aceite mais de um ponto por trecho. A fere dados acessados (entra onde não foi chamada); B fere comandos e dados acessados (manda a pasta para fora; quem não lê código pega por arquivos e scripts); C fere permissões (executa sem pedir) |
| A3, as ordens escondidas | 18, revelação no 19 | 2 min | abre o PDF do kit e conta quantas ordens dirigidas à IA há nele | duas, as duas em branco, a cor do papel: um parágrafo em corpo 2 no meio da página 1 (entre "Dos fatos" e "Do direito"), que a seleção costuma revelar; e uma linha em corpo 2 colada ao canto inferior direito da página 2, a 1 pt das bordas, que quase ninguém vê. Localização exata nas notas do slide 18 e no gabarito do kit. O agente pode obedecer ou ignorar sem avisar |
| A4, tomada ou pacote | 24 | 4 min | classifica seis situações em skill, conector da lista, conector por endereço ou plugin | 1 conector da lista; 2 conector por endereço; 3 skill; 4 conector por endereço (servidor autorizado pela TI; ligar sistema interno não é decisão do aluno); 5 plugin; 6 skill |
| A5, o tema | 27, conferência em 31 a 33 | 2 min mais a conferência | vota entre execução fiscal, improbidade e ICMS; depois cada dupla confere três linhas contra o espelho, com o botão "copiar" para colar o número na pesquisa do STJ | não há gabarito; conta quem achou divergência |
| A6, o que é agendável | 41 | 8 min | classifica três tarefas e sugere outras | boletim semanal de notícias do CNJ, agendar (se falhar, perde-se uma leitura); andamento do processo no e-SAJ resumido para você, com conferência (a fonte continua o e-SAJ do TJMS, e a intimação, o DJEN e o Domicílio Judicial Eletrônico); esse resumo enviado ao cliente por WhatsApp, aprovar antes (a mensagem sai do escritório e não volta; um aviso padrão e limitado, combinado por escrito com o cliente, pode valer como autorização prévia daquele modelo). É exemplo: ninguém cria consulta automática nem envio real |

Na A6, se uma das sugestões da sala couber em "agendar", você pode criar essa rotina ao vivo; senão, crie a do boletim,
que já está pronta no slide 39. O portal da tarefa 2 é a consulta pública do e-SAJ do TJMS pelo número unificado
(`esaj.tjms.jus.br/cpopg5/open.do`, 1º grau, com reCAPTCHA invisível; `esaj.tjms.jus.br/cposg5/open.do`, 2º grau),
conferida em 07/11/2026 sem entrar em conta nem consultar processo. O DataJud, do CNJ, é Beta e não garante atualidade;
o Comunica PJe só traz o que saiu no DJEN. Nenhum dos dois substitui o andamento no tribunal.

## 5. Aula 4: Quem decide é você

### 5.1. O que a aula quer

A Aula 4 tem mais conversa que tela. Cada bloco termina numa decisão da sala: o acesso que se dá ao assistente, o que
quebra se o plano mudar, em que condições um modelo chinês pode rodar no órgão, como cada um imagina a própria carreira daqui a 20 anos, o plano de 30 dias. Não há demonstração
ao vivo nem arquivo para abrir; os dois vídeos, nos slides 5 e 13, tocam sozinhos. As seis atividades (A7 a A11 e o debate do futuro)
dispensam computador, e a última é a devolutiva do curso inteiro.

### 5.2. O mapa, minuto a minuto

Os blocos são assistentes 26 minutos, harness 6, quem paga 19, geopolítica 15 e futuro 24.

| minuto | slides | o que acontece | quem trabalha |
|---|---|---|---|
| 0 a 3 | 1 e 2 | capa e roteiro | você |
| 3 a 13 | 3 a 7 | o chat responde, o assistente age; os sete do mercado; o vídeo do seu Grok Bot; o que ele lê; quem escreve para você | você narra o vídeo |
| 13 a 21 | 8 a 10 | o sigilo e o acesso; cortar o acesso não apaga a memória; assinatura não é contrato (treino e retenção) | você |
| 21 a 26 | 11 | A7, o acesso mínimo | duplas |
| 26 a 32 | 12 a 14 | o harness: o vídeo dos oito agentes e duas buscas, e o custo de cada um | você narra o vídeo |
| 32 a 41 | 15 a 20 | a computação que já cabe na receita (treino incluído), os US$ 895 bi, quem banca, o usuário pesado, o plano que encolhe | você |
| 41 a 45 | 21 e 22 | bolha ou não (mão levantada) e a tese | você pergunta |
| 45 a 51 | 23 e 24 | A8, e se o plano mudar; o que vai com você | duplas |
| 51 a 60 | 25 a 30 | chips, os quatro meses, aberto não é seguro, CLOUD Act, as regras | você |
| 60 a 66 | 31 | A9, em que condições o modelo chinês pode rodar no órgão | duplas |
| 66 a 71 | 32 a 38 | e em 20 anos? o ritmo, os quatro cenários da OCDE, os otimistas, os pessimistas, o que já se mede (19%), os horizontes de 2 a 20 anos | você |
| 71 a 79 | 39 | debate: sua carreira em 2046 | duplas |
| 79 a 80 | 40 | os sinais para acompanhar | você |
| 80 a 85 | 41 | A10, o plano de 30 dias | cada um |
| 85 a 89 | 42 | A11, a devolutiva (cronômetro de 4 minutos: dois escrevendo, depois a roda) | cada um, depois a roda |
| 89 a 90 | 43 e 44 | os quatro verbos; o fecho | você |

No slide 5, o vídeo do Grok Bot tem 62 segundos e efeitos sonoros baixos, sem voz; você fala por cima, na ordem das
cenas: resumo de IA de manhã (5 a 13 s), WhatsApp e agenda (13 a 22), t3code com as quatro IAs (22 a 31), E-MS (31 a
38), PGE.Net (38 a 44), eventos e editais (44 a 50), compras (50 a 55) e todos ligados ao centro (55 a 62). Mensagens,
ofícios e compromissos do vídeo são fictícios.

No slide 13, o vídeo tem 40 segundos, também com efeitos sonoros baixos, e você fala por cima dele, na ordem em que os agentes aparecem (o vídeo escreve
"10 agentes" porque conta as duas buscas, marcadas nele como ferramenta): o classificador,
os dois leitores, o agrupador, o redator, os validadores e, por último, o agente que confere o ofício. O slide 12
lembra que a co.juris não fala em nome da PGE-MS; diga isso antes do vídeo.


No slide 29 (CLOUD Act), "quem pode mandar entregar" quer dizer o seguinte: se o órgão contrata a nuvem de uma empresa
americana, uma autoridade dos EUA pode ordenar a essa empresa que preserve ou entregue os dados sob o controle dela,
mesmo guardados num data center no Brasil (18 U.S.C. § 2713). O lugar do servidor não protege; o que conta é quem
controla o dado. Para o conflito com a lei do outro país, só Reino Unido e Austrália têm acordo com os EUA.

No slide 16, os 57% são toda a computação da Anthropic sobre a receita, treino dos modelos incluído; só atender
clientes pagantes custou cerca de 14,5% da receita. O que ainda não se paga são os compromissos de data centers dos
próximos anos (slides 17 e 18).

No slide 34, os quatro cenários são da OCDE e estão no Relatório Internacional de Segurança da IA (fev. 2026), que
diz não haver consenso sobre o mais provável. A projeção de tarefas de software de vários dias em 2030 é do METR, se a
tendência atual continuar; os gargalos de dados, chips, capital e energia são opinião de alguns especialistas para
depois de 2030. Os slides 35 a 38 trazem quem disse cada coisa e quando; as notas de cada um têm a fonte.

No slide 10, quem decide é o tipo de contrato. Na assinatura individual o treino depende de um botão (ligado
por padrão no ChatGPT e no Gemini pessoal; no Claude, escolha pedida desde 28/08/2025, com até cinco anos de guarda
para quem permite treino e 30 dias para quem não permite). No contrato empresarial e na API paga, Anthropic, OpenAI,
Google, AWS e Microsoft declaram não treinar com os dados do cliente; ainda assim guardam por até 30 dias (Google, 55)
para detectar abuso, e retenção zero só vem com pedido aprovado. A API gratuita do Gemini usa o conteúdo para melhorar
produtos. Fonte e prazos por serviço em `docs/pesquisa/dia2-retencao-e-treino.md`.

### 5.3. As atividades da sala

| atividade | slide | tempo | o que a sala faz | resposta-modelo |
|---|---|---|---|---|
| A7, o acesso mínimo | 11 | 5 min | escolhe uma tarefa e preenche o que o assistente pode ler, o que pode escrever e o que nunca toca | para a agenda da manhã: lê a agenda e uma conta de e-mail separada, que recebe por encaminhamento só os e-mails escolhidos (no Gmail, a leitura vale para a caixa inteira e o rascunho também envia); escreve um resumo num arquivo ou um rascunho nessa conta; nunca toca a caixa principal, o sistema do tribunal, pagamento, apagar, link ou anexo de quem escreveu. Cortado o acesso, memória e histórico podem continuar retidos no fornecedor. Quarta linha: se ele errar ou se calar, quem percebe? Fecho: "Duas semanas, só lendo." |
| A8, o plano mudou | 23, resposta no segundo clique | 4 min | em dois cenários separados (o preço dobra; a franquia cai à metade), diz o que quebra e quantas horas por mês o aumento precisa poupar, pela própria fatura | quebra o que está preso ao app: instruções só na memória do chat, documentos só no projeto do fornecedor, nenhum segundo fornecedor testado. A conta costuma mudar a resposta de "cancelo" para "pago e tiro o trabalho do app". O slide 24 mostra o que vai com você |
| A9, condições | 31 | 5 min | diz em que condições um modelo aberto chinês, sem internet, no servidor do órgão, pode resumir petições; dois minutos de preparo, três para ouvir as condições | seu fecho: rodar dentro da infraestrutura do órgão tira o dado do alcance de terceiros e desloca o risco para o comportamento do modelo, que é o que o CAISI mediu |
| Debate, sua carreira em 2046 | 39 | 8 min | em dupla, um defende o futuro otimista e o outro o pessimista, cada um com um dado dos slides; 2 min de preparo, 4 de conversa, 2 para três duplas contarem; no fim, cada um diz o que muda já na semana que vem | não há gabarito; o slide 38 lembra que em 20 anos ninguém mede, e a pergunta de fecho puxa para o plano de 30 dias |
| A10, o plano de 30 dias | 41 | 5 min | cada um escreve três linhas no celular: uma skill, uma pasta de caso no próprio disco, uma rotina; em cada semana, teste fictício primeiro, um número de sucesso e o que ela nunca faz | não há gabarito; a quem travar na rotina, pergunte o que se perde se ela falhar em silêncio |
| A11, a devolutiva | 42 | 4 min | dois minutos escrevendo (leva: o que vai fazer na segunda-feira; faltou: o que queria ter feito com as mãos), depois a roda | anote as faltas para a próxima turma; no minuto 89, vá para o fecho |

## 6. Quando algo der errado

A regra das demonstrações vale para todas: uma tentativa ao vivo, e sem resultado útil em 60 segundos (40 no TJMS) você
para e usa a reserva da seção 2; não há gravação. A sala avalia o resultado preparado do mesmo jeito, e a aula não perde
o ritmo. As notas de cada slide trazem a contingência específica; as mais prováveis estão abaixo.

Sem internet, a etapa 2 do scraper roda com a amostra do kit, dentro da pasta `scraper`:
`python3 stj_espelhos.py --tema "execução fiscal" --offline amostra/20260930.json`, que grava `boletim-stj.xlsx` e
`boletim-stj.csv`. A planilha pronta de cada tema (`execucao.xlsx`, `improbidade.xlsx`, `icms.xlsx`) também está em `material/scraper/amostra/`, e a página salva do TJMS substitui a etapa 1, apresentada como gravação do
ensaio. Se aparecer captcha no TJMS, pare a automação, que é exatamente o que o slide 35 ensina, e abra a página salva.

Se o conector não entrar, quase sempre a vaga do plano gratuito está ocupada: desconecte o outro em Customize >
Connectors. Se o Word não sair, confira "Create and edit files" em Settings > Capabilities. Se o projetor falhar ou o
navegador travar, abra o PDF de emergência da aula, que tem um quadro por clique, e siga pelo passador.
