// Motor de palco: apresentação ao vivo em que cada quadro é função pura do tempo t, com paradas. O clique toca o
// trecho até a parada seguinte; o mesmo arquivo vira vídeo, PDF e stills (./ap video, ./ap pdf, ./ap paradas).
// Contrato: docs/palco.md. Decisão: docs/decisao.md.
//
// Na composição continua valendo o contrato do motor HTML (nada de relógio, timer, aleatório sem semente ou CSS
// transition). Este arquivo é o tocador e pode usar o relógio: ele só decide QUAL t desenhar, nunca o que há em t.
import {clamp, lerp, faixa, saida, entradaSaida, sair, chegar, mola, molaAR, escalonar, aleatorio, ruido} from './tempo.js';
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
		if (s.viagem !== undefined && !(typeof s.viagem === 'number' && s.viagem >= 0)) erros.push(`slide "${s.id}": viagem ${s.viagem} inválida`);
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

// ---------- blocos da aula (linha do dia e guia do apresentador) ----------

// Blocos [{id, rotulo, minutos}] e o `bloco` de cada slide: o slide sem `bloco` herda o do anterior. Devolve o índice
// do bloco de cada slide (-1 antes do primeiro), e de cada bloco o trecho do deck (t0, t1; null se nenhum slide do deck
// é dele, como o bloco da aula seguinte) e as paradas que encerram passos dele.
export function planejarDia(plano, blocos = []) {
	const erros = [], ids = blocos.map((b) => b.id);
	blocos.forEach((b, j) => {
		if (!b.id || !b.rotulo) erros.push(`bloco ${j + 1} sem id ou rótulo`);
		if (b.minutos !== undefined && !(b.minutos > 0)) erros.push(`bloco "${b.id}": minutos ${b.minutos} inválidos`);
	});
	let atual = -1;
	const porSlide = plano.slides.map((s) => {
		if (s.bloco !== undefined) {
			atual = ids.indexOf(s.bloco);
			if (atual < 0) erros.push(`slide "${s.id}": bloco "${s.bloco}" não existe`);
		}
		return atual;
	});
	const B = blocos.map((b, j) => {
		const ss = plano.slides.filter((s) => porSlide[s.i] === j);
		return {id: b.id, rotulo: b.rotulo, minutos: b.minutos ?? null, t0: ss.length ? ss[0].t0 : null, t1: ss.length ? ss[ss.length - 1].t1 : null,
			paradas: plano.paradas.filter((p) => p.passo >= 0 && porSlide[p.slide] === j).map((p) => p.n)};
	});
	return {blocos: B, porSlide, erros};
}

// Quanto do bloco já passou na parada `atual`: chegar à primeira parada dele é o começo (0), e a última, o começo do
// último trecho.
export const fracaoDoBloco = (bloco, atual) => (bloco.paradas.length ? Math.max(0, bloco.paradas.filter((n) => n <= atual).length - 1) / bloco.paradas.length : 0);

// Segundos no bloco contra o previsto para a fração dele que já passou: saldo positivo é atraso. Meio minuto de folga.
export function ritmoDoBloco(decorrido, minutos, fracao) {
	if (!minutos) return {saldo: 0, estado: ''};
	const saldo = decorrido - minutos * 60 * clamp(fracao);
	return {saldo, estado: saldo > 30 ? 'atrasado' : saldo < -30 ? 'adiantado' : 'no tempo'};
}

// mm:ss de segundos (negativo leva o sinal).
export const relogio = (seg) => {
	const a = Math.floor(Math.abs(seg)), dois = (n) => String(n).padStart(2, '0');
	return `${seg < 0 ? '-' : ''}${dois(Math.floor(a / 60))}:${dois(a % 60)}`;
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
	const texto = prefixo + v.toLocaleString('pt-BR', {minimumFractionDigits: casas, maximumFractionDigits: casas}) + sufixo;
	if (el.textContent !== texto) el.textContent = texto;   // escrever o mesmo texto força layout a cada quadro
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
// navegador tocar e só corrige se escorregar mais de 0,25 s; parado (o tempo não avança), corrige acima de meio quadro
// (`fps` do clipe), para a parada mostrar o mesmo quadro do PDF. No render, o palco aguarda a busca sozinho.
const ultimoSeg = new WeakMap();
export function video(el, seg, {fps = 30} = {}) {
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
	if (Math.abs(el.currentTime - seg) > (andando ? 0.25 : 0.5 / fps)) el.currentTime = seg;
}

// Caixa de um elemento HTML no mundo ({x, y, w, h} em px de #mundo, ou de #palco fora do modo mundo), pela soma de
// offsetLeft e offsetTop: ignora a escala do tocador, o zoom da câmera e os transforms das animações, que o
// getBoundingClientRect inclui. Meça depois das fontes (o palco as carrega antes do primeiro quadro).
export function caixa(el) {
	if (!(el instanceof HTMLElement)) throw new Error('caixa() mede só elementos HTML');
	const ref = el.closest('#mundo') || el.closest('#palco');
	let x = 0, y = 0;
	for (let n = el; n && n !== ref; n = n.offsetParent) {
		x += n.offsetLeft;
		y += n.offsetTop;
		if (n.offsetParent && n.offsetParent !== ref) { x += n.offsetParent.clientLeft; y += n.offsetParent.clientTop; }
	}
	return {x, y, w: el.offsetWidth, h: el.offsetHeight};
}
// Medida única por elemento (só depois que ele entrou no layout).
const medidas = new WeakMap();
const medida = (el) => {
	let c = medidas.get(el);
	if (!c) { c = caixa(el); if (el.offsetParent) medidas.set(el, c); }
	return c;
};

// Voo FLIP (First, Last, Invert, Play): o elemento fica no lugar dele no layout e é levado por translate e scale da
// caixa `de` (k = 0) até a caixa `para` (k = 1). Caixa é um elemento (medido uma vez por caixa()) ou {x, y, w, h} no
// mesmo sistema de caixa(); `para` nulo é o próprio lugar do elemento, e então k = 1 deixa o transform vazio. `arco`
// levanta o meio do voo em px (-arco·sen(πk)). k pode passar de 1, como numa mola. Ancestrais sem transform próprio.
export function voar(el, de, para, k, {arco = 0} = {}) {
	const N = medida(el);
	const A = de instanceof Element ? medida(de) : de || N, B = para instanceof Element ? medida(para) : para || N;
	const L = (a, b) => (k === 1 ? b : lerp(a, b, k));
	const x = L(A.x, B.x), y = L(A.y, B.y) - arco * Math.sin(Math.PI * clamp(k));
	const sx = L(A.w, B.w) / (N.w || 1), sy = L(A.h, B.h) / (N.h || 1);
	el.style.transformOrigin = '0 0';
	el.style.transform = x === N.x && y === N.y && sx === 1 && sy === 1 ? '' : `translate(${x - N.x}px, ${y - N.y}px) scale(${sx}, ${sy})`;
}

// Texto que se digita. Na primeira chamada o texto vira duas partes, a visível e o resto com visibility: hidden (a
// quebra de linha já é a final desde o começo), e cada caractere ganha um instante num ritmo de digitação fixado pela
// semente, com pausa depois de vírgula e ponto. k de 0 a 1. `cursor: true` mostra uma barra fina depois do último
// caractere visível: um span com fundo var(--cor-destaque), nunca um glifo (▌ cai na fonte do sistema). O deck
// decide quando, por exemplo {cursor: k < 1}. Só texto simples, sem elementos dentro.
const digitados = new WeakMap();
export function digitar(el, k, {cursor = false, semente = 1} = {}) {
	let d = digitados.get(el);
	if (!d) {
		const texto = el.textContent.replace(/\s+/g, ' ').trim();
		const letras = [...new Intl.Segmenter('pt', {granularity: 'grapheme'}).segment(texto)].map((g) => g.segment);
		const rnd = aleatorio(semente);
		let soma = 0;
		const acumulado = letras.map((c, i) => (soma += (0.6 + 0.8 * rnd()) * (/[,.;:!?]/.test(letras[i - 1] || '') ? 3 : 1)));
		const [vis, ancora, barra, resto] = ['span', 'span', 'span', 'span'].map((t) => document.createElement(t));
		resto.style.visibility = 'hidden';
		// Âncora inline vazia: a barra é absoluta dentro dela, então não ocupa largura nem cria ponto de quebra.
		ancora.style.position = 'relative';
		barra.style.cssText = 'position:absolute;left:0;top:0;bottom:0;width:.08em;background:var(--cor-destaque)';
		ancora.appendChild(barra);
		el.replaceChildren(vis, ancora, resto);
		d = {letras, limiares: acumulado.map((a) => a / soma), vis, resto, barra, n: -1};
		digitados.set(el, d);
	}
	let n = 0;
	while (n < d.letras.length && k >= d.limiares[n]) n++;
	if (n !== d.n) {
		d.vis.textContent = d.letras.slice(0, n).join('');
		d.resto.textContent = d.letras.slice(n).join('');
		d.n = n;
	}
	d.barra.style.visibility = cursor ? '' : 'hidden';
}

// Anotação à mão firme: um traço que se desenha (tracar) em volta do alvo ('circulo', 1,05 volta com o raio modulado
// em 1,5% por ruido()) ou embaixo dele ('sublinhado'). Alvo HTML: uma camada SVG é criada no offsetParent dele, em
// volta da caixa com `folga` px (se esse pai corta, anote o contêiner). Alvo <svg> (viewBox em px) ou <path>: o traço
// ocupa a caixa do svg e o deck cuida do estilo. O desenho sai da semente e é guardado: o mesmo k dá o mesmo traço.
const SVG = 'http://www.w3.org/2000/svg';
const anotacoes = new WeakMap();
const numero = (v) => v.toFixed(1);
const tracoCirculo = (w, h, semente, m) => {
	const cx = w / 2, cy = h / 2, rx = w / 2 - m, ry = h / 2 - m, a0 = -2.4, n = 120;
	let d = '';
	for (let i = 0; i <= n; i++) {
		const u = i / n, a = a0 + u * 1.05 * 2 * Math.PI;
		const f = 1 + 0.015 * (2 * ruido(a * 3, semente) - 1) + 0.02 * u;   // leve espiral: o fim passa por fora do começo
		d += `${i ? 'L' : 'M'}${numero(cx + rx * f * Math.cos(a))} ${numero(cy + ry * f * Math.sin(a))}`;
	}
	return d;
};
const tracoSublinhado = (w, h, semente, m) => {
	const n = 48, amp = Math.min(3, h / 2 - m);
	let d = '';
	for (let i = 0; i <= n; i++) {
		const u = i / n;
		d += `${i ? 'L' : 'M'}${numero(lerp(m, w - m, u))} ${numero(h / 2 + amp * (2 * ruido(u * 4, semente) - 1) - 2 * u)}`;
	}
	return d;
};
export function anotar(alvo, k, {forma = 'circulo', semente = 1, folga = 10} = {}) {
	let path = anotacoes.get(alvo);
	if (!path) {
		const m = 8;   // margem para a ponta redonda e para o ruído não saírem da caixa
		let w, h;
		if (alvo instanceof SVGElement) {
			const svg = alvo.ownerSVGElement || alvo;
			const vb = svg.viewBox.baseVal;
			w = vb && vb.width ? vb.width : svg.clientWidth;
			h = vb && vb.height ? vb.height : svg.clientHeight;
			path = alvo.tagName === 'path' ? alvo : svg.appendChild(document.createElementNS(SVG, 'path'));
		} else {
			const pai = alvo.offsetParent;
			if (!pai || !alvo.offsetWidth) return;   // ainda fora do layout: tenta no próximo quadro
			const ax = alvo.offsetLeft, ay = alvo.offsetTop, aw = alvo.offsetWidth, ah = alvo.offsetHeight;
			// O círculo envolve as quinas do alvo: semieixos √2 vezes a meia caixa, mais a folga.
			const c = forma === 'sublinhado'
				? {x: ax - folga, y: ay + ah + 6 - 20, w: aw + 2 * folga, h: 40}
				: {w: aw * Math.SQRT2 + 2 * (folga + m), h: ah * Math.SQRT2 + 2 * (folga + m)};
			if (c.x === undefined) { c.x = ax + aw / 2 - c.w / 2; c.y = ay + ah / 2 - c.h / 2; }
			const svg = document.createElementNS(SVG, 'svg');
			svg.setAttribute('width', c.w);
			svg.setAttribute('height', c.h);
			svg.style.cssText = `position:absolute;left:${c.x}px;top:${c.y}px;overflow:visible;pointer-events:none`;
			pai.appendChild(svg);
			({w, h} = c);
			path = svg.appendChild(document.createElementNS(SVG, 'path'));
		}
		if (path !== alvo) path.style.cssText = 'fill:none;stroke:var(--cor-destaque);stroke-width:6;stroke-linecap:round;stroke-linejoin:round';
		path.setAttribute('d', forma === 'sublinhado' ? tracoSublinhado(w, h, semente, m) : tracoCirculo(w, h, semente, m));
		anotacoes.set(alvo, path);
	}
	tracar(path, k);
}

// Aproximação lenta de foto (Ken Burns): começa em `escala` e assenta em scale(1) exato em k = 1, para a parada sair
// nítida e igual por qualquer caminho. `origem` é o ponto que fica parado (transform-origin).
export function kenburns(el, k, {escala = 1.06, origem = '50% 50%'} = {}) {
	el.style.transformOrigin = origem;
	el.style.transform = k >= 1 ? 'scale(1)' : `scale(${lerp(escala, 1, clamp(k))})`;
}

export {clamp, lerp, faixa, saida, entradaSaida, sair, chegar, mola, molaAR, escalonar, aleatorio, ruido, transformar, enquadrar};

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
#ap-bloco .atrasado { color: #F08A6C; } #ap-bloco .adiantado { color: #8FD3A8; }
#ap-pratica { font-size: 40px; font-weight: 600; color: #E8B04B; } #ap-pratica.passou { color: #F08A6C; }
#ap-guia { font-size: 26px; line-height: 1.45; margin-top: 18px; overflow: auto; } #ap-guia p { margin: 0 0 12px; }
#ap-guia ul { margin: 0 0 12px; padding-left: 1.2em; } #ap-guia .faca { color: #E8B04B; } #ap-guia .ponte { opacity: .7; }
#ap-prox-titulo { font-size: 24px; margin-top: 14px; }
#palco-pratica { right: 16px; bottom: 12px; padding: 2px 12px; border-radius: 8px; background: rgba(8,10,14,.55); font-size: 22px; font-variant-numeric: tabular-nums; opacity: .8; pointer-events: none; display: none; }
/* linha do dia: faixa fina abaixo da trilha, na largura dela (120 a 1800 px). Faz parte do quadro: só var() do tema */
#linha-dia { position: absolute; left: 120px; top: 993px; width: 1680px; display: flex; gap: 40px; z-index: 3; pointer-events: none;
  font: 500 30px/36px var(--fonte-titulo, system-ui); color: var(--cor-tinta-suave); white-space: nowrap; }
#linha-dia .ld-bloco { position: relative; flex: 1 1 auto; height: 44px; }
#linha-dia .ld-trilho { position: absolute; left: 0; right: 0; top: 40px; height: 4px; border-radius: 2px; background: var(--cor-linha); overflow: hidden; }
#linha-dia .ld-trilho b { position: absolute; inset: 0; background: currentColor; transform-origin: 0 50%; }
#linha-dia .atual { color: var(--cor-tinta); }
#linha-dia .atual .ld-trilho b { background: var(--cor-destaque); }
#linha-dia.noite { color: var(--suave-sobre-noite, var(--cor-suave-sobre-tinta)); }
#linha-dia.noite .ld-trilho { background: var(--linha-sobre-noite, var(--cor-linha-sobre-tinta)); }
#linha-dia.noite .atual { color: var(--sobre-noite, var(--cor-sobre-tinta)); }
`;

const $ = (sel) => document.querySelector(sel);

export function palco({titulo = document.title, slides, cenas = {}, desenhar = () => {}, mundo, segura = {}, blocos = [], autoplay = false} = {}) {
	const plano = planejar(slides);
	const dia = planejarDia(plano, blocos);
	plano.erros.push(...dia.erros);
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
	// Progresso suavizado da viagem do slide (viagem 0 é corte seco: faixa vira degrau).
	const viagemK = (t, s) => {
		const p0 = s.passos[0];
		return entradaSaida(faixa(t, p0.t0, p0.t0 + Math.min(s.viagem ?? p0.dur, p0.dur)));
	};
	const camera = (t, s) => {
		if (!s.passos.length || s.i === 0) return poses[s.i];
		const k = viagemK(t, s);
		const pose = misturarPose(poses[s.i - 1], poses[s.i], k);
		return s.recuo ? {...pose, z: pose.z * (1 - s.recuo * Math.sin(Math.PI * k))} : pose;
	};
	const kCamera = (t, s) => (usaCamera && s.i > 0 && s.camera ? viagemK(t, s) : 1);

	const slideEm = (t) => S.find((s) => t <= s.t1 + 1e-9) || S[S.length - 1];

	// Linha do dia: os blocos numa faixa fina abaixo da trilha, fora do mundo (não anda com a câmera). Aparece nos slides
	// que têm bloco e não têm `linhaDia: false`, entra e sai com o slide, troca para as cores da noite no meio da viagem
	// e enche o trilho do bloco atual com o tempo do deck. data-sinalizacao: o oráculo mede a legibilidade dela, mas não
	// a conta como conteúdo do slide (palavras, hierarquia, respiro).
	let linhaDia = null;
	if (blocos.length) {
		const el = document.createElement('div');
		el.id = 'linha-dia';
		el.dataset.sinalizacao = 'linha do dia';
		const itens = dia.blocos.map((b) => {
			const d = document.createElement('div'), rot = document.createElement('span'), trilho = document.createElement('i');
			d.className = 'ld-bloco';
			d.style.flexGrow = String(b.minutos || 1);
			rot.className = 'ld-rot';
			rot.textContent = b.rotulo;
			trilho.className = 'ld-trilho';
			const cheio = trilho.appendChild(document.createElement('b'));
			d.append(rot, trilho);
			el.appendChild(d);
			return {d, cheio};
		});
		palcoEl.appendChild(el);
		const noite = [];
		S.forEach((s, i) => { noite[i] = secoes[s.id] ? secoes[s.id].classList.contains('noite') : !!noite[i - 1]; });
		const mostra = (s) => !!s && dia.porSlide[s.i] >= 0 && s.linhaDia !== false;
		linhaDia = (t, s) => {
			const ant = S[s.i - 1], p0 = s.passos[0];
			const k = ant ? faixa(t, p0.t0, p0.t0 + Math.min(0.4, p0.dur)) : 1;
			// Durante a viagem a trilha cruza os nomes: a linha some no meio da câmera e volta ao assentar.
			const kc = ant ? Math.min(1, Math.max(0, kCamera(t, s))) : 1;
			const op = lerp(mostra(ant) ? 1 : 0, mostra(s) ? 1 : 0, k) * (1 - Math.sin(Math.PI * kc));
			el.style.opacity = String(op);
			el.style.visibility = op > 0 ? '' : 'hidden';
			el.classList.toggle('noite', noite[kCamera(t, s) < 0.5 && ant ? ant.i : s.i]);
			const atual = dia.porSlide[mostra(s) || !ant ? s.i : ant.i];
			itens.forEach(({d, cheio}, j) => {
				const b = dia.blocos[j];
				const f = j < atual ? 1 : j > atual || b.t0 === null ? 0 : faixa(t, b.t0, b.t1);
				d.classList.toggle('atual', j === atual);
				cheio.style.transform = `scaleX(${+f.toFixed(4)})`;
			});
		};
	}

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
	// molas), entrada suavizada, `ocioso` (só no slide atual, parado numa parada), a pose da câmera em t e o progresso
	// suavizado da viagem deste slide (kCamera: 0 antes, 1 depois e quando não há viagem).
	const ctxDe = (s, t, ocioso, atual, pose) => ({
		t, ocioso: atual ? ocioso : 0, modo: estado.modo, slide: s, i: s.i, atual, local: t - s.t0,
		camera: pose, kCamera: kCamera(t, s),
		passo: s.passos.findIndex((p) => t <= p.t1 + 1e-9),
		p: (n) => (s.passos[n] ? faixa(t, s.passos[n].t0, s.passos[n].t1) : 0),
		desde: (n) => t - (s.passos[n] ? s.passos[n].t0 : s.t1),
		entrada: entradaSaida(faixa(t, s.passos[0].t0, s.passos[0].t1)),
	});
	const ctxEm = (t, ocioso, pose) => {
		const s = slideEm(t);
		const k = (id, n = 0) => {
			const o = S.find((x) => x.id === id);
			if (!o) throw new Error(`slide "${id}" não existe`);
			return ctxDe(o, t, 0, false, pose).p(n);
		};
		return {...ctxDe(s, t, ocioso, true, pose), k, de: (id) => ctxDe(S.find((x) => x.id === id), t, 0, false, pose)};
	};

	// Fontes carregadas antes do primeiro quadro, ao vivo e no render: as medidas (caixa, voar, anotar, oráculo) só
	// valem com a métrica final, e document.fonts.ready não carrega fonte que ainda ninguém pediu.
	const fontes = Promise.all([...document.fonts].map((f) => f.load().catch(() => {}))).then(() => document.fonts.ready);

	let ver = async (t, ocioso = 0) => {
		await fontes;
		const c = usaCamera ? camera(t, slideEm(t)) : {cx: W / 2, cy: H / 2, z: 1, rot: 0};
		const ctx = ctxEm(t, ocioso, {...c});
		if (usaCamera) mundoEl.style.transform = `translate(${W / 2}px, ${H / 2}px) rotate(${c.rot || 0}deg) scale(${c.z}) translate(${-c.cx}px, ${-c.cy}px)`;
		visibilidade(t, ctx.slide);
		estado.pendentes = [];
		// Cada cena desenha o próprio slide a partir de t, então pular para qualquer instante dá o mesmo quadro. Desenha o
		// slide atual e o anterior durante a entrada (no modo mundo, todos).
		const s = ctx.slide, p0 = s.passos[0];
		const vis = mundo ? S : s.i > 0 && t > p0.t0 && t < p0.t1 ? [S[s.i - 1], s] : [s];
		for (const o of vis) if (cenas[o.id]) await cenas[o.id](t, o === s ? ctx : ctxDe(o, t, 0, false, ctx.camera));
		await desenhar(t, ctx);
		if (linhaDia) linhaDia(t, s);
		if (estado.pendentes.length) await Promise.all(estado.pendentes);
	};

	// Medida do DOM para o oráculo (./ap sondar): blocos de texto visíveis, em coordenadas do quadro.
	const visivel = (el) => {
		let alfa = 1;
		for (let n = el; n && n !== document.documentElement; n = n.parentElement) {
			const cs = getComputedStyle(n);
			if (cs.display === 'none' || cs.visibility === 'hidden') return 0;
			alfa *= parseFloat(cs.opacity);
		}
		return alfa;
	};
	const medir = () => {
		const blocos = [];
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
			const topoCortado = !!clipaPai && tintaTopo(el, cs, escala) < pai.getBoundingClientRect().top + pai.clientTop * escala - 1;
			// Fonte com área de glifo maior que a entrelinha (título justo) passa da própria caixa em cima e embaixo
			// sem transbordar de fato: a folga vertical desconta essa diferença, linha a linha.
			const lh = parseFloat(cs.lineHeight) * escala, linha = rg.getClientRects()[0];
			const fv = 2 + (lh && linha ? Math.max(0, (linha.height - lh) / 2) : 0);
			const ink = tinta(el, cs, escala, rt);
			blocos.push({
				texto, palavras: texto.split(' ').length, fonte: parseFloat(cs.fontSize) * escala,
				x: rt.left, y: rt.top, w: rt.width, h: rt.height,
				ty: ink.y, th: ink.h,
				cor: cor.slice(0, 3), alfa: alfa * (cor[3] ?? 1),
				transborda: rt.right > r.right + 2 || rt.bottom > r.bottom + fv || rt.left < r.left - 2 || rt.top < r.top - fv ||
					(clipaPai && (rt.right > pai.getBoundingClientRect().right + 2 || rt.bottom > pai.getBoundingClientRect().bottom + fv)),
				topoCortado,
				// isenção declarada do aviso de contraste (temas/*/regras.md): o motivo, ou null
				contrasteOk: el.closest('[data-contraste-ok]')?.dataset.contrasteOk ?? null,
				// sinalização do tocador (linha do dia): legibilidade sim, conteúdo do slide não
				sinalizacao: !!el.closest('[data-sinalizacao]'),
				id: el.id || '', caminho: caminho(el), ...origem(el),
			});
		}
		return blocos;
	};
	// Imagens e vídeos visíveis no quadro: tamanho natural, caixa do layout (ow, oh) e caixa na tela (w, h, já com o
	// zoom da câmera e os transforms), para o oráculo ver foto ampliada e medir o maior elemento da parada.
	const midias = () => [...palcoEl.querySelectorAll('img, video')].map((el) => {
		const r = el.getBoundingClientRect();
		return {
			tag: el.tagName.toLowerCase(), src: el.getAttribute('src') || '',
			nw: el.naturalWidth ?? el.videoWidth, nh: el.naturalHeight ?? el.videoHeight, ow: el.offsetWidth, oh: el.offsetHeight,
			x: r.left, y: r.top, w: r.width, h: r.height, fit: getComputedStyle(el).objectFit, alfa: visivel(el),
			tempo: el.tagName === 'VIDEO' ? el.currentTime : null,
		};
	}).filter((m) => m.alfa >= 0.1 && m.w >= 1 && m.h >= 1 && m.x < W && m.x + m.w > 0 && m.y < H && m.y + m.h > 0);
	// Topo da tinta da primeira linha do texto direto de `el`, em px da tela. A caixa do Range vai da ascendente da fonte
	// ao pé, e o acento de uma maiúscula cabe nela: um pai que corta abaixo da ascendente (título justo dentro de .corte)
	// apaga o acento sem que a caixa transborde. A altura da tinta vem do canvas, com a mesma fonte e a mesma caixa.
	let pincel = null;
	const tintaTopo = (el, cs, escala) => {
		const rg = document.createRange();
		let s = '', topo = null;
		linha: for (const n of el.childNodes) {
			if (n.nodeType !== 3) continue;
			for (let i = 0; i < n.data.length; i++) {
				rg.setStart(n, i);
				rg.setEnd(n, i + 1);
				const b = rg.getClientRects()[0];
				if (!b || !b.height) continue;
				if (topo === null) topo = b.top;
				else if (b.top > topo + b.height / 2) break linha;   // desceu para a segunda linha
				s += n.data[i];
			}
		}
		if (topo === null || !s.trim()) return Infinity;
		const lingua = document.documentElement.lang || undefined;
		if (cs.textTransform === 'uppercase') s = s.toLocaleUpperCase(lingua);
		else if (cs.textTransform === 'lowercase') s = s.toLocaleLowerCase(lingua);
		pincel = pincel || document.createElement('canvas').getContext('2d');
		pincel.font = `${cs.fontStyle} ${cs.fontWeight} ${cs.fontSize} ${cs.fontFamily}`;
		const m = pincel.measureText(s.trim());
		return topo + (m.fontBoundingBoxAscent - m.actualBoundingBoxAscent) * escala;
	};
	// Faixa vertical da tinta do bloco, em px da tela. A caixa do Range vai da ascendente ao pé da fonte, e numa linha
	// display em caixa alta a tinta ocupa só o meio dela: dois títulos empilhados pela tinta (a abertura da biblioteca)
	// têm caixas que se cruzam sem que as letras se toquem. A sobreposição do oráculo mede esta faixa.
	const tinta = (el, cs, escala, rt) => {
		const lingua = document.documentElement.lang || undefined;
		let s = el.textContent.replace(/\s+/g, ' ').trim();
		if (cs.textTransform === 'uppercase') s = s.toLocaleUpperCase(lingua);
		else if (cs.textTransform === 'lowercase') s = s.toLocaleLowerCase(lingua);
		pincel = pincel || document.createElement('canvas').getContext('2d');
		pincel.font = `${cs.fontStyle} ${cs.fontWeight} ${cs.fontSize} ${cs.fontFamily}`;
		const m = pincel.measureText(s);
		const y = rt.top + (m.fontBoundingBoxAscent - m.actualBoundingBoxAscent) * escala;
		const fim = rt.bottom - (m.fontBoundingBoxDescent - m.actualBoundingBoxDescent) * escala;
		return fim > y ? {y, h: fim - y} : {y: rt.top, h: rt.height};
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
		// viagem e camera dizem ao ./ap paradas --viagens onde fotografar; arquetipo (data-arquetipo da seção) e ritmoOk
		// (data-ritmo-ok da seção, ou `ritmoOk` no slide que é só uma pose de câmera, sem seção) vão para o oráculo.
		// notas é texto ou {diga, faca, transicao} (guia), para a tela do apresentador; bloco é o índice em `blocos` (-1 sem bloco)
		slides: S.map((s) => ({id: s.id, titulo: s.titulo, notas: typeof s.notas === 'string' ? s.notas : '', t0: s.t0, t1: s.t1, passos: s.passos.map((p) => p.dur),
			viagem: s.viagem ?? null, camera: !!s.camera, arquetipo: secoes[s.id]?.dataset.arquetipo || '',
			ritmoOk: s.ritmoOk ?? secoes[s.id]?.dataset.ritmoOk ?? null,
			bloco: dia.porSlide[s.i], guia: s.notas && typeof s.notas === 'object' ? s.notas : null, pratica: s.pratica ?? null})),
		paradas: paradas.map((p) => ({...p, id: S[p.slide].id})),
		blocos: dia.blocos,
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
			...resumo, linha: linha.trechos, medir, midias,
			ir: async (n, ocioso = 0) => { await ver(paradas[n].t, ocioso); await new Promise((r) => requestAnimationFrame(() => r())); },
			ver: async (t, ocioso = 0) => { await ver(t, ocioso); await new Promise((r) => requestAnimationFrame(() => r())); },
		};
		return window.__palco;
	}
	if (q.has('apresentador')) return apresentador(resumo);
	return tocador({ver, resumo, palcoEl, previa: q.has('previa') ? Number(q.get('previa')) : null, autoplay, fontes});
}

// ---------- ao vivo ----------

function tocador({ver, resumo, palcoEl, previa, autoplay, fontes}) {
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
	// Cronômetro de prática, discreto no canto e fora do #palco (não sai em still, PDF nem vídeo): conta desde a chegada
	// ao slide com `pratica` (minutos).
	const praticaEl = ui('palco-pratica');
	let pratica = null;

	let atual = Math.min(Number((location.hash.match(/parada=(\d+)/) || [])[1] || 0), paradas.length - 1);
	let tocando = null, chegada = performance.now(), janelaAp = null, digitos = '';
	const inicioPalestra = performance.now();

	const avisarAp = () => janelaAp && !janelaAp.closed && janelaAp.postMessage({palco: {atual, inicio: inicioPalestra}}, ALVO);
	const chegou = (n) => {
		const s = slides[paradas[n].slide];
		if (paradas[n].slide !== paradas[atual].slide || pratica === null) pratica = s.pratica ? {fim: performance.now() + s.pratica * 60000} : null;
		atual = n; tocando = null; chegada = performance.now();
		history.replaceState(null, '', `#parada=${n}`);
		avisarAp();
	};
	// Instante do trecho que está tocando: `vel` 3 quando um clique pediu pressa.
	const tocado = (agora) => Math.min(paradas[tocando.para].t, tocando.de + ((agora - tocando.inicio) / 1000) * tocando.vel);
	const proxima = () => {
		// Clique no meio da animação: o resto dela toca em 3x e o trecho seguinte começa sozinho, sem salto. Um segundo
		// clique durante a pressa completa na hora e segue.
		if (tocando && tocando.vel === 1) {
			const agora = performance.now();
			tocando = {de: tocado(agora), para: tocando.para, inicio: agora, vel: 3, seguir: true};
			return;
		}
		if (tocando) chegou(tocando.para);
		if (atual >= paradas.length - 1) return;
		tocando = {de: paradas[atual].t, para: atual + 1, inicio: performance.now(), vel: 1};
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
			const seguir = tocando.seguir;
			t = tocado(agora);
			if (t >= paradas[tocando.para].t) { chegou(tocando.para); if (seguir) proxima(); }
		} else {
			t = paradas[atual].t;
			ocioso = (agora - chegada) / 1000;
		}
		praticaEl.style.display = pratica ? 'block' : 'none';
		if (pratica) {
			const resta = (pratica.fim - agora) / 1000, txt = resta >= 0 ? relogio(Math.ceil(resta)) : '+' + relogio(-resta);
			if (praticaEl.textContent !== txt) praticaEl.textContent = txt;
		}
		try { await ver(t, ocioso); } finally { desenhando = false; }
	};
	quadro();
	// Abertura automática: na parada 0, a entrada do primeiro slide toca sozinha assim que as fontes carregam. Recarregar
	// no meio da aula (#parada=N) não toca nada.
	if (autoplay && atual === 0) fontes.then(() => { if (atual === 0 && !tocando) proxima(); });
}

// Tela do apresentador: parada atual e próxima (o próprio deck em modo prévia), notas, cronômetro e relógio.
function apresentador(resumo) {
	document.body.classList.add('apresentador');
	document.title = 'Apresentador · ' + resumo.titulo;
	const base = location.pathname + '?previa=';
	const ap = document.createElement('div');
	ap.id = 'ap';
	ap.innerHTML = `
<div id="ap-topo"><b id="ap-crono">00:00</b><span id="ap-relogio"></span><span id="ap-pos"></span><span id="ap-bloco"></span><b id="ap-pratica"></b><span style="opacity:.5">← → avançam daqui também</span></div>
<div><div class="rot">Agora · <span id="ap-slide"></span></div><iframe id="ap-agora" src="${base}0"></iframe><div id="ap-notas"></div><div id="ap-guia"></div></div>
<div><div class="rot">Próxima parada</div><iframe id="ap-prox" src="${base}1"></iframe><div id="ap-prox-titulo"></div></div>`;
	document.body.appendChild(ap);
	const agora = $('#ap-agora'), prox = $('#ap-prox');
	const {paradas, slides, blocos} = resumo;
	let atual = 0, inicio = null, bloco = -1, inicioBloco = null, pratica = null, slideVisto = -1;
	const el = (tag, cls, txt) => { const e = document.createElement(tag); if (cls) e.className = cls; e.textContent = txt; return e; };
	// Guia do slide: {diga, faca (texto ou lista de ações), transicao}.
	const guia = (g) => {
		const out = [];
		if (g.diga) out.push(el('p', '', g.diga));
		if (g.faca) {
			const ul = el('ul', 'faca', '');
			ul.append(...[].concat(g.faca).map((f) => el('li', '', f)));
			out.push(ul);
		}
		if (g.transicao) out.push(el('p', 'ponte', '→ ' + g.transicao));
		return out;
	};
	const proxima = () => {
		if (atual >= paradas.length - 1) return 'fim do deck';
		const p = paradas[atual + 1], s = slides[p.slide], n = s.passos.length;
		const novo = s.bloco >= 0 && s.bloco !== slides[paradas[atual].slide].bloco ? ` · novo bloco: ${blocos[s.bloco].rotulo}` : '';
		return `${s.titulo}${n > 1 ? ` (passo ${p.passo + 1} de ${n})` : ''}${novo}`;
	};
	const pintarRitmo = () => {
		const caixa = $('#ap-bloco');
		if (bloco < 0) { caixa.textContent = ''; return; }
		const b = blocos[bloco], dec = (performance.now() - inicioBloco) / 1000;
		const r = ritmoDoBloco(dec, b.minutos, fracaoDoBloco(b, atual));
		caixa.replaceChildren(`bloco ${bloco + 1} de ${blocos.length} · ${b.rotulo} · ${relogio(dec)}${b.minutos ? ` de ${relogio(b.minutos * 60)}` : ''}`);
		if (r.estado) caixa.append(' · ', el('span', r.estado.replace(' ', '-'), r.estado + (r.estado === 'no tempo' ? '' : ` ${relogio(Math.abs(r.saldo))}`)));
	};
	const pintarPratica = () => {
		const c = $('#ap-pratica');
		if (!pratica) { c.textContent = ''; return; }
		const resta = (pratica.fim - performance.now()) / 1000;
		const txt = resta >= 0 ? relogio(Math.ceil(resta)) : '+' + relogio(-resta);
		if (c.textContent !== txt) c.textContent = txt;
		c.classList.toggle('passou', resta < 0);
	};
	const pintar = () => {
		const p = paradas[atual], s = slides[p.slide];
		agora.contentWindow?.postMessage({palcoPrevia: atual}, ALVO);
		prox.contentWindow?.postMessage({palcoPrevia: Math.min(atual + 1, paradas.length - 1)}, ALVO);
		$('#ap-notas').textContent = s.notas;
		$('#ap-guia').replaceChildren(...(s.guia ? guia(s.guia) : []));
		$('#ap-pos').textContent = `slide ${p.slide + 1} de ${slides.length} · parada ${atual} de ${paradas.length - 1}`;
		$('#ap-slide').textContent = s.titulo;
		$('#ap-prox-titulo').textContent = 'Próxima: ' + proxima();
		pintarRitmo();
		pintarPratica();
	};
	const dois = (n) => String(Math.floor(n)).padStart(2, '0');
	setInterval(() => {
		const d = new Date();
		$('#ap-relogio').textContent = `${dois(d.getHours())}:${dois(d.getMinutes())}`;
		if (inicio !== null) { const s = (performance.now() - inicio) / 1000; $('#ap-crono').textContent = `${dois(s / 60)}:${dois(s % 60)}`; }
		pintarRitmo();
		pintarPratica();
	}, 250);
	addEventListener('message', (m) => {
		if (!deCasa(m) || m.source !== opener || !m.data || !m.data.palco) return;
		atual = m.data.palco.atual;
		const agoraMs = performance.now(), s = slides[paradas[atual].slide];
		if (inicio === null) inicio = agoraMs;
		// o bloco começa a contar quando a tela o vê pela primeira vez; a prática, quando chega ao slide dela
		if (s.bloco !== bloco) { bloco = s.bloco; inicioBloco = agoraMs; }
		if (paradas[atual].slide !== slideVisto) { slideVisto = paradas[atual].slide; pratica = s.pratica ? {fim: agoraMs + s.pratica * 60000} : null; }
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
