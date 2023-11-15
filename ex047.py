#!/usr/bin/python3
#
# ex047 - Contador de pares.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Conta todos os número pares de um a cinquenta.
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 09-10-2023, Jefferson Santana
#   - Versão inicial
#   - importada biblioteca time
#   - criado o for para contar números pares
#
# Licença: MIT.
#
# -----------------------------------------------------------------------------
# importando bibliotecas

from time import sleep

# -----------------------------------------------------------------------------
# Execução

for c in range(2, 51, 2):
    print(c)
    sleep(0.5)

# -----------------------------------------------------------------------------
