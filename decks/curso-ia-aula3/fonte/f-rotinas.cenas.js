// ===== Bloco F: rotinas e fecho =====
// agendavel (S.T.A.R. do bloco): na chegada, as três colunas entram em onda (título da coluna e cartões); no clique,
// a pergunta que decide sobe e a caneta dourada a sublinha.
CENAS.agendavel = (() => {
  const sec = m.secao('agendavel'), fCols = $$(sec, '.f-col'), fPerg = sec.querySelector('.f-pergunta');
  return (t, c) => {
    const x = conteudo(c), y = c.desde(1);
    titulo(sec, x, c);
    fCols.forEach((col, i) => {
      revelar(col.querySelector('.f-col-tit'), molaAR(x - 0.2 - i * 0.25));
      $$(col, '.cartao').forEach((ct, j) => surgir(ct, molaAR(x - 0.35 - i * 0.25 - j * 0.08), {dy: 26}));
    });
    revelar(fPerg, molaAR(y - 0.1));
    anotar(fPerg, saida(faixa(y, 0.6, 1.2)), {forma: 'sublinhado', semente: 7});
    fim(sec, x, 1.2);
  };
})();

// a6 (cena guia): as três tarefas entram uma a uma, depois as respostas possíveis; no clique, a segunda parte.
CENAS.a6 = (() => {
  const sec = m.secao('a6'), fTar = $$(sec, '.f-tarefas li'), fEt = sec.querySelector('.f-a6-et'), fOp = $$(sec, '.f-opcoes li');
  const fDep = sec.querySelector('.f-depois');
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    fTar.forEach((el, n) => surgir(el, molaAR(x - 0.2 - n * 0.25), {dx: -22, dy: 0}));
    revelar(fEt, molaAR(x - 0.9));
    fOp.forEach((el, n) => surgir(el, molaAR(x - 1.0 - n * 0.1), {dx: 18, dy: 0}));
    revelar(fDep, molaAR(c.desde(1) - 0.1));
  };
})();

// kit: a janela chega, o domínio e o nome do repositório sobem, a frase de baixo por último.
CENAS.kit = (() => {
  const sec = m.secao('kit'), q = (s) => sec.querySelector(s);
  const fEnd = q('.f-end'), fDom = q('.f-end-dom'), fRepo = q('.f-end-repo'), fSub = q('.f-kit-sub');
  return (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    surgir(fEnd, molaAR(x - 0.1), {dy: 24});
    revelar(fDom, molaAR(x - 0.35));
    revelar(fRepo, molaAR(x - 0.55));
    revelar(fSub, molaAR(x - 0.9));
    fim(sec, x, 1.2);
  };
})();
