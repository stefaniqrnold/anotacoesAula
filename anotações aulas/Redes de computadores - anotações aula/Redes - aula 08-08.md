RFC -

- **internet** - ligação entre redes, INTERCONEXÃO

PTT - liga os provedores de internet, outros PTT’s, servidores, entre outras varias coisas. é uma infraestrutura física

backbone - responsável por fazer a ligação interna da internet, “espinha dorsal” da internet. liga todos os servidores em um só

- **Evolução**

inicialmente - sistemas altamente centralizado

os componentes da rede eram basicamente computadores de mesa, estações de trabalho, e servidores web, de e-mail e de mensagens

atualmente - sistemas distribuídos

estão sendo conectados

sistemas finais: desktop, celular…

curiosidade: o Brasil foi um dos únicos países que não caiu a internet na pandemia. ele “deu conta”, esteve preparado para uma grande quantidade de consumo de internet simultânea.

cabos oceânicos: servem pra transmitir dados entre longas distancias

envio de pacotes  

o endereçamento dos PCs na versão 4 do IP eh em trono de 4bi

dominio - endereco (youtube.com)

![[Untitled.png]]

  
**CLASSIFICAÇÃO DAS REDES**

se tiver w na frente quer dizer que é sem fio

LAN - Local Area Network: conexão local: predios, campus, delimitado a uma pequena area.

MAN - Metropolitan area network: conexão maior que uma LAN geralmente uma cidade ou uma região metropolitana

WAN - Wide area network: conexão de Estados e países

PAN - Personal area network: conexão pessoal: celular na caixa ed som pelo bluetooth

CAN campus area network: conexão maior que LAN mas menor q uma WAN. dois predios conectados por exemplo

GAN global area network: conexão de wans tipo starlink

BAN body area network: redew de area corporal pra conectar dispositivos ao redor de um corpo humano. tipo aqueles relogios

  

**topologia - forma como a rede eh ligada**

topologia ponto a ponto: ligação entre dois computadores ( tipo uma impressora conectada no pc pelo cabo usb, fone de ouvido no PC)

- forma fisica
- forma lógica: conexão VPN - PC com servidor


### **topologia - anel**

- toda comunicação passa de um computador para o outro. topologia em desuso

### **topologia - barramento**

- todos os hosts compartilham o mesmo meio físico. enquanto um equipamento transmite a informação, todos “escutam”
- Broadcast elevado - manda informação pra todo mundo
  
### **topologia - estrela**

- ligação de todos os computadores em um nó central
- vantagem: se um aparelho parar de funcionar, os outros continuam funcionando. contudo, se o aparelho central cair, todos caem
- é a topologia mais utilizada

### **topologia - malha “**_**mash**_**”**

- Cada dispositivo e conectado a vários outros dispositivos, formando uma rede com múltiplos caminhos entre os dispositivos.
- conexão completa
- conexão parcial
- uma das mais robustas que existem, a mais cara que existe por causa de todas as conexões
- a wifi da UNIJUI não eh considerada uma malha completa
- pra ser completa, os roteadores teriam que estar mais próximos. por isso a conexão da fidene com o campus seria parcial, pois está bem longe(nseipqnavdd)

tipologia - arvore

- funciona como uma arvore genealogica. é por hierarquia, cada nó tem seus respectivos filhos

### Topologia - híbrida

## QUESTÕES

1 - Qual a diferença entre classificação de redes e tipologias de rede?

- **Classificação de redes**: Refere-se à categorização das redes com base em diferentes critérios, como o tamanho, a extensão geográfica e o propósito. Essa classificação leva em consideração o tamanho e a localização das redes.
- **Topologia de rede**: Refere-se à forma como os elementos de uma rede (como computadores, servidores e outros dispositivos) estão conectados uns aos outros.

2 - Qual a diferença entre topologia física e topologia lógica de rede? de exemplos.

- Topologia física - representa o layout da rede (como os dispositivos estão fisicamente conectados).
- Topologia lógica - como os dados são transmitidos (se movem) de um dispositivo para outro, sem levar em conta a parte física.
    - Por exemplo, a conexão VPN entre um servidor e um computador.

3 - Qual topologia física é a mais usada atualmente? Por que? Qual a maior vantagem?

Estrela, é usada porque tem um elemento central que gerencia o fluxo de dados da rede, passando para cada nó. a maior vantagem é que, caso um aparelho dê algum erro de conexão, outros aparelhos continuam funcionando normalmente(com exceção do elemento central).

4 - Dentro de uma rede de computador é possível utilizar mais de uma topologia?

Sim. Por exemplo, a topologia híbrida une duas ou mais topologias.

5 - O que eh PTT (IE) no contexto de rede de computadores e qual sua importância para a internet?

É uma infraestrutura física que permite a troca direta de tráfego entre diferentes redes, como ISPs (provedores de internet) e redes de conteúdo. Sua importância para a internet reside na redução da latência, economia de custos, maior resiliência, e melhoria do desempenho das conexões, tornando a navegação mais rápida e estável para os usuários.

6 - A televisão exibindo um filme em um serviço de streaming é um host? Por que?

Sim, uma televisão exibindo um filme via streaming é considerada um **host** porque, em redes de computadores, um host é qualquer dispositivo que se conecta à rede e troca dados. Ao acessar e reproduzir o conteúdo do serviço de streaming, a televisão está recebendo dados da internet, desempenhando o papel de um host na rede.

7 - O que é a internet?

É uma ligação entre redes - Interconexão

É uma interconexão global de redes de computadores que permite a comunicação e troca de dados entre dispositivos em todo o mundo, utilizando protocolos padronizados como o TCP/IP.

8 - Qual a importância das RFC?

As RFC são importante por conta da sua padronização que determina regras que garantem a segurança

9 - o que é processamento time-sharing?