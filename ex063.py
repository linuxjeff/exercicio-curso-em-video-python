#!/usr/bin/python3
#
# ex063 - Mostra a sequência de Fibonacci.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Recebe n interiro e mostra na tela os nprimeiros elementos de
#   uma sequência de Fibonacci.
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 31-10-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada área para variáveis íniciais- Criado o prnit para exibir frase de destaque
#   - Criado while para calcular a sequência de Fibonacci
#   - Criado print para mostrar o ultimo termo
#   - Criado if para colocar mais um número um caso o primeiro termo seja um
#
# Licença: MIT.
#

# Variáveis íniciais.

Numero = int(input('Digite o primeiro termo da Sequência de Fibonacci.\n>>> '))

NTermos = int(input('Digite os números de termos para ser exibidos.\n>>> ')) - 1

UltimoTermo = int(0)

Inicio = 1

SomaUm = Inicio

SomaDois = Inicio

###
# Exibe a frase para destaque.
print('Sequência de Fibonacci do termo {} e mais {} termos.'.format(Numero, NTermos + 1))
###
# If para colocar mais um número um.
if Numero == 1:
    print('1', end=', ')
    NTermos = NTermos - 1
###
# While para calcular e exibir a sequência de Fibonacci.
while UltimoTermo != NTermos:
    SomaUm = Inicio
    if Inicio >= Numero:
        print('{}'.format(Inicio), end=', ')
        UltimoTermo += 1
    Inicio = SomaUm + SomaDois
    SomaDois = SomaUm
###
# Exibe o ultimo termo.
print(Inicio)
###
