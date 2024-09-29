#Base de datos
lista_libros = [('El aleph',               'Jorge Luis Borges'),
                ('Cien años de soledad',   'Garbriel Garcia Márquez'),
                ('La ciudad y los perros', 'Mario Vargas Llosa')]

nombres_completos = []
apellidos = []

#Pasar tuplas a listas para poder editarlas
for i in range(len(lista_libros)):
    lista_libros[i] = list(lista_libros[i])

#Extraer los nombres
for tupla in lista_libros:
    nombres_completos.append(tupla[1])

#Extraer apellidos
for nombre in nombres_completos:
    for i in range(len(nombre)):
        if nombre[i] == ' ':
            apellidos.append(nombre[i+1::])
            break

#Cambiar nombres completos por apellidos y convertir lista en tupla
for i in range(len(lista_libros)):
    lista_libros[i][1] = apellidos[i]
    lista_libros[i] = tuple(lista_libros[i])
    
#Devolver la nueva lista de tuplas
print(lista_libros)
    
