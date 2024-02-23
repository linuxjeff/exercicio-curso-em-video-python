#!/usr/bin/env python
#
# ex095 - Cadastra o aproventamento de um jogador
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
#  v0.0.2 22-02-2024, Jefferson Santana
#   - Realizada modificação no código que recebe os jogadores
#   - Criado o código para mostrar a tabela com todos os jogadores
#   - Realizada modificações no ódigo para mostrar o resultados
#
# Licença: MIT.
#
# Variáveis iniciais
Jogador = dict()
Gols = list()
Jogadores = list()

FecharWhileReceber = PrintJogador = int(0)
###
# Código para receber os dados.
while True:
    print('-' * 30)
    Jogador['Nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    Total = int(0)
    Jogos = int(input(f'Quantas partidas {Jogador["Nome"]} jogou?\n>>> '))
    for Contador in range(0, Jogos):
        NumeroDeGols = int(input(f'Quantos gols na partida {Contador + 1}: '))
        Total += NumeroDeGols
        Gols.append(NumeroDeGols)
    Jogador['Gols'] = Gols[:]
    Jogador['Total'] = Total
    Jogadores.append(Jogador.copy())
    Jogador.clear()
    Gols.clear()
    while True:
        DesejaContinuar = str(input('Deseja continuar? [S|N]\n>>> ')).upper().strip()
        if DesejaContinuar[0] == 'N':
            FecharWhileReceber = 1
            break
        elif DesejaContinuar[0] == 'S':
            break
        else:
            print('Opçção invalida! Tente novamente.')
    if FecharWhileReceber == 1:
        break

###
# Código para mostrar a tabela com todos os jogadores.
Jlen = len(Jogadores)
print('-_' * 30)
print('Cód  Nome            Gols            Total')
while PrintJogador != Jlen:
    print(f'{PrintJogador + 1:}', end='    ')
    for JogadorL in Jogadores[PrintJogador].values():
        print(f'{JogadorL.__str__():<15}', end=' ')
    print('\n', end='')
    PrintJogador += 1
###
# Código para mostrar o resultados.
ContadorDePartidas = MostrarJogador = int(1)
while MostrarJogador != 999:
    ContadorDePartidas = int(1)
    print('-' * 30)
    MostrarJogador = int(input('Mostrar o dados de qual jogador?\n>>> '))
    if MostrarJogador == 999:
        break
    elif MostrarJogador > Jlen or MostrarJogador < 0:
        print('Opção invalida! Tente novamente.')
    else:
        JogadorReal = MostrarJogador - 1
        print(f'-- Levantamento do jogador {Jogadores[JogadorReal]["Nome"]}:')
        for ValoresGols in Jogadores[JogadorReal]['Gols']:
            print(f'     => Na partida  {ContadorDePartidas}, fez {ValoresGols} gol(s)')
            ContadorDePartidas += 1
        print(f'Foi um total de {Jogadores[JogadorReal]["Total"]} Gol(s).')

print('Volte sempre!')
###