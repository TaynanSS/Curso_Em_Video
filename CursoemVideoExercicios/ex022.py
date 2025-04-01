# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas.
# - O nome com todas minúsculas.
# - Quantas letras ao todo (sem considerar espaços)
# - Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: '))

maiuscula = nome.upper()
minuscula = nome.lower()
primeiro = nome.split()
juntar = ''.join(primeiro)

print('{}\n'
      '{}\n'
      'Quantidade de letras: {}\n'
      'Letras do 1°nome: {}'.format(maiuscula, minuscula, len(juntar), len(primeiro[0])))