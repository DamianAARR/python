import numpy as np
import json

file_name = "texto.txt"

try:
    with open(file_name) as f_objt:
        contenido = f_objt.read()
except:
    mensaje = "El archivo "+ file_name + " no existe en el directorio"
    print(mensaje)
else:
    palabras = contenido.split()
    num_palabras = len(palabras)
    print("El archivo " + file_name + " tiene " + str(num_palabras) + " palabras.")



