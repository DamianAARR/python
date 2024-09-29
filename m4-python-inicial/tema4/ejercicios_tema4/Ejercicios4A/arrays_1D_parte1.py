#Importar librería
import numpy as np

#PASO 1
array_1 = np.zeros(8)
print(array_1)

#PASO 2
array_1[array_1 == 0] = 2
print(array_1)

#PASO 3
array_2 = np.arange(0,11,2)
print(array_2)

#PASO 4
suma1 = 0
suma2 = array_2.sum()

for i in range(0,len(array_2)):
    suma1 += array_2[i]

print(suma1,suma2)

#PASO 5
array_2_reversed = array_2[::-1].copy()

print(array_2_reversed)

#PASO 6
comunes1 = np.intersect1d(array_1,array_2)
comunes2 = np.intersect1d(array_2,array_2_reversed)

print(comunes1)
print(comunes2)

#PASO 7
array_unos = np.ones(int(input('Introduce la longitud del array: ')))
print(array_unos)