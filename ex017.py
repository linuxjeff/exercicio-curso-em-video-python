# Programa que calcula a hipotenusa.

# Importação de libs
from math import hypot

# Variáveis

CatetoOposto = float(input('Qual o cateto oposto?\n>>> '))

CatetoAdjacente = float(input('Qual o cateto adjacente?\n>>> '))

# Execução

print('O triangulo retângulo com o cateto oposto igual a {} e o cateto adjacente igual {} tem a hipotenusa de: {:.2f}'.format(CatetoOposto, CatetoAdjacente, hypot(CatetoOposto, CatetoAdjacente)))
