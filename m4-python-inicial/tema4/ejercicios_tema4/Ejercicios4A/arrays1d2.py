#Importar librerías
import numpy as np
import random as rd

#Inicializar listas y arrays
nums_ale = []
multi1 = 1
multi2 = 0
nums_float = []
alto = 0

#Paso1
#Forma 1
for i in range(0,15):
    nums_ale.append(rd.randint(1,100))

array = np.array(nums_ale)
print(array)
#Forma 2 y EFICIENTE
array_aleatorio = np.random.randint(1,100, size=(15))
print('Array aleatorio de 15 elementos:',array_aleatorio)

#Paso2
for i in range(0,len(array)):
    multi1 *= array[i]
print(multi1)

multi2 = array.prod()
print(multi2)

#Paso3
for i in range(0,15):
    nums_float.append(rd.uniform(0,1))
array2 = np.array(nums_float)

print(array2.round(1))

#Paso4
print('Sumas:')
suma1 = array + array2
print(suma1)

suma2 = np.add(array,array2)
print(suma2)

#Paso5
print('Restas:')
resta1 = array - array2
print(resta1)

resta2 = np.subtract(array,array2)
print(resta2)

#Paso6
print('Multis:')
producto1 = array * array2
print(producto1)

producto2 = np.multiply(array,array2)
print(producto2)

#Paso7
alto = np.max(array)
print(alto)

#Paso8
print('array1')
media1 = array.mean()
mediana1 = np.median(array)
deviacion1 = np.std(array)
print(media1)
print(mediana1)
print(deviacion1)

print('array2')
media2 = array2.mean()
mediana2 = np.median(array2)
deviacion2 = np.std(array2)
print(media2)
print(mediana2)
print(deviacion2)