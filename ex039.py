#
# ex039 - Programa para verificar o andamento do alistamento.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Programa para informar quando deve efetuar o alistamo nas forças
#              armadas.
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 04-09-2023, Jefferson Santana
#   - Versão inicial
#   - Criado a área de variáveis
#   - criado o debug de variáveis
#   - Importando date da biblioteca datetime
#   - Criado if para testar a condição do alistamento
#  v0.0.2 28-09-2023, Jefferson Santana
#   - Criada a opção de sexo
#   - Criado a variável sexo
#   - Modificado o if para tem a opção sexo
#   _ Removida área de debug de variáveis
#
# Licença: MIT.
#

# Importando Bibliotecas

from datetime import date

# -----------------------------------------------------------------------------
# Varáveis ínicias

print('Qual seu sexo\n1 - feminino\n2 - masculino')
Sexo = int(input('>>> '))

AnoDeNascimento = int(input('Qual o ano do seu nascimento?\n>>> '))

AnoAtual = int(date.today().year)

Idade = AnoAtual - AnoDeNascimento

# -----------------------------------------------------------------------------
# If para verificar o ano do alistamento.
if Sexo == 2 and Idade == 18:
    print('Você tem que se alista!')
elif Sexo == 2 and Idade < 18:
    print('Seu alistamento será no ano de {}'.format(AnoAtual + (18 - Idade)))
elif Sexo == 2 and Idade > 18:
    print('Seu alistamento era para ser no ano de {}'.format(AnoAtual - (Idade - 18)))
    print('Caso não tenha se apresentado procure o escritório das forças armadas mais próximo.')
else:
    print('Você é do sexo feminido. Seu alistamento não é obrigatório.')
