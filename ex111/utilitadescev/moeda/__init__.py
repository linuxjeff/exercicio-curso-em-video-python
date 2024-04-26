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
#  v0.0.4 16-04-2024, Jefferson Santana
#   - Versão inicial
#   - Feitas modificações para este documento
#  v0.0.5 16-04-2024, Jefferson Santana
#   - Def aumentar() recebeu a opção form para ativar a formatação
#   - Def diminuir() recebeu a opção form para ativar a formatação
#   - Def dobro() recebeu a opção form para ativar a formatação
#   - Def metade() recebeu a opção form para ativar a formatação
#   - mdificado o módulo ex108 para ex111
#  v0.0.6 18-04-2024, Jefferson Santana
#   - Foi criada a def resume() que mostra um resumo
#   - Foi criada a def mostrealinha() para mostrar títulos decorados
#  v0.0.7 26-04-2024, Jefferson Santana
#   - Modificado a função moeda para mostrar virgula no lugar de ponto
#
# Licença: MIT.
#


def aumentar(p=10, por=10, form=False):
    p = p + ((p * por) / 100)
    if form:
        p = moeda(p)
    return p


def diminuir(p=10, por=10, form=False):
    p = p - ((p * por) / 100)
    if form:
        p = moeda(p)
    return p


def dobro(p=10, form=False):
    p = p * 2
    if form:
        p = moeda(p)
    return p


def metade(p=10, form=False):
    p = p / 2
    if form:
        p = moeda(p)
    return p


def moeda(p=0, vmoeda='R$'):
    p = f'{vmoeda}{p:.2f}'
    return p.replace('.', ',')


def resumo(p=0, aumento=0, reducao=0):
    lista = ['Preço analisado:', moeda(p), 'Dobro do preço:', dobro(p, True), 'Metade do preço:',
             metade(p, True), f'{aumento}% de aumento:', aumentar(p, aumento, True),
             f'{reducao}% de redução:', diminuir(p, reducao, True)]
    valor = int(1)
    mostrealinha('Resumo do Valor', 16)
    for mostra in lista[0::2]:
        print(f'{mostra:<18}{lista[valor]:<8}')
        valor += 2
    mostrealinha('Resumo do Valor', 16, False)


def mostrealinha(msg, espaco=6, titulo=True):
    tamanholen = len(msg) + espaco
    if titulo:
        print('-' * tamanholen)
        print(f'{msg:^{tamanholen}}')
        print('-' * tamanholen)
    else:
        print('-' * tamanholen)
