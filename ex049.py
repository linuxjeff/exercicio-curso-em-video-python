#!/usr/bin/python3
#
# ex049 - Mostra a tabuada de um número
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Ele vai mostrar a tabuada de qualquer número de zero a dez
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 12-10-2023, Jefferson Santana
#   - Versão inicial
#   - Criada área de variável
#   - Criada variável para receber o número
#   - Criado for para gerar tabuada
#   - Criado prints de decoração.
#
# Licença: MIT.
#

# Variáveis principais
Numero = int(input('Digite o número para ver sua tabuada.\n>>> '))

# Principal

print('Tabuada do número: {}'.format(Numero))

print('-' * 15)

for Contador in range(0, 11):
    print('{:^} x {:>2} = {:^}'.format(Numero, Contador, (Numero * Contador)))

print('-' * 15)
