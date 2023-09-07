#!/usr/bin/env bash
#
# ex039 - Programa para verificar o andamento do alistamento.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Programa para informar quando deve efetuar o alistamo nas forças
#              armadas.
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 04-09-2023, Jefferson Santana
#   - Versão inicial
#   - Criado a área de variáveis
#   - criado o debug de variáveis
#   - Importando date da biblioteca datetime
#
# Licença: MIT.
#

# Importando Bibliotecas

from datetime import date

# -----------------------------------------------------------------------------
# Varáveis ínicias

AnoDeNascimento = int(input('Qual o ano do seu nascimento?\n>>> '))

AnoAtual = int(date.today().year)

Idade = AnoAtual - AnoDeNascimento

# -----------------------------------------------------------------------------

if Idade == 18:
    print('Você tem que se alista')

# debug de variáveis

print(AnoDeNascimento, AnoAtual, Idade)
