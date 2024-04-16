#!/usr/bin/env python
#
# ex107-main - Programa para testar os módulos.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Este programa é para testar os módulos do ex107.py.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 12-04-2024, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho
#   - Criada a área de importação de bibliotecas
#   - Criada a área da variáveis globais
#   - Cridado o programa principal
#
# Licença: MIT.
#
# Importando bibliotecas.
import ex107
###
# Variáveis globais.
preco = float(input('Digite um preço: R$'))
###
# Programa principal.
print(f'A metade de R${preco} é {ex107.metade(preco)}')
print(f'O dobro de R${preco} é {ex107.dobro(preco)}')
print(f'Aumentando 10%, temos R${ex107.aumentar(preco, 10)}')
print(f'Reduzindo 13%, temos R${ex107.diminuir(preco, 13)}')
###
