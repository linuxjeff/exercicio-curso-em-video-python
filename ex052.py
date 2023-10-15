#!/usr/bin/python3
#
# ex052 - Fala se um número é primo
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Recebe um número e informa se ele é primo ou não é primo.
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 15-10-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho
#   - Criada a variável Numero para receber o número
#   - Criada a variável NDivisores para somar o divisores
#   - Criado o for para somar os divisores e testar se é divisivel
#   - Criado o if para mostrar se é primo ou composto
#
# Licença: MIT.
#

# Variáveis

Numero = int(input('Digite um número.\n>>> '))

NDivisores = 0

# For para verificar se é primo

for Contador in range(1, Numero+1):
    # If para acrescentar o divisor a variável.
    if Numero % Contador == 0:
        NDivisores = NDivisores + 1

# If para mostra se é primo ou composto.
if NDivisores == 2:
    print('O número {} é primo.'.format(Numero))
else:
    print('O número {} é composto.'.format(Numero))
