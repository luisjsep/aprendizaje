
'''Vamos a comparar los elementos de los indices y determinar cuantas comparaciones tenemos
que realizar.


[0,1,2]
 
0 con 1 / 0 con 2         
1 con 2

3

'''

def comparaListas(lista):
    total=0
    ciclo=len(lista)
    i=1
    while i<ciclo:
        total=total + (ciclo-i)
        i+=1
    return total


num=comparaListas([1,2])
print(num)
num=comparaListas([0,1,2])
print(num)
num=comparaListas([0,1,2,3])
print(num)
num=comparaListas([0,1,2,3,4])
print(num)


