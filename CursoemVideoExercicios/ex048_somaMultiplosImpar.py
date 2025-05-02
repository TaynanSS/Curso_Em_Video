# Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e
# que se encontram no intervalo de 1 até 500

cont = 0
somatorio = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        somatorio += c

print(f'Somatório de todos os {cont} números ímpares divisíveis por 3: {somatorio}')