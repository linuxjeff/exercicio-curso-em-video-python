#!/usr/bin/python3
#
# ex052 - Jogo de adivinhação.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: A CPU sorteia um número e o jogador tem que adivinhar qual numero
#   que foi.
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 26-10-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada área de variáveis inícias
#   - Criado o while para testar o aceto do jogador
#
# Licença: MIT.
#

# Impotado biblioteca(s)

from random import randint

# Variáveis iníciais

Tentativas = 0

NumeroDaCPU = randint(0, 10)

NumeroDoJogador = int(11)

###

# While que testa o acerto do jogador.
while NumeroDoJogador != NumeroDaCPU:
    # Recebendo a resposta do jogado.
    NumeroDoJogador = int(input('Eu pensei em um número de zero(0) a dez(10).\nQual foi o número?\n>>> '))
    # If testa a responta, acrenta as tentativas e informa caso tenha acertado.
    if NumeroDoJogador != NumeroDaCPU:
        Tentativas += 1
    else:
        Tentativas += 1
        print('Você acertou!\n'
              'O número que pensei foi mesmo o número: {}\n'
              'E você tentou {} antes de acerta.'.format(NumeroDaCPU, Tentativas))

###
