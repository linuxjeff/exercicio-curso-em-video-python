# Programa para sortear ordem de apresentação.

# Importando libs
from random import sample

# Variáveis

Primeiro = input('Digite o nome do primeiro aluno.\n>>> ')

Segundo = input('Digite o nome do segundo aluno.\n>>> ')

Terceiro = input('Digite o nome do terceiro aluno.\n>>> ')

Quarto = input('Digite o nome do quarto aluno.\n>>> ')

# Execução
print('Onderm de apresentação: {}'.format(sample([Primeiro, Segundo, Terceiro, Quarto], k=4)))
