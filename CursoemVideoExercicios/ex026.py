# Faça um programa que leia uma frase pelo teclado e mostra:
# - Quantas vezes aparece a letra 'A'
# - Em que posição ela aparece a primeira vez.
# - Em que posição ela aparece a última vez.

entrada = input('Digite uma frase: ')

quantidade = entrada.count('a')
primeira = entrada.find('a')
ultima = entrada.rfind('a')


print('Quantas vezes aparece: {}\n'
      'Qual posição aparece na 1° vez: {}\n'
      'Qual posição aparece na última vez: {}'.format(quantidade, primeira, ultima))

#'Qual posição aparece na 1° vez: {}\n'
 #     'Qual posição aparece na última vez: {}'