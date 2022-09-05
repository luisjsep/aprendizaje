'''
script en python que implemente un procedimiento dentro  del cual se muestre la
tabla de multiplicar de un número recibido como argumento.
El procedimiento contará con un segundo argumento que indicará hasta qué
múltipl se mostrará la tabla de multiplicar. Ese segundo argumento tendrá como valor
por omisión el número 10.
'''

def tabla_multiplicar(numero, limite=10):
    print(f'            Tabla de multiplicar del {numero}')
    for i in range (1,limite+1):
        print(f'{numero} x {i} = {numero * i}')

tabla_multiplicar(7)
tabla_multiplicar(5, 13)

print ('Nos vemos...')
