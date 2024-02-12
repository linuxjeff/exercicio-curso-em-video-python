#!/usr/bin/env python
#
# ex093 - Cadastra o aproventamento de um jogador
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: O programa recebe o números de jogos e os gols feitos nos jogos
#   de um jogador. Depois mostra o aproveitamento.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 10-02-2024, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada a área de variáveis iniciais
#   - Criado o código para receber os dados
#
# Licença: MIT.
#
# Variáveis iniciais
Jogador = dict()
Gols = list()
###
# Código para receber os dados.
Jogador['Nome'] = str(input('Nome do jogador: ')).strip().capitalize()
Total = int(0)
Jogos = int(input('Quantos Jogos ele jogou?\n>>> '))
for Contador in range(0, Jogos):
    NumeroDeGols = int(input(f'Quantos gols na partida {Contador + 1}: '))
    Total += NumeroDeGols
    Gols.append(NumeroDeGols)
Jogador['Gols'] = Gols
Jogador['Total'] = Total
###
print(Jogador, Jogos, Gols, Total)
