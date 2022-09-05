'''
script en Python que implemente una función encargada de convertir 
grados Fahrenheit a Celsius
'''

def fahrenheit_a_celcius():
    f=float(input('Grados Fhrenheit: '))
    c=(f-32)/1.8
    return c

print('Programa que convierte grados Fahrenheit a Celcius')
celcius=fahrenheit_a_celcius()
print (f'Celcius: {celcius :.2f}')

print ('Nos vemos')