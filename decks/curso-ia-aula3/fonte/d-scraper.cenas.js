// ===== Bloco D: scraper =====
// a5 (guia): as três placas entram em fila; a regra da votação por último.
CENAS.a5 = (() => {
  const sec = m.secao('a5'), placas = $$(sec, '.d-temas li'), voto = sec.querySelector('.d-voto');
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    placas.forEach((el, n) => surgir(el, molaAR(x - 0.2 - n * 0.18), {dy: 30}));
    revelar(voto, molaAR(x - 0.9));
    fim(sec, x, 1.2);
  };
})();

// etapa2-pedido: a janela entra, o pedido sobe e o [tema] acende por último.
CENAS['etapa2-pedido'] = (() => {
  const sec = m.secao('etapa2-pedido'), jan = sec.querySelector('.d-cc'), ped = sec.querySelector('.d-cc-pedido'), tema = sec.querySelector('.d-tema');
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    surgir(jan, molaAR(x - 0.1), {dy: 30});
    revelar(ped, molaAR(x - 0.5));
    tema.style.setProperty('--d-acende', saida(faixa(x, 1.2, 1.7)).toFixed(4));
    fim(sec, x, 1.6);
  };
})();

// conferir (três variantes iguais): a planilha entra com a legenda; cada clique troca a linha em foco, traça o fio
// dourado e traz o espelho daquela linha; a legenda sai no primeiro clique e cada espelho sai no clique seguinte.
const dConferir = (id) => {
  const sec = m.secao(id), csv = sec.querySelector('.d-csv'), lins = $$(sec, '.d-lin'), realces = $$(sec, '.d-realce');
  const leg = sec.querySelector('.d-leg'), fios = $$(sec, '.d-fios path'), esps = $$(sec, '.d-esp');
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    surgir(csv, molaAR(x - 0.15), {dy: 24});
    lins.forEach((el, n) => surgir(el, molaAR(x - 0.45 - n * 0.15), {dx: -20, dy: 0}));
    const kLeg = c.desde(1) > 0 ? 1 - faixa(c.desde(1), 0, 0.3) : molaAR(x - 1.0);
    surgir(leg, kLeg, {dy: 18});
    vis(leg, kLeg > 0.001);
    for (let n = 0; n < 3; n++) {
      const d = c.desde(n + 1), sai = n < 2 ? faixa(c.desde(n + 2), 0, 0.3) : 0;
      realces[n].style.opacity = (sai > 0 ? 1 - sai : saida(faixa(d, 0, 0.3))).toFixed(4);
      tracar(fios[n], sai > 0 ? 1 - sai : saida(faixa(d, 0.15, 0.7)));
      const k = sai > 0 ? 1 - sai : molaAR(d - 0.55);
      surgir(esps[n], k, {dy: 20});
      vis(esps[n], k > 0.001);
    }
    fim(sec, x, 1.4);
  };
};
CENAS['conferir-execucao'] = dConferir('conferir-execucao');
CENAS['conferir-improbidade'] = dConferir('conferir-improbidade');
CENAS['conferir-icms'] = dConferir('conferir-icms');

// limites: os cartões do ajudante da base.
CENAS.limites = cartoes('limites');

// scraper-cap: sem foto, o "em lote" cresce até 1040 px, para a abertura respirar como respiro.
CENAS['scraper-cap'] = {largura: 1040};
