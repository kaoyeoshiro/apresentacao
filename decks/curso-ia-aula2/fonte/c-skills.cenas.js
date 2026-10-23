
// ===== Bloco C: skills =====
// Ícones desenhados por código (caixas do diagrama "liga"): arquivo, tomada e pacote, em viewBox 64 x 76.
const C_ICONES = {
  arquivo: ['M8 4H40L56 20V72H8Z', 'M40 4V20H56', 'M18 40H46M18 52H46M18 64H36'],
  tomada: ['M14 30H50V50Q50 64 36 64H28Q14 64 14 50Z', 'M24 30V10M40 30V10', 'M32 64V76'],
  pacote: ['M6 22L32 8L58 22V58L32 72L6 58Z', 'M6 22L32 36L58 22M32 36V72'],
};
for (const el of document.querySelectorAll('.c-ic[data-ic]')) {
  const s = document.createElementNS(NS, 'svg');
  s.setAttribute('viewBox', '0 0 64 76');
  for (const d of C_ICONES[el.dataset.ic]) traco(s, d);
  el.appendChild(s);
}

// skill: o painel abre com o cabeçalho (nome e descrição, anotados); no clique 2 o editor rola até as instruções, o
// cabeçalho sai pelo alto da vista e a regra "não encontrei nos documentos" ganha o sublinhado dourado.
CENAS.skill = (() => {
  const sec = m.secao('skill'), arq = sec.querySelector('.c-arq'), txt = sec.querySelector('.c-arq-txt'), aba = sec.querySelector('.c-arq-cab');
  const cab = $$(sec, '.c-cab'), ins = $$(sec, '.c-ins'), regra = sec.querySelector('.c-regra'), rod = sec.querySelector('.c-rod');
  const nNome = sec.querySelector('.c-n-nome'), nDesc = sec.querySelector('.c-n-desc'), nIns = sec.querySelector('.c-n-ins');
  const lNome = sec.querySelector('.c-l-nome'), lDesc = sec.querySelector('.c-l-desc'), lIns = sec.querySelector('.c-l-ins');
  const sub = document.createElement('div');
  sub.className = 'c-sub';
  txt.appendChild(sub);
  let rolar = null;
  const montar = () => {
    if (rolar !== null) return;
    rolar = ins[0].offsetTop - cab[0].offsetTop;   // a primeira instrução sobe até o lugar da primeira linha
    const y0 = arq.offsetTop + 4 + 68 + txt.offsetTop, xa = arq.offsetLeft + arq.offsetWidth;
    // cada anotação fica na altura do centro do que ela aponta; o traço vai da borda do painel até ela
    const pos = (nota, liga, centro) => {
      const yc = Math.round(y0 + centro);
      nota.style.top = `${yc - 26}px`;
      liga.setAttribute('d', `M${xa + 14} ${yc}H${nota.offsetLeft - 20}`);
    };
    const meio = (el) => el.offsetTop + 24;   // centro da primeira linha da linha lógica
    pos(nNome, lNome, meio(cab[1]));
    pos(nDesc, lDesc, cab[2].offsetTop + cab[2].offsetHeight / 2);
    // o sublinhado da regra mora numa caixa irmã das linhas, para a camada dele não entrar na medida do texto
    const ln = regra.parentElement;
    Object.assign(sub.style, {left: `${ln.offsetLeft + regra.offsetLeft}px`, top: `${ln.offsetTop + regra.offsetTop}px`, width: `${regra.offsetWidth}px`, height: `${regra.offsetHeight}px`});
    const fimIns = ins[ins.length - 1].offsetTop + ins[ins.length - 1].offsetHeight;
    pos(nIns, lIns, (ins[0].offsetTop + fimIns) / 2 - rolar);
  };
  return (t, c) => {
    montar();
    const x = conteudo(c), y = c.desde(1);
    titulo(sec, x, c);
    surgir(arq, molaAR(x - 0.1), {dy: 30});
    revelar(aba, molaAR(x - 0.2));
    const ks = entradaSaida(faixa(y, 0, 0.9));
    txt.style.transform = ks > 0 ? `translateY(${(-rolar * ks).toFixed(1)}px)` : '';
    // cabeçalho: entra linha a linha e sai com a rolagem
    cab.forEach((el, n) => {
      const k = clamp(molaAR(x - 0.3 - n * 0.12)), o = k * (1 - faixa(ks, 0, 0.55));
      el.style.opacity = String(o);
      vis(el, o > 0.001);
    });
    // instruções: sobem com a rolagem, uma linha depois da outra
    ins.forEach((el, n) => {
      const o = saida(faixa(y, 0.45 + n * 0.09, 0.85 + n * 0.09));
      el.style.opacity = String(o);
      vis(el, o > 0.001);
    });
    // anotações do cabeçalho e o rodapé saem quando o editor rola
    const sai = 1 - faixa(y, 0, 0.3);
    for (const [nota, liga, d] of [[nNome, lNome, 0.85], [nDesc, lDesc, 1.0]]) {
      revelar(nota, molaAR(x - d));
      nota.style.opacity = String(sai);
      tracar(liga, saida(faixa(x, d - 0.15, d + 0.15)) * (sai > 0 ? 1 : 0));
      liga.style.opacity = String(sai);
      if (sai <= 0) vis(nota, false);
    }
    revelar(rod, molaAR(x - 1.2));
    rod.style.opacity = String(sai);
    if (sai <= 0) vis(rod, false);
    revelar(nIns, molaAR(y - 0.95));
    tracar(lIns, saida(faixa(y, 0.8, 1.1)));
    anotar(sub, saida(faixa(y, 1.3, 1.8)), {forma: 'sublinhado', semente: 5, folga: 4});
    fim(sec, x, 1.4);
  };
})();

// onde: os nomes dos apps, depois uma linha da grade por vez (onde mora, como chamar), com os fios entre as linhas.
CENAS.onde = (() => {
  const sec = m.secao('onde'), grade = sec.querySelector('.c-grade'), rod = sec.querySelector(':scope > .rodape');
  const tits = $$(sec, '.c-col-tit');
  const linhas = [[...$$(sec, '[style*="grid-area: la"], [style*="grid-area: a1"], [style*="grid-area: b1"]')],
    [...$$(sec, '[style*="grid-area: lb"], [style*="grid-area: a2"], [style*="grid-area: b2"]')]];
  const camada = document.createElementNS(NS, 'svg');
  camada.setAttribute('class', 'c-traco');
  camada.setAttribute('viewBox', '0 0 1920 1080');
  sec.prepend(camada);
  let fios = null;
  const montar = () => {
    if (fios) return;
    const y1 = grade.offsetTop + 96, y2 = y1 + 150;
    fios = [traco(camada, `M120 ${y1}H1800`), traco(camada, `M120 ${y2}H1800`)];
  };
  return (t, c) => {
    montar();
    const x = conteudo(c);
    titulo(sec, x, c);
    tits.forEach((el, n) => revelar(el, molaAR(x - 0.1 - n * 0.12)));
    tracar(fios[0], saida(faixa(x, 0.25, 0.65)));
    linhas[0].forEach((el, n) => surgir(el, molaAR(x - 0.45 - n * 0.12), {dx: -18, dy: 0}));
    tracar(fios[1], saida(faixa(x, 0.75, 1.15)));
    linhas[1].forEach((el, n) => surgir(el, molaAR(x - 0.9 - n * 0.12), {dx: -18, dy: 0}));
    revelar(rod, molaAR(x - 1.4));
    fim(sec, x, 1.5);
  };
})();

// liga: clique 1, o agente e a skill; clique 2, o MCP; clique 3, o plugin e o traço dourado que embrulha os dois.
CENAS.liga = (() => {
  const sec = m.secao('liga'), q = (s) => sec.querySelector(s), rod = q(':scope > .rodape');
  const ag = q('.c-agente'), sk = q('.c-skill'), mc = q('.c-mcp'), pl = q('.c-plugin');
  const dSk = q('.c-d-sk'), dMc = q('.c-d-mc'), dPl = q('.c-d-pl');
  return (t, c) => {
    const x = conteudo(c), y = c.desde(1), z = c.desde(2);
    titulo(sec, x, c);
    surgir(ag, molaAR(x - 0.1), {dy: 0, escala: 0.06});
    tracar(dSk, saida(faixa(x, 0.35, 0.65)));
    surgir(sk, molaAR(x - 0.5), {dx: -30, dy: 0});
    tracar(dMc, saida(faixa(y, 0.05, 0.35)));
    surgir(mc, molaAR(y - 0.2), {dx: 30, dy: 0});
    surgir(pl, molaAR(z - 0.05), {dy: -30});
    // o pacote se fecha depois que o plugin pousa; o tracejado volta quando o traço termina (o CSS dá o padrão)
    const kp = saida(faixa(z, 0.35, 1.0));
    tracar(dPl, kp);
    if (kp >= 1) { dPl.removeAttribute('pathLength'); dPl.style.strokeDasharray = ''; }
    revelar(rod, molaAR(z - 0.8));
    fim(sec, x, 1.2);
  };
})();
