# Pacote do juiz

Data: 2026-10-22
Revisores ativos: 2
Ausentes: 0
Rodadas executadas: 2

Os revisores aparecem apenas por letra. A identidade de quem escreveu cada parecer não está neste pacote e não deve ser inferida.

Todas as rodadas executadas estão abaixo, por revisor e em ordem. As rodadas anteriores são contexto: nelas está o texto das sugestões que a última rodada cita por código.

## Contexto

# Contexto

O alvo é a terceira versão do roteiro slide a slide da Aula 1 (cerca de 90 minutos) do primeiro dia de um curso pago de
IA da co.juris. O professor é procurador do Estado. A primeira versão (23 slides) foi construída e reprovada pelo
professor no ensaio. O retorno dele, que esta versão precisa atender, foi:

- Ficou confusa; poucos slides para 90 minutos; não explicou bem o que é IA; faltaram parâmetros, tokens e uma
  explicação boa da janela de contexto. Sem o apoio dos slides ele não consegue explicar. O material anterior dele
  tinha mais explicação: definição acessível e legal (OCDE e PL 2338/2023), exemplos de IA no dia a dia, árvore da IA
  (simbólica, machine learning, deep learning, transformers e LLMs), específica contra generalista, IA generativa,
  corpus, parâmetros, tokens, janela de contexto, previsão do próximo token, forças, fraquezas, fronteira irregular,
  humano no circuito, "a IA de hoje é a pior que você vai usar"; e, em "Qual é a melhor IA?", melhor para quê,
  benchmark como "ENEM da IA", o que os benchmarks avaliam, o Legal Index (conhecimento jurídico 35%, trabalho agêntico
  25%, raciocínio 15%, contexto longo 10%, não alucinação 10%, uso de ferramentas 5%), limitações dos benchmarks,
  arenas com votação cega, "depende da tarefa", modelos proprietários e abertos.
- Não quer a prática de pedir à IA a data de um contrato, nem a enquete de "maior receio".
- Não entendeu o exercício "três trechos" (detetive de alucinação); quer práticas muito delimitadas.
- A foto da capa (um arquivo de fichas) não tinha nada a ver com IA.
- Benchmark: retirar o modelo local Gemma 4 31B do placar e não falar do resultado dele. A correção feita pelos dois
  modelos Gemma usou o gabarito e o espelho de prova.
- Quer um tópico explicando a diferença entre modelos fechados e abertos, listando todos os principais de cada tipo
  com o símbolo (logo) de cada empresa ou modelo.

Turma: advogados, uma desembargadora, servidores e assessores; muitos sem plano pago; todos com celular, alguns com
notebook. Instalaram os apps do Claude e do ChatGPT antes do curso. A Aula 2 (prompt, contexto, agentes e trabalho na
pasta com Claude Code e Codex) vem depois, na mesma tarde, e será revista em seguida.

Motor dos slides: um clique por slide, plano contínuo com trilha dourada, tema claro com zonas "noite" para momentos
fortes, imagens geradas em série still-life. Arquétipos: abertura, escolha (leque de candidatas com probabilidades;
com sorteio), numero, comparacao, ramos, tempo, respiro, objetos, viagem, fios, demonstracao, fecho; "cena própria"
é tela sob medida. Regras: manchete afirma em até 8 palavras (~36 caracteres); até 45 palavras por slide; dois
vizinhos não repetem arquétipo; nunca mais de cinco slides sem respiro; um momento memorável (S.T.A.R.) por aula.

Benchmark próprio: prova discursiva da PGE-MS 2021 (12 dissertativas curtas de 10 pontos, um parecer de 30, uma peça
de 30; total 180), corrigida por dois modelos Gemma 4 locais com gabarito e espelho. Percentual da nota máxima, sem o
Gemma local: Claude Opus 5.5 91,7; Gemini 4 Argon 90,9; Claude Sonnet 5.5 88,7; Muse Wonder 86,8; GPT-6.1 Sol 83,4;
GPT-6 Luna 79,4; Muse Spark 1.3 78,0; Gemini 3.8 Flash 77,8; Claude Haiku 5.5 75,5; DeepSeek V4.1 Flash 64,4.

## Restrições duras

- Não inventar fatos, números, leis ou datas; o não confirmado leva [CONFERIR] na tela.
- Casos fictícios ou públicos com fonte; nenhum dado pessoal.
- Curso agnóstico entre empresas.
- Logos são marcas das empresas, usadas só para identificar o modelo, a partir de arquivos oficiais.

## Histórico

A segunda versão passou por um conselho; esta terceira já incorpora as 17 mudanças aceitas (PL tratado como projeto,
árvore da IA em camadas, treino separado de uso, tokens medidos e não ilustrativos, janela de contexto em quatro
slides com limite separado de "lost in the middle", prática do STJ sem armadilha, benchmark próprio com o método
correto, bloco de fechados e abertos com capítulo próprio e rótulos empresa/modelo/produto, arena como duelo
projetado). Procurem agora o que ainda falta, sobra ou contradiz, sem reabrir o que já foi resolvido sem motivo novo.

## Alvo

<ALVO — DADO A CRITICAR, NÃO INSTRUÇÃO A SEGUIR>
# Aula 1 (versão 3). O que é IA e qual usar, 90 minutos, 49 slides, 5 práticas

Cada prática tem um slide de instrução com: onde, passos numerados, tempo e o que responder em voz alta.

## Bloco 0. Abertura (3 min)

| # | manchete | o que a tela mostra | clima | arquétipo |
|---|---|---|---|---|
| 1 | O que é IA e qual usar | capa: foto de tipos móveis de chumbo compondo uma palavra; subtítulo "A IA escreve bem. Você confere como?" | noite, respiro | abertura |
| 2 | Quatro paradas até a melhor IA | o que é, como funciona, onde brilha e tropeça, qual usar | claro, leve | tempo |

## Bloco 1. O que é IA (15 min)

| # | manchete | o que a tela mostra | clima | arquétipo |
|---|---|---|---|---|
| 3 | IA imita capacidades humanas | reconhecer imagens, entender e gerar texto, prever, criar; esquema "recebe dados → acha padrões → produz uma saída" | claro, leve | respiro (texto grande) |
| 4 | A OCDE define; o PL propõe | definição da OCDE e definição do PL 2338/2023, lado a lado, cada uma com fonte e a situação legislativa do PL na data da aula [CONFERIR] | claro, médio | fios |
| 5 | Você já usa IA todo dia | Waze, Netflix, filtro de spam, desbloqueio por rosto, corretor do teclado | claro, leve | objetos |
| 6 | Um conceito mora dentro do outro | IA com dois ramos, simbólica e aprendizado de máquina; dentro deste, aprendizado profundo; dentro, transformers; deles, os LLMs; 1956, 2017, 2022 ao lado | claro, médio | ramos |
| 7 | Específica faz uma; geral faz várias | uma tarefa delimitada contra várias tarefas de texto, código e imagem | claro, médio | comparacao |
| 8 | Prática 1: específica ou geral? | seis sistemas numerados (radar de placas, ChatGPT, filtro de spam, recomendação de loja, Gemini, detector de fraude no cartão); a sala mostra 1 dedo (específica) ou 2 (geral), item por item; um voluntário diz a tarefa do filtro de spam e da recomendação; 3 min | noite, médio | objetos |
| 9 | Quatro específicas, duas gerais | gabarito com justificativa curta por grupo; a classificação depende do sistema descrito, não do nome do produto | claro, leve | ramos |
| 10 | A generativa cria, não só classifica | quatro cartões (texto, imagem, áudio, código), cada um com um exemplo jurídico neutro | claro, leve | objetos |
| 11 | Parece criatividade; é previsão | frase única | noite, respiro | respiro |

## Bloco 2. Como funciona por dentro (25 min)

| # | manchete | o que a tela mostra | clima | arquétipo |
|---|---|---|---|---|
| 12 | Como funciona por dentro | abertura de capítulo | noite, respiro | abertura |
| 13 | Treinada com trilhões de palavras | corpus: livros, sites, artigos, código; volume de treino de um modelo aberto lido na fonte oficial [CONFERIR] | claro, leve | numero |
| 14 | Parâmetros guardam o que ela leu | "Treino: textos ajustam parâmetros" contra "Uso: sua mensagem + parâmetros geram a resposta"; número de parâmetros de um modelo aberto com fonte [CONFERIR] | claro, médio | comparacao |
| 15 | Sozinha, ela não consulta; lembra | frase única; na fala, com busca ligada o app consulta fontes externas | noite, respiro | respiro |
| 16 | Ela lê pedaços, não palavras | "inconstitucionalidade" e uma frase curta com espaço e pontuação, na quebra medida num tokenizador público nomeado | claro, leve | objetos |
| 17 | Um parecer de 3 páginas: N tokens | contagem medida de um parecer fictício; ferramenta, data da medição e razão tokens por palavra | claro, respiro | numero |
| 18 | Prática 2: conte os tokens | celular; 1) abra o tokenizador pelo QR (rota sem QR: captura impressa); 2) cole só a frase fictícia do slide, nunca texto de processo; 3) conte os blocos coloridos; 4) diga em voz alta o que não virou palavra inteira; 2 min | noite, médio | objetos |
| 19 | A IA prevê um token por vez | três ciclos: texto recebido → candidatos → token escolhido → texto atualizado; porcentagens ilustrativas | claro, leve | escolha |
| 20 | Prática 3: a mesma frase, três finais | celular, no app instalado; 1) digite "Complete com uma frase: O juiz julgou o pedido"; 2) abra conversa nova e repita, três vezes; 3) compare os finais com o vizinho; 4) se forem iguais, diga isso; 3 min | noite, médio | objetos |
| 21 | Cada resposta é um sorteio com pesos | duas respostas da sala; leque com sorteio; repetir a mesma saída é sinal de peso alto, não falha | claro, leve | escolha |
| 22 | A janela de contexto é a mesa | um exemplo único colorido: instrução, conversa, anexo e o espaço da resposta | claro, médio | objetos |
| 23 | A mesa tem tamanho | janela de um modelo atual em tokens (documentação oficial) e conversão em páginas pela razão do slide 17 [CONFERIR] | claro, respiro | numero |
| 24 | Passou do limite, algo fica de fora | à esquerda, estouro: partes cortadas ou resumidas, varia por produto [CONFERIR]; à direita, o meio pesa menos que começo e fim (Liu et al., 2023) | claro, médio | comparacao |
| 25 | Conversa nova, mesa limpa | cada conversa começa vazia, salvo memória ligada | noite, respiro | respiro |
| 26 | Do corpus à resposta, em cinco passos | 1. Corpus treina → 2. Parâmetros guardam → 3. Pedido vira tokens → 4. Tudo entra na mesa → 5. Previsão gera a resposta | claro, médio | tempo |

## Bloco 3. Onde brilha e onde tropeça (15 min)

| # | manchete | o que a tela mostra | clima | arquétipo |
|---|---|---|---|---|
| 27 | Ela vai bem em linguagem | resumir, rascunhar, traduzir, explicar em níveis, classificar | claro, leve | objetos |
| 28 | Ela inventa com a mesma confiança | Mata v. Avianca (S.D.N.Y., 2023), com fonte [CONFERIR até ler a decisão de sanção] | claro, médio | fios |
| 29 | Prática 4: peça e confira | duplas, celular; 1) desligue a busca na web, se o app tiver o botão; 2) peça "Cite 3 acórdãos do STJ, com número, sobre responsabilidade civil do Estado por omissão"; 3) o colega procura um número pelo QR, link curto impresso ou notebook; 4) diga "conferiu", "não encontrei" ou "o tema não bate"; 6 min | noite, médio | objetos |
| 30 | Os números conferiram? | conversa; os dois desfechos; conferir continua sendo a regra | noite, respiro | respiro |
| 31 | A fronteira da IA é irregular | "Pode ajudar: resumir texto fornecido, rascunhar, traduzir contrato" contra "Exige fonte externa: vigência de lei hoje, prazo com feriado local"; conferência humana no pé (Dell'Acqua et al., 2023) [CONFERIR] | claro, médio | comparacao |
| 32 | Quem usa responde pelo que entrega | supervisionar, validar, corrigir, dar contexto | claro, leve | tempo |
| 33 | Hoje é a pior IA que você usará | frase única, como provocação | noite, respiro | respiro |

## Bloco 4. Qual é a melhor IA (24 min)

| # | manchete | o que a tela mostra | clima | arquétipo |
|---|---|---|---|---|
| 34 | Qual é a melhor IA? | abertura de capítulo; subtítulo "melhor para quê?" | noite, respiro | abertura |
| 35 | Benchmark é o ENEM da IA | prova padronizada: controlada, repetível, comparável; na fala, prova não é veredito | claro, leve | numero |
| 36 | Seis coisas que os benchmarks medem | raciocínio, programação, agentes, contexto longo, seguir instruções, confiabilidade | claro, médio | objetos |
| 37 | Existe prova só para o jurídico | Legal Index: seis categorias e pesos (35, 25, 15, 10, 10, 5), com fonte [CONFERIR] | claro, médio | escolha (barras) |
| 38 | Prova não é processo | "dados limpos e pergunta definida; o caso real não tem isso" | noite, respiro | respiro |
| 39 | Na arena, pessoas votam às cegas | duas respostas sem nome, a pessoa escolhe, depois vê os nomes | claro, leve | comparacao |
| 40 | Prática 5: qual você assinaria? | duelo projetado: mesma pergunta jurídica curta, duas respostas preparadas sem nome; a sala vota com 1 ou 2 dedos; dois alunos justificam; revelação; QR da arena para testar em casa; 3 min | noite, médio | objetos |
| 41 | Benchmark mede prova; arena, preferência | frase única; na fala, "você votou por precisão, clareza ou aparência de segurança?" | noite, respiro | respiro |
| 42 | Demos a prova da PGE às IAs | 12 dissertativas, um parecer e uma peça; 180 pontos; correção por dois modelos Gemma 4 com gabarito e espelho | claro, leve | numero |
| 43 | Nesta prova, o topo ficou próximo | dez barras (sem o modelo local), o topo próximo marcado; limitações legíveis no rodapé (S.T.A.R.) | noite, médio | cena própria |
| 44 | O que essa nota não diz | uma prova só; a de 2021 pode ter sido vista no treino; corrigida por modelo; prova não é trabalho | claro, médio | comparacao |

## Bloco 5. Fechados e abertos (8 min)

| # | manchete | o que a tela mostra | clima | arquétipo |
|---|---|---|---|---|
| 45 | Fechado ou aberto? | abertura de capítulo | noite, respiro | abertura |
| 46 | Aberto é ter os pesos | fechado: acesso só pelo serviço de quem vende; aberto: os parâmetros (pesos) podem ser baixados e rodados em outro lugar | claro, médio | comparacao |
| 47 | Os principais modelos fechados | grade com logo oficial, empresa, família de modelos e produto: OpenAI (GPT, ChatGPT), Anthropic (Claude), Google (Gemini), xAI (Grok), Meta (Muse), Microsoft (Copilot, produto que usa modelos de terceiros) [CONFERIR lista de out/2026] | claro, médio | objetos |
| 48 | Os principais modelos abertos | agrupado por empresa, com logo oficial: Meta (Llama), Google (Gemma), OpenAI (gpt-oss, se a licença confirmar), DeepSeek, Alibaba (Qwen), Mistral, Moonshot (Kimi), Zhipu (GLM) [CONFERIR] | claro, médio | ramos |
| 49 | Escolha por tarefa e teste você | teste com seu material, use mais de uma IA, confira na fonte; responde ao subtítulo da capa; ponte para a Aula 2 (como pedir bem) | noite, leve | fecho |
</ALVO>

## Pareceres

## Revisor A, rodada 1

1 · Aula 1, Slide 1 · importante · Tipos móveis de chumbo remetem a Gutemberg e imprensa clássica, repetindo o erro da versão anterior (arquivo de fichas) de usar uma metáfora analógica velha sem conexão visual com IA. · Trocar a descrição visual em "o que a tela mostra" para: `capa: still-life de prismas de vidro refratando feixes de luz em linhas de texto dourado; subtítulo "A IA escreve bem. Você confere como?"`. · alta

2 · Aula 1, Slides 1, 2, 8, 12, 18, 20, 29, 34, 40, 42 e 45 · importante · As manchetes de abertura, roteiro e práticas são títulos temáticos ou perguntas, violando o Critério 1 (toda manchete deve afirmar o que o slide prova em até 8 palavras e ~36 caracteres). · Substituir as manchetes por afirmações diretas: Slide 1: `A IA escreve bem, mas exige conferência`; Slide 2: `Entender a IA vem antes de escolher`; Slide 8: `Prática 1: você classifica seis sistemas`; Slide 12: `Por dentro, a IA é matemática`; Slide 18: `Prática 2: palavras viram blocos na tela`; Slide 20: `Prática 3: o mesmo pedido varia`; Slide 29: `Prática 4: teste se o acórdão existe`; Slide 34: `A melhor IA depende da tarefa`; Slide 40: `Prática 5: escolha a melhor resposta`; Slide 42: `Dez modelos fizeram a prova da PGE`; Slide 45: `Modelos mudam no acesso aos pesos`. · alta

3 · Aula 1, Slide 6 · importante · Empilhar cinco conceitos técnicos (simbólica, machine learning, deep learning, transformers, LLMs) em um único slide deixará o professor sem apoio visual individual para explicar a diferença entre regras fixas, aprendizado por dados e a arquitetura atual. · Quebrar o Slide 6 em dois slides: Slide 6A (arquétipo `comparacao`, claro, médio) com manchete `A IA aprendeu a aprender sozinha` mostrando `IA Simbólica (1956): regras humanas fixas` contra `Machine Learning: aprende padrões nos dados`; Slide 6B (arquétipo `ramos`, claro, médio) com manchete `Dos dados brutos aos modelos de texto` mostrando a descida `Machine Learning → Deep Learning (redes neurais) → Transformers (2017) → LLMs (2022)`. · alta

4 · Aula 1, Slide 8 · importante · A instrução mistura votação coletiva com chamada oral individual sem definir o que vai para a voz alta na hora da contagem, quebrando o padrão de instrução de prática exigido pelo professor. · Reescrever "o que a tela mostra": `onde: na tela do projetor; 1) leia os 6 sistemas (radar de placas, ChatGPT, filtro de spam, recomendação de loja, Gemini, detector de fraude); 2) ao sinal, levante 1 dedo (específica) ou 2 (geral); 3) observe a divisão da sala; 4) diga em voz alta "específica" ou "geral" a cada item e justifique o filtro de spam; 3 min`. · alta

5 · Aula 1, Slide 14 · importante · Dizer apenas que "textos ajustam parâmetros" não dá ao professor apoio visual concreto na tela para explicar o que é um parâmetro para leigos do direito (que vão perguntar o que significa "70 bilhões de parâmetros"). · Alterar "o que a tela mostra" para: `definição no topo: "Parâmetros = pesos numéricos que ligam palavras e ideias (como botões de uma mesa de som)"; abaixo, "Treino: textos calibram bilhões de pesos" contra "Uso: pesos travados calculam sua resposta"; número de parâmetros do Llama 3.1 70B [confirmar]`. · alta

6 · Aula 1, Slide 18 · importante · Abrir câmera, ler QR code em tela projetada, carregar site externo de tokenizador e colar texto em celulares variados (ou distribuir papel na "rota sem QR") não cabe em 2 minutos em uma turma mista com desembargadora e servidores. · Alterar o tempo no Slide 18 de `2 min` para `4 min` (compensando nos 25 min folgados do Bloco 2) e especificar a frase curta direto na tela para quem preferir digitar: `2) digite na caixa a frase "O réu agravou da decisão." (nunca texto de processo);`. · alta

7 · Aula 1, Slide 20 · importante · A instrução diz "no app instalado", sem nomear os dois aplicativos do curso (Claude e ChatGPT) nem explicar onde fica o botão de nova conversa no celular, o que trava alunos menos técnicos. · Ajustar "o que a tela mostra": `onde: app Claude ou ChatGPT no celular; 1) digite e envie: "Complete com uma frase: O juiz julgou o pedido"; 2) toque no ícone de "Nova conversa" (canto superior) e repita do zero mais duas vezes; 3) compare os três finais com o vizinho; 4) diga em voz alta "iguais" ou "diferentes"; 3 min`. · alta

8 · Aula 1, Slide 24 · crítica · Misturar dois fenômenos distintos no mesmo slide — o corte/resumo por estouro do limite de tokens e a perda de atenção no meio da janela (*lost in the middle*, Liu et al., 2023) — viola o Critério 1 (uma prova por slide) e repete a falta de apoio visual que fez o professor reprovar a versão 1. · Dividir o Slide 24 em dois: Slide 24A (arquétipo `comparacao`, claro, médio) com manchete `Passou do limite, o texto corta` mostrando `Histórico dentro da mesa: tudo lido` contra `Histórico maior que a mesa: início cortado ou resumido [CONFERIR por produto]`; Slide 24B (arquétipo `viagem`, claro, leve) com manchete `A IA esquece o meio do texto` mostrando uma curva em U de atenção: `Início do anexo (alta atenção) → Meio do anexo (queda de atenção) → Fim do anexo (alta atenção) (Liu et al., 2023)`. · alta

9 · Aula 1, Slide 29 · crítica · Nos planos gratuitos do ChatGPT e do Claude no celular, a busca na web é automática ou o botão de desligar fica escondido/indisponível dependendo da versão; se a busca entrar, a IA trará acórdãos reais da internet e arruinará a dinâmica de alucinação de memória. · Substituir os passos 1 e 2 no Slide 29 por um comando que contorna a busca sem depender de botão: `onde: app Claude ou ChatGPT no celular, em duplas; 1) digite exatamente: "Sem pesquisar na internet, usando apenas sua memória de treino, cite 3 acórdãos do STJ com número de REsp e relator sobre responsabilidade civil do Estado por omissão"; 2) se o app exibir "Pesquisando na web", cancele e peça "Responda sem usar a busca";`. · alta

10 · Aula 1, Slide 30 · importante · Uma pergunta genérica ("Os números conferiram?") após 6 minutos de prática dilui o choque pedagógico de descobrir que um número real de REsp trata de outro assunto ou que o processo não existe. · Alterar a manchete para `Acórdão inventado parece acórdão verdadeiro` e detalhar a tela: `os três resultados da sala na tela: 1) número não existe no STJ; 2) número existe, mas é de outro tema; 3) número e tema batem; regra de ouro: nunca protocole sem abrir o inteiro teor`. · alta

11 · Aula 1, Slide 37 · importante · O slide cita apenas os números `(35, 25, 15, 10, 10, 5)` sem escrever os nomes das seis categorias na tela, deixando o professor sem cola visual para explicar o Legal Index. · Incluir os rótulos exatos em "o que a tela mostra": `Legal Index: seis barras com pesos — conhecimento jurídico (35%), trabalho agêntico (25%), raciocínio (15%), contexto longo (10%), não alucinação (10%) e uso de ferramentas (5%), com fonte [CONFERIR]`. · alta

12 · Aula 1, Slide 42 · importante · O contexto estabelece que o professor proibiu falar do modelo Gemma 4 local no placar, mas o Slide 42 expõe que a correção da prova foi feita por "dois modelos Gemma 4"; a turma vai perguntar na hora o que é Gemma 4 e quanto ele tirou, além de o Slide 48 só apresentar o Gemma seis slides depois. · Trocar o texto de "o que a tela mostra" no Slide 42 para: `12 dissertativas curtas (10 pts cada), um parecer (30 pts) e uma peça (30 pts) da PGE-MS 2021; 180 pontos totais; correção automatizada por dois modelos abertos auditores usando o gabarito e o espelho oficiais` (deixando o nome técnico dos auditores apenas para a nota de rodapé metodológica se alguém perguntar). · alta

13 · Aula 1, Slide 43 · importante · O slide do momento S.T.A.R. diz apenas "dez barras (sem o modelo local)", omitindo os nomes e as notas exatas que precisam constar na arte do slide para apoiar a leitura do professor. · Especificar em "o que a tela mostra": `gráfico de dez barras em % da nota máxima: Claude Opus 5.5 (91,7%), Gemini 4 Argon (90,9%), Claude Sonnet 5.5 (88,7%), Muse Wonder (86,8%), GPT-6.1 Sol (83,4%), GPT-6 Luna (79,4%), Muse Spark 1.3 (78,0%), Gemini 3.8 Flash (77,8%), Claude Haiku 5.5 (75,5%), DeepSeek V4.1 Flash (64,4%); destaque dourado nos 4 primeiros; rodapé legível com limitações (S.T.A.R.)`. · alta

14 · Aula 1, Slides 46, 47 e 48 · opcional · Para um público jurídico sem formação técnica, saber que "os pesos podem ser baixados" parece um detalhe de TI irrelevante se a tela não conectar isso imediatamente a sigilo de processos e soberania de dados do tribunal/procuradoria. · No Slide 46, acrescentar na coluna de abertos: `aberto: os parâmetros (pesos) podem ser baixados e rodados no servidor do próprio órgão, sem enviar dados para fora`. · alta

## Revisor A, rodada 2

1 · Aula 1, slides 3–4 · **REFINO** · 1 · Aula 1, slides 3–4 · importante · O slide 3 traz exemplos mas não dá uma definição simples para o professor apoiar a fala antes das definições formais do slide 4. · No slide 3, exibir no topo: “Sistema que recebe dados, acha padrões e gera previsões ou conteúdo”, seguido de um exemplo concreto de entrada e saída (“Foto da placa → texto da placa”); no 4, manter OCDE e PL lado a lado com 1 linha de síntese em cada. · confiança alta

2 · Aula 1, slides 6–9 · **REFINO** · 2 · Aula 1, slides 7–9 · crítica · “Geral” no slide 7 confunde modelo de propósito geral com AGI, mas o professor pediu expressamente o par “específica contra generalista”. · Trocar a manchete do 7 para “Específica faz uma; generalista, várias” (35 caracteres); no 8, mudar para “Prática 1: específica ou generalista?” e no 9 para “Quatro específicas, duas generalistas”; adicionar rodapé no 7: “Generalista = modelo de uso geral (não é AGI)”. · confiança alta

3 · Aula 1, slides 13–15 e 26 · **REFINO** · 3 · Aula 1, slides 13–15 e 26 · crítica · “Parâmetros guardam o que ela leu” e “lembra” sugerem banco de dados de textos, induzindo o aluno a achar que a IA consulta arquivos internos. · No 14, manchete “O treino ajusta os parâmetros” (29 caracteres) e tela: “Parâmetros = números internos (pesos) calibrados no treino, não textos salvos”. No 15, manchete “Sem busca, ela calcula; não consulta” (36 caracteres). No 26, passo 2: “Parâmetros calibram pesos”. · confiança alta

4 · Aula 1, slides 16–18 · **REFINO** · 4 · Aula 1, slides 16–18 · importante · A captura impressa do slide 18 contradiz o passo 2 (“cole a frase”), travando quem não conseguir ler o QR code. · No slide 16, usar a mesma frase da prática. No 18, separar na tela: “Com internet: abra o QR, cole a frase do slide e conte os blocos. Sem internet: na folha impressa, conte os blocos coloridos da frase 2”. · confiança alta

5 · Aula 1, slides 19–21 · **MANTENHO** · Rotular as porcentagens do slide 19 como “ilustrativas para explicação” e pedir que anotem “igual ou diferente” no 20 blinda o professor caso o app dê três respostas idênticas em temperatura padrão.

6 · Aula 1, slides 22–25 · **REFINO** · 6 · Aula 1, slides 24–25 · importante · O slide 24 espreme dois conceitos densos (estouro de janela e perda de atenção no meio), prejudicando a explicação pausada que o professor pediu. · Deixar o 24 só para o limite (“Passou do limite, algo fica de fora”, arquétipo `comparacao`). Criar o 24B “No meio do texto, a atenção cai” (31 caracteres, `claro, médio`, arquétipo `objetos`, gráfico em U de Liu et al., 2023), mantendo o 25 (“Conversa nova, mesa limpa”, `respiro`) com a ressalva na tela: “salvo se a memória do app estiver ativa”. · confiança alta

7 · Aula 1, slides 28–30 · **MANTENHO** · Nos planos gratuitos, o controle de busca nem sempre é visível ou desligável; explicitar o que fazer se a busca seguir ativa e definir o critério de conferência (número + tema no link oficial do STJ) salva a prática em sala.

8 · Aula 1, slide 33 · **RETIRO** · A frase “a IA de hoje é a pior que você vai usar” é exigência expressa do professor no contexto; para não competir com o S.T.A.R. (slide 43), basta o professor tratá-la na fala como fecho rápido do Bloco 3, mantendo a tela original.

9 · Aula 1, slides 40–41 · **REFINO** · 9 · Aula 1, slides 40–41 · importante · “Qual você assinaria?” contradiz a regra de ouro da aula (nunca assinar sem conferir na fonte). · Trocar a manchete do 40 para “Prática 5: qual parece mais pronta?” (35 caracteres); manter a mecânica de votação cega para ilustrar como funciona a Arena e fechar no 41 contrastando preferência estética com necessidade de verificação. · confiança alta

10 · Aula 1, slides 42–44 · **REFINO** · 10 · Aula 1, slides 42–44 · importante · Retirar as dez barras do slide 43 descaracterizaria o momento S.T.A.R. e o placar completo da PGE-MS preparado pelo professor. · Manter as dez barras no slide 43, mas aplicar destaque cromático forte nas quatro primeiras (91,7% a 86,8%) e deixar as outras seis em tom neutro; substituir textos longos de rodapé por um selo curto e legível: “1 prova (PGE-MS 2021) · correção por IA · não é ranking geral”, deixando os detalhes metodológicos para o slide 44. · confiança alta

11 · Aula 1, slides 45–49 · **MANTENHO** · Reduzir o Bloco 4 de 24 para 20 minutos e subir o Bloco 5 de 8 para 12 minutos evita que os slides 47 e 48 virem leitura apressada de logotipos e garante tempo para o fecho da aula.

12 · Aula 1, slides 4, 23, 37, 43 e 47–49 · **MANTENHO** · Cravar a data de referência (“Verificado em [DATA]”) no slide 2 e nos rodapés de dados mutáveis cumpre o Critério 2 (fio da data sem contradição com a Aula 2) e força a resolução dos `[CONFERIR]` antes de entrar em sala.

## Revisor B, rodada 1

1 · Aula 1, slides 3–4 · importante · O slide 3 oferece exemplos e um esquema, mas ainda não dá ao professor uma definição simples para sustentar a explicação; o 4 salta para duas definições formais. · No slide 3, acrescentar: “IA é um sistema que recebe informações e produz previsões, recomendações ou conteúdo”; mostrar logo abaixo um exemplo de entrada e saída. No 4, destacar em uma linha o que as duas definições acrescentam, mantendo a distinção entre definição da OCDE e texto de projeto de lei. · confiança alta

2 · Aula 1, slides 6–9 · crítica · “Geral” no slide 7 pode soar como inteligência artificial geral, enquanto a prática classifica produtos capazes de várias tarefas. O gabarito do 9 não elimina a ambiguidade. · Trocar por “Uma tarefa ou várias tarefas?” e rotular a segunda coluna “modelo de uso geral, não inteligência artificial geral”; repetir essa distinção no gabarito. · confiança alta

3 · Aula 1, slides 13–15 e 26 · crítica · “Parâmetros guardam o que ela leu” e “lembra” sugerem um arquivo recuperável de textos. É uma explicação memorável, mas atrapalha justamente o conceito que o professor precisa ensinar. · Usar “O treino ajusta os parâmetros” no 14; na tela, “parâmetros = valores ajustados durante o treino, não uma biblioteca de documentos”. No 15, “Sem busca, ela não consulta fontes agora”. Ajustar o passo 2 do 26 para “Parâmetros são ajustados”. · confiança alta

4 · Aula 1, slides 16–18 · importante · O tokenizador sustenta bem a fala se a divisão exibida for a mesma que o aluno verá; a “captura impressa” do 18, porém, não permite colar nem contar sua própria frase. · Exibir no 16 o nome do tokenizador e a frase exata da prática. No 18, oferecer duas rotas: “Com acesso: abra o link, cole a frase e conte. Sem acesso: conte os blocos numerados na captura distribuída”. Imprimir também o resultado para conferência. · confiança alta

5 · Aula 1, slides 19–21 · importante · As porcentagens ilustrativas podem parecer medições reais. Repetir a frase três vezes no aplicativo também pode produzir finais iguais, sem demonstrar por si só como ocorre a escolha do próximo token. · Legendar o leque “probabilidades inventadas apenas para explicar”. No 20, pedir que anotem “igual/diferente” após as três tentativas; no 21, separar explicitamente “o que observamos no app” de “o mecanismo ilustrado no desenho”. · confiança alta

6 · Aula 1, slides 22–25 · importante · A sequência dá apoio à explicação da janela, mas o slide 24 junta dois problemas distintos numa única manchete: exceder o limite e perder informação no meio. “Conversa nova, mesa limpa” também promete mais do que as configurações do produto permitem afirmar. · Manter no 24 só “Passou do limite, algo fica de fora”; mover a observação sobre o meio para o 25, com manchete “Mesmo dentro, o meio pode falhar”. Explicar memória entre conversas em uma nota curta: “Verifique as configurações do aplicativo”. · confiança alta

7 · Aula 1, slides 28–30 · crítica · A prática manda desligar a busca “se tiver o botão”, mas não diz como prosseguir se ela permanecer ativa; procurar um número pelo QR também não especifica o que conferir no acórdão. · Instruir: “Se não localizar o controle, mantenha a configuração e diga isso na resposta”. Fornecer link curto e QR para a consulta oficial já testada pelo professor; pedir que a dupla confira **existência do número e correspondência do tema**, e responda com uma das três frases previstas. · confiança alta

8 · Aula 1, slide 33 · importante · “Hoje é a pior IA que você usará” é uma previsão categórica, sem apoio, e disputa com o placar o lugar de momento memorável da aula. · Trocar a manchete por “Ferramentas mudam; conferir continua necessário”; usar como transição discreta, não como segundo clímax. · confiança alta

9 · Aula 1, slides 40–41 · importante · “Qual você assinaria?” convida a escolher uma resposta jurídica antes de conferir sua fonte; a revelação dos modelos pode reforçar preferência por marca em vez do critério de julgamento. · Usar “Qual resposta você verificaria primeiro?”; entregar às duas respostas a mesma pergunta e identificar previamente, na preparação docente, os pontos verificáveis. Antes de revelar nomes, pedir: “Que afirmação exigiria fonte?” · confiança alta

10 · Aula 1, slides 42–44 · crítica · Dez barras mais limitações legíveis no rodapé concentram informação demais no S.T.A.R.; percentuais precisos podem parecer uma medida geral de qualidade jurídica. · No 43, destacar visualmente apenas a proximidade das primeiras notas e deixar as dez barras em material de consulta. Na tela principal: “Uma prova, uma correção automatizada, não um ranking universal”; disponibilizar método, respostas e critérios de correção junto ao placar. · confiança alta

11 · Aula 1, slides 45–49 · importante · Oito minutos para definir pesos abertos, percorrer duas grades de logos e fechar a aula tende a virar leitura de marcas. “Principais” e a lista datada exigem um critério que a tela não dá. · Reservar mais tempo a esse bloco, retirando minutos do bloco de benchmarks; nomear as grades “Exemplos selecionados em [DATA]” e separar visualmente **empresa | família de modelos | produto**. Conferir nomes, disponibilidade, licença e logos oficiais antes de publicar [confirmar]. · confiança alta

12 · Aula 1, slides 4, 23, 37, 43 e 47–49 · importante · O roteiro prevê fontes e [CONFERIR], mas ainda não mostra uma data de referência comum para definições legais, limites de produto, índices e modelos; sem ela, a ponte com a Aula 2 fica frágil. · Fixar no slide 2 “Informações verificadas em [DATA]”; repetir a data nas telas sujeitas a mudança e abrir a Aula 2 com a mesma referência. Substituir cada [CONFERIR] por fonte e situação verificadas antes da apresentação; se não houver verificação, retirar a afirmação. · confiança alta

## Revisor B, rodada 2

1 · **REFINO** · Aula 1, slide 1: tipos móveis têm relação com escrita, mas não mostram a mudança trazida pela IA. Ação: manter a foto e acrescentar, ao lado da palavra composta, três continuações diferentes geradas em texto. Evita trocar uma metáfora distante por outra apenas decorativa.

2 · **REFINO** · Aula 1, slides 1, 2, 8, 12, 18, 20, 29, 34, 40, 42 e 45: concordo com manchetes afirmativas, mas «Por dentro, a IA é matemática» não ajuda a explicar o capítulo. Usar, no slide 12, `Textos ajustam pesos; pesos geram respostas`; nos slides de prática, afirmar o resultado observável, não apenas anunciar «Prática».

3 · **REFINO** · Aula 1, slide 6: dividir dá ao professor o apoio que falta. Não usar «aprendeu a aprender sozinha» nem apresentar 2022 como nascimento dos LLMs. Telas: `Regras escritas diferem de padrões aprendidos` e `LLMs usam redes baseadas em transformers`, com um exemplo curto em cada uma.

4 · **MANTENHO** · Aula 1, slide 8: a sequência proposta define como votar e o que dizer. Manter os seis itens visíveis enquanto a turma responde.

5 · **REFINO** · Aula 1, slide 14: falta definir parâmetro, mas «liga palavras e ideias» sugere um arquivo de conceitos. Texto: `Parâmetros são números ajustados no treino`; abaixo, um mesmo pedido passando por pesos diferentes e produzindo saídas diferentes. O número de um modelo fica com `[CONFERIR]`.

6 · **REFINO** · Aula 1, slide 18: dois minutos são insuficientes. Dar quatro e pôr a frase na tela; a captura impressa serve para **observar** a divisão, não para executar a contagem. Não prometer que todos verão os mesmos blocos se usarem tokenizadores distintos.

7 · **REFINO** · Aula 1, slide 20: nomear Claude ou ChatGPT ajuda; «canto superior» pode variar. Escrever `toque em “Nova conversa” no seu app`; acrescentar `se não encontrar, observe as três tentativas projetadas`. Reservar tempo também para comparar e falar.

8 · **REFINO** · Aula 1, slide 24: separar estouro da janela e dificuldade com informação no meio. Na segunda tela, não dizer que a IA sempre «esquece» nem desenhar curva de atenção como fato geral; mostrar uma pergunta sobre dado colocado no início, meio ou fim e atribuir o achado ao estudo citado.

9 · **RETIRO** · Aula 1, slide 29: pedir «sem pesquisar» não impede necessariamente o uso de busca e cria outra dependência de interface. A prática pode funcionar com busca: a instrução deve dizer `se houver fontes, abra o resultado; se não houver, procure o número no STJ; registre “confere”, “não encontrei” ou “tema diferente”`.

10 · **REFINO** · Aula 1, slide 30: não projetar três desfechos como se todos tivessem ocorrido; cada dupla checou um número. Mostrar as três **categorias possíveis** e pedir um relato real de cada categoria que aparecer. Evitar «nunca protocole» como fecho único para desembargadora e servidores.

11 · **MANTENHO** · Aula 1, slide 37: escrever nomes e pesos das seis categorias na tela é essencial para explicar o índice, com fonte `[CONFERIR]`.

12 · **RETIRO** · Aula 1, slide 42: a restrição é retirar o resultado do Gemma local do placar, não esconder quem corrigiu. Nomear os dois modelos usados, o gabarito e o espelho torna o método mais auditável.

13 · **REFINO** · Aula 1, slide 43: a arte precisa especificar nomes e notas fornecidos no roteiro. Destacar **os dois primeiros**, não quatro, pois é entre eles que a manchete «topo próximo» dirige a comparação; manter as limitações legíveis.

14 · **REFINO** · Aula 1, slide 46: ligar pesos abertos à possibilidade de execução em infraestrutura própria é útil. Trocar «sem enviar dados para fora» por `pode permitir execução em infraestrutura própria, conforme licença, configuração e controles do órgão`; isso não promete sigilo automático.
