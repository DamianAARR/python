#Funciones
def leer_lista(lista):
    #Lee los strings
    lista_mayus = []
    for elemento in lista:
        # Llamar a la función que almacena longitudes
        mayus = almacenar_mayus(elemento,lista_mayus)
    return mayus


def almacenar_mayus(elemento,lista):
    #Almacena las longitudes
    lista.append(elemento.upper())
    return lista


#Caso de uso

lista = ['hola','mundo','de','developers','autodidactas','que','es','lo','que']

#Llamar a la función que lee la lista
mayus = leer_lista(lista)

#Imprimir longitudes
print(mayus)