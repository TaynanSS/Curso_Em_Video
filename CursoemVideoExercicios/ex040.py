# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:

# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if nota1 or nota2 < 0:
    print('Digite uma nota entre 0 e 10')
elif nota1 or nota2 > 10:
    print('Digite uma nota entre 0 e 10')
elif media < 5.0:
    print(f'Média:{media:.2f}\nREPROVADO!')
elif media >= 5.0 and media <= 6.9:
    print(f'Média:{media:.2f}\nRECUPERAÇÃO')
else:
    print(f'Média:{media:.2f}\nAPROVADO')