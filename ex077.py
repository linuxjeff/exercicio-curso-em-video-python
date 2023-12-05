#!/usr/bin/env python
#
# ex077 - Mostra as vogais das palavras
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Programa recebe palavras de uma tupla e mostra todas as vogais.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 01-12-2023, Jefferson Santana
#   - Versão inicial
#   - Criado cabeçalho do programa
#   - Criada área das variáveis iniciais
#   - Criado código para pegar e mostrar a vogais das palavras
#
# Licença: MIT.
#
# Variáveis iniciais
ListaDePalavras = ('Carro', 'Banana', 'Nokia', 'show', 'Angelica', 'Elemento')
###
# Criado código para pegar e mostrar cada vogal das palavras.
print('Quais são as vogais?')
for Palavra in ListaDePalavras:
    Vogais = str()
    print(f'A vogais da palavra {Palavra.upper()} são:', end=' ')
    for Letras in Palavra:
        if Letras.lower() == 'a' or Letras.lower() == 'e' or Letras.lower() == 'i' or Letras.lower() == 'o' or Letras.lower() == 'u':
            Vogais += Letras.lower() + ' '
    print(Vogais)
###