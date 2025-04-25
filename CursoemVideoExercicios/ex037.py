# Escreva um programa que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de conversão:

# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

num = int(input('Digite um número inteiro: '))

print('Escolha a opção que deseja converter o número digitado.\n'
      'Binário => 1\n'
      'Octal => 2\n'
      'Hexadecimal => 3\n')

escolha = int(input('Digite a opção desejada: '))

if escolha == 1:
    print(f'O número {num} em binário é => {bin(num)[2:]}') # O [2:] irá fatiar e fazer com que inicie a partir da 3°posição.
elif escolha == 2:
    print(f'O número {num} em octal é => {oct(num}[2:]')
elif escolha == 3:
    print(f'O número {num} em hexadecimal é => {hex(num)[2:]}') 
else:
    print('Digite um número dentre as opções.')
