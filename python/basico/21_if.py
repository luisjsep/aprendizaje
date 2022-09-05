
'''
script en python que solicita al usuario que intente adivianr un número entre 1 y 10.
Si el usuario lo adivina, entonces lo felicita por su logro; en caso contrario
le indica cual era el número secreto.
'''

import random
secreto = random.randint(1,10)
print('Acabo de generar un número secreto entre 1 y 10.')
usuario = int(input ('¿Cuál crees que sea mi número secreto?: '))

if usuario == secreto:
    print('Logro desbloqueado: Adivina mistico')
else:
    print(f'Mi numero secreto era {secreto}')

print ('Que tengas un buen día')
