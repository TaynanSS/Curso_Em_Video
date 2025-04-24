# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:

# - Até 9anos: MIRIM
# - Até 14anos: INFANTIL
# - Até 19anos: JUNIOR
# - Até 20anos: SÊNIOR
# - Acima: MASTER

from datetime import date

nascimento = int(input('Digite seu ano de nascimento: '))

ano = date.today().year

if ano - nascimento <= 0:
    print('Você acabou de nascer ou nem nasceu ainda.\n\033[1mImpossível ser atleta!\033[m')
elif ano - nascimento <= 9:
    print(f'Você tem {ano - nascimento}ano(s).\nAlocado na categoria \033[1mMIRIM\033[m')
elif ano - nascimento <= 14:
    print(f'Você tem {ano - nascimento}ano(s).\nAlocado na categoria \033[1mINFANTIL\033[m')
elif ano - nascimento <= 19:
    print(f'Você tem {ano - nascimento}ano(s).\nAlocado na categoria \033[1mJUNIOR\033[m')
elif ano - nascimento <= 20:
    print(f'Você tem {ano - nascimento}ano(s).\nAlocado na categoria \033[1mSÊNIOR\033[m')
else:
    print('Você tem mais de 20 anos.\nAlocado na categoria \033[1mMASTER\033[m')