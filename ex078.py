#!/usr/bin/env python
#
# ex078 - Recebe cinco números pelo teclado
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: programa recebe cinco número pelo teclado e analiza o maior
#   e o menor e mostra em qual posição foram colocados.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 09-12-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada área de variáveis iniciais
#   - Criado código para receber cinco números pelo teclado
#
# Licença: MIT.
#
# Variáveis iniciais.
Numeros = list()
###
# Código para receber númneros
for Contador in range(0, 5):
    Numeros.append(int(input('Digite um número: ')))
###