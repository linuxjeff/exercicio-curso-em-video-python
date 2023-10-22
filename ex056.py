#!/usr/bin/python3
#
# ex056 - Recebe nome, idade e sexo.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Recebe nome, idade e sexo de quatro pessoas. Fala a média de
#              idade, o homem mais velo e e quantas mulheres tem menos de
#              vinte.
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 19-10-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho
#   - Criada área de variáveis
#   - Criado for para receber cadastro das pessoas e filtrar os dados.
#   - Criados prints para escrever o resultados na tela.
#
# Licença: MIT.
#

# Variáveis
Media = 0

HomemVelho = ''

IdadeVelho = 0

MulheresMenorVinte = 0
####

# For para receber e testar pessoas cadastradas.
for pessoas in range(1, 5):
    Nome = str(input('Qual seu Nome?\n>>> ')).lstrip().rstrip().title()
    Idade = int(input('Qual a sua idede?\n>>> '))
    Sexo = str(input('Qual seu sexo?\nDigite H (homem) e M (mulher).\n>>> ')).lstrip().rstrip().upper()
    Media = Media + Idade
    if Sexo == 'H' and Idade > IdadeVelho:
        IdadeVelho = Idade
        HomemVelho = Nome
    if Sexo == 'M' and Idade < 20:
        MulheresMenorVinte = MulheresMenorVinte + 1
###

# Escrevendo resultados na tela.
print('A média de idade das quatro pessoas é de: {:.0f}'.format(Media/4))
print('O homem mais velho é: {}'.format(HomemVelho))
print('O número de mulheres menores de 20 anos é de: {}'.format(MulheresMenorVinte))
###
