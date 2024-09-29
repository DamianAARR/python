def sumar_lista(lista,suma_total):

    if len(lista) ==0:
        return suma_total
    else:
        suma_total = suma_total + lista[-1]
        del lista[-1]
        return sumar_lista(lista,suma_total)


lista = [1,2,3,4,5,6,7,8,9]

suma_total = sumar_lista(lista[:],0)
print(suma_total)