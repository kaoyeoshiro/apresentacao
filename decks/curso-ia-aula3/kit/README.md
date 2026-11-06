# Kit do Dia 2 (Aulas 3 e 4): do arquivo ao mundo e quem decide

Material para refazer em casa as demonstrações da Aula 3 e as atividades da Aula 4 do curso de IA da co.juris (Dia 2). O escritório Dias & Moura,
a petição e a skill são fictícios. As informações sobre cada ferramenta foram conferidas nas páginas oficiais em
05/11/2026; menus e planos mudam, então confira a tela no dia em que for usar.

## O que tem aqui

- `skill-defeituosa/SKILL.md`: skill fictícia com três defeitos, para a auditoria da Atividade 1. **Não instale.** Ela
  traz um aviso no topo e usa o domínio `exemplo.invalid`, que não existe na internet.
- `peticao/peticao-injecao.pdf`: petição fictícia com uma ordem escondida para o agente de IA (Atividade 3).
- `escritorio/`: o modelo timbrado em Word (`modelo-timbrado.docx`), o logo e o padrão de documentos do escritório.
- `scraper/`: o script `stj_espelhos.py`, que monta um boletim de acórdãos do STJ por tema em planilha (CSV), e a pasta
  `amostra/` com o arquivo de setembro de 2026 da Primeira Turma e o dicionário de dados, para usar sem internet.
- `gabarito/atividades.md`: as respostas das Atividades 1 e 3. Só abra depois de tentar.
- `aula4/`: as fichas em branco das Atividades 7 (acesso mínimo) e 10 (plano de 30 dias) e o gabarito das
  Atividades 7, 8 e 9. A Aula 4 não tem arquivo para abrir; as fichas servem para refazer as atividades em casa.

## Como baixar

Na página do repositório, botão verde **Code** > **Download ZIP**, e extraia a pasta. O ZIP traz os arquivos, sem o
histórico de versões.

## Como refazer cada demonstração

Em cada demonstração, a marca diz como fica no ChatGPT e no Gemini em comparação com o Claude: **equivalente**,
**exige adaptação** ou **não disponível**. Onde a pesquisa da aula não achou página oficial que responda, está escrito
"não conferido".

### 1. Parecer em Word no modelo timbrado

No Claude, confirme em Settings > Capabilities que "Create and edit files" (ou "Code execution and file creation") está
ligado. Envie `escritorio/modelo-timbrado.docx` e peça o parecer dentro do modelo, seguindo
`escritorio/padrao-do-escritorio.md`. A skill de Word funciona em todos os planos, inclusive o gratuito; confira o
resultado página por página. O Claude for Word, suplemento que roda dentro do Word, exige plano Pro, Max, Team ou
Enterprise e não roda no Word 2016 ou 2019 de licença perpétua.

- ChatGPT: não conferido.
- Gemini: não conferido.

### 2. Conector MCP (a "tomada")

No Claude, Customize > Connectors > "+ Add" > "Add custom connector", com a URL `https://learn.microsoft.com/api/mcp`
(servidor da Microsoft com documentação pública, sem login e sem custo). Faça uma pergunta sobre o Word e veja a
resposta vir da documentação oficial. No plano gratuito, ele ocupa a única vaga de conector personalizado; para
liberar a vaga, desconecte em Customize > Connectors.

- ChatGPT: **exige adaptação**. Na versão web, MCP só entra por plugin; no aplicativo de desktop, Settings > MCP servers >
  Add server > Streamable HTTP > Save, e reinicie o aplicativo.
- Gemini: **não disponível** no Brasil. Os aplicativos personalizados por MCP exigem morar nos EUA, ter 18 anos e usar
  o Gemini em inglês.

### 3. Plugin jurídico (o "pacote")

No Claude, Customize > Plugins > "Add" > "Add marketplace", escolha o Legal, instale um plugin e veja a entrevista
inicial. Plugins exigem plano pago (Pro, Max, Ultra, Team ou Enterprise). Os plugins jurídicos seguem o direito dos
EUA e entregam rascunho para revisão de advogado. A página de ajuda explica como remover o marketplace inteiro (menu
no canto do marketplace > "Remove"); no Claude Code, o comando é `/plugin uninstall <plugin>`.

- ChatGPT: **exige adaptação**. Há aba de plugins (abrir o plugin > "+" para instalar, "Uninstall plugin" para tirar),
  mas a página oficial não lista plugin nem categoria jurídica.
- Gemini: não conferido.

### 4. Boletim de jurisprudência do STJ

O script `scraper/stj_espelhos.py` não depende de IA nem de biblioteca extra: precisa só do Python 3 instalado no
computador. Abra o terminal na pasta `scraper` e rode:

```
python3 stj_espelhos.py --tema "execução fiscal"
python3 stj_espelhos.py --tema saude --offline amostra/20260930.json
```

O primeiro comando pede ao Portal de Dados Abertos do STJ o arquivo mais recente dos "Espelhos de acórdãos" da Primeira
Turma (licença Creative Commons Atribuição) e grava `boletim.csv`, que abre no Excel. O segundo faz o mesmo sem
internet, com a amostra de setembro de 2026. Para outro conjunto do portal, use `--turma`; para outro nome de
arquivo, `--saida`. Pesquise por tema, nunca por pessoa (Resolução CNJ 121/2010, art. 5º), e confira cada acórdão na
fonte antes de citá-lo.

Para ver o agente escrever o script, peça ao Claude Code, numa pasta vazia, um script em Python que baixe o JSON mais
recente desse conjunto, filtre a ementa por um tema e grave um CSV.

- ChatGPT: **exige adaptação**. Use o Codex ou o ChatGPT no aplicativo de desktop, que trabalham em pasta do
  computador; a versão web não trabalha em pasta local.
- Gemini: não conferido.

A etapa 1 da aula, a consulta ao e-SAJ do TJMS pelo navegador, usa o Claude in Chrome, extensão do Chrome para planos
pagos que não funciona em outros navegadores nem no celular.

- ChatGPT: **exige adaptação**. O Computer Use roda no aplicativo de desktop "in supported regions", e a página não diz
  se o Brasil está entre elas.
- Gemini: **não disponível** no Brasil. A navegação automática no Chrome exige morar nos EUA e usar o aparelho em inglês.

### 5. GitHub

Não depende de IA, e o caminho é o mesmo para todos. Abra `github.com/anthropics/claude-for-legal`, leia o README, veja
**Code** > **Download ZIP** e as abas Issues (lista de tarefas e discussões do projeto) e Pull requests (propostas de
mudança). Para levar uma skill do GitHub ao Claude, baixe o ZIP, separe a pasta da skill, compacte só ela e envie em
Customize > Skills > "+" > "+ Create skill" > "Upload a skill".

### 6. Rotina agendada

No Claude, Scheduled > New task ("Create with Claude" ou "Set up manually"), com frequência diária ou semanal. Exige
plano pago. A tarefa roda na nuvem mesmo com o computador dormindo ou o aplicativo fechado, salvo quando precisa de
arquivo ou aplicativo do seu computador.

- ChatGPT: **equivalente**, com limites por plano. São até 3 tarefas ativas no gratuito, rodando no máximo uma vez por
  dia em janela flexível, e 5 no Plus; nos planos pagos, até de hora em hora e com horário exato.
- Gemini: **equivalente** para o agendamento nas conversas (até 10 ativos, com o Keep Activity ligado, no menu
  "Scheduled"). As páginas do ChatGPT e do Gemini não dizem se a tarefa roda com o aparelho desligado.

## As atividades em casa

**Atividade 1.** Abra `skill-defeituosa/SKILL.md` num editor de texto, sem instalar, e procure três defeitos: quando a
skill dispara, o que o comando faz com os seus arquivos e o que ela manda o agente fazer sem perguntar. Depois peça a um
assistente de IA que audite o arquivo e compare com o que você achou.

**Atividade 3.** Abra `peticao/peticao-injecao.pdf` e procure a ordem escondida antes de entregar o arquivo a um agente
(dica: selecione todo o texto). Depois peça a um assistente que resuma a petição e veja se ele obedece à ordem, avisa
dela ou a ignora.

O gabarito está em `gabarito/atividades.md`. As atividades da Aula 4 estão em `aula4/`.
