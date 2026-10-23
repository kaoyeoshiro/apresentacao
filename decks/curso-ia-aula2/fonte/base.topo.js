import {palco, revelar, surgir, tracar, contar, digitar, voar, anotar, caixa, kenburns, escalonar, molaAR, faixa, saida, entradaSaida, clamp, lerp} from '../../motor/palco.js';
import {mundo, conteudo, titulo, fim} from '../../motor/cenas.js';

// Seis blocos da linha do dia, somando 90 minutos. Os ids são os de `bloco` nos slides.
const blocos = [
  {id: 'pedir', rotulo: 'Pedir bem', minutos: 25},
  {id: 'escolhas', rotulo: 'Duas escolhas', minutos: 22},
  {id: 'skills', rotulo: 'Skills', minutos: 8},
  {id: 'pasta', rotulo: 'Na pasta', minutos: 16},
  {id: 'mao', rotulo: 'Mão na massa', minutos: 15},
  {id: 'fecho', rotulo: 'Fecho', minutos: 4},
];

// Uma linha por slide, na ordem da aula. Cada bloco de fonte/ acrescenta as suas com SLIDES.push(...).
// `notas` é o guia do apresentador: {diga, faca, transicao}.
const SLIDES = [];

