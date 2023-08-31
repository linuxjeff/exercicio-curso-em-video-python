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
#   - Criada as varáveis e o debug de variáveis.
#   - Consertado erro de espaço na variável NumeroD
#   - Colocado local mais apropiado para a escolha do número na variável Base.
#   - Criado o if aninhado para converter os nomeros.
#   - Retirado o print de debug.
#
# Licença: MIT.
#

# Variáveis

NumeroD = int(input('Digite um número.\n>>> '))
Base = int(input('Para qual base quer converter seu número?\n1 - Binário\n2 - Hexedecimal\n3 - Octal\n>>> '))

if Base == 1:
    pBinary = format(NumeroD, 'b')
    print('O número {} em binário é: {}'.format(NumeroD, pBinary))
elif Base == 2:
    pHexede = format(NumeroD, 'x')
    print('O número {} em hexedecimal é: {}'.format(NumeroD, pHexede))
elif Base == 3:
    pOctal = format(NumeroD, 'o')
    print('O número {} em octal é: {}'.format(NumeroD,pOctal))