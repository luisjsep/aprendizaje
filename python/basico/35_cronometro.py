'''
cronometro en python usando la función time sleep
'''

# 1 segundo = 1000 milisegundos
# 1 minuto = 60 segundos
# 1 hora = 60 minutos
# ¿Cuántos milisegundos se encuentran en un segundo?
#Un milisegundo es el período que corresponde a la milésima fracción de un segundo (10−3 o 1/1000) = (0,001s).

import time
import os
print ('''          Crónometro

Expresar en:

1) Horas
2) Minutos
3) Segundos

''')

opc = int (input('Ingrese opción: '))



if opc == 1:
        for horas in range (24):
          for minutos in range(60):        
            for segundos in range (60):
                os.system ('cls')
                print (f'{horas} : {minutos} : {segundos}')
                time.sleep(1)
              
    