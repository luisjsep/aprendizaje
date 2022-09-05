'''
script en Python que muestre uno a uno de los símbolos de una palabra
o frase. Por ejemplo si la frase fuera 'Hola' se debería
imprimir:
H
o
l
a
'''

frase = input('Ingresa una frase o palabra: ')
print('Los simbolos de tu frase/palabra son: ')

for simbolo in frase:
    print(f'{simbolo}')

print('Nos vemos')