# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.


r1 = float(input('Comprimento da primeira reta: '))
r2 = float(input('Comprimento da segunda reta: '))
r3 = float(input('Comprimento da terceira reta: '))

soma1 = r1 + r2
soma2 = r1 + r3
soma3 = r2 + r3

if r1 and r2 < r3:
    if soma1 > r3:
        print('As retas de comprimento {:.2f}, {:.2f} e {:.2f} 1 formam um triângulo.'.format(r1, r2, r3))
else:
    if r1 and r3 < r2:
        if soma2 > r2:
            print('As retas de comprimento {:.2f}, {:.2f} e {:.2f} 2 formam um triângulo.'.format(r1, r2, r3))
    else:
        if r2 and r3 < r1:
            if soma3 > r1:
                print('Essas retas de comprimento {:.2f}, {:.2f} e {:.2f} 3 formam um triângulo.'.format(r1, r2, r3))
        else:
            print('As retas de comprimeiro {:.2f}, {:.2f} e {:.2f} não formam um triângulo.'.format(r1, r2, r3))

