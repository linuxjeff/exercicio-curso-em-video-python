#!/usr/bin/env python
#
# ex106 - Mostra a ajuda interadiva
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Mostra a ajuda interadiva de cada programa.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 05-04-2024, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada a área para importar bibliotecas
#   - Criada a função mostrealinha
#   - Criado o códgo principal
#
# Licença: MIT.
#
# importando bibliotecas
from time import sleep
###
# Funçoes
def mostrealinha(msg):
    tamanholen = len(msg) + 6
    print('-' * tamanholen)
    print(f'{msg:^{tamanholen}}')
    print('-' * tamanholen)


###
# Código principal.
while True:
    mostrealinha('Sistema de ajuda PyHELP')
    comando = str(input('Função ou Biblioteca > ')).strip().lower()
    if comando == 'fim':
        mostrealinha('Até Logo! :)')
        break
    mostrealinha(f'Acesando manual do comando {comando}')
    help(comando)
    sleep(10)
###
