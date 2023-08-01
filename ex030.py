# Programa para saber se um número é impar ou par

numero = int(input('Impar ou par?!\nDigite um número.\n>>> '))

modulo = numero % 2

if modulo == 1:
    print('O número é impar!')
else:
    print('O número digitado é par!')
