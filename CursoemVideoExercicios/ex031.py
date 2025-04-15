# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$ 0,45 para viagens mais longas.

km = float(input('Informe a distância da sua viagem em Km: '))

if km < 0:
    print('Valor inválido. Digite um valor acima de 0Km')
else:
    if km <= 200:
        cobrar = km * 0.5
        print('Sua viagem de {}Km custará R${:.2f}'.format(km, cobrar))
    else:
        cobrar = km * 0.45
        print('Sua viagem de {}Km custará R${:.2f}'.format(km, cobrar))

# OUTRA FORMA DE FAZER

km = float(input('Informe a distância da sua viagem em Km: '))

preço = km * 0.50 if km <= 200 else km * 0.45

print(f'O preço de sua passagem será de R${preço:.2f}')