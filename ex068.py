#!/usr/bin/env python
#
# ex063 - Jogo de par ou irpar.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Você joga par ou irpar contra a CPU. Ao perder é mostrado sua
#   pontuação.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 10-11-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada área para importar biblioteca
#   - Criada área de variáveis iniciais
#   - Criado while para testar a vitoria ou derrota do jogador
#
# Licença: MIT.
#

# Importando bibliotecas.
from random import randint
###
# Variáveis iniciais.
ParOuImpar = ''

ContadorDeVitorias = int(0)
###
# While para realizar o teste.
while True:
    ParOuImpar = ''
    SeuNumero = int(input('Qual o seu número?\n>>> '))
    CPUNumero = randint(0, 10)
    # While para repitir opção Par ou Impar.
    while ParOuImpar != 'P' and ParOuImpar != 'I':
        ParOuImpar = str(input('Você quer par ou impar?\n[P ou I]\n>>> ')).upper().strip()[0]
        if ParOuImpar != 'P' and ParOuImpar != 'I':
            print('Opção Invalida!\nTente Novamente.')
    ###
    Soma = SeuNumero + CPUNumero
    Resultado = Soma % 2
    # If para mostrar frese.
    if Resultado == 0:
        print(f'Você escolheu {SeuNumero} e a CPU escolheu {CPUNumero}. Total de {Soma} deu par!')
    else:
        print(f'Você escolheu {SeuNumero} e a CPU escolheu {CPUNumero}. Total de {Soma} deu impar!')
    ###
    # If para testar se ganhou ou perdeu.
    if Resultado == 0 and ParOuImpar == 'P':
        print('Você ganhou!')
        ContadorDeVitorias += 1
    elif Resultado == 1 and ParOuImpar == 'I':
        print('Você ganhou!')
        ContadorDeVitorias += 1
    else:
        print(f'Você perdeu! Vitória(s) {ContadorDeVitorias}')
        break
    ###
###
