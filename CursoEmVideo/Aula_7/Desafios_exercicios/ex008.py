# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

met = float(input('Digite um valor em metros: '))
cent = met * 100
mili =  met * 1000
print('Valor digitado em centímetros: {} \nValor digitado em milímetros: {}'.format(cent, mili))
