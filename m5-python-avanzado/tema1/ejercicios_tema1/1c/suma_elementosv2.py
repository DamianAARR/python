def sumar_lista(lista):

    if len(lista) ==1:
        return lista[0]
    else:
        return lista[0] + sumar_lista(lista[1:])


lista = [1,2,3,4,5,6,7,8,9]

suma_total = sumar_lista(lista)
print(suma_total)