'''
script en python que muestre el menú cíclico; decho menú será implementado
procedimiento
'''
import os
ESP = 1
ING = 2
NO_SUBS= 3
SALIR= 4

def mostrar_menu():
    print(f'''
    {ESP}) Español
    {ING}) Ingles
    {NO_SUBS}) Sin subtítulos
    {SALIR}) Salir
    ''')


continuar =True

while continuar:
        os.system('cls')
        mostrar_menu()
        opc = int(input('Selecciona una opción: '))
        if opc == ESP:
            os.system('cls')
            print('Subtítulos en español')
        elif opc == ING:
            print ('Subtítulos en ingles')
        elif opc == NO_SUBS:
            print ('Subtítulos apagados')
        elif opc == SALIR:
            continuar = False
        else: 
            print('Opción no válida')
        input ('Preciona enter para continuar')

print ('Nuestra despedida')
        
 
