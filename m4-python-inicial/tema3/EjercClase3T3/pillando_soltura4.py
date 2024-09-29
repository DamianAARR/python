#Crear una lista numérica

numeros = [1,5,8,3,68,32,67,85,15,65]
elementMayores = 0
listaMayores = []

#Pedir al usuario un número por consola

numUsuario = int(input('Introduce un número entero: '))

for i in range(0,len(numeros)):
    if numeros[i] > numUsuario:
        elementMayores = elementMayores + 1
        listaMayores.append(numeros[i])
    
listaMayores.sort()

print('En la lista hay',elementMayores,'elementos mayores que el número', numUsuario,'y son:',*listaMayores)
