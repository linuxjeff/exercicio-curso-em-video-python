#!/usr/bin/python3
#
# ex045 - O jogo de jokenpô
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: O jogador escolhe entre peda papel ou tesousa. Depois o
#              CPU e no final vemos quem ganhou.
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
#   - Criadas as vriáveis "Escolha" e "CPUEscolha"
#   - Criado if para devinir quem ganhou
#   - Criado if para colocar escolha no texto da CPU e do Jogador
#   - Removida área de debug de variáveis
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

CPUEscolha = randrange(1, 4)

# -----------------------------------------------------------------------------
# Execução direta

# If escolha do jogador
if Escolha == 1:
    Jogador = 'Papel'

elif Escolha == 2:
    Jogador = 'Pedra'

else:
    Jogador = 'Tesoura'

# If escolha da CPU
if CPUEscolha == 1:
    CPU = 'Papel'

elif CPUEscolha == 2:
    CPU = 'Pedra'

else:
    CPU = 'Tesoura'

# if que mostra quem ganhou
print('Você escolheu: {}\nA CPU escolheu: {}'.format(Jogador, CPU))
if Escolha == CPUEscolha:
    print('Vocês empataram!')
elif Escolha == 1 and CPUEscolha == 2 or Escolha == 2 and CPUEscolha == 3 or Escolha == 3 and CPUEscolha == 1:
    print('Você Ganhou!')
else:
    print('Você perdeu!')
# -----------------------------------------------------------------------------
