#Crear lista de números enteros

numbers = [3,5,3,5,7,1,3,5,12,3,23,5,132,543,3,2,32,4,45,2,4,12,3,31,2,32,12,3,]
total_primos = 0
primos = []
suma_primos = 0
#Bucle para recorrer lista
for num in numbers:
    prime = True
    if num < 2:
        prime = False
    else:
        for i in range(2,num):
            if num % i == 0:
                prime = False
                break
    if prime == True:
        primos.append(num)
        total_primos = total_primos + 1
        suma_primos = suma_primos + num

print('Lista de números primos:',primos)
print('Números primos encontrados:',total_primos)
print('Suma total de los números primos:',suma_primos)