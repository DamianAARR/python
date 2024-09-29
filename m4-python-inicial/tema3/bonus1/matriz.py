#Inicializar listas y variables
m1 = [[2,5,3],[6,1,8],[7,5,4]]
'''[[2,5,3],
    [6,1,8],
    [7,5,4]]'''

m2 = [[4,2,3],[4,5],[6,8,2]]
'''[[4,2,3],
    [4,5],
    [6,8,2]]'''

posiciones = []
filaMax = 0
columnaMax = 0
listaFilaMax = []
listaColumnaMax = []
long = 0
matriz = False
#Comprobar si la lista 1 es una matriz
for i in range(0,len(m1)):
    #Guardamos la longitud de la primera sublista
    long = len(m1[0])
    #Comprobamos si la longitud de las demás sublistas coincide con la de la primera. En ese caso, es una matriz.
    if len(m1[i]) == long:
        matriz = True
    else:
        matriz = False
        break

#Si es una matriz, seguimos con el ejercicio
if matriz == True:
    for i in range(0,len(m1)):
        for j in range(0,len(m1)):
            #Comprobamos que fila suma el máximo
            if sum(m1[i]) > filaMax:
                filaMax = sum(m1[i])
                listaFilaMax = m1[i]
            #Comprobamos que columna suma el máximo
            posiciones.append(m1[j][i])
        if sum(posiciones) > columnaMax:
            columnaMax = sum(posiciones)
            listaColumnaMax = posiciones
        #Vaciamos la lista para volver a añadir los valores de las nuevas posiciones
        posiciones = []

    print('----Lista M1----')
    print(f'Fila que suma el máximo: {listaFilaMax}')
    print(f'Columna que suma el máximo: {listaColumnaMax}')
else:
    print(listaFilaMax)
    print(listaColumnaMax)

matriz = False
listaFilaMax = []
listaColumnaMax = []

#COMPROBAR LISTA 2----------
for i in range(0,len(m2)):
    #Guardamos la longitud de la primera sublista
    long = len(m2[0])
    #Comprobamos si la longitud de las demás sublistas coincide con la de la primera. En ese caso, es una matriz.
    if len(m2[i]) == long:
        matriz = True
    else:
        matriz = False
        break
#Si es una matriz, seguimos con el ejercicio
if matriz == True:
    for i in range(0,len(m2)):
        for j in range(0,len(m2)):
            #Comprobamos que fila suma el máximo
            if sum(m2[i]) > filaMax:
                filaMax = sum(m2[i])
                listaFilaMax = m2[i]
            #Comprobamos que columna suma el máximo
            posiciones.append(m2[j][i])
        if sum(posiciones) > columnaMax:
            columnaMax = sum(posiciones)
            listaColumnaMax = posiciones
        #Vaciamos la lista para volver añadir los valores de las nuevas posiciones
        posiciones = []

    print('----Lista M2----')
    print(f'Fila que suma el máximo: {listaFilaMax}')
    print(f'Columna que suma el máximo: {listaColumnaMax}')
else:
    print('----Lista M2----')
    print(listaFilaMax)
    print(listaColumnaMax)
