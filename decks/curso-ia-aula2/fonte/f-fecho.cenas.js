
// ===== Bloco F: fecho =====
// levar é o arquétipo tempo da biblioteca: sem cena própria.

// dia2: "Dia" e o "2" sobem, e a lista entra item a item, de cima para baixo.
CENAS.dia2 = (() => {
  const sec = m.secao('dia2'), fDia = $$(sec, '.f-dia span'), fItens = $$(sec, '.f-lista li');
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    fDia.forEach((el, n) => surgir(el, molaAR(x - 0.1 - n * 0.25), {dy: 40}));
    fItens.forEach((li, n) => surgir(li, molaAR(x - 0.5 - n * 0.12), {dx: -20, dy: 0}));
    fim(sec, x, 1.4);
  };
})();

// fecho (fundo claro, como o encerramento da Aula 1): o logo sobe, o fio se traça de cima para baixo e o texto entra
// linha a linha; a mensagem encolhe, no primeiro quadro, até a linha mais larga caber em 1000 px.
CENAS.fecho = (() => {
  const sec = m.secao('fecho'), fLogo = sec.querySelector('.f-logo'), fFio = sec.querySelector('.f-fio');
  const fLinhas = [sec.querySelector('.rotulo'), ...$$(sec, '.f-tit > span'), sec.querySelector('.f-obg')];
  let pronto = false;
  return (t, c) => {
    if (!pronto) {
      pronto = true;
      const tit = sec.querySelector('.f-tit'), largura = Math.max(...$$(sec, '.f-tit > span').map((el) => el.scrollWidth));
      if (largura > 1000) tit.style.fontSize = `${Math.floor(124 * 1000 / largura)}px`;
    }
    const x = conteudo(c);
    surgir(fLogo, molaAR(x - 0.15, {resposta: 0.7, amortecimento: 0.9}), {dy: 24});
    fFio.style.transform = `scaleY(${saida(faixa(x, 0.55, 1.1)).toFixed(4)})`;
    fLinhas.forEach((el, n) => revelar(el, molaAR(x - 0.8 - n * 0.16)));
    fim(sec, x, 1.6);
  };
})();
