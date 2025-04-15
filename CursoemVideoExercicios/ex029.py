# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada Km acima do limite.

carro = input('Qual a velocidade do carro? ')

if carro.isalpha():
    print('Por favor, digite a quilometragem.')
else:
    carro = float(carro)
    if carro > 80:
        multa = (carro - 80) * 7
        print('Você foi multado! Excedeu o limite permitido de 80km/h')
        print(f'Valor da multa: R${multa:.2f}')
    else:
        if carro == 80:
            print('Você está no limite de velocidade!')
        else:
            if carro < 0:
                print('Você está dando ré, freie imediatamente!')
            else:
                if carro == 0:
                    print('Você está parado!')

print('Você está abaixo do limite de velocidade. Dirija com cuidado!')
