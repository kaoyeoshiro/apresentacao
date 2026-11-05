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

// skillmd: chegada, o editor com o cabeçalho, as anotações de nome e descrição e o sublinhado dourado da descrição;
// clique 1, as linhas do corpo e a anotação; clique 2, a linha do script, a anotação e o rodapé da licença.
CENAS.skillmd = (() => {
  const sec = m.secao('skillmd'), q = (s) => sec.querySelector(s);
  const bArq = q('.b-arq'), bAba = q('.b-arq-cab'), bTxt = q('.b-arq-txt'), bDesc = q('.b-desc');
  const bCab = $$(sec, '.b-dim, .b-cab'), bBarras = $$(sec, '.b-corpo i'), bScr = q('.b-scr'), bRod = q('.b-rod');
  const bLns = $$(sec, '.b-ln');
  const notas = {nome: q('.b-n-nome'), desc: q('.b-n-desc'), corpo: q('.b-n-corpo'), scr: q('.b-n-scr')};
  const ligas = {nome: q('.b-l-nome'), desc: q('.b-l-desc'), corpo: q('.b-l-corpo'), scr: q('.b-l-scr')};
  // o sublinhado mora numa caixa irmã das linhas, para a camada dele não entrar na medida do texto
  const bSub = document.createElement('div');
  bSub.className = 'b-sub';
  bTxt.appendChild(bSub);
  let pronto = false;
  const montar = () => {
    if (pronto) return;
    pronto = true;
    const y0 = bArq.offsetTop + 4 + bTxt.offsetTop, xa = bArq.offsetLeft + bArq.offsetWidth;
    const centro = (n) => y0 + bLns[n].offsetTop + 24;
    // a anotação fica na altura pedida; o traço sai da borda do editor na altura da linha e dobra até ela
    const pos = (k, yLinha, yNota) => {
      notas[k].style.top = `${Math.round(yNota - 26)}px`;
      ligas[k].setAttribute('d', `M${xa + 14} ${Math.round(yLinha)}H${xa + 46}V${Math.round(yNota)}H${notas[k].offsetLeft - 20}`);
    };
    pos('nome', centro(1), centro(1) - 30);
    pos('desc', centro(2), centro(2) + 22);
    pos('corpo', centro(6), centro(6) - 20);
    pos('scr', centro(8), centro(8));
    const ln = bDesc.parentElement;
    Object.assign(bSub.style, {left: `${ln.offsetLeft + bDesc.offsetLeft}px`, top: `${ln.offsetTop + bDesc.offsetTop}px`, width: `${bDesc.offsetWidth}px`, height: `${bDesc.offsetHeight}px`});
  };
  const nota = (k, d) => {
    const kk = molaAR(d);
    revelar(notas[k], kk);
    vis(notas[k], d > 0);
    tracar(ligas[k], saida(faixa(d + 0.25, 0, 0.35)));
    vis(ligas[k], d + 0.25 > 0);
  };
  return (t, c) => {
    montar();
    const x = conteudo(c), y = c.desde(1), z = c.desde(2);
    titulo(sec, x, c);
    surgir(bArq, molaAR(x - 0.1), {dy: 30});
    revelar(bAba, molaAR(x - 0.2));
    bCab.forEach((el, n) => revelar(el, molaAR(x - 0.35 - n * 0.1)));
    nota('nome', x - 0.85);
    nota('desc', x - 1.05);
    anotar(bSub, saida(faixa(x, 1.5, 2.0)), {forma: 'sublinhado', semente: 7, folga: 4});
    bBarras.forEach((el, n) => {
      el.style.transform = `scaleX(${saida(faixa(y, 0.1 + n * 0.18, 0.45 + n * 0.18)).toFixed(4)})`;
    });
    nota('corpo', y - 0.7);
    revelar(bScr, molaAR(z - 0.1));
    vis(bScr, z > 0);
    nota('scr', z - 0.45);
    revelar(bRod, molaAR(z - 0.9));
    vis(bRod, z > 0);
    fim(sec, x, 1.6);
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
