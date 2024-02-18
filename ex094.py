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
#   - Criado o código para mostrar resultados
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
# Código para mostrar resultados.
print('-_' * 30)
print(f'- O grupo tem {TotalGrupo} pessoas.')
MediaDeIdade = TotalIdade / TotalGrupo
print(f'- A média de idade é de {MediaDeIdade:.2f} anos.')
print('- As mulheres cadastradas foram: ', end='')
Mulheres.sort()
for Mulher in Mulheres:
    print(f'{Mulher}', end=' ')
print('\n- Lista das pessoas que estão acima da média: ')
print('\n', end='')
for Cadastro in CadastroDePessoas:
    if Cadastro['Idade'] > MediaDeIdade:
        for Item, Valor in Cadastro.items():
            print(f'{Item} = {Valor}', end='; ')
        print('\n')
###