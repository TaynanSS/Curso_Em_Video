nome = str(input('Digite seu nome: '))

if nome == 'Taynan':
    print('Que nome lindo!')
elif nome == 'Vivian' or nome == 'Damião' or nome == 'Leonardo':
    print('Que nome de peidão!')
elif nome in 'Silva Rodrigues Paula':
    print('Esse sobrenome é bem comum no Brasil')
else:
    print('Seu nome é bem comum.')
print(f'Bom dia, {nome}!')