#!/usr/bin/python3
#
# ex053 - Verifica se a frase é um palíndromo.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Este programa recebe uma frase e verificar se ela é um
#              palíndromo.
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 15-10-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho
#   - Criada área de variáveis
#   - Criado o FOR para inveter frese
#   - Cirado o IF para verificar se a frase é um palíndromo
#
# Licença: MIT.
#

# Variáveis

TrocaDeCara = str.maketrans({' ': '', '.': '', '!': '', '?': '', ',': ''})

Frase = input('Digite uma frase.\n>>> ').lower().strip().lstrip().translate(TrocaDeCara)

Valor = len(Frase)

ContagemDeCaracteres = Valor - 1

Esarf = ''

# For para inveter frese.
for c in range(0, Valor):
    Esarf = Esarf + Frase[ContagemDeCaracteres]
    ContagemDeCaracteres = ContagemDeCaracteres - 1

# If para verificar se a frase é um palíndromo.
if Frase == Esarf:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo.')
