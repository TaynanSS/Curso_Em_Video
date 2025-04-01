# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos Dólares ela pode comprar.
# Considere US$1.00 = R$3.27

valor = float(input('Quanto você tem na carteira? -> '))
valor1 = float(input('Dolar: '))
dolar = 3.27
conv = valor / dolar
conv1 = dolar * 3.27
print('Com seu dinheiro atual, você poderá comprar {} em dólares.'.format(conv))
print('valor do dolar em real: {}'.format(conv1))
