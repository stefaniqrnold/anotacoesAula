Qual camada?
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
