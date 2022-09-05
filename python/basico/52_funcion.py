'''
script en Python que implemente una función qye haga el cálculo del IMC del usuario.
La función debe recibir el peso y la estatura del usuario y como resultado regresa el valor
del índice de masa corporal
'''

def calcular_IMC(peso, estatura):
    return peso/ (estatura ** 2)

print('Programa que calcuña eñ índice de masa corporal')
print('Ingresa los siguientes datos')
p= float(input('Peso: '))
e=float(input('Estatura: '))



print(f'IMC = {calcular_IMC(p,e)}')