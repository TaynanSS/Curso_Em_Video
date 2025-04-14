# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

num = input('Digite um número: ')

if num.isalpha():
    print('Não foi digitado um número. Por favor digite um número inteiro.')
else:
    num = int(num)
    if num % 2 == 0:
        print('O número digitado é par')
    else:
        print('O número digitado é ímpar')