# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

print(f'{ ' 10 TERMOS DE UMA PA ':=^40}\n')
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

print('-=-' * 18)
for c in range(10):
    termo = primeiro + c * razao
    print(termo, end=', ')
print('ACABOU!')
print('')
print('-=-' * 18)

# FORMA FEITA PELO GUANABARA

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 -1) * razao

for c in range(primeiro, decimo + razao, razao):
    print(c, end=' -> ')
print('ACABOU!')
