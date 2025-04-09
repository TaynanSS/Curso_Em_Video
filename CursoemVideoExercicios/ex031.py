# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$ 0,45 para viagens mais longas.

km = float(input('Qual a distância da sua viagem em Km: '))

cobrar1 = km * 0.5
cobrar2 = km * 0.45

if km < 0:
    print('Valor inválido. Digite um valor acima de 0Km')
else:
    if km <= 200:
        print('Sua viagem de {}Km custará {:.2f}'.format(km, cobrar1))
    else:
        print('Sua viagem de {}Km custará {:.2f}'.format(km, cobrar2))
