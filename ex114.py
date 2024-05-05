#!/usr/bin/env python
#
# ex114 - Teste se o site esta no ar
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: O programa testa se um site esta funcionando.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 05-05-2024, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criado a área para importar bibliotecas
#   - Criado programa principal que testa se o site esta acessível
#
# Licença: MIT.
#
# Importando bibliotecas
import requests

###
# Programa principal
try:
    resposta = requests.get('https://www.google.com.br')
    print('\033[32mO site esta acessível no momento\033[m')
except:
    print('\033[31mO site não esta inacessível.\033[m')
###
