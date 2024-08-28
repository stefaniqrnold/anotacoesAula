# operador ternário
"""idade = int(input("informe sua idade:\n> "))
tipo = "adulto" if idade >= 18 else "menor de idade"
print(f"você é {tipo}")

def saudacao(nome, saudar = True):
    if saudar:
        return f"olá, {nome}"
    else:
        return f"Adeus, {nome}"
retorno = saudacao("Stefani")
print(retorno)

# função lambda
quadrado = lambda x: x ** 2
valor = int(input("Qual número deseja calcular o quadrado?\n > "))
print(quadrado(valor)) # 25

# abrindo e lendo arquivos
with open('arquivo.txt', 'r') as file:
    conteudo = file.read()
print(conteudo)

# escrevendo em arquivos
with open('arquivo.txt', 'a') as file:
      file.write("batata.")
with open('arquivo.txt', 'r') as file:
    conteudo = file.read()
print(conteudo)

# iterações avançadas
n = int(input("até que valor vamos verificar os pares?\n> "))
pares = [x for x in range(n) if x % 2 == 0]
print(f"os pares até {n} são: {pares}")
"""
# uso de geradores
a = int(input('Enter 1st number: '))
def contador(max):
    n = 0
    while n < max:
        yield n
        n += a

for numero in contador(5):
    print(numero)
    
