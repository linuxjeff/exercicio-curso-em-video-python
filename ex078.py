#!/usr/bin/env python
#
# ex078 - Recebe cinco números pelo teclado
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: programa recebe cinco número pelo teclado e analiza o maior
#   e o menor e mostra em qual posição foram colocados.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 09-12-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada área de variáveis iniciais
#   - Criado código para receber cinco números pelo teclado
#   - Criado código para mostrar maior e menor números e suas posições
#   - Melhoria para mostrar a posição que o número vai oculpar
#   - Criado código para mostrar números digitados
#
# Licença: MIT.
#
# Variáveis iniciais.
Numeros = list()
RealPosicao = int(1)
###
# Código para receber númneros
for Contador in range(0, 5):
    Numeros.append(int(input(f'Digite um número {RealPosicao}: ')))
    RealPosicao += 1
###
# Código para mostrar os números digitados
print(f'Você digitou os números: ', end='')
for EmNumeros in Numeros:
    print(EmNumeros, end=' ')
###
# Código para mostrar o maior e menor números e suas posições.
Maior = max(Numeros)
Menor = min(Numeros)
print(f'\nMaior número é {Maior}, ele esta na(s) Posição(ães): ', end='')
for Posicao, Numero in enumerate(Numeros):
    if Numero == Maior:
        print(Posicao + 1, end=' ')
print(f'\nMaior número é {Menor}, ele esta na(s) Posição(ães): ', end='')
for Posicao, Numero in enumerate(Numeros):
    if Numero == Menor:
        print(Posicao + 1, end=' ')
###
