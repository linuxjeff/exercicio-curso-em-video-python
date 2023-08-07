# Indica se o ano é bissexto

from calendar import isleap
from datetime import date

Ano = int(input('Digite um ano, digite 0 para analizar o ano atual.\n>>> '))

if Ano == 0:
    Ano = date.today().year

if str(isleap(Ano)) == 'True':
    print('O ano {} é bissexto!'.format(Ano))
else:
    print('O ano {} não é bissexto!'.format(Ano))
