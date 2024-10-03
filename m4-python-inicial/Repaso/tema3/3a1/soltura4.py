#FUNCIONES
def comprobar_mayores(num):
    # Comprueba los números mayores del número introducido por el usuario
    numeros = [3,5,20,45,32,43,89,76,54,24,25,81,29,38]
    mayores = []

    for numero in numeros:
        if numero > num:
            mayores.append(numero)
    return mayores


#Caso de uso
num_user = int(input('Introduce un número: \n'))

#Llamar a la funcion que compruebe los números mayores
mayores = comprobar_mayores(num_user)

#Imprimir mayores (ordenados)
print(sorted(mayores))