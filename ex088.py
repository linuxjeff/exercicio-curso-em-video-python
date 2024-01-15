#!/usr/bin/env python
#
# nome_completo - Gera palpites da megasena
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: O programa gera quantos palpites da mega sena for desejados.
#
# -----------------------------------------------------------------------------
# Histórico:
#
#  v0.0.1 11-01-2024, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho do programa
#   - Criada a área para importa a biblioteca
#   - Criada a área das variáveis inicias
#   - Criado o código para gerar os números das apostas
#   - Criado o código para mostrar o resultado
#  v0.0.2 15-01-2024, Jefferson Santana
#   - Colocado a biblioteca time para uso da função sleep
#   - Revisto as quebras de linha no printes dos resultados
#
# Licença: MIT.
#
# Importando Bibliotecas
from random import randint
from time import sleep
###
# Variaveis iniciais
Palpites = list()

Jogos = int(input('Você deseja quantos palpites da megasena?\n>>> ')) + 1

Contador = Apostas = Casou = int(0)
###
# Código que gera os palpites das apostas.
while Apostas + 1 != Jogos:
    Contador = int(0)
    Palpites.append(list())
    while Contador != 6:
        NovoNumero = randint(1, 60)
        for Duplicado in Palpites[Apostas]:
            if Duplicado == NovoNumero:
                Casou = Duplicado
        if Casou != NovoNumero:
            Palpites[Apostas].append(NovoNumero)
            Palpites[Apostas].sort()
            Contador += 1
    Apostas += 1
###
# Código para mostrar resultados.
Njogos = len(Palpites)
print(f'-_-_-_ Sorteado(s) {Jogos -1} jogo(s) _-_-_-', end='')
for Contador in range(0, Njogos):
    sleep(1.5)
    print(f'\nJogo {Contador + 1}: ', end='')
    for Nnumeros in Palpites[Contador]:
        print(f'{Nnumeros}', end=' ')
print(f'\n-_-_-_-_-_-_ Boa sorte _-_-_-_-_-_-')
###
