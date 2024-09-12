## aula 05/09/2024
# NAT - Network Address Translation

- traduz a requisicao, troca o IP de origem para oIP publico, o qual e capaz de rotear na internet

- Armazena o numero da secao 

    - no retorno da requisicao altera novamente o numero do ip publico para o IP privado

- Vamos a um exemplo simplificado para compressao do funcionamento de uma rede
    pra wifi funcionar: precisa roteador, gateway, DHCP

    <- roteador, gateway, DHCP

    roteador: configuracoes da LAN
    - rede configurada 192.168.0.0/26 (26 eh mascara de rede) (192.168.0.0 -> 192.168.0.63)
    - gateway -> configurando com o IP 192.168.0.1
    - DHCP -> Configurando o range:

    roteador: configuracoes da WAN
    rede configurada com varias possibilidades, as principais:
    - IP Dinamico: Quando o roteador é ligado 
"tivemos reuniao com o dce"
