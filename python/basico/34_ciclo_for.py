

'''
script en Python que muestre una cuenta regresiva usando un ciclo 
for y esperando un segundo entre cada número
'''

import os
import time

#por defaul incrementa en 1, hay que indicarle que se decremeta
for numero in range(10, -1, -1):
    os.system('cls')
    print(numero)
    #esperar un segundo
    time.sleep(1)
else:
    print('Feliz año nuevo')