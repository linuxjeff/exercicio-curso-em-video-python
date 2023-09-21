#!/usr/bin/python3
#
# ex044 - Programa aplica desconto em valor de compra.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: O programa aplica o desconto ao produto dependendo a forma de
#              pagamento. O programa aceita pagamento em dinheiro, cheque
#              (á vista), cartão crédito e cartão de débito.
#
#   Exemplos:
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 21-09-2023, Jefferson Santana
#   - Versão inicial
#   - Criada área de variáveis
#   - Criado debug de variáveis
#   - Criado variáveis ValorProduto e FormaPagamento
#   - Criado printes para mostrar opções
#
# Licença: MIT.
#

# Variáveis

ValorProduto = float(input('Qual o valor do produto: R$'))

print('Qual a forma de pagamento?')
print('1 - Cheque (á vista) ou dinheiro')
print('2 - Cartão débito ou crédito (á vista)')
print('3 - Cartão de crédito em duas vezes')
print('4 - Cartão de crédito em três vezes')
FormaPagamento = int(input('>>> '))

# -----------------------------------------------------------------------------
# Debug variáveis

print(ValorProduto, FormaPagamento)

# -----------------------------------------------------------------------------
