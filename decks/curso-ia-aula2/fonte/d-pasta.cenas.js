
// ===== Bloco D: na pasta =====
// O slide "papeis" é o arquétipo viagem (a biblioteca faz o voo dos objetos #ob-*) e "fonte" é o arquétipo fios.

// estrutura: a árvore nasce pela raiz, os ramos se traçam, as anotações entram à direita e o cronologia.md, tracejado
// em dourado, chega por último: é o único arquivo que o agente vai criar.
CENAS.estrutura = (() => {
  const sec = m.secao('estrutura'), camada = sec.querySelector('.d-arv-svg'), arv = sec.querySelector('.d-arv');
  const rod = sec.querySelector(':scope > .rodape'), exts = $$(sec, '.d-ext');
  const ICONE = {pasta: ['M3 12H15L19 17H37V38H3Z'], arquivo: ['M8 4H25L34 13V40H8Z', 'M25 4V13H34']};
  const nos = $$(sec, '.d-no').map((el, n) => {
    const nivel = Number(el.dataset.nivel || 0), nome = document.createElement('span'), ic = document.createElement('span');
    nome.className = 'd-nome';
    nome.append(...el.childNodes);
    ic.className = 'd-ic';
    const s = document.createElementNS(NS, 'svg');
    s.setAttribute('viewBox', '0 0 40 44');
    for (const d of ICONE[el.dataset.tipo]) traco(s, d);
    ic.appendChild(s);
    el.append(ic, nome);
    Object.assign(el.style, {left: `${56 * nivel}px`, top: `${64 * n}px`});
    return {el, nivel, x: 56 * nivel, y: 64 * n, novo: el.classList.contains('d-novo')};
  });
  let ramos = null, guias = null;
  const montar = () => {
    if (ramos) return;
    const X = arv.offsetLeft, Y = arv.offsetTop;
    ramos = nos.map((no, n) => {
      if (!no.nivel) return null;
      let p = n - 1;
      while (p > 0 && nos[p].nivel !== no.nivel - 1) p--;
      return traco(camada, `M${X + nos[p].x + 20} ${Y + nos[p].y + 50}V${Y + no.y + 28}H${X + no.x - 8}`);
    });
    // cada anotação na altura do nó (ou do meio do grupo); colchete para os três papéis, guia pontilhada para os outros
    guias = exts.map((ext) => {
      const alvo = ext.dataset.de === 'd-papel' ? nos.filter((no) => no.el.classList.contains('d-papel')) : nos.filter((no) => no.el.id === ext.dataset.de);
      const dir = Math.max(...alvo.map((no) => X + no.x + no.el.offsetWidth)) + 28;
      const y1 = Y + alvo[0].y + 28, y2 = Y + alvo[alvo.length - 1].y + 28, ym = (y1 + y2) / 2, xe = ext.offsetLeft - 22;
      ext.style.top = `${ym - 25}px`;
      if (alvo.length > 1) return traco(camada, `M${dir} ${y1}H${dir + 16}V${y2}H${dir}M${dir + 16} ${ym}H${xe}`);
      const g = traco(camada, `M${dir} ${ym}H${xe}`);
      g.classList.add('d-guia');
      return g;
    });
  };
  return (t, c) => {
    montar();
    const x = conteudo(c);
    titulo(sec, x, c);
    let ordem = 0;
    nos.forEach((no, n) => {
      const d = no.novo ? 1.55 : 0.1 + 0.08 * ordem++;
      surgir(no.el, molaAR(x - d), {dx: -18, dy: 0});
      if (ramos[n]) tracar(ramos[n], saida(faixa(x, d - 0.05, d + 0.3)));
    });
    exts.forEach((ext, n) => {
      const novo = ext.classList.contains('d-ext-novo'), d = novo ? 1.75 : 0.85 + n * 0.14;
      // a guia de traço tracejado/pontilhado só ganha o padrão do CSS quando termina de se traçar
      const k = saida(faixa(x, d - 0.2, d + 0.1));
      tracar(guias[n], k);
      if (k >= 1) { guias[n].removeAttribute('pathLength'); guias[n].style.strokeDasharray = ''; }
      revelar(ext, molaAR(x - d));
    });
    revelar(rod, molaAR(x - 1.95));
    fim(sec, x, 2.0);
  };
})();

// memoria: o painel abre, as linhas entram uma por uma e a linha de prazo e multa ganha o sublinhado dourado.
CENAS.memoria = (() => {
  const sec = m.secao('memoria'), arq = sec.querySelector('.d-arq'), aba = sec.querySelector('.d-arq-cab'), txt = sec.querySelector('.d-arq-txt');
  const lns = $$(sec, '.d-ln'), regra = sec.querySelector('.d-mm-regra'), rod = sec.querySelector(':scope > .rodape');
  // o sublinhado mora numa caixa irmã das linhas, para a camada dele não entrar na medida do texto
  const sub = document.createElement('div');
  sub.className = 'd-sub';
  txt.appendChild(sub);
  let pronto = false;
  return (t, c) => {
    if (!pronto) {
      pronto = true;
      const ln = regra.parentElement;
      Object.assign(sub.style, {left: `${ln.offsetLeft + regra.offsetLeft}px`, top: `${ln.offsetTop + regra.offsetTop}px`, width: `${regra.offsetWidth}px`, height: `${regra.offsetHeight}px`});
    }
    const x = conteudo(c);
    titulo(sec, x, c);
    surgir(arq, molaAR(x - 0.1), {dy: 30});
    revelar(aba, molaAR(x - 0.2));
    lns.forEach((el, n) => revelar(el, molaAR(x - 0.35 - n * 0.13)));
    anotar(sub, saida(faixa(x, 1.3, 1.75)), {forma: 'sublinhado', semente: 8, folga: 4});
    revelar(rod, molaAR(x - 1.5));
    fim(sec, x, 1.6);
  };
})();

// pedido: clique 1, o pedido se digita na caixa; clique 2, os cinco passos entram em onda.
CENAS.pedido = (() => {
  const sec = m.secao('pedido'), q = (s) => sec.querySelector(s);
  const ent = q('.d-entrada'), ped = q('.d-pedido'), etP = q('.d-et-ped'), passos = $$(sec, '.d-passos li');
  return (t, c) => {
    const x = conteudo(c), y = c.desde(1);
    titulo(sec, x, c);
    revelar(etP, molaAR(x - 0.05));
    surgir(ent, molaAR(x - 0.1), {dy: 24});
    digitar(ped, faixa(x, 0.35, 2.65), {cursor: x > 0.25 && x < 2.8, semente: 7});
    passos.forEach((li, n) => surgir(li, molaAR(y - 0.1 - n * 0.12), {dx: -18, dy: 0}));
  };
})();

// demo: simulação por código de uma sessão de agente na pasta, em quatro cliques. 1: o pedido se digita na caixa.
// 2: vai para a conversa e o agente lê os três papéis. 3: a conversa rola, o plano aparece e o "Permitir" é apertado.
// 4: rola de novo, o arquivo se escreve e a resposta diz o que não encontrou; o cronologia.md acende em dourado.
CENAS.demo = (() => {
  const sec = m.secao('demo'), q = (s) => sec.querySelector(s);
  const jan = q('.d-jan'), fio = q('.d-fio'), rolo = q('.d-rolo'), comp = q('.d-comp'), compTxt = q('.d-comp-txt'), enviar = q('.d-enviar');
  const eu = q('.d-eu'), lendo = q('.d-lendo'), plano = q('.d-plano'), perm = q('.d-perm'), escr = q('.d-escr'), resp = q('.d-resp');
  const chips = $$(lendo, '.d-arqchip'), rodaL = lendo.querySelector('.d-roda'), rodaE = escr.querySelector('.d-roda');
  const plTit = plano.querySelector('.d-plano-tit'), itens = $$(plano, 'li'), btSim = q('.d-bt-sim'), barra = q('.d-barra i');
  const r1 = q('.d-resp-1'), r2 = q('.d-resp-2'), novo = q('.d-novo-chip');
  const blocos = [eu, lendo, plano, perm, escr, resp];
  let M = null;
  const montar = () => {
    if (M) return;
    M = {cheio: comp.offsetHeight, curto: 84, H: jan.clientHeight, topo: 62,
      S2: plano.offsetTop - 22, S3: escr.offsetTop - 22, caixas: blocos.map((b) => [b.offsetTop, b.offsetHeight])};
  };
  // gira enquanto trabalha (função do tempo) e fica cheia quando termina
  const roda = (el, t, pronta) => {
    el.classList.toggle('pronta', pronta);
    el.style.transform = pronta ? '' : `rotate(${((t * 400) % 360).toFixed(1)}deg)`;
  };
  return (t, c) => {
    montar();
    const x = conteudo(c), y = c.desde(1), z = c.desde(2), w = c.desde(3);
    titulo(sec, x, c);
    surgir(jan, molaAR(x + 0.45), {dy: 40});   // a janela chega antes da câmera, a viagem não cruza o vazio
    // 1. digitar; 2. enviar: a caixa encolhe e o texto vira a mensagem da conversa
    digitar(compTxt, faixa(x, 0.5, 2.5), {cursor: x > 0.4 && x < 2.6, semente: 11});
    const ke = entradaSaida(faixa(y, 0, 0.45)), oc = 1 - faixa(y, 0, 0.15);
    compTxt.style.opacity = String(oc);
    vis(compTxt, oc > 0.001);
    enviar.classList.toggle('cheio', x > 2.5 && y < 0.1);
    const hComp = lerp(M.cheio, M.curto, ke);
    comp.style.height = `${hComp.toFixed(1)}px`;
    fio.style.height = `${(M.H - M.topo - 24 - hComp - 14).toFixed(1)}px`;
    // a conversa rola até o plano (clique 3) e até a escrita (clique 4)
    const S = lerp(0, M.S2, entradaSaida(faixa(z, 0, 0.6))) + (M.S3 - M.S2) * entradaSaida(faixa(w, 0, 0.6));
    rolo.style.transform = S > 0 ? `translateY(${(-S).toFixed(1)}px)` : '';
    surgir(eu, molaAR(y - 0.15), {dy: 40});
    surgir(lendo, molaAR(y - 0.55), {dy: 16});
    chips.forEach((ch, n) => surgir(ch, molaAR(y - 0.8 - n * 0.32), {dx: -12, dy: 0}));
    roda(rodaL, t, y > 1.85);
    surgir(plano, molaAR(z - 0.3), {dy: 20});
    revelar(plTit, molaAR(z - 0.35));
    itens.forEach((li, n) => surgir(li, molaAR(z - 0.45 - n * 0.15), {dx: -12, dy: 0}));
    surgir(perm, molaAR(z - 1.15), {dy: 20});
    btSim.classList.toggle('apertado', z > 1.9);
    surgir(escr, molaAR(w - 0.3), {dy: 16});
    barra.style.transform = `scaleX(${saida(faixa(w, 0.5, 1.5)).toFixed(4)})`;
    roda(rodaE, t, w > 1.5);
    surgir(resp, molaAR(w - 1.2), {dy: 16});
    digitar(r1, faixa(w, 1.3, 2.0), {semente: 13});
    digitar(r2, faixa(w, 2.0, 2.55), {semente: 17});
    surgir(novo, molaAR(w - 2.55), {dy: 0, escala: 0.1});
    // o que rolou para cima da vista sai da tela (e da contagem); quadro em função de S, nunca de estado
    blocos.forEach((b, n) => {
      const [top, h] = M.caixas[n], f = clamp((top + h - S) / h), o = Number(b.style.opacity || 1) * f;
      b.style.opacity = String(o);
      vis(b, o > 0.001);
    });
    fim(sec, x, 1.0);
  };
})();

// trecho: a linha da cronologia entra, a página do contrato chega e o fio dourado liga a fonte à cláusula marcada.
CENAS.trecho = (() => {
  const sec = m.secao('trecho'), q = (s) => sec.querySelector(s);
  const lin = q('.d-lin'), partes = [...lin.children], fonte = q('.d-lin-fonte'), pag = q('.d-pag'), img = q('.d-pag-img'), leg = q('.d-pag-leg');
  const fioT = q('.d-tr-fio'), ca = q('.d-tr-a'), cb = q('.d-tr-b');
  // a cláusula terceira, no tamanho natural da imagem (900 x 1274): começa em x 96 e ocupa as linhas de y 650 a 700
  const CLAUSULA = {x: 96, y: 675};
  let pronto = false;
  const montar = () => {
    if (pronto) return;
    pronto = true;
    const ax = lin.offsetLeft + fonte.offsetLeft + fonte.offsetWidth + 24, ay = lin.offsetTop + fonte.offsetTop + fonte.offsetHeight / 2;
    const bx = pag.offsetLeft + pag.clientLeft + img.offsetLeft + CLAUSULA.x - 20, by = pag.offsetTop + pag.clientTop + img.offsetTop + CLAUSULA.y;
    const dy = Math.abs(by - ay), xm = (ax + bx) / 2;
    fioT.setAttribute('d', `M${ax} ${ay}H${xm - dy / 2}L${xm + dy / 2} ${by}H${bx}`);
    for (const [el, px, py] of [[ca, ax, ay], [cb, bx, by]]) { el.setAttribute('cx', px); el.setAttribute('cy', py); }
  };
  return (t, c) => {
    montar();
    const x = conteudo(c);
    titulo(sec, x, c);
    partes.forEach((el, n) => revelar(el, molaAR(x - 0.1 - n * 0.12)));
    surgir(pag, molaAR(x - 0.25), {dy: 30});
    kenburns(img, saida(faixa(x, 0, 1.5)), {escala: 1.04, origem: '10% 53%'});
    revelar(leg, molaAR(x - 0.6));
    const k = saida(faixa(x, 0.95, 1.45));
    tracar(fioT, k);
    vis(ca, k > 0);
    vis(cb, k >= 1);
    fim(sec, x, 1.5);
  };
})();

