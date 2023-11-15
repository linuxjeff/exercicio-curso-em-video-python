#!/usr/bin/python3
#
# ex055 - Mostra o maior e o menor peso.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Recebe o peso de cinco pessoas e mostra qual é o maior e qual é
#              o menor.
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 19-10-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho
#   - Criado for para receber e testar qual é o maior e o menor peso
#   - Criado print para mostrar o resultado do for
#
# Licença: MIT.
#

# Variáveis

MaiorPeso = float(0)

MenorPeso = float(0)

# For para receber e testar os pesos.
for pessoas in range(1, 6):
    Peso = float(input('Digite o seu peso.\n>>> '))
    if Peso > MaiorPeso:
        MaiorPeso = Peso
    elif MenorPeso == 0 or Peso < MenorPeso:
        MenorPeso = Peso

# Print que mostra o resultado do for.
print('O Menor peso é: {:.2f}Kg\nO Maior peso é: {:.2f}Kg'.format(MenorPeso, MaiorPeso))
