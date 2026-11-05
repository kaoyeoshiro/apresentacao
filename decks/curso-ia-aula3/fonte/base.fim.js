
// Links das práticas: o clique abre a página em nova aba e não avança o slide.
for (const a of document.querySelectorAll('#mundo a[href]')) a.addEventListener('click', (e) => e.stopPropagation());

palco({slides: m.slides, desenhar: m.desenhar, blocos, autoplay: true, cenas: m.cenas(CENAS)});
