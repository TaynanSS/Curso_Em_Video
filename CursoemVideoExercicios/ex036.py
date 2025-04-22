# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
# ou então o empréstimo será negado.

casa = float(input('Insira o valor da casa: '))
salario = float(input('Insira o valor do salário: '))
anos = int(input('Em quantos anos deseja pagar: '))

meses = anos * 12

if casa / meses > salario * (30/100):
    prestacao = casa / meses
    print('-=-' * 18)
    print(f'Valor da prestação: {prestacao:.2f}\n'
          f'Valor do salário: {salario:.2f}\n'
          f'O valor da prestação excedeu 30% do seu salário: {salario * (30/100)}\n'
          f'Seu empréstimo foi negado.')
    print('-=-' * 18)
else:
    prestacao = casa / meses
    print('-=-' * 18)
    print(f'Valor da prestação: {prestacao:.2f}\n'
          f'Valor do salário: {salario:.2f}\n'
          f'O valor da prestação abaixo de 30% do seu salário: {salario * (30 / 100):.2f}\n'
          f'Seu empréstimo foi concedido!.')
    print('-=-' * 18)