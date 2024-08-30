"""
# questao 2
A = int(input())
B = int(input())

X = A + B

print(f"X = {X}")

# questao 3
r = float(input())
pi = float(3.14159)

# round(numero, casas)
## funcao round arredonda um numero ate tantas casas decimais
A = round((r**(2)*pi), 4)

# :.4f -> coisa de formatacao do python
print(f"A={A:.4f}")

# questao 4
A = int(input())
B = int(input())

SOMA = A + B

print(f"SOMA = {SOMA}")

# Produto Simples
A = int(input())
B = int(input())

PROD = A * B

print(f"PROD = {PROD}")

# Média 1
A = float(input())
B = float(input())

MEDIA = (A * 3.5 + B * 7.5)/11

print(f"MEDIA = {MEDIA:.5f}")

# Média 2
A = float(input())
B = float(input())
C = float(input())

MEDIA = (A * 2 + B * 3 + C * 5)/10

print(f"MEDIA = {MEDIA:.1f}")

# Diferença
A = int(input())
B = int(input())
C = int(input())
D = int(input())

DIFERENCA = (A * B - C * D)

print(f"DIFERENCA = {DIFERENCA}") 
horas = int(input())
valorHora = float(input())

salario = horas * valorHora

print(f"NUMBER = {numero}")
print(f"SALARY = U$ {salario:.2f}")

# Salário com Bônus
nome = input()
salario = float(input())
vendas = float(input())

total = salario + vendas * 0.15

print(f"TOTAL = R$ {total:.2f}")

# Cálculo Simples
a = list(map(float, input().split(" ")))
b = list(map(float, input().split(" ")))

result = a[1] * a[2] + b[1] * b[2]

print(f"VALOR A PAGAR: R$ {result:.2f}")

# Esfera
r = float(input())
pi = float(3.14159)

# round(numero, casas)
## funcao round arredonda um numero ate tantas casas decimais
v = round((4/3.0) * pi * r**3, 3)

# :.4f -> coisa de formatacao do python
print(f"VOLUME = {v:.3f}")

# Área
lista = list(map(float, input().split(" ")))
a = lista[0]
b = lista[1]
c = lista[2]
pi = 3.14159

triangulo = a * c / 2
circulo = pi * (c ** 2)
trapezio = ((a + b)/2) * c
quadrado = b ** 2
retangulo = a * b

print(f"TRIANGULO: {triangulo:.3f}\nCIRCULO: {circulo:.3f}\nTRAPEZIO: {trapezio:.3f}\nQUADRADO: {quadrado:.3f}\nRETANGULO: {retangulo:.3f}")

# O Maior
lista = list(map(int, input().split(" ")))
a = lista[0]
b = lista[1]
c = lista[2]

maiorAB = (a + b + abs(a - b)) / 2
maiorABC = int((maiorAB + c + abs(maiorAB - c)) / 2)

print(f"{maiorABC} eh o maior")

# Consumo
x = int(input())
y = float(input())

consumo = round(x/y, 3)

print(f"{consumo} km/l")

# Distância Entre Dois Pontos
import math
lista1 = list(map(float, input().split(" ")))
lista2 = list(map(float, input().split(" ")))

x1 = lista1[0]
y1 = lista1[1]
x2 = lista2[0]
y2 = lista2[1]

distancia = math.sqrt(((x2 - x1)**2) + (y2 - y1)**2)

print(f"{distancia:.4f}")

# Distância
distancia = int(input())
tempoMin = int((distancia / 30) * 60)
print(f"{tempoMin} minutos")

# Gasto de Combustível
tempo = int(input())
velocidade = int(input())

gasto = (tempo * velocidade)/12

print(f"{gasto:.3f}")

# Cédulas
valor = int(input())
qtdd100 = int(valor/100)
qtdd50 = int((valor % 100)/50)
qtdd20 = int(((valor % 100) % 50)/20)
qtdd10 = int((((valor % 100) % 50) % 20)/10)
qtdd5 = int(((((valor % 100) % 50) % 20) % 10)/5)
qtdd2 = int((((((valor % 100) % 50) % 20) % 10) % 5)/2)
qtdd1 = int((((((valor % 100) % 50) % 20) % 10) % 5) % 2)

print(f"{valor}\n{qtdd100} nota(s) de R$ 100,00\n{qtdd50} nota(s) de R$ 50,00\n{qtdd20} nota(s) de R$ 20,00\n{qtdd10} nota(s) de R$ 10,00\n{qtdd5} nota(s) de R$ 5,00\n{qtdd2} nota(s) de R$ 2,00\n{qtdd1} nota(s) de R$ 1,00")

# Conversão de Tempo
tempo = int(input())
horas = int(tempo/3600)
minutos = int((tempo % 3600)/60)
segundos = int((tempo % 3600) % 60)

print(f"{horas}:{minutos}:{segundos}")

# Idade em Dias
tempo = int(input())
anos = int(tempo/365)
meses = int((tempo % 365)/30)
dias = int((tempo % 365) % 30)

print(f"{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)")

# Notas e Moedas -> refazer com dicionario
valor = float(input())
qtdd100 = int(valor/100)
qtdd50 = int((valor % 100)/50)
qtdd20 = int(((valor % 100) % 50)/20)
qtdd10 = int((((valor % 100) % 50) % 20)/10)
qtdd5 = int(((((valor % 100) % 50) % 20) % 10)/5)
qtdd2 = int((((((valor % 100) % 50) % 20) % 10) % 5)/2)

qtdd1 = int((((((valor % 100) % 50) % 20) % 10) % 5) % 2)
qtdd050 = int((((((((valor % 100) % 50) % 20) % 10) % 5) % 2) % 1)/0.50)
qtdd025 = int((((((((valor % 100) % 50) % 20) % 10) % 5) % 2) % 0.50)/0.25)
qtdd010 = int(((((((((valor % 100) % 50) % 20) % 10) % 5) % 2) % 0.50) % 0.25)/0.10)
qtdd005 = int((((((((((valor % 100) % 50) % 20) % 10) % 5) % 2) % 0.50) % 0.25) % 0.10)/0.05)
qtdd001 = int(((((((((((valor % 100) % 50) % 20) % 10) % 5) % 2) % 0.50) % 0.25) % 0.10) % 0.05)/0.01)

# print(f"NOTAS:
{qtdd100} nota(s) de R$ 100.00
{qtdd50} nota(s) de R$ 50.00
{qtdd20} nota(s) de R$ 20.00
{qtdd10} nota(s) de R$ 10.00
{qtdd5} nota(s) de R$ 5.00
{qtdd2} nota(s) de R$ 2.00
MOEDAS:
{qtdd1} moeda(s) de R$ 1.00
{qtdd050} moeda(s) de R$ 0.50
{qtdd025} moeda(s) de R$ 0.25
{qtdd010} moeda(s) de R$ 0.10
{qtdd005} moeda(s) de R$ 0.05
{qtdd001} moeda(s) de R$ 0.01")

# Teste de Seleção 1
lista = list(map(int, input().split(" ")))
a = lista[0]
b = lista[1]
c = lista[2]
d = lista[3]

if b > c and d > a and (c + d) > (a + b) and c >= 0 and d >= 0 and a % 2 == 0:
      print("Valores aceitos")
else:
    print("Valores nao aceitos")

# Fórmula de Bhaskara
import math

lista = list(map(float, input().split(" ")))
a = lista[0]
b = lista[1]
c = lista[2]

delta = (b ** 2) - (4 * a * c)

# print(math.sqrt(delta))
# print(delta)
if a == 0 or delta < 0:
    print("Impossivel calcular")
else:
    x1 = (- b + (math.sqrt(delta))) / (2 * a)
    x2 = (- b - (math.sqrt(delta))) / (2 * a)
    print(f"R1 = {x1:.5f}\nR2 = {x2:.5f}")

# Intervalo
valor = float(input())

if 0 <= valor <= 25:
    print("Intervalo [0,25]")
    
elif 25 < valor <= 50: 
    print("Intervalo (25,50]")
    
elif 50 < valor <= 75:
    print("Intervalo (50,75]")
    
elif 75 < valor <= 100:
    print("Intervalo (75,100]")
    
else:
    print("Fora de intervalo")
"""