'''
script en Python que implemente una función para calcular el área de un
triángulo. Dicha función deberá recibir como argumentos el valor de
la base y la altura y regresará el área calculada
'''

def area_triangulo(altura, base):
    return base * altura/2


print('Programa que calcula el área de un triángulo')
print('Ingresa los siguientess valores')
altura= float (input('Altura: '))
base= float (input('Base: '))

print(f'Area = {area_triangulo(altura, base)}')
print('Nos vemos...')

