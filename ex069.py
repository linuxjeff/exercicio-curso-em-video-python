#!/usr/bin/env python
#
# ex069 - Cadastro de pessoas
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Programa cadastra pessoas por idade e sexo.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 10-11-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada área de variáveis iniciais
#   - Criado while para receber idade e sexo
#   - Criado print para mostrar o resultado
#
# Licença: MIT.
#

# Variáveis iniciais.
MaiorDeIdade = Homens = MulheresComMenosDeVinte = int(0)
###
# While para receber idade e sexo. Ele também contabiliza o resultado.
while True:
    # Limpando a variáavel.
    Sexo = Continuar = str('')
    ###
    # Pegando a idade.
    Idade = int(input('Qual a idade?\n>>> '))
    ###
    # Pegando o sexo.
    while Sexo != 'F' and Sexo != 'M':
        Sexo = str(input('Qual o sexo? [F/M]\n>>> ')).strip().upper()[0]
        if Sexo != 'F' and Sexo != 'M':
            print('Opção inválida!\nTente novamente.')
    ###
    # Pegando a opção de continuar.
    while Continuar != 'S' and Continuar != 'N':
        Continuar = str(input('Deseja continuar? [S/N]\n>>> ')).strip().upper()[0]
        if Continuar != 'S' and Continuar != 'N':
            print('Opção inválida!\nTente novamente.')
    ###
    # If para somar maores de 18 anos.
    if Idade > 18:
        MaiorDeIdade += 1
    ###
    # If para somar quantos homens foram cadastrados.
    if Sexo == 'M':
        Homens += 1
    ###
    # If somar a mulheres menores de vinte.
    if Sexo == 'F' and Idade < 20:
        MulheresComMenosDeVinte += 1
    if Continuar == 'N':
        break
###
# Mostrando resultados.
print(f'Temos {MaiorDeIdade} pessoas maior de Idade.'
      f'\nAo todo temos {Homens} homem(ns).'
      f'\nE temos {MulheresComMenosDeVinte} mulher(es) com mais de 20 anos de idade.')
###
