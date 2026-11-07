# Retenção de dados e uso para treino: assinatura individual x contrato empresarial e API

Pesquisa feita em 06/11/2026, só com páginas lidas nesta data. Fonte primária em quase todos os itens; o que não foi confirmado está marcado. As páginas da OpenAI recusam acesso automatizado (HTTP 403) e foram lidas no navegador integrado.

## Resumo

1. Nas assinaturas individuais o treino depende de configuração do usuário: no ChatGPT e no Gemini pessoal vem ligado por padrão; no Claude a Anthropic pede uma escolha desde 28/08/2025, e quem permite treino tem os chats guardados por até 5 anos.
2. Nos contratos empresariais (Claude Team/Enterprise, ChatGPT Business/Enterprise/Edu, Gemini no Workspace, Microsoft 365 Copilot) e nas APIs pagas, as cinco empresas declaram que não treinam com os dados do cliente por padrão.
3. "Não treinar" não quer dizer "não guardar": as APIs da Anthropic e da OpenAI guardam entradas e saídas por até 30 dias; a do Google, 55 dias para monitoramento de abuso; retenção zero (ZDR) existe, mas depende de pedido aprovado.
4. A API gratuita do Gemini usa o conteúdo para melhorar produtos e admite leitura por revisores humanos; a paga não usa para melhorar produtos.
5. Novidade de 2025-2026: os modelos mais novos da Anthropic (Fable 5 e 5.1, Mythos 5 e 5.1) exigem 30 dias de retenção e ficam fora da ZDR, inclusive no AWS Bedrock; e a ordem judicial do caso NYT, que obrigava a OpenAI a guardar tudo, terminou em 26/09/2025.

## Tabela comparativa

| Serviço | Treina com seus dados? | Guarda por quanto tempo | Fonte | Confiança |
|---|---|---|---|---|
| Claude Free, Pro, Max | Só se o usuário permitir ("Help improve Claude"); escolha exigida desde 28/08/2025 | Com treino: até 5 anos (desidentificado). Sem treino: 30 dias. Apagado: sai em até 30 dias. Sinalizado por segurança: até 2 anos (pontuação de classificação, 7 anos). Feedback: 5 anos | [A1], [A2], [A3] | Alta (pré-seleção do botão para conta nova: não confirmada) |
| Claude Team / Enterprise | Não, por padrão (salvo feedback ou adesão) | Chats ficam enquanto a organização quiser (política definida pelo administrador); apagado sai em até 30 dias; sinalizado até 2 anos | [A4], [A5], [A6] | Alta |
| API Claude (Claude Developer Platform) | Não, sem permissão expressa | Até 30 dias; ZDR sob pedido à equipe de vendas; modelos Fable/Mythos exigem 30 dias e não entram na ZDR | [A4], [A6] | Alta |
| ChatGPT Free, Plus, Pro | Sim, por padrão; desliga em "Improve the model for everyone" | Salvo até o usuário apagar; apagado e chat temporário: até 30 dias | [O1], [O2] | Alta |
| ChatGPT Business / Enterprise / Edu | Não, por padrão | Administrador define; apagado sai em até 30 dias | [O3] | Alta |
| API OpenAI | Não, por padrão (desde 01/03/2023) | Até 30 dias para monitoramento de abuso; ZDR e "Modified Abuse Monitoring" com aprovação prévia | [O4], [O3] | Alta |
| Gemini app pessoal | Sim, com "Keep Activity" ligado (padrão para maiores de 18) | 18 meses por padrão (3, 36 meses ou sem limite); desligado ou chat temporário: 72 horas; chats revisados por humanos: até 3 anos | [G1], [G2] | Alta |
| Gemini no Workspace | Não, sem permissão do cliente | Gemini no Workspace: 90 dias a indefinido, a critério do administrador; app Gemini corporativo: até 36 meses | [G3] | Alta |
| Gemini API gratuita | Sim, para melhorar produtos; revisores humanos podem ler | 55 dias para abuso (prazo de treino não informado) | [G4], [G5] | Alta |
| Gemini API paga | Não usa para melhorar produtos | 55 dias para abuso; registros (logs) de projeto até 55 dias, ligados por padrão em projetos novos desde 26/10/2026 | [G4], [G5], [G6] | Alta |
| Vertex AI (Google Cloud) | Não, sem permissão | Cache de até 24 horas (desligável); Grounding com Google Search: 3 dias, sem como desligar; registro de prompt para abuso sem prazo informado | [G7] | Alta (prazo do registro de abuso: não confirmado) |
| AWS Bedrock | Não; fabricante não tem acesso a prompts nem a logs | Em regra, não guarda; Claude Fable 5 e 5.1 e modelos OpenAI (tráfego sinalizado): até 30 dias dentro da AWS, sem repasse ao fabricante | [W1], [W2], [W3] | Alta |
| Azure OpenAI / Microsoft Foundry | Não; dados não vão à OpenAI | Só conteúdo sinalizado vai a armazenamento para revisão humana; isenção por formulário ("modified abuse monitoring"); prazo em dias não aparece na página atual | [M1], [M2] | Alta (prazo: não confirmado) |
| Microsoft Copilot consumidor | Sim, salvo opt-out ("Model training on text/voice") | Histórico de 18 meses | [M3] | Média (página vale para o app antigo; exclusão do Brasil: não confirmada) |
| Microsoft 365 Copilot | Não treina modelos de base | Segue as regras do Microsoft 365; administrador define pelo Purview | [M4] | Alta |

## Detalhe por empresa

### Anthropic

Em 28/08/2025 a Anthropic mudou os termos do consumidor: os planos Free, Pro e Max (inclusive o Claude Code usado nessas contas) passaram a oferecer a escolha de permitir treino, com prazo até 08/10/2025 para os usuários existentes decidirem. Quem permite tem os chats novos ou retomados guardados por até 5 anos; quem não permite fica no prazo de 30 dias. A mudança não atinge Team, Enterprise, Claude Gov, Claude for Education nem a API, inclusive via Bedrock e Vertex [A2]. A página de retenção do consumidor (datada de 01/07/2026) confirma 30 dias para conversa apagada, até 2 anos para conteúdo sinalizado por violação de política e 5 anos para feedback; o chat anônimo ("Incognito") não é usado para treino [A1]. A página de treino do consumidor (16/03/2026) diz que o uso ocorre quando o usuário "escolhe permitir" [A3]; se o botão vem pré-ligado para conta nova não foi confirmado em fonte primária (apenas guias de terceiros afirmam que sim).

Nos produtos comerciais, a Anthropic não usa entradas e saídas para treino por padrão (página de 18/08/2026), salvo feedback ou adesão; o administrador de Team e Enterprise pode desligar o envio de feedback [A5]. A API apaga entradas e saídas em até 30 dias, com exceções para recursos que guardam dados por natureza (Files API, Batch, execução de código), acordo de ZDR, violação de política e exigência legal [A4]. A documentação técnica diz que a ZDR é pedida à equipe de vendas e ativada por organização; os modelos Fable 5, Fable 5.1, Mythos 5 e Mythos 5.1 ("Covered Models") exigem 30 dias de retenção e não entram em ZDR salvo autorização expressa [A6]. A mesma página registra uma frase ambígua ("conversation content is not retained by default"), escrita no contexto dos recursos elegíveis à ZDR; para a API comum vale o prazo de 30 dias da página de privacidade. As interfaces de chat do Team e do Enterprise não são elegíveis à ZDR, com exceção do Claude Code no Enterprise [A6].

### OpenAI

No ChatGPT Free, Plus e Pro o compartilhamento para treino vem ligado por padrão e se desliga em Configurações > Controles de dados > "Improve the model for everyone", sem perder o histórico [O1]. A mesma página (atualizada em 05/11/2026) registra uma novidade: em sessões do programa "Trusted Access" (Daybreak) a OpenAI pode usar o conteúdo para treino mesmo com o botão desligado. O chat temporário não aparece no histórico, não é usado para treino e pode ser guardado por até 30 dias para segurança; conversa apagada sai dos sistemas em até 30 dias, salvo dado já desidentificado ou obrigação legal [O1], [O2]. Feedback (polegar) pode levar a conversa inteira ao treino mesmo com opt-out [O1].

ChatGPT Business, Enterprise, Edu, Healthcare e Teachers e a API não são usados para treino por padrão (página de 08/01/2026). No Enterprise e no Edu o administrador define a retenção; apagados saem em 30 dias [O3]. A API guarda entradas e saídas por até 30 dias para prestar o serviço e detectar abuso; ZDR e "Modified Abuse Monitoring" exigem aprovação prévia e se configuram em Settings > Organization > Data controls [O4], [O3].

A ordem de preservação do caso New York Times terminou: segundo a OpenAI (atualização de 22/10/2025), as obrigações acabaram em 26/09/2025 e a empresa voltou aos 30 dias. Continua guardado, sob bloqueio legal, um conjunto limitado de dados de usuários de abril a setembro de 2025; a ordem nunca atingiu ChatGPT Enterprise, Edu nem API com ZDR [O5]. Relatos de imprensa mencionam ainda contas específicas indicadas pelo NYT, ponto não confirmado em fonte primária.

### Google

No app Gemini pessoal, "Keep Activity" vem ligado para maiores de 18 e a atividade se apaga após 18 meses (ajustável para 3 ou 36 meses, ou sem limite) [G2]. A página de privacidade (26/10/2026) diz que a atividade é usada inclusive para treinar modelos generativos, que uma parte dos chats é lida por revisores humanos, que chats revisados ficam até 3 anos e que, com a atividade desligada ou em chat temporário, os chats ficam 72 horas na conta; a página pede que o usuário não digite informação confidencial que não queira ver lida por um revisor [G1].

No Workspace, o Google não usa dados do cliente para treino sem permissão, o conteúdo não passa por revisão humana fora do domínio e a retenção vai de 90 dias a indefinido no Gemini do Workspace, conforme o administrador (página de 06/10/2026) [G3]. Na Gemini API, os termos vigentes desde 23/03/2026 separam o serviço gratuito, cujo conteúdo é usado para "fornecer, melhorar e desenvolver" produtos e pode ser lido por revisores, do pago, que não usa prompts nem respostas para melhorar produtos [G4]. A política de uso fixa 55 dias de guarda para detecção de abuso [G5]; os logs de projeto pago têm teto de 55 dias e ficam ligados por padrão em projetos criados a partir de 26/10/2026 [G6].

### Nuvens

Vertex AI: o Google não treina com dados do cliente sem permissão; há cache em memória e cache durável, ambos ligados por padrão, apagados em até 24 horas e desligáveis pelo administrador; o Grounding com Google Search guarda consultas por 3 dias sem opção de desligar; para ZDR é preciso desligar cache e outros recursos [G7]. A página não informa o prazo do registro de prompts para abuso.

AWS Bedrock: os fabricantes não têm acesso às contas onde os modelos rodam, nem a logs, prompts ou respostas [W1]. A retenção agora é configurada por modo (`none`, `default`, `aws_review`); o Claude Fable 5 e 5.1 só funcionam com `aws_review`, que guarda prompts e respostas por até 30 dias dentro da AWS, com revisão humana feita pela própria AWS e sem repasse à Anthropic [W2]. Para modelos da OpenAI no Bedrock, o tráfego sinalizado fica até 30 dias; clientes do programa Enterprise Frontier Safeguards têm ZDR para o Fable até 31/12/2026 [W3].

Azure (Foundry, inclusive Azure OpenAI): prompts e respostas não ficam disponíveis à OpenAI, não são usados para treinar modelos de base e o serviço não fala com os sistemas da OpenAI [M1]. A revisão de abuso é automatizada por padrão; só o conteúdo sinalizado vai a um armazenamento para revisão humana, na mesma geografia do recurso. Quem lida com dado altamente sigiloso pode pedir isenção ("modified abuse monitoring") por formulário, sujeita a critérios de acesso limitado [M2]. O prazo de 30 dias aparece só em versões antigas da documentação; a página atual não dá número (não confirmado).

### Microsoft Copilot

No Copilot de consumidor (conta Microsoft pessoal), há opt-out de treino em texto e voz e o histórico fica 18 meses; a página avisa que vale para o app antigo e que uma versão nova saiu em 18/08/2026 [M3]. A exclusão de usuários do Brasil do treino aparece só em guias de terceiros (não confirmada). No Microsoft 365 Copilot, prompts, respostas e dados do Microsoft Graph não treinam modelos de base, o Copilot não usa a revisão humana de abuso do Azure OpenAI e a retenção segue as regras do Microsoft 365, configuráveis no Purview [M4].

## O que muda para quem trabalha com processo sob sigilo

Na assinatura individual, a regra depende de um botão que o próprio usuário controla e que, no ChatGPT e no Gemini, vem ligado; com ele ligado, o texto colado pode entrar em treino e, no Gemini, ser lido por revisor humano e guardado por até 3 anos. Desligar o treino não zera a guarda: o ChatGPT mantém conversa apagada ou temporária por até 30 dias, o Gemini por 72 horas e o Claude por 30 dias. Nos contratos empresariais e nas APIs pagas não há treino por padrão e o prazo é fixado em contrato ou pelo administrador, mas ainda há guarda curta para monitoramento de abuso, que só some com ZDR ou isenção aprovada. Os modelos mais novos da Anthropic exigem 30 dias mesmo em contrato, o que deve entrar na conta de quem precisa de retenção zero.

## Proposta de slide

- Rótulo: Sigilo
- Manchete: Assinatura não é contrato
- Coluna "Assinatura individual":
  - Treino depende de você
  - Guarda até 5 anos
  - Revisão humana possível
- Coluna "Contrato empresarial / API":
  - Sem treino por padrão
  - 30 dias ou zero
  - Prazo fixado no contrato
- Linha de fonte: Fonte: políticas oficiais, lidas em 06/11/2026

Contagem: 40 palavras visíveis. "Até 5 anos" é o teto do Claude com treino permitido; "30 dias ou zero" resume Anthropic e OpenAI (o Google usa 55 dias na API, o que cabe na fala, não na tela).

## Fontes lidas em 06/11/2026

- [A1] https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data (data na página: 01/07/2026)
- [A2] https://www.anthropic.com/news/updates-to-our-consumer-terms (28/08/2025)
- [A3] https://privacy.claude.com/en/articles/10023555 (16/03/2026)
- [A4] https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data (01/07/2026)
- [A5] https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training (18/08/2026)
- [A6] https://platform.claude.com/docs/en/manage-claude/api-and-data-retention (sem data)
- [O1] https://help.openai.com/en/articles/7730893-data-controls-faq (atualizada em 05/11/2026)
- [O2] https://help.openai.com/en/articles/8983778 (atualizada em 03/11/2026)
- [O3] https://openai.com/enterprise-privacy/ (versão pt-BR, 08/01/2026)
- [O4] https://developers.openai.com/api/docs/guides/your-data (sem data além de 01/03/2023)
- [O5] https://openai.com/index/response-to-nyt-data-demands/ (05/06/2025, atualização de 22/10/2025)
- [G1] https://support.google.com/gemini/answer/13594961?hl=en (26/10/2026)
- [G2] https://support.google.com/gemini/answer/13278892?hl=en (sem data)
- [G3] https://knowledge.workspace.google.com/admin/gemini/generative-ai-in-google-workspace-privacy-hub?hl=en (06/10/2026)
- [G4] https://aistudio.google.com/docs/terms (vigente desde 23/03/2026)
- [G5] https://aistudio.google.com/docs/usage-policies (sem data)
- [G6] https://aistudio.google.com/docs/logs-policy (sem data; menciona 26/10/2026)
- [G7] https://docs.cloud.google.com/vertex-ai/generative-ai/docs/data-governance (sem data)
- [W1] https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html
- [W2] https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html
- [W3] https://docs.aws.amazon.com/bedrock/latest/userguide/abuse-detection.html
- [M1] https://learn.microsoft.com/en-us/azure/ai-foundry/responsible-ai/openai/data-privacy (ms.date 18/05/2026)
- [M2] https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/abuse-monitoring (ms.date 13/05/2026)
- [M3] https://support.microsoft.com/topic/microsoft-copilot-privacy-controls-8e479f27-6eb6-48c5-8d6a-c134062e2be6
- [M4] https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-privacy (atualizada em 04/11/2026)

Não confirmados e onde se procurou: pré-seleção do botão de treino em conta nova do Claude (privacy.claude.com, artigos 10023555 e 12109829 por busca); prazo em dias da revisão de abuso no Azure (página atual de abuse monitoring e de data privacy); prazo do registro de abuso no Vertex AI (página de data governance); exclusão do Brasil do treino no Copilot consumidor (página de controles de privacidade e blog da Microsoft de 16/08/2024); contas indicadas pelo NYT ainda preservadas (só imprensa, como Engadget).
