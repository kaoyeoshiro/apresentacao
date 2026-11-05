// ===== Bloco A: abertura =====
// Ícones desenhados por código (caixas do diagrama "pecas"): arquivo, tomada, pacote e relógio, em viewBox 64 x 76.
const A_ICONES = {
  arquivo: ['M8 4H40L56 20V72H8Z', 'M40 4V20H56', 'M18 40H46M18 52H46M18 64H36'],
  tomada: ['M14 30H50V50Q50 64 36 64H28Q14 64 14 50Z', 'M24 30V10M40 30V10', 'M32 64V76'],
  pacote: ['M6 22L32 8L58 22V58L32 72L6 58Z', 'M6 22L32 36L58 22M32 36V72'],
  relogio: ['M32 12A28 28 0 1 0 32.01 12', 'M32 24V40L44 48'],
};
for (const el of document.querySelectorAll('.a-ic[data-ic]')) {
  const s = document.createElementNS(NS, 'svg');
  s.setAttribute('viewBox', '0 0 64 76');
  for (const d of A_ICONES[el.dataset.ic]) traco(s, d);
  el.appendChild(s);
}

// pecas: agente e skill; o conector; o plugin, cujo tracejado embrulha os dois; a rotina embaixo.
CENAS.pecas = (() => {
  const sec = m.secao('pecas'), q = (s) => sec.querySelector(s);
  const ag = q('.a-agente'), sk = q('.a-skill'), co = q('.a-conector'), pl = q('.a-plugin'), ro = q('.a-rotina');
  const dSk = q('.a-d-sk'), dCo = q('.a-d-co'), dPl = q('.a-d-pl'), dRo = q('.a-d-ro');
  return (t, c) => {
    const x = conteudo(c), y = c.desde(1), z = c.desde(2), w = c.desde(3);
    titulo(sec, x, c);
    surgir(ag, molaAR(x - 0.1), {dy: 0, escala: 0.06});
    tracar(dSk, saida(faixa(x, 0.35, 0.65)));
    surgir(sk, molaAR(x - 0.5), {dx: -30, dy: 0});
    tracar(dCo, saida(faixa(y, 0.05, 0.35)));
    surgir(co, molaAR(y - 0.2), {dx: 30, dy: 0});
    surgir(pl, molaAR(z - 0.05), {dy: -30});
    const kp = saida(faixa(z, 0.35, 1.0));
    tracar(dPl, kp);
    if (kp >= 1) { dPl.removeAttribute('pathLength'); dPl.style.strokeDasharray = ''; }
    tracar(dRo, saida(faixa(w, 0.05, 0.3)));
    surgir(ro, molaAR(w - 0.2), {dy: 30});
    fim(sec, x, 1.2);
  };
})();
