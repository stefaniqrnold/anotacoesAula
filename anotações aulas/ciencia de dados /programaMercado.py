# Passo 1: Cadastro de Produtos
produtos = {
    101: {'nome': 'Arroz', 'preco': 20.00},
    102: {'nome': 'Feijão', 'preco': 10.00},
    103: {'nome': 'Açúcar', 'preco': 5.00},
    104: {'nome': 'Óleo', 'preco': 7.50},
    105: {'nome': 'Sal', 'preco': 2.50},
    106: {'nome': 'Café', 'preco': 12.00},
    107: {'nome': 'Leite', 'preco': 4.00},
    108: {'nome': 'Farinha', 'preco': 6.00},
    109: {'nome': 'Manteiga', 'preco': 8.00},
    110: {'nome': 'Carne', 'preco': 30.00}
}

# Passo 2: Receber os itens da compra
compra = []
while True:
    codigo = int(input("Digite o código do produto (0 para finalizar): "))
    if codigo == 0:
        break
    if codigo in produtos:
        quantidade = int(input(f"Digite a quantidade de {produtos[codigo]['nome']}: "))
        compra.append((codigo, quantidade))
    else:
        print("Código inválido.")

# Passo 3: Exibir os itens da compra
print("\nItens da compra:")
valor_total = 0
for item in compra:
    codigo, quantidade = item
    nome = produtos[codigo]['nome']
    preco_unitario = produtos[codigo]['preco']
    preco_total = preco_unitario * quantidade
    print(f"{nome} - {quantidade} unidades - R${preco_total:.2f}")
    valor_total += preco_total

print(f"Valor total da compra: R${valor_total:.2f}")

# Passo 4: Receber a forma de pagamento
forma_pagamento = int(input("Digite o código da forma de pagamento (1 - à vista, 2 - 2x, 3 - 3x): "))

# Passo 5: Simular switch-case para forma de pagamento
pagamento_opcoes = {
    1: ("à vista", 1, 0),  # Sem parcelas e sem juros
    2: ("parcelado em 2 vezes", 2, 0),  # 2x sem juros
    3: ("parcelado em 3 vezes", 3, 0.015)  # 3x com 1.5% de juros ao mês
}

if forma_pagamento in pagamento_opcoes:
    descricao, parcelas, juros_mensal = pagamento_opcoes[forma_pagamento]
    
    if parcelas == 3:
        valor_final = valor_total * (1 + juros_mensal * 3)  # Juros sobre 3 meses
    else:
        valor_final = valor_total
    
    print(f"Forma de pagamento: {descricao}")
    print(f"Valor final da compra: R${valor_final:.2f}")
    
    if parcelas > 1:
        valor_parcela = valor_final / parcelas
        print(f"Pagamento em {parcelas}x de R${valor_parcela:.2f}")
else:
    print("Forma de pagamento inválida.")
