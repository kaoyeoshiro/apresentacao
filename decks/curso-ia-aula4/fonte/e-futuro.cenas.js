// ===== Bloco E: futuro e fecho =====
// futuro-cap (respiro), horizontes, sinais e curso (tempo) e fecho são arquétipos da biblioteca: sem cena própria.
// otimistas e pessimistas usam os cartões da base.
CENAS.otimistas = cartoes('otimistas');
CENAS.pessimistas = cartoes('pessimistas');

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

// cenarios: os quatro degraus crescem de baixo para cima, um depois do outro, da esquerda para a direita; o texto de
// cada um entra quando ele assenta, e a fonte por último.
CENAS.cenarios = (() => {
  const sec = m.secao('cenarios'), eDg = $$(sec, '.e-degrau'), eFonte = sec.querySelector('.e-dg-fonte');
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    eDg.forEach((el, n) => {
      const k = saida(faixa(x, 0.1 + n * 0.25, 0.55 + n * 0.25));
      el.style.transform = `scaleY(${k.toFixed(4)})`;
      vis(el, k > 0);
      [...el.children].forEach((f) => revelar(f, molaAR(x - 0.45 - n * 0.25)));
    });
    revelar(eFonte, molaAR(x - 1.4));
    fim(sec, x, 1.6);
  };
})();

// medido: o "19%" sobe, o traço dourado se estende embaixo dele, a legenda entra ao lado e a linha menor por último.
CENAS.medido = (() => {
  const sec = m.secao('medido'), q = (s) => sec.querySelector(s);
  const eN = q('.e-md-n'), eTr = q('.e-md-traco'), eLeg = q('.e-md-leg'), eSub = q('.e-md-sub');
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    surgir(eN, molaAR(x - 0.1), {dy: 50});
    contar(eN, saida(faixa(x, 0.1, 0.9)), 0, 19, {sufixo: '%'});
    eTr.style.transform = `scaleX(${saida(faixa(x, 0.8, 1.2)).toFixed(4)})`;
    revelar(eLeg, molaAR(x - 0.6));
    revelar(eSub, molaAR(x - 1.2));
    fim(sec, x, 1.5);
  };
})();

// debate (cena guia): na chegada, a pergunta e as duas setas, que se traçam (a que sobe, depois a que desce); no clique,
// o enunciado entra e a pergunta do fim chega por último, com a barra dourada.
CENAS.debate = (() => {
  const sec = m.secao('debate'), q = (s) => sec.querySelector(s);
  const eSob = q('.e-seta-s'), eDes = q('.e-seta-d'), eEnun = q('.e-db-enun'), eFim = q('.e-db-fim');
  return (t, c) => {
    const x = conteudo(c), d = c.desde(1);
    titulo(sec, x, c);
    tracar(eSob, saida(faixa(x, 0.2, 0.9)));
    tracar(eDes, saida(faixa(x, 0.6, 1.3)));
    fim(sec, x, 1.3);
    vis(eEnun, d > 0); vis(eFim, d > 0);
    revelar(eEnun, molaAR(d - 0.05));
    surgir(eFim, molaAR(d - 0.5), {dx: -20, dy: 0});
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
