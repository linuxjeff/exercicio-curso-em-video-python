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
#  v0.0.1 xx-xx-xxxx, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criado o código para sortear os números dos jogadores
#   - Criado o código que arruma as posições dos jogadores no pódio
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
for Contador in range(1, 5):
    Jogador = str(f'Jogador{Contador}')
    Jogos[Jogador] = randint(1, 6)
    print(f'O {Jogador} tirou {Jogos[Jogador]}')
    sleep(0.7)
###
# Código que arruma as posições dos jogadores no pódio.
Nsort = ContadorDaLista = int(0)
Lados = list()
CopiaDaJogo = Jogos.copy()
for Lista in CopiaDaJogo.values():
    Lados.append(Lista)
Lados.sort()
MaxParaWhileDoSort = len(Lados)
Jogos.clear()
while Nsort != MaxParaWhileDoSort:
    for Jog, Dado in CopiaDaJogo.items():
        if Dado == Lados[ContadorDaLista]:
            Nsort += 1
            Jogos[Jog] = Dado
            del CopiaDaJogo[Jog]
            break
    ContadorDaLista += 1
###
print(Lados, CopiaDaJogo, Jogos)


