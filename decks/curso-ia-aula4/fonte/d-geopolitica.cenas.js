// ===== Bloco D: geopolítica =====
// geo-cap (abertura), cloud-act (ramos) e regras (tempo) são arquétipos da biblioteca: sem cena própria.
// chips: os cartões da base; depois, as duas barras do teto crescem da esquerda, a da China até a metade.
CENAS.chips = (() => {
  const base = cartoes('chips'), sec = m.secao('chips'), dBarras = $$(sec, '.d-barra');
  return (t, c) => {
    base(t, c);
    const x = conteudo(c);
    dBarras.forEach((el, n) => { el.style.transform = `scaleX(${saida(faixa(x, 0.8 + n * 0.35, 1.4 + n * 0.35)).toFixed(4)})`; });
  };
})();
CENAS['aberto-seguro'] = cartoes('aberto-seguro');

// quatro-meses: o "4" sobe, "meses" chega ao lado, a caneta dourada sublinha o número; a legenda e a definição depois.
CENAS['quatro-meses'] = (() => {
  const sec = m.secao('quatro-meses'), q = (s) => sec.querySelector(s);
  const dN = q('.d-num-n'), dU = q('.d-num-u'), dLeg = q('.d-num-leg'), dRod = q('.rodape');
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    surgir(dN, molaAR(x - 0.1), {dy: 50});
    surgir(dU, molaAR(x - 0.35), {dx: -30, dy: 0});
    anotar(dN, saida(faixa(x, 0.7, 1.2)), {forma: 'sublinhado', semente: 4});
    revelar(dLeg, molaAR(x - 0.9));
    revelar(dRod, molaAR(x - 1.3));
    fim(sec, x, 1.4);
  };
})();

// a9 (cena guia): a pergunta do debate; as três perguntas entram uma a uma; os dois lados da sala por último.
CENAS.a9 = (() => {
  const sec = m.secao('a9'), dPerg = sec.querySelector('.d-a9-perg'), dEt = sec.querySelector('.d-a9-et');
  const dLis = $$(sec, '.d-a9-lista li'), dLados = $$(sec, '.d-lado');
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    revelar(dPerg, molaAR(x - 0.15));
    revelar(dEt, molaAR(x - 0.5));
    dLis.forEach((li, n) => surgir(li, molaAR(x - 0.6 - n * 0.2), {dx: -22, dy: 0}));
    dLados.forEach((el, n) => surgir(el, molaAR(x - 1.3 - n * 0.15), {dx: 22, dy: 0}));
    fim(sec, x, 1.6);
  };
})();
