# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}° pessoa: '))
    if peso > maior:
        maior = peso
        peso = menor
    elif menor < peso:
        menor = peso

    print(maior)
    print(menor)

print(f'O maior valor foi {maior}')
print(f'O menor valor foi {menor}')