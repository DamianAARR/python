
def calcular_factorial(n):
    """Calcula el factorial de n de forma recursiva:"""
    #INPUT:
    # - n: int
    #OUTPUT:
    # - resultado: int
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_factorial(n-1)
    

factorial = calcular_factorial(3)
print(factorial)