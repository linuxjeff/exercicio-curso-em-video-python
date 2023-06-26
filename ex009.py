# Variáveis
Numero = int(input('Digite um número: '))

Mutiplicador = 1

# Execução
print('-' * 15 )
print('Tabuada do {}\n{:^} x {:>2} = {:^}\n{:^} x {:>2} = {:^}'.format(Numero, Numero, Mutiplicador -1 , Numero * 0, Numero, Mutiplicador, Numero * 1))
print('{:^} x {:>2} = {}'.format(Numero, Mutiplicador + 1, Numero * 2))
print('{:^} x {:>2} = {:^}\n{:^} x {:>2} = {:^}\n{:^} x {:>2} = {:^}'.format(Numero, Mutiplicador + 1, Numero * 3, Numero, Mutiplicador + 3, Numero * 4, Numero, Mutiplicador + 4, Numero * 5))
print('{:^} x {:>2} = {:^}\n{} x {:>2} = {:^}\n{:^} x {:>2} = {:^}'.format(Numero, Mutiplicador + 5, Numero * 6, Numero, Mutiplicador + 6, Numero * 7, Numero, Mutiplicador + 7, Numero * 8))
print('{:^} x {:>2} = {:^}\n{:^} x {:<} = {:^}'.format(Numero, Mutiplicador + 8, Numero * 9, Numero, Mutiplicador + 9, Numero * 10))
print('-' * 15)
