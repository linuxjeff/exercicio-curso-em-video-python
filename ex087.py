#!/usr/bin/env python
#
# ex087 - Cria uma matriz
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Programa recebe valores do teclado e cria uma matriz dimencional
#   de 3x3 na saída final do programa.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 26-12-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada a área das variáveis iniciais
#   - Criado o código para receber os números e colocalos na lista Matriz
#   - Criado o código para mostrar a matriz na tela
#  v0.0.2 10-01-2024, Jefferson Santana
#   - Criado o código que mostra os dados de somas dos pares, soma de todos os números da
#     terceira coluna e maior número da segunda linha
#   - Modificado o código para mostrar a matriz na tela
#   - Modificado a área das variáveis iniciais
# Licença: MIT.
#
# Variáveis iniciais.
Matriz = [[], [], []]

Numero =int(0)

SomaPares = int(0)

SomaTerceiraCol = int(0)

MaiorValorLS = int(0)
###
# Código para receber números e colocalos na lista matriz.
for contador in range(0, 3):
    Matriz[0].append(int(input(f'Digite um Valor para [0, {Numero}]: ')))
    Numero += 1

Numero =int(0)

for contador in range(0, 3):
    Matriz[1].append(int(input(f'Digite um Valor para [1, {Numero}]: ')))
    Numero += 1

Numero =int(0)

for contador in range(0, 3):
    Matriz[2].append(int(input(f'Digite um Valor para [2, {Numero}]: ')))
    Numero += 1
###
# Código para mostrar a matriz na tela.
print('_-' * 30)
for Posicao, Digitos in enumerate(Matriz[0]):
    if Digitos % 2 == 0:
        SomaPares += Digitos
    if Posicao == 2:
        SomaTerceiraCol += Digitos
    print(f'[ {Digitos} ]', end='')

print('\n', end='')
for Posicao, Digitos in enumerate(Matriz[1]):
    if Digitos % 2 == 0:
        SomaPares += Digitos
    if Posicao == 2:
        SomaTerceiraCol += Digitos
    if MaiorValorLS == 0 or Digitos > MaiorValorLS:
        MaiorValorLS = Digitos
    print(f'[ {Digitos} ]', end='')

print('\n', end='')
for Posicao, Digitos in enumerate(Matriz[2]):
    if Digitos % 2 == 0:
        SomaPares += Digitos
    if Posicao == 2:
        SomaTerceiraCol += Digitos
    print(f'[ {Digitos} ]', end='')
###
# Código mostra os dados de somas dos pares, soma de todos os números da
# terceira coluna e maior número da segunda linha.
print('\n', end='')
print('_-' * 30)
print(f'A soma dos valores pares é: {SomaPares}')
print(f'A soma dos valores da terceira coluna é: {SomaTerceiraCol}')
print(f'O maior valor da segunda linha é: {MaiorValorLS}')
###
