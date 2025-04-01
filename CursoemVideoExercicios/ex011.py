# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m².

larg = float(input('Digite a largura: '))
alt = float(input('Digite a altura: '))
area = (larg * alt)
tinta = area / 2
print('Sua parede tem uma área de {}.\n'
      'Será necessário {}m² litros de tinta para pintar a parede'.format(area, tinta))
