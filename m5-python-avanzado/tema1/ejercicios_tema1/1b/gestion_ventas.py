# ---- FUNCIONES ----
def agregar_producto(productos_vendidos):
    # ----- Permite agregar los productos a la base de datos
    venta = {}
    venta['producto'] = input('Nombre del producto: ')
    venta['precio'] = input('Precio del producto: ')
    productos_vendidos.append(venta)
    return productos_vendidos

def mostrar_ventas(productos):
    # ----- Muestra las ventas que se han realizado
    print()
    for venta in productos:
        print(venta['producto'].title(),':',venta['precio'],'euros')
    print()

# ---- FUNCIONALIDAD ----
continuar = True
lista_productos_vendidos = []

while continuar:
    opcion = input('1. Agregar producto\n2. Mostrar ventas\n3. Salir del programa\n')
    
    if opcion == '1':
        productos_vendidos = agregar_producto(lista_productos_vendidos)
    
    elif opcion == '2':
        mostrar_ventas(productos_vendidos)
    
    elif opcion == '3':
        print()
        print('Saliendo del programa')
        continuar = False
    else:
        print('Esa opción no es válida, escoge otra')
