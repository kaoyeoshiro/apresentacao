// ===== Bloco C: MCP e plugins =====
// Página de petição desenhada por código (a3 e injecao). data-linhas é uma lista de linhas: número = linha de texto
// (largura em %), tNN título, hNN seção, dNN data à direita, _ linha em branco, w a linha em texto branco, s a
// assinatura, r o rodapé minúsculo, c o cabeçalho e p o número da página.
const C_LINHA = (cls) => { const d = document.createElement('div'); d.className = `c-l ${cls}`; return d; };
const C_BARRA = (pai, esq, larg, topo) => {
  const i = document.createElement('i');
  Object.assign(i.style, {left: `${esq}%`, width: `${larg}%`}, topo == null ? {} : {top: `${topo}px`});
  pai.appendChild(i);
  return i;
};
for (const pag of document.querySelectorAll('.c-pag[data-linhas]')) {
  for (const tk of pag.dataset.linhas.split(/\s+/)) {
    const n = parseFloat(tk.replace(/^[a-z]/, ''));
    let l;
    if (tk === '_') l = C_LINHA('c-v');
    else if (tk === 'c') { l = C_LINHA('c-c'); C_BARRA(l, 34, 32); }
    else if (tk === 'p') { l = C_LINHA('c-p'); C_BARRA(l, 42, 16); }
    else if (tk === 's') { l = C_LINHA('c-s'); C_BARRA(l, 22, 56); C_BARRA(l, 30, 40); C_BARRA(l, 26, 48); }
    else if (tk === 'r') { l = C_LINHA('c-r'); C_BARRA(l, 0, 100, 0); C_BARRA(l, 0, 64, 6); }
    else if (tk === 'w') { l = C_LINHA('c-w'); C_BARRA(l, 0, 100); C_BARRA(l, 0, 100).className = 'c-w-tinta'; }
    else if (tk[0] === 't') { l = C_LINHA('c-t'); C_BARRA(l, 0, n); }
    else if (tk[0] === 'h') { l = C_LINHA('c-h'); C_BARRA(l, 0, n); }
    else if (tk[0] === 'd') { l = C_LINHA(''); C_BARRA(l, 100 - n, n); }
    else { l = C_LINHA(''); C_BARRA(l, 0, n); }
    pag.appendChild(l);
  }
}
// Caixa de um elemento relativa à section (offsets somados até ela).
const C_LOCAL = (el, sec) => {
  let x = 0, y = 0;
  for (let n = el; n && n !== sec; n = n.offsetParent) { x += n.offsetLeft + (n !== el ? n.clientLeft : 0); y += n.offsetTop + (n !== el ? n.clientTop : 0); }
  return {x, y, w: el.offsetWidth, h: el.offsetHeight};
};

// a3: a página entra; a lupa marca o pé da página e o rodapé ampliado se abre ao lado, sem destaque.
CENAS.a3 = (() => {
  const sec = m.secao('a3'), q = (s) => sec.querySelector(s);
  const pag = q('.c-pag'), enun = q('.c-enun'), amp = q('.c-amp'), ass = q('.c-amp-ass'), rod = q('.c-amp-rod');
  const lq = q('.c-lupa-q'), ll = q('.c-lupa-l');
  let pronto = false;
  return (t, c) => {
    if (!pronto) {
      pronto = true;
      const s = C_LOCAL(pag.querySelector('.c-s'), sec), r = C_LOCAL(pag.querySelector('.c-r'), sec), a = C_LOCAL(amp, sec);
      const x0 = s.x - 12, x1 = s.x + s.w + 12, y0 = s.y - 10, y1 = r.y + r.h + 10;
      lq.setAttribute('d', `M${x0} ${y0}H${x1}V${y1}H${x0}Z`);
      ll.setAttribute('d', `M${x1} ${y0}L${a.x} ${a.y}M${x1} ${y1}L${a.x} ${a.y + a.h}`);
    }
    const x = conteudo(c);
    titulo(sec, x, c);
    surgir(pag, molaAR(x - 0.1), {dx: -24, dy: 0});
    revelar(enun, molaAR(x - 0.4));
    tracar(lq, saida(faixa(x, 0.8, 1.1)));
    tracar(ll, saida(faixa(x, 1.05, 1.4)));
    if (faixa(x, 1.05, 1.4) >= 1) { ll.removeAttribute('pathLength'); ll.style.strokeDasharray = ''; ll.style.strokeDashoffset = ''; }
    surgir(amp, molaAR(x - 1.25), {dx: -30, dy: 0});
    surgir(ass, molaAR(x - 1.4), {dy: 0});
    revelar(rod, molaAR(x - 1.5));
    fim(sec, x, 1.8);
  };
})();

// injecao: 1 o rodapé ganha o destaque; 2 a seleção varre três linhas e a de texto branco aparece, ampliada ao lado;
// 3 o fio leva a ordem ao agente, que responde o que ela mandou.
CENAS.injecao = (() => {
  const sec = m.secao('injecao'), q = (s) => sec.querySelector(s);
  const pag = q('.c-pag'), rl = pag.querySelector('.c-r'), wl = pag.querySelector('.c-w'), wt = wl.querySelector('.c-w-tinta');
  const tagR = q('.c-tag-rod'), br = q('.c-branco'), brTag = q('.c-tag-br'), brTxt = q('.c-branco-txt');
  const lupa = q('.c-inj-lupa'), fio = q('.c-inj-fio'), ag = q('.c-agente'), bal = q('.c-balao');
  const mk = document.createElement('span');
  mk.className = 'c-mk';
  rl.prepend(mk);
  // a seleção: da última linha dos fatos, pela linha branca, até o título do direito
  const selLinhas = [wl.previousElementSibling, wl, wl.nextElementSibling];
  const sels = selLinhas.map((l) => { const s = document.createElement('span'); s.className = 'c-sel'; l.prepend(s); return s; });
  let pronto = false;
  return (t, c) => {
    if (!pronto) {
      pronto = true;
      const w = C_LOCAL(wl, sec), b = C_LOCAL(br, sec), a = C_LOCAL(ag, sec), r = C_LOCAL(rl, sec);
      const xw = w.x + w.w + 6, yw = w.y + w.h / 2;
      lupa.setAttribute('d', `M${xw} ${yw}L${b.x} ${b.y + 14}M${xw} ${yw}L${b.x} ${b.y + b.h - 14}`);
      fio.setAttribute('d', `M${a.x + a.w / 2} ${b.y + b.h}V${a.y}`);
      tagR.style.top = `${r.y + r.h / 2 - 18}px`;
    }
    const x = conteudo(c), y = c.desde(1), z = c.desde(2), u = c.desde(3);
    titulo(sec, x, c);
    surgir(pag, molaAR(x - 0.1), {dx: -24, dy: 0});
    // 1: o rodapé
    mk.style.transform = `scaleX(${saida(faixa(y, 0.05, 0.6)).toFixed(4)})`;
    mk.style.opacity = (1 - saida(faixa(z, 0.05, 0.4))).toFixed(4);
    revelar(tagR, molaAR(y - 0.5));
    // a etiqueta sai com o destaque: dali em diante a ordem em foco é a do texto branco
    tagR.style.opacity = mk.style.opacity;
    // 2: a seleção varre as três linhas; a linha branca aparece dentro dela; a lupa abre a ordem ao lado
    sels.forEach((s, n) => { s.style.transform = `scaleX(${saida(faixa(z, 0.05 + n * 0.22, 0.3 + n * 0.22)).toFixed(4)})`; });
    wt.style.opacity = saida(faixa(z, 0.4, 0.6)).toFixed(4);
    tracar(lupa, saida(faixa(z, 0.75, 1.05)));
    surgir(br, molaAR(z - 0.95), {dx: -24, dy: 0});
    revelar(brTag, molaAR(z - 1.05));
    revelar(brTxt, molaAR(z - 1.15));
    // 3: o fio desce ao agente, que responde
    tracar(fio, saida(faixa(u, 0.05, 0.5)));
    surgir(ag, molaAR(u - 0.4), {dy: 0, escala: 0.06});
    surgir(bal, molaAR(u - 0.8), {dx: -24, dy: 0});
  };
})();

CENAS.casos = cartoes('casos');
CENAS.plugin = cartoes('plugin');

// plugin-tela: ícones desenhados por código (o pacote e o triângulo de aviso); a janela entra, depois o cabeçalho, os
// itens do que o plugin traz e, por último, o aviso com a borda dourada.
const C_ICONES = {
  pacote: ['0 0 64 76', ['M6 22L32 8L58 22V58L32 72L6 58Z', 'M6 22L32 36L58 22M32 36V72']],
  aviso: ['0 0 64 60', ['M32 4L61 56H3Z', 'M32 22V38', 'M32 46V47']],
};
for (const [cls, nome] of [['.c-pl-ic', 'pacote'], ['.c-av-ic', 'aviso']]) {
  for (const el of document.querySelectorAll(cls)) {
    const s = document.createElementNS(NS, 'svg');
    s.setAttribute('viewBox', C_ICONES[nome][0]);
    for (const d of C_ICONES[nome][1]) traco(s, d);
    el.appendChild(s);
  }
}
CENAS['plugin-tela'] = (() => {
  const sec = m.secao('plugin-tela'), q = (s) => sec.querySelector(s);
  const jan = q('.c-jan'), cab = q('.c-pl-cab'), traz = [q('.c-traz-et'), ...$$(sec, '.c-chip')], av = q('.c-aviso');
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    surgir(jan, molaAR(x - 0.1), {dy: 30});
    surgir(cab, molaAR(x - 0.4), {dy: 0});
    traz.forEach((el, n) => surgir(el, molaAR(x - 0.7 - n * 0.1), {dx: -16, dy: 0}));
    surgir(av, molaAR(x - 1.3), {dy: 0, escala: 0.04});
    fim(sec, x, 1.7);
  };
})();

// a4: na chegada, as quatro categorias com a frase; no clique, as frases saem, os cartões encolhem e as seis situações
// entram em onda.
CENAS.a4 = (() => {
  const sec = m.secao('a4'), cats = $$(sec, '.c-cat'), frases = $$(sec, '.c-cat-f'), sits = $$(sec, '.c-sits li');
  return (t, c) => {
    const x = conteudo(c), y = c.desde(1);
    titulo(sec, x, c);
    const sai = saida(faixa(y, 0, 0.3)), encolhe = entradaSaida(faixa(y, 0.2, 0.6));
    cats.forEach((el, n) => {
      surgir(el, molaAR(x - 0.2 - n * 0.12), {dy: 24});
      el.style.height = `${lerp(330, 170, encolhe).toFixed(2)}px`;
    });
    frases.forEach((el, n) => {
      const k = sai > 0 ? 1 - sai : molaAR(x - 0.35 - n * 0.12);
      surgir(el, k, {dy: 12});
      vis(el, k > 0.001);
    });
    sits.forEach((el, n) => {
      const k = molaAR(y - 0.6 - n * 0.1);
      surgir(el, k, {dy: 24});
      vis(el, k > 0.001);
    });
  };
})();
