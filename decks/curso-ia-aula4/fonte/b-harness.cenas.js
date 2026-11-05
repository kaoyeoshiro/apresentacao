// ===== Bloco B: harness =====
// harness-cap (abertura) e harness (demonstracao) são arquétipos da biblioteca; redator é cena própria.

// redator: as linhas entram em onda; os trilhos crescem juntos, na mesma escala (o do redator é o inteiro); por fim,
// o 87% conta.
CENAS.redator = (() => {
  const sec = m.secao('redator'), bCab = sec.querySelector('.b-cab'), bLns = $$(sec, '.b-ln');
  const bTrs = bLns.map((ln) => ln.querySelector('.b-t i')), bMax = Math.max(...bLns.map((ln) => +ln.dataset.v));
  bLns.forEach((ln, n) => { bTrs[n].style.width = `${(100 * +ln.dataset.v / bMax).toFixed(3)}%`; });
  const bPct = sec.querySelector('.b-pct'), bPctN = sec.querySelector('.b-pct-n'), bPctLeg = sec.querySelector('.b-pct-leg');
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    revelar(bCab, molaAR(x - 0.1));
    bLns.forEach((ln, n) => surgir(ln, molaAR(x - 0.2 - n * 0.06), {dx: -18, dy: 0}));
    const k = saida(faixa(x, 0.9, 1.9));
    bTrs.forEach((el) => { el.style.transform = `scaleX(${k.toFixed(4)})`; });
    surgir(bPct, molaAR(x - 1.9), {dy: 20});
    contar(bPctN, saida(faixa(x, 1.9, 2.6)), 0, 87, {sufixo: '%'});
    revelar(bPctLeg, molaAR(x - 2.3));
    fim(sec, x, 2.6);
  };
})();
