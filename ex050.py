#!/usr/bin/python3
#
# ex050 - Mostra a soma dos números pares.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Programa lê seis números e soma somente os pares.
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 12-10-2023, Jefferson Santana
#   - Versão inicial
#   - Criado cabeçalho
#   - Criada área de variáveis principais
#   - Criado for para somar nímeros pares
#   - Criado print para mostrar soma final.
#   - Adicionado comentário(s) para ajudar a letura do código.
#
# Licença: MIT.
#

# variáveis principais

Soma = 0

# For para somar números.

for Contador in range(1, 7):
    Numero = int(input('Digite um número.\n>>> '))
    if Numero % 2 == 0:
        Soma = Soma + Numero

# Print que mostra a soma dos números pares.

print('Soma dos valores pares digitados: {}'.format(Soma))
