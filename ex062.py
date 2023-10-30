#!/usr/bin/python3
#
# ex062 - Mostrar uma PA com termos indefinodos.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Mostra os termos de uma PA e pergunta se deseja ver mais
#   termos.
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 29-10-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criado while para receber opção
#
# Licença: MIT.
#

# Variáveis íniciais

Contador = 0

PrimeiroTermo = int(input('Digite o primeiro termo da PA.\n>>> '))

Razao = int(input('Digite a razão da PA.\n>>> '))

Opcao = 0

OTermo = 0

Rotdatnoc = 8

###
while Opcao != 2:
    OTermo = PrimeiroTermo
    Contador = 0
    Opcao = 0
    # Printe do ínicio da PA.
    print('PA: ({}, '.format(OTermo), end='')
    ###
    # While para calcular oito termos da PA.
    while Contador != Rotdatnoc:
        OTermo += Razao
        print('{}, '.format(OTermo), end='')
        Contador += 1
    ###
    # Printe do último termo da PA.
    print('{})'.format(OTermo + Razao))
    ###
    # Este while recebe a opção e o número de termos a ser mostrados.
    while Opcao != 1 and Opcao != 2:
        Opcao = int(input('Deseja ver mais termos da PA?\nO padrão é dez termos.\n1 - Sim\n2 - Não\n>>> '))
        if Opcao != 1 and Opcao != 2:
            print('Opção invalida. Tente novamente.')
        elif Opcao == 1:
            Rotdatnoc = int(input('Quantos termos deseja ver da PA?\n>>> '))
            if Rotdatnoc <= 10:
                Rotdatnoc = 8
            Rotdatnoc = Rotdatnoc - 2
    ###