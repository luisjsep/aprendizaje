'''
script en python que implemente un procedimiento para saludar al usuario
de manera personalizada; el procedimiento deberá recibir el nombre  del usuario como
argumento. Se deberá crear otro procedimiento llamado "main"
desde el cual se inicie la ejecución del programa y dentro del cual se solicite
el nombre del usuario y se actualice el primer procedimiento descrito
'''

def saludo_personalizado(nombre):
    print(f'Gusto de verte {nombre}')

def main():
    usuario= input('¿Hola como te llamas? ')
    saludo_personalizado(usuario)


#evalua si el script es el principal
if __name__ == '__main__':
    main()