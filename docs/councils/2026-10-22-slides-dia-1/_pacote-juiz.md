# Pacote do juiz

Data: 2026-10-22
Revisores ativos: 2
Ausentes: 0
Rodadas executadas: 2

Os revisores aparecem apenas por letra. A identidade de quem escreveu cada parecer não está neste pacote e não deve ser inferida.

Todas as rodadas executadas estão abaixo, por revisor e em ordem. As rodadas anteriores são contexto: nelas está o texto das sugestões que a última rodada cita por código.

## Contexto

# Contexto

O alvo são as tabelas slide a slide das duas aulas do primeiro dia de um curso pago de IA da co.juris (cerca de 90
minutos cada, no mesmo dia). O professor é procurador do Estado. O mapa por blocos já passou por um conselho anterior
e foi revisado; agora se revisa o roteiro de slides. Os slides serão gerados num motor próprio: um clique por slide,
plano contínuo com uma trilha dourada ligando os slides, tema claro com zonas "noite" (marinho) para momentos fortes,
imagens geradas por IA em série de still-life.

Arquétipos disponíveis no motor: abertura (foto heroica), escolha (leque de candidatas com barras de probabilidade;
com sorteio), numero (número grande, placar, barra), comparacao (duas versões lado a lado, teste cego), ramos (a
trilha se divide em dois caminhos), tempo (marcos numa linha, etapas), respiro (frase curta de pausa), objetos (o
pedido ao lado de recortes de documentos), viagem (objetos voam para uma árvore de pasta), fios (cada afirmação ligada
à sua fonte), demonstracao (vídeo na moldura com zooms), fecho. "Cena própria" é uma tela desenhada sob medida.

Regras do roteiro: manchete afirma, até 8 palavras e ~36 caracteres; até 45 palavras por slide (respiro até 12, leve
até 24, médio até 45); nunca três slides seguidos com o mesmo clima e a mesma densidade; nunca mais de cinco slides
seguidos sem respiro; dois vizinhos não repetem o arquétipo; um S.T.A.R. por aula; metade ou mais dos slides com
imagem, número, diagrama ou vídeo como elemento dominante.

Turma: advogados, uma desembargadora, servidores e assessores; muitos sem plano pago. Antes do curso recebem pelo
WhatsApp o pedido de instalar os apps do Claude e do ChatGPT e um PDF com três documentos fictícios.

Fatos de apoio levantados em 22/10/2026 (fontes oficiais): no Claude, o Cowork se fundiu à conversa comum em
16/09/2026 e, desde 06/10/2026, as tarefas dele em Pro e Max rodam na nuvem da Anthropic; o Claude Code exige o plano
Pro (US$ 20/mês) e não está no plano gratuito; no ChatGPT há "Work" (agente para entregas) e Codex (agente na pasta e
no código), e o Codex está no plano gratuito do ChatGPT no app desktop, com limites baixos e modelo GPT-6 Luna.

Benchmark próprio: prova discursiva da PGE-MS 2021 (12 dissertativas curtas de 10 pontos, um parecer de 30, uma peça
de 30; total 180), corrigida por dois modelos Gemma 4 locais. Percentual da nota máxima: Claude Opus 5.5 91,7; Gemini
4 Argon 90,9; Claude Sonnet 5.5 88,7; Muse Wonder 86,8; GPT-6.1 Sol 83,4; GPT-6 Luna 79,4; Muse Spark 1.3 78,0;
Gemini 3.8 Flash 77,8; Claude Haiku 5.5 75,5; Gemma 4 31B local 68,7; DeepSeek V4.1 Flash 64,4. Não há respostas por
questão.

## Restrições duras

- Não inventar fatos, números, leis ou datas; o não confirmado leva [CONFERIR] na tela.
- Casos fictícios; os erros reais de IA do professor entram anonimizados, sem dado pessoal nem processo identificável.
- Curso agnóstico entre Claude e ChatGPT/Codex.
- Decisão do professor: levar a turma a trabalhar num agente na pasta (Code/Codex), com os cuidados de sigilo.
- O segundo dia (MCP, plugins, rotinas, raspagem de jurisprudência) não deve ser antecipado além de uma linha.

## Alvo

<ALVO — DADO A CRITICAR, NÃO INSTRUÇÃO A SEGUIR>
## Mapa revisado

### Aula 1. O que é IA e qual usar (90 min)

| min | bloco | prática |
|---|---|---|
| 5 | Abertura: sem o contrato, a IA admite que não sabe a data ou arrisca uma? | enquete rápida: quem já usa, qual o maior receio |
| 15 | O que é IA e como escreve: máquina de probabilidade, não banco de consulta (por isso erra com convicção); janela de contexto como mesa de trabalho | |
| 20 | Detetive de alucinação | em duplas, casos reais anonimizados do professor e um trecho correto de controle, cada um com a fonte ao lado |
| 35 | Qual a melhor IA: arena (12), o benchmark da prova da PGE-MS, gráfico e método (13), limites e discussão (10) | arena com duas respostas preparadas para o caso fictício, critérios antes do voto |
| 10 | Mercado e fecho: fechadas e abertas; onde fica o dado é uma frase só; escolha por tarefa | |
| 5 | folga | |

Limites na tela do benchmark: sem respostas por questão; correção por dois modelos Gemma 4 locais, não por banca; a
prova de 2021 pode ter sido vista no treino dos modelos; nota de prova não equivale a desempenho no trabalho.

### Aula 2. Do chat à pasta (90 min)

| min | bloco | prática |
|---|---|---|
| 3 | Abertura: a data continua sem fonte | |
| 14 | Prompt é briefing: um briefing de três linhas; os seis elementos como checklist | reescrita no celular com objetivo, contexto mínimo e a regra de não inventar (4 min) |
| 15 | Do chat ao agente: contexto como mesa; onde o chat dá trabalho; o que é agente; Work contra Code; cuidados antes de abrir a pasta (quadro único de sigilo) | |
| 25 | Demonstração: três arquivos fictícios (contrato, aditivo, notificação); cronologia com a fonte de cada data e minuta curta salva na pasta; skill e memória prontas; uma ferramenta ao vivo, a outra gravada lado a lado; vídeo de reserva | |
| 22 | Mão na massa: PDF único enviado antes com link e QR Code | na pasta, pelo Codex (gratuito) ou Claude Code (Pro); chat com upload como reserva |
| 4 | Fecho: cada um registra uma resposta, a fonte exata e uma verificação humana pendente; o que vem no segundo dia | |
| 7 | folga | |

# Roteiro slide a slide

Fio do dia: na Aula 1, sem o contrato, a IA admite que não sabe a data ou arrisca uma; na Aula 2, a pasta do caso
mostra a data com a fonte (contrato fictício de 12/03/2019).

## Aula 1. O que é IA e qual usar (26 slides)

| # | manchete | o que a tela mostra | clima | arquétipo | mídia |
|---|---|---|---|---|---|
| 1 | O que é IA e qual usar | abertura | noite, respiro | abertura | foto heroica já existente |
| 2 | Seu maior receio com a IA | sigilo, erro, tempo, não sei usar; a sala levanta a mão | claro, respiro | respiro | |
| 3 | Pergunte a data sem dar o contrato | o pedido ao lado do lugar vazio do contrato; o professor pergunta ao vivo e a turma vê se a IA admite ou arrisca | claro, leve | objetos | recortes de documentos |
| 4 | De regras escritas a dados | linha do tempo: 1956, aprendizado por dados, 2017, 2022, hoje | claro, médio | tempo | |
| 5 | Uma tarefa só, ou qualquer tarefa | a trilha se divide: filtro de spam e radar de um lado; ChatGPT, Claude e Gemini do outro | claro, médio | ramos | |
| 6 | A IA escreve uma palavra por vez | leque de palavras candidatas com probabilidades (ilustrativas) | claro, leve | escolha | |
| 7 | Probabilidade, não consulta | frase única | noite, respiro | respiro | |
| 8 | Sem o contrato, a data é inventada | leque raso de datas e sorteio de uma data plausível | noite, leve | escolha | |
| 9 | A janela de contexto é a mesa | papéis voam para a mesa; o que não cabe fica de fora | claro, médio | viagem | foto de mesa gerada |
| 10 | Ela erra com a mesma convicção | frase única | noite, respiro | respiro | |
| 11 | A fronteira da IA é irregular | fácil para nós e difícil para ela, e o contrário | claro, médio | comparacao | |
| 12 | Três trechos, cada um com sua fonte | instrução da prática em duplas, com os três trechos | claro, leve | objetos | casos anonimizados do professor |
| 13 | Onde estava o erro | fios ligam cada trecho à fonte: um sem fonte, um contradito, um certo | claro, médio | fios | |
| 14 | Quem assina continua respondendo | frase única | noite, respiro | respiro | |
| 15 | Qual é a melhor IA? | abertura do bloco | noite, respiro | abertura | foto heroica nova |
| 16 | Duas formas de medir uma IA | a trilha se divide: prova com gabarito e votação de pessoas | claro, médio | ramos | |
| 17 | Benchmark, a mesma prova com gabarito | uma caneta corrige uma prova (nota ilustrativa) | claro, respiro | numero | |
| 18 | Vote antes de saber qual é qual | respostas A e B sem nome sobre o caso fictício; a sala vota | claro, leve | comparacao | duas respostas preparadas |
| 19 | Na arena, milhões votam às cegas | número real de votos da LMArena, com data | claro, respiro | numero | [CONFERIR] |
| 20 | Demos a prova da PGE às IAs | frase única | noite, respiro | respiro | |
| 21 | 14 questões, 180 pontos | 12 curtas de 10, parecer de 30, peça de 30 | claro, leve | numero | |
| 22 | Onze IAs fizeram a prova da PGE | as onze barras crescem; os três primeiros quase empatam; o modelo local destacado (S.T.A.R.) | noite, médio | cena própria | gráfico redesenhado |
| 23 | O que essa nota não prova | o que mede e o que não mede: sem respostas por questão, juízes Gemma, prova de 2021, prova não é trabalho | claro, médio | comparacao | |
| 24 | 68,7% sem sair do computador | o Gemma 4 31B rodando no computador do usuário | claro, respiro | numero | |
| 25 | Onde fica o dado do cliente | modelos fechados e abertos; servidor de quem vende e servidor próprio | claro, médio | ramos | [CONFERIR] lista de out/2026 |
| 26 | Escolha por tarefa e teste você | fecho, com a ponte: a data continua sem fonte | noite, leve | fecho | |

## Aula 2. Do chat à pasta (24 slides, mais dois zooms no vídeo)

| # | manchete | o que a tela mostra | clima | arquétipo | mídia |
|---|---|---|---|---|---|
| 1 | Do chat à pasta | abertura com foto de pasta kraft | noite, respiro | abertura | foto já existente |
| 2 | A data ainda não tem fonte | retoma o fio da Aula 1 | noite, respiro | respiro | |
| 3 | Prompt é briefing para colega novo | "Resume esse acórdão" ao lado de um briefing de três linhas | claro, médio | comparacao | |
| 4 | Seis itens antes de enviar | objetivo, contexto, persona, formato, exemplos, regras, como checklist | claro, médio | objetos | |
| 5 | Reescreva em três linhas | objetivo, contexto mínimo, não invente; quatro minutos | noite, respiro | respiro | |
| 6 | Duas versões, duas respostas | o professor projeta duas versões de alunos e as respostas | claro, leve | comparacao | ao vivo |
| 7 | Contexto é o material do pedido | o pedido ao lado dos papéis | claro, médio | objetos | recortes |
| 8 | O chat esquece quando fecha | frase única; na fala, subir arquivos toda vez e receber texto em vez de arquivo | noite, respiro | respiro | |
| 9 | O agente planeja, você aprova | pedido, plano, aprovação (dourado), ação, entrega | claro, médio | tempo | |
| 10 | Work entrega; Code trabalha no caso | a trilha se divide: Work (nuvem, suba os arquivos, receba pronto) e Code (pasta sua, skill e memória em arquivo), com os nomes nas duas empresas | noite, médio | ramos | |
| 11 | O arquivo fica, o conteúdo viaja | o que fica com você (arquivos, organização, skill, memória) e o que vai ao modelo (o que o agente lê) | claro, médio | comparacao | |
| 12 | Antes de abrir a pasta | só fictício hoje, só a subpasta do caso, revise toda edição | noite, respiro | respiro | |
| 13 | Três papéis na pasta do caso | contrato, aditivo e notificação voam para a árvore da pasta | claro, médio | viagem | recortes gerados |
| 14 | A skill guarda o jeito de fazer | o pedido vira o arquivo SKILL.md | claro, médio | cena própria | |
| 15 | A memória é um arquivo legível | trecho do arquivo de memória: "prazos em dias úteis, cite folha e trecho" | claro, leve | objetos | |
| 16 | Agora, funcionando | frase única; o professor troca para o app | noite, respiro | respiro | |
| 17 | Funcionando, ao vivo no Claude | moldura com vídeo de reserva e dois zooms (a cronologia; a minuta salva na pasta) | noite, leve | demonstracao | vídeo feito por código |
| 18 | Cada data aponta para o seu papel | fios da cronologia aos três papéis; a data da Aula 1 acende quando o fio do contrato chega (S.T.A.R.) | noite, médio | fios | |
| 19 | O mesmo pedido no Codex | Claude e Codex lado a lado, "gravado em [data]" | claro, médio | comparacao | gravação de tela do professor |
| 20 | Agora na sua pasta | o PDF enviado antes, QR Code e o pedido: cronologia com arquivo e trecho; se não achar, diga | claro, médio | objetos | |
| 21 | Pasta de graça, ou chat de reserva | dois caminhos: Codex grátis ou Claude Pro na pasta; chat com upload para quem travar | claro, leve | ramos | |
| 22 | Quem achou as três datas? | conversa com a sala | noite, respiro | respiro | |
| 23 | Resposta, fonte e o que conferir | cada um registra três linhas | claro, leve | tempo | |
| 24 | Trabalhe no caso, não no chat | fecho e anúncio do dia 2 numa linha | noite, leve | fecho | |
</ALVO>

## Pareceres

## Revisor A, rodada 1

1 · Aula 1, slides 3 e 8 · crítica · O slide 3 promete uma pergunta ao vivo para ver se a IA "admite ou arrisca", mas o slide 8 pressupõe que ela sempre inventa ("Sem o contrato, a data é inventada"). Em outubro de 2026, modelos de fronteira frequentemente recusam responder sem o documento, o que quebraria o arco dramático da aula ao vivo. · Na Aula 1, slide 3, mude o que a tela mostra para: `pedido induzindo erro ("Qual a data da cláusula 4ª do contrato padrão?") ou print real preparado` e a manchete do slide 8 para: `Sem o contrato, a IA pode chutar` · alta

2 · Aula 1, slides 1, 2, 15, 21 e Aula 2, slides 1, 5, 12, 16, 20 · crítica · Dez manchetes não são afirmações completas (são títulos vagos, perguntas ou comandos), violando a Regra 1 ("a manchete afirma essa coisa"). Uma tela que diz apenas "O que é IA e qual usar" ou "Agora, funcionando" desperdiça o espaço nobre de retenção da turma. · Reescreva as manchetes: Aula 1, #1 `A IA escreve por probabilidade`; #2 `O medo de errar trava o uso`; #15 `A melhor IA depende da tarefa`; #21 `A prova tem 14 questões e 180 pontos`. Aula 2, #1 `O trabalho real acontece na pasta`; #5 `Três linhas bastam para o briefing`; #12 `O sigilo exige três cuidados simples`; #16 `O agente lê a pasta e entrega a minuta`; #20 `Sua pasta já tem os três arquivos` · alta

3 · Aula 1, slide 12 · crítica · O arquétipo `objetos` exige limite de densidade (até 24 palavras no modo `leve`), mas a tela tenta mostrar a instrução da prática mais três trechos jurídicos e suas fontes. Ninguém na sala conseguirá ler três casos projetados na parede para fazer o exercício em duplas. · Na Aula 1, slide 12, mude "o que a tela mostra" para: `Na tela, apenas o comando de 3 linhas e QR Code; os 3 trechos vão em folha impressa ou link no WhatsApp` · alta

4 · Aula 2, slide 10 · crítica · O slide contrapõe "Work" e "Code" nas duas empresas, mas nos fatos de apoio de 22/10/2026 o Cowork do Claude já se fundiu à conversa comum em 16/09/2026 (rodando na nuvem nos planos Pro/Max), enquanto "Work" é marca apenas do ChatGPT. Ensinar taxonomia defasada ou misturada confunde quem for abrir o aplicativo na hora. · Na Aula 2, slide 10, mude a manchete para `Agente na nuvem ou agente na pasta` e o texto da tela para: `Nuvem (ChatGPT Work e conversa no Claude Pro/Max) vs. Pasta local (ChatGPT Codex gratuito e Claude Code pago)` · alta

5 · Aula 2, slides 13, 20 e 21 · crítica · O contexto diz que a turma recebeu antes "um PDF com três documentos fictícios" (também citado no slide 20 como "o PDF único"), mas o slide 13 mostra três arquivos separados voando para a pasta, e o exercício no Codex/Code exige pasta no computador. Alunos de celular ou com um PDF único não conseguirão reproduzir a árvore de três arquivos da demonstração. · Na Aula 2, slide 20, forneça no link/QR Code duas opções explícitas na tela: `1. Pasta .zip com 3 arquivos (para quem está no notebook com Codex/Code); 2. PDF único (para quem está no celular ou no chat)` · alta

6 · Aula 1, slides 3 a 6 · importante · Há quatro slides consecutivos com o clima `claro` (slides 3, 4, 5 e 6) e o bloco de abertura (slides 1 a 10) soma 10 slides para apenas 20 minutos no mapa (média de 2 min/slide, incluindo enquete e teste ao vivo). A história da IA desde 1956 (slide 4) e filtro de spam (slide 5) tomam tempo precioso de um público jurídico que precisa entender janela de contexto e alucinação. · Elimine os slides 4 e 5 da Aula 1, fundindo a ideia de "regras vs. probabilidade" na fala do slide 6; isso reduz a Aula 1 para 24 slides e elimina a sequência de quatro telas claras seguidas · alta

7 · Aula 1, slide 25 · importante · A manchete diz `Onde fica o dado do cliente`, expressão de escritório privado que exclui a desembargadora, o procurador e os servidores públicos da turma (Critério 6). No setor público e no Judiciário, fala-se em dado do processo, da parte ou da instituição. · Na Aula 1, slide 25, substitua a manchete por: `Onde fica o dado do processo` (28 caracteres, 6 palavras) · alta

8 · Aula 2, slides 5 e 6 · importante · O slide 5 pede que os alunos reescrevam um prompt no celular em 4 minutos, e o slide 6 prevê que o professor projete ao vivo duas versões de alunos e gere as respostas. Coletar textos de celulares da turma e projetar na tela do computador do professor consome facilmente 10 minutos de logística e quebra o ritmo do bloco de 14 minutos. · Na Aula 2, slide 6, mude a mídia para `semi-ao vivo` e a ação para: `Dois alunos leem suas 3 linhas em voz alta (sem projetar o celular); o professor digita apenas uma delas ao vivo e compara com o prompt fraco do slide 3` · alta

9 · Aula 2, slides 17 a 19 · importante · Os slides 16, 17 e 18 têm todos o clima `noite` (respiro, leve, médio), criando um túnel escuro antes do S.T.A.R. no slide 18, além de dar protagonismo ao vivo apenas ao Claude Code (pago) no slide 17 e deixar o Codex (a única opção gratuita na pasta para a turma) como vídeo gravado secundário no slide 19. Isso fere a neutralidade entre ferramentas (Critério 4) e desanima quem não paga US$ 20/mês. · Na Aula 2, slide 17, mude a manchete para `Na pasta, o agente cria a minuta` (demonstrando o Codex gratuito ao vivo ou dividindo a tela igualmente com o Claude Code); no slide 19, mude a manchete para `As duas ferramentas entregam na pasta` · alta

10 · Aula 2, slides 14 e 15 · importante · Apresentar `SKILL.md` e arquivos de memória antes de a turma ver o agente funcionando na pasta (que só ocorre no slide 17) é abstrato demais para profissionais do direito sem formação técnica. Eles ainda não viram o agente ler um contrato e já estão vendo configuração de arquivo markdown. · Inverta a ordem na Aula 2: coloque os atuais slides 14 e 15 (`SKILL.md` e memória) logo após o slide 19, como explicação de "como padronizar o que vocês acabaram de ver", ou simplifique o slide 14 para mostrar apenas uma instrução em texto comum dentro da pasta · média

11 · Aula 1, slides 22 e 24 · opcional · O slide 22 já destaca o modelo local como momento S.T.A.R. no gráfico das onze IAs, tornando o slide 24 (`68,7% sem sair do computador`) repetitivo (Critério 3: nenhum slide que só repete o anterior). · Na Aula 1, tire o destaque do modelo local do slide 22 (deixe o S.T.A.R. focado no empate técnico do topo entre Opus 5.5 com 91,7% e Gemini 4 Argon com 90,9% contra o custo/abertura) ou elimine o slide 24, incorporando os 68,7% do Gemma 4 31B diretamente como a surpresa final do slide 22 · média

12 · Aula 1, slide 17 · opcional · A manchete `Benchmark, a mesma prova com gabarito` tem 37 caracteres (no limite da regra) e é uma definição nominal, sem verbo. · Na Aula 1, slide 17, mude a manchete para: `O benchmark aplica a mesma prova` (32 caracteres, 6 palavras) · alta

## Revisor A, rodada 2

1 · Aula 1, slides 3 e 8 · crítica · O slide 8 pressupõe que a IA inventará a data no teste ao vivo do slide 3, quando ela pode admitir que não sabe. · **MANTENHO** a proposta do Revisor B: trocar a manchete do 8 por `"Sem fonte, a data não se sustenta"` (33 caracteres, 6 palavras) e mostrar recusa ou palpite como desfechos possíveis. · confiança alta

2 · Aula 1, slides 4 e 5 · importante · Duas telas seguidas (`claro, médio`) atrasam o retorno ao teste da data e trazem marcos sem fonte. · **REFINO**: fundir num único slide `claro, leve` (arquétipo `ramos`) com a manchete `"De regras fixas a padrões de dados"` (34 caracteres, 7 palavras); levar as datas históricas para a fala ou marcar `[CONFERIR]`. · confiança alta

3 · Aula 1, slides 12 e 13 · crítica · A manchete do 12 promete fonte para os três trechos, contradizendo o 13 (“um sem fonte”) e entregando a resposta antes da prática. · **REFINO**: no slide 12, manchete `"Três afirmações para conferir na fonte"` (38 caracteres, 6 palavras), entregando os documentos-base para as duplas classificarem em *sustentada, contradita ou sem amparo*; revelar os fios no 13. · confiança alta

4 · Aula 1, slide 14 · importante · “Quem assina” exclui servidores e assessores que elaboram minutas mas não subscrevem a peça. · **MANTENHO** a proposta do Revisor B: manchete `"A verificação continua humana"` (29 caracteres, 4 palavras). · confiança alta

5 · Aula 1, slides 14 e 15 · crítica · Os slides 14 e 15 violam a regra de ritmo ao repetir o mesmo clima e densidade (`noite, respiro`) em sequência. · **REFINO**: retirar o slide 15 e abrir o bloco no slide 16 com a manchete afirmando `"A melhor IA depende da tarefa"` (29 caracteres, 6 palavras), pois as regras do motor exigem que a manchete afirme, não pergunte. · confiança alta

6 · Aula 1, slides 16 e 17 · crítica · “Prova com gabarito” contradiz o método real (prova discursiva corrigida por dois modelos Gemma 4 locais). · **MANTENHO** a proposta do Revisor B: usar a manchete `"Dois modelos corrigiram a prova"` (31 caracteres, 5 palavras) já na apresentação do benchmark. · confiança alta

7 · Aula 1, slide 19 · importante · Depende de cifra com `[CONFERIR]` e tira o foco do teste cego da sala no slide 18. · **MANTENHO** a proposta do Revisor B: se o número oficial não for confirmado até o fechamento, usar `"Na arena, pessoas votam às cegas"` (32 caracteres, 6 palavras) e mudar o arquétipo de `numero` para `comparacao` ou `respiro`. · confiança alta

8 · Aula 1, slides 20–23 · crítica · O gráfico S.T.A.R. no slide 22 pode ser lido como ranking absoluto antes da tela de limites no 23. · **MANTENHO** a proposta do Revisor B: titular o 22 como `"Nesta prova, as notas ficaram próximas"` (38 caracteres, 6 palavras), incluir aviso no rodapé do gráfico e manter os quatro limites explícitos no 23. · confiança alta

9 · Aula 1, slide 24 · crítica · Promete execução no computador do aluno sem ressalvar o hardware exigido por um modelo de 31B parâmetros. · **MANTENHO** a proposta do Revisor B: manchete `"Modelo local: 68,7% nesta prova"` (31 caracteres, 5 palavras). · confiança alta

10 · Aula 1, slide 25 · crítica · Confunde pesos abertos/fechados com local de processamento (nuvem de terceiros vs. infraestrutura própria) e traz `[CONFERIR]`. · **REFINO**: separar os dois eixos no diagrama (`ramos`) e usar manchete afirmativa: `"Licença aberta não garante sigilo"` (33 caracteres, 5 palavras). · confiança alta

11 · Aula 2, slides 1–5 · importante · Os slides 1 e 2 repetem `noite, respiro` em sequência, e o checklist de seis itens no 4 confunde a prática de três linhas no 5. · **REFINO**: fundir 1 e 2 na abertura (`"Do chat à pasta: falta a fonte"`, 30 caracteres, 7 palavras) e aplicar no slide 5 o molde copiável proposto pelo Revisor B (`Objetivo: __. Contexto disponível: __. Regra: não invente; indique o que falta.`). · confiança alta

12 · Aula 2, slide 6 · importante · Projetar respostas de alunos ao vivo gera atraso e risco de exposição. · **MANTENHO** a proposta do Revisor B: ter duas respostas fictícias de reserva prontas no slide. · confiança alta

13 · Aula 2, slides 8–10 · crítica · Ignora que o Cowork se fundiu ao chat comum do Claude (16/09/2026) rodando na nuvem em Pro/Max (06/10/2026), enquanto no ChatGPT há Work e Codex. · **REFINO**: no slide 8, usar `"No chat, você sobe tudo de novo"` (31 caracteres, 7 palavras); no 10, separar o fluxo de *agente em nuvem* (Claude / ChatGPT Work) do *agente na pasta local* (Claude Code Pro / ChatGPT Codex). · confiança alta

14 · Aula 2, slides 9, 11 e 12 · crítica · “Você aprova” e “o conteúdo viaja” escondem que os trechos lidos na pasta local são enviados à API na nuvem. · **MANTENHO** a proposta do Revisor B: explicitar na linha do tempo do 9 `"Peça plano → confira acessos e trechos enviados → autorize ações → revise arquivos alterados"`. · confiança alta

15 · Aula 2, slides 14 e 15 · importante · “Prazos em dias úteis” aplica regra de direito processual a um caso administrativo/contratual sem conferência, e `SKILL.md` precisa soar agnóstico. · **MANTENHO** a proposta do Revisor B: trocar o exemplo de memória por `"Identifique a regra de contagem aplicável; cite arquivo e trecho; sinalize dúvidas."` · confiança alta

16 · Aula 2, slides 17–19 · importante · Os slides 16, 17 e 18 têm três climas `noite` seguidos, e os zooms do 17 não preparam o S.T.A.R. do 18. · **REFINO**: mudar o slide 17 para `claro, leve` e aplicar a proposta do Revisor B para os dois zooms (focar na *data de 12/03/2019 no contrato* e na *data na cronologia*). · confiança alta

17 · Aula 2, slides 20–23 · crítica · O pré-envio é um PDF único, mas a demonstração usa três arquivos na pasta; além disso, o Codex gratuito exige app desktop e parte da turma estará no celular. · **MANTENHO** a proposta do Revisor B: exibir três rotas claras no slide 21 (*desktop com Codex gratuito; desktop com Claude Code Pro; celular ou reserva via chat com upload do PDF único*), exigindo a mesma entrega no slide 23. · confiança alta

## Revisor B, rodada 1

1 · Aula 1, slides 3 e 8 · crítica · O teste ao vivo pode terminar com a IA admitindo que não sabe; o slide 8 afirma antecipadamente que ela inventou. · Trocar a manchete por **“Sem fonte, a data não se sustenta”** e mostrar dois desfechos possíveis: recusa ou palpite. · confiança alta

2 · Aula 1, slides 4 e 5 · importante · Duas telas de classificação atrasam a resposta à pergunta aberta no slide 3. As datas da linha do tempo também entram sem fontes indicadas. · Fundir os slides: “IA pode aprender padrões dos dados”; manter apenas marcos com fonte na tela e levar o restante à fala. · confiança alta

3 · Aula 1, slides 12 e 13 · crítica · “Cada um com sua fonte” contradiz a revelação de “um sem fonte”; além disso, ver a fonte antes pode esvaziar o exercício. · No slide 12, projetar três afirmações e entregar os documentos de conferência; pedir que cada dupla classifique **sustentada, contradita ou não localizada**. Revelar os fios no 13. · confiança alta

4 · Aula 1, slide 14 · importante · “Quem assina” não representa igualmente assessores e servidores e reduz a verificação a quem subscreve o documento. · Usar **“A verificação continua humana”** e perguntar, na fala, quem confere antes de cada entrega. · confiança alta

5 · Aula 1, slides 14 e 15 · opcional · São duas pausas noturnas consecutivas, e a segunda reabre a aula como se começasse outra apresentação. · Retirar o slide 15; abrir o bloco com a pergunta “Melhor para qual tarefa?” no slide 16. · confiança alta

6 · Aula 1, slides 16 e 17 · crítica · “Prova com gabarito” não descreve o método informado: respostas discursivas corrigidas por dois modelos Gemma 4 locais, não por uma banca ou gabarito objetivo. · Trocar por **“Dois modelos corrigiram a prova”**; nomear o método já na primeira tela que apresenta o benchmark. · confiança alta

7 · Aula 1, slide 19 · importante · “Milhões votam” depende de número e data ainda marcados para conferência e desloca a atenção do teste cego feito pela sala. · Retirar a cifra se não houver fonte verificável na versão final; usar **“Na arena, pessoas votam às cegas”**. · confiança alta

8 · Aula 1, slides 20–23 · crítica · O gráfico é o momento memorável, mas pode ser lido como ranking de desempenho profissional antes que seus limites apareçam. · No slide 22, titular **“Nesta prova, as notas ficaram próximas”** e manter no rodapé “correção por modelos; não mede trabalho jurídico”. No 23, explicitar também que a prova de 2021 pode ter integrado o treino. · confiança alta

9 · Aula 1, slide 24 · crítica · “68,7% sem sair do computador” mistura o resultado do Gemma local no benchmark com uma promessa sobre o computador de cada participante. · Trocar por **“Modelo local: 68,7% nesta prova”**; na fala, distinguir execução local do teste e viabilidade no equipamento da turma. · confiança alta

10 · Aula 1, slide 25 · crítica · A oposição “modelo fechado = servidor de quem vende; aberto = servidor próprio” confunde licença do modelo com local de processamento. · Desenhar dois eixos independentes: **“Qual modelo?”** e **“Onde os dados são processados?”**; fechar com “verifique a configuração antes de usar dados do caso”. · confiança alta

11 · Aula 2, slides 3–5 · importante · O checklist de seis itens pode parecer obrigatório, enquanto a prática pede só três; a turma precisa saber o que efetivamente escrever em quatro minutos. · No slide 5, exibir o molde copiável: **“Objetivo: __. Contexto disponível: __. Regra: não invente; indique o que falta.”** Tratar os seis itens como opções de melhoria. · confiança alta

12 · Aula 2, slide 6 · importante · Projetar duas respostas de alunos ao vivo introduz espera e risco de expor conteúdo que não foi combinado. · Deixar duas versões fictícias preparadas como reserva; só usar contribuições da sala com consentimento e após conferir o que será projetado. · confiança alta

13 · Aula 2, slides 8–10 · crítica · “O chat esquece quando fecha” é absoluto, e “Work contra Code” apresenta produtos e fluxos distintos como equivalentes entre empresas. · Usar **“No chat, você pode refazer a organização”**; no slide 10, mostrar tarefas concretas — receber uma entrega e trabalhar em arquivos da pasta — com os nomes e requisitos de cada ferramenta separados. · confiança alta

14 · Aula 2, slides 9, 11 e 12 · crítica · “Você aprova” pode soar como garantia automática, enquanto “o conteúdo viaja” fica abstrato justamente no ponto de sigilo. · Substituir o fluxo por **“Peça plano → confira acessos e trechos enviados → autorize ações → revise arquivos alterados”**. Na demonstração, usar apenas o caso fictício e mostrar a subpasta selecionada. · confiança alta

15 · Aula 2, slides 14 e 15 · importante · SKILL.md e “memória” aparecem como arquivos prontos sem deixar claro se o mesmo preparo funciona nas duas demonstrações. “Prazos em dias úteis” ainda embute uma regra não conferida. · Mostrar o conteúdo como instrução reaproveitável, adaptada a cada ferramenta; trocar o trecho por **“Identifique a regra de contagem aplicável; cite arquivo e trecho; sinalize dúvidas.”** · confiança alta

16 · Aula 2, slides 17–19 · importante · O momento da fonte corre o risco de passar durante a troca entre app, vídeo e comparação gravada. · Reservar os dois zooms do slide 17 para **data no documento** e **data na cronologia**; pausar antes do fio do slide 18 e pedir que a sala aponte o trecho que o sustenta. · confiança alta

17 · Aula 2, slides 20–23 · crítica · O exercício promete trabalho “na pasta”, mas o pré-envio descrito é um PDF único, muitos estarão no celular, e o acesso gratuito ao Codex informado no contexto é pelo app desktop. · Dar três rotas na tela: **desktop com Codex; desktop com Claude Code (Pro); celular ou bloqueio técnico com chat e upload**. Explicar como obter os três documentos a partir do PDF [confirmar] e pedir a mesma entrega mínima em qualquer rota: data, arquivo/trecho e pendência de conferência. · confiança alta

## Revisor B, rodada 2

1 · **REFINO** · Aula 1, slides 3 e 8: o teste ao vivo pode produzir uma recusa correta; não se deve induzir o erro para salvar a narrativa. Manchete do #8: `Sem fonte, a data pode ser chute`. Levar um erro real anonimizado como alternativa preparada.

2 · **REFINO** · Aula 1, slides 1, 2, 15 e 21; Aula 2, slides 1, 5, 12, 16 e 20: mantenho a exigência de manchetes afirmativas, mas `Sua pasta já tem os três arquivos` contradiz o PDF único enviado à turma. No #20, usar `O material do caso está no link`; nos demais, aplicar as reescritas propostas.

3 · **MANTENHO** · Aula 1, slide 12: três trechos jurídicos, fontes e instruções não serão legíveis como exercício projetado. Tela só com tarefa e acesso; trechos no material distribuído.

4 · **REFINO** · Aula 2, slide 10: a oposição útil é entre fluxo na conversa/nuvem e trabalho na pasta, não entre marcas supostamente equivalentes. Manchete: `Conversa e pasta mudam o trabalho`. Tela: `ChatGPT Work / conversa no Claude | Codex / Claude Code na pasta`; indicar que trabalhar na pasta **não** significa processamento offline.

5 · **REFINO** · Aula 2, slides 13, 20 e 21: oferecer `.zip` com três arquivos e PDF único resolve a inconsistência, mas a instrução precisa distinguir dispositivos. Texto do #20: `Notebook: extraia o .zip e abra a pasta. Celular: abra o PDF no chat. Em ambos: peça datas com arquivo e trecho; sem fonte, diga que não achou.`

6 · **REFINO** · Aula 1, slides 3 a 6: quatro telas claras não violam a regra, pois a densidade muda. Ainda assim, #4 exige fonte para os marcos e #5 pouco prepara o teste da data. Cortar #4; integrar a distinção entre tarefas específicas e gerais à fala do #6, sem prolongar o bloco.

7 · **REFINO** · Aula 1, slide 25: `cliente` exclui parte da turma; `processo` ainda estreita o exemplo. Manchete: `Onde fica o dado do caso`.

8 · **REFINO** · Aula 2, slides 5 e 6: projetar respostas recebidas dos celulares é logística demais para 14 minutos. Dois voluntários leem seus briefings; o professor compara **uma versão preparada** com o pedido fraco do #3. Não depender de digitação ou geração ao vivo.

9 · **REFINO** · Aula 2, slides 17 a 19: três telas noturnas com densidades diferentes não infringem a regra. A assimetria de acesso, sim, importa: demonstrar **Codex gratuito ao vivo**, com vídeo de reserva; mostrar Claude Code em gravação equivalente, sem chamar uma ferramenta de principal.

10 · **REFINO** · Aula 2, slides 14 e 15: skill e memória antes da entrega tornam a demonstração abstrata. Adiar ambos para depois do #19 **apertaria a prática**; melhor mostrar uma instrução legível na pasta, sem ensinar `SKILL.md` ou memória nesta aula.

11 · **REFINO** · Aula 1, slides 22 e 24: retirar o #24 e fazer do modelo local a revelação final do gráfico no #22. Não chamar a diferença no topo de “empate técnico”: o roteiro não apresenta método que sustente essa conclusão.

12 · **MANTENHO** · Aula 1, slide 17: `O benchmark aplica a mesma prova` é mais curto e afirma a ideia que a tela precisa demonstrar.
