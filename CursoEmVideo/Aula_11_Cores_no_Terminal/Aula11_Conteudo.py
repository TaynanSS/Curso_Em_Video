# Código ANSI (escape sequence)
# Exemplo: \033[0;33;44m
# \033[Style;Text;Back m

# Style:
#   0 -> None
#   1 -> Bold (Letra mais gorda NEGRITO)
#   4 -> Underlinne (Letra sublinhada)
#   7 -> Negative (Vai inverter as configs, a cor de fundo vai pra letra, e a cor da letra vai pro fundo dela.)

# Text:
#  30 -> Branco
#  31 -> Vermelho
#  32 -> Verde
#  33 -> Amarelo
#  34 -> Azul Escuro
#  35 -> Roxo
#  36 -> Azul Ciano
#  37 -> Cinza

# Back (Fundo):
#  40 -> Branco
#  41 -> Vermelho
#  42 -> Verde
#  43 -> Amarelo
#  44 -> Azul Escuro
#  45 -> Roxo
#  46 -> Azul Ciano
#  47 -> Cinza

print('\033[31;43mOlá Mundo') # Irá mostrar a letra vermelha e fundo amarelo
print('\033[1;40;41mOlá Mundo') # Irá mostrar a letra brana em negrito e fundo vermelho.
print('\033[4;30;45mOlá Mundo\033[m') # Para que o fundo não fique na linha inteira, coloca \033[m no fim do print.
print('\033[30mOlá Mundo\033[m')

nome = 'Taynan'
print('Olá, {}{}{}'.format('\033[4;34m', nome, '\033[m'))
# Dessa forma acima, as configs de cores não vão atrapalhar dentro do print

# Fazendo de uma forma mais organizada.

nome = 'Taynan'
cores = {'limpo':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}  # Dessa forma irá organizar, dentro da variável os tipos de cores que quer.

print('Olá, prazer em te conhecer, {}{}{}'.format(cores['pretoebranco'], nome, cores['limpo']))
