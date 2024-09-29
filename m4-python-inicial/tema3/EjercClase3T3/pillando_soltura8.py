#Inicializar variables y listas
lista = [65,40,53,40,56,84,92,40,98,2,34,40,17,22,15,14,13,40,11,40,27,40]
numRepetido = 0
numVeces = 0
repite = False

#Bucle para recorrer la lista
for i in range(0,len(lista)):
    for j in range(i + 1,len(lista)):
#--> Comprobar si algún número se repite
        if lista[i] == lista[j]:
            repite = True
            numRepetido = lista[i]

#-->Comprobar cuantas veces se repite
numVeces = lista.count(numRepetido)

#Devolver el número que se repite y cuantas veces
if repite == True:
    print('El número',numRepetido,'se repite',numVeces,'veces en la lista')
else:
    print('No se repite ningún número')
        
#VERSIÓN PROFE
numeros = [23,65,23]
objetivo = 23
print(numeros.count(objetivo))
for elemento in numeros:
    print('El elemento',{elemento},'aparece',{numeros.count(elemento),'veces'})





