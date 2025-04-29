for c in range(0,6):
    print('Oi')         # Irá mostrar o 'Oi' 6 vezes
print('FIM')

'_________________________________________________________________________________________'
for c in range(0,6):
    print('Oi')         # Irá mostrar o 'Oi', 'FIM' 6 vezes
    print('FIM')

'_________________________________________________________________________________________'
for c in range(0,6):
    print(c)            # Irá mostrar a número colocado em c. Ficaria ==> 0, 1, 2, 3, 4, 5
print('FIM')

'_________________________________________________________________________________________'
for c in range(1, 7):
    print(c)            # Irá mostrar a contagem de 1 até 6 ==> 1, 2, 3, 4, 5, 6
print('FIM')

'_________________________________________________________________________________________'
for c in range(6, 0, -1):
    print(c)                # Irá fazer a contagem inversa ==> 6, 5, 4, 3, 2, 1
print('FIM')

'_________________________________________________________________________________________'
for c in range(0, 7, 2):
    print(c)                # Irá contar de 0 até 6, pulando de 2 em 2 ==> 0, 2, 4, 6
print('FIM')

'_________________________________________________________________________________________'
i = int(input('Inicio: '))  # Irá escolher o inicio da contagem
f = int(input('Fim: '))     # Irá escolher o fim da contagem
p = int(input('Passo: '))   # irá escolher de quanto em quantos números será pulado em cada contagem
for c in range(i, f+1, p):  # No 'f+1' foi colocado +1 para que na contagem fique o valor correto.
    print(c)
print('FIM')

'_________________________________________________________________________________________'
for c in range(0, 3):
    n = int(input('Digite um valor: '))     # Aqui irá solicitar que o usuário digite um valor 3 vezes
print('FIM')

'_________________________________________________________________________________________'
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos os valores foi {s}')
