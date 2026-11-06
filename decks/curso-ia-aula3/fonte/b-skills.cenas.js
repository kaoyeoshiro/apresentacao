// ===== Bloco B: skills e Word =====
// word-cap, word-antes, word-demo, a1-voto e a1-gabarito são arquétipos da biblioteca; word-addin e checklist usam os
// ajudantes da base (cartoes, partes).
CENAS['word-addin'] = cartoes('word-addin');
CENAS.checklist = partes('checklist');

// word-pedido: a caixa de mensagem sobe, o anexo entra e o pedido se digita; o botão de enviar fecha.
CENAS['word-pedido'] = (() => {
  const sec = m.secao('word-pedido'), bCaixa = sec.querySelector('.b-caixa'), bAnexo = sec.querySelector('.b-anexo');
  const bPedido = sec.querySelector('.b-pedido'), bEnviar = sec.querySelector('.b-enviar');
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    surgir(bCaixa, molaAR(x - 0.1), {dy: 30});
    surgir(bAnexo, molaAR(x - 0.35), {dx: -18, dy: 0});
    digitar(bPedido, faixa(x, 0.6, 2.5), {cursor: true});
    surgir(bEnviar, molaAR(x - 2.5), {dy: 0, escala: 0.2});
    fim(sec, x, 2.6);
  };
})();

// a1: o enunciado, os três trechos em onda e, por fim, a coluna dos sete pontos.
CENAS.a1 = (() => {
  const sec = m.secao('a1'), bEnun = sec.querySelector('.b-enun'), bTr = $$(sec, '.b-trechos li'), bPt = $$(sec, '.b-sete li');
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    revelar(bEnun, molaAR(x - 0.1));
    bTr.forEach((el, n) => surgir(el, molaAR(x - 0.3 - n * 0.22), {dx: -24, dy: 0}));
    bPt.forEach((el, n) => surgir(el, molaAR(x - 1.0 - n * 0.06), {dx: 18, dy: 0}));
    fim(sec, x, 1.5);
  };
})();

// a2: os três passos em onda, com o passo atual em destaque (um por parada); a folha da skill sobe só com o tracejado,
// o nome, a descrição e as três regras se digitam no segundo passo e o visto se traça no terceiro.
CENAS.a2 = (() => {
  const sec = m.secao('a2'), bPs = $$(sec, '.b-passos li'), bFolha = sec.querySelector('.b-folha');
  const bLinhas = $$(sec, '.b-fl'), bTracejos = bLinhas.map((p) => p.querySelector('i'));
  const bVisto = sec.querySelector('.b-visto'), bVistoTr = [...bVisto.querySelectorAll('circle, path')];
  // cada trecho digitável ganha uma faixa do segundo passo proporcional ao tamanho dele, em ordem
  const bTrechos = bLinhas.flatMap((p, n) => $$(p, ':scope > span').map((el) => ({el, n, tam: el.textContent.length})));
  const bTotal = bTrechos.reduce((a, b) => a + b.tam, 0), bIni = 0.15, bDur = 2.0;
  let bAc = 0;
  for (const tr of bTrechos) { tr.a = bIni + bDur * bAc / bTotal; bAc += tr.tam; tr.b = bIni + bDur * bAc / bTotal; }
  const bComeca = bLinhas.map((_, n) => bTrechos.find((tr) => tr.n === n).a);
  return (t, c) => {
    const x = conteudo(c), y = c.desde(1), z = c.desde(2);
    titulo(sec, x, c);
    const agora = z > 0 ? 2 : y > 0 ? 1 : 0;
    bPs.forEach((li, n) => {
      surgir(li, molaAR(x - 0.2 - n * 0.2), {dx: -22, dy: 0});
      li.classList.toggle('b-agora', n === agora);
    });
    surgir(bFolha, molaAR(x - 0.6), {dy: 30});
    bTrechos.forEach((tr) => digitar(tr.el, faixa(y, tr.a, tr.b), {cursor: y > tr.a && y < tr.b}));
    bTracejos.forEach((el, n) => { el.style.opacity = String(1 - faixa(y, bComeca[n], bComeca[n] + 0.15)); });
    vis(bVisto, z > 0);
    bVistoTr.forEach((el, n) => tracar(el, saida(faixa(z, 0.2 + n * 0.4, 0.7 + n * 0.4))));
    fim(sec, x, 1.4);
  };
})();
