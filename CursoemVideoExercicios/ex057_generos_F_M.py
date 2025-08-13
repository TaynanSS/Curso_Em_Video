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


# VERSÃO GUANABARA

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0] # O [0] vai pegar apenas a primeira letra que o user digitar.
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
