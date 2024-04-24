#!/usr/bin/env python
#
# dado - Neste pacote tem várias funções.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: pacote com funções para tratar dados.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 23-04-2024, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do pacote
#   - Criada a função leiadinheiro()
#
# Licença: MIT.
#


def leiadinheiro(valor):
    numeromonetario = False
    texto = valor
    valor = str(input(f'{texto}'))
    contadorlen = len(valor)
    contavirgula = contaponto = int(0)
    while True:
        for c in valor:
            if c.isnumeric():
                numeromonetario = True
            elif c == ',':
                contavirgula += 1
                if contavirgula == 2:
                    print(f'O valor {valor} é invalido.')
                    valor = str(input(f'{texto}'))
                    contadorlen = len(valor)
                    contavirgula = int(0)
                    break
            elif c == '.':
                contaponto += 1
                if contaponto == 2:
                    print(f'O valor {valor} é invalido.')
                    valor = str(input(f'{texto}'))
                    contadorlen = len(valor)
                    contaponto = int(0)
                    break
            else:
                print(f'O valor {valor} é invalido.')
                valor = str(input(f'{texto}'))
                contadorlen = len(valor)
                break
            contadorlen -= 1
        if contadorlen == 0:
            retiravirgula = valor.split(',')
            valor = '.'.join(retiravirgula)
            valor = float(valor)
            return valor
