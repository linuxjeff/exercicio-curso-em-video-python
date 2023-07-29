# Programa para calcular multa.

Velocidade = int(input('Qual a velocidade do veículo?\n>>> '))

if Velocidade > 80:
    print('Você ultrapassou o limite de velocidade.\nSua multa tel o valor de: {:.2f}'.format((Velocidade - 80)*7))
else:
    print('Você é um condutor responsável!')
