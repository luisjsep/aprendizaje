
'''
script en python que dentro de un procedimiento solicite el nombre y la edad del usuario y en caso de ser 
mayor o igual que 18 le indique que es mayor de edad, en caso contrario
indicarle que aún es menor.
'''

def mayoria_edad():
    nombre=input('Hola, ¿Cómo te llamas? ')
    edad=int(input('¿ Cuál es tu edad? '))
    if edad >= 18:
        print(f'Ya eres mayor de edad, {nombre}')
    else:
        print(f'Aún eres menor, {nombre}')

mayoria_edad()

print('Nos vemos')
        	