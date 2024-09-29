#Funciones
def mostrar_contenido(filename):
    try:
        with open(filename) as f_objt:
            contenido = f_objt.read()
            print()
            print(contenido)
            

    except FileNotFoundError:
        pass
        

#Funcionalidad
filenames = ['dogs.txt','cats.txt']

for filename in filenames:
    mostrar_contenido(filename)

print()