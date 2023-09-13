# ex041 - Indica a categoria do atleta.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Vai mostrar a qual categoria de natação que o atleta pertence.
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 13-09-2023, Jefferson Santana
#   - Versão inicial
#   - Criada área de variáveis
#   - Criado debug de variáveis
#   - Criada área de importação de bibliotecas
#   - importada a biblioteca datetime
#   - Criada a variável "Idade"
#
# Licença: MIT.
#

# importando bibliotecas

from datetime import date

# -----------------------------------------------------------------------------
# Variável

AnoDeNascimento = int(input('Qual seu ano de nascimento?\n>>> '))

Idade = date.today().year - AnoDeNascimento

# -----------------------------------------------------------------------------
# Debug de variáveis

print(AnoDeNascimento, Idade)

# -----------------------------------------------------------------------------
