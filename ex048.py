#!/usr/bin/python3
#
# ex048 - Soma números mutiplos de três
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Soma os números multiplos de três de um a quinhentos.
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 09-10-2023, Jefferson Santana
#   - Versão inicial
#   - criado cabeçalho
#   - Criado for para somar mutiplos
#   - Criado print para mostrar resultado
#
# Licença: MIT.
#

mutiplos = 0

for contador in range(1, 501):
    if c % 3 == 0:
        mutiplos = mutiplos + contador
print('A soma dos multiplos é: {}'.format(mutiplos))
