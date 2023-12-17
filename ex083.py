#!/usr/bin/env python
#
# nome_completo - Recebe e analisa uma expressão regular.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Recebe uma expressão regular e analiza se ela esta correta.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 16-12-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada a área de variáveis iniciais
#   - Criado código para contar os parênteses e mostrar o resultado.
#
# Licença: MIT.
#
# Variaveis inicias
Parenteses = list(str(input('Digite uma expressão: ')))
###
# Código para verificar a quantidade de parênteses e mostra o resultado.
Contador = int(0)
for Caracteres in Parenteses:
    if Caracteres == '(' or Caracteres == ')':
        Contador += 1
if Contador % 2 == 0:
    print('A expressão esta correta!')
else:
    print('A expressão esta incorreta!')

###
