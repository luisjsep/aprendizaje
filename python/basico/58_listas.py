
no_olvidar = ["huevos", "palta", "lechuga", "naranjas", 7000]

#recorrer una lista
for elem in no_olvidar:
    print("No olvides", elem)


#modificar una lista

no_olvidar[1]="queso"
no_olvidar[3]=10000
print(no_olvidar)


#concatenar listas(+)
tambien=["apio", "tomates"]
no_olvidar= no_olvidar + tambien
print (no_olvidar)
print(tambien * 2)

#se agregan en un lista diferente
no_olvidar.append(["apio", "tomate"])
print (no_olvidar)
#se agregan en un la misma lista
no_olvidar.append(["cepillo", "jabon"])
print (no_olvidar)


no_olvidar.insert(0, "piña")
print(no_olvidar)

lista=["huevos", "palta", "lechuga", "naranjas", 7000]
#lista.pop() elimina el primer elemento de la lista y lo entrega como retorno
compra=lista.pop()
print(lista)
print (f'Se eliminó: {compra}')
compra=lista.remove()
print (lista)
print (f'Se eliminó: {compra}')

