# Programa para sortear alunos.

# importado Libs

from random import choice

# Variáveis

Primeiro = input('Digite o primeiro aluno\n>>> ')

Segundo = input('Digite o segundo aluno.\n>>> ')

Terceiro = input('Digite o terceiro aluno.\n>>> ')

Quarto = input('Digite o quarto aluno.\n>>> ')

# Exececução

print('O Aluno que vai apagar a lousa hoje é: {}'.format(choice([Primeiro, Segundo, Terceiro, Quarto])))
