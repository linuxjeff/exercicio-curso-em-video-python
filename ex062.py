#!/usr/bin/python3
#
# ex062 - Mostrar uma PA com termos indefinodos.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Mostra os termos de uma PA e pergunta se deseja ver mais
#   termos.
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 29-10-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criado while para receber opção
#  v0.0.2 09-11-2023, Jefferson Santana
#  - O while foi refeito para mostrar o número de termos desejados a seguir
#  - Incluido um contador de termos
#
# Licença: MIT.
#

# Variáveis íniciais

Numero = int(input('Qual o primeiro termo da PA\n>>> '))

Razao = int(input('Qual a razão da PA?\n>>> '))

Contador = int(0)

PA = Numero

Parada = int(10)

Soma = int(0)

ContadorDeTermos = int(0)

###
# While para fazer a PA
while Contador != Parada:
    print('{} '.format(PA), end='')
    Contador += 1
    PA = PA + Razao
    if Contador == Parada:
        ContadorDeTermos = ContadorDeTermos + Parada
        Soma = int(input('\nVocê deseja mais quantos termos?\n>>> '))
        Contador = 0
        Parada = Soma
###
print('Foram mostrados {} termos.'.format(ContadorDeTermos))
