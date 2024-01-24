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
#   - Criado código que mostra os alunos e suas médias
#   - Criado código para mostrar notas de cada aluno por escolha do usuário
#
# Licença: MIT.
#
# Variáveis iniciais
Dados = list()
###
# Código que recebe o cadastro dos alunos e suas notas e já cacula a média.
while True:
    FimCadastro = int(0)
    Nome = input('Nome do aluno: ').capitalize()
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
# Código mostra os alunos e suas médias.
print('N° Nome            Média')
for Posicao, Aluno in enumerate(Dados):
    print(f'{Posicao + 1}  {Dados[Posicao][0]:<18}{Dados[Posicao][1][2]:.1f}')
###
# Código para mostrar notas de cada aluno por escolha por escolha do usuário.
Inicio = int(0)
while True:
    if Inicio == 1:
        print('N° Nome            Média')
        for Posicao, Aluno in enumerate(Dados):
            print(f'{Posicao + 1}  {Dados[Posicao][0]:<18}{Dados[Posicao][1][2]:.1f}')
        AlunaN = int(input('Digite o número do aluno: '))
        print(f'{Dados[AlunaN - 1][0]:<18}{Dados[AlunaN - 1][1][0]:.1f}, {Dados[AlunaN - 1][1][1]:.1f}')
    elif Inicio == 2:
        break
    while True:
        VerNotas = str(input('Deseja ver a nota de algum aluno? [S|N]\n>>> ')).upper()
        if VerNotas[0] == 'N':
            Inicio = 2
            break
        elif VerNotas[0] == 'S':
            Inicio = 1
            break
###
