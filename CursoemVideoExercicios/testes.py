r1 = float(input('Comprimento da primeira reta: '))
r2 = float(input('Comprimento da segunda reta: '))
r3 = float(input('Comprimento da terceira reta: '))

soma1 = r1 + r2
soma2 = r1 + r3
soma3 = r2 + r3

if r1 < r2 and r1 < r3:
    if r2 < r3 and soma1 > r3:
        print('Reta forma triangulo')
else:
    if r2 < r1 and r2 < r3:
        if r1 < r3:
            print('Reta forma triangulo 1')
    else:
        if r3 < r1 and r3 < r2:
            if r