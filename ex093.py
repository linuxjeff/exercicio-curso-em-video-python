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
#   - Criado o ódigo para mostrar o resultados
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
Jogos = int(input(f'Quantas partidas {Jogador["Nome"]} jogou?\n>>> '))
for Contador in range(0, Jogos):
    NumeroDeGols = int(input(f'Quantos gols na partida {Contador + 1}: '))
    Total += NumeroDeGols
    Gols.append(NumeroDeGols)
Jogador['Gols'] = Gols
Jogador['Total'] = Total
###
# Código para mostrar o resultados.
ContadorDePartidas = int(1)
print('-_' * 30)
print(Jogador)
print('-_' * 30)
for Descricao, Item in Jogador.items():
    print(f'O campo {Descricao} tem o valor: {Item}')
print('-_' * 30)
print(f'O jogador {Jogador["Nome"]} jogou {Jogos} partidas')
for ValoresGols in Jogador['Gols']:
    print(f'     => Na partida  {ContadorDePartidas}, fez {ValoresGols} gol(s)')
    ContadorDePartidas += 1
print(f'Foi um total de {Jogador["Total"]} Gol(s).')
###
