# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year
maior = 0
menor = 0

for c in range(0, 7):
    ano = int(input('Digite seu ano de nascimento: '))
    idade = atual - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
if maior == 0:
    print('\n' + f'Há {menor} menores de idade.')
    print('Não há nenhum maior de idade!')
elif menor == 0:
    print('\n' + f'Há {maior} maiores de idade.')
    print('Não há nenhum menor de idade.')
else:
    print('\n' + f'Há {menor} menores de idade.')
    print(f'Há {maior} maiores de idade.')
