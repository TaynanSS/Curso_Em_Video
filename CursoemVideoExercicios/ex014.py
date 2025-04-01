# Escreva um programa que converta uma temperatura
# digitada em °C e converta para °F.

cel = float(input('Informe a temperatura em Celsius: ? °'))
conv = (cel * 9/5) + 32
print('A temperatura de {:.1f}°C é equivalente a {:.1f}°F'.format(cel, conv))