"""• Crie um programa, em Python, que simula uma lista de mercado.
O programa deverá:
Receber os itens da compra, incluindo o código do produto e a quantidade.
Calcular os valores com base no código e quantidade do produto.
Receber a forma de pagamento, incluindo o código de pagamento e a quantidade de parcelas.
Mostrar o valor final, adicionando juros de 1,5% ao mês caso o pagamento seja parcelado em 3 vezes.
Simulação de Switch-Case utilizando um dicionário para simular um comportamento de switch-case na seleção da forma de pagamento."""

# Passos da Atividade
# 1. Cadastro de Produtos
# Crie um dicionário para pré-cadastrar 20 produtos com seus respectivos códigos e preços.
# O dicionário deve seguir a estrutura:
# {codigo: {'nome': 'nome_produto', 'preco': preco_produto}}

# 2. Recebendo os Itens da Compra
# Solicite ao usuário que insira o código do produto e a quantidade desejada.○ Continue pedindo até que o usuário insira o código 0 para 
# finalizar a compra. Armazene os itens da compra em uma lista de tuplas, onde cada tupla contém o código do produto e a quantidade comprada.

# 3. Exibindo os Itens da Compra
# Itere sobre a lista de itens da compra e exiba o nome do produto, a quantidade e o valor total (preço unitário multiplicado pela quantidade).

# 4. Calculando o Valor Total da Compra
# Calcule o valor total da compra somando o preço de cada item (preço unitário multiplicado pela quantidade) presente na lista de compra.

# 5. Recebendo a Forma de Pagamento com Switch-Case
#Solicite ao usuário que insira o código da forma de pagamento:
"""1 para à vista,
2 para parcelado em 2 vezes,
3 para parcelado em 3 vezes."""
# Utilize um dicionário para simular um comportamento de switch-case na seleção da forma de pagamento. 
# Determine a quantidade de parcelas com base no código inserido.

# 6. Calculando e Exibindo o Valor Final
# Se o pagamento for parcelado em 3 vezes, adicione um juros de 1,5% ao mês sobre o valor total.
# Exiba o valor final da compra.
# Se o pagamento for parcelado, exiba também o valor de cada parcela.

"""Requisitos Técnicos
● Utilize estruturas de controle como while e if-elif-else.
● Manipule listas e dicionários para armazenar e processar os dados.
● Realize operações aritméticas para calcular o valor total da compra e os juros para
pagamento parcelado.
● Utilize um dicionário para simular um comportamento de switch-case."""