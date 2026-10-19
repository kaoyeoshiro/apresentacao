---
name: apresentacao
description: Produz apresentações ao vivo de alto impacto feitas por código (motor de palco), para projetar com passador de slides, com animação a cada clique, imagens geradas por GPT ou Gemini, vídeo por código ou pelo Gemini Omni dentro do slide, tela do apresentador, PDF de contingência e pacote que roda sem internet. Use para "faz uma apresentação", "slides para minha palestra", "deck para a aula", "apresentação animada", "transforma isso em slides", "palestra sobre X", ou para revisar por que um deck parece PowerPoint de modelo. Não use para .pptx editável nem para vídeo narrado.
---

# apresentacao

O agente é diretor de arte, roteirista, programador e revisor da apresentação. O deck é código em
`decks/<slug>/deck.html`, sobre `motor/palco.js`; o contrato técnico está em `docs/palco.md` e o dos temas em
`docs/temas.md`. A apresentação existe para alguém falar na frente dela: a tela carrega imagem, número e frase
curta, e a fala carrega o argumento.

## Protocolo (nesta ordem)

### 1. Perguntar

Use a ferramenta de perguntas, no máximo três por vez, a opção recomendada primeiro. Sempre, mesmo que o pedido
já cite um deles, confirme:

1. **Tema**: um de `temas/` (`ls temas | grep -v '^_'`: hoje `noite`, `cojuris`, `pge`) ou "Outro". Nunca herde o
   tema da apresentação anterior. Tema novo se cria antes de tudo (`docs/temas.md`, seção final).
2. **Modo**: "Slides com transições (Recomendado)", em que cada slide entra por corte, fade ou empurrão, ou "Plano
   contínuo", em que os slides ficam espalhados num mundo e a câmera viaja entre eles (`camera` em cada slide e
   `<div id="mundo">`). O plano contínuo impressiona mais e custa mais a fazer bem: cada viagem precisa de um motivo
   no conteúdo.
3. **Público, duração e a mensagem** que a plateia deve levar em uma frase, se o pedido não disser.

Dúvida técnica não vira pergunta: decida e anote no briefing.

### 2. Briefing → `decks/<slug>/briefing.md`

Público, duração, ocasião (sala, auditório, online), a mensagem em uma frase, o que a plateia deve fazer ou decidir
no fim, tema e modo escolhidos, prazo. Leia `temas/<tema>/regras.md` antes de escrever qualquer texto: ele manda
em voz, grafia de nomes e cargos, avisos obrigatórios e no que a marca nunca diz. Se o usuário mandar material
(roteiro, apostila, deck antigo) e um arquivo não abrir, diga onde tentou; não invente o conteúdo.

### 3. Apuração

Cada número, nome, lei, data e caso vem de fonte lida nesta sessão e fica anotado no briefing ao lado do slide que
o usa. O que não tiver fonte sai do deck; o que ficou por confirmar aparece na tela com `[CONFERIR]` e entra na
lista de pendências da entrega; exemplo ilustrativo aparece marcado como tal. Telas de sistemas entram por captura
no claude_video_maker (`./cvm capturar`), com dados pessoais mascarados, e chegam ao deck por `./ap trazer`.

### 4. Arco e roteiro de slides

Escreva o arco antes dos slides: abertura que cria tensão, três a cinco movimentos, fecho com a mensagem e o
pedido. Depois, uma linha por slide no briefing: a ideia única, o que a tela mostra, o que a fala diz, quantos
cliques e, no plano contínuo, o que a câmera carrega de um slide ao seguinte. Densidade: até 45 palavras visíveis
por parada, de preferência menos de 20. Um slide por minuto e meio a dois de fala é o ponto de partida. O texto que
o público vê é escolha do usuário: mostre o roteiro e espere o sim antes de construir.

### 5. Criar e prototipar

```bash
./ap novo <slug> --tema <tema>
```

Isso copia `decks/demo/` com o tema trocado. Cor, fonte e logo nunca aparecem no deck: só `var(--...)` do tema
(cores próprias do deck, se precisar, misturadas com `--cor-tinta` por `color-mix`, como `--azul` e `--erro` da
demonstração). Implemente primeiro a abertura, o slide mais denso e um slide com dado ou diagrama; rode `./ap
sondar` e `./ap paradas`, abra a folha de contato e cada still, e corrija o sistema visual antes de seguir.

### 6. Deck completo

Movimento com função: revelar o que a fala anuncia, construir um diagrama na ordem do raciocínio, levar o olhar
de um dado ao seguinte. Uma coisa se mexe por vez; cada passo dura de 0,5 a 1,5 s; entradas com `entrar` e
`revelar`, nunca bounce nem zoom contínuo sem causa. Cada slide termina parado, numa tela estável para o
apresentador falar em cima. Espaço vazio é bem-vindo, e um momento autoral por apresentação basta.

Matéria-prima que eleva o slide, sempre arquivo local em `midia/` com crédito em `midia/creditos.json`:

- imagem gerada (`./ap imagem decks/<slug> <nome> "prompt"`, GPT Image por padrão, `--backend gemini` para o
  Gemini) quando prova ou ilustra algo que o código não desenha bem: fotografia, textura, cena. Nunca para
  enfeitar, nunca logo, nunca pessoa real. Descreva luz, lente, composição e paleta do tema no prompt;
- clipe do Gemini Omni (`./ap video-ia ...`), que custa dinheiro: rode sem `--aprovado`, mostre ao usuário o
  custo e o que o clipe mostra, e só com o sim dele para aquele clipe e aquele custo rode com `--aprovado HASH`;
- vídeo por código (`./cvm html`, Remotion ou Manim no claude_video_maker), trazido com `./ap trazer` e tocado com
  `video(el, seg)`;
- gráficos desenhados no próprio deck (SVG com `tracar`, números com `contar`), com a fonte no briefing.

Logo é sempre recorte do arquivo oficial em `temas/<tema>/marca/`, por `var(--logo-marca)`; logo com tinta escura
só entra sobre fundo claro. Notas do apresentador em cada slide (`notas`), escritas para leitura de relance.

### 7. Crítica (três rodadas)

A cada rodada: `./ap sondar` sem ERRO, `./ap paradas` com a folha e os stills abertos, e as perguntas: cada parada
se lê em três segundos do fundo da sala? há slide que é só texto? o destaque aponta para a coisa certa? alguma
animação existe só para enfeitar? o slide termina parado? Nomeie os piores defeitos, corrija os três maiores e
registre o que ficou. Depois abra ao vivo (`./ap abrir decks/<slug>`) e passe o deck inteiro pelas teclas, com a
tela do apresentador aberta (P).

### 8. Entrega

`./ap empacotar decks/<slug>` gera a pasta que abre sem internet, com o PDF de emergência; `./ap video` se pedido.
Diga ao usuário onde está o pacote, como abrir (dois cliques em `apresentacao.html` no Chrome; F tela cheia; P tela
do apresentador; o passador funciona como as setas) e que deve ensaiar uma vez no computador e no projetor do
evento. Liste as pendências: `[CONFERIR]`, fonte provisória do tema, gastos de geração.

## Proibido

- Fato sem fonte, logo redesenhado ou gerado por IA, foto de banco genérica, ícone como decoração.
- Lista de tópicos como layout padrão; parágrafo em slide.
- Texto abaixo de 30 px; cor, fonte ou logo escritos no deck em vez de vir do tema.
- Recurso da internet em tempo de palco (fonte, vídeo, imagem, iframe): tudo local no pacote.
- Gerar clipe pago sem o sim do usuário para aquele custo.
- Copiar código ou texto do onetake (PolyForm Noncommercial): as ideias inspiraram o plano contínuo, o código é
  próprio.
