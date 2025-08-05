# Faça um programa que leia um número qualquer
# e mostre o seu fatorial.

# EX: 5! = 5x4x3x2x1 = 120

valor = float(input('Digite um valor: '))

fatorial = valor
resultado = 1

print(f'{valor}! = {valor}', end='')
while fatorial != 1:
    resultado *= fatorial
    fatorial -= 1

    print(' *', fatorial, end='')

print(f' = {resultado}')
