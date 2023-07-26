# Informa quantos letras a tem no texto

LetrasA = input('Digite uma frase.\n>>> ').lower().strip()

print('O número de letras a é: {}'.format(LetrasA.count('a')))
print('O primeiro a esta na posição: {}'.format(LetrasA.find('a')))
print('O ultimo a esta na posição: {}'.format(LetrasA.rfind('a')))
