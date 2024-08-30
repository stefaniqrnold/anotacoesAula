# aula 30/08/2024

## Comunicação distribuída

● Processo de troca de informações entre sistemas ou processos em diferentes lógicos ou geográficos

● Essencial para colaboração, eficiência e escalabilidade de sistemas complexos

● Através de troca de mensagens

    – Diferentes formas

● Sisteme operacional fornece através de bibliotecas esse recurso aos processos de usuário para troca de mensagens

● Basicamente, duas chamadas de biblioteca

    – send(dest, &mptr)

● Envia a mensagem apontada por mptr para um processo dest

● Pode ser bloqueante (espera a confirmação de recebimento) ou não bloqueante

    – receive(addr, &mptr)

● Recebe um mensagem de addr, armazenando no buffer apontado por mptr e

● Pode bloquear o processo até a mensagem ser recebida, ou não bloqueante

● Chamadas bloqueantes (síncronas)

    – Enquanto a mensagem está sendo recebida ou enviada, o processo que solicitou a operação é suspendo (bloqueado)
    – O processo é acordado depois que a operação de envio ou recebimento é concluída

● Chamadas não-bloqueantes (assíncronas)

    – Os processos não precisam estar prontos ao mesmo tempo para troca de mensagens
    – O processo não é bloqueado após fazer uma chamada para envio ou recebimento de mensagem

– Mais eficientes –

    ● Processo pode continuar usando CPU
    ● Maior flexibilidade e desempenho

– Exemplos:

    ● Serviços de mensageria, fila de mensagens

● Abordagem diferente das diretivas send e recieve

    – Baseadas em entrada e saída
    – Troca de dados somente

● RPC → Programas podem chamar rotinas localizadas em outras CPUs

● Ideia: chamada de um procedimento remoto como se fosse local

    – Quem chama o procedimento é conhecido como cliente
    – O procedimento chamado é conhecido como servidor
    – Intermediada pelas bibliotecas stub (do cliente e do servidor)

# to com preguiça de copiar o resto, tem no slide
