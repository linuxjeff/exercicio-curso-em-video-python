# Execícior 004

# Variáveis

Conteudo = input('Digite um valor: ')

# Execução
print('O tipo primitivo deste dado é: {}'.format(type(Conteudo)))
print('Só tem espaços? \n Resposta: {}'.format(Conteudo.isspace()))
print('Tem somente números? \n Resposta: {}'.format(Conteudo.isnumeric()))
print('Tem somente letras? \n Resposta: {}'.format(Conteudo.isalpha()))
print('Tem letras e/ou núemros? \n Resposta: {}'.format(Conteudo.isalnum()))
print('Esta somente em maiúsculas? \n Resposta: {}'.format(Conteudo.isupper()))
print('Esta somente em minúculas? \n Resposta: {}'.format(Conteudo.islower()))
print('Esta capitalizado? \n Resposta: {}'.format(Conteudo.istitle()))
