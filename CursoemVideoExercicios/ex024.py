# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'.

nome = input('Digite um nome de uma cidade: ')

comeca = nome.split()

print('Santo' in comeca[0])