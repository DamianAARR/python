#Bucle que recorra los números del 2 al 100

for i in range(2,101):
    prime = True #Inicializamos prime en True por defecto

# Bucle que para cada número compruebe los divisores
    for num in range(2,i):
        if i % num == 0: #Comprueba si al divididir por 2 el resto es 0. Si es así 2 es divisor.
            prime = False #Por lo tanto no sería primo ya que los primos solo tienen divisor 1 y ellos mismos.
            break #OPCIONAL: Si en la primera división se sabe que no es primo, se rompe el bucle. Eficiencia.
    if prime == True: #Fuera del bucle: si es primo imprime el número.
        print(i)

#---CON BUCLE WHILE---


# for num in range(2,101):
#     prime = True
#     i = 2
#     while prime == True and i < num:
#         if num % i == 0:
#             prime = False
#         i = i + 1
#     if prime == True:
#         print(num)
