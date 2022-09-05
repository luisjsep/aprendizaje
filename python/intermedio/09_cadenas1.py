#cadenas

cadena="Hola mundo"
cadena[3]
print(cadena)

#cantidad de elementos de una cadena
print(len(cadena))
 
#notación de rebanada
#desde la posición3
print (cadena[3:])

#notación de rebanada
#desde la posición 3 a la posición 7
print(cadena[3:7])

#busca cuantas veces se repite esa letra en la cadena
num=cadena.count('o')
print (num)

#busca cuantas veces se repite esa letra en la cadena
num=cadena.count('l')
print (num)

#buscar donde esta un simbolo, encuentra la primera ocurrencia de ese simbolo que 
#pusimo como argumento
num=cadena.find('o')
print(num)

#al entregar un simbolo que no se encuentra en la cadena
#find devuelve un -1
num=cadena.find('x')
print(num)

#find también sirve para encontrar cadenas

num=cadena.find('ol')
print(num)

