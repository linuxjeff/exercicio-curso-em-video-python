#!/usr/bin/env python
#
# nome_completo - Guarda as duas notas dos alunos.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Guarda as duas notas dos alunos e calcula a média.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 15-01-2024, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criado código que recebe os alunos e suas notas
#
# Licença: MIT.
#
# Variáveis iniciais
Dados = list()
###
# Código que recebe o cadastro dos alunos e suas notas e já cacula a média.
while True:
    FimCadastro = int(0)
    Nome = input('Nome do aluno: ')
    NotaUm = float(input('Primenira nota: '))
    NotaDois = float(input('Segunda nota: '))
    Media = (NotaUm + NotaDois) / 2
    Dados.append([Nome, [NotaUm, NotaDois, Media]])
    while True:
        Proximo = str(input('Deseja continuar? (S|N)\n>>> ')).upper()
        if Proximo[0] == 'N':
            FimCadastro = 1
            print('Fim do cadastro!')
            break
        elif Proximo[0] == 'S':
            print('Próximo Aluno!')
            break
        else:
            print('Opção invalida! Tente novamente.')
    if FimCadastro == 1:
        break
###
print(Dados)
