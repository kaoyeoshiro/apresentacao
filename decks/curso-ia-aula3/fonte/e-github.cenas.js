// ===== Bloco E: GitHub =====
// repositorio: a página chega; em cada clique o ponteiro vai a uma parte dela, o quadro dourado a cerca e a definição
// troca à direita. No segundo clique o ponteiro passa pelo botão Code, o menu abre e ele desce ao Download ZIP; no
// terceiro o menu fecha. Posições medidas uma vez, no primeiro quadro (fontes já carregadas), relativas à seção.
CENAS.repositorio = (() => {
  const sec = m.secao('repositorio'), q = (s) => sec.querySelector(s);
  const ePag = q('.e-pag'), eMenu = q('.e-menu'), eAlvo = q('.e-alvo'), ePont = q('.e-ponteiro'), eDefs = $$(sec, '.e-def');
  const eAlvos = [q('.e-readme'), q('.e-zip'), q('.e-issues'), q('.e-prs')];
  let eB = null, eP = null, eCode = null;
  const eRel = (el) => { const a = caixa(el), s = caixa(sec); return {x: a.x - s.x, y: a.y - s.y, w: a.w, h: a.h}; };
  const eInfla = (b, f, g = f) => ({x: b.x - f, y: b.y - g, w: b.w + 2 * f, h: b.h + 2 * g});
  const ePonto = (b, fx, fy) => ({x: b.x + b.w * fx, y: b.y + b.h * fy});
  const eMix = (a, b, k) => Object.fromEntries(Object.keys(a).map((n) => [n, lerp(a[n], b[n], k)]));
  return (t, c) => {
    if (!eB) {
      const r = eAlvos.map(eRel), cd = eRel(q('.e-code'));
      eB = [eInfla(r[0], 10), eInfla(r[1], 4), eInfla(r[2], 14, 2), eInfla(r[3], 14, 2)];
      eP = [ePonto(r[0], 0.6, 0.84), ePonto(r[1], 0.8, 0.86), ePonto(r[2], 0.72, 0.92), ePonto(r[3], 0.3, 0.92)];
      eCode = ePonto(cd, 0.45, 0.6);
    }
    const x = conteudo(c), d1 = c.desde(1), d2 = c.desde(2), d3 = c.desde(3), d4 = c.desde(4);
    titulo(sec, x, c);
    surgir(ePag, molaAR(x - 0.1), {dy: 24});

    // ponteiro: entra pela direita no clique 1 e anda de parte em parte
    const inicio = {x: 1240, y: 860};
    let p = inicio;
    if (d1 > 0) p = eMix(inicio, eP[0], entradaSaida(faixa(d1, 0, 0.7)));
    if (d2 > 0) p = d2 < 0.9 ? eMix(eP[0], eCode, entradaSaida(faixa(d2, 0, 0.6))) : eMix(eCode, eP[1], entradaSaida(faixa(d2, 0.9, 1.3)));
    if (d3 > 0) p = eMix(eP[1], eP[2], entradaSaida(faixa(d3, 0, 0.7)));
    if (d4 > 0) p = eMix(eP[2], eP[3], entradaSaida(faixa(d4, 0, 0.7)));
    ePont.style.opacity = faixa(d1, 0, 0.3);
    ePont.style.transform = `translate(${(p.x - 4).toFixed(1)}px, ${(p.y - 4).toFixed(1)}px)`;

    // menu do botão Code: abre no clique 2, fecha no 3
    const kMenu = d3 > 0 ? 1 - faixa(d3, 0, 0.3) : molaAR(d2 - 0.55);
    surgir(eMenu, kMenu, {dy: -12});
    vis(eMenu, kMenu > 0.001);

    // quadro dourado: aparece no README e desliza para cada parte
    let b = eB[0];
    if (d2 > 0) b = eMix(eB[0], eB[1], saida(faixa(d2, 0.9, 1.4)));
    if (d3 > 0) b = eMix(eB[1], eB[2], saida(faixa(d3, 0.1, 0.7)));
    if (d4 > 0) b = eMix(eB[2], eB[3], saida(faixa(d4, 0.1, 0.7)));
    const kAlvo = molaAR(d1 - 0.6);
    eAlvo.style.left = `${b.x.toFixed(1)}px`; eAlvo.style.top = `${b.y.toFixed(1)}px`;
    eAlvo.style.width = `${b.w.toFixed(1)}px`; eAlvo.style.height = `${b.h.toFixed(1)}px`;
    eAlvo.style.opacity = clamp(kAlvo * 1.6, 0, 1);
    vis(eAlvo, kAlvo > 0.001);

    // definições: uma por clique, a anterior sai
    const ent = [d1 - 0.7, d2 - 1.1, d3 - 0.5, d4 - 0.5], sai = [d2, d3, d4, -1];
    eDefs.forEach((el, n) => {
      const k = sai[n] > 0 ? 1 - faixa(sai[n], 0, 0.25) : molaAR(ent[n]);
      surgir(el, k, {dy: 20});
      vis(el, k > 0.001);
    });
    fim(sec, x, 0.8);
  };
})();
