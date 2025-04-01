# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
# e o último nome separamente.
#Ex:
# Ana Maria de Souza
# primeiro = Ana
# último = Souza

nome = input('Escreva seu nome completo: ')

primeiro = nome.split()
ultimo = nome.split()


print('Primeiro: {}\n'
      'Último: {}'.format(primeiro[0], ultimo[-1]))
