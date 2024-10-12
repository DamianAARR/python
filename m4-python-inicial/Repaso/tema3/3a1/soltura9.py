#Funciones
def comprobar_positivos():
    #Comprueba cuales son positivos
    enteros = [2,-3,2,6,4,-4,-2,6,2-3245,2,4,-2,-43,4,7,5,-3,-3,-1,-6,34,3]
    positivos = []
    for entero in enteros:
        if entero > 0:
            lista_positivos = almacenar_positivo(entero,positivos)
    return lista_positivos


def almacenar_positivo(numero,lista):
    #Almacena los positivos en una nueva lista
    lista.append(numero)
    return lista


def imprimir_mensaje(positivos):
    print('Lista de positivos:',*positivos)


#Caso de uso
#Llamar funciona que comprueba los positivos
positivos = comprobar_positivos()

#Llamar función que devuelve los positivos
imprimir_mensaje(positivos)