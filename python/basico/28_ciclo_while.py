

'''
script en Python que sume valores pares y multiplique valores impares mientras 
el usuario no ingrese  un 0.Se deberá utilizar la estructura repetitiva "mientras"
para solicitar al usuario un número y dependiendo del número lo suma o lo multiplica

'''

print ('Programa que suma los números pares y multiplica lso impares')
suma= 0
multiplicacion= 1 #no inicializar por cero, todo número multiplicado por cero es cero

numero= -1
while numero != 0:
    numero = int(input('Ingresa un número (0 para salir): '))
    if numero % 2 == 0:
        suma= suma + numero
    else:
        multiplicacion=multiplicacion * numero
    print (f'suma: {suma}')
    print (f'multiplicacion: {multiplicacion}')

print ('Nos vemos')

    