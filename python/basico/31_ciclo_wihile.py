'''
script en Python que implemente el juego de adivinar un número, pero
esta vez en modo competitivo. La computadora deberá generar un número aleatorio
entre 1 y 100 y tanto el usuario como la computadora deberán intentar adivinar dicho
número. Para que ele juego sea retador el jugador máquina deberá ser 'inteligente'
y competir para ganar. El juego se realizará por turnos, primero la máquina y después el
usuario y por cada intento la computadora responderá si el número
es mayor o menor que el secreto.
'''

import os
import random

secreto= random.randint(1, 100)
usuario = -1
computadora = random.randint(1, 100)
acumulador=1
bandera=True

while usuario != secreto:
    os.system('cls')
    
    usuario=int (input('Usuario, ¿Cuál crees que sea el número secreto? : ' ))
    print (f'Computadora, ¿Cuál crees que sea el número secreto? : {computadora}')
   
    if usuario < secreto:
        print('USUARIO Tu número es mayor')
    elif usuario > secreto:
        print('USUARIO Tu numero es menor')
    else:
        print('El usuario ha ganado')

    if computadora < secreto:
        while bandera == True:
            acumulador=computadora
            acumulador=acumulador + random.randint(1, 100)
            print(f'{acumulador} mayor')        
            if acumulador <= 100:
                bandera=False
        print('COMPUTADORA Tu número es mayor')

    elif computadora > secreto:        
        while bandera == True:
            acumulador=computadora
            acumulador=acumulador - random.randint(1, 100)
            print(f'{acumulador} menor')
            if acumulador > 0:
                bandera=False
        print('COMPUTADORA Tu numero es menor')
       
    else:
        print('La computadora ha ganado')
    
    computadora=acumulador
    bandera=True
 
    print (computadora)
    print ('numero secreto', secreto)
    
    input('Presiona enter para continuar...')

print ('Nos vemos')
print (f'El número es {secreto}')

