#!/usr/bin/python3
#
# ex064 - Recebe varios números.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Recebe vários números até que o usuário escolha não digitar mais
#   um número. Depois mostra a média, o número maior e o número menor.
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 04-11-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada área de variáveis
#   - Criado while para receber, contar, somar, verificar o maior número e verificar o menor número
#   - Criados os prints para mostrar o resultados
#
# Licença: MIT.
#

# Variáveis iniciais.

Numero = int(0)

Contador = int(0)

MaiorNumero = int(0)

MenorNumero = int(0)

Saida = str()

Soma = int(0)

###
# While para receber, contar, somar, verificar o maior número e verificar o menor número.
while Saida != 'N':
    Saida = str()
    Numero = int(input('Digite um número.\n>>> '))
    Contador += 1
    Soma = Soma + Numero
    if Numero > MaiorNumero:
        MaiorNumero = Numero
    if MenorNumero == 0 or Numero < MenorNumero:
        MenorNumero = Numero
    while Saida != 'S' and Saida != 'N':
        Saida = str(input('Deseja digitar, mais um número?\nDigite S para sim e Digite N para não.\n>>> ')).upper()
###
# Printes para mostrar os resultados.
print('Você digitou o total de: {}\nA soma dos número é de: {}'.format(Contador, Soma))
print('A média dos números é de:{}'.format(Soma / Contador))
print('O maior número digitado é: {}\nO menor número digitado é: {}'.format(MaiorNumero, MenorNumero))
###
