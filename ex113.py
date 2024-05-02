#!/usr/bin/env python
#
# ex113 - O programa recebe dois valores.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: O programa recebe um valor inteiro e um valor flutuante.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 01-05-2024, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada a função leiaint() para validar a leitura de números inteiros
#   - Criada a função leiaflot() para validar a leitura de númeroa reais
#   - Criado o programa principal que recebe os números e mostra o resultados
#
# Licença: MIT.
#
# Funções
def leiaint(valor):
    valorint = True
    numero = int(0)
    while valorint:
        try:
            numero = int(input(f'{valor}').strip())
            valorint = False
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não dititar este número.\033[m')
            numero = int(0)
            break
        except:
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')

    return numero


def leiaflot(valor):
    valorflot = True
    numero = float(0)
    while valorflot:
        try:
            numero = float(input(f'{valor}').replace(',', '.').strip())
            valorflot = False
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não dititar este número.\033[m')
            valorflot = False
            numero = float(0)
        except:
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')

    return numero


# Programa principal.
intvalor = leiaint("Digite um Inteiro: ")
flovalor = leiaflot("Digite um Real: ")
print(f'O valor inteiro digitado foi {intvalor} e o real foi {flovalor}')
