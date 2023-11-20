#!/usr/bin/env python
#
# ex072 - Mostra nome do número por extenso.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Recebe um número pelo teclado e mostra seu nome por extenso.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 20-11-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada área de importação de biblioteca
#   - Criada área de variáveis iniciais
#   - Criado while para receber número e testar se esta entre um e vinte
#   - Criado print para mostrar o resultado
#
# Licença: MIT.
#
# Importando bibliotecas.
from time import sleep
###
# Variáaveis iniciais.
Numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

Extenso = int(0)
###
# Recebe o número e verifica se esta entre um e vinte.
while True:
    Extenso = int(input('Qual o número de um(1) a vinte(20)?\n>>> '))
    if 0 <= Extenso <= 20:
        break
    else:
        print('Opção invalida! Tente novamente. ;)')
        sleep(1.5)
###
# Escreve o resultado.
print(f'{Numeros[Extenso]}')
###
