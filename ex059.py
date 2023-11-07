#!/usr/bin/python3
#
# ex059 - Uma calculadora
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Programa recebe dois número e realiza uma operação matemática
#   escolhida.
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 27-10-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada área para variáveis iníciais
#   - Criado while para o teste
#   - Criado o if para operação com números
#   - Criado o if para ver qual número é maior
#   - Criado um elif para opção cinco(5) e o else ficou para opção inválida
#
# Licença: MIT.
#

# Variáveis iníciais

NumeroUm = float(input('Digite um número.\n>>> '))

NumeroDois = float(input('Digite outro número.\n>>> '))

Opcao = 0

###

# while para testar os números recebidos.
while Opcao != 5:
    # Variável que recebe a opção do while.
    Opcao = int(input('Digite o número da opção escolhida. ↓\n'
                      '1 - Somar\n2 - multiplicar\n3 - Maior\n'
                      '4 - Novos números\n5 - Sair\n>>> '))
    # If que faz os testes dos números.
    if Opcao == 1:
        print('A soma de {} com {} é {}'.format(NumeroUm, NumeroDois, NumeroUm+NumeroDois))
    elif Opcao == 2:
        print('{} mutiplicado por {} é igual a {}'.format(NumeroUm, NumeroDois, NumeroUm * NumeroDois))
    elif Opcao == 3:
        # if para testar qual é o maior número.
        if NumeroUm == NumeroDois:
            print('O número {} é igual ao número {}'.format(NumeroUm, NumeroDois))
        elif NumeroUm > NumeroDois:
            print('O número {} é maior que o {}'.format(NumeroUm, NumeroDois))
        else:
            print('O número {} é maior que o número {}'.format(NumeroDois, NumeroUm))
    elif Opcao == 4:
        NumeroUm = float(input('Digite um número.\n>>> '))

        NumeroDois = float(input('Digite outro número.\n>>> '))
    elif Opcao == 5:
        print('Até a próxima! :)')
    else:
        print('Opção inválida!')

