from pylab import *
import matplotlib.pyplot as plt

lista = list()
valor = input('introduce un valor: ')
valor = int(valor)
lista.append(valor)
while valor != 1:
	if valor % 2 == 0:
		valor = valor / 2
		lista.append(valor)
		print(str(valor))
	else:
		valor = valor * 3
		valor = valor + 1
		lista.append(valor)
		print(str(valor))

cuantos = len(lista)
print('La lista es de ' + str(cuantos) + ' valores')
x = lista
plot(x)
show()
print('fin... ' + str(lista))