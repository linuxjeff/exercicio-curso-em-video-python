#!/usr/bin/env python
#
# ex098 - Contador personalizado
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Programa recebe três parametros e gera uma contagem aparti
#   dele.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 11-03-2024, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada a área de importação de bibliotecas
#   - Criada a área das defs
#   - Criada a área de exemplos
#   - Criada o código para receber e mostrar a contagem
#  v0.0.2 13-03-2024, Jefferson Santana
#   - Modificado o ano da versão anterior
#   - Modificada a def contador para fazer a inversão de números negativos
#   - Modificada a def contador para fazer a inversão do zero para um
#
#
# Licença: MIT.
#
# Importado bibliotecas
from time import sleep


# Defs

def contador(inicio, fim, passo):
    if passo < 0:
        passo = passo * -1
    elif passo == 0:
        passo = 1
    print('-_' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if fim <= 0:
        fim = fim + -1
    elif fim <= inicio:
        fim = fim - 1
    else:
        fim = fim + 1
    if fim < inicio:
        passo = passo - (passo * 2)
    for numero in range(inicio, fim, passo):
        sleep(0.5)
        print(numero, end=' ')
    print('FIM')


###
# Área de exemplos.
contador(0, 10, 1)

contador(10, 0, 2)
###
# Código para receber e mostrar a contagem.
print('-_' * 30)
Inicio = int(input('Inicío: '))
Fim = int(input('Fim: '))
Passo = int(input('Passo: '))

contador(Inicio, Fim, Passo)
###
