#!/usr/bin/env python
#
# ex100 - Sortea vários valores e soma os pares.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: O programa tedm duas defs uma faz o sorteio dos valores e a
#   outra soma somente os números pares.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 15-03-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada a área de importação de bibliotecas
#   - Criada a área das DEFs
#   - Criada a def sortea que sortea cinco números
#   - Criada a def somapar que soma somente os numeros pares em uma lista
#   - Criada a área das variáveis iniciais
#   - Criado o código de execução principal
#
# Licença: MIT.
#
# Importando bibliotecas.
from random import randint
from time import sleep


###
# Área das DEFs
def sortea(lista):
    print('Sorteando cinco valores da lista: ', end='')
    for numero in range(1, 6):
        paralista = randint(0, 10)
        sleep(0.5)
        if numero == 5:
            print(f'{paralista} PRONTO!')
        else:
            print(f'{paralista}', end=' ')
        lista.append(paralista)


def somapar(lista):
    somadospares = int(0)
    for numero in lista:
        if numero % 2 == 0:
            somadospares += numero
    print(f'Somando os números pares de {lista}, temos {somadospares}')


###
# Área de variáveis iniciais.
NumerosAleatorios = list()
###
# Código de execução principal.
sortea(NumerosAleatorios)
somapar(NumerosAleatorios)
###
