'''
Script en Python que simule el sistema de validación de datos de una plataforma digital.
Se le solicitará al usuario su nombre y contraseña mientras la información proporcionada
no coincida con la información previamente registrada
'''
#modulo os para limpiar pantalla
import os

USER= 'pepe_nava'
PASSWORD= 'v1dr1o'

user= ''
password= ''

while USER != user or PASSWORD != password:
    #limpiar pantalla
    os.system('cls')
    print('                 kit-kot')
    user= input('Usuario: ')
    password= input('Contraseña: ')

    if USER != user or PASSWORD !=password:
        print('Credenciales incorrectas')
        print ('Intenta de nuevo')
        input('Presiona enter para continuar...')
else:
    print ('Bienvenido')