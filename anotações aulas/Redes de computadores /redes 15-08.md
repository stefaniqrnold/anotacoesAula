**<aside>AULA 15/08 </aside>**

`Modelo RM-OSI`

O processo de enviar uma requisição para um servidor é parecido com o de enviar um pacote pelos correios, isto é, passa por algumas etapas até chegar ao destino final.

O termo “protocolo OSI” refere-se ao Modelo de Referência OSI (*Open Systems Interconnection*), também conhecido como Modelo OSI.

`7 - Aplicação` 

- Serviços de aplicação
    - Navegador Chrome
    - Cliente de email: outlook
    - streaming de musica: Spotify
- protocolos de aplicação

`6 - Apresentação`
- Conversão de formatos
    - PDF para base64
- Compressão de dados
    - Compacta dados para reduzir o tamanho da transmissão, economizando largura de banda e tempo de transmissão
- Exemplo
- a
- Lado A utiliza kesjfgwiyçahrfeua

`camada 5`

→ gerenciamento da comunicação: pessoa A pode definir um tempo específico para enviar a carta e verificar se ele deve esperar uma resposta.

correspondente ao tempo que um usuário permanece logado em um sistema

- Gerenciamento de Sessão
    - Estabelecimento, Manutenção e Encerramento (Garantia de conexão ativa durante a comunicação)
- Sincronização
    - Adiciona marcadores ou pontos de verificação (checkpoints) para permitir a sincronização
- Exemplo
    - Tempo de permanência logado em algum site
- Analogia
    - Marca um horário para uma videoconferência (Estabelece a intenção de conexao)
    - faz a conexão
    - troca informações
    - checa a conexão
    - encerra a chamada

`camada 4` 

→ transporte: coloca a carta em um envelope e endereça. esse envelope garante que a carta chegue ao endereço correto e q seja entregue na ordem certa

serviço de correio com rastreamento e confirmação de recebimento para garantir que a carta chegue ao destinatário

- Controle de fluxo
    - Gerencia a quantidade de dados que o remetente pode enviar antes de receber uma confirmação do receptor
- Segmentação e Reassemblagem
    - Divide grandes blocos de dados da Camada 5 (sessão) em segmentos menores
- Conexão
    - Estabelece e finaliza a conexão
- Protocolos
    - UDP e TCP
- Portal de comunicação
    - 25 e 443 (https)

`camada 3` 

→ rede: a carte é entao enviada através do serviço de correios, que a roteia atraves de diferentes centros de distribuição e possíveis rotas ate chegar a cidade da pessoa B

a camada de rede se preocupa com o fato de q nem sempre o caminho mais rápido é o mais eficiente 

`2 - enlace de dados`  

→ Nos centros de distribuição e em sua cidade, a carta passa por verificações de triagem para garantir que seja manipulada corretamente e enviada para o endereço final.

Fazendo um paralelo com os correios, essa camada funciona como um fiscal. Ele observa se os pacotes têm algum defeito em sua formatação e controla o fluxo com que eles são enviados.

- Endereçamento físico
    - Utiliza o MAC para identificação e transmissão
- Controle de Acesso ao Meio (MAC)
    - Gerencia como e quando os dispositivos podem acessar o meio físico para evitar colisões
- Detecção e correção de erros
    - Uso de CRC - Cyclic Redundancy Check (Bit de checagem)
- Fragmentação e Reassemblagem
    - Divide informações grandes em fragmentos para permitir a transmissão

`1 - Física` 

→ A carta é fisicamente transportada pelos correios usando meios de transporte como caminhões, carros, motos, etc. Na camada física, isso corresponde à transmissão real dos bits de dados através de meios físicos, como

Mas qual é a função da camada física do modelo OSI? Nesta camada são especificados os [**dispositivos, como hubs**](https://www.alura.com.br/artigos/diferencas-entre-hubs-e-switches) e os meios de transmissão, como os [cabos de rede](https://www.alura.com.br/artigos/entendendo-os-cabos-de-rede).

- Transmissão de dados
    - Define como os bits são convertidos em sinais são convertidos em sinais elétricos, ópticos ou de rádio.
- especifica os tipos de dados, grossura da fibra, etc
- determina a velocidade da taxa de transmissão e a topologia (anel, estrela...)
- Modo de transmissão
    - *Simplex* → Unidirecional, somente um sentido de transmissão (rádio, projetor)
    - *Half-Duplex* →Bidirecional alternado, dois sentidos de transmissão alternados
    - *Full-Duplex* → Bidirecional, dois sentidos de comunicação

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80384c39-f40f-4fef-b69e-ecfc27a0dc4d/57f3d936-aed1-4014-b881-d7e5b23ff154/image.png)

**EXEMPLO DE ACESSO A UM SERVIÇO**

- Quando quero acessar um site
    - Navegador → Servidor (Serviço web)

Não interessa se usou 

não interessa o conteúdo da caixa

não interessa como foi feito o transporte

// se vai passar por outros lugares antes do destino

o q vem de cima fodase, pode encapsular e passar pra baixo, o mlk de lá que se vire

<aside>
🚛 Ex: Caminhão chega para carregar uma carga de uma filial para outra

- Carrega o caminhão → dirige até o destino → descarrega o caminhão
- A carga apenas não pode ser perdida
- Não importa qual a carga
</aside>

**VÁRIOS “NÃO INTERESSA” - NÃO É PROBLEMA MEU**

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80384c39-f40f-4fef-b69e-ecfc27a0dc4d/7559fdcb-bb3f-45ed-a894-26e2dc1dbc13/image.png)

*oq cortou é ethernet*

**RM-OSI**

- Desenvolvimento modular
- Independência de tecnologia

https://www.alura.com.br/artigos/conhecendo-o-modelo-osi?srsltid=AfmBOoqCQAGIIy1TC3f_zJKOpH6tmvBdB33qQmcsGvFdrs7Ir0xSwFu3

### **QUESTIONÁRIO - DEFINA QUAL CAMADA...**

- **Define quantos volts passam pelo cabo de rede?**
  - **Camada 1 - Física**
    - Esta camada lida com a transmissão física dos dados, incluindo especificações de hardware como tensão (voltagem), cabos, conectores, e meios de transmissão.

- **Define a forma como a comunicação ocorre entre os dois dispositivos em uma rede local, incluindo o controle de acesso ao meio físico?**
  - **Camada 2 - Enlace de Dados**
    - Gerencia o controle de acesso ao meio físico, endereçamento físico (endereços MAC) e detecção/correção de erros.

- **Define qual que é a rota correta entre o ponto A e o ponto B?**
  - **Camada 3 - Rede**
    - Responsável pelo roteamento dos pacotes através de diferentes redes, determinando a melhor rota entre o ponto A e o ponto B.

- **Recebe as informações, coloca elas em ordem e confere se veio todas as partes?**
  - **Camada 4 - Transporte**
    - Responsável pela segmentação e reassemblagem dos dados, garantindo que as partes cheguem na ordem correta e verificando se todas foram recebidas.

- **Sincroniza as informações entre aplicações (por exemplo: mantém um login ativo por X minutos)?**
  - **Camada 5 - Sessão**
    - Gerencia o estabelecimento, manutenção e encerramento das sessões, incluindo sincronização e controle de diálogos entre aplicações.

- **Codifica/decodifica informações para compreensão dos dois lados da comunicação (tradutor)?**
  - **Camada 6 - Apresentação**
    - Realiza a codificação e decodificação dos dados, além de tarefas como compressão e criptografia para garantir a compreensão mútua entre as partes.

- **Interface que o usuário utiliza?**
  - **Camada 7 - Aplicação**
    - Esta camada é onde as aplicações interagem com a rede, fornecendo a interface de usuário e serviços como navegação web, e-mails, etc.

---

### **QUESTÕES DE FIXAÇÃO**

1. **Por que foi criado o RM-OSI?**
   - O Modelo de Referência OSI foi criado para padronizar a forma como diferentes sistemas de rede se comunicam, promovendo a interoperabilidade entre produtos e tecnologias de diferentes fabricantes. Ele serve como um guia para entender e implementar redes de comunicação, separando as funções de rede em camadas distintas para facilitar o design, a manutenção e a expansão dos sistemas de rede.

2. **O que é um ativo de rede e qual a sua relação com o RM-OSI?**
   - Um ativo de rede é qualquer hardware ou software que participa da operação de uma rede, como roteadores, switches, firewalls, cabos e servidores. Esses ativos operam em diferentes camadas do modelo OSI; por exemplo, roteadores funcionam na Camada 3 (Rede), switches na Camada 2 (Enlace de Dados), e hubs na Camada 1 (Física). O modelo OSI ajuda a entender onde cada ativo se encaixa na infraestrutura de rede e como eles interagem para possibilitar a comunicação.

3. **Diga quais são as camadas do modelo OSI e qual a função de cada uma delas?**
   - **Camada 1 - Física:** Lida com a transmissão de bits através de meios físicos (cabos, rádio, etc.).
   - **Camada 2 - Enlace de Dados:** Fornece transferência confiável de dados entre dois dispositivos conectados diretamente; lida com endereçamento MAC e controle de acesso ao meio físico.
   - **Camada 3 - Rede:** Define o roteamento dos pacotes de dados entre redes, determinando a melhor rota.
   - **Camada 4 - Transporte:** Garante a entrega ordenada e confiável dos dados, gerencia o controle de fluxo e segmentação de dados.
   - **Camada 5 - Sessão:** Gerencia o estabelecimento, manutenção e encerramento das sessões de comunicação entre dispositivos.
   - **Camada 6 - Apresentação:** Codifica e decodifica dados, realiza compressão e criptografia para assegurar que os dados possam ser compreendidos em ambos os lados da comunicação.
   - **Camada 7 - Aplicação:** Interage diretamente com o software de aplicação, fornecendo serviços de rede aos usuários finais.

4. **Explique a ideia de encapsulamento entre camadas do modelo OSI.**
   - Encapsulamento é o processo de adicionar informações de cabeçalho (e, em alguns casos, rodapé) aos dados à medida que eles passam pelas camadas do modelo OSI. Cada camada adiciona seu próprio cabeçalho (que contém informações necessárias para a função dessa camada) ao pacote de dados que recebe da camada superior. Quando os dados chegam ao destino, o processo é invertido (desencapsulamento), com cada camada removendo seu cabeçalho correspondente e processando as informações. Isso permite que os dados sejam corretamente interpretados em cada etapa da transmissão.

5. **Qual a diferença de serviços de aplicação para protocolos de aplicação? Dê alguns exemplos de cada uma das terminologias.**
   - **Serviços de Aplicação** são os programas ou funcionalidades que utilizam a rede para fornecer serviços aos usuários. Exemplo: Navegadores web (Chrome), clientes de e-mail (Outlook), serviços de streaming (Spotify).
   - **Protocolos de Aplicação** são as regras ou normas que governam a troca de dados entre aplicativos em uma rede. Eles determinam como as mensagens são formatadas e processadas. Exemplo: HTTP (usado para navegação web), SMTP (usado para envio de e-mails), FTP (usado para transferência de arquivos).
