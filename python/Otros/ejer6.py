'''
Realizar una función que reciba una lista de números.
El número cero se considera par.
Si el índice es par que sume su elemento y si es impar que lo reste.
retornar el total.

ejemplo. 

lista=[1,2,3] cantidad de elemento -1 -> el último elemento de la lista
       0,1,2




sumar= 1 +  3 = 4
restar 2

total= suma - resta
total=2

2 - 2 + 4 - 2
      2

2 - 2 + 4 - 2
    6 -4
     2
'''


def retornaTotal(lista):
    suma=0
    resta=0

    for i in range(len(lista)):
        if i%2==0 or i==0:
            suma=suma + lista[i]
        else:
            resta=resta + lista[i]
           
    total=suma - resta 
    return total

        





lista=[100,100]
      
num=retornaTotal(lista)

print(num)

