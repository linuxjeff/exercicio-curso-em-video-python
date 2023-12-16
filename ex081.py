#!/usr/bin/env python
#
# ex081 - Recebe vários números
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Programa recebe vários números e mostra quantos números foram
#   digitados, mostra os números em ordem decrescente e mostra se o número
#   cinco foi digitado.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 14-12-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada área para importa bibliotecas
#   - Criado área das variáveis iniciais
#   - Criado código para receber números
#   - Criado código para mostrar resultados
#
# Licença: MIT.
#
# Importando bibliotecas.
from time import sleep
###
# Variáveis iniciais
Numeros = list()
###
# Código para receber os números e colocalos na lista.
Contador = int(0)

FimCH = int(0)

while FimCH != 1:
    Numeros.append(int(input('Digite um número.\n>>> ')))
    Contador += 1
    while True:
        Opcao = str(input('Deseja continuar? [S/N]\n>>> ')).upper()
        if Opcao[0] == 'S':
            break
        elif Opcao[0] == 'N':
            FimCH = 1
            break
        else:
            print('Opção invalida. Tente novamente!')
            sleep(1)
###
# Código para mostrar o resultado.
print('-_' * 30)
print(f'Você digitou o total de: {Contador}')
Numeros.sort(reverse=True)
print('Os números em ordem decrescente são: ', end='')
for Ordem in Numeros:
    print(Ordem, end=' ')
if 5 in Numeros:
    print('\nFoi encontrado o número 5 na lista.')
else:
    print('\nNão foi encontrado o número 5 na lista.')
###
