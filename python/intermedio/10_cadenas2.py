


#csv

cadena="Hola mundoooo"
#la diferencia entre index y find, es que index si no encuentra un elemento entrega un error
 
#print(cadena.index('x'))

#index puede indicarle desde que posición buscar
num=cadena.index('o', 5)
print(f'"o" esta en la posición {num}')

print('x' in cadena)

#join, por cada elemento que yo haya puesto lo va a separar según 
#elemento que yo haya puesto

print('/'.join(['nombre', 'apellido', 'ciudad']))

#sin corchetes
print('/'.join('nombre'))


#convertir cadena a minuscula
print('NombrE'.lower())


#convertir cadena en mayuscula
print('nombre'.upper())

#Reemplazar un dato. El primer valor corresponde al dato a reeplazar 
#y el segundo corresponde al valor que tomará su lugar

print (cadena.replace('o', 'O'))


#Toma los primeros 3 elementos y los reemplaza
print(cadena.replace('o','O',3))


#Toma el primer elemento y lo reemplaza
print(cadena.replace('o','O',3))

#las cadenas son objetos imutables, por tanto no podemos asignar mediantes corchetes un valor.
#cadena[9]= 'O'

#Poner la m por la un M mayuscula
cadena1= 'Hola mundo'
print(cadena1)

cadena1 = cadena1[:5] + 'M' + cadena1[6:]
print(cadena1)


#convertir cadena a una lista, se parar por espacio

cadena2="Hola mi nombre es Luis y me encanta mejorar"
l1=cadena2.split(" ")
print(l1)




