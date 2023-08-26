# convert-py - Programa convert números decimal para outras bases
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Programa converte números decimais para binário, hexedecimal e
#              octal
#
#   Exemplos:
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 26-08-2023, Jefferson Santana
#   - Versão inicial
#   - Criada as varáveis e o debug de variávei.
#
# Licença: MIT.
#

# Variáveis

NumeroD = int(input('Digite um número.\n>>>'))

Base = int(input('Para qual base quer converter seu número?\n1 - Binário\n2 - Hexedecimal\n3 - Octal'))

# Debug das variávei
print(NumeroD, Base)
