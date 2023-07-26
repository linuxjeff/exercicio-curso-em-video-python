# Mostra o primeiro e o ultimo nome

SeuNomeCompleto = input('Digite seu nome completo\n>>> ').strip().title()

ListaDeNomesL = SeuNomeCompleto.split(maxsplit=1)

ListaDeNomesR = SeuNomeCompleto.rsplit(maxsplit=1)

print('O seu primeiro nome é: {}'.format(ListaDeNomesL[0]))
print('O seu ultimo nome é: {}'.format(ListaDeNomesR[1]))
