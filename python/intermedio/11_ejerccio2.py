

'''
script en python que implemente el clásico juego de "ahorcado".
El juego consiste en que el usuario intente adivinar una palabra
secreta de la cual incialmente sólo se le muestre la cantidad de letras que contiene.
Para esta versión del juego, el usuario deberá intentar adivinar el nombre
de alguno de los 35 países que conforman el continente americano

El juego debe comenzar seleccionando de forma aleatoria el nombre 
de alguno de los países;
dichos nombres deberán estar almacenados en una lista. Una vez seleccionado el país, se le 
mostrará al usuario una cadena formada por tantos guiones bajos como letras y espacios en 
blanco haya en el nombre del país.
Por ejemplo si el país es "Cuba", al usuario se le mostrarían "____"(4 guiones bajos).

A partir de ahí el usuario debe intentar adivinar las letras que conforman el nombre, teniendo
hasta 5 oportunidades para fallar. Si el usuario propone una letra y existe en el nombre del
país, entonces todas las ocurrencias de esa letra se reemplazan en la palabra secreta;
por ejemplo, para la palabra "Cuba", si el usuario propusiera la "a", entonces la palabra
secreta se actualizaría para mostrar "____a"

'''
import os
import random

MAX_FALLOS=5
paises=['Antigua y Barbuda', 'Argentina', 'Bahamas', 'Barbados', 'Belice', 'Brasil', 'Canadá',
    'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Dominicana', 'Ecuador', 'El Salvador', 
    'Estados Unidos', 'Granada', 'Guatemala', 'Guayuna', 'Haití',
    'Honduras', 'Jamaica', 'México', 'Nicaragua', 'Panamá', 'Paraguay', 
    'Peru', 'República Dominicana', 'San Cristóbal y Nieves',
    'San Vicente y las Granadinas','Santa Lucía','Surinam'
     'Trinidad y Tobago', 'Uruguay','Venezuela']

def crear_cadenas():
    #toma un elemento aleatorio de una colección
    pais=random.choice(paises)
    secreto='_'*len(pais)
    return pais,secreto

def reemplazar_simbolo(original, secreto, simbolo):
    cantidad = original.count(simbolo)
    inicio=0
    for i in range(cantidad):
        pos = original.find(simbolo, inicio)
        secreto= secreto[:pos] + simbolo + secreto[pos+1:]
        inicio=pos + 1
    return secreto


def ahorcado():
    print(f'Hola, vamos a jugar el juego del ahorcado. La\
palabra secreta será el nombre de uno de los {len(paises)} paises del continente americano. Tienes oportunidad de fallar hasta {MAX_FALLOS} veces. ¡Comencemos!')
    input('Presiona enter para comenzar...')
  
    original, secreto=crear_cadenas()
    fallos=0
    while secreto != original and fallos < MAX_FALLOS:
        os.system('cls')
        print(f'Palabra: {secreto}')
        s= input('¿Cuál símbolo quieres destapar? ')
        if s in original:
            secreto= reemplazar_simbolo(original, secreto, s)
            print ('¡Bien Hecho! El símbolo es parte de la palabra')
        else:
            print('Lo siento, el símbolo no es parte de la palabra')
            fallos+=1
        input('Presiona enter para continuar......')
    
    if secreto == original:
        print (f'Felicidades, el pái es {secreto}')
    else:
        print (f'Lo siento, el símbolo no es parte de la palabra')
        fallos +=1
    input('Input presiona enter para continuar.....')
    if secreto == original:
        print(f'Felicidades, el país es {secreto}')
    else:
        print(f'Lo siento, el páis era {original}')



def main():
    ahorcado()

if __name__== '__main__':
    main()
