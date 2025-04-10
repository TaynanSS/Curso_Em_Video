# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00 calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Informe o valor do seu salário: R$'))

aum = (salario * 0.10) + salario
aum1 = (salario * 0.15) + salario

if salario <= 0:
    print('Impossível, por favor digite seu salário verdadeiro')
else:
    if salario <= 1250:
        print('Seu salário com aumento de 15% será: {:.2f}'.format(aum1))
    else:
        if salario > 1250:
            print('Seu salário com aumento de 10% será: {:.2f}'.format(aum))
