#PASO 1
#FUNCIONES
def buscar_duplicados(lista):
    duplicados = []
    for elemento in lista:
        if lista.count(elemento) > 1:
            almacenar_duplicados(elemento,duplicados)
            lista.remove(elemento)
    # Devuelve la lista de elementos únicos
    return lista


def almacenar_duplicados(elemento,lista):
    # Almacena los duplicados
    lista.append(elemento)


def imprimir_unicos(unicos):
    # Imprime los unicos
    print(unicos)


#Ejemplo de uso
lista = ['hola','mundo','feliz','mundo','casa','hola','otro','hola']

# Llamar a la funcion que comprueba los duplicados
unicos = buscar_duplicados(lista)

# Imprimir lista de duplicados
imprimir_unicos(unicos)
