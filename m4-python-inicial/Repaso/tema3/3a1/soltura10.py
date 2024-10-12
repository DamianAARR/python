#Funciones
def leer_lista(lista):
    #Lee las longitudes de los strings
    lista_longitudes = []
    for elemento in lista:
        longitud = len(elemento)
        # Llamar a la función que almacena longitudes
        longitudes = almacenar_longitudes(longitud,lista_longitudes)
    return longitudes


def almacenar_longitudes(longitud,lista):
    #Almacena las longitudes
    lista.append(longitud)
    return lista


#Caso de uso

lista = ['hola','mundo','de','developers','autodidactas','que','es','lo','que']

#Llamar a la función que lee la lista
longitudes = leer_lista(lista)

#Imprimir longitudes
print(longitudes)