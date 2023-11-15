#!/usr/bin/python3
#
# ex064 - Recebe vários numeros
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: O programa recebe vários números até receber o número
#   novecentos e noventa e nove, depois mostra o total de números dititado
#   e soma todos os número digitados.
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 01-11-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada área de variáveis iniciais
#   - Criado while para receber números
#   - Crado print para mostrar o resultado
#
# Licença: MIT.
#

# Variáveis íniciais.

Numero = int(0)

Contador = int(0)

Total = int(0)
# Variáveis íniciais. ##
# While para receber os números.
while Numero != 999:
    Numero = int(input('Para parar digite: 999\nDigite um número.\n>>> '))
    if Numero != 999:
        Contador += 1
        Total = Total + Numero
# While para receber os números. ##
# Printe do resultado.
print('Você digitou {} números. A soma de todos eles é: {}'.format(Contador, Total))
# Printe do resultado. ##
