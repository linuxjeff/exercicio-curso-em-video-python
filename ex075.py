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
#   - A variável CNove foi movida para o local correto
#   - Criado código para mostrar os números digitados
#   - Modificação para mostrar a opção nenhum caso não tenha números pares
#   - Modificação para consertar a opção nenhum
#  v0.0.2 05-12-2023, Jefferson Santana
#   - Correção no texto
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
# Números digitados.
print('Você digitou o números: ', end='')
for Mostrar in Numeros:
    print(Mostrar, end=' ')
print('\n')
##
# Mostra quantos números nove foram digitados.
CNove = int(0)
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
Pares = int(0)
print('Números pares: ', end='')
for Par in Numeros:
    if Par % 2 == 0:
        print(f'{Par}', end=' ')
    else:
        Pares += 1
        if Pares == 4:
            print('Nenhum')
            break
###