#!/usr/bin/env python
#
# ex091 - Sortea o dado para quatro jogadores.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Programa sortea o número de um a seis para quatro jogadore e
#   depois coloca em ordem.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 31-01-2024, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criado o código para sortear os números dos jogadores
#   - Criado o código que arruma as posições dos jogadores no pódio
#   - Alterado ordem do pódio
#   - Alterado o código para utilizar apenas uma, dicionário
#   - Colocado a data no cabeçalho
#   - Criado print para imprimir a frase do começo
#   - Criado o código que mostra o rank na tela
#   - Feito a edentação dos printes que mostram o resultado
#
# Licença: MIT.
#
# Importando bibliotecas.
from random import randint
from time import sleep
###
# Variáveis iniciais.
Jogos = dict()
###
# Código para sortear os números dos jogadores.
print('Valores Sorteados:')
for Contador in range(1, 5):
    Jogador = str(f'Jogador{Contador}')
    Jogos[Jogador] = randint(1, 6)
    print(f'   O {Jogador} tirou {Jogos[Jogador]}')
    sleep(0.7)
###
# Código que arruma as posições dos jogadores no pódio.
Nsort = ContadorDaLista = int(0)
Lados = list()
for Lista in Jogos.values():
    Lados.append(Lista)
Lados.sort(reverse=True)
MaxParaWhileDoSort = len(Lados)
while Nsort != MaxParaWhileDoSort:
    for Jog, Dado in Jogos.items():
        if Dado == Lados[ContadorDaLista]:
            Nsort += 1
            del Jogos[Jog]
            Jogos[Jog] = Dado
            break
    ContadorDaLista += 1
###
# Código que mostra o rank na tela.
PosicaoR = int(1)
print('Ranking dos jogadores:')
for Jogador, Dados in Jogos.items():
    print(f'   {PosicaoR}º lugar: {Jogador} com {Dados}')
    PosicaoR += 1
    sleep(0.7)
###
