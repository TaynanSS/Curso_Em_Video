# Exemplo de CONDICIONAL

tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo!')
else:
    print('Carro velho!')
print('--FIM--')

# OUTRA FORMA DE FAZER O EXEMPLO DE CIMA

tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novo!' if tempo <= 3 else 'Carro velho!')
print('--FIM--')