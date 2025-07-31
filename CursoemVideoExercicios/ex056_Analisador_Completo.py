# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# a média de idade do grupo,
# qual é o nome do homem mais velho e
# quantas mulheres têm menos de 20 anos.

idadevelho = 0
contM = 0
media = 0
for i in range(1,5):
    print('-'*5, f'{i}° PESSOA', '-'*5)        # Pra deixar mais organizado
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Informe sua idade: '))
    sexo = str(input('Gênero (F/M): ')).upper().strip()

    if sexo == 'F' and idade < 20: :    # posso fazer o filtro dessa forma -> if sexo in 'Ff' and idade < 20       ELIMINANDO O .UPPER() 
        contM += 1    # Aqui já farei o filtro em mulheres abaixo de 20anos e coloco um contador sempre que houver outra.


    # posso fazer o filtro dessa forma -> if sexo in 'Mm' and idade > idadevelho
    if sexo == 'M' and idade > idadevelho:    # Na primeira repetição irá substituir o valor de "idadevelho" para o que entrou em "idade"
        idadevelho = idade        # caso entre outro valor acima do que está em "idadevelho", ele é substituído novamente.
        maisvelho = nome # Aqui salvará o último nome que passou por esse filtro.

    media += idade    # somatório básico

print(f'Idade média do grupo: {media/4}\n',    # printa já fazendo a divisão por 4, economizando uma linha
      f'Homem mais velho: {maisvelho.capitalize()} - Idade: {idadevelho}\n',    # Coloquei um Capitalize para sempre no primeiro nome vim a 1°letra em maiúsculo. Apenas algo visual.
      f'Mulheres com menos de 20anos: {contM}')    
