'''
Script en python que determina el número  de comparaciones de una lista.
por ejemplo, conocer el número de  veces  que se tiene realizar comparaciones para saber
cuantas veces se repite un número.
'''


def numeroCompara(lista):
    i=1
    ciclo=len(lista)
    total=0
    while i<ciclo:
        total=total + (ciclo-i)
        print(total)
        i+=1
    print (total)


numeroCompara([0,1,2])
numeroCompara([0,1,2,3])
numeroCompara([0,1,2,3,4])






