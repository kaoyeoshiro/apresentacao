// ===== Bloco A: assistentes =====
CENAS.cinco = cartoes('cinco');
CENAS.sigilo = cartoes('sigilo');

// Desenhos por código: o olho do assistente (alcance) e o cabo do acesso com as duas marcas do corte (memoria).
for (const el of document.querySelectorAll('.a-olho')) {
  const s = document.createElementNS(NS, 'svg');
  s.setAttribute('viewBox', '0 0 100 60');
  traco(s, 'M4 30Q50 -10 96 30Q50 70 4 30Z');
  traco(s, 'M50 18A12 12 0 1 0 50.01 18');
  el.appendChild(s);
}
for (const el of document.querySelectorAll('.a-cabo')) {
  const s = document.createElementNS(NS, 'svg');
  s.setAttribute('viewBox', '0 0 320 60');
  traco(s, 'M0 30H160', 'a-cabo-e');
  traco(s, 'M160 30H320', 'a-cabo-d');
  traco(s, 'M150 10L138 50', 'a-corte');
  traco(s, 'M182 10L170 50', 'a-corte');
  el.appendChild(s);
}

// alcance (S.T.A.R. do bloco): a caixa chega, o assistente se liga a ela e o feixe lê as cinco mensagens, marcando cada
// uma como lida. Cada clique acende uma sensível (cliente, minuta, parte contrária); a barra dourada fica só na atual, e
// as que não estão acesas passam à tinta suave.
CENAS.alcance = (() => {
  const sec = m.secao('alcance'), q = (s) => sec.querySelector(s);
  const aCx = q('.a-cx'), aMsgs = $$(sec, '.a-msg'), aFeixe = q('.a-feixe'), aFio = q('.a-fio'), aAss = q('.a-ass');
  const aSens = [0, 2, 4], aPasso = 0.3;   // linhas acesas, na ordem dos cliques; segundos do feixe em cada linha
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    surgir(aCx, molaAR(x - 0.1), {dy: 24});
    aMsgs.forEach((el, n) => surgir(el, molaAR(x - 0.25 - n * 0.08), {dy: 14}));
    tracar(aFio, saida(faixa(x, 0.6, 0.9)));
    surgir(aAss, molaAR(x - 0.75), {dx: 30, dy: 0});
    const kf = faixa(x, 1.1, 1.1 + aPasso * (aMsgs.length - 1));
    aFeixe.style.transform = `translateY(${kf * 98 * (aMsgs.length - 1)}px)`;
    aFeixe.style.opacity = faixa(x, 0.95, 1.1) * (1 - faixa(x, 2.4, 2.6));
    aMsgs.forEach((el, n) => {
      el.querySelector('.a-lido').style.opacity = faixa(x, 1.15 + n * aPasso, 1.3 + n * aPasso);
      const j = aSens.indexOf(n), acesa = j >= 0 && c.desde(j + 1) > 0;
      const k = acesa ? saida(faixa(c.desde(j + 1), 0, 0.5)) : 0;
      el.querySelector('.a-luz').style.opacity = k;
      el.querySelector('.a-barra').style.opacity = j >= 0 && j < 2 ? k * (1 - faixa(c.desde(j + 2), 0, 0.3)) : k;
      el.classList.toggle('a-fora', c.desde(1) > 0 && !acesa);
    });
    fim(sec, x, 1.6);
  };
})();

// memoria: uma linha por parada. O nome entra, o cabo do acesso se traça e se corta (as pontas se afastam e as marcas
// do corte aparecem, douradas só na linha atual), e a caixa do que fica na memória chega por último.
CENAS.memoria = (() => {
  const sec = m.secao('memoria'), aEts = $$(sec, '.a-mem-et'), aLs = $$(sec, '.a-mem-l');
  return (t, c) => {
    const x = conteudo(c), d = (n) => (n === 0 ? x - 0.15 : c.desde(n));
    titulo(sec, x, c);
    aEts.forEach((el, n) => revelar(el, molaAR(x - 0.05 - n * 0.1)));
    let agora = 0;
    for (let n = 1; n < aLs.length; n++) if (c.desde(n) > 0) agora = n;
    aLs.forEach((l, n) => {
      const dn = d(n), [esq, dir, ...cortes] = l.querySelectorAll('path');
      vis(l, dn > 0);
      l.classList.toggle('a-agora', n === agora);
      surgir(l.querySelector('.a-mem-nome'), molaAR(dn), {dx: -20, dy: 0});
      tracar(esq, saida(faixa(dn, 0.1, 0.35)));
      tracar(dir, saida(faixa(dn, 0.35, 0.6)));
      const kc = saida(faixa(dn, 0.7, 1.0));
      esq.style.transform = `translateX(${-18 * kc}px)`;
      dir.style.transform = `translateX(${18 * kc}px)`;
      cortes.forEach((p) => { p.style.opacity = faixa(dn, 0.75, 0.95); });
      surgir(l.querySelector('.a-mem-txt'), molaAR(dn - 0.9), {dx: 24, dy: 0});
    });
    fim(sec, x, 1.0);
  };
})();

// a7 (cena guia): o enunciado sobe, as três colunas entram em onda e as linhas em branco de cada uma se traçam.
CENAS.a7 = (() => {
  const sec = m.secao('a7'), aEnun = sec.querySelector('.a-enun'), aCols = $$(sec, '.a-col');
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    revelar(aEnun, molaAR(x - 0.15));
    aCols.forEach((col, n) => {
      surgir(col, molaAR(x - 0.5 - n * 0.15), {dy: 26});
      $$(col, 'i').forEach((el, j) => { el.style.transform = `scaleX(${saida(faixa(x, 0.9 + n * 0.15 + j * 0.1, 1.3 + n * 0.15 + j * 0.1))})`; });
    });
    fim(sec, x, 1.0);
  };
})();
