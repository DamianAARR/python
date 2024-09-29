# -- FUNCIONES --
def sumar(num1,num2):
    # Suma los dos valores introducidos
    
    resultado = num1 + num2
    return resultado

# -- ALGORÍTMO --
continuar = True

while continuar:
    try:
        num1 = int(input('Introduce un número:\n'))
        num2 = int(input('Introduce otro número:\n'))
        resultado = sumar(num1,num2)
        print('El resultado de la suma es: ',resultado)
        continuar = False

    except ValueError:
        print('Has introducido un caracter inválido. Prueba de nuevo.')
        print()