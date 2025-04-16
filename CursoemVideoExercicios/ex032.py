# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date

ano = int(input('Digite um ano: '))
print('Caso queira analisar o ano atual, digite 0.')

anobi = ano % 4
anobi1 = ano % 400
naobi = ano % 100

if anobi == 0 and anobi1 == 0 and naobi == 0:
        print('O ano {} é bissexto'.format(ano))
else:
    if anobi == 0 and naobi != 0:
        print('O ano {} é bissexto.'.format(ano))
    else:
        print('O ano {} não é bissexto.'.format(ano))

# OUTRA FORMA DE FAZER

ano = int(input('Digite um ano: '))
print('Caso queira analisar o ano atual, digite 0.')

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} NÃO é BISSEXTO.')

