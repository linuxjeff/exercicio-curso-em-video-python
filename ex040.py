# ex040 - Faz cálculo de média.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Recebe duas notas do aluno e faz o cálculo da média. Mostra se
#              o aluno foi aprovado, reprovado ou ficou de recuperação.
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 07-09-2023, Jefferson Santana
#   - Versão inicial
#   - Criado área de variáveis iniciais
#   - Criado o debug de variáveis
#   - Criadas e testadas às variáveis NotaUm e NotaDois
#   - Criada e testada a variável Media
#  v0.0.2 13-09-2023, Jefferson Santana
#   - Criado IF para resuldado da média
#   - Retirado debug da variável
#
# Licença: MIT.
#

# Variáveis Inicias

NotaUm = float(input('Qual a primeira nota do aluno?\n>>> '))

NotaDois = float(input('Qual a segunda nota no aluno?\n>>> '))

Media = (NotaUm + NotaDois) / 2

# -----------------------------------------------------------------------------
# If para resultado da média.

if Media <= 5:
    print('Sua média foi {:.2f}, você esta reprovado.'.format(Media))
elif Media < 6.9:
    print('Sua média foi {:.2f}, você esta de recuperação.'.format(Media))
elif Media >= 6.91:
    print('Sua média foi {:.2f}, você esta aprovado'.format(Media))

# -----------------------------------------------------------------------------
