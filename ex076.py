#!/usr/bin/env python
#
# ex076 - Lista de produtos
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Programa mostra uma lista de produtos gerados por uma tupla.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 28-11-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada área das variáveis inicias
#   - Criado o código para criar a tabulação dos produtos com seus valores
#
# Licença: MIT.
#
# Variáveis iniciais.
Lista = ('Ovo', 0.20, 'Marcarão', 2, 'Gilo', 2.99, 'Sabão', 1.99, 'Óleo de Soja', 5)
Nome = str('Lista de Produtos')
Anderlane = '_' * 40
###
# Mostrando lista na tela.
print(f'{Anderlane}')
print(f'{Nome:^40}')
print(f'{Anderlane}')
Preco = int(1)
for Produto in Lista[0::2]:
    print(f'{Produto:•<30} R${Lista[Preco]:> .2f}')
    Preco += 2
print(f'{Anderlane}')
###
