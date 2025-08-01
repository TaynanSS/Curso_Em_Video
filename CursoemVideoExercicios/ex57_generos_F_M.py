# Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente
# até ter um valor correto.

print('Insira M para Masculino e F para Feminino.')

sexo = ''
while 'M' != sexo != 'F':
    sexo = str(input('Gênero [M/F]: ')).upper().strip()
    if sexo == 'F':
        print('Você é mulher!')
    elif sexo == 'M':
        print('Você é Homem!')
    else:
        print('Opção incorreta. Insira um gênero entre M ou F.')


