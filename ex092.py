#!/usr/bin/env python
#
# ex092 - Lê nome, ano de nascimento e ctps.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Programa recebe o nome, ano de nascimento e CTPS. Caso tenha
#   CTPS pede o ano de contratação e mostra o resultado na tela.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 07-02-2024, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criado o código para receber os dados
#   - Criado o código que mostra o resultado na tela
#
# Licença: MIT.
#
# Importando bibliotecas
from datetime import date
###
# Variáveis iniciais.
Pessoa = dict()
###
# Código para receber os dados.
Pessoa['Nome'] = str(input('Qual o nome: ')).strip().capitalize()
Ano = int(input('Qual o ano de nascimento: '))
Pessoa['Idade'] = int(date.today().year - Ano)
CTPS = int(input('Carteira de trabalho (0 não tem): '))
Pessoa['CTPS'] = CTPS

if CTPS > 0:
    AnoContratacao = int(input('Ano de contratação: '))
    Pessoa['Contratação'] = AnoContratacao
    Salario = float(input('Sálario: R$ '))
    Pessoa['Sálario'] = Salario
    Pessoa['Aposentadoria'] = (AnoContratacao - Ano) + 35
###
# Código que mostra o resultado na tela.
print('-_' * 30)
for Item, Valor in Pessoa.items():
    print(f'{Item} tem o valor {Valor}')
###
