# Crie um programa que faça o computador jogar JOKENPO com você.

from random import choice
from time import sleep

print('Vamos jogar JOKEMPO?')

escolha = str(input('Escolha entre pedra, papel ou tesoura: ')).upper().strip()
print('Pedra')
sleep(1)
print('Papel')
sleep(1)
print('Tesoura!!!')

lista = ['PEDRA', 'PAPEL', 'TESOURA']
maquina = choice(lista)

if escolha == maquina:
    print(f'EMPATE!\nOs dois escolheram {escolha}')
elif escolha == 'PEDRA' and maquina != 'PAPEL':
    print('O JOGADOR VENCEU.\nEscolheu a PEDRA\nMáquina escolheu a TESOURA')
elif escolha == 'PAPEL' and maquina != 'TESOURA':
    print('O JOGADOR VENCEU.\nEscolheu o PAPEL.\nMáquina escolheu a PEDRA')
elif escolha == 'TESOURA' and maquina != 'PEDRA':
    print('O JOGADOR VENCEU.\nEscolheu a TESOURA.\nMáquina escolheu o PAPEL')
else:
    print(f'MÁQUINA VENCEU.\nEscolheu {maquina}.\nJogador escolheu {escolha}')


# FORMA DE FAZER PASSADA PELO GUANABARA

from random import randint

print('Vamos jogar JOKEMPO?')
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

jogador = int(input('Escolha entre pedra, papel ou tesoura: '))

print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
