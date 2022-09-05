
'''
script en python que implemente un procedimiento que reciba el nombre
y la edad del usuario y en caso que la edad sea mayor o igual que 18
le indique que ya es mayor de edad; en caso contrario le indique que es menor
menor de edad.
'''

def mayoria_edad(nombre, edad):
    print(f'Hola {nombre}, un gusto verte de nuevo')
    if edad >= 18:
        print('Veo que ya eres mayor de edad')
    else:
        print('Veo que aún eres menor de edad')

mayoria_edad ('Juan', 55)
mayoria_edad ('Luis', 15)

#alterar el orden
mayoria_edad(edad=99, nombre='Susana')