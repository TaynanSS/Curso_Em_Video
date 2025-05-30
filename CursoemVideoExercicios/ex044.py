# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:

# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: Preço normal
# - 3x ou mais no cartão: 20% de juros

print(f'{ 'LOJAS NANZINHO ':=^40}')

produto = int(input('Informe o valor do produto: '))


print('Para forma de pagamento, escolha uma das opções abaixo:')
print('1 - À vista dinheiro/cheque (10% de desconto)'
      '\n2 - À vista no cartão (5% de desconto)'
      '\n3 - Em até 2x no cartão (Preço Normal)'
      '\n4 - 3x ou mais no cartão (20% de juros)\n')

escolha = int(input('Informe a forma de pagamento: '))

if escolha == 1:
    desconto = produto * 10 / 100
    print(f'Valor do produto: {produto:.2f}'
          f'\nValor a ser pago: {produto - desconto:.2f}')
elif escolha == 2:
    desconto = produto * 5 / 100
    print(f'Valor do produto: {produto:.2f}'
          f'\nValor a ser pago: {produto - desconto:.2f}')
elif escolha == 3:
    print(f'Valor do produto: {produto:.2f}'
          f'\nValor a ser pago: {produto:.2f}')
elif escolha == 4:
    juros = produto * 20 / 100
    parcela = int(input('Escolha a quantidade de parcelas: '))
    print(f'Valor do produto: {produto:.2f}'
          f'\nValor a ser pago: {produto + juros:.2f}'
          f'\nParcelado em {parcela}x de {(produto + juros)/ parcela:.2f}')
else:
    print('Opção inválida. Escolha uma das opções de pagamento.')
    
