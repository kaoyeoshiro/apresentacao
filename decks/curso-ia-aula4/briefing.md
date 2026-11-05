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

- **A7, acesso mínimo (slide 9, 7 min).** Exercício 22.1 da apostila. Fecho nas notas: "Duas semanas, só lendo" (A 22.6, caixa "Duas semanas de teste com pouco acesso"). Resposta-modelo para "a agenda da manhã": pode
  ler a agenda e só os e-mails de uma pasta; pode escrever um rascunho salvo, nunca enviado; nunca: a caixa inteira, o
  sistema do tribunal com certificado, pagamento, apagar.
- **A8, plano B (slide 21, 5 min).** O que quebra costuma ser o que está preso ao app: instruções só na memória do chat,
  documentos só no projeto do fornecedor, nenhum segundo fornecedor testado. O slide 22 é o gabarito.
- **A9, debate (slide 29, 6 min).** Sem gabarito: o professor fecha com a leitura da ficha de geopolítica (seção 2),
  de que rodar dentro da infraestrutura do órgão tira o dado do alcance de terceiros e desloca o risco para o
  comportamento do modelo, que é o que a avaliação do CAISI mediu.
- **A10, plano de 30 dias (slide 34, 5 min).** Individual; cada um guarda o seu.
- **A11, devolutiva (slide 35, 5 min).** Em roda; o professor anota as faltas para a próxima turma.

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
