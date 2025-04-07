# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
# e o último nome separamente.
#Ex:
# Ana Maria de Souza
# primeiro = Ana
# último = Souza

nome = str(input('Escreva seu nome completo: ')).strip().split()

print('Primeiro nome: {}\n'
      'Último nome: {}'.format(nome[0], nome[-1]))

# OUTRA FORMA

print('Primeiro nome: {}\n'
      'Último nome: {}'.format(nome[0], nome[len(nome)-1]))
