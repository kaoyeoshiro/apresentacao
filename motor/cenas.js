// Biblioteca de cenas do plano contínuo: o maquinário que a prévia do curso de IA (decks/previa-curso-ia) escreveu à
// mão, generalizado. O mundo (posição de cada slide, a trilha dourada de circuito, as zonas noite e os traços das
// aberturas que descem até a trilha), os andamentos de viagem e um ajudante por arquétipo. O texto fica no HTML das
// sections (o oráculo mede o HTML); os dados de cada cena vão em atributos data-*. Tudo é função pura do tempo, com
// medidas feitas uma vez, no primeiro quadro, depois das fontes. Contrato: docs/cenas.md. Estilos: motor/cenas.css.
//
//   const m = mundo(slides);
//   palco({slides: m.slides, cenas: m.cenas(), desenhar: m.desenhar});
import {planejar, revelar, surgir, tracar, contar, video, digitar, voar, anotar, kenburns, caixa,
        molaAR, escalonar, faixa, saida, entradaSaida, sair, clamp, lerp, ruido, aleatorio} from './palco.js';
import {trilha as alvos} from './tempo.js';

const W = 1920, H = 1080;
const NS = 'http://www.w3.org/2000/svg';
const svg = (pai, tag, attrs) => { const el = document.createElementNS(NS, tag); for (const k in attrs) el.setAttribute(k, attrs[k]); pai.appendChild(el); return el; };
const html = (pai, tag, cls, txt) => { const el = document.createElement(tag); if (cls) el.className = cls; if (txt !== undefined) el.textContent = txt; pai.appendChild(el); return el; };
const vis = (el, sim) => { el.style.visibility = sim ? '' : 'hidden'; };
const sem = (k) => 1 - k;
const duas = (x) => Math.round(x * 100) / 100;
const ICONE = '<svg viewBox="0 0 34 42"><path d="M2 2h20l10 10v28H2z M22 2v10h10"/></svg>';

// ---------- andamentos de viagem ----------
// `viagem` em segundos e `recuo` (0 a 1) como no palco. O padrão de cada slide sai do arquétipo e do vizinho (ver
// mundo()); `andamento: 'nome'` na entrada do slide escolhe outro, e `viagem`/`recuo` explícitos vencem os dois.
export const ANDAMENTOS = {
	corte: {viagem: 0, recuo: 0},           // muda o assunto: a câmera salta, o título já está lá
	curta: {viagem: 0.8, recuo: 0.06},      // vizinho no mesmo capítulo
	media: {viagem: 1.0, recuo: 0.12},      // sai de uma abertura (os traços descem) ou leva objetos de um slide a outro
	longa: {viagem: 1.5, recuo: 0.15},      // entra num momento forte (demonstração) ou sai de um mergulho
	capitulo: {viagem: 2.2, recuo: 0.22},   // muda de capítulo: a câmera recua e a plateia vê a trilha
	mergulho: {viagem: 1.4, recuo: 0},      // a câmera entra numa região de um slide (vídeo da demonstração)
};

// ---------- geometria do mundo ----------
const BASE_Y = 975, X0 = 120, X1 = 1800;               // a trilha corre em y 975, de x 120 a 1800 de cada slide
const VAO = 400, VAO_ABERTURA = 1100, VAO_CAPITULO = 1000;
const DEGRAUS = [240, -300, 0, 260, -300, 280, -180];   // subidas e descidas entre slides: as curvas de 45° da placa
// Traços das aberturas: chegam pela borda direita, acabam em ilhas e, na viagem ao slide seguinte, continuam para fora,
// descem em 45° e se juntam à trilha (paralelos, sem se cruzar). Pedem 1000 px de vão e o vizinho na mesma altura.
const SAIDA_Y = [250, 310, 370, 430], ILHA_X = [1690, 1740, 1790, 1835], DOBRA = [290, 210, 130, 50];

// Segundos do conteúdo de um slide: começa antes de a câmera pousar, 0,5 s nas viagens curtas e na segunda metade
// das longas (capítulo, demonstração, fecho), para a viagem não atravessar um quadro vazio.
const lideranca = (viagem) => Math.max(0.5, viagem / 2);
const espera = (viagem) => Math.max(0, viagem - lideranca(viagem));   // segundos do passo antes de o conteúdo começar
export const conteudo = (c) => c.desde(0) - espera(c.slide.viagem ?? 0);

// Cor computada de uma variável do tema, em 0..255 (o Chrome devolve color-mix como color(srgb r g b)).
const corDe = (sonda, nome) => {
	sonda.style.color = `var(${nome})`;
	const c = getComputedStyle(sonda).color, n = c.match(/[\d.]+/g).map(Number);
	return c.startsWith('color(') ? n.slice(0, 3).map((v) => v * 255) : n.slice(0, 3);
};
const lum = (rgb) => rgb.map((v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; })
	.reduce((s, v, i) => s + v * [0.2126, 0.7152, 0.0722][i], 0);
const contraste = (a, b) => { const [x, y] = [lum(a), lum(b)].sort((p, q) => q - p); return (x + 0.05) / (y + 0.05); };

// ---------- o mundo ----------
// Recebe a lista de slides do palco, com campos a mais (ver docs/cenas.md): `andamento`, `dy`, `vao`, `x`, `y`,
// `mergulho: {em, x, y, f, furos}` e `video: [de, dur]`. Posiciona as sections, cria a trilha e as zonas noite e
// devolve os slides prontos para o palco (câmera, viagem, recuo e passos preenchidos), as cenas e o desenhar global.
export function mundo(lista, {degraus = DEGRAUS} = {}) {
	const palcoEl = document.getElementById('palco'), mundoEl = document.getElementById('mundo');
	if (!mundoEl) throw new Error('o plano contínuo precisa de <div id="mundo"> dentro de #palco');
	const secao = (id) => mundoEl.querySelector(`section[data-slide="${id}"]`);
	const ids = new Set(lista.map((s) => s.id));
	for (const sec of mundoEl.querySelectorAll('section[data-slide]')) {
		if (ids.has(sec.dataset.slide)) continue;
		sec.style.display = 'none';   // section sem entrada na lista: fora do palco
		console.warn(`cenas: section "${sec.dataset.slide}" não está na lista de slides e fica escondida`);
	}
	const tipoDe = (s) => (s && !s.mergulho ? secao(s.id)?.dataset.arquetipo || null : null);

	// 1. andamento, câmera e passos
	const slides = lista.map((s, i) => {
		const sec = s.mergulho ? null : secao(s.id);
		if (!s.mergulho && !sec) throw new Error(`cenas: slide "${s.id}" sem <section data-slide="${s.id}">`);
		const tipo = tipoDe(s), ant = lista[i - 1], tipoAnt = tipoDe(ant);
		if (tipo && !ARQUETIPOS[tipo]) throw new Error(`cenas: arquétipo "${tipo}" não existe (${Object.keys(ARQUETIPOS).join(', ')})`);
		// "capítulo", com acento, vale como "capitulo" (o roteiro escreve com acento)
		const nome = (s.andamento?.normalize('NFD').replace(/[\u0300-\u036f]/g, '')) ?? (i === 0 ? 'corte' : s.mergulho ? 'mergulho' : tipo === 'abertura' ? 'capitulo'
			: tipoAnt === 'abertura' || tipo === 'viagem' ? 'media' : ant?.mergulho || tipo === 'demonstracao' ? 'longa' : 'curta');
		const and = ANDAMENTOS[nome];
		if (!and) throw new Error(`cenas: andamento "${nome}" não existe (${Object.keys(ANDAMENTOS).join(', ')})`);
		const viagem = i === 0 ? 0 : s.viagem ?? and.viagem;
		const o = {...s, andamento: nome, viagem, recuo: s.recuo ?? and.recuo, camera: s.camera ?? true};
		if (!o.passos) {
			const fimVideo = s.video ? s.video[0] + s.video[1] + 0.2 : 0;
			const dur = s.mergulho ? Math.max(viagem + 1.2, fimVideo)
				: Math.max(espera(viagem) + (tipo ? DURACAO[tipo](sec) : 2), viagem + 0.4, fimVideo);   // pousa antes da parada
			o.passos = [duas(dur)];
		}
		return o;
	});

	// 2. posições: cada slide depois do anterior, com vão e degrau; a abertura pede vão largo e o vizinho na mesma altura
	const pos = {};
	let ant = null, k = 0;
	for (const s of slides) {
		if (s.mergulho) continue;
		const sec = secao(s.id), tipo = sec.dataset.arquetipo || null;
		let x = s.x ?? 0, y = s.y ?? 0;
		if (ant) {
			const aposAbertura = ant.tipo === 'abertura';
			x = s.x ?? ant.x + W + (s.vao ?? (aposAbertura ? VAO_ABERTURA : s.andamento === 'capitulo' ? VAO_CAPITULO : VAO));
			y = s.y ?? ant.y + (s.dy ?? (aposAbertura ? 0 : degraus[k++ % degraus.length]));
		}
		sec.style.left = `${x}px`;
		sec.style.top = `${y}px`;
		ant = pos[s.id] = {id: s.id, x, y, tipo, noite: sec.classList.contains('noite')};
	}
	const nos = slides.filter((s) => !s.mergulho).map((s) => pos[s.id]);

	// 3. mergulhos: a câmera enquadra uma fração da tela do vídeo do slide `em`
	for (const s of slides) {
		if (!s.mergulho) continue;
		const {em, x = 0, y = 0, f = 0.56} = s.mergulho, tela = secao(em)?.querySelector('.tela');
		if (!tela) throw new Error(`cenas: mergulho "${s.id}" aponta para "${em}", que não tem section com .tela`);
		const b = caixa(tela);
		s.camera = {x: b.x + x * b.w, y: b.y + y * b.h, w: b.w * f, h: b.h * f};
	}

	// 4. tempos: início e duração da viagem de cada slide, como o palco calcula
	const plano = planejar(slides), T0 = {}, V = {};
	for (const s of plano.slides) { T0[s.id] = s.t0; V[s.id] = s.i === 0 || !s.passos.length ? 0 : Math.min(s.viagem ?? s.passos[0].dur, s.passos[0].dur); }
	const kCam = (t, id) => (V[id] > 0 ? entradaSaida(faixa(t - T0[id], 0, V[id])) : t > T0[id] ? 1 : 0);
	const proximo = (id) => slides[slides.findIndex((s) => s.id === id) + 1]?.id;

	// 5. zona noite e dourado sobre ela. No tema escuro (tinta mais clara que o fundo) a zona não inverte para a tinta
	// creme: fica num tom abaixo do fundo, puxado para o dourado (ou a --cor-noite do tema), com a tinta clara por
	// cima, e o holofote, o véu e a legenda vêm junto. O dourado como texto ali passa a vir puxado para a cor do texto
	// da noite quando não dá 3:1. Texto sobre o dourado (a .marca) usa a tinta ou o fundo, o que contrastar mais com
	// ele. A sombra dos objetos recortados é a mais escura das duas (no tema escuro, o fundo).
	const sonda = html(palcoEl, 'span'), dourado = corDe(sonda, '--cor-destaque'), tinta = corDe(sonda, '--cor-tinta'), fundo = corDe(sonda, '--cor-fundo');
	if (lum(tinta) > lum(fundo)) {
		const escuro = {'--noite': 'var(--cor-noite, color-mix(in srgb, var(--cor-destaque) 6%, var(--cor-fundo)))',
			'--sobre-noite': 'var(--cor-tinta)', '--suave-sobre-noite': 'var(--cor-tinta-suave)', '--linha-sobre-noite': 'var(--cor-linha)'};
		for (const k in escuro) palcoEl.style.setProperty(k, escuro[k]);
	}
	if (contraste(dourado, corDe(sonda, '--noite')) < 3) palcoEl.style.setProperty('--sinal-noite', 'color-mix(in srgb, var(--cor-destaque) 60%, var(--sobre-noite))');
	palcoEl.style.setProperty('--sobre-destaque', contraste(dourado, tinta) >= contraste(dourado, fundo) ? 'var(--cor-tinta)' : 'var(--cor-fundo)');
	palcoEl.style.setProperty('--cor-sombra', lum(tinta) <= lum(fundo) ? 'var(--cor-tinta)' : 'var(--cor-fundo)');
	sonda.remove();

	// 6. zonas noite (slides noite vizinhos dividem uma zona só) e a trilha
	const zonas = [];
	nos.forEach((n, i) => {
		if (!n.noite) return;
		const z = i > 0 && nos[i - 1].noite ? zonas[zonas.length - 1] : (zonas.push({x0: Infinity, y0: Infinity, x1: -Infinity, y1: -Infinity}), zonas[zonas.length - 1]);
		Object.assign(z, {x0: Math.min(z.x0, n.x - 400), y0: Math.min(z.y0, n.y - 900), x1: Math.max(z.x1, n.x + W + 400), y1: Math.max(z.y1, n.y + H + 900)});
	});
	let tr = document.getElementById('trilha');
	if (!tr) { tr = document.createElementNS(NS, 'svg'); tr.id = 'trilha'; }
	mundoEl.prepend(tr);
	for (const z of zonas.reverse()) {
		const el = document.createElement('div');
		el.className = 'zona-noite';
		Object.assign(el.style, {left: `${z.x0}px`, top: `${z.y0}px`, width: `${z.x1 - z.x0}px`, height: `${z.y1 - z.y0}px`});
		mundoEl.prepend(el);
	}
	const xs = nos.map((n) => n.x), ys = nos.map((n) => n.y);
	const caixaTr = {x: Math.min(...xs) - 600, y: Math.min(...ys) - 1000, w: Math.max(...xs) + W + 1200 - Math.min(...xs), h: Math.max(...ys) + H + 2000 - Math.min(...ys)};
	tr.setAttribute('viewBox', `${caixaTr.x} ${caixaTr.y} ${caixaTr.w} ${caixaTr.h}`);
	Object.assign(tr.style, {left: `${caixaTr.x}px`, top: `${caixaTr.y}px`, width: `${caixaTr.w}px`, height: `${caixaTr.h}px`});

	// base em cada slide, vão com degrau de 45° entre slides, pads por cima das linhas
	nos.forEach((n, i) => {
		if (i > 0) {
			const a = nos[i - 1], x1 = a.x + X1, y1 = a.y + BASE_Y, x2 = n.x + X0, y2 = n.y + BASE_Y, dy = Math.abs(y2 - y1), xm = (x1 + x2) / 2;
			n.vao = svg(tr, 'path', {d: `M${x1} ${y1}H${xm - dy / 2}L${xm + dy / 2} ${y2}H${x2}`});
		}
		n.base = svg(tr, 'path', {d: `M${n.x + X0} ${n.y + BASE_Y}H${n.x + X1}`});
	});
	nos.forEach((n, i) => {
		n.pads = [svg(tr, 'circle', {cx: n.x + X0, cy: n.y + BASE_Y, r: 11}), svg(tr, 'circle', {cx: n.x + X1, cy: n.y + BASE_Y, r: 11})];
		if (i === nos.length - 1) n.fim = svg(tr, 'circle', {cx: n.x + X1, cy: n.y + BASE_Y, r: 26, class: 'fim-anel'});   // a trilha termina
	});

	// circuito das aberturas: os traços dentro do slide e a continuação deles na trilha
	const circuitos = {};
	for (const n of nos) {
		if (n.tipo !== 'abertura') continue;
		const sec = secao(n.id);
		let el = sec.querySelector('.circuito');
		if (!el) { el = svg(sec, 'svg', {class: 'circuito', viewBox: '0 0 1920 1080'}); }
		circuitos[n.id] = SAIDA_Y.map((sy, j) => [svg(el, 'path', {d: `M1920 ${sy}H${ILHA_X[j]}`}), svg(el, 'circle', {cx: ILHA_X[j], cy: sy, r: 12})]);
		n.prox = proximo(n.id);
		if (!n.prox) continue;
		const E = n.x + W;
		n.continua = SAIDA_Y.map((sy, j) => {
			const xb = E + DOBRA[j], xj = xb + (BASE_Y - sy);
			return [svg(tr, 'path', {d: `M${E} ${n.y + sy}H${xb}L${xj} ${n.y + BASE_Y}`}), svg(tr, 'circle', {cx: xj, cy: n.y + BASE_Y, r: 9})];
		});
	}
	const circuito = (id, dt) => (circuitos[id] || []).forEach(([p, c], j) => {
		tracar(p, saida(faixa(dt - j * 0.08, 0, 0.5)));
		const q = molaAR(dt - j * 0.08 - 0.42, {resposta: 0.4, amortecimento: 0.75});
		vis(c, q > 0);
		c.style.transformOrigin = `${c.getAttribute('cx')}px ${c.getAttribute('cy')}px`;
		c.style.transform = `scale(${q})`;
	});

	const depois = [];
	const desenhar = (t, ctx) => {
		// trilha: o vão até um slide se traça com a viagem da câmera, e a base completa quando ela pousa
		nos.forEach((n, i) => {
			const lt = t - T0[n.id], v = V[n.id];
			const kv = v > 0 ? saida(faixa(lt, 0, v * 0.9)) : lt > 0 ? 1 : 0;
			const kb = i === 0 ? saida(faixa(lt, 0.2, 1.2)) : v > 0 ? saida(faixa(lt, v * 0.6, v + 0.7)) : saida(faixa(lt, 0, 0.6));
			if (n.vao) tracar(n.vao, kv);
			tracar(n.base, kb);
			// pads: visitado em dourado cheio, futuro só em contorno (o miolo tem a cor do fundo da zona)
			const [pe, pd] = n.pads, chegou = i === 0 ? kb > 0 : kv >= 1;
			pe.style.fill = chegou ? 'var(--cor-destaque)' : n.noite ? 'var(--noite)' : 'var(--cor-fundo)';
			pd.style.fill = 'var(--cor-destaque)';
			vis(pd, kb >= 1);
			if (n.fim) {
				const q = molaAR(lt - (i === 0 ? 1.2 : v + 0.7), {resposta: 0.45, amortecimento: 0.7});
				vis(n.fim, q > 0);
				n.fim.style.transformOrigin = `${n.fim.getAttribute('cx')}px ${n.fim.getAttribute('cy')}px`;
				n.fim.style.transform = `scale(${q})`;
			}
			if (n.continua) {
				const kc = saida(faixa(t - T0[n.prox], 0, V[n.prox] * 0.85));
				n.continua.forEach(([ps, junta]) => { tracar(ps, kc); junta.style.fill = 'var(--cor-destaque)'; vis(junta, kc >= 1); });
			}
		});
		for (const f of depois) f(t, ctx);
	};

	const m = {
		slides, T0, V, pos, kCam, secao, circuito, desenhar, proximo,
		depois: (f) => depois.push(f),   // o que atravessa slides e precisa desenhar depois de todas as cenas
		// Cenas de todas as sections com data-arquetipo; `ajustes[id]` é um objeto de opções do arquétipo ou uma cena
		// própria (t, c) => {...}, que substitui a da biblioteca.
		cenas: (ajustes = {}) => {
			const out = {};
			for (const s of slides) {
				const a = ajustes[s.id];
				if (typeof a === 'function') out[s.id] = a;
				else if (pos[s.id]?.tipo) out[s.id] = ARQUETIPOS[pos[s.id].tipo](m, s.id, a || {});
			}
			return out;
		},
	};
	for (const nome in ARQUETIPOS) m[nome] = (id, op = {}) => ARQUETIPOS[nome](m, id, op);
	return m;
}

// ---------- peças comuns às cenas ----------
// Exportadas para a cena própria ter o mesmo acabamento dos arquétipos: titulo(sec, x, c) faz rótulo e manchete
// (com o encaixe), e fim(sec, x, t0) faz pílula, selo e data-entra; x é conteudo(c). Exemplo em docs/cenas.md.

// Manchete numa linha de até 1680 px: o corpo desce até 56 px; abaixo disso ela quebra (.quebra) e o console avisa.
const encaixadas = new WeakSet();
export const encaixar = (el) => {
	if (encaixadas.has(el)) return;
	encaixadas.add(el);
	const tam = parseFloat(getComputedStyle(el).fontSize), w = el.offsetWidth;
	if (w <= 1680) return;
	if (tam * 1680 / w >= 56) { el.style.fontSize = `${Math.floor(tam * 1680 / w)}px`; return; }
	el.classList.add('quebra');
	console.warn(`cenas: manchete longa demais, quebra em duas linhas e aperta o conteúdo; encurte: "${el.textContent.trim()}"`);
};
// Rótulo e manchete entram juntos; num corte seco já estão na tela no clique.
export const titulo = (sec, x, c) => {
	const k = (d) => (c.slide.viagem === 0 && c.slide.i > 0 ? (x > 0 ? 1 : 0) : molaAR(x - d));
	const r = sec.querySelector(':scope > .rotulo'), m = sec.querySelector(':scope > .manchete');
	if (r) revelar(r, k(0));
	if (m) { encaixar(m); revelar(m, k(0.06)); }
};
// Pílula e selo entram por último; qualquer elemento com data-entra="s" surge naquele segundo do conteúdo. Quando os
// dois caem no mesmo canto (slide claro), o selo vai para a esquerda da pílula, na mesma faixa: subir o selo o poria
// sobre as legendas dos objetos, e descer, sobre a trilha.
const aoLado = new WeakSet();
export const fim = (sec, x, t0) => {
	const pil = sec.querySelector(':scope > .pilula'), selo = sec.querySelector(':scope > .selo-ia');
	if (pil && selo && !aoLado.has(sec)) {
		aoLado.add(sec);
		const cruza = (a, b, pos, tam) => a[pos] < b[pos] + b[tam] && b[pos] < a[pos] + a[tam];
		if (cruza(selo, pil, 'offsetTop', 'offsetHeight') && cruza(selo, pil, 'offsetLeft', 'offsetWidth'))
			Object.assign(selo.style, {left: 'auto', right: `${W - pil.offsetLeft + 28}px`});
	}
	for (const el of sec.querySelectorAll(':scope > .pilula, :scope > .selo-ia')) surgir(el, molaAR(x - t0), {dy: 0});
	for (const el of sec.querySelectorAll('[data-entra]')) surgir(el, molaAR(x - Number(el.dataset.entra)), {dy: 0});
};
// Caixa de um elemento relativa à section dele.
const local = (el, sec) => { const c = caixa(el), s = caixa(sec); return {x: c.x - s.x, y: c.y - s.y, w: c.w, h: c.h}; };
// Arquivo da árvore ou da lista de fontes: ícone à esquerda e o nome num span (para o marca-texto do pouso).
const iconizar = (no) => {
	if (no.querySelector('.no-nome')) return;
	const nome = html(no, 'span', 'no-nome');
	nome.append(...[...no.childNodes].filter((n) => n !== nome));
	if ('arquivo' in no.dataset) { const ic = document.createElement('span'); ic.className = 'ic'; ic.innerHTML = ICONE; no.prepend(ic); }
};
// Métricas da primeira linha de um título, em px a partir do topo da caixa: linha de base, topo da tinta e o recuo
// do primeiro glifo (para alinhar a tinta, não a caixa, na margem de 120 px).
let pincel = null;
const tinta = (el) => {
	const cs = getComputedStyle(el), tam = parseFloat(cs.fontSize);
	pincel = pincel || document.createElement('canvas').getContext('2d');
	pincel.font = `${cs.fontStyle} ${cs.fontWeight} ${cs.fontSize} ${cs.fontFamily}`;
	let s = el.textContent.trim();
	if (cs.textTransform === 'uppercase') s = s.toLocaleUpperCase('pt-BR');
	const mm = pincel.measureText(s), lh = cs.lineHeight === 'normal' ? tam * 1.2 : parseFloat(cs.lineHeight);
	const base = (lh - (mm.fontBoundingBoxAscent + mm.fontBoundingBoxDescent)) / 2 + mm.fontBoundingBoxAscent;
	return {base, topo: base - mm.actualBoundingBoxAscent, esq: mm.actualBoundingBoxLeft, larg: mm.width, tam};
};
// Texto display que cresce até a linha mais larga ocupar `largura` px, entre `min` e `max` px de corpo. `el` encolhe
// para caber (absoluto, sem largura) e as linhas não quebram; `alvos` recebem o corpo novo (padrão: o próprio el).
const crescer = (el, largura, min, max, alvos = [el]) => {
	const tam = parseFloat(getComputedStyle(alvos[0]).fontSize);
	const novo = Math.round(clamp(tam * largura / el.offsetWidth, min, max));
	for (const a of alvos) a.style.fontSize = `${novo}px`;
};

// ---------- arquétipos ----------
// Cada um recebe (m, id, opções) e devolve a cena (t, c). DURACAO dá o conteúdo em segundos (o palco soma a viagem).

const DURACAO = {
	abertura: () => 1.8,
	escolha: (sec) => (sec.querySelector('.leque[data-sorteio]') ? 2.95 : 1.75 + 1.25 * (sec.querySelectorAll('.leque').length - 1)),
	numero: (sec) => Math.max(2.4, agenda(marcas(sec)).fim + 0.35),
	comparacao: () => 2.8,
	ramos: () => 2.2,
	tempo: (sec) => 1.9 + 0.12 * Math.max(0, sec.querySelectorAll('.etapas > li').length - 4),
	objetos: () => 2.1,
	viagem: () => 2.0,
	fios: (sec) => 2.45 + 0.18 * (sec.querySelectorAll('.linha[data-fonte]').length - 1),
	demonstracao: () => 2.0,
	respiro: (sec) => 1.2 + 0.14 * (sec.querySelectorAll('.respiro > span').length - 1),
	fecho: () => 2.0,
};

// abertura: zona noite, rótulo, título display em linhas (a palavra-chave .sinal grande), subtítulo, foto heroica
// sob véu e os traços do circuito. As linhas se empilham pela tinta e a palavra-chave cresce até caber em 760 px.
const abertura = (m, id, {largura = 760} = {}) => {
	const sec = m.secao(id), foto = sec.querySelector('.heroi'), linhas = [...sec.querySelectorAll('.ab-linha')], sub = sec.querySelector('.ab-sub');
	let montado = false;
	const montar = () => {
		if (montado) return;
		montado = true;
		for (const el of linhas) if (el.classList.contains('sinal') && !el.style.fontSize) {
			const {larg, tam} = tinta(el);
			el.style.fontSize = `${Math.round(clamp(tam * largura / larg, tam, 420))}px`;
		}
		// tinta da linha seguinte começa 44 px abaixo da base da anterior; o subtítulo, 100 px abaixo da última
		let base = 0;
		const tops = linhas.map((el, n) => { const mt = tinta(el), top = n ? base + 44 - mt.topo : -mt.topo; base = top + mt.base; el.style.left = `${120 + mt.esq}px`; return top; });
		const topoSub = base + 100, fundo = topoSub + (sub ? sub.offsetHeight : 0);
		const d = Math.max(240, 905 - fundo);   // o bloco assenta em 905 (acima da trilha) sem subir além de 240
		linhas.forEach((el, n) => { el.style.top = `${tops[n] + d}px`; });
		if (sub) sub.style.top = `${topoSub + d}px`;
	};
	return (t, c) => {
		montar();
		const x = conteudo(c), x0 = -espera(c.slide.viagem), x1 = x0 + c.slide.passos[0].dur;
		if (foto) kenburns(foto, saida(faixa(x, x0 + (c.slide.viagem > 0 ? 0.2 : 0), x1 - 0.1)), {escala: 1.06, origem: '70% 55%'});
		const r = sec.querySelector(':scope > .rotulo');
		if (r) revelar(r, molaAR(x - 0.05));
		linhas.forEach((el, n) => revelar(el, molaAR(x - 0.15 - n * 0.12)));
		if (sub) revelar(sub, molaAR(x - 0.7));
		m.circuito(id, x - 0.45);
		fim(sec, x, 0.95);
	};
};

// escolha: a frase se escreve e cada .leque é uma rodada de candidatas (li com data-pct; a vencedora tem class
// "vence", ou é a primeira); a vencedora voa para a palavra data-alvo da frase. Com data-sorteio, uma rodada só: as
// barras ficam rasas, um anel sorteia e a palavra sai sublinhada, com a legenda .frase-leg.
const VOO = 0.68, LARGURA_LEQUE = 390 + 20 + 240 + 20 + 110;
const escolha = (m, id) => {
	const sec = m.secao(id), frase = sec.querySelector('.frase'), base = frase.querySelector('span');
	const cursor = frase.querySelector('.cursor') || html(frase, 'i', 'cursor');
	const fios = sec.querySelector('.fios-leque') || svg(sec, 'svg', {class: 'fios-leque', viewBox: '0 0 1920 1080'});
	sec.prepend(fios);
	const leques = [...sec.querySelectorAll('.leque')].map((ol) => {
		const itens = [...ol.children], escala = Number(ol.dataset.escala || 60);
		const vence = Math.max(0, itens.findIndex((li) => li.classList.contains('vence')));
		const L = {ol, alvo: document.getElementById(ol.dataset.alvo), vence, sorteio: 'sorteio' in ol.dataset, passo: itens.length > 3 ? 76 : 84};
		if (!L.alvo) throw new Error(`cenas: leque de "${id}" aponta para data-alvo="${ol.dataset.alvo}", que não existe`);
		L.linhas = itens.map((li, n) => {
			const v = Number(li.dataset.pct), txt = li.textContent.trim();
			li.className = 'cand' + (n === vence ? ' vence' : '');
			li.textContent = '';
			const w = html(html(li, 'span', 'pal'), 'span', '', txt);
			const barra = html(html(li, 'span', 'trilho'), 'span', 'barra');
			barra.style.width = `${(v / escala) * 100}%`;   // escala comum: 60% enche o trilho, então 8% fica raso
			return {row: li, w, barra, pct: html(li, 'span', 'pct', '0%'), v};
		});
		return L;
	});
	const sorteio = leques.find((L) => L.sorteio);
	const anel = sorteio && (sec.querySelector('.anel-sorteio') || html(sec, 'div', 'anel-sorteio'));
	const leg = sec.querySelector('.frase-leg');
	let cursores = null;
	const montar = () => {
		if (cursores) return;
		const ult = leques[leques.length - 1].alvo;
		cursores = [...leques.map((L) => L.alvo.offsetLeft - 14), ult.offsetLeft + ult.offsetWidth + 12];
		const fr = local(frase, sec);
		for (const L of leques) {
			const a = local(L.alvo, sec);
			L.topo = fr.y + fr.h + (L.sorteio ? 120 : 52);
			L.esq = clamp(a.x - 30, 120, 1800 - LARGURA_LEQUE);
			L.ol.style.left = `${L.esq}px`;
			L.linhas.forEach(({row}, n) => { row.style.top = `${L.topo + n * L.passo}px`; });
			const yb = fr.y + fr.h + 4, yh = yb + 22, xb = L.esq - 26;
			L.fios = L.linhas.map((_, n) => svg(fios, 'path', {d: `M${a.x - 14} ${yb}V${yh}H${xb}V${L.topo + n * L.passo + 38}H${L.esq - 8}`}));
		}
		if (leg) { const a = local(sorteio ? sorteio.alvo : ult, sec); leg.style.left = `${a.x + a.w - leg.offsetWidth}px`; }
	};
	// Uma rodada, em segundos desde o começo dela: as candidatas surgem com as barras (desde `xe`), a vencedora voa para
	// a frase e, se a rodada não fica na tela, as outras caem.
	const rodada = (L, x, {fica = false, xe = x} = {}) => {
		L.linhas.forEach(({row, barra, pct, v}, n) => {
			const cai = fica ? 0 : sair(faixa(x, n === L.vence ? 1.0 : VOO + 0.04, n === L.vence ? 1.25 : VOO + 0.36));
			if (cai > 0) surgir(row, sem(cai), {dy: 26}); else surgir(row, molaAR(xe - n * 0.07), {dx: -16, dy: 0});
			const k = molaAR(xe - 0.12 - n * 0.07);
			barra.style.transform = `scaleX(${k})`;
			contar(pct, k, 0, v, {sufixo: '%'});
		});
		// o fio some antes de a vencedora decolar, para ela voar sobre o claro
		L.fios.forEach((f, n) => { tracar(f, saida(faixa(xe - n * 0.07, 0, 0.35))); f.style.opacity = fica ? 1 : sem(sair(faixa(x, VOO - 0.18, VOO + 0.06))); });
		const k = molaAR(x - VOO, {resposta: 0.55, amortecimento: 0.85});
		vis(L.alvo, x > VOO);
		voar(L.alvo, L.linhas[L.vence].w, null, k, {arco: 70});
		return k;
	};
	return (t, c) => {
		montar();
		const x = conteudo(c);
		titulo(sec, x, c);
		revelar(base, molaAR(x - 0.12));
		if (sorteio) {
			const L = sorteio, k = rodada(L, x - 1.27, {fica: true, xe: x - 0.3});
			// sorteio: o anel passeia pelas candidatas e para na vencedora; depois ela voa
			const T1 = 1.65, onde = (s) => (L.linhas.length - 1) * ruido(s * 6, 7);
			const p = x < T1 ? onde(x) : lerp(onde(T1), L.vence, molaAR(x - T1, {resposta: 0.45, amortecimento: 0.8}));
			Object.assign(anel.style, {left: `${L.esq - 18}px`, width: `${LARGURA_LEQUE + 36}px`, top: `${L.topo + p * L.passo}px`});
			anel.style.opacity = faixa(x, 0.7, 0.85) * sem(faixa(x, 2.1, 2.35));
			vis(anel, x > 0.7 && x < 2.35);
			cursor.style.left = `${cursores[0]}px`;
			vis(cursor, x > 0.3 && k < 0.85);
			anotar(L.alvo, saida(faixa(x, 2.3, 2.65)), {forma: 'sublinhado', semente: 5, folga: 4});
			if (leg) revelar(leg, molaAR(x - 2.45));
			fim(sec, x, 2.45);
			return;
		}
		const ks = leques.map((L, r) => rodada(L, x - 0.35 - 1.25 * r, {fica: r === leques.length - 1}));
		let r = ks.length - 1;
		while (r >= 0 && !(ks[r] > 0.85)) r--;
		cursor.style.left = `${cursores[r + 1]}px`;
		vis(cursor, x > 0.3);
		fim(sec, x, 0.35 + 1.25 * (leques.length - 1) + 0.8);
	};
};

// numero: grade de itens corrigidos a caneta (data-marcas="1101..." na .grade: 1 certo, 0 errado) e o placar
// .numero com .conta, que conta os certos, e a barra .numero-barra.
const marcas = (sec) => [...(sec.querySelector('.grade')?.dataset.marcas || '')].map((ch) => ch === '1');
const agenda = (ms) => {
	const tracos = [];
	let t = 0.45;
	ms.forEach((ok, n) => (ok ? [0] : [0, 1]).forEach((m, j, ds) => {
		const dur = ok ? 0.14 : 0.08;
		tracos.push({n, ok, m, t0: t, t1: t + dur});
		t += dur + (j === ds.length - 1 ? 0.04 : 0.02);
	}));
	return {tracos, fim: tracos.length ? tracos[tracos.length - 1].t1 : 0.45};
};
const numero = (m, id) => {
	const sec = m.secao(id), grade = sec.querySelector('.grade'), ms = marcas(sec), cols = Number(grade?.dataset.colunas || 5);
	const tela = svg(sec, 'svg', {class: 'tinta-caneta', viewBox: '0 0 1920 1080'});
	const celulas = ms.map((ok, n) => {
		const el = html(grade, 'div', 'celula'), cx = 120 + (n % cols) * 168, cy = 410 + Math.floor(n / cols) * 168;
		Object.assign(el.style, {left: `${cx}px`, top: `${cy}px`});
		html(el, 'span', '', String(n + 1));
		return {el, cx, cy};
	});
	const {tracos} = agenda(ms);
	for (const tr of tracos) {
		const {cx, cy} = celulas[tr.n];
		tr.p = svg(tela, 'path', {d: tr.ok ? `M${cx + 38} ${cy + 74}L${cx + 60} ${cy + 98}L${cx + 104} ${cy + 44}`
			: tr.m === 0 ? `M${cx + 50} ${cy + 52}L${cx + 100} ${cy + 102}` : `M${cx + 100} ${cy + 52}L${cx + 50} ${cy + 102}`});   // o X fica longe do número
	}
	const caneta = svg(tela, 'circle', {r: 11});
	const certos = tracos.filter((tr) => tr.ok), total = ms.length || 1;
	const ALVOS = [{t: -1, v: 0}, ...certos.map((tr, n) => ({t: tr.t1, v: n + 1}))];
	const conta = sec.querySelector('.numero .conta'), placar = sec.querySelector('.numero');
	const trilho = sec.querySelector('.numero-trilho'), barra = sec.querySelector('.numero-barra'), leg = sec.querySelector('.numero-leg');
	let atrasos = null;
	return (t, c) => {
		if (!atrasos) { atrasos = escalonar(celulas.map(({cx, cy}) => ({x: cx, y: cy, w: 136, h: 136})), {de: {x: 120, y: 975}, quantidade: 0.3}); for (const tr of tracos) tr.L = tr.p.getTotalLength(); }
		const x = conteudo(c);
		titulo(sec, x, c);
		celulas.forEach(({el}, n) => surgir(el, molaAR(x - 0.05 - atrasos[n]), {dy: 0, escala: 0.08}));
		// a ponta da caneta segue o traço e salta de um ao seguinte
		let ponta = null;
		tracos.forEach((tr, n) => {
			const k = saida(faixa(x, tr.t0, tr.t1));
			tracar(tr.p, k);
			if (x < tr.t0 - 0.06) return;
			if (x <= tr.t1) ponta = tr.p.getPointAtLength(tr.L * k);
			else if (tracos[n + 1] && x < tracos[n + 1].t0 - 0.06) {
				const a = tr.p.getPointAtLength(tr.L), b = tracos[n + 1].p.getPointAtLength(0), u = faixa(x, tr.t1, tracos[n + 1].t0);
				ponta = {x: lerp(a.x, b.x, u), y: lerp(a.y, b.y, u)};
			}
		});
		vis(caneta, !!ponta);
		if (ponta) { caneta.setAttribute('cx', ponta.x.toFixed(1)); caneta.setAttribute('cy', ponta.y.toFixed(1)); }
		const txt = String(certos.filter((tr) => x >= tr.t1).length);
		if (conta && conta.textContent !== txt) conta.textContent = txt;
		if (placar) revelar(placar, molaAR(x - 0.3));
		if (trilho) surgir(trilho, molaAR(x - 0.4), {dy: 0});
		if (barra) barra.style.transform = `scaleX(${alvos(x, ALVOS, {rigidez: 240, amortecimento: 24}) / total})`;
		if (leg) revelar(leg, molaAR(x - 0.5));
		fim(sec, x, 1.9);
	};
};

// comparacao: duas .janela sem nome (data-linhas com a largura de cada linha em %), separadas pelo .fio-v; a
// .janela.escolhida tem a .letra circulada no fim.
const comparacao = (m, id) => {
	const sec = m.secao(id), janelas = [...sec.querySelectorAll('.janela')];
	const fio = sec.querySelector('.fio-v') || html(sec, 'div', 'fio-v');
	const ritmo = janelas.map((jn, w) => {
		const rnd = aleatorio(11 + w);
		let t = 0.5 + w * 0.06;
		return (jn.dataset.linhas || '').trim().split(/\s+/).filter(Boolean).map(Number).map((pct, i) => {
			const el = html(jn, 'i');
			Object.assign(el.style, {top: `${240 + i * 34}px`, width: `${pct * 7.1}px`});
			const dur = (0.16 + 0.14 * rnd()) * (w ? 1.25 : 1), r = {el, t0: t, t1: t + dur};
			t += dur + 0.04;
			return r;
		});
	});
	const tA = Math.max(1.6, ...ritmo.flat().map((r) => r.t1)) + 0.05;
	const escolhida = sec.querySelector('.janela.escolhida .letra');
	return (t, c) => {
		const x = conteudo(c);
		titulo(sec, x, c);
		janelas.forEach((jn, n) => surgir(jn, molaAR(x - 0.12 - n * 0.1), {dy: 30}));
		fio.style.transform = `scaleY(${saida(faixa(x, 0.1, 0.6))})`;
		for (const ls of ritmo) for (const {el, t0, t1} of ls) el.style.transform = `scaleX(${saida(faixa(x, t0, t1))})`;
		if (escolhida) anotar(escolhida, saida(faixa(x, tA, tA + 0.45)), {semente: 4, folga: 12});
		fim(sec, x, tA + 0.25);
	};
};

// ramos: a trilha se divide em ramos (cada .ramo com data-y, as .estacao em ordem e uma .caixa-txt de destino).
// Os ramos saem do pad esquerdo da trilha, sobem e seguem até as caixas.
const ramos = (m, id) => {
	const sec = m.secao(id), mapa = svg(sec, 'svg', {class: 'mapa', viewBox: '0 0 1920 1080'});
	sec.prepend(mapa);
	const rs = [...sec.querySelectorAll('.ramo')].map((r, n) => {
		const y = Number(r.dataset.y || 450 + 270 * n), comp = BASE_Y - (y + 70) + 70 * Math.SQRT2 + 1070;
		const traco = svg(mapa, 'path', {class: 'ramo-traco', d: `M120 ${BASE_Y}V${y + 70}L190 ${y}H1260`});
		const quadro = svg(mapa, 'rect', {x: 1260, y: y - 85, width: 540, height: 170, rx: 18});
		const txt = r.querySelector('.caixa-txt');
		if (txt) txt.style.top = `${y - 53}px`;
		const estacoes = [...r.querySelectorAll('.estacao')].map((e, k) => {
			const ex = 330 + 260 * k;
			Object.assign(e.style, {left: `${ex - 140}px`, top: `${y - 62}px`});
			const ponto = svg(mapa, 'circle', {cx: ex, cy: y, r: 9});
			// quando o traço passa pela estação (o ramo se desenha com saida em 0,1..1,0 s)
			const fr = (BASE_Y - (y + 70) + 70 * Math.SQRT2 + (ex - 190)) / comp;
			let q = 0;
			while (q < 1 && saida(q) < fr) q += 0.005;
			return {e, ponto, t: 0.1 + 0.9 * q};
		});
		return {traco, quadro, txt, estacoes};
	});
	const leg = sec.querySelector('.ramos-leg');
	return (t, c) => {
		const x = conteudo(c);
		titulo(sec, x, c);
		const kr = saida(faixa(x, 0.1, 1.0)), kc = saida(faixa(x, 0.9, 1.35));
		for (const r of rs) {
			tracar(r.traco, kr);
			tracar(r.quadro, kc);
			if (r.txt) revelar(r.txt, molaAR(x - 1.1));
			for (const {e, ponto, t: te} of r.estacoes) {
				const k = molaAR(x - te);
				surgir(e, k, {dy: 14});
				ponto.style.transformOrigin = `${ponto.getAttribute('cx')}px ${ponto.getAttribute('cy')}px`;
				ponto.style.transform = `scale(${clamp(k, 0, 1.2)})`;
				vis(ponto, k > 0);
			}
		}
		if (leg) revelar(leg, molaAR(x - 1.45));
		fim(sec, x, 1.6);
	};
};

// objetos: o .pedido se digita na .entrada ao lado dos objetos recortados (.objetos > figure > img.objeto +
// figcaption.doc-leg), sob duas .etiqueta.
const objetos = (m, id) => {
	const sec = m.secao(id), ets = [...sec.querySelectorAll(':scope > .etiqueta')], entrada = sec.querySelector('.entrada'), pedido = sec.querySelector('.pedido');
	const figs = [...sec.querySelectorAll('.objetos figure')].map((f) => [f.querySelector('.objeto'), f.querySelector('.doc-leg')]);
	return (t, c) => {
		const x = conteudo(c);
		titulo(sec, x, c);
		ets.forEach((el, n) => revelar(el, molaAR(x - 0.1 - n * 0.3)));
		if (entrada) surgir(entrada, molaAR(x - 0.1), {dy: 24});
		if (pedido) digitar(pedido, faixa(x, 0.3, 1.55), {cursor: x > 0.2 && x < 1.75, semente: 3});
		figs.forEach(([ob, leg], n) => {
			if (ob) surgir(ob, molaAR(x - 0.5 - n * 0.12), {dy: -28});
			if (leg) revelar(leg, molaAR(x - 0.75 - n * 0.12));
		});
		fim(sec, x, 1.4);
	};
};

// viagem: a .arvore (cada .no com data-nivel; data-arquivo ganha ícone) nasce pela raiz, e cada .no com
// data-de="id" recebe o objeto daquele id, que voa do slide dele: atravessa grande, encolhe perto da árvore e entra
// no ícone; a folha surge no pouso e o nome acende em dourado depois.
const viagem = (m, id) => {
	const sec = m.secao(id), arvore = sec.querySelector('.arvore'), foto = sec.querySelector('.viagem-foto');
	const nos = [...arvore.querySelectorAll('.no')].map((el, n) => {
		const nivel = Number(el.dataset.nivel || 0);
		iconizar(el);
		Object.assign(el.style, {left: `${52 * nivel}px`, top: `${72 * n}px`});
		return {el, nivel, x: 52 * nivel, y: 72 * n, nome: el.querySelector('.no-nome'), ic: el.querySelector('.ic'), de: document.getElementById(el.dataset.de || '')};
	});
	const linhas = svg(arvore, 'svg', {class: 'arvore-ramos', viewBox: '0 0 1920 1080'});
	arvore.prepend(linhas);
	const ramosArv = [];
	nos.forEach((no, n) => {
		if (!no.nivel) return;
		let p = n - 1;
		while (p > 0 && nos[p].nivel !== no.nivel - 1) p--;
		ramosArv.push({p: svg(linhas, 'path', {d: `M${nos[p].x + 18} ${nos[p].y + 52}V${no.y + 28}H${no.x - 10}`}), n});
	});
	const voos = nos.filter((no) => no.de && no.ic);
	for (const no of voos) no.de.classList.add('viaja');
	let atrasos = null;
	const montar = () => { atrasos ??= escalonar(nos.map((n) => ({x: n.x, y: n.y})), {de: 'inicio', quantidade: 0.45}); };
	// o voo: dono do objeto só enquanto voa (antes, a cena do slide de origem; depois, escondido)
	m.depois((t) => {
		montar();
		voos.forEach((no, j) => {
			// o voo acompanha a câmera: sai logo e chega 0,3 s depois dela, para estar no quadro durante a viagem
			const atraso = j * 0.06, k = entradaSaida(faixa(t - m.T0[id], atraso + 0.05, m.V[id] + 0.3 + atraso));
			const el = no.de;
			if (k > 0) {
				const A = caixa(el), I = caixa(no.ic), pw = 130, ph = pw * A.h / A.w;
				const P = {x: I.x - 110 - pw, y: I.y + I.h / 2 - ph / 2, w: pw, h: ph};   // pouso grande, à esquerda do ícone
				// o centro vai ao pouso e depois ao ícone; o tamanho fica inteiro até a metade do voo
				const k1 = entradaSaida(faixa(k, 0, 0.7)), k2 = entradaSaida(faixa(k, 0.7, 1)), ks = entradaSaida(faixa(k, 0.45, 0.7));
				const cx = k < 0.7 ? lerp(A.x + A.w / 2, P.x + P.w / 2, k1) : lerp(P.x + P.w / 2, I.x + I.w / 2, k2);
				const cy = (k < 0.7 ? lerp(A.y + A.h / 2, P.y + P.h / 2, k1) - 80 * Math.sin(Math.PI * k1) : lerp(P.y + P.h / 2, I.y + I.h / 2, k2));
				const w = k < 0.7 ? lerp(A.w, P.w, ks) : lerp(P.w, I.w, k2), h = k < 0.7 ? lerp(A.h, P.h, ks) : lerp(P.h, I.h, k2);
				voar(el, null, {x: cx - w / 2, y: cy - h / 2, w, h}, 1);
				el.style.opacity = sem(faixa(k, 0.96, 1));
				vis(el, k < 1);
			} else {
				// antes do voo o objeto é do slide de origem: desfaz o que o voo deixou (quadro = função do tempo)
				vis(el, true);
				el.style.transformOrigin = '';
			}
			surgir(no.el, faixa(k, 0.9, 1), {dx: -18, dy: 0});
			const pouso = m.T0[id] + m.V[id] + 0.3 + atraso;
			no.nome.style.boxShadow = `inset 0 -${(0.34 * saida(faixa(t - pouso, 0, 0.35))).toFixed(3)}em 0 var(--cor-destaque)`;
		});
	});
	return (t, c) => {
		montar();
		const x = conteudo(c);
		titulo(sec, x, c);
		if (foto) surgir(foto, molaAR(x + 0.35), {dy: 30});   // entra ainda na viagem: a foto é a primeira a aparecer
		nos.forEach((no, n) => { if (!voos.includes(no)) surgir(no.el, molaAR(x - 0.15 - atrasos[n]), {dx: -18, dy: 0}); });
		for (const {p, n} of ramosArv) tracar(p, saida(faixa(x - 0.1 - atrasos[n], 0, 0.35)));
		fim(sec, x, 1.25);
	};
};

// fios: cada .linha da .minuta com data-fonte="id" ganha um fio desde a fonte (em qualquer lugar do mundo; na
// biblioteca, a lista .fontes do próprio slide). Só o fio da linha que tem .marca é dourado, e a marca acende quando
// ele chega; a linha sem data-fonte é sublinhada e a .sem-fonte aparece.
const fios = (m, id) => {
	const sec = m.secao(id), minuta = sec.querySelector('.minuta'), cab = minuta.querySelector('.cab');
	const linhas = [...minuta.querySelectorAll('.linha')], fontes = [...sec.querySelectorAll('.fontes .no')], semFonte = minuta.querySelector('.sem-fonte');
	fontes.forEach(iconizar);
	const camada = svg(sec, 'svg', {class: 'fios', viewBox: '0 0 1920 1080'});
	sec.prepend(camada);
	const ligadas = linhas.filter((l) => l.dataset.fonte), soltas = linhas.filter((l) => !l.dataset.fonte);
	let fs = null;
	const montar = () => {
		if (fs) return;
		const s = caixa(sec), N = ligadas.length;
		fs = ligadas.map((l, n) => {
			const fonte = document.getElementById(l.dataset.fonte);
			if (!fonte) throw new Error(`cenas: linha de "${id}" aponta para data-fonte="${l.dataset.fonte}", que não existe`);
			// o fio chega à esquerda da linha, na altura da marca (se houver): nunca atravessa o texto
			const marca = l.querySelector('.marca'), ini = caixa(l.firstElementChild || l), mc = marca && caixa(marca);
			const f = caixa(fonte.querySelector('.no-nome') || fonte);
			const a = {x: f.x + f.w - s.x, y: f.y + f.h / 2 - s.y}, b = {x: ini.x - s.x, y: (mc ? mc.y + mc.h / 2 : ini.y + 30) - s.y};
			if (Math.abs(b.y - a.y) < 16) b.y = a.y;
			const x1 = a.x + 24, x2 = b.x - 26, dy = b.y - a.y, xm = (x1 + x2) / 2 + (n - (N - 1) / 2) * 40;
			const r = {marca, p: svg(camada, 'path', {d: `M${x1} ${a.y}H${xm - Math.abs(dy) / 2}L${xm + Math.abs(dy) / 2} ${b.y}H${x2}`}),
				c1: svg(camada, 'circle', {cx: x1, cy: a.y, r: 8}), c2: svg(camada, 'circle', {cx: x2, cy: b.y, r: 8})};
			if (!marca) for (const el of [r.p, r.c1, r.c2]) el.classList.add('neutro');   // dourado só no fio que chega à marca
			return r;
		});
	};
	const tFios = 1.3 + 0.18 * (ligadas.length - 1);
	return (t, c) => {
		montar();
		const x = conteudo(c);
		titulo(sec, x, c);
		fontes.forEach((el, n) => surgir(el, molaAR(x - 0.1 - n * 0.08), {dx: -18, dy: 0}));
		if (cab) surgir(cab, molaAR(x - 0.15), {dy: 20});
		linhas.forEach((el, n) => surgir(el, molaAR(x - 0.25 - n * 0.1), {dy: 20}));
		fs.forEach(({p, c1, c2, marca}, n) => {
			const t1 = 1.3 + n * 0.18, k = saida(faixa(x, t1 - 0.5, t1));
			tracar(p, k);
			vis(c1, k > 0);
			vis(c2, k >= 1);
			if (!marca) return;
			// a marca só acende quando o fio chega a ela (o CSS de .marca é o valor final)
			const cor = `color-mix(in srgb, var(--cor-destaque) ${(100 * saida(faixa(x, t1 - 0.05, t1 + 0.25))).toFixed(1)}%, transparent)`;
			marca.style.background = cor;
			marca.style.boxShadow = `0 0 0 5px ${cor}`;
		});
		soltas.forEach((l) => anotar(l.firstElementChild || l, saida(faixa(x, tFios + 0.3, tFios + 0.7)), {forma: 'sublinhado', semente: 9, folga: 4}));
		if (semFonte) revelar(semFonte, molaAR(x - tFios - 0.55));
		fim(sec, x, tFios + 0.6);
	};
};

// demonstracao: o vídeo da .tela toca numa moldura de navegador neutra. Cada slide com `video: [de, dur]` toca dur
// segundos do clipe a partir de `de` segundos do seu início; os slides com `mergulho: {em: este, ..., furos}`
// levam a câmera a uma região do vídeo, com holofote (marinho quase cheio fora dos furos, frações do quadro) e a
// .legenda[data-mergulho="id"] (data-x, data-y em frações). Cada holofote novo chega cheio antes de o anterior sair.
const demonstracao = (m, id) => {
	const sec = m.secao(id), tela = sec.querySelector('.tela'), vid = tela.querySelector('video'), moldura = sec.querySelector('.moldura');
	const nota = sec.querySelector('.nota-lateral'), tw = tela.offsetWidth || 1100, th = tela.offsetHeight || 618.75;
	const trechos = m.slides.filter((s) => s.video && (s.id === id || s.mergulho?.em === id));
	const furo = ([fx, fy, fw, fh], g = 7) => {
		const x = fx * tw - g, y = fy * th - g, w = fw * tw + 2 * g, h = fh * th + 2 * g, r = 8;
		return `M${x + r} ${y}H${x + w - r}Q${x + w} ${y} ${x + w} ${y + r}V${y + h - r}Q${x + w} ${y + h} ${x + w - r} ${y + h}H${x + r}Q${x} ${y + h} ${x} ${y + h - r}V${y + r}Q${x} ${y} ${x + r} ${y}Z`;
	};
	const mergs = m.slides.filter((s) => s.mergulho?.em === id).map((s) => {
		const h = svg(tela, 'svg', {class: 'holofote', viewBox: `0 0 ${tw} ${th}`});
		svg(h, 'path', {d: `M-10 -10H${tw + 10}V${th + 10}H-10Z` + (s.mergulho.furos || []).map((r) => furo(r)).join('')});
		const leg = tela.querySelector(`.legenda[data-mergulho="${s.id}"]`);
		if (leg) { tela.appendChild(leg); Object.assign(leg.style, {left: `${Number(leg.dataset.x || 0) * tw}px`, top: `${Number(leg.dataset.y || 0) * th}px`}); }
		return {id: s.id, h, leg};
	});
	const saiDe = mergs.length ? m.proximo(mergs[mergs.length - 1].id) : null;
	for (const leg of tela.querySelectorAll('.legenda')) if (!mergs.some((g) => g.leg === leg)) leg.style.display = 'none';   // mergulho apagado
	return (t, c) => {
		const x = conteudo(c);
		titulo(sec, x, c);
		if (moldura) surgir(moldura, molaAR(x + 0.45), {dy: 40});   // a moldura chega antes da câmera: a viagem não cruza o vazio
		if (nota) revelar(nota, molaAR(x - 0.5));
		// o vídeo toca no clique e para sozinho em cada parada
		if (vid) video(vid, trechos.reduce((a, s) => a + clamp(t - m.T0[s.id] - s.video[0], 0, s.video[1]), 0));
		// o último holofote só sai quando a câmera já deixou o vídeo: antes disso a tela inteira viraria um cinza-ardósia
		const saida0 = saiDe ? faixa(m.kCam(t, saiDe), 0.3, 0.8) : 0;
		mergs.forEach(({id: mid, h, leg}, j) => {
			const l = t - m.T0[mid], prox = mergs[j + 1];
			const entra = j === 0 ? saida(faixa(l, 0.35, 0.95)) : saida(faixa(l, 0, 0.4));   // o escuro acompanha o zoom
			const sai = prox ? sem(saida(faixa(t - m.T0[prox.id], 0.4, 0.8))) : sem(saida0);
			const k = entra * sai;
			h.style.opacity = k;
			vis(h, k > 0);
			if (!leg) return;
			// a legenda sai antes de o próximo recorte acender embaixo dela
			const kl = molaAR(l - 1.6) * (prox ? sem(saida(faixa(t - m.T0[prox.id], 0, 0.25))) : sem(saida0));
			surgir(leg, kl, {dy: 6});
			vis(leg, kl > 0);
		});
		fim(sec, x, 1.2);
	};
};

// tempo: agenda, cronograma, linha do tempo ou etapas. Cada li de .etapas é um marco (<b> com a data ou a hora, em
// cima da linha, e o texto embaixo); a linha se traça da esquerda, cada marco surge quando ela passa, e o marco
// .agora ganha o ponto dourado, que cresce depois de todos. Os marcos se distribuem por igual entre 120 e 1800 px.
const LINHA_Y = 600;
const tempo = (m, id) => {
	const sec = m.secao(id), itens = [...sec.querySelectorAll('.etapas > li')], n = itens.length || 1, passo = 1680 / n;
	const camada = svg(sec, 'svg', {class: 'tempo-linha', viewBox: '0 0 1920 1080'});
	sec.prepend(camada);
	const linha = svg(camada, 'path', {d: `M120 ${LINHA_Y}H1800`});
	const marcos = itens.map((li, k) => {
		const cx = 120 + passo * (k + 0.5);
		Object.assign(li.style, {left: `${cx - passo / 2 + 16}px`, width: `${passo - 32}px`});
		const agora = li.classList.contains('agora');
		const ponto = svg(camada, 'circle', {cx, cy: LINHA_Y, r: agora ? 20 : 13, class: agora ? 'agora' : ''});
		ponto.style.transformOrigin = `${cx}px ${LINHA_Y}px`;
		return {li, ponto, agora, t: 0.1 + 0.9 * (cx - 120) / 1680};   // quando a linha passa por ele
	});
	const leg = sec.querySelector('.tempo-leg'), tAgora = 1.25;
	return (t, c) => {
		const x = conteudo(c);
		titulo(sec, x, c);
		tracar(linha, faixa(x, 0.1, 1.0));
		for (const {li, ponto, agora, t: tm} of marcos) {
			const k = molaAR(x - tm);
			surgir(li, k, {dy: 14});
			// o anel do marco .agora já é dourado; o miolo enche de dourado com a mola, depois de todos
			const q = agora ? molaAR(x - tAgora, {resposta: 0.45, amortecimento: 0.7}) : 0;
			ponto.style.transform = `scale(${clamp(k, 0, 1.2) * (1 + 0.25 * q)})`;
			ponto.style.fill = agora && q > 0 ? `color-mix(in srgb, var(--cor-destaque) ${(100 * clamp(q, 0, 1)).toFixed(1)}%, var(--ponto-tempo))` : '';
			vis(ponto, k > 0);
		}
		if (leg) revelar(leg, molaAR(x - 1.4));
		fim(sec, x, 1.55);
	};
};

// respiro: uma frase curta (até 12 palavras), grande, em linhas (.respiro > span), centrada na altura.
const respiro = (m, id) => {
	const sec = m.secao(id), frase = sec.querySelector('.respiro'), linhas = [...frase.children];
	let montado = false;
	return (t, c) => {
		if (!montado) {
			montado = true;
			crescer(frase, 1680, 110, 180, linhas);
			frase.style.top = `${Math.round(560 - frase.offsetHeight / 2)}px`;
		}
		const x = conteudo(c);
		titulo(sec, x, c);
		linhas.forEach((el, n) => revelar(el, molaAR(x - 0.1 - n * 0.14)));
		fim(sec, x, 0.6);
	};
};

// fecho: a mensagem (.fecho-msg em linhas) e o que a plateia faz agora (.fecho-passos); a trilha termina no anel.
const fecho = (m, id) => {
	const sec = m.secao(id), caixaMsg = sec.querySelector('.fecho-msg'), lista = sec.querySelector('.fecho-passos');
	const msg = [...sec.querySelectorAll('.fecho-msg > span')], passos = [...sec.querySelectorAll('.fecho-passos li')];
	let montado = false;
	return (t, c) => {
		if (!montado && caixaMsg) {
			montado = true;
			crescer(caixaMsg, 1680, 110, 150);
			if (lista) lista.style.top = `${caixaMsg.offsetTop + caixaMsg.offsetHeight + 56}px`;
		}
		const x = conteudo(c);
		titulo(sec, x, c);
		msg.forEach((el, n) => revelar(el, molaAR(x - 0.1 - n * 0.12)));
		passos.forEach((el, n) => surgir(el, molaAR(x - 0.6 - n * 0.15), {dx: -16, dy: 0}));
		fim(sec, x, 1.2);
	};
};

export const ARQUETIPOS = {abertura, escolha, numero, comparacao, ramos, tempo, objetos, viagem, fios, demonstracao, respiro, fecho};
