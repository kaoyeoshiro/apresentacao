
// ===== Bloco E: mão na massa =====
// pratica2: os títulos das colunas entram em onda, cada passo logo depois do seu título, e por fim o pedido para copiar.
CENAS.pratica2 = (() => {
  const sec = m.secao('pratica2'), eCols = $$(sec, '.e-col'), ePedido = sec.querySelector('.e-pedido');
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    eCols.forEach((col, n) => {
      const t0 = 0.15 + n * 0.22;
      surgir(col.querySelector('.e-col-tit'), molaAR(x - t0), {dy: 20});
      $$(col, 'li').forEach((li, k) => surgir(li, molaAR(x - t0 - 0.12 - k * 0.1), {dx: -18, dy: 0}));
    });
    surgir(ePedido, molaAR(x - 1.0), {dy: 26});
    fim(sec, x, 1.4);
  };
})();

// escritorio: o logo sobe, e as oito regras entram em onda, da esquerda para a direita e de cima para baixo; o filete
// de cada regra se traça antes do texto.
CENAS.escritorio = (() => {
  const sec = m.secao('escritorio'), eLogo = sec.querySelector('.e-logo-cx'), eRegras = $$(sec, '.e-regras li');
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    surgir(eLogo, molaAR(x - 0.1), {dy: 24});
    eRegras.forEach((li, n) => surgir(li, molaAR(x - 0.5 - n * 0.1), {dy: 24}));
    fim(sec, x, 1.4);
  };
})();

// desafio: os três passos da missão entram com as setas entre eles; depois as três janelas, uma por ferramenta, e o
// comando de cada uma se digita na caixa, uma depois da outra.
CENAS.desafio = (() => {
  const sec = m.secao('desafio'), eMissao = $$(sec, '.e-missao li'), eSetas = $$(sec, '.e-setas path');
  const eEt = sec.querySelector('.e-et-criar'), eJans = $$(sec, '.e-jan'), eCmds = $$(sec, '.e-cmd');
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    eMissao.forEach((li, n) => surgir(li, molaAR(x - 0.1 - n * 0.32), {dx: -18, dy: 0}));
    eSetas.forEach((p, n) => tracar(p, saida(faixa(x, 0.3 + n * 0.32, 0.55 + n * 0.32))));
    revelar(eEt, molaAR(x - 1.0));
    eJans.forEach((j, n) => surgir(j, molaAR(x - 1.1 - n * 0.12), {dy: 30}));
    eCmds.forEach((el, n) => digitar(el, faixa(x, 1.6 + n * 0.5, 2.05 + n * 0.5), {semente: 11 + n}));
    fim(sec, x, 3.0);
  };
})();

// alvo: a página do Word sobe; cada parte que importa ganha a moldura dourada e a linha que a liga à legenda, uma de
// cada vez, de cima para baixo.
CENAS.alvo = (() => {
  const sec = m.secao('alvo'), eFolha = sec.querySelector('.e-folha'), ePaths = $$(sec, '.e-ligas path'), eLegs = $$(sec, '.e-leg');
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    surgir(eFolha, molaAR(x - 0.1), {dy: 30});
    eLegs.forEach((leg, n) => {
      const d = 0.6 + n * 0.45;
      tracar(ePaths[2 * n], saida(faixa(x, d, d + 0.3)));
      tracar(ePaths[2 * n + 1], saida(faixa(x, d + 0.2, d + 0.45)));
      surgir(leg, molaAR(x - d - 0.35), {dx: -18, dy: 0});
    });
    fim(sec, x, 2.2);
  };
})();

// pratica3: os cinco passos em onda à esquerda e, por fim, o pedido exato do desafio na caixa da direita.
CENAS.pratica3 = (() => {
  const sec = m.secao('pratica3'), eCinco = $$(sec, '.e-cinco li'), ePed = sec.querySelector('.e-pedido2');
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    eCinco.forEach((li, n) => surgir(li, molaAR(x - 0.15 - n * 0.1), {dx: -18, dy: 0}));
    surgir(ePed, molaAR(x - 0.8), {dy: 26});
    fim(sec, x, 1.3);
  };
})();

CENAS.travou = cartoes('travou');
