# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com sua idade:

# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

hoje = date.today().year

ano = int(input('Digite o ano que nasceu: '))

if hoje - ano < 18:
    print(f'Você ainda vai se alistar para o serviço militar.\nFaltam {18 - (hoje - ano)}ano(s).')
elif hoje - ano == 18:
    print('Você tem 18anos, está no período de alistamento.')
else:
    print(f'Você já passou do período de alistamento.\nDeveria ter se alistado há {(hoje - ano) - 18}ano(s)')