
// ===== Bloco A, pedir bem =====

// Ícone redondo com ✗ (pedido vago) ou ✓ (pedido bom), desenhado por código e posto antes do texto da caixa.
const aIcone = (caixaEl, certo) => {
  const s = document.createElementNS(NS, 'svg');
  s.setAttribute('class', 'a-ic');
  s.setAttribute('viewBox', '0 0 64 64');
  const ci = document.createElementNS(NS, 'circle');
  ci.setAttribute('cx', 32); ci.setAttribute('cy', 32); ci.setAttribute('r', 29);
  s.appendChild(ci);
  const p = traco(s, certo ? 'M19 33L28 42L45 23' : 'M22 22L42 42M42 22L22 42');
  caixaEl.prepend(s);
  return p;
};

// Par: clique 1 traz o pedido vago; clique 2, o pedido bom, as marcas de texto em sequência e a linha de baixo.
const aPar = (id) => {
  const sec = m.secao(id), err = sec.querySelector('.a-err'), cer = sec.querySelector('.a-cer');
  const extra = sec.querySelector(':scope > .a-extra'), mks = $$(sec, '.a-mk');
  const xErr = aIcone(err, false), xCer = aIcone(cer, true);
  return (t, c) => {
    const x = conteudo(c), y = c.desde(1);
    titulo(sec, x, c);
    surgir(err, molaAR(x - 0.2), {dx: -24, dy: 0});
    tracar(xErr, saida(faixa(x, 0.45, 0.8)));
    const k = molaAR(y - 0.05);
    surgir(cer, k, {dy: 34});
    vis(cer, y > 0);
    tracar(xCer, saida(faixa(y, 0.35, 0.7)));
    mks.forEach((mk, n) => { mk.style.backgroundSize = `${(100 * saida(faixa(y, 0.75 + n * 0.35, 1.2 + n * 0.35))).toFixed(2)}% 100%`; });
    if (extra) { revelar(extra, molaAR(y - 1.1 - mks.length * 0.2)); vis(extra, y > 1.1 + mks.length * 0.2); }
    fim(sec, x, 1.0);
  };
};
for (const id of ['objetivo', 'contexto', 'persona', 'saida', 'regras', 'tce']) CENAS[id] = aPar(id);

// Tentativas: um cartão por clique; a barra da distância nasce no tamanho da tentativa anterior e encolhe.
CENAS.tentativas = (() => {
  const sec = m.secao('tentativas'), et = sec.querySelector('.a-tn-et'), fimEl = sec.querySelector('.a-tn-fim');
  const cs = $$(sec, '.a-tn').map((el) => ({el, v: Number(el.dataset.v), b: el.querySelector('.a-tn-b')}));
  for (const q of cs) q.b.style.width = `${q.v}%`;
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    revelar(et, molaAR(x - 0.1));
    cs.forEach(({el, v, b}, n) => {
      const d = n === 0 ? x - 0.2 : c.desde(n);
      surgir(el, molaAR(d), {dy: 30});
      vis(el, d > 0);
      const de = n === 0 ? 0 : cs[n - 1].v, k = clamp(molaAR(d - 0.4, {resposta: 0.6, amortecimento: 0.9}), 0, 1.02);
      b.style.transform = `scaleX(${(lerp(de, v, k) / v).toFixed(4)})`;
    });
    const df = c.desde(2) - 1.0;
    revelar(fimEl, molaAR(df));
    vis(fimEl, df > 0);
  };
})();

// Personas: a pergunta fica; um papel por clique; a frase e a pílula vêm com o último.
CENAS.personas = (() => {
  const sec = m.secao('personas'), pg = sec.querySelector('.a-pg'), cols = $$(sec, '.a-col'), fr = sec.querySelector('.a-pg-fim');
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    revelar(pg, molaAR(x - 0.15));
    cols.forEach((el, n) => {
      const d = n === 0 ? x - 0.5 : c.desde(n);
      surgir(el, molaAR(d), {dy: 30});
      vis(el, d > 0);
    });
    const df = c.desde(2) - 0.8;
    revelar(fr, molaAR(df));
    vis(fr, df > 0);
    const pil = sec.querySelector(':scope > .pilula');
    surgir(pil, molaAR(df - 0.2), {dy: 0});
    vis(pil, df > 0.2);
  };
})();

CENAS.exemplos = cartoes('exemplos');

// Junta: as seis linhas acendem em onda, de cima para baixo; o fundo do rótulo cresce depois do trecho.
CENAS.junta = (() => {
  const sec = m.secao('junta'), ls = $$(sec, '.a-jl'), rod = sec.querySelector(':scope > .rodape');
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    ls.forEach((el, n) => {
      surgir(el, molaAR(x - 0.2 - n * 0.28), {dx: -22, dy: 0});
      el.style.setProperty('--a-acende', saida(faixa(x, 0.35 + n * 0.28, 0.7 + n * 0.28)).toFixed(4));
    });
    revelar(rod, molaAR(x - 2.0));
  };
})();

// Prática 1: os passos entram um a um, depois o checklist.
CENAS.pratica1 = (() => {
  const sec = m.secao('pratica1'), ps = $$(sec, '.a-ps li'), et = sec.querySelector('.a-ck-et'), ck = $$(sec, '.a-ck li');
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    ps.forEach((el, n) => surgir(el, molaAR(x - 0.2 - n * 0.25), {dx: -22, dy: 0}));
    revelar(et, molaAR(x - 0.9));
    ck.forEach((el, n) => surgir(el, molaAR(x - 1.0 - n * 0.08), {dx: 18, dy: 0}));
  };
})();
