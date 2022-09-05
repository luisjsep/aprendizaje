
'''
script en python que implemente una función encargada de convertir una cantidad de segundos 
a minutos y segundos. La función deberá recibir como argumento una cantidad de segundos 
y deberá regresar la cantidad de minutos y segundos equivalentes
'''

def segundos_minutos(segundos):
    m= segundos // 60
    s= segundos % 60
    return m,s

print ('Programa que convierte segundos a minutos y segundos')
seg = int (input('Segundos a convertir: '))


min, segu = segundos_minutos(seg)
print (f'El equivalente es : {min} : {segu}')

print('Nos vemos.....')





