'''

exemplos de estrutura de repetição:

Um personagem precisa andar em cima de pisos, onde cada piso é um passo.
No local que tem 6 pisos e no último piso tem uma maçã, o personagem vai ter que andar 6vezes e na quinta vez pegar a maçã.

em portugol seria algo do tipo:
PASSO, PASSO, PASSO, PASSO, PASSO, PASSO, PEGA

laço c no intervalo(0,6) |   for c in range(0,6):
    passo                |      passo
pega                     |   pega

Usando o mesmo exemplo acima e ao invés de 6 pisos, são 10, mas a cada dois pisos, tem um buraco, no fim pegando a maçã.
Seria algo do tipo:

PASSO, PULA, PASSO, PULA, PASSO, PULA, PASSO, PULA, PASSO, PEGA

laço c no intervalo(0,4)   |    for c in range(0,4):
    passo                  |        passo
    pula                   |        pula
passo                      |    passo
pega                       |    pula

Se após o buraco, haver uma moeda para pegar, como seria feito?

laço c no intervalo(0,4)    |   for c in range(0,4):
    se MOEDA                |       if MOEDA:
        pega                |           pega
    passo                   |       passo
    pula                    |       pula
passo                       |   passo
pega                        |   pega

'''