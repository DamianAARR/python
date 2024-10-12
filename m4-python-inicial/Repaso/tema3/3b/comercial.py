#FUNCIONES
def contar_ventas(unidades):
    # Cuenta las ventas totales
    total_ventas = sum(unidades)
    return total_ventas


def facturacion_producto(unidades,precios):
    #Cuenta el dinero facturado
    facturacion = []

    for i in range(0,len(unidades)):
        fact_prod = unidades[i] * precios[i]
        facturacion.append(fact_prod)

    return facturacion


def print_results(totalventas,totalfact):
    #Devuelve los resultados

    print('Se han vendido',totalventas,'unidades en total.')
    print('Facturación por producto:\n')
    for i in range(0,len(totalfact)):
        if totalfact[i] != 0:
            print('Producto',i+1,':',totalfact[i],'euros.')
    print()
    print('Facturación total:',str(sum(totalfact)),'euros.')


#CASO DE USO
unds_vendidas = [3,1,0,0,7,2,0,0,4,0]
precio_unidad = [30,9.8,42.5,32.6,71.5,44,21.2,53.2,25.3,57.8]

#Llamar a la función que cuenta las ventas totales
total_ventas = contar_ventas(unds_vendidas)

#Llamar a la función que calcula la facturación por producto
facturacion_individual = facturacion_producto(unds_vendidas,precio_unidad)

#Llamar a la función que devuelve los resultados
print_results(total_ventas,facturacion_individual)

