# Briefing: prévia do curso de IA da co.juris (Fase 1)

Prévia de 14 slides, um clique por slide, para o usuário aprovar ao vivo (`./ap abrir decks/previa-curso-ia`) o
estilo das duas primeiras aulas antes do roteiro completo. As manchetes são provisórias. Cada aula tem um único
momento de surpresa (a data inventada na Aula 1, os papéis que viram skill e pasta na Aula 2), e o resto fica em tom
quieto.

- Público presumido: advogados e profissionais do direito sem formação técnica (confirmar).
- Tema `cojuris`, em plano contínuo. Os slides são nós de uma trilha de circuito dourada; nas aberturas, quatro traços
  saem pela borda direita da foto e descem até a trilha durante a viagem.
- Partitura de luz: aula1, data, aula2 e os três quadros da demonstração em marinho; o resto em off-white. O dourado
  marca só o que está sendo apontado; sobre o claro ele aparece como preenchimento, nunca como texto miúdo.
- Sem logo nesta prévia: o `regras.md` só admite o logo sobre fundo claro e as aberturas são escuras.

## Decisões do usuário em 19/10/2026

A Fase 1 foi aprovada inteira. Todos os geradores de imagem do image-video-api ficam liberados, Azure/SERPRO
incluídos; nesta fase o Gemini fez todas as imagens da tela, e o GPT Image foi tentado uma vez, sem aprovação, na
heroica da Aula 2. A demonstração é um vídeo de exemplo neutro, feito por código, sobre um
caso fictício. Continua valendo um clique por slide, e a trilha dourada com os traços das aberturas descendo até ela
fica, porque o usuário gostou dela. Clipe de vídeo pago (Omni, Veo) não está autorizado.

## Slides

| # | slide | manchete provisória | o que a tela prova | mídia | fonte ou pendência |
|---|---|---|---|---|---|
| 1 | aula1 | O que é IA | abertura | `heroi-aula1.webp` (selo) | só título |
| 2 | palavra | A IA escreve uma palavra por vez | a frase cresce em duas rodadas; leque de candidatas com barras, a vencedora voa para a frase | código | mecanismo geral; pedido 52/21/9 e procedente 46/38/9 são ilustrativos (pílula) |
| 3 | data | Sem o contrato, a data é inventada | leque achatado de quatro datas (6% a 8%), anel de sorteio, 05/08/2020 entra sublinhada como "plausível e inventada" | código | datas e valores ilustrativos (pílula); nenhuma candidata coincide com 12/03/2019, a data do contrato fictício dos slides 11 e 14; a fala sobre alucinação depende de Kalai et al. [CONFERIR] |
| 4 | benchmark | Benchmark, a mesma prova com gabarito | dez questões corrigidas a caneta, nota 8 de 10 | código | mecanismo geral; nota ilustrativa (pílula) |
| 5 | arena | Arena, pessoas votam sem saber qual IA | duas respostas sem nome, cada uma com o rótulo "modelo oculto"; a pessoa circula B | código | mecanismo da LMArena [CONFERIR] (pílula na tela); nenhum número na tela |
| 6 | mercado | Onde fica o dado do cliente | a trilha se divide em dois ramos iguais; seis nomes só em texto, mesmo peso, sem vencedor; a legenda diz que gpt-oss e Gemma também rodam no escritório, sem usar o termo "pesos abertos" | código | [CONFERIR] lista e exceções de out/2026 (pílula na tela) |
| 7 | aula2 | Prompt, contexto e skill | abertura; a foto é a mesma pasta kraft do slide 10, fechada e vista de cima, menor que a tela e com as bordas dissolvidas no marinho, abaixo dos traços do circuito | `heroi-aula2.webp` (selo) | só título |
| 8 | prompt | Prompt é o pedido; contexto é o material | o pedido se digita ao lado da inicial, do contrato e do modelo | `doc-peticao`, `doc-contrato`, `doc-modelo` (selo) | pedido escrito para a prévia; os papéis não têm texto legível |
| 9 | skill | A skill guarda o pedido e o modelo | o cartão do pedido viaja inteiro com o texto e vira o SKILL.md (mesmo ícone de arquivo da árvore do slide 10), e o modelo vai para referências; inicial e contrato, menores e lado a lado, ficam de fora, sob o rótulo "deste caso" | os mesmos papéis | [CONFERIR] formato de Agent Skills (pílula na tela) |
| 10 | pasta | Os autos vão para a pasta do caso | a árvore nasce pela raiz; inicial e contrato cruzam a tela ainda grandes até perto da árvore e só no último terço encolhem até os ícones de `autos/`; o arquivo surge no pouso e só então o nome acende em dourado | `pasta-aberta.webp` (selo sob a foto) | estrutura ilustrativa, caso fictício |
| 11 | fonte | Cada linha aponta para um documento | fios da minuta até contrato, inicial e SKILL.md (dourado só no da data); a linha da data é a maior da minuta e a data só acende em dourado quando o fio do contrato chega a ela; uma linha fica sem fio, com "sem fonte: conferir" | código | caso fictício; 12/03/2019 é a data do contrato fictício, a mesma do vídeo |
| 12 | demo | Funcionando, num caso fictício | o vídeo toca numa moldura de navegador neutra | `demo.mp4`, `demo-capa.webp` | vídeo feito por código, sem dado real |
| 13 | demo-skill | (mergulho) | zoom na árvore e no selo "skill carregada", holofote e legenda | `demo.mp4` | idem |
| 14 | demo-minuta | (mergulho) | zoom na minuta; holofote na linha da data, que veio de `autos/contrato.pdf` | `demo.mp4` | idem |

A pergunta da data fica aberta do slide 3 ao slide 11, onde o fio do contrato a responde, e volta na legenda do slide
14. A linguagem visual do leque segue Grant Sanderson ("But what is a GPT?", 3Blue1Brown, 2024) e o FT Visual
Storytelling Team ("Generative AI exists because of the transformer", set/2023), como referência de estilo, sem dado
tirado deles.

## Mídia, créditos e custo

As seis imagens da tela são uma série de still-life em preto e branco gerada pelo Gemini (image-video-api) e tratada
nas cores do tema; prompt, parâmetros, tratamento e original de cada uma estão em `midia/creditos.json` e em
`midia/originais/` (fora do git). Toda imagem gerada leva o selo "imagem gerada por IA" no próprio slide. O vídeo da demonstração
saiu do `./cvm html` (código próprio, caso fictício) e não custou nada; a escrita da minuta, de 6,6 s em diante, e a
digitação do pedido, de 0 a 4,8 s, foram aceleradas 2x com ffmpeg, para o primeiro passo da demonstração caber em 3,5 s
e o último mergulho em 4,6 s. O vídeo ficou com 8,9 s; o original fica em `midia/originais/demo.mp4`.

| arquivo | gerador | custo estimado (US$) |
|---|---|---|
| `heroi-aula1.webp` | Gemini | 0,113 |
| `heroi-aula2.webp` | Gemini | 0,0504 |
| `doc-peticao.webp`, `doc-contrato.webp`, `doc-modelo.webp`, `pasta-aberta.webp` | Gemini | 0,0504 cada |
| `demo.mp4`, `demo-capa.webp` | código (`./cvm html`) | 0 |

No total foram 38 gerações únicas: 37 no Gemini, somando cerca de US$ 1,64, valor estimado pela tabela do plano e
ainda sem conferência com a fatura, e uma no GPT Image (sunburst), cujo preço segue sem fonte documentada; as entradas `.webp` do `creditos.json` repetem o custo do original e não somam de novo.

## Conferir antes do deck final

- Kalai, Nachum, Vempala e Zhang, "Why Language Models Hallucinate", arXiv:2509.04664: ler antes de falar de
  alucinação no slide data, porque o `regras.md` exige fonte ao tratar de risco. Mata v. Avianca (S.D.N.Y., 2023), se
  for citado.
- A lista do mercado em out/2026, com fonte e data, e a ressalva de que a OpenAI publicou pesos abertos (gpt-oss), o
  Google mantém o Gemma e modelos fechados também rodam em nuvens parceiras.
- A documentação oficial de Agent Skills: o arquivo SKILL.md, a pasta de referências e o caminho `.claude/skills/`.
- LegalBench (Guha et al., arXiv:2308.11462) e uma posição datada da LMArena (Chiang et al., arXiv:2403.04132), só se
  entrar número real em benchmark ou arena.
- A Montserrat, provisória enquanto a fonte do logo não for confirmada.
- Os preços de sunburst, FLUX e Ideogram, que não têm fonte documentada, o custo real do Omni pela CLI e o limite de
  taxa do Gemini no image-video-api.
- A licença do Remotion, se ele for usado.

## Pendências

- Aprovação ao vivo das manchetes, das imagens e da sequência de 14 slides.
- Abertura da Aula 2: escolher entre a pasta em duotone (atual, cinza-azulada) e `midia/originais/heroi-aula2-tri.webp` (tritone da
  mesma v6, pardo como a pasta do slide 10, sem custo de geração). Se o pardo brigar com o "SKILL" dourado, manter o
  duotone e só aumentar a pasta para uns 520 px de largura, com a borda direita antes dos traços do circuito.
- Roteiro completo de cada aula, com duração e o que a turma deve fazer no fim.
- Ensaio no equipamento do evento, com a luz da sala acesa (o projetor lava o marinho) e conferindo a fluidez.
- O vídeo de exemplo imita uma interface genérica de 19/10/2026; refazer se o fluxo real mudar antes da aula.
