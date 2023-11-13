#!/usr/bin/env python
#
# ex070 - Calculadora de compra
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Programa recebe nome e valor de vários produtos e calcular o
#   total da compra. Também mostra os produtos acima de mil reais e o produto
#   mais barato.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 13-11-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada área de variáveis iniciais
#   - Criado while para receber o produto e seu valor e realizar os calculos
#   - Criado o print para mostrar o resultado
#
# Licença: MIT.
#

# Variáveis iniciais.
ValorTotal = MenorValor = float(0)

MaiorDeMil = int(0)
###
# Recebendo e calculando os produtos.
while True:
    # Variáveis do while.
    ValorDoProduto = float(0)
    NomeDoProduto = str('')
    RespostaDaSaida = str('')
    ValorDoProduto = float(input('Digite o valor do produto: R$'))
    NomeDoProduto = str(input('Digite o nome do produto.\n>>> '))
    ###
    # Teste se a opção de continuar ou sair esta correta.
    while RespostaDaSaida != 'S' and RespostaDaSaida != 'N':
        RespostaDaSaida = str(input('Quer continuar? [S/N]\n>>> ')).strip().upper()[0]
        if RespostaDaSaida != 'S' and RespostaDaSaida != 'N':
            print('Opção inválida!\nTente novamente. ;)')
    ###
    # Somando os valores dos produtos.
    ValorTotal += ValorDoProduto
    ###
    # Verificando se o produto tem o valor acima de mil.
    if ValorDoProduto > 1000:
        MaiorDeMil += 1
    ###
    # Verificando se o produto é o mais barato.
    if MenorValor == 0 or MenorValor > ValorDoProduto:
        MenorValor = ValorDoProduto
        MenorValorNome = NomeDoProduto
    ###
    # Saindo do while principal.
    if RespostaDaSaida == 'N':
        break
    ###
###
# Escrevendo o resultado.
print(f'O total da compra foi: R${ValorTotal}'
      f'\nTemos {MaiorDeMil} produto(s) custando mais de mil reais'
      f'\nO produto mais barato foi {MenorValorNome} que custa: R${MenorValor}')
###
