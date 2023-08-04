# calcular o amento de salário

Salario = float(input('Digite o valor do salário do funcionário.\n>>> R$ '))

if Salario <= 1250:
    Salario = (Salario*15/100)+Salario
else:
    Salario = (Salario*10/100)+Salario

print('O novo salário será de: R$ {:.2f}'.format(Salario))
