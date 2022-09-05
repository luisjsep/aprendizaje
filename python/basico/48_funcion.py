
'''
script en pyhton que implemente una función para calcular el área de un triángulo
'''

def area_triangulo():
    base=float(input('Base: '))
    altura=float(input('Altura: '))
    area= base * altura / 2
    return area

print ('Programa para calcular área de un triángulo')
a = area_triangulo()
print(f'Area = {a}')


