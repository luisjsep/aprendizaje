
#arrays
v=[1,2,3,4,5,6,8,9]
#recorrer un array
for i in v:
    print(i, " ", end="")
print('\n')
#formas de recorrer un array
for i in range(len(v)):
    print(v[i], " ",end="")
print('\n')
#matricez

m=[[1,2,3],[4,5,6],[7,8,9]]

print('\n')

#largo de array
for i in range(len(m)):
    #largo de los elementos dentro del array 
    for j in range(len(m[i])):
        print(m[i][j]," ", end="")
    print("")