

lista=[0,1,2,3,4,5,6]

#indicar en que posición queremos agregar un dato
#primer valor indica posición y segundo el valor
lista.insert(1,33)
print(lista)


#Podemos insertar en cualquier posición y python se encargara de resolver de manera adecuada.
lista.insert(55,15)
print(lista)


lista.insert(-65,15)
print(lista)

#imprimir el elemento en la posicion del indice
print(lista[2])

#mostrar elementos  a partir de valores negativos
#-1 sería el primer valor de la lista y se cuenta de izquierda a derecha 
print(lista[-1])




