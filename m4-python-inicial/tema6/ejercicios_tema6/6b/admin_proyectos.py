#Crear database vacía (Diccionario)
proyecto = {}

#Añadir tareas a database
proyecto['tarea1'] = {'nombre':'diseño', 'descripcion' : 'diseño de la web en figma', 'responsable': 'juan'}
proyecto['tarea2'] = {'nombre':'desarrollo', 'descripcion' : 'desarrollo de la web con react', 'responsable': 'pedro',}
proyecto['tarea3'] = {'nombre':'seo', 'descripcion' : 'articulo para posicionamiento seo', 'responsable': 'ana',}

#Añadir nueva tarea
proyecto['tarea4'] = {'nombre':'lanzamiento', 'descripcion' : 'lanzar la web con ads', 'responsable': 'lucas',}

#Asignar nuevo responsable a tarea existente
proyecto['tarea2']['responsable'] = 'pedro, damian'

#Actualizar descripción de tarea
proyecto['tarea1']['descripcion'] = 'diseñar la web con photoshop'
print(proyecto['tarea1']['descripcion'])

#Mostrar la lista completa de tareas y responsables
for tarea, info_tarea in proyecto.items():
    print(tarea.title(),':',info_tarea['nombre'].title(),'-', info_tarea['responsable'].title())

