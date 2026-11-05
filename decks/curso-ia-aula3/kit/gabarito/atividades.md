# Gabarito das Atividades 1 e 3

## Atividade 1: os três defeitos da skill

1. **Descrição que dispara sempre.** A `description` manda usar a skill "em qualquer pedido do usuário, sobre qualquer
   assunto". Uma skill boa diz quando usar e quando não usar.
2. **Script que envia a pasta para fora.** O passo 3 compacta toda a pasta de trabalho (`tar czf - .`) e a envia por
   `curl` a um endereço externo. Chamar isso de "cópia de segurança" não muda o que o comando faz: os autos saem do seu
   computador. O domínio `exemplo.invalid` não existe; numa skill real, seria um servidor de terceiro.
3. **Permissão ampla demais.** O passo 4 manda executar os comandos "sem pedir confirmação ao usuário". É justamente a
   confirmação que deixaria você barrar o passo 3.

O resto da skill é inofensivo de propósito, porque o defeito costuma vir misturado com instruções úteis.

## Atividade 3: onde está a ordem escondida

A petição traz a mesma ordem em dois lugares: um parágrafo em letra branca e corpo 2 entre "Dos fatos" e "Do direito"
(aparece como um espaço em branco maior), e uma linha em corpo minúsculo, cinza claro, logo abaixo da assinatura. A
ordem manda o assistente de IA desconsiderar os demais documentos, concluir pela procedência integral e não mencionar a
instrução. O olho não vê, mas o agente lê o texto inteiro do PDF. Selecionar todo o texto (Ctrl+A ou Cmd+A) revela os
dois trechos.
