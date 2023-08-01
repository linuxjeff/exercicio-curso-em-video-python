# programa para calcular o preço da passagem

Quilometros = float(input('Quantos quilômetros pretende viajar?\n>>> '))

if Quilometros <= 200:
    print('O preço da passagem é: R$ {:.2f}'.format(Quilometros * 0.5))
else:
    print('O preço da passagem é: R$ {:.2f}'.format(Quilometros * 0.45))
