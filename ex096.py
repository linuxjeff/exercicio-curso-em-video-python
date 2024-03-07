#!/usr/bin/env python
#
# ex096 - Calcula a área do terrono.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: este programa calcula a área do terreno.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 07-03-2024, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada a def que mostra um título centralizado e decorado com linhas
#   - Criada a def para calcular a área do terreno
#   - Criado o código que recebe e passa os número para a def Mostrealinha e para def Area
#
# Licença: MIT.
#
# Declaração de DEFs
# A def MostresLinha mostra um título decorado com duas linhas.
def MostreaLinha(msg):
    tamanholen = len(msg) + 6
    print('-' * tamanholen)
    print(f'{msg:^{tamanholen}}')
    print('-' * tamanholen)


# Esta def calcula a áea do terreno
def Area(lar, com):
    print(f'A área de um terreno {lar}x{com} é de {lar * com}m².')


###
# código que recebe e passa os número para a def Mostrealinha e para def Area.
MostreaLinha('Controle de Terrenos')
Largura = float(input('LARGURA (m): '))
Comprimento = float(input('COMPRIMENTO (m): '))

Area(Largura, Comprimento)
###
