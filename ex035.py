# Calula se três retas formão um triângulo.

RetaUm = float(input('Digite o tamanho da primeira reta.\n>>> '))

RetaDois = float(input('Digite o tamanho da segunda reta.\n>>> '))

RetaTres = float(input('Digite o tamanho da terceira reta.\n>>> '))

UmDois = RetaUm + RetaDois

if UmDois > RetaTres:
    print('Às três retas formam um triângulo.')
else:
    print('Às três retas não formam um triângulo.')
