// ===== Bloco C: quem paga a conta =====
// conta-cap, quem-banca, encolhe, bolha e tese são arquétipos da biblioteca; pesado e portavel usam os cartões da base.
CENAS.pesado = cartoes('pesado');
CENAS.portavel = cartoes('portavel');

// custo: a linha dos 100% se traça na chegada; um ano por parada (2024 na chegada, 2025 e 2026 nos cliques). A barra
// cresce, o valor conta e, na de 653%, a quebra aparece depois que ela passa do ponto.
CENAS.custo = (() => {
  const sec = m.secao('custo'), cCab = sec.querySelector('.c-cab'), cCem = sec.querySelector('.c-cem i'), cCemLeg = sec.querySelector('.c-cem-leg');
  const cFonte = sec.querySelector('.c-fonte'), cAnos = $$(sec, '.c-ano');
  const PX = 280 / 100, TETO = 1080;   // 100% da receita = 280 px; o que passa do teto é desenhado quebrado
  const cLin = cAnos.map((el) => {
    const bar = el.querySelector('.c-bar'), v = +bar.dataset.v, w = Math.min(v * PX, TETO);
    bar.style.width = `${w}px`;
    const pct = el.querySelector('.c-pct');
    pct.style.left = `${Math.max(320 + w, 320 + 100 * PX) + 30}px`;   // o valor nunca cruza a linha dos 100%
    return {el, n: el.querySelector('.c-ano-n'), i: bar.querySelector('i'), u: bar.querySelector('u'), pct, v};
  });
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    revelar(cCab, molaAR(x - 0.1));
    cCem.style.transform = `scaleY(${saida(faixa(x, 0.2, 0.8)).toFixed(4)})`;
    revelar(cCemLeg, molaAR(x - 0.6));
    revelar(cFonte, molaAR(x - 0.8));
    cLin.forEach((l, n) => {
      const d = n === 0 ? x - 0.7 : c.desde(n);
      vis(l.el, d > 0);
      surgir(l.n, molaAR(d), {dx: -18, dy: 0});
      const k = saida(faixa(d, 0.15, 1.05));
      l.i.style.transform = `scaleX(${k.toFixed(4)})`;
      surgir(l.pct, molaAR(d - 0.9), {dx: -12, dy: 0});
      contar(l.pct, saida(faixa(d, 0.9, 1.4)), 0, l.v, {sufixo: '%'});
      if (l.u) l.u.style.opacity = String(faixa(d, 0.75, 0.95));
    });
    fim(sec, x, 1.0);
  };
})();

// compromissos: o número conta até 895; a moeda e a unidade entram junto, e a legenda sobe depois.
CENAS.compromissos = (() => {
  const sec = m.secao('compromissos'), q = (s) => sec.querySelector(s);
  const cMoeda = q('.c-moeda'), c895 = q('.c-895'), cBi = q('.c-bi'), cLeg = q('.c-num-leg'), cRod = q(':scope > .rodape');
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    surgir(cMoeda, molaAR(x - 0.1), {dy: 0});
    surgir(c895, molaAR(x - 0.1), {dy: 0});
    contar(c895, saida(faixa(x, 0.1, 1.4)), 0, 895);
    surgir(cBi, molaAR(x - 0.3), {dy: 0});
    revelar(cLeg, molaAR(x - 1.4));
    revelar(cRod, molaAR(x - 1.5));
    fim(sec, x, 1.8);
  };
})();

// a8: na chegada, só a pergunta; no segundo clique (depois do cronômetro), o checklist em miniatura, item por item.
CENAS.a8 = (() => {
  const sec = m.secao('a8'), cPerg = sec.querySelector('.c-perg'), cEt = sec.querySelector('.c-mini-et');
  const cMini = sec.querySelector('.c-mini'), cIt = $$(sec, '.c-mini li');
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    surgir(cPerg, molaAR(x - 0.2), {dy: 24});
    fim(sec, x, 1.2);
    const d = c.desde(1);
    vis(cEt, d > 0); vis(cMini, d > 0);
    revelar(cEt, molaAR(d - 0.05));
    surgir(cMini, molaAR(d - 0.1), {dy: 0});
    cIt.forEach((el, n) => surgir(el, molaAR(d - 0.2 - n * 0.12), {dx: 18, dy: 0}));
  };
})();
