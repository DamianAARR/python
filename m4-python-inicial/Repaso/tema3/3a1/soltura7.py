#funciones
def comprobar_comunes(lista1,lista2):
    lista_comunes = []
    for elemento in lista1:
        if elemento in lista2:
            lista_comunes.append(elemento)
    return lista_comunes


#caso de uso
lista1 = ['naranja','hola','primero','mundo','mañana']
lista2 = ['hola','lucas','primeo','mundo','lunes']

#Llamar a la funciona que comprueba los comunes
comunes = comprobar_comunes(lista1,lista2)

#Devolver comuenes
print(comunes)