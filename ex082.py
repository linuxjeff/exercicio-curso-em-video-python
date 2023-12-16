#!/usr/bin/env python
#
# nome_completo - Recebe números e separa em pares e impares
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Recebe quantos números forem digitados e separa em duas listas,
#   uma lista dos números pares e outra lista dos números impares
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 16-12-2023, Jefferson Santana
#   - Versão inicial
#   - Criado cabeçalho do programa
#   - Criada área de importação de bibliotecas
#   - Criada área de variáveis iniciais
#   - Criado código para recolher números
#   - Criado código para tratar e mostrar dados
#
# Licença: MIT.
#
# Importando bibliotecas.
from time import sleep
###
# Varáveis iniciais.
Numeros = list()
###
# Código para receber números.
FimCH = int(0)
while FimCH != 1:
    Numeros.append(int(input('Digite um número.\n>>> ')))
    while True:
        Opcao = str(input('Deseja continuar? [S/N]\n>>> ')).upper()
        if Opcao[0] == 'S':
            break
        elif Opcao == 'N':
            FimCH = 1
            break
        else:
            print('Opção invalida. Tente novamente!')
            sleep(1)
###
# Código para tratar e mostrar dados.
Numeros.sort()

Pares = list()

Impares = list()
print('Lista completa em ordem crescente: ', end='')
for Numero in Numeros:
    print(Numero, end=' ')
    if Numero % 2 == 0:
        Pares.append(Numero)
    else:
        Impares.append(Numero)
print('\nNúmeros pares: ', end='')
for Par in Pares:
    print(Par, end=' ')
print('\nNúmeros impares: ', end='')
for Impar in Impares:
    print(Impar, end=' ')
###
