'''
sript en Python que imprima los números pars desde el 2 hasta el 
20 haciendo uso de un ciclo for
'''

print ('Programa que muestra los números pares desdee el 2 hasta el 20')

print ('método 1')
for numero in range(1, 11):
    print(f'par: {numero*2}')



print ('método 2')
for numero in range(2,21):
    if numero % 2 == 0:
        print(f'par: {numero}')


print ('método 3')
#incrementa en 2
for par in range(2, 21, 2):
    print(f'par:{par}')        

print('Nos vemos')