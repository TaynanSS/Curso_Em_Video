'''
CADEIAS DE STRING

* FATIAMENTO
Exemplo:

frase = 'Curso em Video Python'

C u r s o   e m   V  i  d  e  o     P  y  t  h  o  n
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

print(frase[9])  ---> Irá mostrar na tela o espaço 9 da lista frase ---> V

frase[9:13] --> Irá mostrar o que tá nas caixas 9 até 12. Sempre no final uma caixa a menos --> V i d e

frase[9:21] --> Irá mostrar 9 até 20. Sempre no final com 1 a menos --> V i d e o  P y t h o n

frase[9:21:2] --> Irá mostrar de 9 até 20, só que pulando de 2 em 2 --> V d o P t o

frase[:5] --> é o mesmo que escrever frase[0:5]. vai do 0 até 5 --> C u r s o

frase[15:] --> Seria do espaço 15 até o final da lista --> P y t h o n

frase[9::3] --> Mostraria os caracteres do 9 até o final da lista, só que pulando de 3 em 3
 ---> V e P h

* ANÁLISE

C u r s o   e m   V  i  d  e  o     P  y  t  h  o  n
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

__Função LEN__
Exemplo:
len(frase) --> Analisa o comprimento de frase --> 21 caracteres)

__Função COUNT__
Exemplo:
frase.count('o') --> Está pedindo para contar quantas vezes aparece 'o' da forma que está escrita
entre parênteses.
Exemplo²:
frase.count('C') --> conta quantas vezes aparece 'C' na variável frase.
Exemplo³:
frase.count('o', 0, 13) --> Análise com fatiamento. Pede quantos 'o' aparecem na variável frase
entre o espaço 0 e 13. Nesse caso seria apenas 1, pois o 'o' do caracter 13 não é conta.

__Função FIND__
Exemplo:
frase.find('deo') --> Indica onde começa o 'deo' na variável frase. Resultado seria 11.
Exemplo²:
frase.find('Android') --> Como 'Android' não existe, o programa irá retornar '-1' indicando que
a String 'Android' não existe na String 'Curso em Video Python'

__Operador IN__
'Curso' in frase --> Irá retornar 'True', pois a String 'Curso' existe na String 'Curso em Video Python'


* Transformação

C u r s o   e m   V  i  d  e  o     P  y  t  h  o  n
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

__Função REPLACE__
Exemplo¹:
frase.replace('Python', 'Android') --> Irá buscar em frase a String 'Python' e substituir por 'Android'

__Método UPPER__
Exemplo¹:
frase.upper() --> Deixará toda a String em maiúsculo.
C U R S O  EM  V I D E O  P Y T H O N

__Método LOWER__
Exemplo:
frase.lower() --> Deixará toda a String em minúsculo.
c u r s o  e m  v i d e o  p y t h o n

__Função CAPITALIZE__
Exemplo¹:
frase.capitalize() --> Deixará toda String em minúsculo, exceto o 1° caractere.
C u r s o  e m  v i d e o  p y t h o n

__Função TITLE__
Exemplo¹:
frase.title() --> Localizar todas as palavras da String, e deixar o primeiro caracter de cada uma
delas em maísculo
C u r s o  E m  V i d e o  P y t h o n

__Função STRIP__
Exemplo¹:
frase.strip() --> Remove todos os espaços inúteis.
    Aprenda Python
Irá remover os espaços que tiverem antes de Aprenda, e depois de Python.

__Função RSTRIP__
Exemplo²:
frase.rstrip() --> Remove todos os espaços inúteis do lado direito.
__Função LSTRIP__
Exemplo³:
frase.lstrip() --> Remove todos os espaços inúteis do lado esquerdo..

* DIVISÃO

__Função Split__
frase.split() --> Irá separar as String por espaço, gerando uma nova lista sempre que tiver um espaço.
C u r s o   e m   V  i  d  e  o     P  y  t  h  o  n
0 1 2 3 4   0 1   0  1  2  3  4     0  1  2  3  4  5
___ 0 __   __1__  ______2______     _______3________

* JUNÇÃO
Exemplo:
'-'.join(frase) --> Irá juntar as String da frase que foi separada no SPLIT, colocando '-' entre os espaços.
Curso-em-Video-Python

