#FUNCIONES
def unir_listas(lista1,lista2):
    combinada = lista1 + lista2
    return combinada
    

#Ejemplo de uso
apellidos1 = ['rodriguez','arellano','dehn','gutierrez']
apellidos2 = ['morente','perez','avila','sanchez']


#Llamar a la función que une las listas
combinadada = unir_listas(apellidos1,apellidos2)


# Imprimir lista combinada ordenada alfabéticamente
print(sorted(combinadada))

