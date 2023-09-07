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
#   - Criado if para testar a condição do alistamento
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
# If para verificar o ano do alistamento.
if Idade == 18:
    print('Você tem que se alista!')
elif Idade < 18:
    print('Seu alistamento será no ano de {}'.format(AnoAtual + (18 - Idade)))
elif Idade > 18:
    print('Seu alistamento era para ser no ano de {}'.format(AnoAtual - (Idade - 18)))
    print('Caso não tenha se apresentado procure o escritório das forças armadas mais próximo.')

# debug de variáveis

print(AnoDeNascimento, AnoAtual, Idade)
