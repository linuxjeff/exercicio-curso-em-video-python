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
#
# Licença: MIT.
#

# Variáveis

Altura = float(input('Qual a sua altura?\n>>> '))

Peso = float(input('Qual o seu peso?\n>>> '))

IMC = Peso / Altura

# -----------------------------------------------------------------------------
# Debug de variáveis

print(Altura, Peso, IMC)

# -----------------------------------------------------------------------------
