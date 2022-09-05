'''
script en Python que muestre la tabla de multiplicar de un número ingresado por el
usuario. El usuario también podrá ingresar hasta que valor llegará la tabla de multiplicar
'''

numero= int (input('¿De qué número deseas ver la tabla de multiplicar? : '))
limite = int(input ('¿Hasta qué múltiplo deas ver? : '))


print(f'                       Tabla del {numero}')    
for multiplo in range(1, limite+1):
    print(f'{numero} x {multiplo} = {numero * multiplo}')

print ('nos vemos')

