'''
script en Python que implemente un sistema de redondeo de 
calificaciones. El usuario es el encargado de ingresar su
calificación. Si a la calificación le faltan 4 unidades o menos
para el siguiente multiplo de 10, entonces su calificación será
redondeada al siguiente multiplo de 10, en caso contrario la califación no es modificada

Ejemplo:
Si el usuario obtuvo 76 entonces se redondea a 80
Si el usuario obtuvo 77 entonces se redondea a 80
Si el usuario obtuvo 75 entonces calificacion es 75

'''

calificacion = int (input ('Cuál es tu calificación: '))
#me dara como residuo la unidad del número
residuo= calificacion % 10
mensaje = 'Tu calificación no amerita redondeo'

if  0 <= calificacion <= 100 and residuo >= 6:
    calificacion = calificacion + (10 - residuo)
    mensaje= f'Tu calificación es: {calificacion}'

print(mensaje)


