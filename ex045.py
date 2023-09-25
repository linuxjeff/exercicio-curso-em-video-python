#!/usr/bin/python3
#
# ex045 - O jogo de jokenpô
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: O jogador escolhe entre peda papel ou tesousa. Depois o
#              CPU escolhe e no final vemos quem ganhou.
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 25-09-2023, Jefferson Santana
#   - Versão inicial
#   - Criado área para importa bibliotáca
#   - importando função randrange da bibliotéca random
#   - Criada área de variáveis
#   - Criada área de debug de variáveis
#   - Criada área de execução direta
#   - Criadas as vriáveis "Escolha" e "CPU"
#   - Cirado if para devinir quem ganhou
#
#
# Licença: MIT.
#

# Importado bibliotéca

from random import randrange

# -----------------------------------------------------------------------------
# Variáveis

print('Jokenpô!')
print('Escolha uma das opções!')
print('1 - Papel')
print('2 - Pedra')
print('3 - Tesoura')
Escolha = int(input('>>> '))

CPU = randrange(1, 4)

# -----------------------------------------------------------------------------
# Execução direta

if Escolha == CPU:
    print('Vocês empataram!')
elif Escolha == 1 and CPU == 2 or Escolha == 2 and CPU == 3 or Escolha == 3 and CPU == 1:
    print('Você Ganhou!')
else:
    print('Você perdeu!')
# -----------------------------------------------------------------------------
# Debug de variáveis

print(Escolha, CPU)

# -----------------------------------------------------------------------------
