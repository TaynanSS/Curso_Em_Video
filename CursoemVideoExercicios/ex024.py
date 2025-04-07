# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'.

nome = str(input('Digite um nome de uma cidade: ')).strip().split()

#comeca = nome.split()

print(nome[0].lower() == 'santo')
