#Base de datos
lista_libros = [('El aleph',               'Jorge Luis Borges'),
                ('Cien años de soledad',   'Garbriel Garcia Márquez'),
                ('La ciudad y los perros', 'Mario Vargas Llosa')]
nueva_lista = []
titulos = []
apellidos = []

for titulo,nombre in lista_libros:
    apellido = nombre.split()[-1]
    nueva_lista.append((titulo,apellido))

print(nueva_lista)