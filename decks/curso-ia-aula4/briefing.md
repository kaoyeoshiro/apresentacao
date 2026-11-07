# Briefing: curso de IA da co.juris, dia 2, Aula 4. Decidir (versão 1, 05/11/2026)

Segunda de duas aulas de cerca de 90 minutos do dia 2, depois de `decks/curso-ia-aula3` ("Fazer"). O desenho está em
`docs/curso-ia-dia2.md` e o plano em `docs/curso-ia-dia2-plano.md`. O deck é montado por `montar.py` a partir de
`fonte/`; edite `fonte/`, nunca o `deck.html`.

## Para quem, onde e o que fica

- Mesma turma: advogados, uma desembargadora, servidores e assessores; muitos sem plano pago. Exemplos neutros.
- Sala presencial, projetor e passador. Tema `cojuris`, plano contínuo, a mesma trilha dourada.
- Mensagem em uma frase: delegar à IA é decidir o que ela alcança, quanto ela custa e de quem você passa a depender.
- No fim, cada um sai com o desenho de acesso mínimo de um assistente, um plano B para o caso de o preço mudar, uma
  posição própria sobre onde o dado do órgão pode rodar e um plano de 30 dias; a turma dá a devolutiva do curso.
- Dinâmica: aula de mais conversa que tela; a sala faz cinco atividades (A7 a A11) com enunciado no slide e cronômetro,
  sem plano pago, instalação nem papel. Uma única demonstração, o vídeo do harness.
- Zero `[CONFERIR]` na tela. Número da OpenAI ou da xAI nunca aparece sem dizer que vem de vazamento a jornal; linha
  de confiança média das fichas só com a fonte nomeada no slide; linha de confiança baixa não vai à tela.
- Linha do dia (90 min): assistentes 27 (com a abertura), harness 6, quem paga 23, geopolítica 18, futuro e fecho 16.

## Arco

A Aula 3 terminou com "dê o jeito, a tomada e a agenda". A Aula 4 abre com o preço disso: quando a IA age sozinha, a
pessoa decide o que ela alcança, quanto paga por ela e a quem fica presa. Quatro movimentos respondem. O assistente que
lê a caixa de entrada inteira, onde está o cliente (assistentes); dez agentes e um só caro fazendo uma peça (harness);
o custo de cada uso, que já fechou, contra US$ 895 bilhões contratados em computação (quem paga); o dado guardado no
Brasil por empresa sujeita à lei americana (geopolítica). O futuro fecha com sinais datados, sem previsão de
consultoria, e com o plano de 30 dias de cada um.

## Roteiro

Mesmas convenções da Aula 3: "própria" é cena sem `data-arquetipo`; "guia" é a cena das atividades, com cronômetro;
"cartões" é o ajudante de `base.meio.js`.

| # | slide | manchete | o que a tela prova | clima e densidade | arquétipo | mídia e custo |
|---|---|---|---|---|---|---|
| 1 | capa | Quem decide é você | abertura da Aula 4; sub: "Assistentes, custos, geopolítica e o futuro." | noite, respiro | abertura | heroica gerada 2K, cerca de US$ 0,05 |
| 2 | mapa | Hoje, o que delegar e a que preço | cinco marcos (assistentes, harness, quem paga, geopolítica, futuro), assistentes aceso. Legenda: "Cada etapa termina numa decisão sua." | claro, leve | tempo | código |
| 3 | chat-agente | O chat responde; o assistente age | A "chat": responde quando você pede; B "assistente": age sem você pedir, de hora em hora | claro, leve | comparacao | código |
| 4 | cinco | Cinco assistentes, em novembro de 2026 | cinco cartões: Claude Duet (Anthropic, prévia, só EUA); dots (OpenAI, plano Pro, inclui o Brasil); Muse (Meta, no WhatsApp, EUA e Singapura); Grok Bot (xAI, beta, sem lista de países); Hermes Agent (código aberto, roda onde você instalar) | claro, médio | cartões | código |
| 5 | alcance | Na sua caixa está o cliente | **S.T.A.R. do bloco.** A caixa de entrada desenhada por código; o assistente "lê tudo" e acendem, uma por clique, a conversa com o cliente, a minuta antes do protocolo e a mensagem da parte contrária | noite, médio | própria | código |
| 6 | entrada | Quem escreve para você escreve para ele. | respiro: cada mensagem que chega é texto que o assistente lê | noite, respiro | respiro | nenhuma |
| 7 | sigilo | O sigilo vai junto com o acesso | quatro cartões: "E-mail da advocacia é inviolável" (EAOAB, art. 7º, II); "Violar sigilo sem justa causa é infração" (EAOAB, art. 34, VII); "Fornecedor que proteja dados e não treine com eles" (Recomendação OAB 001/2024, item 2.2); "Sigiloso na IA externa, só anonimizado ou com proteção técnica" (Res. CNJ 615/2025, art. 19, § 3º, IV, regra para magistrados e servidores) | claro, médio | cartões | código |
| 8 | memoria | Cortar o acesso não apaga a memória | três linhas, uma por clique: Duet, o que aprendeu fica até zerar a memória; dots, só se apaga o dot inteiro; Grok Bot, apagar o Bot não limpa o computador compartilhado | noite, médio | própria | código |
| 9 | a7 | Sua vez: o acesso mínimo | A7, 7 min. "Em dupla, escolham uma tarefa (a agenda da manhã, por exemplo) e preencham três colunas: pode ler, pode escrever, nunca." | claro, médio | guia, `pratica: 7` | código |
| 10 | harness-cap | O sistema em volta do modelo | abertura do bloco harness (capítulo); sub: "Uma peça da PGE-MS, por dentro." Aviso de rodapé: "A co.juris não fala em nome da PGE-MS." | noite, respiro | abertura | heroica gerada 2K, cerca de US$ 0,05 |
| 11 | harness | Dez agentes, uma peça | **S.T.A.R. do bloco.** O vídeo da Tarefa 6A (claude_video_maker, `agentes-peca-2`); nota: "Dados de uma peça real, sem processo." | noite, respiro | demonstracao | vídeo por código, US$ 0 |
| 12 | redator | O caro só onde faz diferença | barras do custo por agente na peça do print: o redator, US$ 1,39 de US$ 1,59 (87%); os outros nove somados, US$ 0,21 | claro, leve | própria | código |
| 13 | conta-cap | Quem paga a conta | abertura do bloco (capítulo); sub: "O uso já se paga. A corrida, não." | noite, respiro | abertura | heroica gerada 2K, cerca de US$ 0,05 |
| 14 | custo | Cada uso já se paga | barras do custo de computação da Anthropic sobre a receita: 653% (2024), 160% (2025), 57% (jan. a set. de 2026). Fonte no slide: prospecto na SEC, 02/11/2026 | claro, leve | própria | código |
| 15 | compromissos | US$ 895 bi | **S.T.A.R. do bloco.** O número a 320 px; legenda: "em computação contratada pela Anthropic, pagos com ou sem uso" | noite, respiro | própria | código |
| 16 | quem-banca | Quem banca a corrida | ramo 1 investidores, para "treino e data centers"; ramo 2 usuário leve, para "usuário pesado". Legenda: "O preço de hoje não paga a próxima geração." | claro, leve | ramos | código |
| 17 | pesado | O usuário pesado custa caro | dois cartões datados: Altman, jan./2025, "currently losing money on openai pro subscriptions"; Anthropic, jul./2025, limites semanais para menos de 5% dos assinantes, um deles com "tens of thousands" de dólares de uso num plano de US$ 200 | claro, médio | cartões | código |
| 18 | encolhe | O plano fixo está encolhendo | marcos: jun./2026, Copilot passa a cobrar por consumo; jul./2026, o modelo de ponta da Anthropic sai do Pro; nov./2026, o plano Go do ChatGPT "pode incluir anúncios". Legenda: "A própria Anthropic lista isso como risco." | claro, leve | tempo | código |
| 19 | bolha | Bolha ou não? | A "alerta": BIS (jun./2026) e FMI (out./2026) veem risco de correção, com dívida e acordos opacos; B "contra": receita crescendo e 55,9% das empresas dos EUA pagando por IA (Ramp, set./2026) | claro, médio | comparacao | código |
| 20 | tese | A tecnologia fica. O preço muda. | respiro com a tese da aula | noite, respiro | respiro | nenhuma |
| 21 | a8 | Sua vez: e se o preço dobrar? | A8, 5 min. "Em dupla: o que quebra no seu trabalho se o plano dobrar de preço na sexta?" Ao lado, o checklist de portabilidade (slide 22) em miniatura | noite, médio | guia, `pratica: 5` | código |
| 22 | portavel | O que vai com você de um app a outro | cartões: a skill (o mesmo `SKILL.md` no Claude e no ChatGPT/Codex); a pasta no seu disco; as instruções em texto; um segundo fornecedor já testado | claro, médio | cartões | código |
| 23 | geo-cap | Quem manda no dado | abertura do bloco geopolítica (capítulo); sub: "Chips, modelos abertos, regras e jurisdição." | noite, respiro | abertura | heroica gerada 2K, cerca de US$ 0,05 |
| 24 | chips | Chip de ponta é política de Estado | dois cartões: a TSMC fabrica quase todo chip de IA de ponta (AI Index 2026); desde 15/01/2026 os EUA licenciam caso a caso a venda à China, com teto de metade do volume vendido nos EUA | claro, médio | cartões | código |
| 25 | quatro-meses | 4 meses | o número a 320 px; legenda: "é a distância dos melhores modelos abertos para os fechados (Epoch AI, mai./2026)" | noite, respiro | própria | código |
| 26 | aberto-seguro | Aberto não quer dizer seguro | CAISI/NIST, 30/09/2025: agentes sobre o DeepSeek R1-0528 seguiram instruções maliciosas 12 vezes mais; com um jailbreak comum, atenderam 94% dos pedidos maliciosos, contra 8% dos americanos. Rodapé: "Avaliação do governo dos EUA sobre modelos chineses." | claro, médio | cartões | código |
| 27 | cloud-act | Dado no Brasil, empresa nos EUA | **S.T.A.R. do bloco.** Ramo 1 "data center no Brasil", para "onde o dado mora"; ramo 2 "provedor americano", para "quem pode mandar entregar". Legenda: "CLOUD Act: os EUA têm acordo só com Reino Unido e Austrália." | claro, leve | ramos | código |
| 28 | regras | As regras chegam em datas diferentes | marcos do AI Act: fev./25 proibições; ago./26 fiscalização; dez./27 alto risco (Anexo III); ago./28 produtos regulados. Legenda: "No Brasil, o PL 2338/2023 espera parecer na Câmara." | claro, leve | tempo | código |
| 29 | a9 | Debate: modelo chinês no órgão? | A9, 6 min. "Modelo aberto chinês, rodando no servidor do órgão: pode?" Três perguntas para preparar: onde roda? quem controla a empresa? o que ele faz com uma ordem maliciosa? Metade da sala defende cada lado | noite, médio | guia, `pratica: 6` | código |
| 30 | futuro-cap | E em 2030? | respiro que abre o bloco futuro (capítulo) | noite, respiro | respiro | nenhuma |
| 31 | ritmo | 5x ao ano | o número a 320 px; legenda: "cresce o cômputo de treino dos modelos líderes; a eficiência, de 2 a 6x" (Relatório Internacional de Segurança da IA, 2026) | claro, respiro | própria | código |
| 32 | cenarios | De ganho modesto a salto rápido | ramo 1 "modesto"; ramo 2 "rápido", para "tarefas de software de vários dias". Legenda: "Gargalos: dados, chips, dinheiro e energia." | claro, leve | ramos | código |
| 33 | sinais | Sinais para acompanhar | marcos: dez./26, regras de transparência do AI Act; Câmara, parecer do PL 2338; Epoch, nova medição da distância dos abertos; abr./27, novo AI Index | claro, médio | tempo | código |
| 34 | a10 | Seu plano de 30 dias | A10, 5 min. Três linhas para cada um preencher: semana 1, uma skill do seu jeito; semanas 2 e 3, uma pasta de caso; semana 4, uma rotina que pode falhar sem dano | noite, médio | guia, `pratica: 5` | código |
| 35 | a11 | O que você leva, o que faltou | A11, 5 min. Devolutiva em roda: cada um diz uma coisa que leva e uma que faltou | claro, leve | guia, `pratica: 5` | código |
| 36 | curso | Quatro aulas, quatro verbos | marcos: entender (Aula 1), pedir (Aula 2), fazer (Aula 3), decidir (Aula 4), o último aceso | claro, leve | tempo | código |
| 37 | fecho | Delegue pouco. Confira a fonte. | mensagem do curso; notas: agradecimento e onde está o kit | noite, respiro | fecho | nenhuma |

Mídia prevista: quatro heroicas geradas (capa e três capítulos), cerca de US$ 0,20 mais rascunhos, dentro do teto; o
vídeo do harness sai do claude_video_maker sem custo.

### Conferência do roteiro

1. Arco com tensão na abertura, quatro movimentos e fecho com pedido: sim.
2. Um S.T.A.R. por bloco: alcance (assistentes), harness, compromissos (quem paga), cloud-act (geopolítica); o futuro
   fica quieto e termina no plano de cada um.
3. A maior sequência sem respiro tem cinco slides; os números a 320 px (15, 25, 31) contam como respiro.
4. Vizinhos não repetem arquétipo; a10 e a11 são duas cenas guia seguidas, de propósito, porque fecham a aula com a
   sala.
5. a 9. Manchetes curtas e afirmativas; nenhuma parada prevista acima de 45 palavras (as de cartões ficam no limite e
   serão medidas); mais da metade com número, diagrama, gráfico ou vídeo; cada dado com fonte abaixo; gasto dentro do
   teto.

## Atividades (enunciado na tela, gabarito nas notas)

- **A7, acesso mínimo (slide 11, 5 min).** Exercício 22.1 da apostila. Fecho nas notas: "Duas semanas, só lendo" (A 22.6, caixa "Duas semanas de teste com pouco acesso"). Resposta-modelo para "a agenda da manhã" (revista em
  06/11/2026): pode ler a agenda e uma conta de e-mail separada, que recebe por encaminhamento só os e-mails escolhidos
  (no Gmail, a permissão de leitura vale para a caixa inteira e a de rascunho também envia); pode escrever um resumo num
  arquivo, ou um rascunho nessa conta separada; nunca toca a caixa principal, o sistema do tribunal com certificado,
  pagamento, apagar, abrir link ou anexo de quem escreveu. Cortado o acesso, memória e histórico podem continuar retidos:
  conferir a política do fornecedor e usar os recursos de exclusão; apagar no app não garante que o provedor apague
  cópias retidas. A ficha ganhou a quarta linha "Se ele errar ou se calar: quem percebe, e como?".
- **A8, plano B (slide 23, 4 min).** Dois cenários separados: o plano dobra de preço; o preço fica e a franquia cai à
  metade. Para cada um, o que quebra e, pela fatura, quantas horas por mês o aumento precisa poupar (conta da revisão:
  US$ 20 para US$ 40 se paga com 0,3 a 0,9 hora; US$ 200 que dobra, com 2,7 a 9,3 horas, com hora de R$ 150 a R$ 300 e
  câmbio de 4 a 7, fictícios). O que quebra costuma ser o que está preso ao app: instruções só na memória do chat,
  documentos só no projeto do fornecedor, nenhum segundo fornecedor testado; vai na tela no segundo clique. O slide 22
  mostra o que vai com você.
- **A9, condições (slide 31, 5 min).** Pergunta de condições, sem lados de debate: "Modelo aberto de laboratório
  chinês, rodando sem internet no servidor do órgão, para resumir petições. Em que condições pode?", com "Onde roda, e
  quem opera a máquina? O que a empresa ainda controla, se o dado não sai? O que ele faz com uma petição que traz ordem
  escondida?" (encurtadas na tela). Sem gabarito: o professor fecha com a leitura da ficha de geopolítica (seção 2),
  de que rodar dentro da infraestrutura do órgão tira o dado do alcance de terceiros e desloca o risco para o
  comportamento do modelo, que é o que a avaliação do CAISI mediu.
- **A10, plano de 30 dias (slide 34, 5 min).** Individual; cada um guarda o seu. Em cada semana: com que dado fictício
  testo primeiro, como sei que deu certo (um número), o que ela nunca faz e quem confere; semanas 2 e 3, a pasta no
  próprio disco, fora do app; semana 4, rotina agendada exige plano pago e registra "rodou e achou zero".
- **A11, devolutiva (slide 35, 4 min, minutos 85 a 89).** Leva: o que vai fazer na segunda-feira, numa frase. Faltou: o
  que queria ter feito com as mãos e não fez. Dois minutos escrevendo, depois a roda; o professor anota as faltas para a
  próxima turma. Os slides 36 e 37 ficam com o minuto 89 a 90.

## Fontes por slide

Fichas de 05/11/2026 em `docs/pesquisa/`: economia (E, `dia2-economia-subsidio-bolha.md`), geopolítica (G,
`dia2-geopolitica-ia.md`), harness (H, `dia2-harness-quatilex.md`). Apostila v2 (A), capítulo 22 e a ficha
`fontes/cap22-assistentes.md`.

| slides | afirmação | fonte |
|---|---|---|
| 3, 4 | os cinco assistentes, fabricante, data, planos e Brasil, retrato de 02/11/2026 (Duet 21/10/2026, prévia, Pro, Max e Ultra, só EUA; dots 29/09/2026, Pro, mercados exceto EEE, Suíça e Reino Unido; Muse 08/09/2026, EUA e Singapura; Grok Bot 11/08/2026, beta, sem lista de países; Hermes Agent, código aberto) | A 22.2 a 22.4, Tabela 22.1; fontes/cap22-assistentes.md |
| 5, 6, 8 | o que o assistente lê na caixa; quem escreve para você escreve na entrada dele; memória depois de revogar o acesso (Duet, dots, Grok Bot) | A 22.5 |
| 7 | Lei 8.906/1994, art. 7º, II (redação da Lei 11.767/2008), e art. 34, VII; Recomendação OAB 001/2024, item 2.2 ("não utilização dos dados fornecidos para treinamento"); Res. CNJ 615/2025, art. 19, § 3º, IV (vale para magistrados e servidores; anonimização na origem ou mecanismos técnicos e procedimentais), conferidos na fonte oficial em 05/11/2026 | `docs/pesquisa/dia2-sigilo-normas.md` (planalto.gov.br, s.oab.org.br, atos.cnj.jus.br) |
| 11, 12 | 10 agentes, 6 modelos, US$ 1,5928 a peça, redator em Claude Opus 5.5 com US$ 1,3859 (87,0%); papéis e ordem | H (print de 05/11/2026 e leitura do código, com a correção do `afirmacao_oficio`) |
| 14, 15 | custo de computação da Anthropic sobre a receita (653%, 160%, 57%); compromissos de cerca de US$ 895,4 bi, "regardless of actual utilization" | E, S-1/A da Anthropic na SEC, 02/11/2026 (confiança alta) |
| 17 | Altman, 05/01/2025; Anthropic, limites semanais anunciados em 28/07/2025 | E (TechCrunch, confiança alta) |
| 18 | Copilot por consumo desde 01/06/2026; Fable fora dos limites do Pro (promoção encerrada em 19/07/2026); "This plan may include ads" no Go; risco de mudar limites declarado no S-1/A | E (github.blog, support.claude.com, chatgpt.com/pricing, SEC; confiança alta) |
| 19 | BIS, 28/06/2026; FMI, 13/10/2026 (confiança alta); Ramp AI Index, 55,9% em set./2026 (confiança média, fonte nomeada no slide) | E |
| 22 | o mesmo `SKILL.md` serve ao Claude e ao ChatGPT/Codex | briefing da Aula 2 (decisão 6) e apostila 16.5 |
| 24 | TSMC e AI Index 2026; 91 FR 1684, licença caso a caso, teto de 50% | G 1.1 (confiança alta) |
| 25 | defasagem de cerca de quatro meses (Epoch AI, 29/05/2026) | G 1.2 (alta) |
| 26 | CAISI/NIST, 30/09/2025: 12 vezes; 94% contra 8% | G 1.2 (alta) |
| 27 | CLOUD Act, 18 U.S.C. § 2713; acordos só com Reino Unido e Austrália | G 1.5 (alta) |
| 28 | calendário do AI Act e do Omnibus; PL 2338/2023 aguardando parecer em 05/11/2026 | G 1.4 (alta) |
| 31, 32 | Relatório Internacional de Segurança da IA, 03/02/2026: cômputo 5x ao ano, eficiência 2 a 6x, cenários da OCDE, gargalos | G 1.6 (alta) |
| 33 | sinais datados | G seção 3 (itens 1, 4, 5 e 7) |

## Pendências deste briefing

- O vídeo do harness (slide 11) depende da Tarefa 6A, no claude_video_maker.
- *A próxima onda* (Suleyman e Bhaskar) fica fora: não há edição em mãos para citar página.
- Notas `{diga, faca, transicao}` de cada slide: escritas na montagem, só com os fatos acima.

## Montagem (05/11/2026)

Blocos montados por subagentes e conferidos pela folha de contato; deck inteiro com lint limpo e 0 erro(s) no oráculo.
Ajustes na integração: no slide 7 (sigilo), as referências ficaram curtas na tela ("EAOAB 7º, II", "EAOAB 34, VII",
"Rec. OAB 1/2024", "CNJ 615/2025") e dois cartões foram encurtados ("Fornecedor que não treine com os dados";
"Sigiloso na IA externa, só anonimizado ou protegido"), para caber em 45 palavras; as referências completas e a
ressalva da Res. CNJ 615 estão nas notas. O slide 27 (cloud-act, S.T.A.R. da geopolítica) foi para a noite, para
quebrar três claros seguidos. Pelos subagentes: pesado (17) foi para a noite pelo mesmo motivo; ritmo (31) saiu sem
rótulo. O vídeo do harness (slide 11) ainda é o marcador; a animação vem do claude_video_maker (Tarefa 6A).

Aviso aceito: hierarquia (23 de 37 sem nada acima de 120 px), a rever depois das heroicas.

## Decisão sobre imagens (05/11/2026)

O professor decidiu "sem foto, como antes": nenhuma imagem gerada nesta aula, como nas Aulas 1 e 2. A capa segue o
modelo da capa da Aula 2 (logo oficial da co.juris à esquerda, fio e título à direita, fundo claro) e as aberturas de
capítulo ficam no arquétipo abertura sem `.heroi-caixa`. A coluna "mídia e custo" do roteiro que previa heroicas fica
sem efeito; gasto de imagem: zero.

## Crítica

**Rodada 1 (05/11/2026, subagente crítico com o prompt de `critica.md`).** Corrigidos: em chips, o cartão "Venda à
China" dizia o contrário da regra e passou a "até metade do que vendem nos EUA", com as barras "vendido nos EUA" e
"teto"; em a8, a resposta aparecia antes do tempo da dupla e agora entra no segundo clique; em pesado, "US$ 200" ficou
grande e é o único dourado; em sigilo, o cartão da CNJ 615 ganhou a borda dourada; em aberto-seguro, só o 94% fica em
dourado e o 8% vai na tinta suave; quatro-meses passou para o claro, e o rodapé com a definição de modelo aberto foi
para as notas, para não formar três claros parecidos; em cenarios, a faixa fica atribuída à OCDE e as tarefas de vários
dias ao Relatório Internacional de Segurança da IA 2026; o aviso de harness-cap ficou na linha do subtítulo; os dois
subtítulos de a11 dizem "diga uma".

Depois da rodada, a capa passou ao modelo da Aula 2 e o slide 11 toca a animação do harness (`midia/harness.mp4`, 40 s,
do claude_video_maker), com `ritmoOk` declarado porque o professor narra por cima. O vídeo-marcador `demo.mp4` saiu da
pasta. A primeira busca desse vídeo longo às vezes fotografava o quadro antigo; o motor passou a esperar o quadro
apresentado (`requestVideoFrameCallback`) no modo de render. Oráculo: 0 erro(s), 1 aviso (hierarquia), 1 isenção.

**Rodada 2 (05/11/2026).** Corrigidos: no harness, a capa do vídeo era o quadro de 2,5 s, com a cena já montada, e
aparecia inteira na viagem para sumir no pouso, quando o clipe começa do quadro 0 (cheio, vazio, cheio em menos de dois
segundos); a capa passou a ser o próprio quadro 0, gravada de novo a partir do vídeo, que não mudou, e o crédito
registra o segundo 0. Tirar a capa resolvia a viagem mas deixava o oráculo instável no instante em que o clipe ainda
não pintou o primeiro quadro, por isso ela voltou com o quadro novo. Em quatro-meses, o "4" no dourado de texto e o
sublinhado no dourado da trilha eram dois dourados que se chocavam; saiu o sublinhado e o número fica como o único
dourado. Em encolhe, as aspas de "pode incluir anúncios" ficavam no fim da linha de cima e agora vão inteiras para a de
baixo. Ficam como estão, por serem da biblioteca e baixos: a elipse de "Assistente" em chat-agente passa a 10 px do
divisor, e a moldura do vídeo do harness termina a 23 px da trilha, como no catálogo.

**Rodada 3 (05/11/2026).** Corrigido: em futuro-cap, a viagem de capítulo só fecha a base da trilha e acende o pad da
direita 0,7 s depois do pouso, depois do fim do passo, e a parada ficava sem o pad; o slide ganhou `passos: [3.0]`.
Nenhum defeito alto ou médio restante. Em aberto para o professor, de gravidade baixa: sigilo e chips são os únicos
slides de conteúdo sem rótulo acima da manchete (proposta "ASSISTENTES" e "GEOPOLÍTICA"); no cartão do Altman, em
pesado, sobra meia altura vazia. Numa das rodadas, a folha de `paradas --viagens` fotografou o vídeo do harness no
quadro 0 na parada final; o defeito era do modo de render do motor, que esperava
só 0,3 s pelo quadro; com 1 s, três rodadas seguidas deram o mesmo still. Oráculo: 0
erro(s), 1 aviso (hierarquia), 1 isenção (harness).

## Revisão pós-feedback (06/11/2026)

O professor aprovou o relatório `relatorio-feedback-aulas-3-e-4.md`. O roteiro acima fica como registro da versão 1; o
que mudou: harness passou a "Oito agentes, duas buscas, uma peça" (o vídeo, que não foi alterado, escreve "10 agentes"
porque conta as duas buscas como ferramenta), com a legenda "Peça real; o print não mostra dado do processo", e a nota
do redator diz que 82% do US$ 1,39 é carregar e reler o contexto e 18% é escrever; a A7, a A8, a A9, a A10 e a A11
mudaram como descrito em "Atividades"; o slide 28 traz no rodapé "Na comparação americana entrou o gpt-oss, também
aberto; idioma dos testes não informado.", e a origem da avaliação ("governo dos EUA") subiu para a linha da fonte; o
fecho mostra o endereço do kit. O slide cinco (assistentes) não foi tocado. Ficam com o professor, sem mudança: CLOUD
Act, LGPD e lei chinesa no fecho da A9; a ressalva da Res. CNJ 615/2025 no cartão do slide 7; a menção do Estatuto aos
procuradores; o formulário anônimo da A11, que ainda não existe.

Avisos aceitos nesta revisão: aberto-seguro com 52 palavras (o rodapé novo é o texto aprovado e a ressalva do governo
dos EUA continua na tela); oito slides sem respiro de sigilo a custo, porque a legenda nova do harness passou de 12
palavras.

Pastas e Projetos (06/11/2026, aprovado em t96u, `parecer-pastas-vs-projetos.md`, seção 9.3): nas notas de `portavel`, as
instruções fora da memória do chat ganham o exemplo "como o CLAUDE.md ou o AGENTS.md da pasta". O slide `cinco` não foi
tocado.

## Slide do Grok Bot (06/11/2026)

A pedido do professor, entrou depois de cinco o slide grokbot ("Como eu uso o meu"), com uma animação de 62 s feita no
claude_video_maker (`videos/grokbot`, branch `video/grokbot`): o assistente pessoal do professor e o que ele faz com ele,
nas palavras da mensagem de 06/11/2026 (resumo diário de IA do X, do Reddit e do YouTube; WhatsApp e recados para a
agenda; orquestração pelo t3code no Claude, no GPT, no opencode e no Gemini; ofícios, CIs e processos no E-MS,
respondidos sozinho por escolha do professor; pendências do PGE.Net; eventos de legaltech e editais da semana;
pesquisa de compras). Avatares desenhados por código, sem logotipo; mensagens, ofícios e compromissos fictícios. Tem som: só os efeitos sintetizados, a 30% do volume, para o professor falar por cima; no mesmo dia o vídeo do
harness passou a ter o mesmo tratamento, também a pedido do professor. As prévias
da tela do apresentador ficam sempre mudas. O deck passa a 38 slides.

## Ajustes do professor (06/11/2026, noite)

Fonte de tudo o que entrou: `docs/pesquisa/dia2-futuro-e-assistentes.md` (F). O slide `cinco` passou a sete
assistentes, sem destaque dourado (F 2.1 a 2.3; o OpenBot é o da CopilotKit, sem data confirmada, por isso sem data
nas notas). Em `custo`, os 57% são a computação total, treino incluído (F 1); a manchete virou "A computação já cabe
na receita", e os 14,5% do atendimento ficam só nas notas (cálculo sobre a nota 8 do S-1/A). Em `quem-banca`, o ramo
de cima leva "data centers dos próximos anos". O bloco futuro ficou: futuro-cap ("E em 20 anos?"), ritmo, cenarios
(os quatro cenários da OCDE, F 4), otimistas e pessimistas (F 3.1 e 3.2), medido (Stanford, 19%, F 3.2 e 3.3),
horizontes (fecho da F 3), debate (8 min), sinais, a10, a11, curso e fecho. Para o trecho de sigilo a custo não passar
de cinco slides sem respiro, o "87%" de `redator` subiu para 206 px. Sobram três avisos de palavras aceitos: cinco
(58, texto ditado), aberto-seguro (52, anterior) e medido (46, texto ditado).

## Slide retencao (06/11/2026)

"Assinatura não é contrato": treino e retenção na assinatura individual contra contrato empresarial e API. Fonte: `docs/pesquisa/dia2-retencao-e-treino.md`, políticas oficiais de Anthropic, OpenAI, Google, AWS e Microsoft lidas em 06/11/2026. "Pode guardar por anos": Claude com treino permitido até 5 anos, Gemini pessoal 18 meses (revisados até 3 anos). "Na API, guarda até 30 dias (Google, 55)": APIs da Anthropic e da OpenAI até 30 dias; Gemini API 55 dias para abuso; Bedrock em regra não guarda. Não confirmado e fora da tela: prazo em dias da revisão de abuso no Azure e no Vertex.
