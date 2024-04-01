#!/usr/bin/env python
#
# ex102 - Calcula o fatorial
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Programa recebe um número natural maior ou igual a dois e
#   calcula seu fatorial.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 22-03-2024, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criado a função fatorial
#   - Criado o código que mostra o resultado(Programa principal)
#
# Licença: MIT.
#
# Funções
def fatorial(numero, show=False):
    '''
    fatorial(numero, show=False)
    -> Calcula o fatorial de um número.
    :param numero: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor  do Fatorial de um número n.
    '''
    anterior = numero
    total = 0
    while numero != 0:
        if show:
            if numero == 1:
                print(f'{numero}', end='=')
            else:
                print(f'{numero}', end='x')
        numero = numero - 1
        anterior = anterior * numero
        if numero == 1:
            total = anterior

    return total


###
# Código para mostrar o resultado
print('-' * 30)
print(fatorial(5, True))
###
