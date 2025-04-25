# Crie um programa que faça o computador jogar JOKENPO com você.

import random

print('Vamos jogar JOKEMPO?')

escolha = str(input('Escolha entre pedra, papel ou tesoura: ')).upper().strip()

lista = ['PEDRA', 'PAPEL', 'TESOURA']
maquina = random.choice(lista)

if escolha == maquina:
    print(f'EMPATE!\nOs dois escolheram {escolha}')
elif escolha == 'PEDRA' and maquina != 'PAPEL':
    print('O jogador venceu.\nEscolheu a PEDRA\nMáquina escolheu a TESOURA')
elif escolha == 'PAPEL' and maquina != 'TESOURA':
    print('O jogador venceu.\nEscolheu o PAPEL.\nMáquina escolheu a PEDRA')
elif escolha == 'TESOURA' and maquina != 'PEDRA':
    print('O jogador venceu.\nEscolheu a TESOURA.\nMáquina escolheu o PAPEL')
else:
    print(f'Máquina venceu.\nEscolheu {maquina}.\nJogador escolheu {escolha}')