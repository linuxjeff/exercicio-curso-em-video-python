#!/usr/bin/env python
#
# ex084 - Recebe nome e peso das pessoas
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Programa recebe nome e peso de várias pessoas e mostra quantas
#   pessoas foram cadastradas os mais pesados e os menos pesados.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 19-12-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada a área de importação de bibliotecas
#   - Criada a área de variáveis iniciais
#   - Criado o código para receber o nome e o peso das pessoas e contar o número de cadastros
#   - Criado o código para analizar e mostrar as pessoas com maior peso
#   - Criado o código para analizar e mostrar as pessoas com maior peso
#   - Feito alteração no print para consequir exibir corretamente quando ouver apenas um resultado
#
# Licença: MIT.
#
# Importando bibliotecas.
from time import sleep
###
# Variáveis iniciais.
Pessoas = list()

Cadastro = list()
###
# Código para receber o nome e o peso e contar quantas pessoas foram cadastradas.
Sair = str()
Contador = int(0)
while Sair != 'N':
    Contador += 1
    Cadastro.append(str(input('Digite o nome da pessoa: ')).title())
    Cadastro.append(int(input('Digite o peso da pessoa: ')))
    Pessoas.append(Cadastro[:])
    Cadastro.clear()
    while True:
        Sair = str(input('Você deseja continuar? [S|N]\n>>> ')).upper()
        if Sair[0] == 'N':
            break
        elif Sair[0] == 'S':
            break
        else:
            print('Opção invalida. Favor tente novamente!')
            sleep(1)
print(f'Você cadastrou ao todo: {Contador}')
###
# Código para analizar o maior peso e  mostrar o resultado.
ListaMaior = list()
MaiorPeso = int(0)
for Pessoa in Pessoas:
    if Pessoa[1] > MaiorPeso:
        ListaMaior.clear()
        ListaMaior.append(Pessoa[0])
        MaiorPeso = Pessoa[1]
    elif Pessoa[1] == MaiorPeso:
        ListaMaior.append(Pessoa[0])
print(f'O maior peso foi {MaiorPeso}Kg. As pessoas com este peso são:  ', end='')
MaiorFim = len(ListaMaior)
for PosicaoMaior, PessoaMaior in enumerate(ListaMaior):
    if MaiorFim == 1:
        print(f'{PessoaMaior}.')
    elif MaiorFim == PosicaoMaior + 1:
        print(f' e {PessoaMaior}.')
    elif MaiorFim - 1 == PosicaoMaior + 1:
        print(PessoaMaior, end='')
    else:
        print(PessoaMaior, end=', ')
###
# Código para analizar o menor peso e mostrar o resultado.
ListaMenor = list()
MenorPeso = int(0)
for Pessoa in Pessoas:
    if Pessoa[1] < MenorPeso or MenorPeso == 0:
        ListaMenor.clear()
        ListaMenor.append(Pessoa[0])
        MenorPeso = Pessoa[1]
    elif Pessoa[1] == MenorPeso:
        ListaMenor.append(Pessoa[0])
print(f'O menor peso foi {MenorPeso}Kg. As pessoas com este peso são: ', end='')
Menofim = len(ListaMenor)
for PosicaoMenor, PessoaMenor in enumerate(ListaMenor):
    if Menofim == 1:
        print(print(f'{PessoaMenor}.'))
    elif Menofim == PosicaoMenor + 1:
        print(f' e {PessoaMenor}.')
    elif Menofim - 1 == PosicaoMenor + 1:
        print(PessoaMenor, end='')
    else:
        print(PessoaMenor, end=', ')
###
