# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

num = int(input('Digite um valor pra tabuada: '))

print(f'Segue abaixo a tabuada do {num}\n')

for c in range(1, 11):
    tabuada = num * c
    print(f'{num} x {c} = {tabuada}')
