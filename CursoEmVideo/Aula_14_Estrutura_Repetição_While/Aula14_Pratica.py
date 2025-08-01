"""for c in range(1, 10): #
    print(c) #asd
print('Fim') # """

"""c = 1   # dando valor inicial da variável de repetição
while c < 10:   # adicionando a condição
    print(c)
    c += 1      # adicionando o contador para tenha uma prograssão na variável 'c'
print('Fim')"""

#----------------------------------- OUTRA SITUAÇÃO --------------------------------------------------#

# Nessa situação sempre terá a entrada máxima de 4
"""for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('Fim')"""

# Nessa situação não sabemos quantas entradas terão até que o usuário digite '0'

"""n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')"""

# Também podemos fazer com que a repetição exista até que o usuário decida parar, usando esse exemplo:

"""r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar [S/N]: ')).upper() # Coloquei um UPPER para não ter erro.
print('Fim')"""

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print(f'Você digitou {par} números pares e {impar} números ímpares. ')