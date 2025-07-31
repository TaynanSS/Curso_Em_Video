# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# a média de idade do grupo,
# qual é o nome do homem mais velho e
# quantas mulheres têm menos de 20 anos.

idadevelho = 0
contM = 0
media = 0
for i in range(1,5):
    print('-'*5, f'{i}° PESSOA', '-'*5)
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Informe sua idade: '))
    sexo = str(input('Gênero (F/M): ')).upper().strip()

    if sexo == 'F':
        if idade < 20:
            contM += 1

    if sexo == 'M' and idade > idadevelho:
        idadevelho = idade
        maisvelho = nome

    media += idade

print(f'Idade média do grupo: {media/4}\n', f'Homem mais velho: {maisvelho.capitalize()} - Idade: {idadevelho}\n', f'Mulheres com menos de 20anos: {contM}')