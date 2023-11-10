#!/usr/bin/python3
#
# ex066 - recebe números até ser digitado a flag.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: O programa recebe os números até ser digitado o número flag.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 10-11-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada área de variáveis iniciais
#   - Criado while para receber e somar os números
#   - Criado o print para monstrar o resultado
#
# Licença: MIT.
#

# Variáveis iniciais.

Soma = Contador = int(0)

###
# While para receber e somar número
while True:
    Numero = int(input('Digite um número.\nPara sair do programa digite: 999\n>>> '))
    if Numero == 999:
        break
    Soma += Numero
    Contador += 1
###
# Print para mostrar o resultado.
print(f'Você digitou {Contador} números e a soma  deles é: {Soma}')
###
