# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input('Digite um número inteiro: '))
ant = num - 1
suc = num + 1
print('Número digitado: {} \n'
      'Seu antecessor é {} \n'
      'Seu sucessor é {}'.format(num, ant, suc))
