# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo,
# desconsiderando os espaços.

frase = input('Digite uma frase: ').strip().upper()

for letra in frase:
    juntar = ''.join(frase)
    if juntar == juntar[::-1]:
        print(f'A frase "{frase.capitalize()}" é um palíndromo')
        break
    else:
        print(f'A frase "{frase.capitalize()}" não é um palíndromo')
        break
