# Programa para calcular o almento dos funcionarios

# Variáveis

ValorSalarioAtual = float(input('Qual o salário atual do funcionario?\n>>> '))

ValorComAlmento = ((ValorSalarioAtual / 100) * 15) + ValorSalarioAtual

# Execução

print('O valor com almento é: R$ {:.2f}'.format(ValorComAlmento))
