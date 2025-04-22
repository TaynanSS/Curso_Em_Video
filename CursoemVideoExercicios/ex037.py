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
    bina = bin(num)
    print(f'O número {num} em binário é => {bina}')
elif escolha == 2:
    octal = oct(num)
    print(f'O número {num} em octal é => {octal}')
elif escolha == 3:
    hexa = hex(num)
    print(f'O número {num} em hexadecimal é => {hexa}')
else:
    print('Digite um número dentre as opções.')