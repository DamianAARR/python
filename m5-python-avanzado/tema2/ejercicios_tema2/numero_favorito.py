#Importar módulos
import json

# --FUNCIONES--
def preguntar_numero():
    num_user = int(input('Introduce tu número favorito: '))
    almacenar_numero(num_user)
    return num_user

def comprobar_numero():
    try:
        with open('favorito.json') as file:
            num_fav = json.load(file)
        return num_fav
    
    except FileNotFoundError:
        return None


def almacenar_numero(num_user):
    #Almacena el num fav en un archivo .json
    
    with open('favorito.json', "w") as f_objt:
        json.dump(num_user,f_objt)

   

#Funcionalidad usuario

#Comprobar si el número está almacenado
num_fav = comprobar_numero()

if num_fav:
    print('Tu número fav es: ',num_fav)
else:
    num_fav = preguntar_numero()
    print('Tu número favorito es: ',num_fav)
    



