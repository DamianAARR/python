import numpy as np

longUser = int(input('Introduce la longitud: '))
array = np.arange(longUser)
print(array)

filas = int(input('Introduce las filas: '))
columnas = int(input('Introduce las columnas: '))

if filas * columnas == longUser:
    array_nuevo = array.reshape(filas,columnas)
    print(array_nuevo)
else:
    print('No se puede hacer el reshape')