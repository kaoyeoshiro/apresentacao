// Bloco A, abertura (4 min): capa, mapa e as quatro peças. Fatos só do briefing.md.
SLIDES.push(
  {id: 'capa', titulo: 'A IA fora do chat', bloco: 'abertura', linhaDia: false, segura: 3,
   notas: {diga: 'Boa tarde. No dia 1 terminamos com uma frase: trabalhe no caso, não no chat. Hoje a IA sai do chat de vez. Ela vai escrever no papel timbrado do escritório, ligar em sistemas, coletar jurisprudência e trabalhar enquanto vocês dormem. Tudo ao vivo, e vocês decidem junto comigo.',
     faca: ['a capa toca sozinha quando o deck abre', 'conferir se a conta do Claude da demonstração está aberta e com o modelo timbrado à mão'],
     transicao: 'O caminho da tarde.'}},
  {id: 'mapa', titulo: 'Hoje, do arquivo ao mundo',
   notas: {diga: 'Cinco etapas. Skills, para a IA fazer do jeito do escritório. MCP e plugins, para ligar a IA a sistemas. O scraper, que coleta jurisprudência em lote. GitHub, onde essas coisas moram. E rotinas, o trabalho agendado. Em cada etapa eu faço ao vivo e vocês têm uma tarefa curta, em dupla, sem precisar de computador.',
     faca: ['mostrar a linha embaixo da tela: ela marca a etapa em que estamos'],
     transicao: 'Antes, as quatro peças que vamos usar.'}},
  {id: 'pecas', titulo: 'Quatro peças em volta do agente', passos: [1.7, 1.2, 1.7, 1.3],
   notas: {diga: 'No centro, o agente, a IA que executa. A skill é o jeito: as instruções de como o escritório faz. O conector é a tomada: liga o agente a um sistema, como o Drive ou o Gmail. O plugin é o pacote: junta skills e conectores e se instala de uma vez. E a rotina é a agenda: o agente trabalha num horário marcado, sem vocês pedirem. A aula de hoje é uma peça de cada vez.',
     faca: ['clique 1: agente e skill', 'clique 2: conector', 'clique 3: o plugin, que embrulha os dois', 'clique 4: a rotina'],
     transicao: 'Começo pela primeira: a skill, no Word.'}},
);
