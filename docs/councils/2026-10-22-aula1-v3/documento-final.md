# Documento final do conselho: Aula 1, versão 3

**Status.** Revisores ativos: A e B (2). Ausentes: nenhum. Rodadas executadas: 2.

Códigos usados abaixo: A1 a A14 são as sugestões do Revisor A na rodada 1; B1 a B12, as do Revisor B na rodada 1. Na rodada 2, cada revisor respondeu às sugestões do outro (A às de B, B às de A). Nenhuma sugestão ficou sem debate, então nenhuma leva a marca `[não debatido]`.

## 1. Consensos

Os dois revisores convergiram, depois da segunda rodada, nos pontos abaixo.

- Slides 3 e 4 (B1): o slide 3 precisa de uma definição simples com exemplo de entrada e saída antes das definições formais do slide 4.
- Slides 7 a 9 (B2): "geral" se confunde com IA geral (AGI); o termo do professor, "generalista", resolve, com rodapé que afaste a confusão.
- Slides 13 a 15 e 26 (B3, A5): "parâmetros guardam o que ela leu" e "lembra" sugerem arquivo de textos; parâmetro deve aparecer como número ajustado no treino.
- Slide 6 (A3): dividir em dois slides dá ao professor o apoio que falta.
- Slide 8 (A4): a instrução precisa dizer como votar e o que falar em voz alta.
- Slides 16 a 18 (B4, A6): mesma frase no slide 16 e na prática, tokenizador nomeado, duas rotas (com e sem acesso) e 4 minutos em vez de 2.
- Slides 19 a 21 (B5): porcentagens rotuladas como ilustrativas e registro "igual ou diferente" na prática 3.
- Slide 20 (A7): nomear Claude ou ChatGPT e dizer como abrir conversa nova.
- Slide 24 (A8, B6): estouro da janela e perda no meio são dois fenômenos e vão para telas separadas.
- Slide 29 (B7): a prática precisa dizer o que fazer se a busca continuar ligada e o que conferir (número e tema).
- Slide 37 (A11): nomes e pesos das seis categorias escritos na tela.
- Slide 46 (A14): ligar pesos abertos à execução em infraestrutura própria, sem prometer sigilo automático.
- Blocos 4 e 5 (B11): o bloco de fechados e abertos precisa de mais tempo, tirado do bloco de benchmarks.
- Data de referência (B12): "verificado em [DATA]" no slide 2 e nos rodapés de dados que mudam.

## 2. Divergências

**Capa, slide 1 (A1).** A quer trocar os tipos móveis por prismas de vidro refratando luz em texto dourado, porque os tipos repetiriam o erro da foto de fichas. B quer manter a foto e acrescentar três continuações diferentes da palavra composta, porque os prismas seriam outra metáfora apenas decorativa e as continuações mostram o que a IA faz.

**Manchetes de abertura e prática (A2).** A pede manchete afirmativa em onze slides, inclusive capa e aberturas de capítulo. B concorda com o princípio, mas recusa "Por dentro, a IA é matemática" por não explicar nada, e pede que as práticas afirmem o resultado observável em vez de anunciar "Prática".

**Slide 6 (A3).** A propõe "A IA aprendeu a aprender sozinha" e a sequência "Transformers (2017) → LLMs (2022)". B aceita a divisão, mas recusa a manchete (antropomorfiza) e recusa 2022 como nascimento dos LLMs.

**Slide 14 (A5).** A quer definir parâmetro como "pesos que ligam palavras e ideias, como botões de uma mesa de som". B acha que "liga palavras e ideias" volta a sugerir arquivo de conceitos e prefere "números ajustados no treino".

**Slide 24 (A8, B6).** A cria um 24B com curva em U de atenção; B, na rodada 1, levava o tema do meio para o slide 25 e, na rodada 2, recusa a curva como fato geral e propõe mostrar um dado posto no início, no meio ou no fim, com o achado atribuído ao estudo. A, por sua vez, quer preservar o slide 25 como respiro.

**Slide 29 (A9).** A quer um comando escrito ("sem pesquisar na internet, usando só a memória de treino") para contornar a busca automática. B recusa porque o pedido não impede a busca e cria outra dependência de interface; para ele a prática funciona com ou sem busca, desde que a dupla confira a fonte.

**Slide 30 (A10).** A quer a manchete "Acórdão inventado parece acórdão verdadeiro" e os três desfechos projetados, fechando com "nunca protocole sem abrir o inteiro teor". B diz que cada dupla checou um número só, que a tela não deve presumir os três desfechos e que "nunca protocole" fecha mal para desembargadora e servidores.

**Slide 33 (B8).** B quer trocar "Hoje é a pior IA que você usará" por "Ferramentas mudam; conferir continua necessário", por ser previsão sem apoio e competir com o momento S.T.A.R. A lembra que a frase é pedido expresso do professor.

**Slide 40 (B9).** Os dois concordam que "Qual você assinaria?" contraria a regra de conferir antes de assinar. A propõe "qual parece mais pronta?", preservando a lógica de preferência da arena; B propõe "qual você verificaria primeiro?" e uma pergunta antes da revelação ("que afirmação exigiria fonte?").

**Slide 42 (A12).** A quer omitir o nome dos corretores (dois Gemma 4), para a turma não perguntar a nota do Gemma local. B lembra que a restrição do professor é tirar o resultado do Gemma local do placar, não esconder quem corrigiu, e que nomear o método o torna auditável.

**Slide 43 (A13, B10).** A quer as dez barras com nomes e notas, destaque nos quatro primeiros e um selo curto no lugar do rodapé longo. B, na rodada 1, queria as dez barras fora da tela principal; na rodada 2 aceita nomes e notas, mas pede destaque só nos dois primeiros, porque é entre eles que "o topo ficou próximo" se verifica.

## 3. Lista final, por severidade

Cada item traz entre parênteses os códigos que decide e se foi aceito ou adaptado.

**Críticos**

1. **Slide 29, protocolo da prática 4** (B7 aceita; A9 rejeitada, ver seção 4). Passos na tela: "1) se o app tiver o botão de busca, desligue; se não achar, siga assim mesmo; 2) peça 'Cite 3 acórdãos do STJ, com número, sobre responsabilidade civil do Estado por omissão'; 3) se a resposta trouxer fontes, abra uma; se não trouxer, procure um número no site do STJ pelo QR ou link curto testado pelo professor; 4) confira duas coisas, se o número existe e se o tema bate; diga 'confere', 'não encontrei' ou 'tema diferente'". O critério de conferência é o que a aula ensina, e ele funciona com ou sem busca ligada.

2. **Slides 14, 15 e 26, parâmetros** (B3 aceita, com o texto de A na rodada 2; A5 adaptada). Slide 14: manchete "O treino ajusta os parâmetros"; na tela, "Parâmetros são números ajustados no treino, não textos salvos"; abaixo, "Treino: textos ajustam os números" contra "Uso: sua mensagem passa pelos números e gera a resposta"; número de parâmetros de um modelo aberto com fonte e `[CONFERIR]`. Slide 15: manchete "Sem busca, ela calcula; não consulta". Slide 26, passo 2: "Treino ajusta parâmetros". A analogia da mesa de som sai, porque "liga palavras e ideias" reabre a ideia de arquivo e porque "mesa" já é a metáfora da janela de contexto (slide 22).

3. **Slides 7 a 9, específica e generalista** (B2 adaptada, com a proposta de A na rodada 2). Slide 7: "Específica faz uma; generalista, várias", com rodapé "Generalista = modelo de uso geral; não é IA geral (AGI)". Slide 8: o termo da votação passa a ser "generalista". Slide 9: "Quatro específicas, duas generalistas", repetindo a distinção no gabarito. Prevalece o par que o professor pediu; a manchete do 7 passa um pouco dos ~36 caracteres (39), excesso aceitável para manter o termo dele.

4. **Slide 24, estouro e meio da janela** (A8 adaptada; B6 adaptada). Slide 24 fica só com o limite: "Passou do limite, algo fica de fora", arquétipo `comparacao`, "histórico dentro da mesa: tudo entra" contra "histórico maior que a mesa: partes cortadas ou resumidas, varia por produto `[CONFERIR]`". Novo slide 24B, `claro, médio`, arquétipo `objetos`, manchete "No meio, o dado pode se perder": o mesmo dado posto no início, no meio e no fim de um anexo, com o achado atribuído a Liu et al., 2023, sem curva de atenção desenhada como lei geral. O slide 25 continua respiro, com "salvo se a memória do app estiver ligada; veja as configurações".

**Importantes**

5. **Slide 43, placar S.T.A.R.** (A13 adaptada; B10 adaptada). Dez barras em percentual da nota máxima com nomes e notas do roteiro: Claude Opus 5.5 91,7; Gemini 4 Argon 90,9; Claude Sonnet 5.5 88,7; Muse Wonder 86,8; GPT-6.1 Sol 83,4; GPT-6 Luna 79,4; Muse Spark 1.3 78,0; Gemini 3.8 Flash 77,8; Claude Haiku 5.5 75,5; DeepSeek V4.1 Flash 64,4. Destaque dourado só nos dois primeiros (diferença de 0,8 ponto, que é o que a manchete afirma); as demais em tom neutro. O rodapé longo vira selo legível: "1 prova (PGE-MS 2021) · correção por IA · não é ranking geral"; o detalhe metodológico fica no slide 44. O placar fica na tela porque é o momento memorável preparado pelo professor.

6. **Slide 6 dividido em dois** (A3 adaptada com as correções de B). 6A, `comparacao`, "Regras escritas ou padrões aprendidos": simbólica (regras escritas por pessoas, 1956) contra aprendizado de máquina (padrões tirados dos dados), um exemplo curto em cada lado. 6B, `ramos`, "LLMs nascem dos transformers": aprendizado de máquina → aprendizado profundo → transformers (2017) → LLMs, com 2022 rotulado como lançamento do ChatGPT, não como origem dos LLMs. Observação do juiz: com o 6B, os slides 4 a 10 somam sete sem respiro; quem montar deve conferir a regra de "nunca mais de cinco sem respiro" e, se o tema noite da prática 8 não contar como respiro, inserir um.

7. **Slides 16 a 18, prática de tokens** (B4 aceita, com A6 adaptada pela rodada 2 de B). Slide 16 nomeia o tokenizador e mostra "inconstitucionalidade" e a frase fictícia da prática ("O réu agravou da decisão."). Slide 18, 4 minutos, com duas rotas na tela: "Com internet: abra o QR, cole a frase do slide e conte os blocos. Sem internet: observe na folha impressa como a frase se dividiu". A folha serve para observar, não para contar outra frase. Não prometer os mesmos blocos a quem usar outro tokenizador. Os 2 minutos a mais saem da fala do próprio Bloco 2.

8. **Slide 30, conversa depois da conferência** (A10 adaptada pela rodada 2 de B). Manchete atual mantida. A tela mostra as três categorias possíveis ("número não existe", "existe, mas tema diferente", "número e tema batem"), e o professor pede um relato real de cada categoria que tiver aparecido. Sai "nunca protocole sem abrir o inteiro teor"; o fecho é "conferir continua sendo a regra", que já está no roteiro.

9. **Slides 40 e 41, prática 5** (B9 adaptada). Sobretítulo "Prática 5" e manchete "A sala vota sem ver o nome"; a pergunta da votação passa a ser "qual parece mais pronta?", que preserva a lógica de preferência da arena sem mandar assinar nada. A pergunta de B ("que afirmação exigiria fonte?") vai para a fala do slide 41, ao lado de "você votou por precisão, clareza ou aparência de segurança?", para não estourar os 3 minutos.

10. **Manchetes de práticas e roteiro** (A2 adaptada; refino de B aceito em parte). "Prática N" vira sobretítulo e a manchete afirma o que a sala observa: slide 2, "Entender a IA vem antes de escolher"; slide 8, "Você classifica seis sistemas"; slide 18, "Palavras viram blocos na tela"; slide 20, "O mesmo pedido pode variar"; slide 29, "Você confere se o acórdão existe"; slide 40, conforme o item 9. Ficam como estão a capa (slide 1, título do curso), as aberturas de capítulo (12, 34 e 45, marcadores de seção do arquétipo `abertura`; o 34 é a pergunta do próprio professor) e o slide 42, que já afirma ("Demos a prova da PGE às IAs"; "Dez modelos fizeram a prova" seria impreciso, porque o modelo local também fez).

11. **Slide 8, instrução da prática 1** (A4 aceita, com o termo do item 3). "Onde: na tela do projetor; 1) leia os seis sistemas; 2) ao sinal, levante 1 dedo (específica) ou 2 (generalista); 3) observe a divisão da sala; 4) um voluntário diz a tarefa do filtro de spam e da recomendação; 3 min". Os seis itens ficam visíveis durante toda a votação.

12. **Slide 20, prática 3** (A7 adaptada pela rodada 2 de B). "Onde: app Claude ou ChatGPT no celular; 1) digite e envie 'Complete com uma frase: O juiz julgou o pedido'; 2) toque em 'Nova conversa' no seu app e repita mais duas vezes; 3) anote 'igual' ou 'diferente' e compare com o vizinho; se não encontrar o botão, observe as três tentativas projetadas". O professor grava antes as três tentativas para a projeção; "canto superior" sai porque a posição varia.

13. **Slides 19 e 21, sorteio com pesos** (B5 aceita). Legenda no leque do 19: "probabilidades inventadas para explicar". No 21, duas faixas separadas: "o que vimos no app" e "o mecanismo ilustrado".

14. **Slides 3 e 4, definição** (B1 aceita, com o texto de A na rodada 2). No topo do 3: "Sistema que recebe dados, acha padrões e gera previsões ou conteúdo", com o exemplo "foto da placa → texto da placa". As cinco capacidades passam para a fala, para o slide caber em 45 palavras. No 4, uma linha de síntese sob cada definição, mantendo o PL como projeto.

15. **Slide 37, Legal Index** (A11 aceita). Seis barras rotuladas: conhecimento jurídico 35%, trabalho agêntico 25%, raciocínio 15%, contexto longo 10%, não alucinação 10%, uso de ferramentas 5%, com fonte e `[CONFERIR]`.

16. **Tempo dos Blocos 4 e 5 e grades de modelos** (B11 adaptada). Bloco 4 passa de 24 para 20 minutos e Bloco 5 de 8 para 12. As manchetes dos slides 47 e 48 continuam "Os principais modelos...", porque é o pedido do professor, com rodapé "seleção verificada em [DATA]"; a grade separa visualmente empresa, família de modelos e produto. Nomes, licenças e logos oficiais conferidos antes da aula.

17. **Data de referência** (B12 adaptada). Slide 2 com "Informações verificadas em [DATA]"; a mesma data nos rodapés dos slides 4, 23, 37, 43, 47 e 48, e na abertura da Aula 2. Todo `[CONFERIR]` deve ser resolvido antes do ensaio; o que não for confirmado continua com `[CONFERIR]` na tela, como manda a regra do repositório, em vez de ser simplesmente retirado.

**Opcionais**

18. **Capa, slide 1** (A1 adaptada pela rodada 2 de B). Mantém a foto de tipos móveis e acrescenta, ao lado da palavra composta, três continuações diferentes em texto, desenhadas pelo motor e não pela imagem gerada. A cena liga a capa à previsão do próximo token (slides 19 a 21) sem trocar uma metáfora por outra decorativa.

19. **Slide 46, aberto é ter os pesos** (A14 adaptada pela rodada 2 de B). Na coluna dos abertos: "os pesos podem ser baixados e rodados em servidor próprio, conforme licença, configuração e controles do órgão". Fica a ligação com sigilo sem prometer que ele é automático.

## 4. Rejeitadas

- A9 (slide 29, comando "sem pesquisar na internet"): o pedido não garante que o app deixe de buscar, e a prática já funciona com ou sem busca pelo item 1.
- A12 (slide 42, omitir os corretores Gemma 4): o professor pediu tirar o resultado do Gemma local, não esconder o método, que fica mais auditável nomeado.
- B8 (slide 33, trocar a frase da pior IA): a frase é pedido expresso do professor; na fala, ela entra como tendência e transição rápida, não como segundo clímax.

## 5. Custo

Copiado de `_custo.json` (gerado em 2026-10-22 18:42:22).

| letra | rodada | tokens de entrada | tokens de saída |
|---|---|---|---|
| a | 1 | 4788 | 2484 |
| b | 1 | 4627 | 2467 |
| a | 2 | 6223 | 1488 |
| b | 2 | 7034 | 1397 |

Total: 22672 tokens de entrada, 7836 de saída. Custo estimado: US$ 0,00.
