#eliminar elemento de la lista,recibe indice
#elimina por indice

lista=[0,1,2,3,4]
lista.pop(2)

print(lista)

#devuelve el ultimo elemento de la lista y lo elimina

print(lista.pop())
print(lista)

#elimina por valor
#si el elemento no existe en la lista arroja error
lista.remove(3)
print(lista)

#preguntar si un valor esta en la lista
print (33 in lista)


#consultar la posición de un elemento de la lista 

print(lista.index(0))

lista.extend([2,15,20,45])
print(lista)


#encontrar una posición a partir de un elemento
#El primero parametro es el elemento a buscar  y el segundo es desde que posicion va a partir
print(lista.index(15,1))

lista.extend([3,2,3,6,7])
print(lista)


#ordenar los elementos de una lista
lista.sort()
print(lista)

#eliminar todos los elementos de la lista
lista.clear()
print(lista)
lista=[1,2,3,4,5,6,7]
lista=[]
print(lista)

#cantidad de elementos de la lista
lista=[1,2,3,4,5,6,7]
print(lista)
print(len(lista))


#menor de lista
print("Menor de la lista ",min(lista))
print("Máximo de lista ", max(lista))


#ayuda, recibe el tipo de dato
#help(list)

#otra forma de inicializar una lista

l1=[0] * 10
l1[0,0,0,0,0,0,0,0,0,0,0]