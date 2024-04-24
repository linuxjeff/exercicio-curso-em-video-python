#!/usr/bin/env python
#
# ex111-main - Programa para testar os módulos.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Este programa é para testar os módulos do ex111.py.
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
#   - Devido a mudança na biblioteca ex111 foram aterados linha correspondentes
#  v0.0.4 19-04-2024, Jefferson Santana
#   - Mudanças no programa principal para mostrar as formatações com a nova opção
#  v0.0.5 20-04-2024, Jefferson Santana
#   - Alterado programa principal para usar a def resumo
#  v0.0.6 24-04-2024, Jefferson Santana
#   - Alterado para incluir a função dado
#
# Licença: MIT.
#
# Importando bibliotecas.
from ex111.utilitadescev import moeda
from ex111.utilitadescev import dado

###
# Variáveis globais.
preco = dado.leiadinheiro('Digite um preço: R$')
###
# Programa principal.
moeda.resumo(preco, 80, 35)
###
