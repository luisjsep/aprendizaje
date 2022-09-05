
'''
Dada una cadena, devuelva una lista que contiene los caracteres
de la cadena. Si un carácter es un espacio o un digito
mayor que 5, elimínelo y no lo incluya en la matriz.


'''
def str_to_list(str):
    lista=[]
    
    for cadena in str:
        if cadena.isdigit() and int(cadena)>=5 or cadena == " ":
            continue
        else:
             lista.append(cadena) 
                
    print(lista)
    

str_to_list("Hola mundo 5")


   
            
