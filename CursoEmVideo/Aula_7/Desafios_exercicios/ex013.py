# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
# com 15% de aumento.

salario = float(input('Informe seu salário: '))
aum = salario * 0.15 + salario
print('Salário após aumento de 15%: {}'.format(aum))