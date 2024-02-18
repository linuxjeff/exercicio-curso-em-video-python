#!/usr/bin/env python
#
# ex094 - Cadastra varias pessoas com sexo e idade.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Programa cadastra pessoas com o sexo e a idade. Depois mostra
#   um relatórios dos dados.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 14-02-2024, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada a área de variáveis iniciais
#   - Criado o código que recebe o cadastro
#
# Licença: MIT.
#
# Variáveis iniciais.

CadastroDePessoas = list()

Mulheres = list()

Pessoa = dict()

Idade = TotalIdade = TotalGrupo = FimDoCadastro = int(0)
###
# Código que recebe o cadastro.
while True:
    Pessoa['Nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        Sexo = str(input('Sexo: [M/F] ')).strip().upper()
        if Sexo[0] == 'M' or Sexo[0] == 'F':
            Pessoa['Sexo'] = Sexo[0]
            break
        else:
            print('Opção invalida! Tente novamente.')
    if Pessoa['Sexo'] == 'F':
        Mulheres.append(Pessoa['Nome'])
    Idade = int(input('Idade: '))
    Pessoa['Idade'] = Idade
    TotalIdade += Idade
    TotalGrupo += 1
    CadastroDePessoas.append(Pessoa.copy())
    Pessoa.clear()
    while True:
        QuerContinuar = str(input('Quer Continuar? [S|N]\n>>> ')).strip().upper()
        if QuerContinuar[0] == 'N':
            FimDoCadastro = 1
            break
        elif QuerContinuar[0] == 'S':
            break
        else:
            print('Opção invalida! Tente novamnete.')
    if FimDoCadastro == 1:
        break
###
print(Mulheres, Pessoa, TotalIdade, TotalGrupo, CadastroDePessoas)
