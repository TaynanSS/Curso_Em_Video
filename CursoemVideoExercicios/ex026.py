# Faça um programa que leia uma frase pelo teclado e mostra:
# - Quantas vezes aparece a letra 'A'
# - Em que posição ela aparece a primeira vez.
# - Em que posição ela aparece a última vez.

entrada = str(input('Digite uma frase: ')).strip().lower()

quantidade = entrada.count('a')
primeira = entrada.find('a') + 1
ultima = entrada.rfind('a') + 1


print('Quantas vezes aparece: {}\n'
      'Qual posição aparece na 1° vez: {}\n'
      'Qual posição aparece na última vez: {}'.format(quantidade, primeira, ultima))

#'Qual posição aparece na 1° vez: {}\n'
 #'Qual posição aparece na última vez: {}'
