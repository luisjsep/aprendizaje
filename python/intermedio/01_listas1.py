

#declaración

lista=[]
lista=[1,2,3]

'''agregar elementos'''
#se agrega al final
#Al usar .append()la lista original se modifica. 
# El método no crea una copia de la lista, muta la lista original en la memoria.
#https://www.freecodecamp.org/news/python-list-append-vs-python-list-extend/#:~:text=append()%20adds%20a%20single,the%20end%20of%20the%20list.
lista.append(4)

#otra forma de agregar
lista+=[5,6,7]
lista.extend([8,9,10])
print (lista)
