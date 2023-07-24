# Programa para dizer se o nome da cidade começa comsantos

NomeDaCidade = input('Digite o nome da cidade onde mora.\n>>> ')

NomeStrip = NomeDaCidade.strip()

NomeTitle = NomeStrip.title()

NomeSlit = NomeTitle.split()

PrimeiraPalavra = NomeSlit[0]

print('O primeiro nome da minha cidade tem Santo?\nReposta: {}'.format('Santo' in NomeSlit))
