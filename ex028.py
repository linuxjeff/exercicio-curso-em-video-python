# programa sorteia um número entre um e seis e pessoa tem que acerta

from random import randrange

D6 = randrange(1, 7)

Aposta = int(input('Vou jogar um dado de seis lados.\nQual lado vai cair?\n>>> '))

if D6 == Aposta:
    print('Você acertou!\nLado: {}'.format(D6))
else:
    print('Você errou!\nLado {}'.format(D6))
