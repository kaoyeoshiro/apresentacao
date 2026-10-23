
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
CENAS.travou = cartoes('travou');
