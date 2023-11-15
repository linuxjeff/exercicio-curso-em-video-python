#!/usr/bin/python3
#
# ex054 - Mostra quem já compretou a maior idade.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Recebe sete anos de nacimento e cálcula quais anos já passaram
#              da maior idade.
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 16-10-2023, Jefferson Santana
#   - Versão inicial
#   - Criado cabeçalho
#   - Criada área de impotações de bibliotecas
#   - Criado área de variáveis
#   - Criado for para pegar os anos
#   - Criado if para testar a maior idade
#   - Criado print para imprimir o resultado na tela
#   - Colocados algumas execução do programa clear para limpar a tela do console
#
# Licença: MIT.
#

# Importando biblioteca

from datetime import date
from os import system

# Variáveis

TodosDeMaior = 0

AnoAtual = date.today().year

# Limpa a tela
system('export TERM=xterm ; clear') or None

# For para pegar e cálcular anos
for nascimento in range(1, 8):
    Ano = int(input('Qual o seu ano de nascimento?\n>>> '))
    if 21 <= (AnoAtual - Ano):
        TodosDeMaior = TodosDeMaior + 1
    # Limpa a tela
    system('export TERM=xterm ; clear') or None

# Print para informar o resultado.
print('Dos sete {} são de maior e {} são de menor.'.format(TodosDeMaior, (7 - TodosDeMaior)))
