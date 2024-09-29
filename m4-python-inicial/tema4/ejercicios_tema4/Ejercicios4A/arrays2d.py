#Importar librerías
import numpy as np

#Paso9
longUser = int(input('Introduce la longitud del array: '))
arrayUnos = np.ones(longUser)

print(arrayUnos)

#Paso10 y 11
filas = int(input('Introduce las filas: '))
columnas = int(input('Introduce las columnas: '))

if filas * columnas == longUser:
    array_nuevo = arrayUnos.reshape(filas,columnas)
    print('Array reshapeado:')
    print(array_nuevo)

    arrayIdentidad = np.eye(filas,columnas)
    print('Array identidad: ')
    print(arrayIdentidad)

    print('Horizontalmente concatenate')
    conHorizontal = np.concatenate((array_nuevo,arrayIdentidad), axis=1)
    print(conHorizontal)

    print('Verticalmente concatenate')
    conVertical = np.concatenate((array_nuevo,arrayIdentidad), axis=0)
    print(conVertical)



else:
    print('No se puede hacer el reshape')

pass
#Paso12


print('Horizontalmente hstack()')
conHorizontal = np.hstack((array_nuevo,arrayIdentidad))
print(conHorizontal)

print('Verticalmente vstack()')
conVertical = np.vstack((array_nuevo,arrayIdentidad))
print(conVertical)
