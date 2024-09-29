#Paso1
def saludar(nombre):
    print('Hola',nombre)

saludar('Lucas')
print()

#Paso2
def suma(a,b):
    suma = a + b
    print(suma)

num1 = 5
num2 = 10
suma(num1,num2)
print()

#Paso3
def calcular_area_rect(base,altura):
    area = base * altura
    print(area,'cm2')

lado = 34
alto = 10
calcular_area_rect(lado,alto)
print()

#Paso4
def imprimir_lista(lista):
    print(lista)

numeros = [1,2,3,4,5,6,7,8,9,10]

imprimir_lista(numeros)
print()

#Paso5
def es_par(numero):
    if numero % 2 == 0:
        print(True)
    else:
        print(False)

for i in range(1,5):
    es_par(i)
print()

#Paso6
def concatenar_sting(cadena1,cadena2):
    print(cadena1.title()+cadena2.title())

parte1 = 'java'
parte2 = 'script'
concatenar_sting(parte1,parte2)
print()

#Paso7
def obtener_maximo(lista):
    maximo = max(lista)
    print('Máximo:',maximo)

numeros = [1,2,3,4,5,6,7,8,9,10]
obtener_maximo(numeros)
print()

#Paso8
def convertir_fahrenheit_celsius(grados):
    celsius = (grados_fahrenheit - 32) * 5 / 9
    print(round(celsius,2),'ºC')

grados_fahrenheit = 80
convertir_fahrenheit_celsius(grados_fahrenheit)
print()

#Paso9
def calcular_edad(actual,nacimiento):
    edad_actual = actual - nacimiento
    print(edad_actual,'años')

año_actual = 2024
año_nacimiento = 1998
calcular_edad(año_actual,año_nacimiento)
print()

#Paso10
def es_divisible(num,divisor):
    if num % divisor == 0:
        print(True)
    else:
        print(False)

valor1 = 10
valor2 = 3
es_divisible(valor1,valor2)
print()

#Paso11
def mostrar_info_persona(nombre=None,edad=None,ciudad=None):
    print(nombre,'tiene',edad,'años y es de',ciudad)

mostrar_info_persona(nombre='Marta',edad=26,ciudad='Madrid')
print()

#Paso12
def calcular_promedio(lista = []):
    if len(lista) == 0:
        promedio = 0
    else:
        promedio = sum(lista) / len(lista)
    
    print('Promedio lista:',promedio)

calcular_promedio()
print()

#Paso13
def calcular_potencia(base,exponente=2):
    potencia = base ** exponente
    print('Potencia de',base,'elevado a',exponente,':',potencia)

calcular_potencia(10)
print()

#Paso14
def imprimir_info_alumno(nombre, edad=None, curso=None, promedio=None):
    print('Nombre:',nombre)
    if edad is not None:
        print('Edad:',edad)
    if curso is not None:
        print('Curso:',curso)
    if promedio is not None:
        print('Promedio:',promedio)

imprimir_info_alumno('Miguel')

