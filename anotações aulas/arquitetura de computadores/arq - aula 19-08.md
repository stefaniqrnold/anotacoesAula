# aula 12/08/2024
## multiprocessamento simétrico ou SMP (Symmetric Multi-Processing)
- como resolver a incoerência?

    protocolos de coerência baseados em hardware

- Subsistemas de memória

    armazenar (escrever) uma variavel -> memória (caixa de correio -  cada caixa tem um endereço) -> leitura do código (recuperação)

- Hierarquia de memórias (ver slides)

    RAM (random acess memory)

    separada em Endereçamento e Célula/conteúdo

- Organização básica

    memória principal (ver slide)

- capacidade da memória principal

    1 bit

    8 bits = 1 byte

    1 K = $2^{10}$ = 1.024 bits

    1 M = $2^{20}$ = 1.048.576 bits

    1 G = $2^{30}$ = 1.073.741.824 bits

    maior endereço: N - 1

    T = N . M

    célula = palavra

    ex2: Um computador, cuja memória RAM (MP) tem uma capacidade máxima de 2K palavras de 16 bits cada, possul um REM (Registrador de Endereço de Memória) em um RDM (Registrador de Dados da Memória). Qual o tamanho destes registradores? Qual o valor do maior endereço dessa MP?/Qual a quantidade total de bits que nela podem ser armazenados?
        N (REM) = 2 . $2^{10}$ = $2^{11}$
        M (RDM) = 16 = $2^{4}$
        T = $2^{11}$ . $2^{4}$ = $2^{15}$ = 32.768 bits
---
## Exercício: Memória RAM e Registradores

Um computador, cuja memória RAM (MP) tem uma capacidade máxima de 2K palavras de 16 bits cada, possui um REM (Registrador de Endereço de Memória) em um RDM (Registrador de Dados da Memória).

1. **Qual o tamanho destes registradores?**
2. **Qual o valor do maior endereço dessa MP?**
3. **Qual a quantidade total de bits que nela podem ser armazenados?**


### 1. Tamanho dos Registradores (REM e RDM)

- **REM (Registrador de Endereço de Memória):**
  - A memória RAM tem uma capacidade máxima de 2K palavras, onde "K" em termos de memória refere-se a 1024 (ou seja, 1K = 1024).
  - 2K palavras significa que a memória pode endereçar até 2048 palavras (2 * 1024 = 2048).
  - Para endereçar 2048 posições, precisamos determinar quantos bits são necessários para representar esse número.
  - O número de bits necessário para endereçar "n" posições é dado por \( \log_2(n) \).
  - Portanto, \( \log_2(2048) = 11 \) bits.
  - **Conclusão:** O REM deve ter **11 bits** para endereçar 2048 palavras.

- **RDM (Registrador de Dados da Memória):**
  - Cada palavra na memória tem 16 bits.
  - O RDM deve ser capaz de armazenar qualquer palavra da memória, então ele precisa ter 16 bits.
  - **Conclusão:** O RDM deve ter **16 bits**.

### 2. Valor do Maior Endereço da MP

- O maior endereço que pode ser representado com 11 bits é:
  - Em notação decimal: \( 2^{11} - 1 = 2047 \).
  - Isso significa que o maior endereço da MP é **2047** (em decimal).

### 3. Quantidade Total de Bits que Podem Ser Armazenados na Memória

- A memória tem 2048 palavras, e cada palavra tem 16 bits.
- A quantidade total de bits que podem ser armazenados é:
  - \( 2048 \text{ palavras} \times 16 \text{ bits/palavra} = 32768 \text{ bits} \).
- **Conclusão:** A memória pode armazenar um total de **32768 bits**.

---

**Resumo:**
1. O REM deve ter **11 bits** e o RDM deve ter **16 bits**.
2. O maior endereço da MP é **2047**.
3. A quantidade total de bits que a memória pode armazenar é **32768 bits**.
       
