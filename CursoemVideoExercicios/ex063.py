# Escreva um programa que leia um número n inteiro qualquer
# e mostre na tela os n primeiros elementos de uma
# Sequência de Fibonacci.

# EX: 0 -> 1 -> 2 -> 3 -> 5 -> 8

print('='* 5, 'SEQUÊNCIA DE FIBONACCI', '='* 5)

user = int(input('Quantidade de elementos da sequência [informe em inteiros]: '))

cont = 0
primeiro = 0
segundo = 1

while cont != user:
    print(f'{cont + 1}°: {primeiro}')

    proximo = primeiro + segundo
    primeiro = segundo
    segundo = proximo
    cont += 1

