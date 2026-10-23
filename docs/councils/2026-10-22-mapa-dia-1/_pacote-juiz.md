# Pacote do juiz

Data: 2026-10-22
Revisores ativos: 2
Ausentes: 0
Rodadas executadas: 2

Os revisores aparecem apenas por letra. A identidade de quem escreveu cada parecer não está neste pacote e não deve ser inferida.

Todas as rodadas executadas estão abaixo, por revisor e em ordem. As rodadas anteriores são contexto: nelas está o texto das sugestões que a última rodada cita por código.

## Contexto

# Contexto

O alvo é o mapa (blocos, minutos e práticas) do primeiro dia de um curso pago de IA da co.juris: duas aulas de cerca
de 90 minutos cada, no mesmo dia. O professor é procurador do Estado e usa IA intensamente no trabalho. Os slides
serão gerados depois a partir deste mapa, num motor de apresentação próprio (um clique por slide, imagens geradas,
vídeo de demonstração). Um segundo dia, fora deste mapa, tratará de MCP, plugins, rotinas, raspagem de
jurisprudência do TJMS e do STF, casos práticos, artefatos e devolutiva dos alunos.

Turma: advogados, uma desembargadora, servidores e assessores; muitos sem plano pago de IA. Antes do curso, o
professor manda mensagem no WhatsApp pedindo que todos instalem o app do Claude e o do ChatGPT. Prática no formato
misto: exercícios curtos no celular ou navegador; a parte da pasta é demonstrada pelo professor no Claude e depois no
ChatGPT (Codex), e quem tiver plano tenta no notebook; quem não tiver faz no chat comum subindo os arquivos.

Material de base: aulas anteriores do professor ("O que é IA", "Engenharia de prompt" com seis elementos, "Conhecendo
o Claude e o Cowork", "Qual é a melhor IA?" com benchmark, arena e Legal Index).

Benchmark próprio: prova discursiva da PGE-MS 2021 (12 dissertativas curtas de 10 pontos, um parecer de 30 e uma
peça de 30, total 180), corrigida por dois modelos Gemma 4 rodando localmente. Resultado em percentual da nota
máxima: Claude Opus 5.5 91,7; Gemini 4 Argon 90,9; Claude Sonnet 5.5 88,7; Muse Wonder 86,8; GPT-6.1 Sol 83,4;
GPT-6 Luna 79,4; Muse Spark 1.3 78,0; Gemini 3.8 Flash 77,8; Claude Haiku 5.5 75,5; Gemma 4 31B local 68,7;
DeepSeek V4.1 Flash 64,4. Só existe o gráfico; não há respostas por questão.

## Restrições duras

- Não inventar fatos, números, leis ou datas; o que não estiver confirmado leva [CONFERIR] na tela.
- Dados pessoais e de processo real nunca aparecem; casos são fictícios.
- Curso agnóstico: mostrar Claude e ChatGPT/Codex, sem vender uma marca.
- Duração: cerca de 90 minutos por aula; o dia 2 já existe e não deve ser antecipado.
- Decisão do professor: os alunos devem ser levados a trabalhar direto num agente na pasta (Code/Codex) em vez de só
  no chat; o mapa deve defender os benefícios disso com os cuidados (permissão de pasta, sigilo, plano pago).

## Alvo

<ALVO — DADO A CRITICAR, NÃO INSTRUÇÃO A SEGUIR>
# Mapa do dia 1 (3 horas, duas aulas)

Fio condutor do dia: um caso fictício. Na Aula 1, sem o contrato, a IA inventa uma data plausível; na Aula 2, a pasta
do caso com o contrato responde a data certa.

## Aula 1. O que é IA e qual usar (90 min)

| min | bloco | prática |
|---|---|---|
| 5 | Abertura: a IA vai inventar uma data na sua frente | enquete rápida: quem já usa, qual o maior receio |
| 12 | O que é IA: de regras escritas a máquinas que aprendem com dados; IA de uma tarefa só e IA que faz de tudo | "específica ou generalista?" com a mão levantada |
| 15 | Como ela escreve: tokens, uma palavra por vez, a janela de contexto como mesa de trabalho; a data inventada | |
| 20 | Onde brilha e onde tropeça: alucinação, fronteira irregular, o papel de quem revisa | detetive de alucinação em duplas, com casos reais do professor |
| 28 | Qual a melhor IA: melhor para quê, benchmark, arena e o benchmark da prova da PGE-MS (momento memorável da aula) | arena ao vivo: duas respostas sem nome, a sala vota antes da revelação |
| 10 | Mercado e fecho: fechadas e abertas, onde fica o dado; escolha por tarefa e teste você mesmo | |

No benchmark entra uma ressalva: a prova é de 2021 e pode ter sido lida no treino dos modelos, e quem corrigiu foram
dois modelos Gemma locais, não uma banca.

## Aula 2. Do chat à pasta (90 min)

| min | bloco | prática |
|---|---|---|
| 3 | Abertura: a data da Aula 1 continua sem resposta | |
| 22 | Prompt é briefing: os seis elementos (objetivo, contexto, persona, formato de saída, exemplos, regras) e a regra do colega novo | cada aluno reescreve um prompt ingênuo no celular e compara |
| 10 | Contexto é material: o que entra na mesa, o que se perde no meio | |
| 5 | Onde o chat para: copiar e colar, esquecer tudo, devolver texto em vez de arquivo | |
| 10 | O que é agente: pede, planeja, você aprova, ele age, entrega | |
| 10 | Por que usar o Code para tudo: o caso inteiro na pasta, lê dezenas de documentos, entrega Word e PDF, skill e memória que duram, cada afirmação conferível no arquivo; cuidados: permissão de pasta, sigilo, plano pago | |
| 15 | Demonstração: a mesma pasta de caso fictício no Claude e depois no Codex, com skill e memória; a data é respondida pelo contrato | |
| 12 | Mão na massa: a pasta do exercício vai pelo WhatsApp | com plano, no Code ou Codex; sem plano, no chat com upload |
| 3 | Fecho: o que fazer amanhã e o que vem no segundo dia | |
</ALVO>

## Pareceres

## Revisor A, rodada 1

1 · Fio condutor: “a IA inventa uma data” · importante · O roteiro depende de o modelo errar; se ele responder que não sabe, o efeito planejado desaparece. · Trocar por: “Sem o contrato, peça a data e observe se a IA admite a falta de informação ou arrisca uma resposta; com o contrato, exija a data e o trecho que a sustenta.” · alta

2 · Aula 1, “detetive de alucinação […] com casos reais do professor” · crítica · Isso contraria a regra de usar apenas casos fictícios e pode trazer dados identificáveis para a sala. · Preparar dois excertos inteiramente fictícios, com fonte e resposta impressas ou em slide; as duplas marcam o que a fonte sustenta, contradiz ou não permite concluir. · alta

3 · Aula 1, “qual a melhor IA”, benchmark e arena · importante · O gráfico é um bom ponto alto, mas não permite examinar respostas por questão; a votação da arena pode parecer uma validação da classificação da PGE-MS sem sê-lo. · Apresentar o gráfico como **resultado deste teste**, declarar na tela “sem respostas por questão; correção por modelos, não por banca; possível presença da prova no treinamento [CONFERIR]” e fazer a arena com duas respostas preparadas para *outro* problema fictício, avaliadas por critérios anunciados antes do voto. · alta

4 · Aula 1, sequência de 12 + 15 + 20 minutos antes do benchmark · importante · Há muita exposição seguida para uma tarde de três horas; a primeira prática substantiva chega tarde. · Redistribuir os seis blocos para **5 / 10 / 10 / 17 / 38 / 10 minutos**. Usar os minutos ganhos no benchmark para votação, revelação dos critérios e discussão do que o gráfico não prova. · alta

5 · Aula 2, “Prompt é briefing: os seis elementos” (22 min) · importante · Uma recapitulação longa retarda a virada prometida para a pasta, sobretudo porque há aula anterior sobre prompts. · Reduzir a 14 minutos: mostrar um briefing de três linhas, dar quatro minutos para reescrita e comparar duas versões. Manter os seis elementos como checklist de consulta, não como seis explicações sucessivas. · alta

6 · Aula 2, “Onde o chat para” e “Por que usar o Code para tudo” · crítica · O contraste é absoluto demais: chat também aceita arquivos, e nem toda tarefa justifica acesso a uma pasta. Isso enfraquece a neutralidade e a justificativa da mudança. · Substituir por: “Use chat para uma pergunta ou documento delimitado; experimente um agente na pasta quando a tarefa envolver vários arquivos e revisões. Autorize apenas a pasta fictícia do exercício e confira o que ele leu, alterou e produziu.” · alta

7 · Aula 2, “entrega Word e PDF, skill e memória que duram, cada afirmação conferível no arquivo” · importante · São promessas diferentes comprimidas num bloco de dez minutos; citar um arquivo também não torna uma afirmação automaticamente correta. · Demonstrar **um** resultado: localizar a data no contrato e produzir uma nota curta com nome do arquivo e trecho de apoio, conferidos pelo professor na tela. Deixar Word/PDF, skill e memória como possibilidades mencionadas brevemente, sem configurá-las na demonstração. · alta

8 · Aula 2, “15 min: […] Claude e depois no Codex, com skill e memória” · crítica · Duas execuções completas, troca de ferramenta e eventual ajuste de acesso deixam pouco tempo para mostrar o que importa: a passagem da pergunta à evidência no contrato. · Reservar 20 minutos: executar o mesmo pedido na pasta fictícia em uma ferramenta; na outra, mostrar o pedido equivalente e o resultado previamente preparado. Ter capturas ou vídeo de reserva se acesso ou rede falharem. · alta

9 · Aula 2, “12 min: a pasta do exercício vai pelo WhatsApp” · crítica · Distribuir arquivos durante o exercício consome a prática e torna desigual a participação de quem está no celular ou sem plano. · Enviar antes da aula um pacote fictício pequeno e uma folha única com o pedido: “Encontre a data contratual; indique arquivo e trecho; se não localizar, diga que não localizou.” Deixar também QR code e cópia local para o dia; dar 20 minutos de prática, com upload no chat como percurso igualmente válido. · alta

10 · Aula 2, ritmo e fecho · importante · Os nove blocos somam 90 minutos sem margem para transições, dúvidas ou falha de rede. · Adotar a distribuição **4 / 14 / 7 / 5 / 8 / 8 / 20 / 20 / 4 minutos**. Encerrar pedindo que cada participante registre uma resposta, sua fonte e uma verificação humana pendente — um produto que serve à advocacia, à magistratura, à assessoria e ao serviço público. · alta

## Revisor A, rodada 2

1 · **MANTENHO** — Os “casos reais do professor” contrariam a restrição de não exibir dados de processo real. A prática deve usar apenas trechos integralmente fictícios, incluindo um trecho correto para que a turma não passe a tratar toda resposta como erro.

2 · **REFINO** — A sequência expositiva de 35 minutos é longa, mas a redistribuição precisa preservar a explicação da virada. Texto novo: `15 min: limite do chat e conceito de agente, com uma ação curta na tela; 25 min: demonstração da pasta, explicando skill e memória quando aparecerem; 22 min: prática`. Os 20 minutos vêm dos quatro blocos hoje somados em 35.

3 · **REFINO** — Entregar três PDFs por WhatsApp ou exigir três uploads ainda pode consumir a prática em suporte técnico. Texto novo: `Enviar antes da aula um link e QR Code para um único arquivo leve com o caso fictício; manter cópia projetada. Todos fazem a auditoria no chat, por upload ou texto copiado; quem já tiver agente configurado compara com a execução na pasta`. Não prometer Word a toda a turma.

4 · **REFINO** — Uma data encontrada em um contrato não demonstra a vantagem da pasta; oito documentos, discussão de prescrição e `.docx` no padrão do gabinete tornam o clímax pesado demais. Texto novo: `O agente cruza três arquivos fictícios, produz uma cronologia com indicação da fonte de cada data e salva uma minuta na pasta; o chat recebe os mesmos arquivos para comparação`. A conclusão jurídica fica para revisão humana.

5 · **MANTENHO** — Enxugar os 27 minutos iniciais abre espaço para a turma fazer algo antes do benchmark. O foco proposto — resposta plausível não é prova, e contexto tem limites — prepara tanto o exercício de alucinação quanto a Aula 2.

6 · **MANTENHO** — Quinze minutos não comportam duas execuções completas e explicações de skill e memória. Uma execução principal, uma comparação breve na outra ferramenta e vídeo de reserva protegem o ponto alto sem transformar neutralidade em duas demonstrações redundantes.

7 · **REFINO** — O gráfico precisa de interpretação, mas os “três achados” propostos extrapolam o que ele permite concluir: não há base para afirmar empate estatístico, efeito de plano/modelo rápido ou teto dos modelos locais. Texto novo: `Arena com respostas previamente preparadas e identificadas como exercício independente; depois, gráfico, método de correção e limites: prova possivelmente conhecida pelos modelos, correção por modelos locais e ausência das respostas por questão. Notas não equivalem a desempenho no trabalho`. Não vincular o voto da arena às notas sem usar as mesmas respostas.

8 · **REFINO** — O cuidado deve vir antes de abrir a pasta, mas o semáforo sugerido dá falsa segurança: plano pago e treino desativado não autorizam, por si, inserir dados de clientes ou processos. Texto novo: `Nesta aula, só arquivos fictícios. No trabalho, verificar regras institucionais e condições da ferramenta antes de qualquer uso de dados; dar ao agente acesso apenas à subpasta necessária e revisar ações de edição ou exclusão`.

9 · **REFINO** — Reduzir a digitação no celular é correto. Retirar, porém, a promessa de que persona, formato e exemplos serão salvos “de forma permanente”: isso depende da configuração. Texto novo: `Reescreva objetivo, contexto mínimo e regra de não inventar. Na demonstração, veja como instruções reutilizáveis podem reduzir repetição — e o que ainda precisa ser conferido a cada tarefa`.

## Revisor B, rodada 1

1 · Aula 1: "detetive de alucinação em duplas, com casos reais do professor" (20 min) · crítica · Viola diretamente a restrição dura de anonimato ("Dados pessoais e de processo real nunca aparecem; casos são fictícios") e expõe um procurador do Estado a risco disciplinar diante de uma desembargadora e advogados. · Substituir na coluna prática por: `detetive de alucinação em duplas, com 3 trechos de peças de casos 100% fictícios inspirados na rotina pública (um com jurisprudência inventada, um com inversão fática sutil e um correto para controle)`. · alta

2 · Aula 2: blocos entre o min 25 e o min 60 ("Contexto é material", "Onde o chat para", "O que é agente", "Por que usar o Code para tudo") · crítica · São 35 minutos ininterruptos de exposição teórica na segunda metade de uma tarde de 3 horas; a turma vai dispersar antes do ponto alto da aula, e os conceitos de agente, skill e memória no vazio soam abstratos para quem não programa. · Fundir os 4 blocos em 15 min de transição prática ("O gargalo do chat e a virada para a pasta") e transferir 20 min para a Demonstração (que sobe para 25 min, absorvendo a explicação de agente, skill e memória enquanto eles aparecem na tela) e para a prática final (que sobe para 22 min). · alta

3 · Aula 2: "Mão na massa: a pasta do exercício vai pelo WhatsApp | com plano, no Code ou Codex; sem plano, no chat com upload" (12 min) · crítica · Em 12 minutos na rede de sala de aula, baixar arquivo do WhatsApp Web, descompactar, abrir agente na pasta (ou subir múltiplos arquivos no celular) vai consumir o tempo inteiro em suporte técnico e frustrar quem não tem plano pago. · Entregar os arquivos em link aberto (sem login nem `.zip`, ex.: pasta pública ou QR Code direto) já no intervalo entre as aulas, com 3 arquivos PDF leves (petição, contrato, certidão), e alterar a prática (agora com 22 min) para: `Todos rodam o mesmo prompt de auditoria fática no chat com upload dos 3 PDFs (no celular ou PC); quem já tiver Code/Codex configurado roda na pasta local para comparar o tempo e a entrega já em arquivo Word`. · alta

4 · Fio condutor do dia ("Na Aula 1, sem o contrato, a IA inventa uma data plausível; na Aula 2, a pasta do caso com o contrato responde a data certa") · importante · Achar uma data num contrato não justifica migrar do chat gratuito para um agente pago na pasta (Code/Codex), pois um `Ctrl+F` no PDF ou o upload de um único arquivo no chat gratuito resolve isso em 5 segundos. · Mudar o desafio do fio condutor para uma tarefa que o chat comum faz mal e a pasta faz bem: `Na Aula 1, sem os autos, a IA inventa a data da notificação e erra a prescrição; na Aula 2, o agente varre uma pasta com 8 documentos (contrato, 3 aditivos, notificações e planilha), cruza as datas, monta o quadro cronológico com referência ao arquivo/página e gera a minuta de preliminar em .docx no padrão do gabinete`. · alta

5 · Aula 1: "O que é IA: de regras escritas a máquinas que aprendem com dados..." (12 min) e "Como ela escreve: tokens..." (15 min) · importante · Gastar 27 minutos (quase um terço da Aula 1) com história da IA simbólica vs. aprendizado de máquina e mecânica de tokens atrasa o ganho prático e soa escolar para magistrados e advogados seniores. · Enxugar a soma dos dois blocos para 15 minutos focados exclusivamente em: `(1) Máquina de probabilidade, não banco de dados de consulta (por que ela mente com convicção); (2) Janela de contexto como mesa de trabalho (por que não cabe o processo inteiro de qualquer jeito)`. · alta

6 · Aula 2: "Demonstração: a mesma pasta de caso fictício no Claude e depois no Codex..." (15 min) · importante · Fazer duas demonstrações completas ao vivo no Claude e no Codex, mostrando criação de arquivo, skill e memória, não cabe em 15 minutos e está sujeito a falha de rede ou lentidão de API na frente da turma. · Subir o bloco para 25 minutos (com o tempo ganho na sugestão 2), rodar o fluxo completo ao vivo em uma ferramenta (ex.: Claude), mostrar na segunda (Codex) apenas a execução equivalente lado a lado, e manter vídeo gravado de backup no motor de slides pronto para disparo em um clique se a rede oscilar. · alta

7 · Aula 1: "Qual a melhor IA... benchmark da prova da PGE-MS (momento memorável da aula)" (28 min) · importante · Como só existe o gráfico das notas gerais e não há as respostas por questão, passar 28 minutos num gráfico estático esvazia o clímax se o professor não traduzir o que significam os números (ex.: Claude Opus 5.5 com 91,7% contra Gemma 4 31B local com 68,7%) na decisão de bolso do aluno. · Estruturar o bloco em três atos claros: `10 min para a Arena ao vivo (com uma questão real da prova PGE-MS 2021 gerada antes da aula por dois modelos do gráfico); 10 min para revelar o gráfico da PGE-MS destacando 3 achados práticos (topo empatado entre marcas, salto entre modelo gratuito/rápido e modelo de raciocínio, e o teto atual de modelos locais para sigilo extremo); 8 min para as ressalvas metodológicas (possível contaminação da prova de 2021 no treino e correção automatizada por dois Gemma 4 locais, não pela banca oficial)`. · alta

8 · Aula 1: "Mercado e fecho: fechadas e abertas, onde fica o dado..." (10 min) e Aula 2: "...cuidados: permissão de pasta, sigilo, plano pago" (10 min) · importante · Sigilo, treino com dados do usuário e governança aparecem quebrados em dois finais de bloco, tratando como detalhe técnico o que é a maior barreira institucional para uma desembargadora, procuradores e advogados. · Unificar o tema num quadro objetivo na Aula 2 logo antes da demonstração da pasta: `Regra do semáforo para o Direito: (1) Conta gratuita = dado público (não subir minuta nem peça com partes); (2) Conta paga com treino desativado no painel = uso controlado; (3) Agente na pasta (Code/Codex) = nunca apontar para a pasta raiz "Meus Documentos" ou drive inteiro do escritório, criar sempre uma subpasta isolada por caso e aprovar comandos de exclusão/edição`. · alta

9 · Aula 2: "Prompt é briefing: os seis elementos (objetivo, contexto, persona, formato de saída, exemplos, regras)... cada aluno reescreve um prompt ingênuo no celular" (22 min) · opcional · Digitar seis elementos de prompt no teclado do celular demora, gera fadiga física e contradiz a tese da segunda metade da aula (de que na pasta as skills e a memória guardam persona, formato, exemplos e regras para o usuário não ter que digitar tudo toda vez). · Na prática do celular, pedir que o aluno reescreva apenas 3 elementos essenciais (`Objetivo, Contexto fático mínimo e Regras de contenção/não inventar`), deixando explícito: `"Os outros 3 elementos (Persona, Formato e Exemplos) vocês não vão digitar no dia a dia: vamos salvá-los de forma permanente na pasta como Skill e Memória daqui a 20 minutos"`. · alta

## Revisor B, rodada 2

1 · Fio condutor: “a IA inventa uma data” · importante · **MANTENHO** · Modelos em outubro de 2026 frequentemente recusam responder sem a fonte; ancorar a abertura numa alucinação garantida ao vivo arrisca quebrar a narrativa nos primeiros cinco minutos se o modelo admitir que não sabe. · Trocar por: “Sem o contrato, peça a data e observe se a IA admite a falta de informação ou arrisca uma resposta; com o contrato, exija a data e o trecho que a sustenta.” · alta

2 · Aula 1, “detetive de alucinação […] com casos reais do professor” · crítica · **MANTENHO** · O uso de casos reais viola frontalmente a restrição dura de anonimato e sigilo do curso, além de expor o procurador e a turma a riscos éticos desnecessários. · Preparar dois excertos inteiramente fictícios, com fonte e resposta impressas ou em slide; as duplas marcam o que a fonte sustenta, contradiz ou não permite concluir. · alta

3 · Aula 1, “qual a melhor IA”, benchmark e arena · importante · **REFINO** · O Revisor A acerta ao desvincular a arena da prova da PGE-MS (já que não há respostas por questão), mas o marcador `[CONFERIR]` sobre contaminação de dados deve ser uma afirmação metodológica direta, pois 2021 certamente está na janela de treino de modelos de 2026. · Apresentar o gráfico declarando na tela: “limites: sem respostas por questão; correção por 2 modelos Gemma 4 locais, não por banca; prova de 2021 sujeita a contaminação de treino”. Fazer a arena com duas respostas preparadas para o caso fictício do curso, votando com critérios prévios. · alta

4 · Aula 1, sequência de 12 + 15 + 20 minutos antes do benchmark · importante · **MANTENHO** · Quarenta e sete minutos até o fim da primeira prática substantiva cansam uma turma jurídica heterogênea; encurtar a teoria inicial dá fôlego ao ponto alto do benchmark e à arena ao vivo. · Redistribuir os seis blocos para **5 / 10 / 10 / 17 / 38 / 10 minutos**, usando o tempo ganho no bloco 5 para votação, revelação dos critérios e debate metodológico. · alta

5 · Aula 2, “Prompt é briefing: os seis elementos” (22 min) · importante · **MANTENHO** · Gastar 22 minutos em engenharia de prompt básica atrasa o diferencial do curso (trabalhar na pasta) e repete material que já é de base, tirando tempo da prática final. · Reduzir a 14 minutos: mostrar um briefing de três linhas, dar quatro minutos para reescrita no celular e comparar duas versões, deixando os seis elementos apenas como checklist visual de apoio. · alta

6 · Aula 2, “Onde o chat para” e “Por que usar o Code para tudo” · crítica · **REFINO** · O Revisor A viu bem o exagero ("chat também aceita arquivos"), mas sua proposta suaviza demais a decisão explícita do professor de levar os alunos a trabalhar direto num agente na pasta. · Substituir por: “Onde o chat dá trabalho (subir arquivos a cada sessão, perder histórico, não editar direto na árvore de pastas) vs. Por que adotar o agente na pasta como padrão (lê o diretório do caso, aplica skills fixas e gera o documento final local), exigindo pasta isolada por sigilo e plano pago.” · alta

7 · Aula 2, “entrega Word e PDF, skill e memória que duram, cada afirmação conferível no arquivo” · importante · **REFINO** · Enxugar a promessa de 10 minutos é essencial, mas descartar a demonstração de *skill* e *memória* esvazia exatamente a vantagem estrutural do agente de pasta sobre o upload avulso no chat comum. · Manter a geração de nota curta com citação do arquivo e trecho da data, mas demonstrar isso acionando uma *skill* pronta na pasta (ex.: `/checar-prazos`) e um arquivo de memória pré-configurado, sem gastar tempo criando-os do zero. · alta

8 · Aula 2, “15 min: […] Claude e depois no Codex, com skill e memória” · crítica · **MANTENHO** · Quinze minutos para rodar dois agentes ao vivo, alternar janelas e explicar resultados é inviável e sujeito a falhas técnicas; fazer um ao vivo e mostrar o outro pré-gravado garante o agnosticismo sem estourar o relógio. · Reservar 20 minutos: executar o pedido ao vivo em uma ferramenta; na outra, exibir o comando equivalente e o resultado previamente preparado (ou em vídeo curto), mantendo capturas de tela como reserva de rede. · alta

9 · Aula 2, “12 min: a pasta do exercício vai pelo WhatsApp” · crítica · **MANTENHO** · Baixar e descompactar pastas pelo WhatsApp na hora do exercício, em rede de sala de aula e em celulares, vai consumir os 12 minutos inteiros em suporte técnico. · Enviar o pacote fictício antes da aula (junto com o aviso de instalação dos apps), disponibilizar QR code em tela no dia e ampliar a prática para 20 minutos, validando o upload no chat gratuito para quem está no celular ou sem plano. · alta

10 · Aula 2, ritmo e fecho · importante · **MANTENHO** · A redistribuição de minutos acomoda o tempo real de transição e prática, e o fecho focado em verificação humana atende da desembargadora ao assessor sem infantilizar. · Adotar a distribuição **4 / 14 / 7 / 5 / 8 / 8 / 20 / 20 / 4 minutos** e encerrar exigindo de cada aluno o registro da resposta, da fonte exata no contrato e de um ponto de verificação humana. · alta
