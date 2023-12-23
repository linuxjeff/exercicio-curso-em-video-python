#!/usr/bin/env python
#
# ex085 - Programa recebe sete números.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: O programa recebe sete numeros e separa em duas listas de
#   numeros pares e impares.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 23-12-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada a área de variáveis iniciais
#   - Criado o código que recebe os números e separa na lista Pares e Impares e depois coloca tudo na lista Numeros
#   - Criado o código que mostra os números pares
#   - Criado o código que mostra os números impares
#
# Licença: MIT.
#
# Variáveis iniciais.
Numeros = list()

Pares = list()

Impares = list()
###
# Código recebe números e coloca nas listas Pares e Impares. Depois coloca as duas listas na lista Numeros.
for Numero in range(1, 8):
    Valor = int(input(f'Digite o {Numero}º número: '))
    if Valor % 2 == 0:
        Pares.append(Valor)
        Pares.sort()
    else:
        Impares.append(Valor)
        Impares.sort()
    if Numero == 7:
        Numeros.append(Pares[:])
        Numeros.append(Impares[:])
##
# Separação.
print('_-' * 30)
###
# Código para mostrar números impares.
print('Números pares: ', end='')
Par = Numeros[0]
LenPares = len(Par)
for Posicao, NuPar in enumerate(Par):
    if LenPares == 1:
        print(NuPar)
    elif LenPares != Posicao + 1:
        print(NuPar, end=', ')
    else:
        print(NuPar)
###
# Código para mostrar números impares.
print('Números impares: ', end='')
Impar = Numeros[1]
LenImpares = len(Impar)
for Posicao, NuImpar in enumerate(Impar):
    if LenImpares == 1:
        print(NuImpar)
    elif LenImpares != Posicao + 1:
        print(NuImpar, end=', ')
    else:
        print(NuImpar)
###
