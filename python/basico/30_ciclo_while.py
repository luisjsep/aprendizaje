
'''
script en Python que muestra un menú con distintos personajes de un videojuego.
Si el usuario selecciona alguno de los personajes, se le mostrarán sus características.
El menú será cíclico y se mostrará mientras el usuario no indique que desea salir.
'''

import os

MAGO=1
GUERRERO=2
SACERDOTISA=3
SALIR=4
#bandera
continuar=True

while continuar:
    os.system('cls')
    print(f'''               Personajes
    {MAGO}) Mago
    {GUERRERO}) Guerrero
    {SACERDOTISA}) Sacerdotisa
    {SALIR}) Salir
    ''')

    opc = int(input('Selecciona tu personaje: '))

    if opc == MAGO:
        print ('''
        Fuerza: 15
        Energía: 20
        Especial: 12
        '''
        )
    elif opc ==  GUERRERO:
        print ('''
        Fuerza: 25
        Energía: 18
        Especial: 10
        '''
        )
    elif opc == SACERDOTISA:
        print(
            '''
         Fuerza: 18
         Energía:25
         Especial: 22    
        '''
        )
    elif opc == SALIR:
        continuar = False
    else:
        print('Opción no válida')
    input('Presiona enter para continuar..')

input('Nos vemos....')

