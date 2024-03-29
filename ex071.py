#!/usr/bin/env python
#
# ex071 - Calcula quantas notas seram entregue.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Programa simula um caixa eletronico
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 13-11-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada área das variáveis inicias
#   - Criado while para cácular o números de cedulas
#   - Criado print para mostrar o resultado
#   - While foi modificado para só mostrar resultado quando tiver cedulas de um determinado valor
#   - Retirado o print para mostrar o resultado do final
#
# Licença: MIT.
#

# Variáveis iniciais
Valor = int(input('Qual o valor você quer sacar?\nR$'))

ControleDeCedula = int(50)
###
# Calculado quantas cédulas de cada valor serão necessárias.
while True:
    # If para cálculo das cédulas.
    if ControleDeCedula == 50:
        Mod50 = Valor // 50
        Valor = Valor - (Mod50 * 50)
        ControleDeCedula = 20
        if Mod50 > 0:
            print(f'Total de cédula(s) de 50 reias: {Mod50}')
    if ControleDeCedula == 20:
        Mod20 = Valor // 20
        Valor = Valor - (Mod20 * 20)
        ControleDeCedula = 10
        if Mod20 > 0:
            print(f'Total de cédula(s) de 20 reias: {Mod20}')
    if ControleDeCedula == 10:
        Mod10 = Valor // 10
        Valor = Valor - (Mod10 * 10)
        ControleDeCedula = 1
        if Mod10 > 0:
            print(f'Total de cédula(s) de 10 reias: {Mod10}')
    if ControleDeCedula == 1:
        Mod1 = Valor // 1
        Valor = Valor - (Mod1 * 1)
        if Mod1 > 0:
            print(f'Total de cédula(s) de um real: {Mod1}')
        break
    ###
###
