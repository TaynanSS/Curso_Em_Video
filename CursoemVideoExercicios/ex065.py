# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e
# qual foi o maior e o menor valores lidos. O programa deve perguntar
# ao usuário se ele quer ou não continuar a digitar valores.

media = 0
continuar = ''
maior = None
menor = None
cont = 0

while continuar != 'N':
    num = int(input('Digite um valor inteiro: '))
    cont += 1

    if maior is None or num > maior:
        maior = num 
    if menor is None or num < menor:
        menor = num

    media += num

    while True:
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()
        if continuar == 'S' or continuar == 'N':
            break
        print('Opção inválida. Digite apenas S ou N.')

print(f'Média dos valores digitados: {media / cont}')
print(f'Maior valor digitado: {maior}')
print(f'Menor valor digitado: {menor}')

