

#append solo agrega un elemento al final de la lista
#si entregamos más de un elemento estos se agregaran como un subelemento de la lista


lista=[1,2,3]

lista.append(["a","b","c"])

print(lista)

lista.extend(["4","5","6"])
print(lista)