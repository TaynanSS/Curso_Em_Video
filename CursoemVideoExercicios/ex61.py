# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro = float(input('Informe o primeiro termo: '))
razao = float(input('Informe a razão da PA: '))

termo = 0
valor = 0

while termo < 10:
    valor = primeiro + termo * razao
    termo += 1

    print(valor, end=' -> ')
print('FIM!')