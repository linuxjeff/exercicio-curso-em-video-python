#!/usr/bin/python3
#
# ex057 - Recebe o sexo da pessoa.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Recebe o sexo da pessoa e termina qunado a resposta for correta.
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 26-10-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho
#   - Criado while para testar a variável Sexo
#
# Licença: MIT.
#

# Variáveis de início.

Sexo = ''

###

# While para testar "Sexo".
while Sexo != 'M' and Sexo != 'F':
    Sexo = str(input('Digite seu sexo. [M para masculino e F para feminino]\n>>> ')).upper()
    if Sexo != 'M' and Sexo != 'F':
        print('Opção invalida!\nTente novamente.')
    else:
        if Sexo == 'M':
            print('Você é do sexo masculino.')
        else:
            print('Você é do sexo feminino.')
