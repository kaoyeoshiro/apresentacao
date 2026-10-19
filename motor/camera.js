// Câmera sobre um mundo em DOM e transformação de um elemento em outro, para o modo mundo do palco (slides espalhados
// num plano e uma câmera que viaja entre eles). Vem do modo take único do claude_video_maker, só com o que o palco usa.
import {lerp} from './tempo.js';

// Pose que mostra `caixa` (mundo: {x, y, w, h}) inteira, com margem relativa.
export const enquadrar = (caixa, {largura, altura}, margem = 0.1) => ({
	cx: caixa.x + caixa.w / 2, cy: caixa.y + caixa.h / 2, rot: 0,
	z: Math.min((largura * (1 - 2 * margem)) / caixa.w, (altura * (1 - 2 * margem)) / caixa.h),
});

// Entre duas poses: zoom geométrico (velocidade percebida constante) e centro interpolado pela largura visível,
// que mantém em linha reta na tela o ponto para onde a câmera está indo.
export const misturarPose = (a, b, k) => {
	const z = a.z * Math.pow(b.z / a.z, k);
	const wa = 1 / a.z, wb = 1 / b.z;
	const s = Math.abs(wb - wa) < 1e-9 ? k : (1 / z - wa) / (wb - wa);
	return {cx: lerp(a.cx, b.cx, s), cy: lerp(a.cy, b.cy, s), z, rot: lerp(a.rot || 0, b.rot || 0, k)};
};

const hex = (c) => {
	let s = c.replace('#', '');
	if (s.length === 3) s = [...s].map((x) => x + x).join('');
	const n = parseInt(s, 16);
	return [(n >> 16) & 255, (n >> 8) & 255, n & 255];
};
export const misturarCor = (a, b, k) => {
	const A = hex(a), B = hex(b);
	return `rgb(${A.map((v, i) => Math.round(lerp(v, B[i], k))).join(',')})`;
};

// O mesmo elemento vai do estado `de` (k = 0) ao `para` (k = 1): {x, y, w, h, raio, cor, alfa}. Passe k já suavizado;
// `kCor` dá à cor um andamento próprio, para não passar tempo demais numa cor intermediária feia.
export const transformar = (el, de, para, k, kCor = k) => {
	const v = (c, d) => lerp(de[c] ?? d, para[c] ?? d, k);
	const s = el.style;
	s.position = 'absolute';
	s.left = `${v('x', 0)}px`;
	s.top = `${v('y', 0)}px`;
	s.width = `${v('w', 0)}px`;
	s.height = `${v('h', 0)}px`;
	s.borderRadius = `${v('raio', 0)}px`;
	s.opacity = v('alfa', 1);
	if (de.cor && para.cor) s.backgroundColor = misturarCor(de.cor, para.cor, kCor);
};
