/* Estilo cinema: uma cena 3D atrás do texto HTML do palco. Contrato em docs/cinema.md.
   three.js r186 vem copiado em motor/vendor/three (MIT, LICENSE ao lado), sem internet em tempo de palco. O quadro continua
   função do tempo: a cena é desenhada dentro do desenhar(t, ctx) do palco, sem relógio, sem animação própria do three.js
   e com aleatório de semente. Texto nunca vai para dentro do 3D: fica no HTML, onde o oráculo mede. */
import * as THREE from './vendor/three/three.module.js';
import {EffectComposer} from './vendor/three/addons/postprocessing/EffectComposer.js';
import {RenderPass} from './vendor/three/addons/postprocessing/RenderPass.js';
import {UnrealBloomPass} from './vendor/three/addons/postprocessing/UnrealBloomPass.js';
import {OutputPass} from './vendor/three/addons/postprocessing/OutputPass.js';
import {Reflector} from './vendor/three/addons/objects/Reflector.js';
import {aleatorio, ruido, clamp, lerp} from './tempo.js';

export {THREE, Reflector};

const W = 1920, H = 1080;

// Cor de um token do tema como THREE.Color. O navegador resolve var() e color-mix, e um pixel de canvas 2D converte
// qualquer espaço de cor (oklch, display-p3) para sRGB; a cor nunca é escrita no deck. Token que não existe é erro,
// porque cairia calado no preto herdado.
let sonda, pixel;
export function corDoTema(token) {
	if (!getComputedStyle(document.documentElement).getPropertyValue(token).trim()) {
		throw new Error(`corDoTema: o tema não define ${token} (docs/temas.md)`);
	}
	sonda ??= Object.assign(document.createElement('i'), {hidden: true});
	if (!sonda.isConnected) document.body.append(sonda);
	sonda.style.color = `var(${token})`;
	pixel ??= Object.assign(document.createElement('canvas'), {width: 1, height: 1}).getContext('2d', {willReadFrequently: true});
	pixel.clearRect(0, 0, 1, 1);
	pixel.fillStyle = getComputedStyle(sonda).color;
	pixel.fillRect(0, 0, 1, 1);
	const [r, g, b, a] = pixel.getImageData(0, 0, 1, 1).data;
	if (a < 255) throw new Error(`corDoTema: ${token} é transparente; a cena precisa de cor sólida`);
	return new THREE.Color().setRGB(r / 255, g / 255, b / 255, THREE.SRGBColorSpace);
}

// Liga o 3D: um canvas de 1920×1080 no fundo do #palco, câmera, brilho (bloom) e saída com tone mapping ACES.
// `desenhar()` renderiza o quadro; chame-a uma vez, no fim do desenhar(t, ctx) do deck.
export function cinema({palco = document.getElementById('palco'), fov = 35, exposicao = 1,
	brilho: {forca = 0.9, raio = 0.55, limiar = 0.8} = {}, amostras = 4} = {}) {
	const canvas = document.createElement('canvas');
	canvas.id = 'cinema';
	canvas.width = W;
	canvas.height = H;
	Object.assign(canvas.style, {position: 'absolute', left: '0', top: '0', width: `${W}px`, height: `${H}px`});
	palco.prepend(canvas);
	// preserveDrawingBuffer: o still do ./ap paradas é tirado depois do quadro; sem ele o canvas pode sair vazio.
	const renderer = new THREE.WebGLRenderer({canvas, antialias: true, preserveDrawingBuffer: true, powerPreference: 'high-performance'});
	renderer.setPixelRatio(1);
	renderer.setSize(W, H, false);
	renderer.toneMapping = THREE.ACESFilmicToneMapping;
	renderer.toneMappingExposure = exposicao;
	const cena = new THREE.Scene();
	const camera = new THREE.PerspectiveCamera(fov, W / H, 0.1, 600);
	const alvo = new THREE.WebGLRenderTarget(W, H, {type: THREE.HalfFloatType, samples: amostras});
	const composer = new EffectComposer(renderer, alvo);
	composer.setPixelRatio(1);
	composer.setSize(W, H);
	composer.addPass(new RenderPass(cena, camera));
	const bloom = new UnrealBloomPass(new THREE.Vector2(W, H), forca, raio, limiar);
	composer.addPass(bloom);
	composer.addPass(new OutputPass());
	return {THREE, cena, camera, renderer, bloom, canvas, desenhar: () => composer.render()};
}

// Câmera por poses: [{pos: [x, y, z], alvo: [x, y, z], fov}], uma por parada. `u` vai de 0 (primeira pose) a
// poses.length - 1; entre inteiros, o caminho é uma Catmull-Rom centrípeta, que curva sem passar do ponto. Pose sem
// fov usa `fov` (padrão 35), nunca o da câmera: o quadro não pode depender do quadro anterior.
export function trajeto(poses, {fov = 35} = {}) {
	const v = (a) => new THREE.Vector3(...a);
	const P = new THREE.CatmullRomCurve3(poses.map((p) => v(p.pos)), false, 'centripetal');
	const A = new THREE.CatmullRomCurve3(poses.map((p) => v(p.alvo)), false, 'centripetal');
	const n = poses.length - 1, olhar = new THREE.Vector3();
	return (camera, u) => {
		const k = n ? clamp(u / n) : 0;
		camera.position.copy(P.getPoint(k));
		olhar.copy(A.getPoint(k));
		const i = Math.min(Math.max(n - 1, 0), Math.floor(clamp(u, 0, n))), f = clamp(u - i);
		const fov0 = poses[i].fov ?? fov, fov1 = (poses[i + 1] ?? poses[i]).fov ?? fov;
		camera.fov = lerp(fov0, fov1, f);
		camera.lookAt(olhar);
		camera.updateProjectionMatrix();
		return olhar;
	};
}

// Respiração de câmera parada: deriva lenta e pequena, de ruído com semente, somada à pose. `s` em segundos (o
// ocioso do palco), `amp` em metros. Some em 1,5 s a partir do zero, para não dar tranco quando a parada começa.
export function respirar(camera, s, {amp = 0.06, semente = 3} = {}) {
	const k = clamp(s / 1.5);
	const d = (eixo) => (ruido(s * 0.18, semente + eixo) - 0.5) * 2 * amp * k;
	camera.position.x += d(0);
	camera.position.y += d(1) * 0.6;
	camera.position.z += d(2);
}

// Fio de luz por uma sequência de pontos retos (traço de circuito). `revelar(k)` desenha do começo até a fração k
// do comprimento; `ponta(k)` dá a posição da frente do traço. Cor acima de 1 (intensidade) passa do limiar do brilho.
export function fio(pontos, {raio = 0.03, cor, intensidade = 4, segmentos = 400, lados = 8} = {}) {
	const caminho = new THREE.CurvePath();
	for (let i = 1; i < pontos.length; i++) caminho.add(new THREE.LineCurve3(new THREE.Vector3(...pontos[i - 1]), new THREE.Vector3(...pontos[i])));
	const geo = new THREE.TubeGeometry(caminho, segmentos, raio, lados, false);
	const mat = new THREE.MeshBasicMaterial({color: cor.clone().multiplyScalar(intensidade)});
	const malha = new THREE.Mesh(geo, mat);
	const porSegmento = lados * 6;
	malha.userData.revelar = (k, de = 0) => {
		const a = Math.floor(clamp(de) * segmentos), b = Math.ceil(clamp(k) * segmentos);
		geo.setDrawRange(a * porSegmento, Math.max(0, b - a) * porSegmento);
		malha.visible = b > a;
	};
	malha.userData.ponta = (k) => caminho.getPointAt(clamp(k));
	malha.userData.revelar(1);
	return malha;
}

// Disco de luz (gradiente radial branco, desenhado uma vez num canvas 2D): textura do halo e dos grãos de poeira.
let disco;
const discoDeLuz = () => {
	if (disco) return disco;
	const c = document.createElement('canvas');
	c.width = c.height = 128;
	const g = c.getContext('2d'), r = g.createRadialGradient(64, 64, 0, 64, 64, 64);
	r.addColorStop(0, 'rgba(255,255,255,1)');
	r.addColorStop(0.18, 'rgba(255,255,255,0.55)');
	r.addColorStop(1, 'rgba(255,255,255,0)');
	g.fillStyle = r;
	g.fillRect(0, 0, 128, 128);
	return (disco = new THREE.CanvasTexture(c));
};

// Halo aditivo: a cabeça do fio, uma lâmpada, um pad. Sem teste de profundidade, porque um halo encostado no chão
// sairia cortado ao meio pela linha do piso.
export function halo(cor, {tamanho = 1, intensidade = 1} = {}) {
	const mat = new THREE.SpriteMaterial({map: discoDeLuz(), color: cor.clone().multiplyScalar(intensidade),
		blending: THREE.AdditiveBlending, depthWrite: false, depthTest: false, transparent: true});
	const s = new THREE.Sprite(mat);
	s.scale.setScalar(tamanho);
	s.renderOrder = 10;
	return s;
}

// Lajes de pedra para o piso: textura em tons de cinza (a cor vem do material), juntas finas e leve variação por laje,
// fixada pela semente. `lado` é quantas lajes a textura tem por lado; repita-a com texture.repeat.
export function lajes({lado = 4, semente = 5, resolucao = 1024, junta = 0.012, variacao = 0.08} = {}) {
	const c = document.createElement('canvas');
	c.width = c.height = resolucao;
	const g = c.getContext('2d'), r = aleatorio(semente), passo = resolucao / lado;
	for (let i = 0; i < lado; i++) for (let j = 0; j < lado; j++) {
		const v = Math.round(255 * (1 - variacao * r()));
		g.fillStyle = `rgb(${v},${v},${v})`;
		g.fillRect(i * passo, j * passo, passo, passo);
	}
	g.fillStyle = 'rgb(90,90,90)';
	const e = Math.max(1, Math.round(junta * resolucao));
	for (let i = 0; i <= lado; i++) {
		g.fillRect(i * passo - e / 2, 0, e, resolucao);
		g.fillRect(0, i * passo - e / 2, resolucao, e);
	}
	const tx = new THREE.CanvasTexture(c);
	tx.wrapS = tx.wrapT = THREE.RepeatWrapping;
	tx.colorSpace = THREE.SRGBColorSpace;
	tx.anisotropy = 8;
	return tx;
}

// Céu em gradiente (esfera vista por dentro): `topo` no zênite, `horizonte` na linha do chão. As cores são uniforms,
// e o deck as troca em t (noite que amanhece) com .copy() ou .lerpColors().
export function ceu({topo, horizonte, raio = 500, expoente = 0.6}) {
	const mat = new THREE.ShaderMaterial({
		side: THREE.BackSide, depthWrite: false, fog: false,
		uniforms: {topo: {value: topo.clone()}, horizonte: {value: horizonte.clone()}, expoente: {value: expoente}},
		vertexShader: 'varying vec3 vP; void main(){ vP = normalize(position); gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }',
		fragmentShader: 'uniform vec3 topo; uniform vec3 horizonte; uniform float expoente; varying vec3 vP; void main(){ float h = pow(max(vP.y, 0.0), expoente); gl_FragColor = vec4(mix(horizonte, topo, h), 1.0); }',
	});
	const m = new THREE.Mesh(new THREE.SphereGeometry(raio, 32, 16), mat);
	m.renderOrder = -1;
	return m;
}

// Poeira no ar: n pontos fixados pela semente dentro de `caixa`, que flutuam devagar em função de t.
export function poeira({n = 500, caixa = [[-20, 0, -20], [20, 12, 20]], semente = 7, cor, tamanho = 0.05, opacidade = 0.8} = {}) {
	const r = aleatorio(semente), base = new Float32Array(n * 3), fase = new Float32Array(n);
	for (let i = 0; i < n; i++) {
		for (let e = 0; e < 3; e++) base[i * 3 + e] = lerp(caixa[0][e], caixa[1][e], r());
		fase[i] = r() * Math.PI * 2;
	}
	const pos = new Float32Array(base);
	const geo = new THREE.BufferGeometry();
	geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
	const mat = new THREE.PointsMaterial({color: cor, size: tamanho, map: discoDeLuz(), transparent: true, opacity: opacidade,
		blending: THREE.AdditiveBlending, depthWrite: false, sizeAttenuation: true});
	const pontos = new THREE.Points(geo, mat);
	pontos.userData.desenhar = (t) => {
		for (let i = 0; i < n; i++) {
			const f = fase[i];
			pos[i * 3] = base[i * 3] + Math.sin(t * 0.13 + f) * 0.35;
			pos[i * 3 + 1] = base[i * 3 + 1] + Math.sin(t * 0.09 + f * 1.7) * 0.25;
			pos[i * 3 + 2] = base[i * 3 + 2] + Math.cos(t * 0.11 + f) * 0.35;
		}
		geo.attributes.position.needsUpdate = true;
	};
	return pontos;
}
