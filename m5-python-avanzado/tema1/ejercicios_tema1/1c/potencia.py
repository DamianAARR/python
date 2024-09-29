def calcular_potencia(base,elevacion,resultado):
    """Calcular potencia de forma recursiva"""

    if elevacion == 0:
        return resultado
    else:
        resultado = base * resultado
        return calcular_potencia(5,elevacion-1,resultado)
    

potencia = calcular_potencia(5,4,1)
print(potencia)