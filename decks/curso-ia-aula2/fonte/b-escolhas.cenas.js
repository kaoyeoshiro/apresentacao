
// ===== Bloco B, três caminhos =====

// Ponte: a frase sobe linha a linha; a caixa "o que a IA lê" aparece e, em onda, entram nela o pedido (pequeno) e o
// que vem junto com ele; a legenda por último.
{
  const sec = m.secao('ponte'), linhas = $$(sec, '.b-pt-frase > span'), caixaP = sec.querySelector('.b-pt-caixa');
  const cabP = sec.querySelector('.b-pt-cab'), itensP = $$(sec, '.b-pt-item'), sub = sec.querySelector('.respiro-sub');
  const rot = sec.querySelector(':scope > .rotulo');
  CENAS.ponte = (t, c) => {
    const x = conteudo(c);
    revelar(rot, molaAR(x));
    linhas.forEach((el, n) => revelar(el, molaAR(x - 0.05 - n * 0.14)));
    surgir(caixaP, molaAR(x - 0.5), {dy: 0, escala: 0.9});
    revelar(cabP, molaAR(x - 0.6));
    itensP.forEach((el, n) => surgir(el, molaAR(x - 0.8 - n * 0.2), {dy: -60}));
    revelar(sub, molaAR(x - 2.0));
  };
}

// Agente: a faixa do chat (primeiro clique) vai do pedido à resposta e termina; a do agente (segundo) se desenha passo
// a passo, com a autorização entre o plano e as ações e o laço do ajuste no fim.
{
  const sec = m.secao('agente'), rots = $$(sec, '.b-ag-rot'), chat = $$(sec, '.b-ag-chat'), ag = $$(sec, '.b-ag-ag');
  const pc = $$(sec, '.b-ag-c'), fimC = sec.querySelector('.b-ag-fim'), pa = $$(sec, '.b-ag-a'), ok = sec.querySelector('.b-ag-ok');
  const laco = sec.querySelector('.b-ag-laco'), aut = sec.querySelector('.b-ag-autoriza'), aju = sec.querySelector('.b-ag-ajusta');
  const div = sec.querySelector('.b-ag-div'), rod = sec.querySelector(':scope > .rodape');
  CENAS.agente = (t, c) => {
    const x = conteudo(c), y = c.desde(1);
    titulo(sec, x, c);
    revelar(rots[0], molaAR(x - 0.1));
    surgir(chat[0], molaAR(x - 0.2), {dx: -20, dy: 0});
    tracar(pc[0], saida(faixa(x, 0.45, 0.75)));
    surgir(chat[1], molaAR(x - 0.7), {dx: -20, dy: 0});
    tracar(pc[1], saida(faixa(x, 0.95, 1.15)));
    tracar(fimC, saida(faixa(x, 1.1, 1.3)));
    // segundo clique
    div.style.transform = `scaleX(${saida(faixa(y, 0, 0.4)).toFixed(4)})`;
    div.style.transformOrigin = '0 50%';
    revelar(rots[1], molaAR(y - 0.05));
    ag.forEach((el, n) => { const d = y - 0.15 - n * 0.4; surgir(el, molaAR(d), {dx: -20, dy: 0}); vis(el, d > 0); });
    pa.forEach((p, n) => tracar(p, saida(faixa(y, 0.4 + n * 0.4, 0.6 + n * 0.4))));
    tracar(ok, saida(faixa(y, 0.85, 1.05)));
    surgir(aut, molaAR(y - 0.8), {dy: -12});
    vis(aut, y > 0.8);
    tracar(laco, saida(faixa(y, 1.95, 2.45)));
    revelar(aju, molaAR(y - 2.3));
    revelar(rod, molaAR(y - 2.5));
  };
}

// Reenvio: cada conversa aparece e os três papéis sobem pelo campo de envio até o balão; a etiqueta dela acende no
// fim. A primeira no primeiro clique; a segunda e a terceira, em seguida, no segundo.
{
  const sec = m.secao('reenvio'), convs = $$(sec, '.b-conv'), rod = sec.querySelector(':scope > .rodape');
  CENAS.reenvio = (t, c) => {
    const x = conteudo(c), y = c.desde(1);
    titulo(sec, x, c);
    convs.forEach((cv, i) => {
      const d = i === 0 ? x - 0.25 : y - 0.05 - (i - 1) * 0.95;
      const k = molaAR(d);
      surgir(cv, k, {dy: 24});
      vis(cv, d > 0);
      $$(cv, '.b-anexos img').forEach((im, j) => surgir(im, molaAR(d - 0.3 - j * 0.12, {resposta: 0.55}), {dy: 170}));
      revelar(cv.querySelector('.b-conv-msg'), molaAR(d - 0.8));
      surgir(cv.querySelector('.b-tag'), molaAR(d - 1.0), {dy: 0, escala: 0.4});
    });
    revelar(rod, molaAR(y - 2.0));
  };
}

// Matriz: o cartão do Projeto e suas três coisas (primeiro clique); no segundo, a pergunta da pasta e as duas respostas.
{
  const sec = m.secao('matriz'), pj = sec.querySelector('.b-pj'), its = $$(sec, '.b-pj-it'), leg = sec.querySelector('.b-pj-leg');
  const et = sec.querySelector('.b-pj-et'), sem = sec.querySelector('.b-pj-sem'), com = sec.querySelector('.b-pj-com');
  const rod = sec.querySelector(':scope > .rodape');
  CENAS.matriz = (t, c) => {
    const x = conteudo(c), y = c.desde(1);
    titulo(sec, x, c);
    surgir(pj, molaAR(x - 0.1), {dy: 24});
    its.forEach((el, n) => revelar(el, molaAR(x - 0.5 - n * 0.2)));
    revelar(leg, molaAR(x - 1.3));
    revelar(et, molaAR(y - 0.05));
    surgir(sem, molaAR(y - 0.3), {dx: 30, dy: 0});
    surgir(com, molaAR(y - 0.7), {dx: 30, dy: 0});
    revelar(rod, molaAR(y - 1.3));
  };
}

// Projeto: a janela do app sobe, a coluna das conversas e o painel do Projeto entram linha a linha; no segundo
// clique, a seta dourada aponta o lápis das instruções e entram a anotação e a linha do ChatGPT.
{
  const sec = m.secao('projeto'), app = sec.querySelector('.b-app'), esq = $$(sec, '.b-app-esq > *'), pcs = $$(sec, '.b-pc');
  const setas = $$(sec, '.b-seta-p path'), anota = sec.querySelector('.b-anota'), gpt = sec.querySelector('.b-chatgpt');
  CENAS.projeto = (t, c) => {
    const x = conteudo(c), y = c.desde(1);
    titulo(sec, x, c);
    surgir(app, molaAR(x - 0.05), {dy: 30});
    esq.forEach((el, n) => surgir(el, molaAR(x - 0.3 - n * 0.08), {dy: 14}));
    pcs.forEach((el, n) => surgir(el, molaAR(x - 0.45 - n * 0.12), {dx: 24, dy: 0}));
    tracar(setas[0], saida(faixa(y, 0.05, 0.45)));
    tracar(setas[1], saida(faixa(y, 0.4, 0.6)));
    revelar(anota, molaAR(y - 0.25));
    revelar(gpt, molaAR(y - 0.7));
  };
}

// Pasta: cinco motivos, um por clique (a cena em partes da base).
CENAS.pasta = partes('pasta');

// Teste: as 348 páginas contam e a barra do anexo enche (primeiro clique); no segundo, a data se digita na busca, o
// tempo aparece e a barra da pasta encolhe de 100% até 0,2%.
{
  const sec = m.secao('teste'), n348 = sec.querySelector('.b-348'), leg = sec.querySelector('.b-348-leg'), n129 = sec.querySelector('.b-129');
  const barLegs = $$(sec, '.b-bar-leg'), bars = $$(sec, '.b-bar'), chat = sec.querySelector('.b-bar-chat');
  const busca = sec.querySelector('.b-busca'), txt = sec.querySelector('.b-busca-txt'), res = sec.querySelector('.b-busca-res');
  const lido = sec.querySelector('.b-lido');
  const MINIMO = 0.012;   // a fatia de 0,2% (1,8 px) desenhada com 11 px, para a sala ver que existe
  CENAS.teste = (t, c) => {
    const x = conteudo(c), y = c.desde(1);
    titulo(sec, x, c);
    const kc = saida(faixa(x, 0.1, 1.3));
    surgir(n348, molaAR(x - 0.05), {dy: 0});
    contar(n348, kc, 0, 348);
    revelar(leg, molaAR(x - 0.3));
    contar(n129, kc, 0, 129, {sufixo: ' mil'});
    revelar(barLegs[0], molaAR(x - 0.7));
    surgir(bars[0], molaAR(x - 0.8), {dy: 0});
    chat.style.transform = `scaleX(${saida(faixa(x, 0.95, 1.7)).toFixed(4)})`;
    // segundo clique
    surgir(busca, molaAR(y - 0.05), {dy: 16});
    digitar(txt, faixa(y, 0.25, 0.85));
    revelar(res, molaAR(y - 0.95));
    revelar(barLegs[1], molaAR(y - 1.05));
    surgir(bars[1], molaAR(y - 1.05), {dy: 0});
    const encolhe = entradaSaida(faixa(y, 1.35, 2.05));
    lido.style.width = `${(100 * lerp(1, MINIMO, encolhe)).toFixed(3)}%`;
    lido.style.opacity = String(clamp((y - 1.1) * 4));
    fim(sec, x, 1.4);
  };
}

// Lei: as duas colunas entram, primeiro a do que se guarda; no segundo clique, a regra para o agente.
{
  const sec = m.secao('lei'), lados = $$(sec, '.b-lado'), fio = sec.querySelector('.b-lado-fio'), regra = sec.querySelector('.b-regra');
  CENAS.lei = (t, c) => {
    const x = conteudo(c), y = c.desde(1);
    titulo(sec, x, c);
    lados.forEach((lado, n) => {
      const d = x - 0.15 - n * 0.45;
      revelar(lado.querySelector('.b-lado-tit'), molaAR(d - 0.05));
      $$(lado, 'li').forEach((li, j) => revelar(li, molaAR(d - 0.25 - j * 0.1)));
    });
    fio.style.transform = `scaleY(${saida(faixa(x, 0.3, 0.8)).toFixed(4)})`;
    fio.style.transformOrigin = '50% 0';
    surgir(regra, molaAR(y - 0.05), {dy: 20});
    vis(regra, y > 0);
  };
}

// PDF ou Markdown: a página entra e o rodapé repetido se marca (primeiro clique); no segundo, o fio sai da cláusula
// terceira do PDF até o Markdown limpo, e as três vantagens entram em fila.
{
  const sec = m.secao('mdpdf'), etPdf = sec.querySelector('.b-et-pdf'), pdf = sec.querySelector('.b-pdf');
  const ruido = sec.querySelector('.b-ruido'), clausula = sec.querySelector('.b-clausula'), rLeg = sec.querySelector('.b-ruido-leg');
  const etMd = sec.querySelector('.b-et-md'), md = sec.querySelector('.b-md'), mdH = sec.querySelector('.b-md-h'), mdP = sec.querySelector('.b-md-p');
  const ganhos = $$(sec, '.b-ganhos li'), fio = sec.querySelector('.b-md-fio path');
  CENAS.mdpdf = (t, c) => {
    const x = conteudo(c), y = c.desde(1);
    titulo(sec, x, c);
    revelar(etPdf, molaAR(x - 0.1));
    surgir(pdf, molaAR(x - 0.15), {dy: 24});
    surgir(ruido, molaAR(x - 0.75), {dy: 0, escala: 0.15});
    revelar(rLeg, molaAR(x - 0.95));
    // segundo clique
    surgir(clausula, molaAR(y - 0.05), {dy: 0, escala: 0.1});
    vis(clausula, y > 0);
    tracar(fio, saida(faixa(y, 0.15, 0.65)));
    revelar(etMd, molaAR(y - 0.3));
    surgir(md, molaAR(y - 0.4), {dx: 30, dy: 0});
    vis(md, y > 0);
    revelar(mdH, molaAR(y - 0.55));
    revelar(mdP, molaAR(y - 0.7));
    ganhos.forEach((li, n) => { surgir(li, molaAR(y - 1.0 - n * 0.15), {dy: 16}); vis(li, y > 0); });
  };
}

// Converter: o "não" chega grande; as três regras entram de cima para baixo e o rodapé por último.
{
  const sec = m.secao('converter'), nao = sec.querySelector('.b-nao'), cs = $$(sec, '.cartao'), rod = sec.querySelector(':scope > .rodape');
  CENAS.converter = (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    surgir(nao, molaAR(x - 0.2, {resposta: 0.6}), {dy: 0, escala: 0.2});
    cs.forEach((el, n) => surgir(el, molaAR(x - 0.55 - n * 0.18), {dx: 30, dy: 0}));
    revelar(rod, molaAR(x - 1.3));
  };
}

CENAS.codigo = cartoes('codigo');

// Ferramentas: o par da entrega (primeiro clique), o par da pasta (segundo) e a faixa do Cowork (terceiro).
{
  const sec = m.secao('ferramentas'), cabs = $$(sec, '.b-par-cab'), emps = $$(sec, '.b-emp'), cels = $$(sec, '.b-ferr');
  const cowork = sec.querySelector('.b-cowork');
  CENAS.ferramentas = (t, c) => {
    const x = conteudo(c), y = c.desde(1), z = c.desde(2);
    titulo(sec, x, c);
    emps.forEach((el, n) => revelar(el, molaAR(x - 0.15 - n * 0.1)));
    cabs.forEach((el, n) => revelar(el, molaAR((n === 0 ? x - 0.25 : y - 0.05))));
    let fila = [0, 0];
    cels.forEach((el) => {
      const col = Number(el.dataset.col), d = (col === 0 ? x - 0.45 : y - 0.2) - fila[col]++ * 0.2;
      surgir(el, molaAR(d), {dy: 24});
      vis(el, d > 0);
    });
    surgir(cowork, molaAR(z - 0.05), {dy: 24});
    vis(cowork, z > 0);
  };
}

// Diferença: uma linha da grade por clique (cabeçalho e "para que serve" no primeiro), cada linha em onda.
{
  const sec = m.secao('diferenca'), gs = $$(sec, '.b-g');
  CENAS.diferenca = (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    const ini = [x - 0.1, x - 0.5, c.desde(1) - 0.05, c.desde(2) - 0.05];
    gs.forEach((el) => {
      const l = Number(el.dataset.l), d = ini[l] - Number(el.dataset.c) * 0.1;
      revelar(el, molaAR(d));
    });
  };
}

// Escolher: uma pergunta por clique; a seta se traça e a rota entra ao lado.
{
  const sec = m.secao('escolher'), linhas = $$(sec, '.b-esc'), setas = $$(sec, '.b-esc-setas path');
  CENAS.escolher = (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    linhas.forEach((ln, n) => {
      const d = n === 0 ? x - 0.3 : c.desde(n) - 0.05;
      revelar(ln.querySelector('.b-esc-q'), molaAR(d));
      tracar(setas[n], saida(faixa(d, 0.25, 0.6)));
      surgir(ln.querySelector('.b-esc-r'), molaAR(d - 0.5), {dx: -24, dy: 0});
    });
  };
}

// Vários: os sete agentes entram em onda (primeiro clique); no segundo, as linhas se traçam até o integrador, que acende.
{
  const sec = m.secao('varios'), et = sec.querySelector('.b-v-et'), cs = $$(sec, '.b-vc'), camada = sec.querySelector('.b-vlinhas');
  const integ = sec.querySelector('.b-vint'), rod = sec.querySelector(':scope > .rodape');
  const linhas = cs.map((_, i) => traco(camada, `M${258 + 234 * i} 540 L${700 + 87 * i} 735`));
  CENAS.varios = (t, c) => {
    const x = conteudo(c), y = c.desde(1);
    titulo(sec, x, c);
    revelar(et, molaAR(x - 0.1));
    cs.forEach((el, n) => surgir(el, molaAR(x - 0.35 - n * 0.14), {dy: 24}));
    linhas.forEach((p, n) => tracar(p, saida(faixa(y, 0.05 + n * 0.05, 0.5 + n * 0.05))));
    surgir(integ, molaAR(y - 0.6), {dy: 0, escala: 0.2});
    vis(integ, y > 0.55);
    revelar(rod, molaAR(y - 1.1));
  };
}

// Quem despacha: uma linha por vez, em onda.
{
  const sec = m.secao('varios2'), ps = $$(sec, '.b-sa p'), rod = sec.querySelector(':scope > .rodape');
  CENAS.varios2 = (t, c) => {
    const x = conteudo(c);
    titulo(sec, x, c);
    ps.forEach((p, n) => revelar(p, molaAR(x - 0.2 - Math.floor(n / 2) * 0.35 - (n % 2) * 0.08)));
    revelar(rod, molaAR(x - 1.2));
  };
}

// PDF lido inteiro? As doze páginas entram na mesa do chat (primeiro clique); na pasta, entram esmaecidas e uma acende (segundo).
{
  const sec = m.secao('pdflido'), pe = $$(sec, '.b-pdfe .b-pg'), pd = $$(sec, '.b-pdfd .b-pg'), on = sec.querySelector('.b-pg-on');
  const ets = $$(sec, '.etiqueta'), txs = $$(sec, '.b-pdftx'), caixas = $$(sec, '.b-pdfcaixa'), rod = sec.querySelector(':scope > .rodape');
  CENAS.pdflido = (t, c) => {
    const x = conteudo(c), y = c.desde(1);
    titulo(sec, x, c);
    revelar(ets[0], molaAR(x - 0.1)); surgir(caixas[0], molaAR(x - 0.15), {dy: 0, escala: 0.9});
    pe.forEach((el, n) => surgir(el, molaAR(x - 0.4 - n * 0.06), {dy: -30}));
    revelar(txs[0], molaAR(x - 1.3));
    revelar(ets[1], molaAR(y - 0.1)); surgir(caixas[1], molaAR(y - 0.15), {dy: 0, escala: 0.9});
    pd.forEach((el, n) => { surgir(el, molaAR(y - 0.4 - n * 0.04), {dy: 0}); if (el !== on) el.style.opacity = String(0.35 * Number(el.style.opacity || 1)); });
    on.style.transform = '';
    revelar(txs[1], molaAR(y - 1.3));
    revelar(rod, molaAR(y - 1.6));
  };
}
