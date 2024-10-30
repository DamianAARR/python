##### FUNCIONES #####
def add_employee(datos):
    #Añade empleados nuevos
    nombre = input('Nombre:\n')
    datos[nombre] = {'salario': int(input('Salario:\n')), 'dept': input('Departamento:\n')}
    return datos


def update_salary(datos):
    #Actualizar Salario
    nombre = input('Nombre:\n')
    datos[nombre]['salario'] = input('Nuevo salario:\n')
    return datos


def show_employees(datos):
    #Muestra lista de empleados
    print()
    for name, info in datos.items():
        print(name.title(), 'Salario:',info['salario'],'Dept:',info['dept'])
    

def show_dept_salary(datos):
    #Muestra la media salarial por departamento
    salarios_it = []
    salarios_finance = []
    salarios_consulting = []

    for nombre, info in datos.items():
        if info['dept'] == 'it':
            salario = info['salario']
            salarios_it.append(salario)
        elif info['dept'] == 'finance':
            salario = info['salario']
            salarios_finance.append(salario)
        else:
            salario = info['salario']
            salarios_consulting.append(salario)
    
    promedio_it = sum(salarios_it) / len(salarios_it)
    promedio_finance = sum(salarios_finance) / len(salarios_finance)
    promedio_consulting = sum(salarios_consulting) / len(salarios_consulting)

    return promedio_it, promedio_finance, promedio_consulting


##### CASO DE USO #####
continuar = True
database ={}

while continuar:
    print()
    option = input('Elige una opción:\n1.-Agregar empleado\n2.-Actualizar salario\n3.-Mostrar empleados\n4.-Promedio salarial por dept\n5.-Salir del programa\n')
    
    if option == '1':
        registro = add_employee(database)
        print()
        [[print(employee)]for employee in registro.items()]
    
    if option == '2':
        registro = update_salary(registro)
        print()
        [[print(employee)]for employee in registro.items()]
        
    if option == '3':
        show_employees(registro)
        print()
        #[[print(tarea)]for tarea in descrip_act.items()]
    
    if option == '4':
        it, finance, consulting = show_dept_salary(registro)

        print()
        print('Salarios promedio:\n-IT:',it,'\n-Finance:',finance,'\n-Consulting:',consulting)
    
    if option == '5':
        print()
        print('Saliendo del programa')
        print()
        continuar = False

