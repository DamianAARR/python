# FUNCIONES
def comprobar_primos(numeros):
    #Comprueba cuáles son los números primos de la lista
    primos = []

    for numero in numeros:
        primo = True
        if numero < 2:
            primo = False
        else:
            for i in range(2,numero):
                if numero % i == 0:
                    primo = False
                    break

        if primo == True:
            primos.append(numero)
    return primos


def contar_primos(primos):
    #Comprueba el número de primos
    num_primos = len(primos)
    return num_primos


def sumar_primos(primos):
    #Suma los números primos encontrados
    suma_primos = sum(primos)
    return suma_primos


#CASO DE USO
numeros = [1,2,3,4,5,6,7,8,9,10]

#LLamar función que comprueba los números primos
primos = comprobar_primos(numeros)

#Llamar a la función que cuenta los primos
num_primos = contar_primos(primos)

#Llamar a la función que suma los primos
suma = sumar_primos(primos)

print('Números primos:',primos)
print('Total números primos:',num_primos)
print('Suma de todos los primos:',suma)
