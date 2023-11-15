#!/usr/bin/env python
#
# ex067 - Mostra a tabuada.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Programa mostra a tabuada de um número digitado. O programa é
#   encerrado quando for digitado um número negadivo.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 10-11-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criado while para receber o número
#   - Criada variável para receber o número a ser mutiplicado
#   - Criado if para encerrar o programa
#   - Criado for que cria a tabuada
#
# Licença: MIT.
#
# While para receber o número.
while True:
    # Variável para receber o número a ser mutiplicado.
    Numero = int(input('Digite um número para ver sua tabuada.\n>>> '))
    ###
    # If para encerrar o programa.
    if Numero < 0:
        break
    ###
    # For que cria a tabuada.
    for Contador in range(1, 11):
        print(f'{Contador:>2} x {Numero:^} = {Contador*Numero:>2}')
    ###
###
