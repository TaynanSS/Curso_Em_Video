# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

valor = int(input('Digite um número inteiro: '))
tab1 = valor * 1
tab2 = valor * 2
tab3 = valor * 3
tab4 = valor * 4
tab5 = valor * 5
tab6 = valor * 6
tab7 = valor * 7
tab8 = valor * 8
tab9 = valor * 9
print('Tabuada do valor digitado: \n')
print('_' * 12)
print('{} x  1 = {:2}\n'
      '{} x  2 = {:2}\n'
      '{} x  3 = {:2}\n'
      '{} x  4 = {:2}\n'
      '{} x  5 = {:2}\n'
      '{} x  6 = {:2}\n'
      '{} x  7 = {:2}\n'
      '{} x  8 = {:2}\n'
      '{} x  9 = {:2}'.format(valor, tab1, valor, tab2, valor, tab3,valor, tab4,valor, tab5,valor, tab6,valor, tab7,valor, tab8, valor, tab9))
print('_' * 12)


