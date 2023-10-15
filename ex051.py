#!/usr/bin/python3
#
# ex051 - cálcula a PA.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Recebe o primeiro termo da PA e sua razão e mostra os próximos
#              dez termos da PA.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 12-10-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada a variável para receber primeiro termo
#   - Criada a variável para receber a razão
#   - Criado o for para gerar oito termos da PA
#   - Criado os prints para mostrar os resultados
#
# Licença: MIT.
#

# Variáveis principais

PrimeiroTermo = int(input('Digite o a1 da PA.\n>>> '))

Razao = int(input('Digite o r da PA.\n>>> '))

# Primeiro termo

print('({}'.format(PrimeiroTermo),end=',')

# For para gerar a PA.

for Contador in range(1, 9):
    PrimeiroTermo = PrimeiroTermo + Razao
    print('{}'.format(PrimeiroTermo),end=',')

print('{})'.format(PrimeiroTermo + Razao))
