#!/usr/bin/python3
#
# ex046 - Contagem regressiva
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Cria uma contagem regressiva para os fogos de fim de ano.
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 06-10-2023, Jefferson Santana
#   - Versão inicial
#   - Importada a biblioteca time
#   - importada a biblioteca datetime
#   - criado for para contagem regressiva
#
# Licença: MIT.
#
# -----------------------------------------------------------------------------
# Importando biblióteca

from time import sleep

from datetime import date

# -----------------------------------------------------------------------------

for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('Feliz {}!!'.format(date.today().year + 1))
