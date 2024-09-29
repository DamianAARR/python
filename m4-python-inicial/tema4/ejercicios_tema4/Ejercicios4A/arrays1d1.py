#importar librerias
import numpy as np

#inicializar arrays y listas
suma_array = 0
suma_array2 = 0
array2_revertido = []
comunes1 = 0
comunes2 = 0

#Paso1
array_1 = np.zeros(8)
print(array_1)
#Paso2
array_1[array_1 == 0] = 2 #Donde sea 0 pon un 2
array_1[:] = 2 #Pero como pueden ser números distintos, con esto cambiamos todos los valores por 2
print(array_1)
#Paso3
array_2 = np.arange(2,11,2)
print(array_2)
#Paso4
for i in range(0,len(array_2)):
    suma_array += array_2[i]
print(suma_array)

suma_array2 = array_2.sum()
print(suma_array2)
#Paso5
array2_revertido = array_2[::-1].copy() #Hacemos una copia con .copy() para que los cambios no afecten al array original
#array2_revertido[:] = array_2[::-1] Esto hace lo mismo que la linea de arriba
print(array2_revertido)
print(array_2)
#Paso6
comunes1 = np.intersect1d(array_1,array_2)
print(comunes1)

comunes2 = np.intersect1d(array_2,array2_revertido)
print(comunes2)
#Paso7

longUser = int(input('Introduce la longitud del array'))
array_unos = np.ones(longUser)

print(array_unos)