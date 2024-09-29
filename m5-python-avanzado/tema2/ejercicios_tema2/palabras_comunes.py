
with open('texto.txt') as f_objt:
    palabra = 'en'
    contenido = f_objt.read()
    palabras = contenido.split()
    num_veces = palabras.count(palabra)

print('La palabra (',palabra,') aparece',num_veces,'veces')

    


