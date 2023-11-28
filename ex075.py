#!/usr/bin/env python
#
# ex075 - Recebe quatro números.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Recebe quatro números e diz quantas vezes o nove apareceu.
#   Diz em qual posição pareceu o primeiro três. Mostra quais form o número
#   pares.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 27-11-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criado variáveis para receber valores da tupla
#   - Criado código para verificar números nove
#   - Criado código para verificar em qual posição aparece o primeiro três
#   - Criado código para contabilizar números pares
#
# Licença: MIT.
#
# Recebendo números e armazena na tuplas.
NumeroUm = int(input('Digite um número\n>>> '))
NumeroDois = int(input('Digite um número\n>>> '))
NumeroTres = int(input('Digite um número\n>>> '))
NumeroQuatro = int(input('Digite um número\n>>> '))

Numeros = (NumeroUm, NumeroDois, NumeroTres, NumeroQuatro)
print()
###
CNove = int(0)
# Mostra quantos números nove foram digitados.
for Nove in Numeros:
    if Nove == 9:
        CNove += 1
if CNove > 0:
    print(f'Foram encontrados {CNove} números nove.')
else:
    print(f'Foram encontrados {CNove} números nove.')
###
# Verifica em qual posição aparece o primeiro número três.
Tres = int(0)
CTres = int(0)
for Tres in Numeros:
    CTres += 1
    if Tres == 3:
        break
if Tres == 3:
    print(f'O primeiro número três esta na posição: {CTres}')
else:
    print('Não foi encontrado o número três.')
###
# Contabiliza os números pares.
print('Números pares: ', end='')
for Par in Numeros:
    if Par % 2 == 0:
        print(f'{Par}', end=' ')
###