##### FUNCIONES #####
def add_votes(datos):
    #Añade candidatos y votos al registro
    nombre = input('Nombre del candidato:\n')
    datos[nombre] = int(input('Votos:\n'))
    return datos


def show_list(datos):
    #Muestra la lista de candidatos y sus votos
    for candidato in datos.items():
        print(candidato)
    

def show_winner(datos):
    #Muestra el candidato ganador
    winner = max(datos, key=datos.get)
    return winner


def votes_percent(datos):
    #Calcula los porcentajes de votos
    votos_totales = 0
    for votos in datos.values():
        votos_totales += votos
    print()
    for clave, valor in datos.items():
        porcentaje = valor * 100 / votos_totales
        print(clave.title(),':',porcentaje,'%')


##### CASO DE USO #####
continuar = True
database ={}

while continuar:
    print()
    option = input('Elige una opción:\n1.-Agregar candidato\n2.-Mostrar lista\n3.-Mostrar ganador\n4.-Porcentajes de votos\n5.-Salir del programa\n')
    
    if option == '1':
        registro = add_votes(database)
        print()
        print(registro)
        #[[print(candidato)]for candidato in registro.items()]
    
    if option == '2':
        show_list(registro)
        
    if option == '3':
        winner = show_winner(registro)
        print()
        print('Candidato ganador:',winner.title())
    
    
    if option == '4':
        votes_percent(registro)
        print()
        
    
    if option == '5':
        print()
        print('Saliendo del programa')
        print()
        continuar = False
