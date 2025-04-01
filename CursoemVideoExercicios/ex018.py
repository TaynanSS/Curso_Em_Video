# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.

# PRIMEIRA FORMA DE FAZER

import math
conv = int(input('Digite um ângulo: '))
valor = math.radians(conv)
print('O ângulo {} possui\n'
      'Seno: {:.2f}\n'
      'Cosseno: {:.2f}\n'
      'Tangente: {:.2f}.'.format(conv, math.sin(valor), math.cos(valor), math.tan(valor)))

# SEGUNDA FORMA DE FAZER

import math
angulo = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))