# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

primeirot = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

for c in range(10):
    termo = primeirot + c * razao
    print(termo)