#FUNCIONES
def pintar_asteriscos(numeroUsuario):
     asteriscos = []
     for i in range(0,numeroUsuario):
          asteriscos.append('*')
          print(*asteriscos)
     for i in range(1,numeroUsuario):
          asteriscos.pop()
          print(*asteriscos)


#Pedir un número entero por pantalla
numeroUsuario = int(input('Introduce un número entero: '))

#Llamar a la función que pinta la figura
pintar_asteriscos(numeroUsuario)


