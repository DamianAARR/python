#FUNCIONES
def saludar(nombre):
    print('Hola',nombre,', bienvenido!')


def calcular_promedio(lista = []):
    if len(lista) == 0:
        print(lista)
    else:
        promedio = sum(lista) / len(lista)
        print('Promedio:',promedio)


#PASO1
print('-----')
saludar(nombre = 'Damian')

#PASO12
print('-----')
lista = [1,2,3,4,5]
calcular_promedio(lista)
