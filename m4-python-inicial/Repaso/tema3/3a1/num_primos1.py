#FUNCIONES
def comprobar_primos():
    #Comprueba si un número es primo
    for i in range(1,100):
        if i % 2 != 0:
            imprimir_primos(i)
        else:
            pass


def imprimir_primos(i):
    #Imprime los números primos
    print(i)

#CASO DE USO
comprobar_primos()