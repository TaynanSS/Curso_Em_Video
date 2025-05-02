# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

num = int(input('Digite um valor para ver sua tabuada: '))

print(f'Segue abaixo a tabuada do {num}\n')

for c in range(1, 11):
    print(f'{num} x {c} = {num * c}')
