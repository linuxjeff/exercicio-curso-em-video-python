#!/usr/bin/env python
#
# ex079 - Recebe vários números sem duplicada.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Programa recebe números pelo teclado sem aceitar números
#   duplicados e mostra valores em ordem crecente no final.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 09-12-2023, Jefferson Santana
#   - Versão inicial
#   - Criado cabeçalho do programa
#   - Criada área de variáveis iniciais
#   - Criado código para receber valores e não aceitar duplicadas
#   - Criado códigos para mostrar valores em ordem crescente
#  v0.0.2 17-12-2023, Jefferson Santana
#   - Consertado Bug do número 0
#
# Licença: MIT.
#
# Variáveis iniciais
Numeros = list()
###
# Código para receber os números.
Casou = ''
Sair = str('A')
while Sair[0] != 'N':
    NovoNumero = int(input('Digite um número: '))
    for Duplicado in Numeros:
        if Duplicado == NovoNumero:
            Casou = int(Duplicado)
    if Casou == NovoNumero:
        print(f'O número {Casou} já existe. Tente outro.')
    else:
        Numeros.append(NovoNumero)
    while True:
        Sair = str(input('Deseja continuar? [S/N]\n>>> ')).strip().upper()
        if Sair[0] in 'NS':
            break
        else:
            print('Opçãp invalida! Tente novamente.')
###
# Código para mostrar os valores digitados em odem
print('Você digitou os sequinte números: ', end='')
Numeros.sort()
for Valores in Numeros:
    print(Valores, end=' ')
###
