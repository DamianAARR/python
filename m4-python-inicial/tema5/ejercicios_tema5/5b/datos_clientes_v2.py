#Bases de datos
base_datos1 = [("Juan",  "juan@example.com",  "555-1234"),
               ("Maria", "maria@example.com", "555-5678"),
               ("Pedro", "pedro@example.com", "555-9012")]

base_datos2 = [("Juan", "Calle 123",  ["Libro1", "Libro2"]),
               ("Maria", "Calle 456", ["Libro3"]),
               ("Luis", "Calle 789",  ["Libro4"])]

#Encontrar los clientes comunes en las dos bases de datos
nombres1 = set([cliente[0] for cliente in base_datos1])
nombres2 = set([cliente[0] for cliente in base_datos2])

nombres_comunes = nombres1 & nombres2

#Crear nueva lista con los datos de los clientes comunes
datos_clientes_comunes = []

for cliente1 in base_datos1:
    if cliente1[0] in nombres_comunes: #Si está en la lista de nombres comunes va a estar en basedatos2
        for cliente2 in base_datos2:
            if cliente2[0] == cliente1[0]: #Si son el mismo nombre, añadimos todos los datos necesarios
                datos_clientes_comunes.append((cliente1[0],cliente1[1],cliente1[2],cliente2[1],cliente2[2]))

print(datos_clientes_comunes)