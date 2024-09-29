def calcular_potencia(base,exponente):
    """Calcular potencia de forma recursiva"""

    # planteamos caso base
    if exponente == 0:
        return 1
    # plantear la sentencia recursiva
    else:
        return base * calcular_potencia(base,exponente-1)
    

potencia = calcular_potencia(3,4)
print(potencia)