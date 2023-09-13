# ex041 - Indica a categoria do atleta.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# Exemplo:
# Qual seu ano de nascimento?
# >>> 2007
# Você é da categoria: junior
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
#   - Criado o IF para testar as idades e passar a categoria
#   - Retirada área de debug
#   - Criada área de exemplo
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
# Execução Direta

if Idade <= 9:
    print('Você é da categoria: mirim')
elif Idade <= 14:
    print('Você é da categoria: infantil')
elif Idade <= 19:
    print('Você é da categoria: junior')
elif Idade <= 20:
    print('Você é da categoria: sênior')
else:
    print('Você é da categoria: Master')

# -----------------------------------------------------------------------------
