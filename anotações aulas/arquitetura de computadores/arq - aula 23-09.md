## aula 23/09/2024
## Resumo sobre ASSEMBLY

**Assembly** (ou Assembler) é uma linguagem de programação de baixo nível, projetada para interagir diretamente com o hardware do computador. Ela é muito dependente da **Arquitetura de Computadores** e utiliza instruções que correspondem diretamente às operações executadas pelo processador.

---

## Principais Conceitos

1. **Linguagem de Baixo Nível**: Assembly trabalha diretamente com o hardware e suas instruções são convertidas para código de máquina. Cada linha de Assembly corresponde a uma instrução que o processador executa.

2. **Arquitetura de Computadores**: Diferentes arquiteturas (como x86, ARM) possuem diferentes conjuntos de instruções (**ISA**). Programar em Assembly significa usar essas instruções específicas do processador.

3. **Registradores**: Unidades de armazenamento dentro do processador usadas para operações rápidas. Exemplo de registradores no processador x86:
   - **AX**, **BX**, **CX**, **DX**: Para operações aritméticas e de controle.
   - **SP** (Stack Pointer), **BP** (Base Pointer): Gerenciam a pilha e funções.

4. **Pilha (Stack)**: Uma área da memória usada para gerenciar chamadas de funções, variáveis locais e controle de fluxo.

5. **Ciclo de Instrução**: O processador executa instruções em quatro fases:
   - **Fetch** (Busca): Carrega a próxima instrução.
   - **Decode** (Decodificação): Traduz a instrução.
   - **Execute** (Execução): Realiza a operação.
   - **Write Back** (Escrita): Armazena o resultado.

---

## Sintaxe e Comandos

- **Seções**:
  - `.data`: Define variáveis e dados.
  - `.text`: Contém o código executável.

- **Comandos Principais**:
  - **MOV**: Move dados entre registradores ou memória.
    - Ex: `MOV AX, 5` (carrega o valor 5 no registrador AX).
  - **ADD**: Soma valores.
    - Ex: `ADD AX, BX` (soma o valor de BX a AX).
  - **SUB**: Subtrai valores.
    - Ex: `SUB AX, 2` (subtrai 2 de AX).
  - **JMP**: Salta para outro endereço no código.
    - Ex: `JMP label` (salta para a etiqueta definida).
  - **CMP**: Compara dois valores.
    - Ex: `CMP AX, 10` (compara o valor de AX com 10).
  - **JE/JNE**: Saltos condicionais (salta se igual / se não for igual).
    - Ex: `JE label` (salta para a etiqueta se a comparação for igual).

---

## Exemplo de Código

Aqui está um exemplo básico que soma dois números e armazena o resultado:

    ```asm
    section .data
        num1 db 10      ; Define o primeiro número
        num2 db 20      ; Define o segundo número
        result db 0     ; Espaço para o resultado

    section .text
        global _start

    _start:
        mov al, [num1]  ; Carrega o valor de num1 no registrador AL
        add al, [num2]  ; Soma o valor de num2 ao conteúdo de AL
        mov [result], al ; Armazena o resultado em "result"

        ; Encerrar o programa
        mov eax, 1       ; Syscall para saída
        xor ebx, ebx     ; Código de retorno 0
        int 0x80         ; Interrupção para sair

---

### Explicação Arquitetural:

- **Registradores**: O valor é carregado no registrador **AL** (parte de AX) para a soma, aproveitando a arquitetura x86.
- **Pilha**: Aqui a pilha não é usada, mas funções e chamadas de sistema geralmente interagem com a **stack**.
- **Movimentação de Dados**: A instrução **MOV** move dados entre a memória e os registradores, que é uma operação fundamental para o processador.

---

## Conclusão

A programação em Assembly fornece controle direto sobre o hardware, interagindo com registradores, memória e instruções do processador. Compreender os princípios da **Arquitetura de Computadores** é essencial para dominar Assembler, pois é a base de como as instruções são executadas e como os dados são manipulados no nível mais baixo do sistema.

### exemplos dado em aula
    ; meu primeiro programa em Assembler
    MOV AL,1 ; copia 1 para AL
    MOV BL,2 ; copia 2 para BL
    MOV CL,3 ; copia 3 para CL
    MOV DL,4 ; copia 4 para DL
    MUL DL,BL ; multiplica DL por BL e guarda o resultado DL
    DIV DL,BL ; divide DL por BL e guarda o resultado em DL
    ADD DL,AL ; soma o valor de AL em DL
    SUB DL,AL ; diminui de DL o valor de AL
    END ; finaliza o programa

---

    ; equação x = 3 * (2 - 1)
    MOV AL, 3
    MOV BL, 2
    MOV CL, 1
    SUB BL, CL
    MUL AL, BL

    END

---

    ; equação x = 2 + 4 * (3-1)
    MOV AL, 2
    MOV BL, 4
    MOV CL, 3
    MOV DL, 1
    SUB CL, DL
    MUL BL, CL
    ADD AL, BL

    END