# Crie um programa que leia dois valores e mostre um menu na tela:
from traceback import print_tb

# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso.

valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))


escolha = 0

while escolha != 5:
    print('-' * 5, ' MENU ', '-' * 5)
    print('  [1] Somar\n'
          '  [2] Multiplicar\n'
          '  [3] Maior\n'
          '  [4] Novos números\n'
          '  [5] Sair do programa\n')
    escolha = int(input('Informe sua escolha: '))
    if escolha == 1:
        soma = valor1 + valor2
        print(f'Resultado da soma: {soma}\n')

    if escolha == 2:
        mult = valor1 * valor2
        print(f'Resultado da multiplicação: {mult}\n')

    if escolha == 3:
        if valor1 > valor2:
            maior = valor1
            print(f'O maior valor: {maior}\n')
        else:
            maior = valor2
            print(f'O maior valor: {maior}\n')

    if escolha == 4:
        print('\nInforme novos números abaixo.')
        valor1 = float(input('Digite o primeiro valor: '))
        valor2 = float(input('Digite o segundo valor: '))

    if escolha == 5:
        print('Programa encerrado.')

    else:
        print('Opção inválida. Tente novamente.\n')

# NÃO TEVE MUITA DIFERENÇA ENTRE O MEU E O DO GUANABARA. Logo não irei colocar a versão dele.
