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
#   - Criado if para desconto e juros de pagamento
#   - Retirada área de debug
#  v0.0.2 06-10-2023, Jefferson Santana
#   - Modificado a opção 4 do if para pedir o número de parcelas
#
# Licença: MIT.
#

# Variáveis

ValorProduto = float(input('Qual o valor do produto: R$'))

print('Qual a forma de pagamento?')
print('1 - Cheque (á vista) ou dinheiro')
print('2 - Cartão débito ou crédito (á vista)')
print('3 - Cartão de crédito em duas vezes')
print('4 - Cartão de crédito em três vezes ou mais')
FormaPagamento = int(input('>>> '))

# -----------------------------------------------------------------------------
# Execução direta

if FormaPagamento == 1:
    ValorDesconto = (ValorProduto * 10) / 100
    print('Valor do desconto: R${:.2f}'.format(ValorDesconto))
    print('Valor do produto com desconto: R${:.2f}'.format(ValorProduto - ValorDesconto))
elif FormaPagamento == 2:
    ValorDesconto = (ValorProduto * 5) / 100
    print('Valor do desconto: R${:.2f}'.format(ValorDesconto))
    print('Valor do produto com desconto: R${:.2f}'.format(ValorProduto - ValorDesconto))
elif FormaPagamento == 3:
    print('Valor do desconto: R$0.00')
    print('Valor das parcelas: R${:.2f}'.format(ValorProduto / 2))
elif FormaPagamento == 4:
    ValorJuros = (ValorProduto * 20) / 100
    NParcelas = int(input('Qual o número de parcelas?\n>>> '))
    print('Valor do Juros: R${:.2f}'.format(ValorJuros))
    print('Valor da parcelas: R${:.2f}'.format((ValorProduto + ValorJuros) / NParcelas))

# -----------------------------------------------------------------------------
