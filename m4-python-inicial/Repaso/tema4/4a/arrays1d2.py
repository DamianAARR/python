import numpy as np

#PASO 1
array_aleatorio = np.random.randint(1,10, size=(15))
print(array_aleatorio)

#PASO 2
multi = 1

for i in range(0,len(array_aleatorio)):
    multi *= array_aleatorio[i]
print(multi)

multi = 1
for elemento in array_aleatorio:
    multi *= elemento
print(multi)

multi = np.prod(array_aleatorio)
print(multi)

multi = array_aleatorio.prod()
print(multi)

#PASO 3 
array_decimales = np.random.rand(15)
print(array_decimales.round(2))

#PASO 4 
suma1 = array_aleatorio + array_decimales
print(suma1)

suma2 = np.add(array_aleatorio,array_decimales)
print(suma2)

#PASO 5
resta1 = array_aleatorio - array_decimales
print(resta1)

resta2 = np.subtract(array_aleatorio,array_decimales)
print(resta2)

#PASO 6
multi1 = array_aleatorio * array_decimales
print(multi1)

multi2 = np.multiply(array_aleatorio,array_decimales)
print(multi2)

#PASO 7
maximo = np.max(array_aleatorio)
print(maximo)

#PASO 8
media = np.mean(array_aleatorio)
mediana = np.median(array_aleatorio)
desv = np.std(array_aleatorio)

print('Media:',media)
print('Mediana:',mediana)
print('Desviación:',desv.round(3))

