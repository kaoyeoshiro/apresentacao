// Motor de palco: apresentação ao vivo em que cada quadro é função pura do tempo t, com paradas. O clique toca o
// trecho até a parada seguinte; o mesmo arquivo vira vídeo, PDF e stills (./ap video, ./ap pdf, ./ap paradas).
// Contrato: docs/palco.md. Decisão: docs/decisao.md.
//
// Na composição continua valendo o contrato do motor HTML (nada de relógio, timer, aleatório sem semente ou CSS
// transition). Este arquivo é o tocador e pode usar o relógio: ele só decide QUAL t desenhar, nunca o que há em t.
import {clamp, lerp, faixa, saida, entradaSaida, mola} from './tempo.js';
import {enquadrar, misturarPose, transformar} from './camera.js';

// Mensagens entre o palco, a tela do apresentador e as prévias: só da mesma origem e só da janela esperada.
// Por file:// a origem é opaca, e o destino fica '*' (o que viaja é só o número da parada).
const ALVO = location.protocol === 'file:' ? '*' : location.origin;
const deCasa = (m) => m.origin === location.origin || location.protocol === 'file:';

const W = 1920, H = 1080;

// ---------- linha do tempo ----------

// Slides com `passos` (durações em s). Cada passo termina numa parada; a primeira parada é t = 0, antes de tudo.
export function planejar(slides) {
	const erros = [];
	let t = 0;
	const paradas = [{n: 0, t: 0, slide: 0, passo: -1}];
	const S = slides.map((s, i) => {
		if (!s.id) erros.push(`slide ${i + 1} sem id`);
		if (!Array.isArray(s.passos) || !s.passos.length) erros.push(`slide "${s.id}" sem passos (precisa de pelo menos a entrada)`);
		const t0 = t;
		const passos = (s.passos || []).map((d, n) => {
			if (!(d > 0)) erros.push(`slide "${s.id}", passo ${n + 1}: duração ${d} inválida`);
			const p = {n, t0: t, t1: t + d, dur: d};
			t += d;
			paradas.push({n: paradas.length, t, slide: i, passo: n});
			return p;
		});
		return {...s, i, t0, t1: t, passos, titulo: s.titulo || s.id};
	});
	const ids = S.map((s) => s.id);
	ids.forEach((id, i) => { if (ids.indexOf(id) !== i) erros.push(`id de slide repetido: "${id}"`); });
	return {slides: S, paradas, duracao: t, erros};
}

// Linha do vídeo: segura cada parada `segura` s (do slide da parada; padrão 2,5; a primeira, `seguraInicio`) e toca os
// passos entre elas. Devolve trechos [{T0, T1, t0, t1, parada}] com t0 == t1 nos repousos.
export function linhaDeVideo(plano, {seguraInicio = 1.5, seguraPadrao = 2.5, seguraFim = 3} = {}) {
	const trechos = [];
	let T = 0;
	plano.paradas.forEach((p, k) => {
		const s = plano.slides[p.slide];
		const ultimo = k === plano.paradas.length - 1;
		const seg = k === 0 ? seguraInicio : ultimo ? Math.max(seguraFim, s.segura ?? 0) : (s.segura ?? seguraPadrao);
		trechos.push({T0: T, T1: T + seg, t0: p.t, t1: p.t, parada: k});
		T += seg;
		const prox = plano.paradas[k + 1];
		if (prox) {
			trechos.push({T0: T, T1: T + (prox.t - p.t), t0: p.t, t1: prox.t, parada: null});
			T += prox.t - p.t;
		}
	});
	return {trechos, duracao: T};
}

export const noVideo = (linha, T) => {
	const tr = linha.trechos.find((x) => T < x.T1) || linha.trechos[linha.trechos.length - 1];
	if (tr.parada !== null) return {t: tr.t0, ocioso: T - tr.T0};
	return {t: tr.t0 + (T - tr.T0), ocioso: 0};
};

// ---------- ajudantes de desenho (puros: o mesmo k dá sempre o mesmo estilo) ----------

// Mola de entrada (0 antes de dt = 0, passa ~3% e assenta). Perto do fim vira 1 exato: escala de 0,999 numa parada
// faz o Chrome rasterizar a camada de jeito diferente conforme o caminho até ali, e o quadro deixa de ser idêntico.
export const entrar = (dt, cfg = {rigidez: 240, amortecimento: 24}) => {
	const k = mola(dt, cfg);
	return dt > 0.3 && Math.abs(k - 1) < 2e-3 ? 1 : k;
};

// Sobe de trás de uma linha de corte, sem transparência (máscara por clip-path no próprio elemento).
export function revelar(el, k, {de = 'baixo', dist = 1.1} = {}) {
	k = clamp(k, 0, 1.2);
	const fora = (1 - Math.min(k, 1)) * dist * 100;
	const s = el.style;
	s.visibility = k <= 0 ? 'hidden' : '';
	if (k >= 1) { s.clipPath = 'none'; s.transform = de === 'baixo' ? `translateY(${(1 - k) * dist * 100}%)` : ''; return; }
	if (de === 'baixo') { s.transform = `translateY(${fora}%)`; s.clipPath = `inset(0 0 ${fora}% 0)`; }
	else if (de === 'esquerda') { s.transform = `translateX(${-fora}%)`; s.clipPath = `inset(0 0 0 ${fora}%)`; }
	else if (de === 'cima') { s.transform = `translateY(${-fora}%)`; s.clipPath = `inset(${fora}% 0 0 0)`; }
}

// Entrada simples: opacidade e deslocamento curtos (use pouco; prefira revelar).
export function surgir(el, k, {dy = 28, dx = 0, escala = 0} = {}) {
	const e = clamp(k, 0, 1.05);
	el.style.opacity = clamp(k * 1.6, 0, 1);
	el.style.transform = `translate(${(1 - e) * dx}px, ${(1 - e) * dy}px) scale(${1 - (1 - clamp(k)) * escala})`;
}

// Número que conta de `de` até `ate` (formato pt-BR).
export function contar(el, k, de, ate, {casas = 0, prefixo = '', sufixo = ''} = {}) {
	const v = lerp(de, ate, clamp(k));
	el.textContent = prefixo + v.toLocaleString('pt-BR', {minimumFractionDigits: casas, maximumFractionDigits: casas}) + sufixo;
}

// Traço SVG que se desenha (o path recebe pathLength=1 na primeira chamada).
export function tracar(path, k) {
	if (path.getAttribute('pathLength') !== '1') path.setAttribute('pathLength', '1');
	k = clamp(k);
	path.style.visibility = k <= 0 ? 'hidden' : '';
	// No fim, sem tracejado: com ponta redonda, o encontro do traço com o vão deixa um ponto que varia entre renders.
	path.style.strokeDasharray = k >= 1 ? 'none' : '1 1';
	path.style.strokeDashoffset = String(1 - k);
}

// Palavra por palavra: embrulha as palavras em <span> uma vez e revela por máscara em sequência.
export function palavras(el, k, {atraso = 0.5} = {}) {
	if (!el.dataset.palavras) {
		const ws = el.textContent.trim().split(/\s+/);
		el.replaceChildren(...ws.map((w) => {
			const sp = document.createElement('span');
			sp.style.cssText = 'display:inline-block;white-space:pre';
			sp.textContent = w + ' ';
			return sp;
		}));
		el.dataset.palavras = String(ws.length);
	}
	const spans = el.children, n = spans.length;
	const passo = n > 1 ? (1 - atraso) / (n - 1) : 0;
	for (let i = 0; i < n; i++) revelar(spans[i], faixa(k, i * passo, i * passo + atraso));
}

// Vídeo dentro do slide, em `seg` segundos do clipe. No render posiciona o quadro exato e espera; ao vivo deixa o
// navegador tocar e só corrige se escorregar mais de 0,25 s. Devolve uma Promise que o palco aguarda sozinho.
const ultimoSeg = new WeakMap();
export function video(el, seg) {
	seg = Math.max(0, Math.min(seg, (el.duration || Infinity) - 0.04));
	if (estado.modo !== 'vivo') {
		// Vídeo que não abriu nunca dispara `seeked`: falha alto em vez de pendurar o render.
		if (el.error || el.readyState === 0) throw new Error(`vídeo não abriu: ${el.getAttribute('src')}`);
		if (Math.abs(el.currentTime - seg) < 1e-3) return;
		el.pause();
		const pronto = new Promise((r, falha) => {
			const prazo = setTimeout(() => falha(new Error(`vídeo não posicionou em ${seg.toFixed(2)} s: ${el.getAttribute('src')}`)), 15000);
			el.addEventListener('seeked', () => { clearTimeout(prazo); r(); }, {once: true});
		});
		el.currentTime = seg;
		estado.pendentes.push(pronto);
		return;
	}
	const antes = ultimoSeg.get(el);
	ultimoSeg.set(el, seg);
	const andando = antes !== undefined && seg > antes;
	if (andando && el.paused) el.play().catch(() => {});
	if (!andando && !el.paused) el.pause();
	if (Math.abs(el.currentTime - seg) > 0.25) el.currentTime = seg;
}

export {clamp, lerp, faixa, saida, entradaSaida, mola, transformar, enquadrar};

// ---------- o palco ----------

const estado = {modo: 'vivo', pendentes: []};

const CSS = `
html, body { margin: 0; height: 100%; background: #000; overflow: hidden; }
#palco { position: absolute; left: 0; top: 0; width: ${W}px; height: ${H}px; overflow: hidden; transform-origin: 0 0; }
:where(#palco section[data-slide]) { position: absolute; left: 0; top: 0; width: ${W}px; height: ${H}px; box-sizing: border-box; }
:where(#mundo) { position: absolute; left: 0; top: 0; width: 0; height: 0; transform-origin: 0 0; }
.palco-ui { position: fixed; z-index: 10; font: 500 18px/1.4 system-ui, sans-serif; color: #eee; }
#palco-preto { inset: 0; background: #000; display: none; }
#palco-indice, #palco-ajuda { inset: 0; background: rgba(8,10,14,.94); display: none; overflow: auto; padding: 48px 64px; box-sizing: border-box; }
#palco-indice ol { columns: 2; column-gap: 64px; font-size: 22px; } #palco-indice li { padding: 6px 0; cursor: pointer; }
#palco-indice li.atual { color: #E8B04B; } #palco-ajuda kbd { display: inline-block; min-width: 28px; padding: 2px 8px; margin-right: 10px; border: 1px solid #555; border-radius: 6px; text-align: center; }
#palco-aviso { left: 16px; bottom: 12px; font-size: 14px; opacity: .45; pointer-events: none; }
body.apresentador { background: #0b0d11; color: #eee; font: 500 18px/1.4 system-ui, sans-serif; overflow: hidden; }
body.apresentador #palco { display: none; }
#ap { position: fixed; inset: 0; display: grid; grid-template-columns: 1.55fr 1fr; grid-template-rows: auto 1fr; gap: 20px; padding: 20px; box-sizing: border-box; }
#ap .rot { font-size: 14px; letter-spacing: .08em; text-transform: uppercase; opacity: .55; margin-bottom: 8px; }
#ap iframe { width: 100%; aspect-ratio: 16 / 9; border: 0; background: #000; border-radius: 6px; display: block; }
#ap-topo { grid-column: 1 / 3; display: flex; gap: 36px; align-items: baseline; font-variant-numeric: tabular-nums; }
#ap-topo b { font-size: 40px; font-weight: 600; } #ap-notas { font-size: 26px; line-height: 1.45; white-space: pre-wrap; overflow: auto; margin-top: 18px; }
`;

const $ = (sel) => document.querySelector(sel);

export function palco({titulo = document.title, slides, cenas = {}, desenhar = () => {}, mundo, segura = {}} = {}) {
	const plano = planejar(slides);
	if (plano.erros.length) throw new Error('palco inválido: ' + plano.erros.join('; '));
	const {paradas, duracao} = plano;
	const S = plano.slides;

	const estilo = document.createElement('style');
	estilo.textContent = CSS;
	document.head.prepend(estilo);
	const palcoEl = $('#palco');
	if (!palcoEl) throw new Error('falta <div id="palco"> no deck');
	const mundoEl = $('#mundo');
	const secoes = Object.fromEntries(S.map((s) => [s.id, document.querySelector(`[data-slide="${s.id}"]`)]));

	// Câmera: `camera: true` enquadra a própria seção; `camera: {x, y, w, h}` enquadra a caixa do mundo. Sem câmera,
	// o slide herda a pose do anterior. A câmera viaja no começo do primeiro passo, durante `viagem` segundos (padrão:
	// o passo inteiro), e `recuo` (0 a 1) afasta a câmera no meio da viagem, para a plateia ver de onde vem e para onde vai.
	const caixaDe = (s) => {
		if (!s.camera) return null;
		if (s.camera === true) {
			const el = secoes[s.id];
			return {x: el.offsetLeft, y: el.offsetTop, w: el.offsetWidth, h: el.offsetHeight};
		}
		return s.camera;
	};
	const usaCamera = !!mundoEl && S.some((s) => s.camera);
	mundo = mundo ?? usaCamera;
	const poses = [];
	S.forEach((s, i) => {
		const c = caixaDe(s);
		poses.push(c ? enquadrar(c, {largura: W, altura: H}, 0) : poses[i - 1] || {cx: W / 2, cy: H / 2, z: 1, rot: 0});
	});
	const camera = (t, s) => {
		if (!s.passos.length || s.i === 0) return poses[s.i];
		const p0 = s.passos[0];
		const k = entradaSaida(faixa(t, p0.t0, p0.t0 + Math.min(s.viagem ?? p0.dur, p0.dur)));
		const pose = misturarPose(poses[s.i - 1], poses[s.i], k);
		return s.recuo ? {...pose, z: pose.z * (1 - s.recuo * Math.sin(Math.PI * k))} : pose;
	};

	const slideEm = (t) => S.find((s) => t <= s.t1 + 1e-9) || S[S.length - 1];

	// Visibilidade e transição padrão (fora do modo mundo): o slide atual aparece; o anterior fica durante a entrada
	// do atual, para a transição ter os dois. `transicao`: 'corte' (padrão), 'fade', 'empurrar'.
	const visibilidade = (t, s) => {
		if (mundo) return;
		const p0 = s.passos[0];
		const entrando = s.i > 0 && t < p0.t1 && t > p0.t0;
		const k = entradaSaida(faixa(t, p0.t0, p0.t1));
		const tipo = s.transicao || 'corte';
		for (const o of S) {
			const el = secoes[o.id];
			if (!el) continue;
			const atual = o === s, anterior = entrando && o.i === s.i - 1;
			el.style.visibility = atual || (anterior && tipo !== 'corte') ? 'visible' : 'hidden';
			el.style.opacity = '';
			el.style.transform = '';
			if (!entrando || tipo === 'corte') continue;
			// Fade em mergulho: o anterior some até a metade e o atual nasce a partir de um terço, sem os dois inteiros juntos.
			if (tipo === 'fade') el.style.opacity = atual ? faixa(k, 0.35, 1) : 1 - faixa(k, 0, 0.55);
			else if (tipo === 'empurrar') el.style.transform = `translateX(${(atual ? 1 - k : -k) * W}px)`;
		}
	};

	// Contexto de um slide em t: progresso linear de cada passo (p), segundos desde o início de cada passo (desde, para
	// molas), entrada suavizada e `ocioso` (só no slide atual, parado numa parada).
	const ctxDe = (s, t, ocioso, atual) => ({
		t, ocioso: atual ? ocioso : 0, modo: estado.modo, slide: s, i: s.i, atual, local: t - s.t0,
		passo: s.passos.findIndex((p) => t <= p.t1 + 1e-9),
		p: (n) => (s.passos[n] ? faixa(t, s.passos[n].t0, s.passos[n].t1) : 0),
		desde: (n) => t - (s.passos[n] ? s.passos[n].t0 : s.t1),
		entrada: entradaSaida(faixa(t, s.passos[0].t0, s.passos[0].t1)),
	});
	const ctxEm = (t, ocioso) => {
		const s = slideEm(t);
		const k = (id, n = 0) => {
			const o = S.find((x) => x.id === id);
			if (!o) throw new Error(`slide "${id}" não existe`);
			return ctxDe(o, t, 0, false).p(n);
		};
		return {...ctxDe(s, t, ocioso, true), k, de: (id) => ctxDe(S.find((x) => x.id === id), t, 0, false)};
	};

	let ver = async (t, ocioso = 0) => {
		const ctx = ctxEm(t, ocioso);
		if (usaCamera) {
			const c = camera(t, ctx.slide);
			mundoEl.style.transform = `translate(${W / 2}px, ${H / 2}px) rotate(${c.rot || 0}deg) scale(${c.z}) translate(${-c.cx}px, ${-c.cy}px)`;
		}
		visibilidade(t, ctx.slide);
		estado.pendentes = [];
		// Cada cena desenha o próprio slide a partir de t, então pular para qualquer instante dá o mesmo quadro. Desenha o
		// slide atual e o anterior durante a entrada (no modo mundo, todos).
		const s = ctx.slide, p0 = s.passos[0];
		const vis = mundo ? S : s.i > 0 && t > p0.t0 && t < p0.t1 ? [S[s.i - 1], s] : [s];
		for (const o of vis) if (cenas[o.id]) await cenas[o.id](t, o === s ? ctx : ctxDe(o, t, 0, false));
		await desenhar(t, ctx);
		if (estado.pendentes.length) await Promise.all(estado.pendentes);
	};

	// Medida do DOM para o oráculo (./ap sondar): blocos de texto visíveis, em coordenadas do quadro.
	const medir = () => {
		const blocos = [];
		const visivel = (el) => {
			let alfa = 1;
			for (let n = el; n && n !== document.documentElement; n = n.parentElement) {
				const cs = getComputedStyle(n);
				if (cs.display === 'none' || cs.visibility === 'hidden') return 0;
				alfa *= parseFloat(cs.opacity);
			}
			return alfa;
		};
		for (const el of palcoEl.querySelectorAll('*')) {
			const nos = [...el.childNodes].filter((n) => n.nodeType === 3 && n.textContent.trim());
			if (!nos.length || el.closest('svg') && el.tagName.toLowerCase() !== 'text') continue;
			const alfa = visivel(el);
			const cs = getComputedStyle(el);
			const cor = rgba(cs.color);
			if (alfa * (cor[3] ?? 1) < 0.1) continue;
			const r = el.getBoundingClientRect();
			const rg = document.createRange();
			rg.selectNodeContents(el);
			const rt = rg.getBoundingClientRect();
			if (r.width < 1 || r.height < 1) continue;
			if (rt.right < 0 || rt.left > W || rt.bottom < 0 || rt.top > H) continue;
			const base = el.offsetWidth || el.getBBox?.().width || r.width;
			const escala = r.width / (base || 1);
			const texto = nos.map((n) => n.textContent).join(' ').replace(/\s+/g, ' ').trim();
			const pai = el.parentElement, csPai = pai && getComputedStyle(pai);
			const clipaPai = csPai && csPai.overflow !== 'visible';
			// Fonte com área de glifo maior que a entrelinha (título justo) passa da própria caixa em cima e embaixo
			// sem transbordar de fato: a folga vertical desconta essa diferença, linha a linha.
			const lh = parseFloat(cs.lineHeight) * escala, linha = rg.getClientRects()[0];
			const fv = 2 + (lh && linha ? Math.max(0, (linha.height - lh) / 2) : 0);
			blocos.push({
				texto, palavras: texto.split(' ').length, fonte: parseFloat(cs.fontSize) * escala,
				x: rt.left, y: rt.top, w: rt.width, h: rt.height,
				cor: cor.slice(0, 3), alfa: alfa * (cor[3] ?? 1),
				transborda: rt.right > r.right + 2 || rt.bottom > r.bottom + fv || rt.left < r.left - 2 || rt.top < r.top - fv ||
					(clipaPai && (rt.right > pai.getBoundingClientRect().right + 2 || rt.bottom > pai.getBoundingClientRect().bottom + fv)),
				id: el.id || '', caminho: caminho(el), ...origem(el),
			});
		}
		return blocos;
	};
	// Canto da seção do slide na tela: o oráculo desconta o movimento da transição entre slides, que é do tocador.
	const origem = (el) => {
		const sec = el.closest('[data-slide]');
		const r = sec ? sec.getBoundingClientRect() : {left: 0, top: 0};
		return {sx: r.left, sy: r.top};
	};
	// Cor computada em 0..255: o Chrome devolve color-mix() como color(srgb r g b / a), com canais de 0 a 1.
	const rgba = (c) => {
		const n = c.match(/[\d.]+/g).map(Number);
		return c.startsWith('color(') ? [n[0] * 255, n[1] * 255, n[2] * 255, n[3] ?? 1] : [n[0], n[1], n[2], n[3] ?? 1];
	};
	const caminho = (el) => {
		const partes = [];
		for (let n = el; n && n !== palcoEl; n = n.parentElement) {
			partes.unshift(n.id ? `#${n.id}` : n.dataset?.slide ? `[${n.dataset.slide}]` : `${n.tagName.toLowerCase()}:${[...n.parentElement.children].indexOf(n) + 1}`);
		}
		return partes.join(' > ');
	};

	const resumo = {
		titulo, largura: W, altura: H, duracao,
		slides: S.map((s) => ({id: s.id, titulo: s.titulo, notas: s.notas || '', t0: s.t0, t1: s.t1, passos: s.passos.map((p) => p.dur)})),
		paradas: paradas.map((p) => ({...p, id: S[p.slide].id})),
	};

	const q = new URLSearchParams(location.search);
	if (navigator.webdriver && !['vivo', 'apresentador', 'previa'].some((x) => q.has(x))) {
		estado.modo = 'render';
		const linha = linhaDeVideo(plano, segura);
		// Antes do primeiro quadro: vídeos com quadro decodificado e imagens prontas (senão o still sai preto).
		let pronta = null;
		const midia = () => pronta || (pronta = Promise.all([
			...[...document.querySelectorAll('video')].map((v) => v.readyState >= 2 || new Promise((r) => {
				v.addEventListener('loadeddata', r, {once: true}); v.addEventListener('error', r, {once: true}); v.load();
			})),
			...[...document.images].map((im) => im.decode().catch(() => {})),
		]));
		const ver0 = ver;
		ver = async (t, ocioso) => { await midia(); await ver0(t, ocioso); };
		window.__meta = {largura: W, altura: H, fps: 30, duracao: linha.duracao};
		window.__seek = async (T) => {
			const {t, ocioso} = noVideo(linha, T);
			await ver(t, ocioso);
			await new Promise((r) => requestAnimationFrame(() => r()));
		};
		window.__events = () => ({T: linha.duracao, eventos: [], voz: []});
		window.__palco = {
			...resumo, linha: linha.trechos, medir,
			ir: async (n, ocioso = 0) => { await ver(paradas[n].t, ocioso); await new Promise((r) => requestAnimationFrame(() => r())); },
			ver: async (t, ocioso = 0) => { await ver(t, ocioso); await new Promise((r) => requestAnimationFrame(() => r())); },
		};
		return window.__palco;
	}
	if (q.has('apresentador')) return apresentador(resumo);
	return tocador({ver, resumo, palcoEl, previa: q.has('previa') ? Number(q.get('previa')) : null});
}

// ---------- ao vivo ----------

function tocador({ver, resumo, palcoEl, previa}) {
	const {paradas, slides} = resumo;
	const ajustar = () => {
		const e = Math.min(innerWidth / W, innerHeight / H);
		palcoEl.style.transform = `translate(${(innerWidth - W * e) / 2}px, ${(innerHeight - H * e) / 2}px) scale(${e})`;
	};
	addEventListener('resize', ajustar);
	ajustar();

	// Prévia (dentro da tela do apresentador): mostra uma parada, parada, e obedece ao pai.
	if (previa !== null) {
		ver(paradas[Math.min(previa, paradas.length - 1)].t);
		addEventListener('message', (m) => {
			if (deCasa(m) && m.source === parent && m.data && m.data.palcoPrevia !== undefined) ver(paradas[Math.min(m.data.palcoPrevia, paradas.length - 1)].t);
		});
		return;
	}

	const ui = (id, html = '') => {
		const d = document.createElement('div');
		d.id = id; d.className = 'palco-ui'; d.innerHTML = html;
		document.body.appendChild(d);
		return d;
	};
	const preto = ui('palco-preto');
	const indice = ui('palco-indice', '<h2></h2><ol></ol>');
	indice.querySelector('h2').textContent = resumo.titulo;
	indice.querySelector('ol').replaceChildren(...slides.map((s) => {
		const li = document.createElement('li');
		li.dataset.i = s.id;
		li.textContent = s.titulo;
		return li;
	}));
	const ajuda = ui('palco-ajuda', `<h2>Atalhos</h2><p><kbd>→</kbd><kbd>espaço</kbd><kbd>PgDn</kbd>avança &nbsp; <kbd>←</kbd><kbd>PgUp</kbd>volta</p>
<p><kbd>B</kbd>tela preta &nbsp; <kbd>F</kbd>tela cheia &nbsp; <kbd>G</kbd>índice &nbsp; <kbd>P</kbd>tela do apresentador</p>
<p><kbd>número</kbd> + <kbd>Enter</kbd> vai ao slide &nbsp; <kbd>Home</kbd><kbd>End</kbd> início e fim &nbsp; <kbd>?</kbd> esta ajuda</p>`);
	const aviso = ui('palco-aviso', 'P apresentador · ? atalhos');

	let atual = Math.min(Number((location.hash.match(/parada=(\d+)/) || [])[1] || 0), paradas.length - 1);
	let tocando = null, chegada = performance.now(), janelaAp = null, digitos = '';
	const inicioPalestra = performance.now();

	const avisarAp = () => janelaAp && !janelaAp.closed && janelaAp.postMessage({palco: {atual, inicio: inicioPalestra}}, ALVO);
	const chegou = (n) => {
		atual = n; tocando = null; chegada = performance.now();
		history.replaceState(null, '', `#parada=${n}`);
		avisarAp();
	};
	const proxima = () => {
		if (tocando) chegou(tocando.para);                 // clique no meio da animação: completa e segue
		if (atual >= paradas.length - 1) return;
		tocando = {de: paradas[atual].t, para: atual + 1, inicio: performance.now()};
		avisarAp();
	};
	const anterior = () => { chegou(tocando ? Math.max(0, tocando.para - 1) : Math.max(0, atual - 1)); };
	const irSlide = (i) => {
		const k = paradas.findIndex((p) => p.slide === i);
		if (k >= 0) chegou(Math.max(0, k - 1)), proxima();
	};

	const tecla = (e) => {
		const k = e.key;
		if (/^\d$/.test(k)) { digitos += k; return; }
		if (k === 'Enter' && digitos) { irSlide(Number(digitos) - 1); digitos = ''; return; }
		digitos = '';
		if (['ArrowRight', 'ArrowDown', ' ', 'PageDown', 'Enter', 'n'].includes(k)) proxima();
		else if (['ArrowLeft', 'ArrowUp', 'PageUp', 'Backspace'].includes(k)) anterior();
		else if (k === 'Home') chegou(0);
		else if (k === 'End') chegou(paradas.length - 1);
		else if (k === 'b' || k === 'B' || k === '.') preto.style.display = preto.style.display === 'block' ? 'none' : 'block';
		else if (k === 'f' || k === 'F') document.fullscreenElement ? document.exitFullscreen() : document.documentElement.requestFullscreen();
		else if (k === 'g' || k === 'G') indice.style.display = indice.style.display === 'block' ? 'none' : 'block';
		else if (k === '?') ajuda.style.display = ajuda.style.display === 'block' ? 'none' : 'block';
		else if (k === 'p' || k === 'P') {
			janelaAp = open(location.pathname + '?apresentador', 'palco-apresentador', 'width=1280,height=800');
			setTimeout(avisarAp, 600);
		} else if (k === 'Escape') { indice.style.display = ajuda.style.display = 'none'; }
		else return;
		e.preventDefault();
	};
	addEventListener('keydown', tecla);
	palcoEl.addEventListener('click', proxima);
	indice.addEventListener('click', (e) => {
		const li = e.target.closest('li');
		if (!li) return;
		indice.style.display = 'none';
		irSlide(slides.findIndex((s) => s.id === li.dataset.i));
	});
	addEventListener('message', (m) => {
		const c = m.data && m.data.palcoComando;
		if (!c || !deCasa(m)) return;
		// Só a tela do apresentador que este palco abriu (ou que se apresenta como aberta por ele) manda comando.
		if (m.source !== janelaAp && !(c === 'ola' && m.source && m.source.opener === window)) return;
		if (c === 'proxima') proxima();
		else if (c === 'anterior') anterior();
		else if (c === 'ola') { janelaAp = m.source; avisarAp(); }
		else if (c === 'tecla') tecla({key: m.data.tecla, preventDefault() {}});
	});

	let parado = null;
	addEventListener('mousemove', () => {
		document.body.style.cursor = '';
		clearTimeout(parado);
		parado = setTimeout(() => { document.body.style.cursor = 'none'; }, 2000);
	});
	setTimeout(() => { aviso.style.display = 'none'; }, 4000);

	let desenhando = false;
	const quadro = async () => {
		requestAnimationFrame(quadro);
		if (desenhando) return;
		desenhando = true;
		const agora = performance.now();
		let t, ocioso = 0;
		if (tocando) {
			const alvo = paradas[tocando.para].t;
			t = Math.min(alvo, tocando.de + (agora - tocando.inicio) / 1000);
			if (t >= alvo) chegou(tocando.para);
		} else {
			t = paradas[atual].t;
			ocioso = (agora - chegada) / 1000;
		}
		try { await ver(t, ocioso); } finally { desenhando = false; }
	};
	quadro();
}

// Tela do apresentador: parada atual e próxima (o próprio deck em modo prévia), notas, cronômetro e relógio.
function apresentador(resumo) {
	document.body.classList.add('apresentador');
	document.title = 'Apresentador · ' + resumo.titulo;
	const base = location.pathname + '?previa=';
	const ap = document.createElement('div');
	ap.id = 'ap';
	ap.innerHTML = `
<div id="ap-topo"><b id="ap-crono">00:00</b><span id="ap-relogio"></span><span id="ap-pos"></span><span style="opacity:.5">← → avançam daqui também</span></div>
<div><div class="rot">Agora</div><iframe id="ap-agora" src="${base}0"></iframe><div id="ap-notas"></div></div>
<div><div class="rot">Próxima parada</div><iframe id="ap-prox" src="${base}1"></iframe><div class="rot" style="margin-top:18px" id="ap-slide"></div></div>`;
	document.body.appendChild(ap);
	const agora = $('#ap-agora'), prox = $('#ap-prox');
	let atual = 0, inicio = null;
	const pintar = () => {
		const p = resumo.paradas[atual], s = resumo.slides[p.slide];
		agora.contentWindow?.postMessage({palcoPrevia: atual}, ALVO);
		prox.contentWindow?.postMessage({palcoPrevia: Math.min(atual + 1, resumo.paradas.length - 1)}, ALVO);
		$('#ap-notas').textContent = s.notas;
		$('#ap-pos').textContent = `slide ${p.slide + 1} de ${resumo.slides.length} · parada ${atual} de ${resumo.paradas.length - 1}`;
		$('#ap-slide').textContent = s.titulo;
	};
	const dois = (n) => String(Math.floor(n)).padStart(2, '0');
	setInterval(() => {
		const d = new Date();
		$('#ap-relogio').textContent = `${dois(d.getHours())}:${dois(d.getMinutes())}`;
		if (inicio !== null) { const s = (performance.now() - inicio) / 1000; $('#ap-crono').textContent = `${dois(s / 60)}:${dois(s % 60)}`; }
	}, 250);
	addEventListener('message', (m) => {
		if (!deCasa(m) || m.source !== opener || !m.data || !m.data.palco) return;
		atual = m.data.palco.atual;
		if (inicio === null) inicio = performance.now();
		pintar();
	});
	addEventListener('keydown', (e) => {
		if (!opener || e.key === 'p' || e.key === 'P') return;
		opener.postMessage({palcoComando: 'tecla', tecla: e.key}, ALVO);
		e.preventDefault();
	});
	agora.addEventListener('load', pintar);
	prox.addEventListener('load', pintar);
	if (opener) opener.postMessage({palcoComando: 'ola'}, ALVO);
}
