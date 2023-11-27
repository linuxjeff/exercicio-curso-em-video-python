#!/usr/bin/env python
#
# ex074 - Coloca cinco números aleatórios em uma tupla.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: O programa coloca cinco números em uma tupla. Depois mostra o
#   maior e o menor.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 xx-xx-xxxx, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho
#   - Criada área para importa bibliotecas
#   - Criada área de variáveis iniciais
#   - Criador for para mostrar os números sorteados
#   - Criado for para pegar o maior e o menor número
#   - Criado print para mostrar o resultados
#
# Licença: MIT.
#
# Importando bibliotecas.
from random import randint

###
# Variáveis iniciais.
Numeros = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
###
# Mostra os cinco números.
print('Números:', end=' ')
for MNumero in Numeros:
    print(MNumero, end=' ')
###
# Mostra maior e menor valor.
print('\n')
MaiorNumero = int(0)
MenorNumero = int(-1)
for MNumero in Numeros:
    if MNumero > MaiorNumero:
        MaiorNumero = MNumero
    if MenorNumero == -1 or MNumero < MenorNumero:
        MenorNumero = MNumero
###
# Mostrar o maior e o menor.
print(f'O maior número foi: {MaiorNumero}')
print(f'O menor número foi: {MenorNumero}')
###
