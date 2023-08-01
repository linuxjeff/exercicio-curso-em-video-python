# Indica se o ano é bissexto

from calendar import isleap

Ano = int(input('Digite um ano.\n>>> '))

if str(isleap(Ano)) == 'True':
    print('O ano é bissexto!')
else:
    print('O ano não é bissexto!')
