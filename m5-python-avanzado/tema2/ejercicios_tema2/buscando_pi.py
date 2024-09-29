from mpmath import mp

#precision a 10000 dígitos
mp.dps = 10000
#valor de pi con 10000 digitos
pi_valor = mp.pi

#crear archivo pi_10000.txt
with open('pi_10000.txt') as f_objt:
    contenido = f_objt.read()
    fecha = '1206'
    if fecha in str(contenido):
        posicion = str(contenido).find(fecha) + 1
        print('Tu fecha se encuentra en la posición',posicion)
    else:
        print('Tu fecha no se encuentra en el número PI')