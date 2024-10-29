##### FUNCIONES #####
def add_date(datos):
    #
    pass


def add_new_date(datos):
    #
    pass


def show_list(datos):
    #
    pass


##### CASO DE USO #####
continuar = True
asistencias = {}

while continuar:
    print()
    option = input('Elige una opción:\n1.- Registrar asistencia\n2.- Agregar fecha asistencia\n3.- Mostrar lista de asistencias\n4.- Salir\n')
    print()

    if option == '1':
        datos = add_date(asistencias)
        print()
        [[print(prod)]for prod in datos.items()]

    if option == '2':
        datos = add_new_date(datos)
        print()
        [[print(prod_act)]for prod_act in datos.items()]
        
    if option == '3':
        ventas = show_list(datos)
        print()
        print('Ventas totales del día:',ventas)
        

    if option == '4':
        print('Saliendo del programa')
        print()
        continuar = False