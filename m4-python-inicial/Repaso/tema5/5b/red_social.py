##### FUNCIONES #####
def borrar_duplicados(datos):
    #Borra los amigos duplicados
    nueva_base = []
    set_convert = set()

    [[nueva_base.append(list(elemento))] for elemento in datos]

    for lista in nueva_base:
        for i in range(0,len(lista)):
            set_convert = set(lista[1])
            lista.remove(lista[1])
            lista.append(list(set_convert))

    return nueva_base


def convert_tuplas(lista):
    #Convierte la base de datos en una tupla de tuplas
    for i in range(0,len(lista)):
        tupla_convert = tuple(lista[i])
        lista[i] = tupla_convert
    
    base_tuplas = tuple(lista)
    return base_tuplas


##### CASO DE USO #####
red_social = [("Juan", ["Maria", "Pedro","Luis"]), ("Maria", ["Juan", "Pedro", "Juan"]), ("Pedro", ["Juan", "Maria"]), ("Luis", ["Juan"])]

# 1.- Eliminar cuentas duplicadas
datos_red = borrar_duplicados(red_social)

# 2.- Devolver tupla de tuplas
red_tuplas = convert_tuplas(datos_red)
print('Base de datos en tupla:\n',red_tuplas)

