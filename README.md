# apresentacao

Apresentações ao vivo feitas por código, para projetar com passador de slides. Cada deck é um arquivo HTML em que
cada clique toca um trecho animado até a parada seguinte. O mesmo arquivo vira a apresentação ao vivo, com tela do
apresentador, um PDF de contingência, um vídeo MP4 e os stills de revisão, e um oráculo mede a legibilidade de
cada parada antes de a plateia ver.

Imagens geradas por GPT Image ou Gemini e clipes do Gemini Omni chegam pelos projetos vizinhos (image-video-api e
claude_video_maker), com o crédito de cada arquivo registrado no deck. Cor, fonte e logo vêm de um tema por marca.

## Começar

```bash
./ap sync
./ap novo minha-palestra --tema noite
./ap abrir decks/minha-palestra
```

No palco: seta, espaço ou o passador avançam; ← volta; F tela cheia; P tela do apresentador; B tela preta; G índice.
Para levar ao evento, `./ap empacotar decks/minha-palestra` gera uma pasta que abre com dois cliques no Chrome, sem
internet, com o PDF de emergência dentro.

Documentação: `docs/palco.md` (motor e ferramentas), `docs/temas.md` (temas), `docs/decisao.md` (por que este
desenho), `.claude/skills/apresentacao/SKILL.md` (como o Claude produz um deck).
