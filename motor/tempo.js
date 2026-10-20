// Biblioteca mínima para composições HTML: tudo é função pura do tempo t (segundos).
// Nada de setTimeout, requestAnimationFrame, Date.now() ou Math.random() sem semente:
// o renderizador chama window.__seek(t) quadro a quadro e o resultado tem de ser idêntico.

export const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
export const lerp = (a, b, k) => a + (b - a) * k;
// De 0 em t0 a 1 em t1. Faixa de duração zero (ou invertida) é um degrau em t0: 0 até t0, 1 depois (sem NaN).
export const faixa = (t, t0, t1) => (t1 <= t0 ? (t > t0 ? 1 : 0) : clamp((t - t0) / (t1 - t0)));

// Curvas (cubic-bezier resolvido numericamente, como no CSS).
export const bezier = (x1, y1, x2, y2) => {
	const A = (a, b) => 1 - 3 * b + 3 * a, B = (a, b) => 3 * b - 6 * a, C = (a) => 3 * a;
	const f = (t, a, b) => ((A(a, b) * t + B(a, b)) * t + C(a)) * t;
	const df = (t, a, b) => 3 * A(a, b) * t * t + 2 * B(a, b) * t + C(a);
	return (x) => {
		if (x <= 0 || x >= 1) return clamp(x);
		let t = x;
		for (let i = 0; i < 8; i++) t -= (f(t, x1, x2) - x) / (df(t, x1, x2) || 1e-6);
		return f(clamp(t), y1, y2);
	};
};
export const saida = bezier(0.16, 1, 0.3, 1);
export const entradaSaida = bezier(0.65, 0, 0.35, 1);
// Para o que deixa a tela (começa devagar e acelera) e para o que pousa (chega rápido e assenta longo).
export const sair = bezier(0.3, 0, 0.8, 0.15);
export const chegar = bezier(0.05, 0.7, 0.1, 1);

// Mola analítica (sub-amortecida): posição em função do tempo decorrido, sem integração.
export const mola = (dt, {rigidez = 170, amortecimento = 20, massa = 1} = {}) => {
	if (dt <= 0) return 0;
	const w0 = Math.sqrt(rigidez / massa);
	const z = amortecimento / (2 * Math.sqrt(rigidez * massa));
	if (z >= 1) return 1 - (1 + w0 * dt) * Math.exp(-w0 * dt);
	const wd = w0 * Math.sqrt(1 - z * z);
	return 1 - Math.exp(-z * w0 * dt) * (Math.cos(wd * dt) + ((z * w0) / wd) * Math.sin(wd * dt));
};

// A mesma mola dita como no design de interface: `resposta` é o período em segundos (rigidez (2π/resposta)²) e
// `amortecimento` é a razão ζ (1 não passa do alvo; 0,77 equivale a entrar()). Perto do fim vira 1 exato, como
// entrar(): escala de 0,999 numa parada rasteriza diferente conforme o caminho até ali.
export const molaAR = (dt, {resposta = 0.5, amortecimento = 0.9} = {}) => {
	const k = mola(dt, {rigidez: (2 * Math.PI / resposta) ** 2, amortecimento: (4 * Math.PI * amortecimento) / resposta});
	return dt > 0.3 && Math.abs(k - 1) < 2e-3 ? 1 : k;
};

// Trilha de valor com vários alvos no tempo: cada mudança de alvo soma uma mola própria, então
// o valor continua de onde estava (com a velocidade que tinha) em vez de reiniciar do zero.
// alvos: [{t, v}] ordenado por t; antes do primeiro alvo vale o primeiro v.
export const trilha = (t, alvos, cfg) => {
	let y = alvos[0].v;
	for (let i = 1; i < alvos.length; i++) y += (alvos[i].v - alvos[i - 1].v) * mola(t - alvos[i].t, cfg);
	return y;
};

// Atrasos de uma onda, em segundos: cada item começa `quantidade` × curva(d / dmax) depois, sendo d a distância dele
// até a origem. `itens`: um número n (fila, a distância é o índice) ou posições medidas uma vez ({x, y} ou caixas
// {x, y, w, h}, que valem pelo centro). `de`: 'inicio' (o primeiro item), 'centro', 'bordas' (de fora para dentro) ou {x, y}.
export const escalonar = (itens, {de = 'inicio', quantidade = 0.4, curva = (x) => x} = {}) => {
	const P = typeof itens === 'number'
		? Array.from({length: itens}, (_, i) => ({x: i, y: 0}))
		: itens.map((c) => ({x: c.x + (c.w || 0) / 2, y: c.y + (c.h || 0) / 2}));
	if (!P.length) return [];
	const centro = {x: P.reduce((a, p) => a + p.x, 0) / P.length, y: P.reduce((a, p) => a + p.y, 0) / P.length};
	const o = de === 'inicio' ? P[0] : de === 'centro' || de === 'bordas' ? centro : de;
	let d = P.map((p) => Math.hypot(p.x - o.x, p.y - o.y));
	const dmax = Math.max(...d);
	if (de === 'bordas') d = d.map((x) => dmax - x);
	return d.map((x) => (dmax > 0 ? quantidade * curva(x / dmax) : 0));
};

// Aleatório com semente (mulberry32): mesmo valor para a mesma semente, sempre.
export const aleatorio = (semente) => {
	let a = semente >>> 0;
	return () => {
		a = (a + 0x6d2b79f5) >>> 0;
		let t = Math.imul(a ^ (a >>> 15), 1 | a);
		t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
		return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
	};
};

// Ruído de valor 1D suave, determinístico.
export const ruido = (x, semente = 1) => {
	const h = (i) => {
		let n = (i * 374761393 + semente * 668265263) | 0;
		n = Math.imul(n ^ (n >>> 13), 1274126177);
		return ((n ^ (n >>> 16)) >>> 0) / 4294967296;
	};
	const i = Math.floor(x), f = x - i, u = f * f * (3 - 2 * f);
	return lerp(h(i), h(i + 1), u);
};

// Registra a composição. `desenhar(t)` pode ser síncrona ou devolver Promise.
export const composicao = ({largura = 1920, altura = 1080, fps = 30, duracao, desenhar}) => {
	window.__meta = {largura, altura, fps, duracao};
	window.__seek = async (t) => {
		await desenhar(t);
		await new Promise((r) => requestAnimationFrame(() => r()));
	};
	// Pré-visualização no navegador comum: toca em tempo real (só fora do renderizador).
	if (!navigator.webdriver) {
		const t0 = performance.now();
		const loop = async () => {
			await desenhar(((performance.now() - t0) / 1000) % duracao);
			requestAnimationFrame(loop);
		};
		loop();
	}
};
