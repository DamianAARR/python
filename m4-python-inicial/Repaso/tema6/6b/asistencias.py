##### FUNCIONES #####
def add_student(datos):
    #Añade una fecha de asistencia
    datos[input('Nº de estudiante:\n')] = {'nombre': input('Nombre de estudiante:\n'), 'asistencias': [input('Fecha de asistencia:\n')]}
    return datos


def add_new_date(datos):
    #Añadir nueva asistencia a estudiante ya existente
    datos[input('Nº de estudiante:\n')]['asistencias'].append(input('Introduce la nueva asistencia:\n'))
    return datos


def show_list(datos):
    #Muestra la lista de estudiantes y fechas de asistencia
    for info in datos.values():
        print('Estudiante:',info['nombre'].title())
        print()
        print('Asistencias:',info['asistencias'])
        print()


##### CASO DE USO #####
continuar = True
asistencias = {}

while continuar:
    print()
    option = input('Elige una opción:\n1.- Registrar estudiante y asistencia\n2.- Agregar nueva asistencia\n3.- Mostrar lista de asistencias\n4.- Salir\n')
    print()

    if option == '1':
        datos = add_student(asistencias)
        print()
        [[print(student)]for student in datos.items()]

    if option == '2':
        datos = add_new_date(datos)
        print()
        [[print(prod_act)]for prod_act in datos.items()]
        
    if option == '3':
        ventas = show_list(datos)
        
        
    if option == '4':
        print('Saliendo del programa')
        print()
        continuar = False