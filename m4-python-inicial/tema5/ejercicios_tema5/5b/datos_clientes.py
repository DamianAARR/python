#Bases de datos
base_datos1 = [("Juan",  "juan@example.com",  "555-1234"),
               ("Maria", "maria@example.com", "555-5678"),
               ("Pedro", "pedro@example.com", "555-9012")]

base_datos2 = [("Juan", "Calle 123",  ["Libro1", "Libro2"]),
               ("Maria", "Calle 456", ["Libro3"]),
               ("Luis", "Calle 789",  ["Libro4"])]

nombres_datos1 = []
nombres_datos2 = []
base_datos_comunes = []
nombre1 = []
nombre2 = []

#Desemaquetar tuplas 'base_datos_1'
for i in range(len(base_datos1)):
    nombre, email, telefono = base_datos1[i]
    nombres_datos1.append(nombre)

nombres1 = set(nombres_datos1)

#Desemaquetar tuplas 'base_datos_2'
for i in range(len(base_datos2)):
    nombre, calle, pedido = base_datos2[i]
    nombres_datos2.append(nombre)

nombres2 = set(nombres_datos2)

#Sacar nombres comunes
comunes = list(nombres1 & nombres2)

nombre1.append(comunes[0])
nombre2.append(comunes[1])

base_datos_comunes.append(nombre1)
base_datos_comunes.append(nombre2)

for i in range(len(base_datos_comunes)):
    base_datos_comunes[i] = tuple(base_datos_comunes[i])
    
print(base_datos_comunes)



