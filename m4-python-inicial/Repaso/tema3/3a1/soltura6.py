#FUNCIONES
def buscar_num_inferiores(num_user):
    #Busca los números menores que el número del usuario
    numeros = [3,5,20,45,32,43,89,76,54,24,25,81,29,38]
    inferiores = []

    for numero in numeros:
        if numero < num_user:
            inferiores.append(numero)
    return inferiores


def buscar_mayor_inferiores(inferiores):
    #Busca el número mayor
    ordenados = sorted(inferiores)
    mayor = ordenados[-1]
    return mayor


#CASO DE USO
num_user = int(input('Introduce un número: \n'))

#Llamar a la función que busca los números inferiores
num_inferiores = buscar_num_inferiores(num_user)

#Buscar el número mayor de los inferiores
mayor_inferiores = buscar_mayor_inferiores(num_inferiores)

#Imprimir número
print(mayor_inferiores)