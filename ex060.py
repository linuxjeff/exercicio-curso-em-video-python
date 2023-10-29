#!/usr/bin/python3
#
# ex060 - Cálcula o fatorial.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Recebe um número e cálcula o seu fatorial.
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 27-10-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada área de variáveis iniciais
#   - Criado while para calcular o Fatorial
#   - Criado o printe para mostrar o resultado
#
# Licença: MIT.
#

# Variáveis iniciais

Numero = int(input('Ditigte um numero para calcular o seu fatorial.\n>>> '))

Fatorial = Numero

RNumero = Numero

###

# While para calcular o fatorial.
while Numero != 1:
    Numero = Numero - 1
    Fatorial = Fatorial * Numero
###
# Printe do resultado
print('O fatorial de {} é: {}'.format(RNumero, Fatorial))
###
