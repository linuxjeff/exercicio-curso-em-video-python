#!/usr/bin/env python
#
# ex107 - Modulos -> aumentar(), diminuir(), dobro() e metade().
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Este módulo é voltado para calculor de moeda.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 12-04-2024, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do módulo
#   - Criada a def aumentar
#   - Criado a def diminuir
#   - Criado a def dobro
#   - Criado a def metade
#
# Licença: MIT.
#

def aumentar(p=10, por=10):
    p = p + ((p * por) / 100)
    return p


def diminuir(p=10, por=10):
    p = p - ((p * por) / 100)
    return p


def dobro(p=10):
    p = p * 2
    return p


def metade(p=10):
    p = p / 2
    return p
