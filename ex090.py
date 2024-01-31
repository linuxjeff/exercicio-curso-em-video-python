#!/usr/bin/env python
#
# ex090 - Recebe a média de um aluno
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Programa recebe a média de um aluno e mostra na tela sua
#   situação.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 xx-xx-xxxx, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada a área das variáveis iniciais
#   - Criado o código para receber nome e média e mostrar a situação final do aluno
#
# Licença: MIT.
#
# Variáveis iniciais.
aluno = dict()
###
# Código para receber nome e média e mostrar a situação final do aluno.
aluno['nome'] = str(input('Digite o nome do aluno: ')).capitalize()

aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

print(f'Nome é igual a {aluno["nome"]}')

print(f'Média é igual a {aluno["media"]}')

if aluno['media'] > 5:
    print('Situação igual a Aprovado')
else:
    print('Situação é igual a Reprovado')
###
