#!/usr/bin/env bash
#
# ex042 - Diz se trẽs retas formam um triângulo.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Programa pede três retas e verifica e estas retas conseguem
#              forma um triângulo e qual tipo de triângulo forma.
#
#   Exemplos:
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 13-09-2023, Jefferson Santana
#   - Versão inicial
#  v0.0.2 18-09-2023, Jefferson Santana
#   - Criada área de variáveis
#   - Criadas às variáveis RetaUm, RetaDois e RetaTrês
#   - Criado o debug de variáveis
#
# Licença: MIT.
#

# Variáveis

RetaUm = float(input('Qual o tamanho da primeira reta?\n>>> '))

RetaDois =float(input('Qual o tanhano da segunda reta?\n>>> '))

RetaTres = float(input('Qual o tamanho da segunda reta?\n>>> '))

# -----------------------------------------------------------------------------
# Debug de variáveis

print(RetaUm, RetaDois, RetaTres)

# -----------------------------------------------------------------------------
