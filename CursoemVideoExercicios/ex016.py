# Crie um programa que leia um número Real qualquer pelo teclado
# e mostre na tela a sua porção inteira.
#EX: Digite um número: 6.127
#O número 6.127 tem a parte inteira 6.

# FORMA IMPORTANDO MATH

from math import trunc
num = float(input('Digite um valor: '))
print('O número {} tem a parte inteira {}'.format(num, trunc(num)))

# Forma SEM IMPORTAR

num = float(input('Digite um valor: '))
print('O número {} tem a parte inteira {}'.format(num, int(num)))
