# Programa para passar informações sobre o nome

# Variáveis

NomeCompleto = input('Qual o seu nome completo?\n>>> ')

NomeCompleto = NomeCompleto.strip()

ListaDoNome = NomeCompleto.split()

Caracteres = ''.join(NomeCompleto.split())

print('Nome com letras maiúsculas: {}'.format(NomeCompleto.upper()))
print('Nome com letras maiúsculas: {}'.format(NomeCompleto.lower()))
print('O nome completo tem {} caracteres.'.format(len(Caracteres)))
print('O primeito nome tem {} caracteres.'.format(len(ListaDoNome[0])))
