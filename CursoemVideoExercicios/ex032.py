# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

ano = int(input('Digite um ano: '))

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

