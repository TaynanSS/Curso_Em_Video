# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

num = input('Digite um número: ')

if num.isalpha():
    print('Não foi digitado um número. Por favor digite um número inteiro.')
else:
    num = int(num)
    par = num % 2
    if par == 0:
        print('O número digitado é par')
    else:
        print('O número digitado é impar')