#
# ex108 - Def para moedas
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Esta def modifica a formatação númerica para ficar com cara de
#   moeda.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 16-04-2024, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho
#   - Criado a def moeda para modificar a formatação
#   - Criada a docstring da função
#  v0.0.2 16-04-2024, Jefferson Santana
#   - Modificação na DOCSTRING
#
# Licença: MIT.
#


def moeda(p):
    """
    Esta função cria uma formatação para no estilo moeda para os números.
    :param p: Número a ser formatado.
    :return: Retorna o número com a formatação.
    """
    p = f'R${p:.2f}'
    return p
