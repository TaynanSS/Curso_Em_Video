# Melhore o DESAFIO 061, perguntando para o usuário
# se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

# DESAFIO 061 ---> # Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro = float(input('Informe o primeiro termo: '))
razao = float(input('Informe a razão da PA: '))

termo = 0   # contador de termos
total = 10  # inicializador para mostrar os 10 primeiros termos
mais = 10   # Inicialização para o loop

while mais != 0:
    while termo < total:
        resultado = primeiro + termo * razao
        print(f'{termo + 1}°: {resultado}')
        termo += 1
    print('\nDeseja ver mais termos? Digite 0 para encerrar o programa.')
    mais = int(input('Informe quantos termos a mais deseja: '))
    total += mais   # Atualiza o total de termos

print('Programa encerrado.')


















