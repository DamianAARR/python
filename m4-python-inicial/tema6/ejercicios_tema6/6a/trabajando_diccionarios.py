#Paso1
mi_diccionario = {}

#Paso2
mi_diccionario['nombre'] = 'dartik'

#Paso3
print(mi_diccionario['nombre'])

#Paso4
print(mi_diccionario.get('edad',False)) #Si no existe edad, imprime False

#Paso5
estudiante = {
    'nombre': 'pepite',
    'edad': 26,
    'materia': 'informatica',
}

#Paso6
estudiante['edad'] = 30

#Paso7
del estudiante['materia']

#Paso8
for nombre, dato in estudiante.items():
    print(nombre.title(), dato)

#Paso9
agenda = {
    'Juan': '1234567890',
    'Joana': '9876543210',
    'Jimena': '5555555555',
}

#Paso10
agenda['Julio'] = 9998887777

#Paso11
print('Numero de entradas agenda:',len(agenda))

#Paso12
claves = list(agenda.keys())


#Paso13
if 'Juan' in claves:
    print(True)
else:
    print(False)

#Paso14
del agenda['Jimena']

#Paso15
for nombre, numero in agenda.items():
    print(nombre,':',numero)

#Paso16
print('Numero de Juan:',agenda.get('Juan','Clave no encontrada'))

#Paso17
agenda.clear()
print(agenda)
