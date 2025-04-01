# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos
# dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.


# PRIMEIRA FORMA DE FAZER
import random

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')


print('\nSegue a ordem de apresentação:\n'
      '{}'.format(random.sample([n1, n2, n3, n4], 4)))

# SEGUNDA FORMA DE FAZER

import random

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

lista = [n1, n2, n3, n4]
random.shuffle(lista)

print('Segue a ordem de apresentação: \n'
      '{}'.format(lista))

