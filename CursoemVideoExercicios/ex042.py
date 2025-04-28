# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# - Equilátero: Todos os lados iguais
# - Isósceles: Dois lados iguais
# - Escaleno: Todos os lados diferentes

# DESAFIO 035: # Desenvolva um programa que leia o comprimento de três retas
               # e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Comprimento da primeira reta: '))
r2 = float(input('Comprimento da segunda reta: '))
r3 = float(input('Comprimento da terceira reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1 and r1 == r2 and r1 == r3:
    print('Todos os lados são iguais.\nO triângulo é \033[1mEquilátero.\033[m\n')
    print(f'As retas de comprimento {r1:.2f}, {r2:.2f} e {r3:.2f} formam um triângulo.')
elif r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1 and r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2 or r2 == r3 and r2 != r1:
    print('Dois lados são iguais.\nO triângulo é \033[1;mIsósceles.\033[m')
elif True and r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Todos os lados são diferentes.\nO triângulo é \033[1mEscaleno.\033[m')
    print(f'As retas de comprimento {r1:.2f}, {r2:.2f} e {r3:.2f} formam um triângulo.')
else:
    print(f'As retas de comprimeiro {r1:.2f}, {r2:.2f} e {r3:.2f} não formam um triângulo.')
  

# OUTRA FORMA DE FAZER

r1 = float(input('Comprimento da primeira reta: '))
r2 = float(input('Comprimento da segunda reta: '))
r3 = float(input('Comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'As retas de comprimeiro {r1:.2f}, {r2:.2f} e {r3:.2f} formam um triângulo.')
  if r1 == r2 == r3:
      print('Todos os lados são iguais.\nO triângulo é \033[1mEquilátero.\033[m\n')
  elif r1 != r2 != r3 != r1:
      print('Todos os lados são diferentes.\nO triângulo é \033[1mEscaleno.\033[m')
  else:
      print('Dois lados são iguais.\nO triângulo é \033[1;mIsósceles.\033[m')
else: 
    print(f'As retas de comprimeiro {r1:.2f}, {r2:.2f} e {r3:.2f} não formam um triângulo.')
