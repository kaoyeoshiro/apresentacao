# apresentacao

Apresentações ao vivo de alta qualidade feitas por código, para projetar com passador de slides. O Claude é
diretor de arte, roteirista, programador e revisor; o deck é um HTML em que cada quadro é função do tempo, com uma
parada por clique. Para qualquer pedido de apresentação, siga a skill `.claude/skills/apresentacao/SKILL.md`.

## Mapa

- `motor/`: `palco.js` (tocador ao vivo, tela do apresentador, modo render, oráculo no navegador), `tempo.js`
  (curvas, mola, aleatório com semente), `camera.js` (plano contínuo). Contrato em `docs/palco.md`.
- `motor/cenas.js` e `motor/cenas.css`: a biblioteca do plano contínuo (mundo, trilha dourada, zonas noite, viagens
  e os 11 arquétipos de slide). Contrato em `docs/cenas.md`.
- `temas/`: um design system por pasta (`noite`, `cojuris`, `pge`, `_modelo`), com `imagem/` para a série de imagens
  geradas. Contrato em `docs/temas.md`.
- `decks/<slug>/`: uma apresentação por pasta (`deck.html`, `briefing.md`, `imagens.toml`, `midia/` com
  `creditos.json`). Moldes: `decks/catalogo/` (plano contínuo, um slide por arquétipo) e `decks/demo/` (slides com
  transições). `decks/previa-curso-ia/` é a régua de qualidade.
- `ferramentas/`: CLIs Python, sempre chamadas por `./ap`.
- `docs/decisao.md`: por que motor próprio e não Slidev ou reveal.js; `docs/pesquisa/`: os relatórios de origem.

## Comandos

```bash
./ap sync                                   # instala o ambiente Python (fora do disco externo)
./ap novo <slug> --tema noite|cojuris|pge [--modo continuo|slides]  # deck novo do catálogo (padrão) ou da demonstração
./ap abrir decks/<slug>                     # ao vivo no Chrome (→ ← B F G P ?)
./ap sondar decks/<slug>                    # oráculo de legibilidade e ritmo em cada parada; sai 1 se houver ERRO
./ap paradas decks/<slug> [--viagens]       # um still por parada e a folha de contato; --viagens: quadros no meio de cada viagem (viagens.png)
./ap lint decks/<slug> | motor/cenas.css    # regras do deck; recusa cor literal na folha do motor (só var() do tema)
./ap imagens decks/<slug> [--rascunhos|--final|--tratar]   # imagens da série do tema: situação, rascunhos, final tratado
./ap pdf | video | empacotar decks/<slug>   # PDF, MP4, pasta que abre sem internet
./ap imagem | video-ia | trazer | midia conferir ...   # matéria-prima avulsa e vídeo (docs/palco.md, seção Mídia)
./ap teste                                  # todos os testes
```

## Regras fixas

- Não inventar fatos, números, nomes, leis ou datas. Cada dado vem de fonte lida na sessão e fica anotado no
  `briefing.md` do deck; o que não foi confirmado leva `[CONFERIR]` na tela.
- Dados pessoais nunca aparecem na tela. Captura de sistema real é feita no claude_video_maker, com máscara.
- Chaves de API nunca entram neste repositório. As de imagem e vídeo ficam nos projetos vizinhos (image-video-api
  e claude_video_maker), que as pontes chamam.
- Clipe do Gemini Omni custa dinheiro: `./ap video-ia` só gera com `--aprovado HASH`, e isso exige um "sim" do
  usuário na conversa para aquele clipe e aquele custo.
- Imagem gerada sai do `./ap imagens`, que recusa a execução acima de `--teto` (US$ 2,00); subir o teto exige o sim
  do usuário na conversa para aquele custo, e quem escolhe entre os rascunhos é ele.
- Cor, fonte e logo só vêm do tema. Logo é recorte do arquivo oficial, nunca redesenhado nem gerado por IA.
- Animação é função do tempo: nada de `setTimeout`, `Date.now()`, `Math.random()` sem semente ou CSS transition.
- Nada da internet em tempo de palco: fontes, vídeos e imagens locais; `./ap empacotar` confere com a rede bloqueada.
- O onetake (PolyForm Noncommercial) inspirou ideias; não copie código nem texto dele.
- O repositório antigo `/Volumes/Projetos/apresentacoes` está parado e foi absorvido: não editar lá.

## Armadilhas conhecidas

- O disco externo (exFAT) cria arquivos `._*`: o ambiente Python fica em `~/.venvs/apresentacao` (o `./ap` já
  cuida disso) e código que lista pastas deve ignorar nomes começando com `._`.
- Título com entrelinha justa e fonte alta (Montserrat) ultrapassa a própria caixa sem transbordar; o oráculo
  desconta essa folga, mas `overflow: hidden` em volta do título ainda pode cortar acento de maiúscula. Olhe os
  stills.
- O claude_video_maker é a pasta vizinha; outro lugar, defina `CVM_PROJETO`.
