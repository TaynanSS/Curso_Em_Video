# Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e
# que se encontram no intervalo de 1 até 500

somatorio = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        pass
    somatorio += c
print(f'Somatório de todos os números ímpares: {somatorio}')