# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

# IMPORTANDO MATH (1°)

import math
cato = float(input('Digite o cateto oposto: '))
cata = float(input('Digite o cateto adjacente: '))
hipo = cato**2 + cata**2
print('Comprimento da hipotenusa: {:.2f}'.format(math.sqrt(hipo)))

# IMPORTANDO MATH (2°)

import math
cato = float(input('Digite o cateto oposto: '))
cata = float(input('Digite o cateto adjacente: '))
hipo = math.hypot(cato, cata)
print('Comprimento da hipotenusa: {:.2f}'.format(hipo))

# SEM IMPORTAR A MATH

cato = float(input('Digite o cateto oposto: '))
cata = float(input('Digite o cateto adjacente: '))
hipo = (cato ** 2 + cata ** 2) ** (1/2)
print('Comprimento da hipotenusa: {:.2f}'.format(hipo))

