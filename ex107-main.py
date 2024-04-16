#!/usr/bin/env python
#
# ex109-main - Programa para testar os módulos.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Este programa é para testar os módulos do ex109.py.
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
#  v0.0.3 16-04-2024, Jefferson Santana
#   - Devido a mudança na biblioteca ex109 foram aterados linha correspondentes
#  v0.0.4 19-04-2024, Jefferson Santana
#   - Mudanças no programa principal para mostrar as formatações com a nova opção
#
# Licença: MIT.
#
# Importando bibliotecas.
from ex109 import moeda
###
# Variáveis globais.
preco = float(input('Digite um preço: R$'))
###
# Programa principal.
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preco, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(preco, 13)}')
###
