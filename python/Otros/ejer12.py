'''Cual es el elemento que más veces se repite dentro de una lista'''

lista=["comida", "cerdo","mariposa", "cerdo", "cerdo", "mariposa","mariposa", "mariposa"]


print(max(set(lista), key=lista.count))



