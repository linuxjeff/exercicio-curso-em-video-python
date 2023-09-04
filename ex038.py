# nome_completo - O programa lê dois valores e os comparam.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: O programa compara os números e mostra uma mensagem dizendo qual
#              é o maior o se são iguais.
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 31-08-2023, Jefferson Santana
#   - Versão inicial.
#   - Criado área de variáveis.
#   - Criado variáveis para colher números.
#   - Criado áreas de execução.
#   - Criado debug de variáveis.
#   - Testado recolhimento de números.
#   - Criado o IF para o teste de qual número é maior.
#   - Retirado o debug de variáveis.
#
# Licença: MIT.
#

# Variáveis
Primeiro = int(input('Digite o primeiro número: '))

Segundo = int(input('Digite o segundo número: '))

# Execução

if Primeiro > Segundo:
    print('O número {} que é o primeiro é maior que o número: {}'.format(Primeiro, Segundo))
elif Segundo > Primeiro:
    print('O número {} que é o segundo é maior que o número: {}'.format(Segundo, Primeiro))
else:
    print('Os dois números são igual!')
