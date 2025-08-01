# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
# em um número entre 0 e 10. Só que agora o jogador vai tentar
# adivinhar até acertar, mostrando no final quantos palpites
# foram necessário para vencer.

from random import randint
from time import sleep

computador = randint(0, 10)

print('-=-' * 24)
print('Olá, vou pensar em um número entre 0 e 10. Consegue adivinhar qual foi?')
print('-=-' * 24 + '\n')

escolha = 0
cont = 0
while escolha != computador:
    escolha = int(input('Escolha um número entre 0 e 10: '))
    if 0 > escolha > 10 :
        print('Escolha um valor entre 0 e 10')
    elif escolha == computador:
        print('\n' + '-=-' * 10)
        print('Você acertou!')
        print('-=-' * 10)
        print(f'Eu escolhi o número {escolha}')
        print('-=-' * 10)
    else:
        print('\n' + '-=-' * 10)
        print('Você errou!')
        print('-=-' * 10)
        print(f'HAHA!! Eu escolhi um número diferrente. Tente de Novo!!!')
        print('-=-' * 10)

    cont += 1

print(f'Você acertou em {cont} tentativas.')