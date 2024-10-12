#FUNCIONES
def leer_palabras(lista,letras):
    #Lee todos los caracteres de cada palabra
    filtradas = []
    for elemento in lista:
        if any(letra in elemento for letra in letras):
            pass
        else:
            filtradas.append(elemento)
    return filtradas


#Caso de uso
lista = ['mañana','estamos','malaga','linux','desarrollo']
letras = ['t','l','y']

#Llamar a la función que lea las palabras aleatorias
palabras = leer_palabras(lista,letras)

print(palabras)
