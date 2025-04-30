# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

print('Vamos saber se o número é primo?')

num = int(input('Digite um número: '))

if num <= 1:
    print(f'O número {num} não é primo')
else:
    for c in range(2, int(num ** 0.5) + 1):
        primo = True
        if num % c == 0:
            print(f'O número {num} não é primo.')
            break
    else:
        print(f'O número {num} é primo')
