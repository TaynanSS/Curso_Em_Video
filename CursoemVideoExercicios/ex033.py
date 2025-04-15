# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 == n2 and n1 > n3:
    print('O primeiro e segundo número são iguais e os maiores.\n'
          f'Número digitado: {n1}')
else:
    if n1 == n3 and n1 > n2:
        print('O primeiro e terceiro número são iguais e os maiores.\n'
              f'Número digitado: {n1}')
    else:
        if n1 > n2 and n1 > n3:
            print('O primeiro número é o maior.\n'
                  f'Número digitado: {n1}')
        else:
            if n2 == n1 and n2 > n3:
                print('O primeiro e segundo número são iguais e os maiores\n'
                      f'Número digitado: {n2}')
            else:
                if n2 == n3 and n2 > n1:
                    print('O segundo e terceiro número são iguais e os maiores.\n'
                          f'Número digitado: {n2}')
                else:
                    if n2 > n1 and n2 > n3:
                        print('O segundo número é o maior.\n'
                              f'Número digitado: {n2}')
                    else:
                        if n1 == n2 and n1 == n3 and n2 == n3:
                            print('Todos os números são iguais e não há um maior.')
                        else:
                            print('O terceiro número é o maior.\n'
                                  f'Número digitado: {n3}')

if n1 == n2 and n1 < n3:
    print('O primeiro e segundo número são iguais e os menores.\n'
          f'Número digitado: {n1}')
else:
    if n1 == n3 and n1 < n2:
        print('O primeiro e terceiro número são iguais e os menores.\n'
              f'Número digitado: {n1}')
    else:
        if n1 < n2 and n1 < n3:
            print('O primeiro número é o menor.\n'
                  f'Número digitado: {n1}')
        else:
            if n2 == n1 and n2 < n3:
                print('O primeiro e segundo número são iguais e os menores\n'
                      f'Número digitado: {n2}')
            else:
                if n2 == n3 and n2 < n1:
                    print('O segundo e terceiro número são iguais e os menores.\n'
                          f'Número digitado: {n2}')
                else:
                    if n2 < n1 and n2 < n3:
                        print('O segundo número é o menor.\n'
                              f'Número digitado: {n2}')
                    else:
                        if n1 == n2 and n1 == n3 and n2 == n3:
                            print('Todos os números são iguais e não há um menor.')
                        else:
                            print('O terceiro número é o menor.\n'
                                  f'Número digitado: {n3}')