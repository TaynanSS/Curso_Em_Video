# Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador

# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep

print('-=-' * 24)
print('Olá, vou pensar em um número entre 0 e 5. Consegue adivinhar qual foi?')
print('-=-' * 24 + '\n')

escolha = input('Escolha um número entre 0 a 5: ')

print('\nPROCESSANDO...')
sleep(2)

if escolha.isalpha():
    print('\n' + '-=-' * 13)
    print('Acha que me engana?\n'
          'Eu pedi um número e não uma letra ><" ')
    print('-=-' * 13)

else:
    escolha = int(escolha)
    if escolha > 5:
        print('Você digitou um número maior que 5')
    else:
        if escolha < 0:
            print('Você digitou um número menor que 0')
        else:
            lista = [0,1,2,3,4,5] # Criei uma lista com os números
            escolhido = random.choice(lista) # Fiz escolher um número da lista.
            if escolha == escolhido:
                print('\n'+'-=-' * 10)
                print('Você acertou!')
                print('-=-' * 10)
                print('Eu escolhi o número {}'.format(escolhido))
                print('-=-' * 10)
            else:
                print('\n'+'-=-' * 10)
                print('Você errou!')
                print('-=-' * 10)
                print('HAHA!! Eu escolhi o número {}'.format(escolhido))
                print('-=-' * 10)

# OUTRA FORMA DE FAZER

from random import randint
from time import sleep

computador = randint(0, 5) # Faz o computador "Pensa" entre os números indicados.

print('-=-' * 24)
print('Olá, vou pensar em um número entre 0 e 5. Consegue adivinhar qual foi?')
print('-=-' * 24 + '\n')

escolha = input('Escolha um número entre 0 a 5: ')

print('\nPROCESSANDO...')
sleep(2) # Faz o programa demorar 2 segundos para passar para próxima linha de comando.

if escolha.isalpha():
    print('\n' + '-=-' * 13)
    print('Acha que me engana?\n'
          'Eu pedi um número e não uma letra ><" ')
    print('-=-' * 13)

else:
    escolha = int(escolha)
    if escolha > 5:
        print('Você digitou um número maior que 5')
    else:
        if escolha < 0:
            print('Você digitou um número menor que 0')
        else:
            if escolha == computador:
                print('\n' + '-=-' * 10)
                print('Você acertou!')
                print('-=-' * 10)
                print('Eu escolhi o número {}'.format(escolhido))
                print('-=-' * 10)
            else:
                print('\n' + '-=-' * 10)
                print('Você errou!')
                print('-=-' * 10)
                print('HAHA!! Eu escolhi o número {}'.format(escolhido))
                print('-=-' * 10)

