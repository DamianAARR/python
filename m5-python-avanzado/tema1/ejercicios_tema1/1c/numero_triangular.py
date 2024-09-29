def calcular_numero_triangular(num_base):
    
    if num_base == 1:
        return 1
    else:
        return num_base + calcular_numero_triangular(num_base-1)


num_tiangular = calcular_numero_triangular(5)
print(num_tiangular)