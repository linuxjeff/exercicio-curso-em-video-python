# Recebe trẽs números e diz qual é o maior e qual é o menor.

Primeiro = int(input('Digite o primeiro número.\n>>> '))

Segundo = int(input('Digite o segundo número.\n>>> '))

Terceiro = int(input('Digite o terceiro número.\n>>> '))

print(Primeiro, Segundo, Terceiro)

# Menor
if Primeiro < Segundo:
    if Primeiro < Terceiro:
        Menor = Primeiro
    else:
        Menor = Terceiro
else:
    if Segundo < Terceiro:
        Menor = Segundo
    else:
        Menor = Terceiro

# Maior
if Primeiro > Segundo:
    if Primeiro > Terceiro:
        Maior = Primeiro
    else:
        Maior = Terceiro
else:
    if Segundo > Terceiro:
        Maior = Segundo
    else:
        Maior = Terceiro

print('O menor número é: {}'.format(Menor))
print('O Maior número é: {}'.format(Maior))
