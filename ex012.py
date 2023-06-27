# Programa para monstrar 5 porcento de desconto

# Variáveis

Valor = float(input('Qual o valor do produto?\n>>> R$'))

Desconto = float(input('Qual a porcentagem do desconto?\n>>> '))

Calculo = Valor - (Valor * Desconto / 100)

# Execução

print('O valor do Produto com desconto é: R${:.2f}'.format(Calculo))
