// ===== Bloco E: futuro e fecho =====
// futuro-cap (respiro), cenarios (ramos), sinais e curso (tempo) e fecho são arquétipos da biblioteca: sem cena própria.

// ritmo: o "5x" sobe, "ao ano" chega ao lado, a caneta dourada sublinha o número; a legenda e a fonte depois.
CENAS.ritmo = (() => {
  const sec = m.secao('ritmo'), q = (s) => sec.querySelector(s);
  const eN = q('.e-num-n'), eU = q('.e-num-u'), eLeg = q('.e-num-leg'), eRod = q('.rodape');
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    surgir(eN, molaAR(x - 0.1), {dy: 50});
    surgir(eU, molaAR(x - 0.35), {dx: -30, dy: 0});
    anotar(eN, saida(faixa(x, 0.7, 1.2)), {forma: 'sublinhado', semente: 9});
    revelar(eLeg, molaAR(x - 0.9));
    revelar(eRod, molaAR(x - 1.3));
    fim(sec, x, 1.4);
  };
})();

// a10 (cena guia): as três faixas do mês entram da esquerda; a linha tracejada de cada uma se estende por último.
CENAS.a10 = (() => {
  const sec = m.secao('a10'), eEt = sec.querySelector('.e-a10-et'), eSem = $$(sec, '.e-sem'), eLin = $$(sec, '.e-linha');
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    revelar(eEt, molaAR(x - 0.15));
    eSem.forEach((el, n) => surgir(el, molaAR(x - 0.3 - n * 0.22), {dx: -24, dy: 0}));
    eLin.forEach((el, n) => { el.style.transform = `scaleX(${saida(faixa(x, 1.0 + n * 0.15, 1.5 + n * 0.15)).toFixed(4)})`; });
    fim(sec, x, 1.6);
  };
})();

// a11 (cena guia): os dois campos sobem, um depois do outro; o pedido da roda por último.
CENAS.a11 = (() => {
  const sec = m.secao('a11'), eCampos = $$(sec, '.e-campo'), eRod = sec.querySelector(':scope > .rodape');
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    eCampos.forEach((el, n) => surgir(el, molaAR(x - 0.2 - n * 0.3), {dy: 30}));
    revelar(eRod, molaAR(x - 0.9));
    fim(sec, x, 1.2);
  };
})();
