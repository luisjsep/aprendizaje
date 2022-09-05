
'''
script  en Python que muestre las tablas de multiplicar de los numeros del 1 al 10.
Cada tabla se muestra hasta el décimo múltiplo.
'''

for numero in range (1, 11):
    print (f'                           Tabla de multiplicar del {numero}')
    for multiplo in range (1, 11):
        print(f'{numero} * {multiplo} = {numero * multiplo}')

print ('Nos vemos')        