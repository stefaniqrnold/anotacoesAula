**• Declaração de Variáveis**
○ Não é necessário declarar o tipo
x = 10
y = "Hello"

**Strings**
nome = "Maria"
saudacao = 'Olá, mundo!'

**• Operações com Strings**
mensagem = "Python " + "é incrível!"

**• Métodos de Strings**
frase = "Python é poderoso"
print(frase.upper()) # PYTHON É PODEROSO
print(frase.lower()) # python é poderoso

**• Listas (coleções ordenadas e mutáveis de itens em Python.)**
lista = [1, 2, 3, 4, 5]

**• Criando e Acessando Listas**
frutas = ["maçã", "banana", "laranja"]
print(frutas) # Saída: ['maçã', 'banana', 'laranja']
print(frutas[1]) # Saída: banana

**• Iterando Sobre Listas**
for fruta in frutas:
print(fruta)

**• Adicionando e Removendo Itens**
frutas.append("manga") # Adiciona 'manga' ao final da lista
print(frutas) # Saída: ['maçã', 'banana', 'laranja', 'manga']

frutas.remove("banana") # Remove o item 'banana' da lista
print(frutas) # Saída: ['maçã', 'laranja', 'manga']

**• Modificando Itens**
frutas[0] = "pera" # Modifica o primeiro item da lista
print(frutas) # Saída: ['pera', 'laranja', 'manga']

**• Tuplas (estruturas de dados imutáveis. Útil para armazenar coleções de itens que não devem mudar.)**
tupla = (1, 2, 3, 4, 5)

**• Acessando Elementos**
primeiro_elemento = tupla[0]
ultimo_elemento = tupla[-1] # retorna o ultimo item da lista

**• Iterando sobre Tuplas**
for elemento in tupla:
print(elemento)

**• Dicionários (estruturas de dados mutáveis que armazenam pares chave-valor. Ideal para associações e buscas rápidas.)**

**• Definição**
dicionario = {
'nome': 'Ana',
'idade': 30,
'cidade': 'São Paulo'
}

**• Acessando Valores**
nome = dicionario['nome']
idade = dicionario['idade']

**• Adicionando e Modificando Itens**
dicionario['profissao'] = 'Engenheira'
dicionario['idade'] = 31

**• Manipulação de Dicionários**
dicionario = {"nome": "Carlos", "idade": 28}
dicionario["idade"] = 29 # Atualiza o valor

**• Removendo Itens**
del dicionario['cidade']

**• Iterando sobre Dicionários**
for chave, valor in dicionario.items():
print(f"{chave}: {valor}")

**• Operadores**
soma = 5 + 3
subtracao = 5 - 3
multiplicacao = 5 * 3
divisao = 5 / 2

**• Comparações**
igual = (5 == 5) # True
diferente = (5 != 3) # True
maior = (5 > 3) # True

**• If, Elif, Else**
1. idade = 18
2. if idade >= 18:
3. print("Adulto")
4. elif idade >= 13:
5. print("Adolescente")
6. else:
7. print("Criança")

**• Laço For**
for i in range(5):
print(i)

**• Laço While**
contador = 0
while contador < 5:
print(contador)
contador += 1

**• Definindo Funções**
def saudacao(nome):
return f"Olá, {nome}!"

**• Chamando Funções**
mensagem = saudacao("João")
print(mensagem)

**• Simulação de Switch-Case**
Diferente de outras linguagens, Python não possui a estrutura switch-case.
Podemos usar dicionários para simular um comportamento semelhante.

**• Simulação de Switch-Case**
1. def executar_acao(acao):
2. acoes = {
3. 1: "Ação 1: Iniciar",
4. 2: "Ação 2: Parar",
5. 3: "Ação 3: Pausar",
6. 4: "Ação 4: Reiniciar"
7. }
8. return acoes.get(acao, "Ação Inválida")
9.
10. codigo_acao = int(input("Digite o código da ação (1-4): "))
11. resultado = executar_acao(codigo_acao)
12. print(resultado)

**• Simulação de Switch-Case**
1. def executar_acao(acao):
2. acoes = {
3. 1: "Ação 1: Iniciar",
4. 2: "Ação 2: Parar",
5. 3: "Ação 3: Pausar",
6. 4: "Ação 4: Reiniciar"
7. }
8. return acoes.get(acao, "Ação Inválida")
9.
10. codigo_acao = int(input("Digite o código da ação (1-4): "))
11. resultado = executar_acao(codigo_acao)
12. print(resultado)

Dicionário acoes: Define as possíveis ações associadas a códigos.
Método get: Retorna a ação correspondente ao código inserido ou uma mensagem de "Ação Inválida" se o código não for encontrado.

## aula 14/08/24

• Tratamento de Exceções
try:
    resultado = 10 / 0
 except ZeroDivisionError:
    print("Não é possível dividir por zero!")

• Importando Módulos
import math
print(math.sqrt(16)) # 4.0

• Criando Módulos
Salve funções em um arquivo .py e importe usando "import nome_arquivo"

• Operador Ternário
# utilizado quando precisamos usar estruturas muito simples
idade = 16
tipo = "adulto" if idade >= 18 else "menor"

• Funções com Valores Default
○ List Comprehensions
    def saudacao(nome, saudar=True):
        if saudar:
            return f"Olá, {nome}!"
        else:
            return f"Até logo, {nome}!"

• Uso de Lambdas
- Uma função lambda é uma pequena função anônima em Python. Elas são definidas usando a palavra-chave lambda e podem ter qualquer número de argumentos, mas apenas uma expressão.
- A expressão é avaliada e retornada.
- Funções lambda são usadas quando uma função *pequena e descartável* é necessária, geralmente para operações simples.
# usada para otimização de codigo, após execução os arquivos de código são descartados

• Uso de Lambdas
quadrado = lambda x: x ** 2
print(quadrado(5)) # 25

• Abrindo e Lendo Arquivos
with open(*'nome_do_arquivo', 'modo'*) as variavel_arquivo:
    # Operações com o arquivo
    *nome_do_arquivo*: O caminho para o arquivo que você deseja abrir.
    *modo*: O modo em que você deseja abrir o arquivo.
        r: leitura (padrão).
        w: escrita (cria um novo arquivo ou sobrescreve o existente).
        a: acrescentar (adiciona ao final do arquivo).
        b: modo binário.
        t: modo texto (padrão).

• Abrindo e Lendo Arquivos
    with open('arquivo.txt', 'r') as file:
        conteudo = file.read()
    print(conteudo)

• Escrevendo em Arquivos
  ○ Gravando Dados em Arquivos
    with open('arquivo.txt', 'w') as file:
      file.write("Texto para o arquivo.")

• Iterações Avançadas
    ○ List Comprehensions
    Uma compreensão de lista é uma construção sintática disponível em algumas linguagens de programação para criação de uma lista baseada em listas existentes.
    A sintaxe é simples e pode incluir condições para filtrar itens.
    List comprehensions são uma maneira concisa e eficiente de criar listas em Python.
    Elas permitem a criação de uma nova lista aplicando uma expressão a cada item de uma sequência ou iterável e, opcionalmente, incluindo uma condição para filtrar itens.

• Exemplo Avançado
    pares = [x for x in range(20) if x % 2 == 0]
    Saída: pares = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

- range(20): Esta função gera uma sequência de números de 0 a 19.
- x for x in range(20): Este é o loop que itera  sobre cada item da sequência gerada pelo range(20).
- if x % 2 == 0: Esta é a condição que filtra os itens da sequência.
- Apenas os números que satisfazem esta condição (números pares) são incluídos na nova lista.
- [x for x in range(20) if x % 2 == 0]: Esta é a list comprehension completa. Para cada x na sequência de 0 a 19, se x for par (ou seja, x % 2 == 0), então x é adicionado à lista pares.

• Iterações Avançadas
○ List Comprehensions
■ quadrados = [x**2 for x in range(10)]
● range(10): Esta função gera uma sequência de números de 0
a 9.
● x**2: Esta é a expressão aplicada a cada item da sequência.
Neste caso, estamos elevando cada número ao quadrado.
● for x in range(10): Este é o loop que itera sobre cada item da
sequência gerada pelo range(10).
● Resultado: quadrados = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

• Uso de Funções como Argumentos
■ def aplicar_funcao(funcao, lista):
■ return [funcao(x) for x in lista]
■
■ resultado = aplicar_funcao(lambda x: x * 2, [1, 2, 3])

• Uso de Geradores
○ Geradores são uma forma de criar iteradores de maneira fácil e eficiente.
○ Semelhantes às funções normais,
1. Usar return para retornar um valor e finalizar a execução da função
2. Usam yield para produzir um valor e pausar a execução, mantendo o estado da função.

○ A execução pode ser retomada de onde foi interrompida na próxima iteração.

• Uso de Geradores
1. def contador(max):
2.  n = 0
3.  while n < max:
4.      yield n
5.      n += 1
6.
7. for numero in contador(5):
8.  print(numero)

• Uso de Geradores

1. def contador(max):
2.  n = 0
3.  while n < max:
4.      yield n
5.      n += 1
6.
7. for numero in contador(5):
8.  print(numero)
Saída:
0
1
2
3
4