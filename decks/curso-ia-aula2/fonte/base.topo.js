import {palco, revelar, surgir, tracar, contar, digitar, voar, anotar, caixa, kenburns, escalonar, molaAR, faixa, saida, entradaSaida, clamp, lerp} from '../../motor/palco.js';
import {mundo, conteudo, titulo, fim} from '../../motor/cenas.js';

// Seis blocos da linha do dia, somando 90 minutos. Os ids são os de `bloco` nos slides.
const blocos = [
  {id: 'pedir', rotulo: 'Pedir bem', minutos: 21},
  {id: 'escolhas', rotulo: 'Três caminhos', minutos: 19},
  {id: 'skills', rotulo: 'Skills', minutos: 8},
  {id: 'pasta', rotulo: 'Na pasta', minutos: 11},
  {id: 'mao', rotulo: 'Mão na massa', minutos: 28},
  {id: 'fecho', rotulo: 'Fecho', minutos: 3},
];

// Uma linha por slide, na ordem da aula. Cada bloco de fonte/ acrescenta as suas com SLIDES.push(...).
// `notas` é o guia do apresentador: {diga, faca, transicao}.
const SLIDES = [];

