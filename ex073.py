#!/usr/bin/env python
#
# ex072 - Mostra algumas coisas da tabela do brasileirão
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: O programa mostra algumas curiosidade da tabela do brasileirão.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 26-11-2023, Jefferson Santana
#   - Versão inicial
#   - Criado cabeçalho do programa
#   - Criada área da variáveis iniciais
#   - Criado for para mostrar os cinco primeiros da tabela
#   - Criado for para mostrar os quadro últimos da tabela
#   - Criado for para mostrar times em ordem  alfabética
#   - Criado for para mostrar a posição do Atlético-MG
#   - Criado código para mostrar a tabela completa
#
# Licença: MIT.
#
# Variáveis inicias
Brasileiro = ('Palmeiras', 'Botafogo', 'Flamengo', 'Grêmio', 'Bragantino', 'Atlético-MG', 'Fluminense', 'Athletico-PR',
              'Cuiabá', 'São Paulo', 'Fortaleza', 'Corinthians', 'Internacional', 'Vasco', 'Santos', 'Bahia',
              'Cruzeiro', 'Goiás', 'Coritiba', 'América-MG')

Valor = int(0)
ValorUltimos = int(0)
###
# Mostra tabela completa.
print('Tabela completa:', end=' ')
for Time in Brasileiro:
    print(Time, end=' ')
###
# Mostra os cinco primeiros.
print('Cinco primeiros: ', end='')
for Time in Brasileiro:
    Valor += 1
    if Valor < 6:
        print(Time, end=' ')
    else:
        print('\n')
        break
###
# Mostra os quatro ultimos.
print('Quatro últimos:', end=' ')
for Time in Brasileiro:
    ValorUltimos += 1
    if ValorUltimos > 16:
        print(Time, end=' ')
###
# Mostra times em ordem alfabética.
print('\n')
print('Times em ordem alfabética:', end=' ')
OrdemAlfabetica = sorted(Brasileiro)
for Time in range(0, 20):
    print(OrdemAlfabetica[Time], end=' ')
###
# Mostra qual a posição do Atlético-MG na table.
print('\n')
AtleticoMG = int(0)
for Time in Brasileiro:
    AtleticoMG += 1
    if Time == 'Atlético-MG':
        print(f'O {Time} esta na: {AtleticoMG}º')
        break
###