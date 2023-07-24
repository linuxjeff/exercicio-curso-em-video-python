# Reconhece o nome Silva.
NomeCompleto = input('Escreva seu nome completo.\n>>> ').title().strip()

print('O nome tem sim: {}'.format('Silva' in NomeCompleto))
