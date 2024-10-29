
##### FUNCIONES #####
def add_task(database):
    #Añade tareas al diccionario que se usa de database
    print()
    database[input('Nº de tarea:\n')] = {'nombre': input('Nombre de la tarea:\n'), 'descripcion': input('Descripción:\n')}
    return database
    

def add_manager(proyecto):
    #Asignar un manager a cada tarea
    print()
    proyecto[input('Nº de tarea\n')]['manager'] = input('Nombre del manager:\n')
    return proyecto
    
    
def change_descript(proyecto):
    #Cambia la descripción de cada tarea
    print()
    proyecto[input('Nº de tarea\n')]['descripcion'] = input('Descripción:\n')
    return proyecto
    

def show_tasks(proyecto):
    #Imprime la lista de tareas
    print()
    for info_task in proyecto.values():
        print(info_task['nombre'].title(),'-',info_task['manager'].title())
        
    
##### CASO DE USO #####

continuar = True
database ={}

while continuar:
    print()
    option = input('Elige una opción:\n1.-Agregar tarea\n2.-Asignar responsable\n3.-Actualizar descripción\n4.-Mostrar lista de tareas y responsables\n5.-Salir del programa\n')
    
    if option == '1':
        proyecto = add_task(database)
        print()
        [[print(tarea)]for tarea in proyecto.items()]
    
    if option == '2':
        proyecto = add_manager(proyecto)
        print()
        [[print(tarea)]for tarea in proyecto.items()]
        
    if option == '3':
        descrip_act = change_descript(proyecto)
        print()
        [[print(tarea)]for tarea in descrip_act.items()]
    
    if option == '4':
        show_tasks(proyecto)
    
    if option == '5':
        print()
        print('Saliendo del programa')
        print()
        continuar = False