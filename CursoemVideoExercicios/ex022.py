# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas.
# - O nome com todas minúsculas.
# - Quantas letras ao todo (sem considerar espaços)
# - Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip() # Já cortará os espaços antes e depois do nome escrito.

maiuscula = nome.upper()
minuscula = nome.lower()
primeiro = nome.split()
juntar = len(''.join(primeiro))

#OUTRA FORMA DE FAZER

#juntar = len(nome) - nome.count(' ')

print('{}\n'
      '{}\n'
      'Quantidade de letras: {}\n'
      'Letras do 1°nome: {}'.format(maiuscula, minuscula, juntar, len(primeiro[0])))

# OUTRA FORMA DE FAZER O "Quantas letras tem o primeiro nome."

print('Há {} no primeiro nome'.format(nome.find(' ')))
#Irá encontrar a posição que está o primeiro ESPAÇO,
#mas só irá funcionar se tiver o STRIP na variável de entrada NOME
# nome = str(input('Digite seu nome completo: ')).strip()
