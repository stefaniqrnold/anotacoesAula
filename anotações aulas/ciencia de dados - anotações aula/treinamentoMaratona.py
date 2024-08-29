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
"""
# Cálculo Simples
a = list(map(float, input().split(" ")))
b = list(map(float, input().split(" ")))

result = a[1] * a[2] + b[1] * b[2]

print(f"VALOR A PAGAR: R$ {result:.2f}")
