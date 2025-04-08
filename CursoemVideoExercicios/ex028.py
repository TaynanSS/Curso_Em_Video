# Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador

# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

print('Olá, esse programa escolheu um número de 0 a 5. \n'
      'Consegue adivinhar qual foi?')
escolha = input('Escolhe entre 0 a 5: ')

if escolha.isalpha():
    print('Por favor digite um número.')

else:
    escolha = int(escolha)
    if escolha > 5:
        print('Você digitou um número maior que 5')
    else:
        if escolha < 0:
            print('Você digitou um número menor que 0')
        else:
            lista = [0,1,2,3,4,5]
            escolhido = random.choice(lista)
            if escolha == escolhido:
                print('Você acertou!')
                print('O número escolhido pelo programa foi {}'.format(escolhido))
            else:
                print('Você errou')
                print('O número escolhido pelo programa foi {}'.format(escolhido))
