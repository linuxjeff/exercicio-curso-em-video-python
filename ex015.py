# Programa para calcular o aluguel de veículos.

# Variáveis

Dias = int(input('Qual o número de dias do aluguel do veículo?\n>>> '))

Quilometros = float(input('Quantos quilômetros foram percoridos?\n>>> '))

Calculo = (Dias * 60) + (Quilometros * 0.15)

# Execução

print('O Aluguel do veículo fica: R${:.2f}'.format(float(Calculo)))
