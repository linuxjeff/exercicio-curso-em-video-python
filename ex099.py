#!/usr/bin/env python
#
# ex096 - Analisa qual o maior número através da def.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Recebe números pelo teclado e analisa qual o maior número
#   através da def.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 13-03-2024, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada a área de importação de bibliotecas
#   - Criada a área das DEFs
#   - Criada a área dos exemplos
#   - Criada a defs maios que analisa o maior número
#
# Licença: MIT.
#
# Importando Bibliotecas.
from time import sleep


###
# Área das defs.
def maior(*num):
    print('-_' * 30)
    valores = len(num)
    maior = int(0)
    print('Analisando os valores passados...')
    for numeros in num:
        sleep(0.5)
        print(f'{numeros}', end=' ')
        if numeros < 0:
            if maior == 0 or numeros > maior :
                maior = numeros
        else:
            if maior == 0 or numeros > maior :
                maior = numeros
    sleep(0.5)
    print(f'Foram informados {valores} valores ao todo.')
    sleep(0.5)
    print(f'O maior número informado foi: {maior}')


###
# Área de exemplos
maior(1, 4, 8)

maior(7, 9, 5, 4)

maior(45, 91, 88, 72, -92)
###
