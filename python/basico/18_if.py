'''
script en python que solicite la calificacion y cantidad de asistencias
a aun curso. Si la calificación es mayor o igual que 60 y 
la cantidad de asistencias es mayor que 20 entonces que le 
indique que ha aprobado el curso.
'''

calificacion= int (input('¿Cual es tu calificación: '))
asistencias = int (input ('¿Cuantas asistencias tuviste: '))

if calificacion >= 60 and asistencias>=20:
    print ('Felicidades aprobaste el curso')
    if calificacion >= 95:
        print('Estudiante sobresaliente. Pídele beca a AMLO')
print('Sigue disfrutando tu día')