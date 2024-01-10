#!/usr/bin/env python
#
# ex086 - Cria uma matriz
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
# Licença: MIT.
#
# Variáveis iniciais.
Matriz = [[], [], []]

Numero =int(0)
###
# Código para receber números e colocalos na lista matriz.
for contador in range(0, 3):
    Matriz[0].append(input(f'Digite um Valor para [0, {Numero}]: '))
    Numero += 1

Numero =int(0)

for contador in range(0, 3):
    Matriz[1].append(input(f'Digite um Valor para [1, {Numero}]: '))
    Numero += 1

Numero =int(0)

for contador in range(0, 3):
    Matriz[2].append(input(f'Digite um Valor para [2, {Numero}]: '))
    Numero += 1
###
# Código para mostrar a matriz na tela.
print('_-' * 30)
for Digitos in Matriz[0]:
    print(f'[ {Digitos} ]', end='')

print('\n', end='')
for Digitos in Matriz[1]:
    print(f'[ {Digitos} ]', end='')

print('\n', end='')
for Digitos in Matriz[2]:
    print(f'[ {Digitos} ]', end='')
###
