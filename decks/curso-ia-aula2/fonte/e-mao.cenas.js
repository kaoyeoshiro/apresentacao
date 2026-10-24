
// ===== Bloco E: mão na massa =====
// github: a janela do navegador sobe, o endereço se digita e os arquivos entram em onda; primeiro clique, o aro dourado
// se traça em volta do botão Code; segundo, o menu abre e o aro cerca o Download ZIP; terceiro, a seta leva à pasta
// extraída, que entra item a item.
CENAS.github = (() => {
  const sec = m.secao('github'), eNav = sec.querySelector('.e-nav'), eUrl = sec.querySelector('.e-url');
  const eArqs = $$(sec, '.e-arqs li'), eMenu = sec.querySelector('.e-menu'), eAros = $$(sec, '.e-aros path');
  const eEt = sec.querySelector('.e-et-zip'), eEx = sec.querySelector('.e-extraida'), eRaiz = sec.querySelector('.e-ex-raiz');
  const eSub = $$(sec, '.e-extraida li'), eUl = sec.querySelector('.e-extraida ul');
  return (t, c) => {
    const x = conteudo(c), y1 = c.desde(1), y2 = c.desde(2), y3 = c.desde(3);
    titulo(sec, x, c);
    surgir(eNav, molaAR(x - 0.1), {dy: 30});
    digitar(eUrl, faixa(x, 0.4, 1.0), {semente: 21});
    eArqs.forEach((li, n) => surgir(li, molaAR(x - 0.6 - n * 0.08), {dx: -18, dy: 0}));
    tracar(eAros[0], saida(faixa(y1, 0, 0.5)));
    surgir(eMenu, molaAR(y2), {dy: -16});
    vis(eMenu, y2 > 0);
    tracar(eAros[1], saida(faixa(y2, 0.3, 0.8)));
    tracar(eAros[2], saida(faixa(y3, 0, 0.45)));
    revelar(eEt, molaAR(y3 - 0.3));
    surgir(eRaiz, molaAR(y3 - 0.4), {dx: -18, dy: 0});
    revelar(eUl, molaAR(y3 - 0.5));
    eSub.forEach((li, n) => surgir(li, molaAR(y3 - 0.6 - n * 0.12), {dx: -18, dy: 0}));
    [eEt, eEx].forEach((el) => vis(el, y3 > 0));
    fim(sec, x, 1.4);
  };
})();

// pratica-caso: na chegada, os passos em onda e a caixa vazia do pedido; no primeiro clique os passos saem, a caixa
// desliza para o centro e mostra a primeira parte; no segundo, a primeira parte sai e a segunda entra no lugar.
CENAS['pratica-caso'] = (() => {
  const sec = m.secao('pratica-caso'), ePassos = $$(sec, '.e-cinco li'), eBox = sec.querySelector('.e-pedido');
  const eEt = eBox.querySelector('.e-ped-et'), ePartes = $$(eBox, '.e-ped-parte'), ePontos = $$(eBox, '.e-ped-pontos i');
  return (t, c) => {
    const x = conteudo(c), y1 = c.desde(1), y2 = c.desde(2);
    titulo(sec, x, c);
    const sai1 = faixa(y1, 0, 0.35);
    ePassos.forEach((li, n) => {
      surgir(li, molaAR(x - 0.15 - n * 0.1) * (1 - sai1), {dx: -18, dy: 0});
      vis(li, sai1 < 1);
    });
    surgir(eBox, molaAR(x - 0.7), {dy: 26});
    eBox.style.left = `${(740 - 310 * molaAR(y1 - 0.2)).toFixed(1)}px`;
    revelar(eEt, molaAR(x - 0.8) * (1 - sai1));
    vis(eEt, sai1 < 1);
    const sai2 = faixa(y2, 0, 0.3);
    revelar(ePartes[0], molaAR(y1 - 0.5) * (1 - sai2));
    vis(ePartes[0], y1 > 0 && sai2 < 1);
    revelar(ePartes[1], molaAR(y2 - 0.35));
    vis(ePartes[1], y2 > 0);
    ePontos.forEach((p, n) => {
      revelar(p, molaAR(y1 - 0.5));
      vis(p, y1 > 0);
      p.classList.toggle('e-agora', n === (y2 > 0 ? 1 : 0));
    });
    fim(sec, x, 1.2);
  };
})();

// relatorio: a página 1 sobe, depois a miniatura da página 3; cada parte que importa ganha a moldura dourada e a linha
// que a liga à legenda, uma de cada vez.
CENAS.relatorio = (() => {
  const sec = m.secao('relatorio'), eP1 = sec.querySelector('.e-pag1'), eP3 = sec.querySelector('.e-pag3');
  const ePaths = $$(sec, '.e-ligas path'), eLegs = $$(sec, '.e-leg');
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    surgir(eP1, molaAR(x - 0.1), {dy: 30});
    surgir(eP3, molaAR(x - 0.3), {dy: 30});
    eLegs.forEach((leg, n) => {
      const d = 0.6 + n * 0.45;
      tracar(ePaths[2 * n], saida(faixa(x, d, d + 0.3)));
      tracar(ePaths[2 * n + 1], saida(faixa(x, d + 0.2, d + 0.45)));
      surgir(leg, molaAR(x - d - 0.35), {dx: -18, dy: 0});
    });
    fim(sec, x, 1.6);
  };
})();

// skill: a janela do SKILL.md sobe, o nome e a descrição entram, e os seis passos em onda; no clique, o texto dos
// passos vira linhas cinza e as formas de instalar entram à direita.
CENAS.skillconf = (() => {
  const sec = m.secao('skillconf'), eJan = sec.querySelector('.e-sk'), eNome = sec.querySelector('.e-sk-nome');
  const eDesc = sec.querySelector('.e-sk-desc'), ePassos = $$(sec, '.e-sk-passos li');
  const eEt = sec.querySelector('.e-inst-et'), eItens = $$(sec, '.e-inst-item');
  return (t, c) => {
    const x = conteudo(c), y1 = c.desde(1);
    titulo(sec, x, c);
    surgir(eJan, molaAR(x - 0.1), {dy: 30});
    revelar(eNome, molaAR(x - 0.4));
    revelar(eDesc, molaAR(x - 0.55));
    const cinza = faixa(y1, 0, 0.4);
    ePassos.forEach((li, n) => {
      surgir(li, molaAR(x - 0.7 - n * 0.1), {dx: -18, dy: 0});
      const txt = li.querySelector('span'), barra = li.querySelector('i');
      txt.style.opacity = (1 - cinza).toFixed(3);
      vis(txt, cinza < 1);
      barra.style.opacity = cinza.toFixed(3);
    });
    revelar(eEt, molaAR(y1 - 0.3));
    eItens.forEach((it, n) => surgir(it, molaAR(y1 - 0.5 - n * 0.25), {dy: 24}));
    [eEt, ...eItens].forEach((el) => vis(el, y1 > 0));
    fim(sec, x, 1.6);
  };
})();

// pratica2: os cinco passos em onda à esquerda e, por fim, o pedido exato na caixa da direita.
CENAS.pratica2 = (() => {
  const sec = m.secao('pratica2'), ePassos = $$(sec, '.e-cinco li'), eBox = sec.querySelector('.e-pedido');
  const eParte = eBox.querySelector('.e-ped-parte');
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    ePassos.forEach((li, n) => surgir(li, molaAR(x - 0.15 - n * 0.1), {dx: -18, dy: 0}));
    surgir(eBox, molaAR(x - 0.7), {dy: 26});
    revelar(eParte, molaAR(x - 0.9));
    fim(sec, x, 1.4);
  };
})();

CENAS.travou = cartoes('travou');
CENAS.casa = cartoes('casa');
