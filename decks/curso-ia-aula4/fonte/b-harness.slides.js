// Bloco B, harness (6 min): o sistema em volta do modelo, o vídeo dos dez agentes e o custo de cada um. Fatos só do
// briefing.md e da ficha docs/pesquisa/dia2-harness-quatilex.md (print de 05/11/2026).
SLIDES.push(
  {id: 'harness-cap', titulo: 'O sistema em volta do modelo', bloco: 'harness', andamento: 'capitulo', linhaDia: false,
   notas: {diga: 'Até aqui, um assistente sozinho. Agora, o que fica em volta do modelo: o harness. É o sistema que divide o trabalho entre vários agentes, cada um com um modelo. Vou mostrar uma peça da PGE-MS por dentro. Falo da experiência de quem trabalha lá; a co.juris não fala em nome da PGE-MS.',
     faca: ['bloco curto, de 6 minutos: o vídeo e o custo de cada agente', 'apontar o aviso do rodapé'],
     transicao: 'Uma peça, dez agentes.'}},
  {id: 'harness', titulo: 'Dez agentes, uma peça', video: [0.9, 39.5], ritmoOk: 'vídeo de 40 s, narrado pelo professor',
   notas: {diga: 'Esta é uma peça real, gerada no quatilex, sem nenhum dado de processo. Dez agentes e seis modelos trabalharam nela. Primeiro, o classificador lê os autos e decide o tipo do caso. Dois leitores baratos leem os autos ao mesmo tempo e listam argumentos e fatos, com a fonte. O agrupador junta o que os dois disseram igual. Aí entra o redator, com o Claude Opus 5.5, que escreve a peça e confere nos autos. Dois validadores checam os julgados e os artigos de lei citados. Por último, um agente confere se a peça afirma um ofício que não foi expedido. Doutrina e jurisprudência são ferramentas de busca que os leitores e o redator chamam.',
     faca: ['o vídeo toca sozinho na moldura; não há nada ao vivo neste slide',
       'o vídeo tem 40 s; falar por cima dele, na ordem em que os agentes aparecem',
       'os números valem para esta peça, não para a média do sistema'],
     transicao: 'E quanto custou cada um?'}},
  {id: 'redator', titulo: 'O caro só onde faz diferença', passos: [3.2],
   notas: {diga: 'A peça inteira custou US$ 1,59. Só o redator, com o modelo caro, custou US$ 1,39: 87% da conta. Os outros nove, somados, custaram US$ 0,21. O modelo caro fica onde a qualidade decide, na escrita. Ler, classificar, buscar e conferir vão para modelos baratos. É isso que um bom harness faz.',
     faca: ['apontar a barra dourada do redator e depois as nove barras finas', 'lembrar: números de uma peça, do print de 05/11/2026'],
     transicao: 'Custo por peça é uma conta. Quem paga a conta inteira é outra história.'}},
);
