# Progama que verifica quanto de tinta será nescessário para pintar a área de uma parede.

# Variáveis

Altura = float(input('Qual a altura da parede?\n>>> '))

Largura = float(input('Qual a largura da parede?\n>>> '))

Area = Altura * Largura

Calculo = Area / 2

# Execução
print('Litros de tintas necessários: {:.2f}'.format(Calculo))
