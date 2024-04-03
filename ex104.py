#!/usr/bin/env python
#
# ex104 - Recebe um número e verifica se é um número interiro
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Programa verifica se o valor digitado é um número inteiro.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 03-04-2024, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada a função leiaint que verifica se o conteudo é um número inteiro
#   - Criado o código principal para mostrar o resultado
#
# Licença: MIT.
#
# Funçãoes
def leiaint(frase=''):
    numero = str(input(f'{frase}')).upper().strip()
    inteiro = numero.isnumeric()
    while True:
        if inteiro:
            numero = int(numero)
            break
        else:
            print('ERRO! Digite um número inteiro válido.')
            numero = str(input(f'{frase}')).upper().strip()
            inteiro = numero.isnumeric()
    return numero


###
# Código principal
Onumero = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número: {Onumero}')
###
