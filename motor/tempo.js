// Biblioteca mínima para composições HTML: tudo é função pura do tempo t (segundos).
// Nada de setTimeout, requestAnimationFrame, Date.now() ou Math.random() sem semente:
// o renderizador chama window.__seek(t) quadro a quadro e o resultado tem de ser idêntico.

export const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
export const lerp = (a, b, k) => a + (b - a) * k;
export const faixa = (t, t0, t1) => clamp((t - t0) / (t1 - t0));

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

// Mola analítica (sub-amortecida): posição em função do tempo decorrido, sem integração.
export const mola = (dt, {rigidez = 170, amortecimento = 20, massa = 1} = {}) => {
	if (dt <= 0) return 0;
	const w0 = Math.sqrt(rigidez / massa);
	const z = amortecimento / (2 * Math.sqrt(rigidez * massa));
	if (z >= 1) return 1 - (1 + w0 * dt) * Math.exp(-w0 * dt);
	const wd = w0 * Math.sqrt(1 - z * z);
	return 1 - Math.exp(-z * w0 * dt) * (Math.cos(wd * dt) + ((z * w0) / wd) * Math.sin(wd * dt));
};

// Trilha de valor com vários alvos no tempo: cada mudança de alvo soma uma mola própria, então
// o valor continua de onde estava (com a velocidade que tinha) em vez de reiniciar do zero.
// alvos: [{t, v}] ordenado por t; antes do primeiro alvo vale o primeiro v.
export const trilha = (t, alvos, cfg) => {
	let y = alvos[0].v;
	for (let i = 1; i < alvos.length; i++) y += (alvos[i].v - alvos[i - 1].v) * mola(t - alvos[i].t, cfg);
	return y;
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
