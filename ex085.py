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
#   - Programa reescrito utilizando logica pedida no exercício
#   - Criada a área de variáveis iniciais
#   - Criado o código para receber os números e colocá-los na lista (Pares ou impares) correspondente
#   - Criado o código para mostrar os números pares
#   - Criado o código para mostrar os números impares
#
#
# Variáveis Iniciais.
Numeros = [[], []]
###
# Recebe os números e coloca na lista (Pares ou impares) correspondente.
for Contatdor in range(1, 8):
    NovoNumero = int(input(f'Digite o {Contatdor}º número: '))
    if NovoNumero % 2 == 0:
        Numeros[0].append(NovoNumero)
        Numeros[0].sort()
    else:
        Numeros[1].append(NovoNumero)
        Numeros[1].sort()
###
# Mostra os números pares.
print('O(s) número(s) par(es): ', end='')
LenPar = len(Numeros[0])
for Posicao, Par in enumerate(Numeros[0]):
    if LenPar == 1:
        print(f'{Par}')
    elif LenPar != Posicao + 1:
        print(f'{Par}', end=', ')
    else:
        print(f'{Par}')
###
# Mostra os números ímpares
print('O(s) número(s) impar(es): ', end='')
LenImpar = len(Numeros[1])
for Posicao, Impar in enumerate(Numeros[1]):
    if LenImpar == 1:
        print(f'{Impar}')
    elif LenImpar != Posicao + 1:
        print(f'{Impar}', end=', ')
    else:
        print(f'{Impar}')
###
