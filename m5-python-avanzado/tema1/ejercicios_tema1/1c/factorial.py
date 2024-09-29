
def calcular_factorial(num,producto):
    """Calcula el factorial de n de forma recursiva:"""
    #INPUT:
    # - n: int
    #OUTPUT:
    # - resultado: int
    if num ==1:
        return producto
    else:
        producto = producto * num
        return calcular_factorial(num-1,producto)
    

num_factorial = calcular_factorial(5,1)
print(num_factorial)