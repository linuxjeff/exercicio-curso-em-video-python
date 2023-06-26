# Programa para converter reias em dolares

# Variáveis
Reais = float(input('Quantos reais você tem?\n>>> R$'))
Dolares = Reais / 3.27

# Execução
print('Com R${:.2f} você compra ${:.2f}'.format(Reais, Dolares))
