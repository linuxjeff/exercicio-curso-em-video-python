# Programa retorna a parte inteira.

# Importando libs
from math import trunc

# Variáveis

Numero = float(input('Digite um número: '))

# Execução

print('A parte inteira do número {} é o número: {}'.format(Numero, trunc(Numero)))
