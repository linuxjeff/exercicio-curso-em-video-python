# O Programa lê um número de 0 a 9999 e retorna a quantidade em cada casa.

Numero = int(input('Ditite um numero de 0 a 9999\n>>> ').strip())

Unidade = Numero // 1 % 10
Dezena = Numero // 10 % 10
Centena = Numero // 100 % 10
Milhar = Numero // 1000 % 10

print('Unidade: {}'.format(Unidade))
print('Dezena: {}'.format(Dezena))
print('Centena: {}'.format(Centena))
print('Milhar: {}'.format(Milhar))
