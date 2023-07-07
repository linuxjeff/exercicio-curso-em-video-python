# Programa para calcular o seno e o cos de um angulo.

# Importando Libs

from math import sin, cos, tan, radians

# Variáveis

Angulo = float(input('Digite um ângulo.\n>>> '))

Radianos = radians(Angulo)

# Execução

print('Ângulo: {:.1f}°'.format(Angulo))

print('Seno: {:.4f}'.format(sin(Radianos)))

print('Cosseno: {:.4f}'.format(cos(Radianos)))

print('Tangente: {:.4f}'.format(tan(Radianos)))
