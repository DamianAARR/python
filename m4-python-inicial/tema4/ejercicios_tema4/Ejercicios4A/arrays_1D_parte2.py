#Importar librerias
import random as rd
import numpy as np

#Inicializar arrrays, listas y variables
lista_azar = []
lista_azar2 = []
resultado_multi = 1

#PASO 1
print()
print('PASO 1')
for i in range(0,15):
    lista_azar.append(rd.randint(1,100))

array_azar = np.array(lista_azar)

print(array_azar)

#PASO 2
print()
print('PASO 2')
for i in range(0,len(array_azar)):
    resultado_multi *= array_azar[i]

print('Multiplicación con bucle: ',resultado_multi)
resultado_multi = array_azar.prod()
print('Multiplicación con numpy: ',resultado_multi)

#PASO 3
print()
print('PASO 3')
for i in range(0,15):
    lista_azar2.append(rd.random())

array_azar2 = np.array(lista_azar2)

print(array_azar2)

#PASO 4
print()
print('PASO 4')
suma_arrays1 = array_azar + array_azar2
suma_arrays2 = np.add(array_azar,array_azar2)

print(suma_arrays1)
print(suma_arrays2)

#PASO 5
print()
print('PASO 5')
resta_arrays1 = array_azar - array_azar2
resta_arrays2 = np.subtract(array_azar,array_azar2)

print(resta_arrays1)
print(resta_arrays2)

#PASO 6
print()
print('PASO 6')
multi_arrays1 = array_azar * array_azar2
multi_arrays2 = np.multiply(array_azar,array_azar2)

print(multi_arrays1)
print(multi_arrays2)

#PASO 7
print()
print('PASO 7')

max_array = array_azar.max()
print(max_array)

#PASO 8
print()
print('PASO 8')

media_array = array_azar.mean()
mediana_array = np.median(array_azar)
desviacion_array = np.std(array_azar)

print(media_array)
print(mediana_array)
print(desviacion_array)
