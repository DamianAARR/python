#Importar librerias
import numpy as np

#Pedir el número de alumnos
numAlu = int(input('Cuantos alumnos hay?: '))
numNotas = int(input('Cuantas notas vas a introducir por alumno? '))
contadorNotas = 0
contadorAlumnos = 1

#Almacenar datos de los alumnos
notas_estudiantes = np.empty((numAlu,numNotas))

for i in range(0,numAlu):
    for j in range(0,numNotas):
        nota = float(input('Introduce una nota:'))
        notas_estudiantes[i,j] = nota
        contadorNotas += 1

        if contadorNotas == numNotas:
            if contadorAlumnos == numAlu:
                break
            else:
                print()
                print('---Siguiente alumno:---')
                contadorNotas = 0
    contadorAlumnos += 1

#Extraer las notas
examen1 = notas_estudiantes[:,0]
examen2 = notas_estudiantes[:,1]
trabajo_final = notas_estudiantes[:,2]
participacion = notas_estudiantes[:,3]

notas_finales = examen1 * 0.3 + examen2 * 0.3 + trabajo_final * 0.3 + participacion * 0.10

#Devolver las notas finales con un bucle
print()
print('NOTAS FINALES:')

for i in range(0,len(notas_finales)):
    print('La nota final del alumno' ,i+1, 'es:', notas_finales[i].round(1))

