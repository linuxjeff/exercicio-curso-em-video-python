#!/usr/bin/python3
#
# nome_completo - Programa para calcular o IMC.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Este programa cálcula o IMC de um indivíduo e diz em qual faixa
#              ele está de peso.
#
#   Exemplos:
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 18-09-2023, Jefferson Santana
#   - Versão inicial
#   - Criada área de variáveis
#   - Criado o debug de variáveis
#   - Criadas às variáveis Altura e Peso
#  v0.0.2 21-09-2023, Jefferson Santana
#   - Criada variável IMC
#   - Criado if de teste do IMC
#   - Criada shebang do python
#
# Licença: MIT.
#

# Variáveis

Altura = float(input('Qual a sua altura?\n>>> '))

Peso = float(input('Qual o seu peso?\n>>> '))

IMC = Peso / Altura

# -----------------------------------------------------------------------------
# Execução direta

if IMC <= 18.50:
    print('Abaixo do peso!')
elif 18.50 < IMC <= 25:
    print('Peso ideal. :)')
elif 25 < IMC <= 30:
    print('Sobrepeso!')
elif 30 < IMC <= 40:
    print('Obesidade!')
elif IMC > 40:
    print('Obesidade mórbida')

# -----------------------------------------------------------------------------
