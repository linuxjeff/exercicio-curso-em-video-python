#!/usr/bin/env python
#
# ex115 - Sistema para cadastro
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: O programa cadastra pessoas e sua idade e quanda em um banco de
#   dado do tipo txt.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 06-05-2024, Jefferson Santana
#   - Versão inicial
#   - Foi criado o cabeçalho do programa
#   - Criada a área de importação de bibliotecas
#   - Programa principal recebe cadastro e mostra quem já foi cadastrados
#   - Mudança na frase da função leiaint() que recebe a opção
#
# Licença: MIT.
#
# Importando bibliotecas
import ex115modulos
from ex111.utilitadescev.moeda import mostrealinha
###
# Programa principal
while True:
    mostrealinha('Menu Principal', 13)
    print('1 - Ver pessoas cadastradas\n2 - Cadastrar nova pessoa\n3 - Sair do sistema')
    opcao = int(ex115modulos.leiaint('>>> ', frasedeerro='Opção invalida!\nTente novamente.').strip())
    if opcao == 1:
        mostrealinha('Pessoas Cadastradas', 12)
        dadosdoscadastros = ex115modulos.crialista(arquivo='cadastro.txt')

        ex115modulos.listaalinhada(dadosdoscadastros)
    elif opcao == 2:
        mostrealinha('Novo Cadastro')
        nome = str(input('Nome: ')).strip().capitalize()
        idade = ex115modulos.leiaint('Idade: ')
        cadastro = ex115modulos.juntastring(nome, idade)
        ex115modulos.escritatxt('cadastro.txt', cadastro)
    elif opcao == 3:
        break
    else:
        print('Opção invalida!\nTente novamente.')
###
