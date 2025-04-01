# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
# com 5% de desconto.

preco = float(input('Qual valor do produto? R$'))
desc = preco * 5/100
valorF = preco - desc
print('Valor do produto: R${}\n'
      'Valor com desconto: R${:.2f}'.format(preco, valorF))

