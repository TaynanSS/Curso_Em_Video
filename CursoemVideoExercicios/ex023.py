# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Ex: Digite um número: 1834
# Unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

num = str(input('Digite um número de 0 a 9999: ')).zfill(4) # Na própria entrada do usuário irá garantir que sempre haja 4 caracteres, preenchendo com zeros à esquerda.

unidade = num[3]
dezena = num[2]
centena = num[1]
milhar = num[0]


print('Unidade: {}\n'
      'Dezena: {}\n'
      'Centena: {}\n'
      'Milhar: {}'.format(unidade, dezena, centena, milhar))

# Se for como INT?
'''
num = int(input('Digite um número de 0 a 9999: '))

num_str = str(num)

num_str = num_str.zfill(4)  # Garante sempre 4 caracteres, preenchendo com zeros à esquerda.

unidade = num_str[3]
dezena = num_str[2]
centena = num_str[1]
milhar = num_str[0]

print('Unidade: {}\n'
      'Dezena: {}\n'
      'Centena: {}\n'
      'Milhar: {}'.format(unidade, dezena, centena, milhar))
'''
