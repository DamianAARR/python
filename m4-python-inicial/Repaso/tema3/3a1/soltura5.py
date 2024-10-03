#FUNCIONES
def comprobar_divisibles(num_user):
    #Comprueba los números divisibles entre num_user del 1 al 10
    lista = []
    for i in range(1,101):
        if i % num_user == 0:
            divisibles = guardar_divisibles(i,lista)
    return divisibles


def guardar_divisibles(num,lista):
    #Almacena los divisibles en una lista
    lista.append(num)
    return lista


def sumar_divisibles(divisibles):
    #Suma los divisibles
    suma = sum(divisibles)
    return suma


#CASO DE USO
num_user = int(input('Introduce un número: \n'))

#Llamar a función que comprueba y almacena los divisibles
divisibles = comprobar_divisibles(num_user)

#Llamar a la función que suma los divisibles
suma_divisibles = sumar_divisibles(divisibles)

#Imprimir la suma total
print(suma_divisibles)
