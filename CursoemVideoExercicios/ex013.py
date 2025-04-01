# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
# com 15% de aumento.

salario = float(input('Informe seu salário: R$'))
aum = (salario * 15/100) + salario
print('Salário após aumento de 15%: R${:.2f}'.format(aum))