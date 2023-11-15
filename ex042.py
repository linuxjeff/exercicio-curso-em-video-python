#!/usr/bin/env bash
#
# ex042 - Diz se trẽs retas formam um triângulo.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Programa pede três retas e verifica e estas retas conseguem
#              forma um triângulo e qual tipo de triângulo forma.
#
#   Exemplos:
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 13-09-2023, Jefferson Santana
#   - Versão inicial
#  v0.0.2 18-09-2023, Jefferson Santana
#   - Criada área de variáveis
#   - Criadas às variáveis RetaUm, RetaDois e RetaTrês
#   - Criado o debug de variáveis
#   - Criado o if para testar as retas
#   - Criado o if para dizer qual é o tipo do triângulo
#   - Retirado área de debug de variáveis
#
# Licença: MIT.
#

# Variáveis

RetaUm = float(input('Qual o tamanho da primeira reta?\n>>> '))

RetaDois =float(input('Qual o tanhano da segunda reta?\n>>> '))

RetaTres = float(input('Qual o tamanho da segunda reta?\n>>> '))

# -----------------------------------------------------------------------------
# Execução direta

# If para testar as retas.
if RetaUm + RetaDois > RetaTres and RetaDois + RetaTres > RetaUm and RetaTres + RetaUm > RetaDois:
    print('As três retas formam um triângulo.')
    # If para dizer qual o tipo do triângulo.
    if RetaUm == RetaDois and RetaDois == RetaTres:
        print('Este triângulo é do tipo equilátero.')
    elif RetaUm == RetaDois or RetaDois == RetaTres or RetaTres == RetaUm:
        print('Este triângulo é do tipo isósceles.')
    else:
        print('Este triângulo é do tipo escaleno.')
else:
    print('As três retas não formam um triângulo.')

# -----------------------------------------------------------------------------
