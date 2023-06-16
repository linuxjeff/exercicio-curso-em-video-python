# Variáveis
Aluno = str(input('Digite o nome do aluno: '))
NotaUm = float(input('Digiite a primeira nota do {}: '.format(Aluno)))
NotaDois = float(input('Digite a segunda nota do {}: '.format(Aluno)))
Media = (NotaUm + NotaDois) / 2

# Execução
print('A média do aluno {} é: {:.1f}'.format(Aluno, Media))
