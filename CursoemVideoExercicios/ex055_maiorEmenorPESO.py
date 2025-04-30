# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maior = None # Criei duas variáveis e não coloquei nenhum valor nelas
menor = None

for c in range(1, 6): # fiz o laço com 5 repetições
    peso = float(input(f'Digite o peso da {c}° pessoa: '))
    if maior is None or peso > maior: # Criei um IF para verificar se o valor de maior é None ou se é menor que Peso
        maior = peso # No primeiro laço, o programa irá identificar que a variável MAIOR é None,
                     # então irá substituir o valor MAIOR de None para o valor que está em PESO.

    if menor is None or peso < menor: # Da mesma forma de cima, identificar se MENOR é None ou tem valor.
        menor = peso                  # No primeiro laço fará o mesmo que MAIOR, saindo de NONE pro valor de PESO

        # Após o primeiro laço, os próximos laços as variáveis MAIOR e MENOR já terão valores.

print(f'O maior valor foi {maior}')
print(f'O menor valor foi {menor}')