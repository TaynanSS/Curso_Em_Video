# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = float(input('Digite um número: '))
dobro = num * 2
tri = num * 3
raiz = num **(1/2)
print('Número digitado: {} \n'
      'Dobro: {} \n'
      'Triplo: {} \n'
      'Raiz quadrada: {}'.format(num, dobro, tri, raiz))