# Programa para verificar o empréstimo bancário.
#
# v0.0.1
#   - início
# v0.0.2
#   - termidado o if para texto de aprovação.
#   - Corrigido erro do if. o printe não estava com variável.
#   - Corrigido erro do printe.

# Variáveis

CasaValor = float(input('Qual o valor da casa?\n>>> R$'))

SalarioDoComprador = float(input('Qual o valor do seu salario?\n>>> R$'))

AnosParaPagar = int(input('Em quantos anos pretende pagar?\n>>> '))

ValorParcelas = CasaValor / (AnosParaPagar * 12)

ValorMaxDaParcelas = SalarioDoComprador / 100 * 30

if ValorParcelas < ValorMaxDaParcelas:
    print('Seu empréstimo foi aprovado e a parcelas tem o valor de: R${:.2f}'.format(ValorParcelas))
else:
    print('O empréstimo não foi aprovado, o valor da parcela excede 30 porcento da sua renda mensal.')

# Debug variáveis

print(CasaValor, SalarioDoComprador, AnosParaPagar, ValorParcelas, ValorMaxDaParcelas)
