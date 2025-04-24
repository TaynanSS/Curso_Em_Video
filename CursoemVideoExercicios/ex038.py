# Escreva um programa que leia dois números inteiros e compare-os,
# mostrando na tela a mensagem:

# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o Segundo valor: '))

if valor1 > valor2:
    print(f'O primeiro valor é maior.\nValor digitado: {valor1}')
elif valor2 > valor1:
    print(f'O segundo valor é maior.\nValor digitado: {valor2}')
else:
    print('Não existe valor maior, os dois são iguais.')