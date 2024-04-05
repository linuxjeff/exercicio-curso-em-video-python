#!/usr/bin/env python
#
# ex105 - Recebe várias notas
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: O programa recebe várias notas e mostra os dados relevantes.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 05-04-2024, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada a função notas que resebe várias nota e mostra o resultado
#   - Criado o código para mostrar o resultado.
#
# Licença: MIT.
#
# Funcões
def notas(*notas, sit=False):
    resultado = dict()
    maiorvalor = menorvalor = media = float(0)
    numerodenotas = len(notas)
    resultado['total'] = numerodenotas
    for contando in notas:
        if maiorvalor == 0 or maiorvalor < contando:
            maiorvalor = contando
        if menorvalor == 0 or contando < maiorvalor:
            menorvalor = contando
        media += contando
    resultado['maior'] = maiorvalor
    resultado['menor'] = menorvalor
    fimmedia = (media / numerodenotas)
    resultado['média'] = fimmedia
    if fimmedia > 9:
        situacao = 'Excelente'
    elif fimmedia > 7:
        situacao = 'Ótima'
    elif fimmedia > 5:
        situacao = 'Boa'
    elif fimmedia > 3:
        situacao = 'Ruim'
    else:
        situacao = 'Péssima'
    if sit:
        resultado['situação'] = situacao
    return resultado


###
# Código para mostrar o resultado.
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
###
