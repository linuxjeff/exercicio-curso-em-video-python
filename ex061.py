#!/usr/bin/python3
#
# ex061 - Calcula uma PA
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Progragrama calcula os dez primeiros termos de uma PA.
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 29-10-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada área de variáveis íniciais
#   - Criado print do ínicio da PA
#   - Criado while para calcular o meio da PA
#   - Criado print para mostrar o fim da PA
#
# Licença: MIT.
#

# Variáveis íniciais

Contador = 0

PrimeiroTermo = int(input('Digite o primeiro termo da PA.\n>>> '))

Razao = int(input('Digite a razão da PA.\n>>> '))

###
# Printe do ínicio da PA.
print('PA: ({}, '.format(PrimeiroTermo), end='')
###
# While para calcular oito termos da PA.
while Contador != 8:
    PrimeiroTermo += Razao
    print('{}, '.format(PrimeiroTermo), end='')
    Contador += 1
###
# Printe do último termo da PA.
print('{})'.format(PrimeiroTermo + Razao))
###