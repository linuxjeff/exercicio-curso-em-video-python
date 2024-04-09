#!/usr/bin/env python
#
# ex101 - Recebe o ano de nascimento e retorna sobre o voto
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: O programa recebe o ano de nascimento e retona a contição atual
#   do seu voto.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 22-03-2024, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada a área de importa bibliotecas
#   - Criada a área de funçãos
#   - Criada a área das variáveis globais
#   - Criada a área do código para exibir o resultado
#   - Criada a função voto para mostrar se o voto é obrigatório
#   - Criada a docstring da função voto
#   - Corrigido problema com aspas simples na docstring da função voto
#  v0.0.1 09-04-2024, Jefferson Santana
#   - Foi a importação da biblioteca para dentro da def
#
# Licença: MIT.
#
# Funções
def voto(ano=date.today().year):
    """
    A função voto mostra se  o voto é obrigatório ou facultativo.
    :param ano: O ano de nascimento da pessoa
    :return: retorna a contição do voto da pessoa
    """
    # Importando bibliotecas.
    from datetime import date
    # A importação foi movida para o escopo da def.
    ###
    idade = date.today().year - ano
    resultado = str('')
    if idade <= 15:
        resultado = f'Com {idade} anos: NÃO VOTA'
    elif idade < 18 or idade > 70:
        resultado = f'Com {idade} anos: VOTO FACULTATIVO'
    else:
        resultado = f'Com {idade} anos: VOTO OBRIGATÓRIO'
    return resultado


###
# Variáveis globais
anodenascimento = int(input('Em que ano você nasceu?\n>>> '))
###
# Código para mostrar resultado.
print(voto(anodenascimento))
###
