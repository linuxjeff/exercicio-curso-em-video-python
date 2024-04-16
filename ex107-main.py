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
#  v0.0.2 16-04-2024, Jefferson Santana
#   - Adicionado a função moeda para formatar os valores
#
# Licença: MIT.
#
# Importando bibliotecas.
import ex107
from ex108 import moeda
###
# Variáveis globais.
preco = float(input('Digite um preço: R$'))
###
# Programa principal.
print(f'A metade de {moeda(preco)} é {moeda(ex107.metade(preco))}')
print(f'O dobro de {moeda(preco)} é {moeda(ex107.dobro(preco))}')
print(f'Aumentando 10%, temos {moeda(ex107.aumentar(preco, 10))}')
print(f'Reduzindo 13%, temos {moeda(ex107.diminuir(preco, 13))}')
###
