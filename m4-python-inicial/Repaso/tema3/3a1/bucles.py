#FUNCIONES
def dibujo(num):
    # Dibuja un triángulo con asteriscos
    for i in range(1,num + 1):
        print('*' * i)
    for i in range(num-1,0,-1):
        print('*' * i)


#Ejemplo de uso
num_user = int(input('Introduce un número:\n'))

#Llamar función dibujadora
dibujo(num_user)