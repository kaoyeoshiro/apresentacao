
const m = mundo(SLIDES);
const CENAS = {};
const $$ = (sec, sel) => [...sec.querySelectorAll(sel)];
const vis = (el, sim) => { el.style.visibility = sim ? '' : 'hidden'; };
const NS = 'http://www.w3.org/2000/svg';
const traco = (pai, d, cls) => { const p = document.createElementNS(NS, 'path'); p.setAttribute('d', d); if (cls) p.setAttribute('class', cls); pai.appendChild(p); return p; };

// Cartões: entram em onda, da esquerda para a direita e de cima para baixo.
const cartoes = (id) => {
  const sec = m.secao(id), cs = [...sec.querySelectorAll('.cartao')], leg = sec.querySelector('.ct-leg'), rodape = sec.querySelector(':scope > .rodape');
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    if (leg) revelar(leg, molaAR(x - 0.1));
    cs.forEach((el, n) => surgir(el, molaAR(x - 0.2 - n * 0.09), {dy: 30}));
    if (rodape) revelar(rodape, molaAR(x - 0.4 - cs.length * 0.09));
    fim(sec, x, 0.5 + cs.length * 0.09);
  };
};

// Definição em partes: um item por clique, o atual em destaque, e a explicação dele à direita.
const partes = (id) => {
  const sec = m.secao(id), itens = $$(sec, '.partes li'), expl = $$(sec, '.explica p'), rod = sec.querySelector(':scope > .rodape');
  return (t, c) => {
    const x = conteudo(c), d = (n) => (n === 0 ? x - 0.1 : c.desde(n));
    titulo(sec, x, c);
    let ativo = 0;
    for (let n = 1; n < itens.length; n++) if (c.desde(n) > 0) ativo = n;
    itens.forEach((li, n) => {
      const k = molaAR(d(n));
      surgir(li, k, {dx: -20, dy: 0});
      vis(li, k > 0);
      li.classList.toggle('ativa', n === ativo);
    });
    expl.forEach((p, n) => {
      const sai = n + 1 < expl.length ? faixa(c.desde(n + 1), 0, 0.2) : 0;
      const k = sai > 0 ? 1 - sai : molaAR(d(n) - 0.2);
      surgir(p, k, {dy: 18});
      vis(p, k > 0.001);
    });
    if (rod) revelar(rod, molaAR(x - 0.8));
    fim(sec, x, 1.0);
  };
};

