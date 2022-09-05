'''
cuando le pasas un valor de una lista a otra en realidad se hace
por referencia. (dirección de la memoria)


notacion de rebanadas
'''
import random

lista=[1,2,3,4,5,6,7]

lista2=lista

lista2.append(10)

print(lista)

# otra forma de inicializar la lista
lista2=[0] * 10
print(lista2)

#realizar una copia para no pasar por referencia
lista2=lista[:]


#imprimir desde la posición 3 en adelante
print(lista2)
print(lista2[3:])

#imprimir hasta la posicion 4
print(lista2[:4])

#imprimir desde la posicion 3 a la posición 7
print(lista2[2:6])


#imprimir de dos en dos
print(lista[1:7:2])


#compactación de listas
lista3= [i for i in range (7)]
print(lista3)

lista4= [i**2 for i in range(10)]
print(lista4)

lista5= [2**i for i in range(10)]
print(lista5)


#aleatorios sin compactación
aleatorios=[random.randint (1,10)] * 20
print (aleatorios)


#aleatorios con compactación
aleatorios2=[random.randint(1, 10) for i in range (20)] 
print(aleatorios2)


