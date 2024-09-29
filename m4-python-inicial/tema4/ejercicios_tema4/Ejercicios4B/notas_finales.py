#Importar librerias
import numpy as np

#Pedir el número de alumnos
numAlu = int(input('Cuantos alumnos hay?: '))
numNotas = int(input('Cuantas notas vas a introducir por alumno? '))
numNotasConst = numNotas
contadorNotas = 0
contadorAlumnos = 1
contadorNotas2 = 1
#Almacenar datos de los alumnos
notas_estudiantes = np.empty((numAlu,numNotas))

for i in range(0,numAlu):
    for j in range(0,numNotas):
        nota = float(input('Introduce una nota:'))
        #Multiplicar por 0.3 o 0.1 (30% y 10%) según la posición
        if contadorNotas2 < numNotas:
            notas_estudiantes[i,j] = nota * 0.3
            contadorNotas += 1
            contadorNotas2 += 1
        else:
            notas_estudiantes[i,j] = nota * 0.1
            contadorNotas += 1
            contadorNotas2 += 1
        
        if contadorNotas == numNotas:
            if contadorAlumnos == numAlu:
                break
            else:
                print()
                print('---Siguiente alumno:---')
                contadorNotas = 0
                contadorNotas2 = 1
    contadorAlumnos += 1

suma_notas = notas_estudiantes.sum(1)
notas_finales = suma_notas.reshape(numAlu,1)

#Devolver notas finales en una sola columna
print()
print('Notas finales:')
print(notas_finales)