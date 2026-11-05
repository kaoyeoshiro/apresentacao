# Dia 2 do curso de IA (Aulas 3 e 4): plano de montagem

> **Para quem executa:** siga tarefa por tarefa; os passos usam caixas (`- [ ]`). Os blocos de cada aula podem ir a
> subagentes em paralelo (Tarefas 5 e 6), cada um só com os próprios arquivos.

**Objetivo:** montar `decks/curso-ia-aula3` ("Fazer") e `decks/curso-ia-aula4` ("Decidir"), cerca de 90 minutos cada,
com as 11 atividades, o kit do Dia 2 e as reservas de contingência, prontos para ensaio e publicação no site.

**Arquitetura:** cada aula repete o molde da Aula 2. `montar.py` concatena `fonte/base.*` com os blocos
`fonte/<bloco>.{css,html,slides.js,cenas.js}` e gera `deck.html`; o motor (`motor/palco.js`, `motor/cenas.js`) e o tema
`cojuris` não mudam. Cada bloco é independente e se ensaia sozinho com `python3 montar.py <bloco>`.

**Ferramentas:** HTML, CSS e JS do motor de palco; Python 3 do `./ap` (`~/.venvs/apresentacao`); pytest para o script
do scraper; Chrome para `sondar` e `paradas`.

**Spec:** `docs/curso-ia-dia2.md`. Fontes: `docs/pesquisa/dia2-*.md` e a Parte V da apostila v2.

## Restrições globais

- Tema `cojuris`, plano contínuo, a mesma trilha dourada das Aulas 1 e 2; cor, fonte e logo só por `var()` do tema.
- Fato só de fonte lida e anotada no `briefing.md`; zero `[CONFERIR]` na tela; linha de confiança baixa nas fichas não
  vai à tela; confiança média só com a fonte nomeada no slide; número de OpenAI ou xAI só com a ressalva de vazamento.
- Animação é função do tempo: nada de `setTimeout`, `Date.now()`, `Math.random()` sem semente, CSS transition.
- Até 45 palavras visíveis por parada; texto nunca abaixo de 30 px; nada da internet em tempo de palco.
- Texto de tela e notas sob as normas de escrita do `~/.claude/CLAUDE.md` (sem travessão, sem "não é X, mas Y", sem
  dois-pontos de anúncio, sem frase-rótulo).
- Dados pessoais nunca; caso fictício no harness do quatilex; nenhum print com número de processo real.
- Imagem gerada só pelo `./ap imagens`, teto US$ 2,00 por execução; acima disso, sim do professor. Escolha de rascunho é
  dele.
- Repositório público do kit, merge e deploy no site são ações externas: cada um só com o sim do professor.
- Código do scraper: a solução mais simples que atende, com teste; nada de recurso especulativo.

## Mapa de arquivos

```
decks/curso-ia-aula3/
  briefing.md                 público, roteiro, fontes por slide, crítica
  montar.py                   cópia do da Aula 2 com BLOCOS próprios
  fonte/base.{cabeca.html,css,topo.js,meio.js,fim.js}   base (topo.js com os blocos da Aula 3)
  fonte/LEIA-ME.md            guia do bloco, adaptado do da Aula 2
  fonte/a-abertura.*  b-skills.*  c-mcp.*  d-scraper.*  e-github.*  f-rotinas.*   (6 blocos)
  midia/ (creditos.json, logos -> mesmo arranjo da Aula 2)
  material/kit.py             gera kit/ a partir de material/
  material/skill-defeituosa/SKILL.md     A1
  material/peticao-injecao.pdf + gerador  A3
  material/scraper/stj_espelhos.py, test_stj_espelhos.py, amostra/   etapa 2 e modo offline
  kit/                        saída do kit.py (vai ao repositório público)
decks/curso-ia-aula4/
  briefing.md, montar.py, fonte/base.*, fonte/LEIA-ME.md
  fonte/a-assistentes.*  b-harness.*  c-conta.*  d-geopolitica.*  e-futuro.*   (5 blocos)
  midia/
```

Blocos e minutos (somam 90 em cada aula):

| Aula 3 | min | Aula 4 | min |
|---|---|---|---|
| a-abertura (`abertura`) | 4 | a-assistentes (`assistentes`, inclui a abertura) | 27 |
| b-skills (`skills`, A1, A2) | 26 | b-harness (`harness`) | 6 |
| c-mcp (`mcp`, A3, A4) | 16 | c-conta (`conta`, A8) | 23 |
| d-scraper (`scraper`, A5) | 20 | d-geopolitica (`geopolitica`, A9) | 18 |
| e-github (`github`) | 7 | e-futuro (`futuro`, A10, A11, fecho) | 16 |
| f-rotinas (`rotinas`, A6, fecho) | 17 | | |

---

### Tarefa 1: Esqueleto das duas aulas

**Arquivos:** criar `decks/curso-ia-aula{3,4}/montar.py`, `fonte/base.*`, `fonte/LEIA-ME.md`, `midia/creditos.json`
e um quarteto vazio por bloco.

**Produz:** `python3 decks/curso-ia-aulaN/montar.py [bloco]`, ids de bloco da tabela acima.

- [ ] Copiar da Aula 2 `montar.py` e `fonte/base.*` para cada aula. Trocar `BLOCOS` pela lista de blocos da aula.
- [ ] Em `fonte/base.topo.js`, trocar a lista `blocos` pela da tabela (id, rótulo curto, minutos).
- [ ] Em `fonte/base.cabeca.html`, reescrever o comentário do topo e o `<title>`: "Fazer · Aula 3" e "Decidir · Aula 4".
- [ ] Ver como `decks/curso-ia-aula2/midia/logos` está ligado (pasta ou link) e repetir o arranjo; `creditos.json` só
  com as entradas de logo.
- [ ] Copiar `fonte/LEIA-ME.md` da Aula 2 trocando nome da aula, lista de blocos, prefixos de classe (`a-` a `f-`) e
  ids de bloco.
- [ ] Criar cada bloco com um slide provisório (um `respiro` com o nome do bloco), para o esqueleto montar e rodar.
- [ ] Verificar, para cada aula:

```bash
python3 decks/curso-ia-aula3/montar.py && ./ap lint decks/curso-ia-aula3 && ./ap sondar decks/curso-ia-aula3
```

Esperado: "lint: tudo certo" e "0 erro(s)". Repetir para a Aula 4.

- [ ] Commit: `Dia 2: esqueleto das Aulas 3 e 4 no molde da Aula 2`.

### Tarefa 2: Briefing e roteiro da Aula 3 (portão do professor)

**Arquivos:** `decks/curso-ia-aula3/briefing.md`.

**Consome:** spec, `docs/pesquisa/dia2-ferramentas-aula3.md`, `dia2-scraper-jurisprudencia.md`, apostila caps. 16 a 19.

- [ ] Ler `temas/cojuris/regras.md` e `.claude/skills/apresentacao/roteiro.md`.
- [ ] Escrever: público, ocasião, mensagem em uma frase ("a IA trabalha fora do chat quando você lhe dá o jeito, a
  tomada e a agenda, e você confere a fonte"), o que a sala faz no fim, tema, modo, prazo, dinâmica das atividades.
- [ ] Tabela do roteiro: slide id, bloco, manchete, o que a tela prova, clima (claro ou noite), densidade, arquétipo
  (`docs/cenas.md`), mídia e custo, fonte da afirmação. Cerca de 50 a 60 slides, como a Aula 2. Cada atividade
  (A1 a A6) tem slide com enunciado e `pratica: N`.
- [ ] Textos exatos dos pedidos de demonstração (skill de Word, Claude for Word, MCP do Microsoft Learn, plugin Legal,
  scraper etapas 1 e 2, rotina agendada), para copiar da tela.
- [ ] Notas por slide `{diga, faca, transicao}` em rascunho curto.
- [ ] Conferir a lista do fim de `roteiro.md`; nenhuma linha acima de 45 palavras.
- [ ] Mostrar o roteiro ao professor e esperar o sim (é texto que o público vê). Mudanças voltam a este passo.
- [ ] Commit: `Aula 3: briefing e roteiro aprovados`.

### Tarefa 3: Briefing e roteiro da Aula 4 (portão do professor)

**Arquivos:** `decks/curso-ia-aula4/briefing.md`.

**Consome:** spec, `dia2-economia-subsidio-bolha.md`, `dia2-geopolitica-ia.md`, apostila cap. 22 e conclusão,
`/Volumes/Projetos/Automacao_Agent` (quatilex; só leitura).

- [ ] Ler `ARCHITECTURE.md`, `AGENTS.md` e `docs/` do quatilex e confirmar, para os 10 agentes de
  `docs/pesquisa/dia2-harness-quatilex.md`, o papel de cada um e a ordem real do fluxo (quem roda em paralelo). Anotar
  na ficha, com o arquivo do quatilex que sustenta cada linha. Nada de dado de processo.
- [ ] Mesmo conteúdo da Tarefa 2 adaptado: mensagem em uma frase ("delegar é decidir o que a máquina alcança e quanto
  você depende de quem a vende"), roteiro, fontes por slide, enunciados de A7 a A11, notas em rascunho.
- [ ] Bloco "Quem paga a conta" com a tese decidida: o uso já se paga, a corrida não. Cada número com a linha da ficha
  ao lado; OpenAI e xAI com a ressalva de origem.
- [ ] *A próxima onda* fica fora, salvo se o professor trouxer a edição com páginas antes desta tarefa.
- [ ] Mostrar o roteiro ao professor e esperar o sim.
- [ ] Commit: `Aula 4: briefing e roteiro aprovados`.

### Tarefa 4: Material e kit do Dia 2

**Arquivos:** `decks/curso-ia-aula3/material/**`, `decks/curso-ia-aula3/kit/**`.

**Produz:** `material/scraper/stj_espelhos.py` com `mais_recente(recursos) -> dict`, `filtrar(registros, termo,
campos) -> list[dict]`, `main(argv)` com `--tema`, `--turma`, `--offline ARQUIVO`, `--saida CSV`.

- [ ] Baixar uma única vez o pacote da Primeira Turma e salvar a amostra para o modo offline e para os testes:

```bash
mkdir -p decks/curso-ia-aula3/material/scraper/amostra && cd decks/curso-ia-aula3/material/scraper/amostra
curl -s 'https://dadosabertos.web.stj.jus.br/api/3/action/package_show?id=espelhos-de-acordaos-primeira-turma' -o pacote.json
python3 -c "import json;r=json.load(open('pacote.json'))['result']['resources'];print([(x['name'],x['url'],x.get('last_modified')) for x in r][-3:])"
```

Baixar o JSON mais recente listado e o dicionário de dados CSV; anotar no briefing os nomes reais dos campos de ementa,
relator, órgão, data e processo (o script usa esses nomes, não suposições).

- [ ] Escrever o teste antes (`test_stj_espelhos.py`):

```python
import json, pathlib
from stj_espelhos import mais_recente, filtrar

AMOSTRA = pathlib.Path(__file__).parent / "amostra"

def test_mais_recente_escolhe_o_json_de_data_maior():
    recursos = [{"name": "20260831.json", "format": "JSON", "url": "a"},
                {"name": "dicionario.csv", "format": "CSV", "url": "b"},
                {"name": "20260930.json", "format": "JSON", "url": "c"}]
    assert mais_recente(recursos)["url"] == "c"

def test_filtrar_acha_o_termo_sem_acento_e_sem_caixa():
    regs = [{"ementa": "FORNECIMENTO DE MEDICAMENTO. Saúde."}, {"ementa": "Tributário."}]
    assert len(filtrar(regs, "medicamento", ["ementa"])) == 1
    assert len(filtrar(regs, "saude", ["ementa"])) == 1

def test_amostra_real_tem_os_campos_usados():
    arq = next(AMOSTRA.glob("2026*.json"))
    regs = json.loads(arq.read_text(encoding="utf-8"))
    from stj_espelhos import CAMPOS
    assert all(c in regs[0] for c in CAMPOS)
```

- [ ] Rodar `~/.venvs/apresentacao/bin/python -m pytest decks/curso-ia-aula3/material/scraper -q`; esperado: falha
  por módulo inexistente.
- [ ] Implementar `stj_espelhos.py` no mínimo que passa: `requests` à API CKAN, `mais_recente` pelo maior nome
  `AAAAMMDD.json`, `filtrar` com `unicodedata` para tirar acento, `CAMPOS` com os nomes anotados, CSV pela biblioteca
  padrão, uma requisição por vez, `User-Agent` honesto ("curso co.juris, demonstração em sala"), `--offline` lendo o
  arquivo local sem rede.
- [ ] Rodar os testes; esperado: 3 passed. Rodar uma vez online e uma offline com `--tema medicamento` e conferir que o
  CSV abre e tem linhas.
- [ ] Gravar a página de resultado do TJMS (busca "fornecimento de medicamento", origem `T`) em `amostra/tjms.html`,
  como reserva da etapa 1. Uma requisição só.
- [ ] `material/skill-defeituosa/SKILL.md` (A1), fictícia, com exatamente três defeitos: descrição que dispara em
  qualquer pedido; script que envia o conteúdo da pasta a um endereço externo inventado e inerte (`exemplo.invalid`);
  instrução para ignorar a confirmação do usuário. Cabeçalho avisando que é material de treino e não deve ser instalada.
- [ ] `material/peticao-injecao/` (A3): gerador de PDF de uma petição fictícia com uma ordem escondida em texto branco
  e em rodapé de corpo minúsculo, no padrão de `decks/curso-ia-aula2/material/casos_gerar/`.
- [ ] Modelo timbrado: reaproveitar o do escritório fictício Dias & Moura (`decks/curso-ia-aula2/material/escritorio/`).
- [ ] `material/kit.py`, no padrão de `decks/curso-ia-aula2/material/kit.py`, gerando `kit/` com README em português
  (o que é cada coisa, como refazer cada demonstração no Claude, no ChatGPT e no Gemini, marcado equivalente, exige
  adaptação ou não disponível, pela ficha `dia2-ferramentas-aula3.md`).
- [ ] Commit: `Dia 2: kit, skill de treino, petição com injeção e scraper do STJ com teste`.

### Tarefa 5: Blocos da Aula 3 (paralelizável, um subagente por bloco)

**Arquivos por bloco:** só `decks/curso-ia-aula3/fonte/<bloco>.{css,html,slides.js,cenas.js}`.

**Consome:** roteiro aprovado da Tarefa 2; `fonte/LEIA-ME.md`; exemplos vivos de cenas próprias em
`decks/curso-ia-aula1/deck.html` e `decks/curso-ia-aula2/fonte/`.

- [ ] Montar primeiro, pelo próprio coordenador, a abertura, o slide mais denso de `d-scraper` e um slide com dado;
  rodar `sondar` e `paradas` neles e acertar o sistema visual antes de despachar o resto.
- [ ] Despachar os outros blocos a subagentes Opus (front-end), um bloco por subagente, com o `LEIA-ME.md` como
  briefing e a lista de slides do roteiro daquele bloco. Telas de app (menu `/`, conector, marketplace, tarefa
  agendada, terminal do Claude Code) desenhadas por código, sem print.
- [ ] Conferir cada retorno: `python3 decks/curso-ia-aula3/montar.py <bloco>`, `./ap sondar decks/_p-<bloco>` sem ERRO,
  e abrir a folha de contato.
- [ ] Montar o deck inteiro e verificar:

```bash
python3 decks/curso-ia-aula3/montar.py && ./ap lint decks/curso-ia-aula3 && ./ap sondar decks/curso-ia-aula3
grep -o "titulo: '[^']*'" decks/curso-ia-aula3/deck.html
```

Esperado: lint e sondar limpos, e a lista de títulos igual à do roteiro, na ordem.

- [ ] Commit: `Aula 3: blocos montados`.

### Tarefa 6: Blocos da Aula 4 (paralelizável)

Igual à Tarefa 5, com `decks/curso-ia-aula4` e os blocos dela. O bloco `b-harness` usa o arquétipo `demonstracao`
com o vídeo da Tarefa 6A, seguido de um slide com o dado (US$ 1,59 a peça, 87% no redator) que faz a ponte para
"Quem paga a conta". Verificação idêntica, trocando o número da aula. Commit: `Aula 4: blocos montados`.

### Tarefa 6A: Animação do harness no claude_video_maker

**Repositório:** `/Volumes/Projetos/claude_video_maker`, seguindo o `CLAUDE.md` e a skill `video-maker` de lá. O `main`
dele tem alterações de outra sessão ainda não salvas: trabalhar num worktree com branch próprio, sem tocar nelas.

**Consome:** `docs/pesquisa/dia2-harness-quatilex.md` (dados e ordem confirmada na Tarefa 3) e o vídeo anterior
`videos/agentes-peca/` (motor `engines/html`, `comp.html`, `sistema.json`, briefing de 07/10/2026).

**Produz:** `videos/agentes-peca-2/output/final.mp4`, 16:9, sem narração, cerca de 40 s.

- [ ] Criar `videos/agentes-peca-2/` a partir de `agentes-peca/`: `briefing.md` com a nova fonte (print de 05/11/2026,
  copiado para a pasta) e as presunções; `sistema.json` com as cores dos dois agentes novos.
- [ ] Ajustar `comp.html` para os 10 agentes e 6 modelos, na ordem confirmada: dois bichinhos novos (`mm_agrupador`, em
  Claude Haiku, e `afirmacao_oficio`), no mesmo traço e humor dos atuais (acordam, trabalham, colam a contribuição na
  folha). O redator ganha uma piada visual de ser o mais caro (o contador de custo dispara quando ele trabalha). Fecho:
  "10 agentes, 6 modelos" e "US$ 1,59 esta peça".
- [ ] `./cvm html videos/agentes-peca-2/comp.html --verificar 1,8,15,22,30,38` (quadro é função do tempo) e stills;
  abrir os stills e corrigir texto cortado, sobreposição e personagem escondido.
- [ ] Render final, `./cvm check`, e mostrar ao professor o vídeo; mudanças voltam ao `comp.html`.
- [ ] Commit no branch do claude_video_maker; trazer para a Aula 4 com `./ap trazer` (contrato em `docs/palco.md`,
  seção Mídia) e registrar o crédito em `midia/creditos.json`.

### Tarefa 7: Imagens das duas aulas (portão de custo e de escolha)

- [ ] Escrever `imagens.toml` de cada aula pela série do tema (`temas/cojuris/imagem/`): só onde a imagem prova algo
  (capa de cada aula e um herói por bloco, no máximo seis por aula).
- [ ] `./ap imagens decks/curso-ia-aula3` e `aula4` sem gastar, para ver o custo. Se a soma passar de US$ 2,00 por
  execução, pedir o sim do professor antes.
- [ ] `--rascunhos -n 3`, mostrar `storyboard/candidatos.png` ao professor, gerar `--final` com a escolha dele.
- [ ] `./ap midia conferir` com "0 erro(s)"; `.selo-ia` em todo slide com imagem gerada.
- [ ] Commit: `Dia 2: imagens das Aulas 3 e 4`.

### Tarefa 8: Crítica, três rodadas por aula

- [ ] Por aula: `./ap sondar` e `./ap paradas --viagens`, uma de cada vez; despachar um subagente Opus com o prompt
  pronto de `.claude/skills/apresentacao/critica.md`; corrigir os três maiores defeitos; registrar a rodada na seção
  "Crítica" do briefing (defeito, evidência, correção).
- [ ] Passa quando há três rodadas e a última não acha defeito alto ou médio; `sondar` sem ERRO; cada AVISO corrigido,
  isento com motivo ou justificado.
- [ ] Commit por rodada: `Aula N: crítica, rodada K`.

### Tarefa 9: Ensaio com o professor e reservas gravadas

- [ ] `./ap abrir decks/curso-ia-aula3` e depois `aula4`; o professor passa cada deck pelo passador com a tela do
  apresentador (P) e diz o que muda. Pedido de mudança volta à Tarefa 5, 6 ou 7 e a uma rodada da Tarefa 8.
- [ ] O professor ensaia na própria conta os cinco itens do spec (timbre no `.docx`, remover plugin, tarefa agendada com
  o app fechado, Chrome e uso do computador visíveis, MCP do Microsoft Learn) e grava as demonstrações de reserva.
  As gravações entram em `midia/` pelo `./ap trazer` ou como vídeo local no slide da demonstração.
- [ ] Passa quando o professor aprova cada deck ao vivo.

### Tarefa 10: Entrega, PR, kit público e site

- [ ] `./ap empacotar decks/curso-ia-aula3` e `aula4`; esperado "pacote: ok, abre sem internet".
- [ ] `./ap teste` inteiro e os testes do scraper; colar a última linha no texto do PR.
- [ ] Autorrevisão do diff por subagente Opus ("liste só o que bloquearia o merge"), corrigir e repetir até vazio.
- [ ] Pedir o sim do professor para: criar o repositório público do kit (`kit-dia2-curso-ia`), juntar o PR e publicar.
- [ ] Com o sim: `gh repo create` do kit e push de `kit/`; `gh pr merge --squash --delete-branch`;
  `./ap publicar decks/curso-ia-aula3 --site <site> --pasta aula-3 ...` e o mesmo para a Aula 4; commit e
  `npm run deploy` no site; abrir as duas páginas publicadas e conferir.
- [ ] Limpeza: remover worktrees e branches da tarefa e rodar `python3 ~/.config/agent-hooks/git_cleanup.py --apply`.

## Portões do professor, em ordem

1. Roteiro da Aula 3 (Tarefa 2) e da Aula 4 (Tarefa 3).
2. Animação do harness (Tarefa 6A) e custo e escolha das imagens (Tarefa 7).
3. Ensaio ao vivo e gravações de reserva (Tarefa 9).
4. Repositório público do kit, merge e publicação (Tarefa 10).
