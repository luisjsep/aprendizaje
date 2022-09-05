'''
script en python que solicite al usuario dos números y posteriormente 
muestre la suma de ambos valores
'''

valor_1= input('Ingresa primer número: ')
#conversión de tipo de str (cadena) a int (entero)
valor_1=int(valor_1)
valor_2=int (input ('Ingrese segundo número: '))

suma=valor_1 + valor_2
#s
print (f'{valor_1} + {valor_2}= {suma}')