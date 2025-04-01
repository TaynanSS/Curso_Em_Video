# Escreva um programa que pergunte a quantidade de Km
# percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
# custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Informe a quantidade de dias alugados: '))
km = float(input('Informe a quantidade de km percorridos: '))

pdias = dias * 60
pkm = 0.15 * km
valor = pdias + pkm
print('\n{} dias alugados (R$60/dia)\n'
      '{}km rodados (R$0,15/km)\n'
      'Total a pagar: {:.2f}'.format(dias, km, valor))