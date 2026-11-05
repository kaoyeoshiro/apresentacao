import {palco, revelar, surgir, tracar, contar, digitar, voar, anotar, caixa, kenburns, escalonar, molaAR, faixa, saida, entradaSaida, clamp, lerp} from '../../motor/palco.js';
import {mundo, conteudo, titulo, fim} from '../../motor/cenas.js';

// 5 blocos da linha do dia, somando 90 minutos. Os ids são os de `bloco` nos slides.
const blocos = [
  {id: 'assistentes', rotulo: 'Assistentes', minutos: 27},
  {id: 'harness', rotulo: 'Harness', minutos: 6},
  {id: 'conta', rotulo: 'Quem paga', minutos: 23},
  {id: 'geopolitica', rotulo: 'Geopolítica', minutos: 18},
  {id: 'futuro', rotulo: 'Futuro', minutos: 16},
];

// Uma linha por slide, na ordem da aula. Cada bloco de fonte/ acrescenta as suas com SLIDES.push(...).
// `notas` é o guia do apresentador: {diga, faca, transicao}.
const SLIDES = [];

