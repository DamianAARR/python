#Paso18


estudiantes = [
    {'nombre': 'Juan', 'edad': 17,},
    {'nombre': 'Paco', 'edad': 15,},
]

for i in range(len(estudiantes)):
    print(estudiantes[i]['nombre'],estudiantes[i]['edad'])
print('--------')

#Paso19
alumno3 = {
    'nombre': 'Luis',
    'edad': 13,
}

estudiantes.append(alumno3)

for i in range(len(estudiantes)):
    print(estudiantes[i]['nombre'],estudiantes[i]['edad'])

#Paso20
estudiantes.pop(1)
print('--------')
for i in range(len(estudiantes)):
    print(estudiantes[i]['nombre'],estudiantes[i]['edad'])

#Paso21
estudiantes[0]['edad'] = 15
print('--------')
for i in range(len(estudiantes)):
    print(estudiantes[i]['nombre'],estudiantes[i]['edad'])