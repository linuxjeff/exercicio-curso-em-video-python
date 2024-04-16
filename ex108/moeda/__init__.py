#
# moeda - tem várias funções voltadas a moedas.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: A várias funcões voltadas ao calculos e formatação de números
#   para moedas
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.4 19-04-2024, Jefferson Santana
#   - Versão inicial
#   - Feitas modificações para este documento
#
# Licença: MIT.
#


def aumentar(p=10, por=10):
    p = p + ((p * por) / 100)
    return p


def diminuir(p=10, por=10):
    p = p - ((p * por) / 100)
    return p


def dobro(p=10):
    p = p * 2
    return p


def metade(p=10):
    p = p / 2
    return p


def moeda(p):
    """
    Esta função cria uma formatação para no estilo moeda para os números.
    :param p: Número a ser formatado.
    :return: Retorna o número com a formatação.
    """
    p = f'R${p:.2f}'
    return p