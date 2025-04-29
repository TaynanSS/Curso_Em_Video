# Desenvolva um programa que leia seis número inteiros e
# moster a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
for c in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
print(f'O somatório dos números pares digitados: {soma}')