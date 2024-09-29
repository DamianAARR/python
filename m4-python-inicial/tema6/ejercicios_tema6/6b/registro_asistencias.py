#Crear database vacía (Diccionario)
asistencia = {}

#Añadir alumnos y asistencias
asistencia['juan'] = [23,15,21,20,12,9]
asistencia['pedro'] = [10,15,22,17,24,18]
asistencia['lucas'] = [17,23,14,16,25,13]

#Añadir nuevas fechas
asistencia['juan'].append(19)

#Devolver estudiantes y fechas de asistencia
for nombre,fechas in asistencia.items():
    print(nombre.title(),':',*fechas)
    print()