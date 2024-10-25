#PASO1 
print('----------')
mi_dic = {}
print(mi_dic)

#PASO2
print('----------')
mi_dic['nombre'] = 'Damian'
print(mi_dic)

#PASO3
print('----------')
print(mi_dic['nombre'])

#PASO4 
print('----------')
print(mi_dic.get('edad',False))

#PASO5
print('----------')
estudiante = {
    'nombre': 'lucas',
    'edad': 19,
    'materia': 'ciencia',
}
print(estudiante)

#PASO6
print('----------')
estudiante['edad'] = 17
print(estudiante)

#PASO7
print('----------')
del estudiante['materia']
print(estudiante)

#PASO8
print('----------')
for clave in estudiante.keys():
    print(clave)

#PASO9
print('----------')
agenda = {
    'juan': 1234567890,
    'joana': 9876543210,
    'jimena': 5555555555,
}
print(agenda)

#PASO10
print('----------')
agenda['julio'] = 9998887777
print(agenda)

#PASO11
print('----------')
print(len(agenda))

#PASO12
print('----------')
claves = []
for clave in agenda.keys():
    claves.append(clave)
print(claves)

#PASO13
print('----------')
if 'juan' in agenda:
    print(True)
else:
    print(False)

#PASO14
print('----------')
jimena = agenda.pop('jimena')
print(agenda)

#PASO15
print('----------')
for clave, valor in agenda.items():
    print(clave.title(),':',valor)

#PASO16
print('----------')
print(agenda.get('juan','Clave no encontrada'))

#PASO17
print('----------')
agenda.clear()
print(agenda)