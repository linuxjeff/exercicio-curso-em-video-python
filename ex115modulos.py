#!/usr/bin/env python
#
# ex115-modulos - Módulos do programa ex115
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Módulos para o programa de cadastro.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 06-05-2024, Jefferson Santana
#   - Versão inicial
#   - Foi criado o cabeçalho dos módulos
#   - Criado a função leituratxt()
#   - Criado a função escritatxt()
#   - Criado a função leiaint()
#   - Criado a função juntastring()
#   - Criado a função crialista()
#   - Criado a função listaalinhada()
#   - Criadas todas as docstrings
#   - Mudanças na função leiaint()
#
# Licença: MIT.
#

def leituratxt(dados):
    """
    Lê o que a no arquivo.
    :param dados: Nome do arquivo.
    :return: Retorna dados do arquivo.
    """
    try:
        with open(f'{dados}', 'r') as arquivo:
            return arquivo.read()
    except IOError:
        return f'\033[31mO arquivo {dados} não existe!\033[m'


def escritatxt(dados='cadastro.txt', inserir=''):
    """
    Escrve em arquivo. Caso o aquivo não exista a função cria ele.
    :param dados: Nome do arquivo a ser criado ou a ser escrito(caso já exista).
    :param inserir: Dado a ser escrito no arquivo.
    :return: Não tem retorno.
    """
    try:
        with open(f'{dados}', 'a') as arquivo:
            arquivo.write(f'\n{inserir}')
    except IOError:
        with open(f'{dados}', 'w') as arquivo:
            arquivo.write(f'\n{inserir}')


def leiaint(frase='Digite um número: ', espaco=True, intoustr=False, frasedeerro='Não é um número interio!'):
    """
    Validado de número inteiro. Coloca um espaço no final se for necessário.
    :param frase: Frase de pedido.
    :param espaco: Coloca um espaço no final, mas entrega o número como string.
    :param intoustr: Devolve a saída como número inteiro.
    :param frasedeerro: Frase para retornar quando tiver erro
    :return: Número inteiro como número ou string.
    """
    status = False
    numero = int(0)
    while True:
        try:
            numero = int(input(f'{frase}').strip())
            status = True
        except KeyboardInterrupt:
            print('Não foi digitado nenhum número. O padrã sera mantido')
            status = True
        except:
            print(f'{frasedeerro}')

        if status:
            break

    if intoustr:
        return int(numero)
    else:
        if espaco:
            return str(f'{numero} ')
        else:
            return str(numero)


def juntastring(*lista):
    """
    Esta função serve para juntar strings?
    :param lista: Lista de strings para serem juntadas.
    :return: Retorna as strings juntadas.
    """
    juntado = ' '.join(lista)
    return juntado


def crialista(arquivo='cadastro.txt'):
    """
    Recebe um arquivo e cria uma lista.
    :param arquivo: Arquivo para ser lido.
    :return: Retorna uma lista com as string do arquivo.
    """
    interiro = str('')
    listadeitens = list()
    for c in leituratxt(f'{arquivo}'):
        if c.isalnum():
            interiro += interiro.join(c)
        elif c == ' ':
            listadeitens.append(interiro)
            interiro = str()

    return listadeitens


def listaalinhada(lista):
    """
    Lista de forma tabulada uma lista com dois valores paralelos.
    :param lista: A lista a ser tabulada.
    :return: Não tem retorno, pois a função já printa a tabulação.
    """
    for c in lista:
        if c.isalpha():
            print(f'{c:<18}', end='')
        else:
            print(f'{c:>8} anos')
