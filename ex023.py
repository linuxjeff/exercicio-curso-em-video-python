# O Programa lê um número de 0 a 9999 e retorna a quantidade em cada casa.

Numero = input('Ditite um numero de 0 a 9999\n>>> ').strip()

print('Unidade: {}'.format(Numero[3]))
print('Dezena: {}'.format(Numero[2]))
print('Centena: {}'.format(Numero[1]))
print('Milhar: {}'.format(Numero[0]))