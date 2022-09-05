'''
script en python solicite el nombre del usuario y lo salude de manera
personalizada haciendo uso de un procedimiento'''


#ls varialbles dentro de la función son locales
def saludo_personalizado():
    nombre=input('Hola ¿Cómo te llamas? ')
    edad= int(input('¿Cuál es tu edad'))

    if edad >=18:
        print(f'Gusto en conocerte, {nombre}')
    else:
        print (f'Aún eres menor, {nombre}')
saludo_personalizado()
print('Nos vemos....')
