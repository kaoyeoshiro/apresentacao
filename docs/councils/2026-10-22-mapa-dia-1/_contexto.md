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
