// ===== Bloco A: abertura =====
// Capa (fundo claro, como a da Aula 2): o logo sobe, o fio se traça de cima para baixo e o texto entra linha a linha.
CENAS.capa = (() => {
  const sec = m.secao('capa'), logo = sec.querySelector('.a-logo-cj'), fio = sec.querySelector('.a-cp-fio');
  const linhas = [sec.querySelector('.rotulo'), ...$$(sec, '.a-cp-tit > span'), sec.querySelector('.a-cp-sub')];
  let pronto = false;
  return (t, c) => {
    if (!pronto) {
      pronto = true;
      const tit = sec.querySelector('.a-cp-tit'), largura = Math.max(...$$(sec, '.a-cp-tit > span').map((el) => el.offsetWidth));
      if (largura > 1000) tit.style.fontSize = `${Math.floor(124 * 1000 / largura)}px`;
    }
    const x = c.desde(0);
    surgir(logo, molaAR(x - 0.15, {resposta: 0.7, amortecimento: 0.9}), {dy: 24});
    fio.style.transform = `scaleY(${saida(faixa(x, 0.55, 1.1)).toFixed(4)})`;
    linhas.forEach((el, n) => revelar(el, molaAR(x - 0.8 - n * 0.16)));
    fim(sec, x, 1.6);
  };
})();
