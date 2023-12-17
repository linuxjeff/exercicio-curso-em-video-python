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
#   - Criado código para contar os parênteses e mostrar o resultado
#  v0.0.2 16-12-2023, Jefferson Santana
#   - Melhoria na lógica, agora são somados os parênteses esquerdos e direitos de forma isoladas
#
# Licença: MIT.
#
# Variaveis inicias
Parenteses = list(str(input('Digite uma expressão: ')))
###
# Código para verificar a quantidade de parênteses e mostra o resultado.
EsquerdoP = int(0)
DireitoP = int(0)
for Caracteres in Parenteses:
    if Caracteres == '(':
        EsquerdoP += 1
    if Caracteres == ')':
        DireitoP += 1
print(f'Esquerdo: {EsquerdoP}')
print(f'Direito: {DireitoP}')
if EsquerdoP == DireitoP:
    print('A expressão esta correta!')
else:
    print('A expressão esta incorreta!')

###
