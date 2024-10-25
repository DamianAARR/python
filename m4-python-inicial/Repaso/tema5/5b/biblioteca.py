##### FUNCIONES #####
def manage_data(lista):
    #Cambiar los datos dentro de las tuplas
    lista_nueva = []
    lista_final = []

    [[lista_nueva.append(list(elemento))] for elemento in lista]
    
    for lista in lista_nueva:
        apellidos = list(lista[1].partition(' '))
        lista.remove(lista[1])
        lista.append(apellidos[2])
    
    [[lista_final.append(tuple(lista))] for lista in lista_nueva]

    tupla_final = tuple(lista_final)
    return tupla_final


##### CASO DE USO #####
lista_libros = [('El aleph',                'Jorge Luis Borges'),
                ('Cien años de soledad',    'Garbriel Garcia Márquez'),
                ('La ciudad y los perros',  'Mario Vargas Llosa')]

#Cambiar datos en las tuplas
datos = manage_data(lista_libros)

print(datos)

