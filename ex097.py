#!/usr/bin/env python
#
# ex097 - Programa recebe frases e faz um decoração
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: O programa rece uma frase e fas uma decoração com duas linhas
#   uma emcima e outra embaixo.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 08-03-2024, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criado a def que cria o título decorado
#   - Criada área de exemplo
#  v0.0.2 18-03-2024, Jefferson Santana
#   - Erros de sintaxe corrigidos
#
# Licença: MIT.
#
# Declarando defs.
def mostrealinha(msg):
    tamanholen = len(msg) + 6
    print('-' * tamanholen)
    print(f'{msg:^{tamanholen}}')
    print('-' * tamanholen)


###
# Aŕea de exemplos
mostrealinha('Gustavo Guanabara')

mostrealinha('Curso de Python no YouTube')

mostrealinha('CeV')
###
