#FUNCIONES
def ordenar_numeros(numeros):
    ordenada = sorted(numeros)
    return ordenada


def encontrar_numero(ordenada):
    numero = ordenada[-2]
    return numero


#Ejemplo de uso
numeros = [3,5,20,45,32,43,89,76,54,24,25,81,29,38]

#Llamar a la funcion que ordene la lista
ordenada = ordenar_numeros(numeros)

#Llamar a la función que encuentre el segundo mayor
segundo_mayor = encontrar_numero(ordenada)

#Imprimir segundo mayor
print(segundo_mayor)