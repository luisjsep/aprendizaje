

'''
1) Suma
2) Resta
3) Multiplicación
4) División
5) Division_Entera
6) Modulo
7) Potencia
'''

SUMA=1
RESTA=2
MULTIPLICACION=3
DIVISION=4
DIVISION_ENTERA=5
MODULO=6
POTENCIA=7

print (f'''             Calculadora
{SUMA}) Suma
{RESTA}) Resta
{MULTIPLICACION}) Multiplicación
{DIVISION}) Division
{DIVISION_ENTERA}) División Entera
{MODULO}) Módulo
{POTENCIA}) Potencia
''')

opc= int(input ('Selecciona una opción: '))

if SUMA <= opc <= POTENCIA:
    op_1=float(input('Primer operando: '))
    op_2=float(input('Segundo operando: '))

    if opc == SUMA:
        print (f'{op_1} + {op_2} = {op_1+op_2}')
    elif opc == RESTA:
        print (f'{op_1} - {op_2} = {op_1-op_2}')
    elif opc == MULTIPLICACION:
        print (f'{op_1} * {op_2} = {op_1*op_2}')
    elif opc == DIVISION:
        if op_2 !=0:
            print(f'{op_1} / {op_2} = {op_1/op_2}')
        else: 
             print ('Operacion no definida')
    elif opc == DIVISION_ENTERA:
        if op_2 !=0:
            print(f'{op_1} // {op_2} = {op_1//op_2}')
        else:
            print('Operación no definida')
    elif opc == MODULO:
        if op_2 != 0:
            print(f'{op_1} % {op_2} = {op_1%op_2}')
        else:
            print('Operacion no definida')
    else:
        print(f'{op_1} ** {op_2} = {op_1**op_2}')    

else:
    print('Opción no válida')