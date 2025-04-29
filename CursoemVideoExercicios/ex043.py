# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - Acima de 40: Obesidade mórbida

# peso / (altura * altura)

print('Iremos calcular seu IMC e informar o status que você está.\n')

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Peso: {peso:.2f}\nAltura: {altura:.2f}\nIMC: {imc:.2f}\nStatus: \033[1mAbaixo do Peso\033[m')
elif imc >= 18.5 and imc < 25:
    print(f'Peso: {peso:.2f}\nAltura: {altura:.2f}\nIMC: {imc:.2f}\nStatus: \033[1mPeso Ideal\033[m')
elif imc >= 25 and imc < 30:
    print(f'Peso: {peso:.2f}\nAltura: {altura:.2f}\nIMC: {imc:.2f}\nStatus: \033[1mSobrepeso\033[m')
elif imc >= 30 and imc <40:
    print(f'Peso: {peso:.2f}\nAltura: {altura:.2f}\nIMC: {imc:.2f}\nStatus: \033[1mObesidade\033[m')
else:
    print(f'Peso: {peso:.2f}\nAltura: {altura:.2f}\nIMC: {imc:.2f}\nStatus: \033[1mObesidade Mórbida\033[m')
