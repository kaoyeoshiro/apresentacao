import {palco, revelar, surgir, tracar, contar, digitar, voar, anotar, caixa, kenburns, escalonar, molaAR, faixa, saida, entradaSaida, clamp, lerp} from '../../motor/palco.js';
import {mundo, conteudo, titulo, fim} from '../../motor/cenas.js';

// 6 blocos da linha do dia, somando 90 minutos. Os ids são os de `bloco` nos slides.
const blocos = [
  {id: 'abertura', rotulo: 'Abertura', minutos: 4},
  {id: 'skills', rotulo: 'Skills e Word', minutos: 26},
  {id: 'mcp', rotulo: 'MCP e plugins', minutos: 16},
  {id: 'scraper', rotulo: 'Scraper', minutos: 20},
  {id: 'github', rotulo: 'GitHub', minutos: 7},
  {id: 'rotinas', rotulo: 'Rotinas', minutos: 17},
];

// Uma linha por slide, na ordem da aula. Cada bloco de fonte/ acrescenta as suas com SLIDES.push(...).
// `notas` é o guia do apresentador: {diga, faca, transicao}.
const SLIDES = [];

