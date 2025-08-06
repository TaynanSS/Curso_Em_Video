# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números
# foram digitados e qual foi a soma entre eles (Desconsiderando o flag.)
# OBS: O flag seria o 999 que é a entrada de dado para parada.


cont = 0
num = 0
soma = 0

print('Digite 999 para encerrar o programa ')
while num != 999:
    num = int(input('Digite um número inteiro: '))
    if num != 999:
        soma += num
        cont += 1


print(f'Quantidade de números digitados: {cont}')
print(f'Soma total dos números digitados: {soma}')
