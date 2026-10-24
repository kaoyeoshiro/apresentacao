
// Bloco C, skills (8 min): skill, onde, liga.
SLIDES.push(
  {id: 'skills', titulo: 'Escreva o seu jeito uma vez', bloco: 'skills', linhaDia: false,
   notas: {diga: 'Falta uma peça. Até aqui o pedido foi bom e a pasta guardou os papéis. Mas você repete o mesmo jeito de fazer toda vez. A skill é a forma de escrever esse jeito uma vez.',
     faca: ['oito minutos neste bloco, seis de aula e dois de perguntas: não deixar virar aula de programação'], transicao: 'Como é uma skill por dentro.'}},
  {id: 'skill', titulo: 'Skill é o seu jeito de fazer, escrito uma vez', passos: [2.4, 2.3],
   notas: {diga: 'Skill é uma pasta com um arquivo, o SKILL.md. Em cima vêm o nome e a descrição, e a descrição diz quando usar. O modelo só lê essas duas linhas até decidir abrir a skill; por isso ela custa pouco contexto. Embaixo ficam as instruções: o seu jeito de fazer, escrito uma vez. Reparem na linha 8. É a regra do "se não souber, diga", agora guardada num arquivo.',
     faca: ['clique 1: o cabeçalho; aponte o nome e a descrição', 'clique 2: o editor rola até as instruções; leia em voz alta a linha "não encontrei nos documentos"', 'avise: esta é a skill que roda daqui a pouco, na demonstração'],
     transicao: 'E esse mesmo arquivo serve nos dois apps.'}},
  {id: 'onde', titulo: 'O mesmo arquivo nos dois',
   notas: {diga: 'A skill segue um padrão aberto. O mesmo SKILL.md serve ao Claude e ao ChatGPT e Codex; muda só a pasta onde ele mora e o jeito de chamar. No Claude, a pasta é .claude/skills e a chamada é barra com o nome. No Codex, .agents/skills e cifrão; no ChatGPT, arroba. No app desktop do ChatGPT, o menu Skills lista as suas.',
     faca: ['aponte o fim dos dois caminhos: o arquivo é o mesmo, SKILL.md', 'prática de skill: dia 2'],
     transicao: 'A skill é uma das peças que ligam o agente ao mundo. Há mais duas.'}},
  {id: 'liga', titulo: 'O que liga o agente ao mundo', passos: [1.7, 1.2, 1.7],
   notas: {diga: 'No centro, o agente. A skill é o jeito: instruções que ele segue quando a tarefa pede. O MCP é a tomada: um padrão aberto para ligar o agente a ferramentas e sistemas externos. O plugin é o pacote: junta skills e, se quiser, conexões MCP, e se instala de uma vez. Plugin e MCP na prática ficam para o dia 2.',
     faca: ['clique 1: agente e skill', 'clique 2: MCP', 'clique 3: o plugin, que embrulha os dois'],
     transicao: 'E uma skill não precisa nascer grande.'}},
  {id: 'cresce', titulo: 'Comece pequeno. Deixe crescer.', passos: [1.6, 1.4, 1.8],
   notas: {diga: 'Não comecem pelo sistema. Comecem por uma skill pequena, de uma página, para uma coisa que vocês repetem toda semana. Quando ela falhar num caso, vocês acrescentam uma regra. Com o tempo ela cresce. A minha, de gerar peças, chegou a ter uma skill de 215 linhas que manda ler 71 arquivos de instruções, cerca de 342 mil palavras. Tem camadas condicionais, como um motor de regras: primeiro verifica se os documentos existem e aborta se faltar algum. Depois olha a ação e o tipo de peça, são dez tipos. Depois carrega a matéria, saúde ou Detran, com os temas e os precedentes vigentes daquela matéria. No fim, confere 15 regras que reprovam a peça se violadas. Nada disso nasceu pronto. Comecem pequeno.',
     faca: ['primeiro clique: a skill de uma página', 'segundo clique: dez, vinte regras', 'terceiro clique: o sistema interno; dizer os números com calma', 'números medidos em 24/10/2026 no projeto Automacao_Total: 6 skills, 94 arquivos de instruções (71 só na geração de peça), saúde com 34 arquivos e Detran com 23'],
     transicao: 'Agora, a pasta do caso que vamos usar.'}},
);
