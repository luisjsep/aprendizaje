'''
script en python que solicite al usuario una calificación y una cantidad 
asistencias a un curso. Si la calificación y la cantidad de asistencia son
aprobatorias entonces se le felecita por su logro;
en caso contrario se le indicará en qué falló.
La calificación mínima aprobatoria será de 60 y la cantidad mínima de asistencias
será de 24
'''
MIN_CAL = 60
MIN_ASI = 24

print('Por favor ingresa los siguientes datos:')
cal =int (input('Calificación: '))
asi =int (input('Asistencia: '))

if cal >= MIN_CAL and asi >= MIN_ASI:
    print('Felicidades aprobaste este curso!')
elif cal < MIN_CAL and asi >= MIN_ASI:
    print(f'Calificación insuficiente. El mínimo es {MIN_CAL}')
elif cal >= MIN_CAL and asi < MIN_ASI:
    print(f'Asistencias insuficientes. El mínimo es {MIN_ASI}')
else: 
    print('Calificación y asistencias insuficientes.')

print ('Que tengas un buen día.')