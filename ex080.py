#!/usr/bin/env python
#
# ex080 - Recebe cinco números e ordena eles na lista.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Programa recebe cinco números pelo teclado e ordena eles
#   na lista sem usar a função sort.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 11-12-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criado código para receber e ordenar os números
#   - Criado código para mostrar resultados
#
# Licença: MIT.
#
# Variáceis iniciais.
Numeros = list()
###
# Código que recebe o número e organiza na lista.
Digito = int(0)
Maior = int(0)
Numeros.append(int(input('Digite um número: ')))
print(f'O número {Numeros[0]} foi adicionado na posição: 0')
for contador in range(1, 5):
    Digito = int(input('Digite um número: '))
    for Posicao, Numero in enumerate(Numeros):
        if Digito <= Numero:
            print(f'O número {Digito} foi adiconado na posição: {Posicao}')
            Numeros.insert(Posicao, Digito)
            Maior = 0
            break
        else:
            Maior = 1
    if Maior == 1:
        for Posicao, Numero in enumerate(Numeros):
            if Digito >= Numero:
                print(f'O {Digito} foi adicionado na última pocição')
                Numeros.append(Digito)
                break
###
# Código para mostrar os números da lista.
print('_-' * 30)
print('Os números digitados são: ', end='')
for Sort in Numeros:
    print(Sort, end=' ')
###
