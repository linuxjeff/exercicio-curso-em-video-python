#!/usr/bin/env python
#
# ex103 - Programa recebe nome e gols feito pelo jogador
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Programa recebe nome e gols feitos pelo jogador e depois mostra
#   o resultado.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 01-04-2024, Jefferson Santana
#   - Versão inicial
#   - Criado cabeçalho do programa
#   - Criada a função ficha
#   - Criada a área de variáveis globais
#   - Criado o código que mostra o resultado(programa principal)
#  v0.0.1 03-04-2024, Jefferson Santana
#   - Melhorada a função ficha para reconhecer número vazios
#
# Licença: MIT.
#
# Funções
def ficha(nome='desconhecido', gols='0'):
    nome.strip().capitalize()
    gols.strip().upper()
    enumero = gols.isnumeric()
    if nome == '' or nome == 'desconhecido':
        nome = '<desconhecido>'
    if enumero:
        gols = gols
    else:
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


###
# Variávés globais
Nome = str(input('Nome do jogador: '))

Gols = input('Número de Gols: ')
###
# Código que mostra o resultado
ficha(Nome, Gols)
###
