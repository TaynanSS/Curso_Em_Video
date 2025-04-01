# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
# com 5% de desconto.

preco = float(input('Digite o preço do produto: '))
desc = preco * 5/100
valorF = preco + desc
print('Valor do produto: {}\n'
      'Valor com desconto: {}'.format(preco, valorF))

