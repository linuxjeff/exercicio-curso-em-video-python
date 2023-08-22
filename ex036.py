# Programa para verificar o empréstimo bancário.
#
# v0.0.1
#   - início

# Variáveis

CasaValor = float(input('Qual o valor da casa?\n>>> R$'))

SalarioDoComprador = float(input('Qual o valor do seu salario?\n>>> R$'))

AnosParaPagar = int(input('Em quantos anos pretende pagar?\n>>> '))

ValorParcelas = CasaValor / (AnosParaPagar * 12)

ValorMaxDaParcelas = SalarioDoComprador / 100 * 30

if ValorParcelas > ValorMaxDaParcelas:


# Debug variáveis

print(CasaValor, SalarioDoComprador, AnosParaPagar, ValorParcelas, ValorMaxDaParcelas)
