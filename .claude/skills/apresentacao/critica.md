# Crítica

O oráculo (`./ap sondar`) mede legibilidade e ritmo, e não vê beleza, causalidade nem continuidade. Esses defeitos só
aparecem olhando os stills e os quadros de dentro das viagens, e foi assim que a prévia chegou ao nível aprovado: três
rodadas de crítica, cada uma com os piores defeitos nomeados e os três maiores corrigidos.

## Procedimento de cada rodada

São pelo menos três rodadas, e a crítica só termina quando a última não acha defeito de gravidade alta ou média.

1. `./ap sondar decks/<slug>` até não sobrar ERRO. Cada AVISO é uma pergunta de direção de arte (o slide tem um
   elemento dominante? algum slide muda de escala? três vizinhos parecem a mesma tela?); responda corrigindo, ou
   declare a exceção no HTML com o motivo (`data-contraste-ok`, `data-ritmo-ok`, `ritmoOk`) ou no briefing.
2. `./ap paradas decks/<slug> --viagens`, que grava em `decks/<slug>/storyboard/` um still por parada, a folha de
   contato e os quadros a 35% e 70% de cada viagem e logo depois do pouso.
3. Abra com a ferramenta Read, nesta ordem: `folha.png` (o deck visto do fundo da sala, onde se julga ritmo, partitura
   e hierarquia), cada `parada-NN-<id>.png` em tamanho cheio e `viagens.png`. Onde um quadro de viagem parecer errado,
   abra o `viagem-NN-<id>-<35|70|pouso>.png` inteiro.
4. Responda a rubrica abaixo, slide por slide, e confira a lista "Defeitos que já apareceram".
5. Nomeie os piores defeitos com gravidade, slide, evidência (arquivo e região do quadro) e correção concreta. Corrija
   os três maiores, rode `./ap sondar` de novo e confira nos quadros que a correção pegou.
6. Registre a rodada na seção "Crítica" do `briefing.md`: uma tabela com gravidade, slide, defeito e evidência, e
   correção feita ou motivo para não fazer.

Gravidade alta é o que quebra a leitura ou a verdade: texto ilegível do fundo da sala, dado errado ou sem marca,
quadro vazio ou borda dura na viagem do momento principal, S.T.A.R. que não se vê. Média é o que enfraquece: dourado
em várias coisas, slide sem elemento dominante, terceiro tom de luz, destaque que acende antes da causa, texto sobre
texto. Baixa é acabamento: quebra de linha, alinhamento de poucos pixels. Mudança de texto que o público vê volta ao
usuário antes de entrar.

## Rubrica

Cada pergunta tem resposta sim ou não, olhando o arquivo indicado.

Deck inteiro, na `folha.png`:

1. A abertura cria tensão (pergunta, problema, contraste), e o fecho diz o que a plateia faz agora?
2. Cada bloco tem um S.T.A.R. visível, e o resto está quieto?
3. O escuro marca capítulos e momentos fortes, sem três vizinhos com o mesmo clima e a mesma densidade?
4. Algum par de vizinhos repete o arquétipo ou o mesmo desenho de tela?
5. Metade dos slides ou mais tem imagem, número, diagrama ou vídeo dominando a tela?
6. A folha deixa de parecer uma página só (mesmo fundo, título sempre no mesmo canto, nada grande)?
7. Algum slide é só texto?

Cada parada, no still em tamanho cheio:

8. Lê-se em três segundos na folha, onde o still tem um quarto do tamanho?
9. Há um elemento dominante, entre 110 e 320 px, pelo menos uma vez e meia maior que o resto?
10. A manchete afirma e cabe numa linha?
11. O dourado aponta uma coisa só (além da trilha)?
12. O ilustrativo tem pílula, o não confirmado tem `[CONFERIR]`, e a imagem gerada tem selo?
13. Há texto sobre texto, legenda sobre elemento, peça encostando na trilha ou na margem?
14. Alguma linha quebra mal (palavra sozinha, parêntese partido, data separada do dia)?
15. A imagem conversa com a série (mesma luz, mesmas cores do tema) e o objeto recortado se separa do fundo?

Cada viagem, em `viagens.png` e nos quadros inteiros:

16. A 35% e a 70% há algo além de papel vazio ou de um slide ainda em branco?
17. A foto entra sem borda dura, sem retângulo sobre a zona noite?
18. Algum objeto some, pisca ou encolhe antes de chegar ao destino?
19. A luz pisca (claro, escuro, claro em poucos segundos), ou surge um terceiro tom, como o cinza-ardósia de um
    holofote sobre interface clara?
20. O destaque acende depois da causa (o fio chega e então a data acende; o papel pousa e então o nome acende)?
21. A trilha continua: nenhum traço some, e os traços da abertura descem até ela?

Movimento e tempo, no sondar e ao vivo:

22. Alguma animação existe só para enfeitar?
23. Algum passo passa de 3,5 s com a sala esperando, sem vídeo que justifique?

## Defeitos que já apareceram

Todos vieram das rodadas de crítica da prévia e da biblioteca. A biblioteca já evita os marcados com (b) nos
arquétipos; numa cena própria, ou com mídia nova, eles voltam.

| defeito | onde se vê | conserto que funcionou |
|---|---|---|
| borda dura de foto na viagem: a heroica aparece como retângulo sobre a zona noite (b) | quadros 35% e 70% saindo de uma abertura | véu com cada degradê começando em tinta cheia; foto pequena vai como `.heroi.recorte`, com as bordas dissolvidas |
| papel branco sumindo no claro: o recorte vira fantasma, sem elemento dominante (b) | folha, slides de objetos | tratamento do papel objeto (gama 1,8, papel uns 8 pontos de L* abaixo do fundo) e sombra dupla |
| foto fora da série: oliva em vez do azul da paleta, objeto da abertura diferente do mesmo objeto no conteúdo | folha, abertura ao lado do slide do objeto | mesmo tratamento por papel; ref de objeto para ser o mesmo objeto |
| holofote acinzentando a tela: terceiro tom ardósia, clarão branco no mergulho, luz bombeando (b) | mergulhos e a viagem que sai do último | holofote quase cheio, que escurece junto com o zoom e só sai quando a câmera deixa o vídeo; trocar furos sem apagar |
| costura no mergulho: a câmera mostra o mundo ao lado do vídeo | still do mergulho, borda esquerda | enquadramento e furos dentro do quadro do vídeo |
| dourado em várias coisas: dez marcas, cinco marcas, dois dourados que se chocam | stills de número, fios, abertura | um dourado por parada; o resto em tinta ou neutro |
| causalidade invertida: a resposta acende antes de o fio chegar; o nome acende antes de o papel pousar | quadros do pouso | acender por tempo, depois da chegada |
| objeto que encolhe cedo no voo e chega como ponto branco (b) | quadros 35% e 70% da viagem | voo em dois tempos: atravessa grande e só encolhe no último terço |
| legenda por cima do que entra: a legenda de um mergulho fica sobre o cartão seguinte (b) | quadro do pouso do mergulho seguinte | a legenda sai antes de o próximo recorte acender |
| quebra de linha ruim: "(caso" numa linha e "fictício)." na outra | still | `<span style="white-space: nowrap">` no trecho |
| slide que parece wireframe: molduras vazias, barras-esqueleto finas | folha | tirar a moldura, linhas grossas o bastante para ler como texto, etiqueta que diz o que é |
| peças sem explicação: papéis estacionados sem rótulo, selo rotulando a coisa errada | still | etiqueta curta ("deste caso"); selo junto da imagem gerada |
| dado que desmente a tese: candidata do leque igual à data verdadeira | roteiro e stills de slides diferentes | trocar o dado ilustrativo e anotar no briefing que não coincide |
| termo que a tela não apresentou ("pesos abertos") | legenda | dizer na língua do slide |
| passo longo com a sala esperando: digitação lenta no vídeo | AVISO de ritmo | acelerar o trecho do vídeo e declarar `ritmoOk` com motivo |
| pílula e selo no mesmo canto, um sobre o outro (b) | AVISO de sobreposição | o selo vai à esquerda da pílula |
| ilustrativo sem marca: a pílula sumiu numa revisão | still e briefing | pílula de volta, entrando por último |
| heroica cobrindo os traços do circuito | still da abertura | foto menor (`.heroi.recorte`) à esquerda dos traços |
| fio dourado riscando o texto da linha (b) | still de fios | marca no começo da linha, porque o fio chega pela esquerda |
| quadro vazio na viagem longa: a câmera pousa num slide que ainda não começou (b) | quadros 70% e pouso | conteúdo começa antes do pouso (`conteudo(c)` da biblioteca) |

## Prompt para o subagente crítico

Quando a sessão puder despachar um subagente, ele critica sem o viés de quem fez o deck. Troque `<slug>` e mande
isto, com o modelo mais forte disponível; ele não edita nada e devolve só a lista. A sessão confere a evidência de
cada item antes de corrigir.

```text
Você é o crítico visual de uma apresentação ao vivo feita por código, no repositório
/caminho/do/repositorio (troque pelo caminho real). O deck é decks/<slug>/deck.html, em plano contínuo, com a
biblioteca motor/cenas.js (contrato em docs/cenas.md). A régua de qualidade é decks/previa-curso-ia, aprovada pelo
usuário. Não edite nenhum arquivo.

1. Rode ./ap sondar decks/<slug> e ./ap paradas decks/<slug> --viagens. Se o storyboard da prévia não existir, rode
   também ./ap paradas decks/previa-curso-ia --viagens.
2. Abra com a ferramenta Read: decks/previa-curso-ia/storyboard/folha.png (a régua), depois
   decks/<slug>/storyboard/folha.png, cada decks/<slug>/storyboard/parada-*.png e decks/<slug>/storyboard/viagens.png.
   Abra inteiro todo viagem-*.png que parecer errado na folha das viagens.
3. Responda, slide por slide, a rubrica e a lista "Defeitos que já apareceram" de
   .claude/skills/apresentacao/critica.md.
4. Devolva no máximo dez defeitos, do mais grave ao menos grave, cada um com: gravidade (alta, média ou baixa),
   slide, o que se vê e onde (arquivo PNG e região aproximada em pixels), a correção concreta (arquivo, seletor ou
   linha, valor) e o quadro que prova a correção depois.

Não proponha o que docs/cenas.md proíbe em "O que a biblioteca não faz" (paralaxe, câmera inclinada, pulsos na
trilha, mix-blend-mode ou will-change no #mundo, duotone ao vivo, notebook ou celular como moldura, rabisco à mão em
toda parada, número ilustrativo gigante). Mudança de texto que o público vê vai marcada "depende do usuário". Não
elogie; se não achar defeito de gravidade alta ou média, diga isso numa linha.
```
