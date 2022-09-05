'''
script en Python que genera un número aleatorio entre 1 y 10 y le 
pide al usuario que intente adivianarlo. Si adivina el número que 
lo felicite por su logro
'''

#Agrega el modulo random a mi programa y con ello me permite
#generar números aleatorios
import random

secreto = random.randint(1, 10)

print ('Acabo de generar un número aletario entre 1 y 10. Intenta adivinarlo')
numero=int(input('¿Cuál crees que sea mi número? '))

if numero == secreto:
    print ('Logro desbloqueado: Haz adivinado!!')

print('Sigue disfrutando tu día')