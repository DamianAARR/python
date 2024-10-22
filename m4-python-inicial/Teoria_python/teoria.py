#TEORÍA PYTHON


#SINTÁXIS BÁSICA

#1.- Las variables no tiene que ser definidas como haciamos en pseudocódigo
# sino que se inicializan directamente
numero_entero = 42
numero_decimal = 12.5
texto = 'Hola Mundo'
variable_logica = True


#IMPORTANTE: Al principio nos puede venir bien inicializarlas de forma específica
numero_entero = int(42)
numero_decimal = float(12.5)
texto = str('Hola Mundo')
variable_logica = bool(True)


#Podemos inicicalizar varias variables en la misma linea 
x = y = z = 10
print(x,y,z)

x,y,z = 12, 6, 98
print(x,y,z)

nombre,apellido,apellido2 = 'Damian', 'Arellano', 'Rodriguez'
print(nombre,apellido,apellido2)

ingles,frances,espanol = True, False, True
print(ingles,frances,espanol)

nombre,edad,altura = 'Damian', 25, 1.82
print(nombre,edad,"años", altura, "metros") 

#Lo que en pseudocodigo era 'Leer' en Python es 'variable = input() '
#IMPORTANTE: input solo lee en tipo texto, ya sea una palabra, número, decimal, etc
# lo lee como tipo texto, como un string.
años = input()
nombre = input()
num1 = input()

#Pero podemos convertir ese imput en entero, float, etc.
edad = int(input('Cuantos años tienes?'))
print('Entonces has vivido', 365*edad, 'días')

#La funcion 'type' nos dice de qué tipo de dato es cada variable
numero_entero = 42
numero_decimal = 45.5
texto = 'Hola mundo'
logico = True

print(type(numero_entero), type(numero_decimal), type(texto), type(logico))

#Podemos dar valores con números y letras a los booleanos.
#Si es '0' será False y si es '1 o mayor' será True
boolean_0 = bool(0) #False
boolean_1 = bool(1) #True
boolean_2 = bool(34.2) #True

#Si es una string deberá tener contenido para ser True
boolean_3 = bool('') #False
boolean_4 = bool('hola') #True

#Para inicializar un string podemos usasr '', "", ''' ''' o incluso combinarlas.
string1 = 'Hola mundo'
string2 = "Hola mundo"
string3 = 'Hola mundo de "Python"'

string4 = ''' Este string
        me permite tener
        saltos de línea'''

#Funciones internas / Al combinarlas en una misma linea influye el orden en el que se colocan
title() - Primera mayúscula
upper() - Todo mayúscula
lower() - Todo minúscula
rstrip() - Eliminar espacio a la derecha (Elimina el espacio a la hora de imprimirlo pero no en el valor de la variable)
lstrip() - Eliminar espacio a la izquierda (Elimina el espacio a la hora de imprimirlo pero no en el valor de la variable)
strip() - Eliminar espacios a drch e izq (Elimina el espacio a la hora de imprimirlo pero no en el valor de la variable)
replace() - Cambiar caractéres por otros (replace("."," ") reemplaza el punto por un espacio)
find() - Buscar parte de un string dentro de un string. Te devuelve la posición donde empieza EJ: string = 'Hola Mundo' / string.find(Hola) = 0 / string.find(do) = 8
startswith() - Comprueba si el string empieza con el valor que le damos EJ: string = 'Hola Mundo' /string.startswith('Hol') = True / string.startswith('Hey') = False
endswith() - Comprueba si el string termina con el valor que le damos EJ: string = 'Hola Mundo' /string.endswith('Hol') = False / string.endswith('do') = True
.split() - #Separa un string por los espacios y devuelve una lista de strings
.isnumeric() #Comprueba si los elementos de un string son todos numéricos
.isinstance() #ABAJO
valor = 124
if isinstance(valor, (int, float, complex)): #Devuelve True o False. Si solo quiero saber si es entero: isinstance(valor, int)
    print('Es un número')

.join() #Une todos los elementos de un iterable en una sola cadena con el separador indicado. Tienen que ser strings.
cadenas = ['Hola','Mundo']
cadena = ' '.join(cadenas) #Imprime: Hola Mundo
cadena = '-'.join(cadenas) #Imprime: Hola-Mundo

#Concatenar dos string o más
print('Escribe tu nombre')
nombre = input()
print('Escribe tu apellido')
apellido = input()
nombre_completo = nombre + ' ' + apellido
mensaje = "Hola, " + nombre_completo.title() + "!"
print(mensaje)

#Imprimir strings de distintas formas
nombre = 'Damian'

print('Hola',nombre,'!') #--> Hola Damián !
print('Hola ' + nombre + '!') #--> Hola Damián!

saludo = 'Hola ' + nombre + '!'
print(saludo) #--> Hola Damián!

edad = 25
print('Tengo',str(edad),'años')
print(f"Tengo {edad} años") #f formatted string literals --> {} replacement field --> reemplaza la variable por su valor

#Imprimir con saltos de línea o sangría
print('Lenguajes:\nFrontend:\tHTML\tCSS\tJavaScript\nBackend:\tPython\tJava\tRust')

#Revertir un string
nombre = "Damian"
print(nombre[::-1]) #Imprime: naimaD

#Imprimir o tener en cuenta una sola posición de un string
print(nombre[0]) #Imprime: D

if nombre[0] == 'D':
    return True #Otro ejemplo donde usarlo

#Longitud de un string
nombre = "Damian"
print(len(nombre)) #Imprime: 6

#Comprobar si un caracter es minúscula o mayúscula
if nombre.islower()
if nombre.isupper()

#Operadores matemáticos:
1. Potencia: ** (3**2 = 9)
2. MOD: % (6 % 2 = 0)
3. a = a + 6 --> a += 6
4. a = a - 6 --> a -= 6
5. a = a * 6 --> a *= 6
6. a = a / 6 --> a /= 6 #En la división tenemos que tener en cuenta el 'dtype ='. No puede ser float. Debemos quitarlo de la linea del array

#Orden matemático de las operaciones:
1. Contenido de los paréntesis
2. Exponentes
3. Multiplicación y división
4. Suma y resta

#Desempaquetar un string: El operador * delante del string desempaqueta la cadena en caracteres individuales.
numero = 12345

print(*numero) Imprime: 1 2 3 4 5

Para imprimirlo en distintas líneas 

#Parámetro sep='x'
print('G','F','G', sep='') Imprime: gfg
print('09','12','2016', sep='-') Imprime:09-12-2016 (puede ser un guion o .,:;)
print('pratik','geeksforgeeks', sep='@') Imprime: pratik@geeksforgeeks
print('G','F','G', sep='\n') Imprime: G F G (Con salto de línea)
print('G','F','G', sep='\t') Imprime: G F G (Con sangría)

#LISTAS
# pueden contener un solo tipo de elemento o varios
embarcaciones = ['bote','yate','velero','catamaran'] #Esto es una lista
print(embarcaciones) #Esto imprime una lista
print(embarcaciones[3]) #Esto imprime un string, por lo tanto se le pueden añadir funciones como .title()
print(embarcaciones[-1]) #Esto imprime el último elemento de la lista
embarcaciones[2] = 'lancha' #cambia el valor de la posición 2 en la lista. velero --> lancha

#MÉTODOS PARA AÑADIR O ELIMINAR ELEMENTOS DE UNA LISTA:
embarcaciones.append('moto') #la función .append añade un elemento al final de la lista 
embarcaciones.append(()) #doble paréntesis para añadir dos elementos a la vez 'TUPLA'
embarcaciones.insert(0,'velero') #la función .insert() añade un elemento en la lista en una posición específica
embarcaciones.pop(1) #la función .pop() elimina un elemento de la lista. Si no se le da ningún valor, elimina el último elemento.
barco_eliminado = embarcaciones.pop(1) #guarda el valor del elemento eliminado en la posición 1 en la lista --> yate
embarcaciones.remove() #la función .remove() elimina un elemento pero dandole como valor un string en vez de una posición/indice como a .pop()
del embarcaciones[1] #la keyword 'del' elimina cualqiuer tipo de elemento (str,int,float,etc) de forma permanente, no guarda el objeto
embarcaciones.sort() #la función .sort() es para ordenar los elementos de una lista. Si no se le da un valor ordena en orden alfabético o numérico
print(sorted(embarcaciones)) #la función sorted() ordena de manera temporal. Imprime la lista ordenada pero no guarda en otra variables el nuevo orden de los elementos
embarcaciones.count('moto') # devuelve el número de veces que aparece el elemento 'moto'
barcos_ordenados = sorted(embarcaciones) #guardamos en otra variable la lista ordenada, pero en la primera variable sigue el orden de creación
print(len(embarcaciones)) #la función len() nos imprime cuantos elementos tiene la lista

#Formas de acceder a una lista con un bucle 'for'
coches = ['audi','bmw','volvo','mercedes','toyota','renault','citroen']

for i in range(0,int(len(coches))):
    print(coches[i])
    
for coche in coches:
    print(coche) #La variable 'coche no está definidia previamente sino que dentro del bucle va cogiendo los valores de la lista

for i in range (0,len(coches)): 
   print(coches[i],precios[i]) #Imprime dos listas a la vez


#Romper un bucle cuando se cumpla una condicion específica
for coche in coches:
    print(coche)
    if coche == 'mercedes':
        break

#Listas numéricas
lista_numeros = list(range(1,11))
print(lista_numeros)

num_pares = list(range(2,21,2)) #Al igual que en el 'for' aquí también podemos decirle: De 2 a 20 Con Paso 2
print(*num_pares)

#Rellenar lista vacía con un bucle
numeros_cuadrados = []

for valor in range(1,11): #Esto de puede comprimir en una linea
    cuadrado = valor**2
    numeros_cuadrados.append(cuadrado)

numeros_cuadrados = [valor**2 for i in range(1,11)] #Ambos imprimen: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

digitos = [1,2,3,4,5,6,7,8,9,0]

min(digitos) = 0
max(digitos) = 9
sum(digitos) = 45

#Trabajar solo con algunos dígitos de la lista
digitos = [1,2,3,4,5,6,7,8,9,0]

algunos_digitos = digitos[2:5]
print(algunos_digitos) #Imprime ['3','4','5']

#Índices negativos en listas
digitos = [1,2,3,4,5,6,7,8,9,0]

print(digitos[4:10]) #Imprime: [5, 6, 7, 8, 9, 0]
print(digitos[4:])   #Imprime: [5, 6, 7, 8, 9, 0]
print(digitos[-6:])  #Imprime: [5, 6, 7, 8, 9, 0]

#Recorrer una porción de un lista con un buble
digitos = [1,2,3,4,5,6,7,8,9,0]

for num in digitos[4:10]:
    print(num)

for i in range(4,len(digitos[0:10])):
    print(digitos[i])

#Crear una lista a partir de otra lista
mi_comida = ['pizza','carne','tarta de queso']

comida_invitado = mi_comida
comida_invitado.append('helado') #Este .append() afecta a ambas listas ya que ocupan el mismo espacio de memoria

comida_invitado = mi_comida[:] #Para evitar que pase lo anterior añadimos '[:]' y cada lista titne un espacio de memoria diferente

print(mi_comida) #Imprimen lo mismo
print(comida_invitado) #Imprimen lo mismo

#LISTAS ANIDADAS:
datos_alumnnos = [['David',25],['Damian',25],['Nayra',28]]

print(type(datos_alumnnos)) #Imprime -class list-
print(datos_alumnnos[1][0]) #Imprime Damian --> [1] elemento 1 de la lista 'datos_alumnos' --> [0] elemento 0 dentro de la lista [1] de la lista 'datos_alumnos'

print(datos_alumnnos[0:2]) #Imprime: ['David',25],['Damian',25]

#CONCATENAR LISTAS
lista1 = ['damian']
lista2 = ['arellano']
unir_listas = lista1 + lista2 #--> ['damian','arellano'] --> Concatena los elementos de dos listas en la nueva lista que hemos creado

lista1.extend(lista2) #-->el método .extend() añade los elementos de la lista2 al final de la lista 1, modificando el valor de la lista original
print(lista1) #-->Imprime: ['damian','arellano']

todas = [lista1,lista2]

#REDONDEAR DECIMALES
nota_media = 6.366666666666666
nota_media_redondeada = round(nota_media,2) #Redondea a dos decimales
print(nota_media_redondeada) #Imprime: 6.37

#-----ARRAYS-----

#Importar librerias 
import numpy as np
import random as rd
import string 

#RANDOM

#Inicializar variable con número aleatorio 
numero_aleatorio = rd.random() #Genera número aleatorio float entre 0.0 y 1.0
numero_aleatorio = rd.randint(1,100) #Genera número aleatorio entero entre 1 y 100
numero_aleatorio = rd.uniform(1,100) #Genera número aleatorio float entero entre 1 y 100
numero_aleatorio = rd.choice(lista1) #Selecciona un elemento al azar de una lista o secuencia de elementos

#STRING
minusculas = string.ascii_lowercase
mayusculas = string.ascii_uppercase
todas = string.ascii_letters
numeros = string.digits
caracteres_especiales = string.punctuation

#Combinar caracteres
caracteres = string.ascii_letters + string.digits + string.punctuation
combi = todas + numeros + caracteres_especiales #Es lo mismo

#NUMPY
np.array() #Para crear array - Ej: my_array = np.array(0,1,2,3,4,5) o my_array = np.array([2,3])
np.arange()  #Para crear array - Ej: my_array = np.arange(6) --> [0 1 2 3 4 5]
np.zeros((2,3)) #Crear array de 2 filas y 3 columnas inicializado con ceros
np.ones((2,3)) #Crear array de 2 filas y 3 columnas inicializado con unos
np.empty((2,3)) #Lo inicializa con valores random - NO ES LA MEJOR OPCIÓN

my_array = np.array([4,5], dtype = np.int8) #Le decimos que solo sea de 8 bits

my_array = np.array([4,5])
print(my_array.shape) # Imprime --> (4, 5)  

#Revertir un array
array = np.arange(8) #Imprime: [0,1,2,3,4,5,6,7]
revertido = np.flip(array) #Imprime: [7,6,5,4,3,2,1] (Si el array es de numpy)
revertido = array[::-1]

#Crear array con números aleatorios y longitud específica (NO NECESITAS IMPORTAR EL MÓDULO 'RANDOM')
array_aleatorio = np.random.randint(10, size=(5)) #Si solo damos un valor al principio, cuenta de 0 a ese valor. EJ: 0 a 10, y longitud 5

#Crear arrays unidad
eye_array = np.eye(3) #Imprime [[1. 0. 0.]
                              # [0. 1. 0.]
                              # [0. 0. 1.]]

eye_array = np.eye(3, k=-1) #Imprime [[0. 0. 0.]
                                   # [1. 0. 0.]
                                   # [0. 1. 0.]]

eye_array = np.eye(3, k=1) #Imprime [[0. 1. 0.]
                                   # [0. 0. 1.]
                                   # [0. 0. 0.]]

#Crear array con lista
lista =  [1,2,3,4,5,]
lista2 = [6,7,8,9,0]

my_array = np.array(lista) #Array unidimensional. Imprime --> [1 2 3 4 5]
my_array = np.array([lista,lista2]) #Array bidimensional. Imprime --> [[1 2 3 4 5]
                                    #                                  [6 7 8 9 0]]

#Cambiar valores de array
eye_array[eye_array == 0] = 5 #En el array 'eye_array' donde el valor sea 0 cámbialo por 5
eye_array[2:, :3] = 5 #En el corchete podemos seleccionar que posiciones queremos cambiar, al igual que hacíamos con las listas
eye_array2 = eye_array[:] #Duplico el array con un espacio nuevo de memoria por lo que los cambios en array_eye no afectan a array_eye2
sorted_array = np.sort(eye_array) #Va fila por fila ordenando de menor a mayor los valores (axis = -1 no es necesario ponerlo)
sorted_array = np.sort(eye_array, axis=0) #Va columna por columna ordenando de menor a mayor los valores

#Duplicar o copiar arrays
eye_array2 = eye_array.view() #con .view() se duplica el array y todos los cambios que agamos en el array original afectarán a la copia también
eye_array2 = eye_array.copy() #con .copy() se crea un array independiente y no afectan los cambios de uno a otro

#Cambiar la forma de un array
my_array = np.array([[1,2,3],[4,5,6]]) #Imprime --> [[1 2 3] --> my_array.shape = (2,3)
                                       #             [4 5 6]]

array2 = my_array.reshape(3,2) #Imprimie --> [[1 2]  --> array2.shape = (3,2)
                               #              [3 4]
                               #              [5 6]]

#Sumar elementos de un array
my_array = np.arange(1,10) #Imprime --> [1 2 3 4 5 6 7 8 9]
suma_array = my_array.sum()
print(suma_array) #Imprime --> 45

suma_total = my_array.sum() #Suma todos los elementos
suma_columnas = my_array.sum(0) #Suma las columnas
suma_filas = my_array.sum(1) #Suma las filas

#Multiplicar elementos de un array
my_array = np.arange(1,10) #Imprime --> [1 2 3 4 5 6 7 8 9]
multi_array = my_array.prod()
print(multi_array) #Imprime --> 362880

multi_total = my_array.prod() #Multiplica todos los elementos
multi_columnas = my_array.prod(0) #Multiplica las columnas
multi_filas = my_array.prod(1) #Multiplica las filas

#Mínimo, máximo, media, mediana y desviacion en arrays (Se pueden esribir: array.mean() o np.mean(array))
my_array.mean() #Imprime --> El valor medio del array
my_array.min() #Imprime --> El valor mínimo del array
my_array.max() #Imprime --> El valor máximo del array
np.median(my_array) #Imprime --> La mediana del array
np.std(my_array) #Imprime --> La desviación standard
np.mean(my_array)

my_array.argmin() #Imprime la posicion del elemento mínimo --> (0)
my_array.argmax() #Imprime la posicion del elemento mínimo --> (8)

#Aplanar un array
#1
my_array = np.arange(1,10).reshape(3,3)
array_plano = my_array.reshape(my_array.size) #Imprime --> [1 2 3 4 5 6 7 8 9]

#2
my_array = np.arange(1,10).reshape(3,3)
array_plano = my_array.flatten() #Imprime --> [1 2 3 4 5 6 7 8 9] - Pasa como con .copy() crea una copia independiente

#3
my_array = np.arange(1,10).reshape(3,3)
array_plano = my_array.ravel() #Imprime --> [1 2 3 4 5 6 7 8 9] - Pasa como con .view() crea una copia pero los cambios afectan a ambos

#Transposicionar un array
my_array = np.arange(1,10).reshape(3,3)

#1
my_transp = np.swapaxes(my_array, 0, 1) #Imprime --> [[1 4 7]
                                        #             [2 5 8]
                                        #             [3 6 9]]
#2
my_transp = my_array.transpose(1,0)     #Imprime --> [[1 4 7]
                                        #             [2 5 8]
                                        #             [3 6 9]]
#Operaciones con matrices
my_array = np.arange(1,10).reshape(3,3)
my_array2 = np.arange(1,10).reshape(3,3)

resultado = my_array + my_array2 #Estas operaciones suman, restan, multiplican o dividen elemento por elemento
resultado = my_array - my_array2
resultado = my_array * my_array2
resultado = my_array / my_array2

resultado = np.add(my_array,my_array2) #Suma los dos arrays elemento por elemento pero en forma de función
resultado = np.subtract(my_array,my_array2) #Resta los dos arrays elemento por elemento pero en forma de función
resultado = np.multiply(my_array,my_array2) #Multiplica los dos arrays elemento por elemento pero en forma de función

#Floor division
arr = np.array([2010, 1995, 1875, 1987])
flor_division = arr // 10 #Esto quita los decimáles si los hubiese. Imprime --> [201 199 187 198]
flor_division = arr // 10 * 10 #Si además lo multiplicamos por 10, le añadimos un 0 y tenemos la década. Imprime--> [2010 1990 1870 1980]

#Muliplicacion de matriz completa
matrix_multi = np.matmul(my_array, my_array2) #Los tres métodos devuelven el mismo resultado
matrix_multi = my_array.dot(my_array2)
matrix_multi = my_array @ my_array2

#Comparar elementos de dos arrays y sacar comunes
comunes1 = np.intersect1d(my_array,my_array2) #Almacena en 'comunes1' los elementos que se repiten en los dos arrays

#Concatenar arrays
#Tienen que tener la misma dimensión, aunque no es obligatorio en el eje en el que se va a concatenar

arrayConcatenado = np.concatenate((my_array,my_array2), axis=0) #axis = 0 concatena horizontalmente, axis = 1 verticalmente
arrayConcatenado = np.hstack(my_array,my_array2) #Concatena horizontalmente
arrayConcatenado = np.vstack(my_array,my_array2) #Concatena verticalmente

#Filtrar datos
array_numeros = np.array([1,0,5,3,8,0,0,5,6])
np.count_nonzero(array_numeros) #Cuenta los elementos del array distintos de 0 #Imprime--> 6
np.unique(array_numeros) #Devuelve los elementos únicos de un array #Imprime--> 0,1,3,5,6,8
np.unique(array_numeros, return_counts=True) #El 'return_counts=True' te devuelve cuantas veces se repite cada elemento
array_indices = np.array([3,7,4,9,1,6,5]) 
np.argsort(array_indices) #Devuelve los índices de los elementos después de ser ordenados Imprime--> 4,0,2,6,5,1,3 


#Manejar archivos con numpy

# --Lectura:

# Leer datos de un archivo csv
data = np.loadtxt('datos.csv', delimiter=',')

# Leer archivos de un archivo de texto
data = np.loadtxt('datos.txt')

# Leer datos de un archivo con encabezados
data = np.genfromtxt('datos.csv', delimiter=',', skip_header=1)

# --Escritura:

# Crear datos de ejemplo
data = np.array([[1,2,3],[4,5,6],[7,8,9]])

# Guardar datos en un archivo CSV
np.savetxt('datos.csv', data, delimiter=',')

#Guardar datos en un archivo de texto
np.savetxt('datos.txt', data)

#Guardar datos en un archivo con encabezados
header = 'Columna1, Columna2, Columna3'

np.savetxt('datos.csv', data, delimiter=',', header=header, comments='')


#TUPLAS

#son inmutables y más rápidas
mi_tupla = (1,2,3,4,5,True,'Hola') #Va entre paréntesis
subtupla = mi_tupla[0:5] #Imprime: 1,2,3,4,5
mi_lista = [1,2,3,4,5]
tupla_a_lista = tuple(mi_lista)
lista_a_tupla = list(mi_tupla)

#funciones comunes a las listas
mi_tupla.count(5) #Numero de veces que aparece el 5
mi_tupla.index(5) #Índice del elemento cuyo valor es 5. Imprime: 4
minimo = min(mi_tupla) #Si la tupla es de arrays y añadimos 'key=len' imprime el string más corto
minimo = max(mi_tupla) #Si la tupla es de arrays y añadimos 'key=len' imprime el string más largo
tupla_ordenada = sorted(mi_tupla) #IMPORTANTE: Me la devuelve en formato 'LISTA'
tupla_ordenada = tuple(sorted(mi_tupla)) #Forma correcta: me devuelve una 'TUPLA'
tupla_invertida = tuple(reversed(mi_tupla)) #Forma correcta: me devuelve una 'TUPLA' 

#Combinar tuplas
mi_tupla2 = ('a','b','c','d','e')
tupla_combinada1 = subtupla + mi_tupla2 #Imprime: ('a','b','c','d','e', 1, 2, 3, 4, 5)
tupla_combinada2 = tuple(zip(subtupla,mi_tupla2)) #Imprime: ((1,'a'),(2,'b'),(3,'c'),()..)
print(tupla_combinada2[3][1]) #Acceder a elementos de una tupla de tuplas, Imprime: d

#Slicing de tupla de tuplas
tupla_tuplas = ((1,2,3),(4,5,6),(7,8,9))
tupla_tuplas[1] #Imprime: (4,5,6)
tupla_tuplas[0:2] #Imprime: (1,2,3),(4,5,6)
tupla_tuplas[1][1:3] #Imprime: 5,6

#Peculiaridades de las tuplas
tupla_unitaria = (1,) #Si no añadimos la coma, print(type(tupla_unitaria)) imprime 'class int'
tupla1 = ('Hola',5,True) #Empaquetado
string, entero, booleano = tupla1 #Desempaquetado. print(string): 'Hola', print(entero): 5, print(booleano): True
lista_tuplas = [('Dami'),('are'),('rodguz')]

for name,surname,surname2 in lista_tuplas: #Desempaquetado y bucle en misma linea
    print(name,surname,surname2) #Imprime: Dami are rodguz

#SETs
#elementos no ordenados, únicos e inmutables, 
mi_set = set{} #set vacío. IMPORTANTE: poner 'set'. mi_set = {} es un diccionario.
mi_set = {'manzana','pera','platano','pera'} #Imprime: 'manzana','pera','platano'. No puede haber elementos repetidos.
print('manzana' in mi_set) #Imprime: True. Mucho más eficientes que las listas para comprobar pertenencia

#añadir o borrar elementos en sets
mi_set.add('naranja')
mi_set.remove('pera') #Si no existe el elemento 'pera', .remove() da error
mi_set.discard('pera') #A este le da exactamente igual que no exista

#pasar de listas a sets y viceversa
nums = [1,2,3,4,5]
nums_set = {1,2,3,4,5}
lista_a_set = set(nums) #print(type(lista_a_set)) imprime: 'class set'
set_a_lista = list(nums_set) #print(type(set_a_lista)) imprime: 'class list'

#Métodos o funciones específicos de sets:
#Unir sets
set1 = {1,2,3}
set2 = {3,4,5}
set_unidos = set1 | set2 #ambos imprimen: {1,2,3,4,5}
set_unidos = set1.union(set2) #ambos imprimen: {1,2,3,4,5}

#Intesección en sets (elemento en el que son comunes, interseccionan)
intersección = set1 & set2 #ambos imprimen: {3}
intersección = set1.intersection(set2) #ambos imprimen: {3}

#Diferencia de sets. Quita de un set los elementos comunes con el otro set
diferencia = set1 - set2 #Imprime: {1,2}
diferencia = set2 - set1 #Imprime: {4,5}
diferencia = set1.difference(set2)

#Diferencia simetrica de sets. Quita los elementos que interseccionan, que son comunes
dif_simetrica = set1 ^ set2 #Imprime: {1,2,4,5}
dif_simetrica = set2 ^ set1 #Imprime: {1,2,4,5}
dif_simetrica = set1.symmetric_difference(set2)

#DICCIONARIOS
datos_persona = {
#    key      value
    'edad':   23,
    'nombre': 'damian',
    'DNI':    '5434543443D',
    }

#Sintaxis básica:
edad = datos_persona['edad'] #Imprime: 23
datos_persona['localidad'] = 'madrid'

#Métodos principales para diccionarios
.keys() #Devuelve una lista de todas las claves del diccionario
.values() #Devuelve una lista de todos los valores del diccionario
.items() #Devuelve una lista de todos los pares del diccionario
.get('clave') #Accede al valor de una clave. Si la clave no exite devuelve el valor predeterminado 'None'
.get('clave',0) #Si la clave no exite devuelve 0
.pop('clave') #Elimina la clave y valor seleccionados y los almacena en la variable 'valor'
.clear() = #Vacía el diccionario

#Pasar de tuplas a diccionarios
mis_tuplas = [('key1', 1), ('key2', 2),('key3', 3), ('key4', 4)]
mi_diccionario = dict(mis_tuplas)
print(mi_diccionario) #Imprime:{'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4}

#Pasar de listas a diccionarios
lista_keys = ['key1','key2','key3','key4']
lista_values = [1,2,3,4]
combi = dict(zip(lista_keys,lista_values))
print(combi) #Imprime:{'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4}

#Pasar de sets a diccionarios
set_tuplas = {('key1',1),('key2',2),('key3',3),('key4',4),}
dict_set = dict(set_tuplas) #Imprime:{'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4}

#Recorrer diccionarios con bucles
programadores = {
    'damian': 'python',
    'jorge': 'flutter',
    'isma': 'ionic',
    'paul': 'python',
}

for nombre, lenguaje in programadores.items():
    print(nombre,lenguaje) #Imprime: todo

for nombre in programadores: #.keys() está por defecto
    print(nombre) #Imprime: damian, jorge, isma, paul

for lenguaje in programadores.values(): #puedo usar .sorted() para ordenar
    print(lenguaje) #Imprime: python, flutter, ionic, python

for lenguaje in set(programadores.values): #set() elimina los repetidos
    print(lenguaje) #Imprime: python, flutter, ionic

#Anidar diccionarios en listas
usuario_0 = {
    'nombre': 'damian',
    'lenguaje': 'python',
    'edad': '26',
    'exp': '1',
}
usuario_1 = {
    'nombre': 'toni',
    'lenguaje': 'java',
    'edad': '30',
    'exp': '3',
}
usuario_2 = {
    'nombre': 'javi',
    'lenguaje': 'aws',
    'edad': '24',
    'exp': '4',
}

usuarios = [usuario_0,usuario_1,usuario_2] #Se anida en una lista
leng_user2 = usuarios[1]['nombre']
print(leng_user2)

#Anidar listas en diccionarios
programadores = {
    'damian': ['python','terminal'], #Cada valor es una lista que se puede recorrer
    'jorge': ['javascript','flutter'],
    'isma': ['ionic', 'java'],
}

for nombre, lenguajes in programadores.items():
    print('El programador',nombre.title(),'conoce los lenguajes:')
    for lenguaje in lenguajes:
        print(lenguaje.title())

#Anidar diccionarios en diccionarios
users = {
    'dartik': {
        'nombre': 'dani',
        'apellido': 'cobo',
        'localizacion': 'esp',
    },
    'pepitogr': {
        'nombre': 'pepe',
        'apellido': 'grillo',
        'localizacion': 'usa',
    }
}
for user, user_info in users.items():
    print('Datos del usuario', user.title(),':')
    nombre_completo = user_info['nombre'] + ' ' + user_info['apellido']
    localizacion = user_info['localizacion']
    print(nombre_completo.title())
    print(localizacion.title())

#Navegación en diccionarios
registros = {'Juan': 15, 'Manuel':20}
jugador_alto = max(registros, key=registros.get)
print(jugador_alto) #Imprime: la key con el value más alto (Manuel)

#FUNCIONES

#Argumentos posicionales y de palabra clave
def nombre_funcion(nombre,numero,edad=26): #Parametros posicionales primero, después de clave
    print(nombre) #Imprime: damian
    print(numero) #Imprime: 54
    print(edad) #Imprime: 26

nombre_funcion('damian',54)

#Argumentos arbitrarios y retorno
def hacer_pizza(dimension,*ingredientes): #Al tener el * puede recibir varios parámetros (tupla)
    print(dimension,'cm',ingredientes) # Imprime: 12cm ('queso,'tomate','oregano')

hacer_pizza(12,'queso','tomate','oregano')

def construir_perfil(nombre,apellido,**info_usuario): #Al tener los ** espera pares 'clave':valor (dict)
    perfil = {}
    perfil['nombre'] = nombre
    perfil['apellido'] = apellido
    
    for clave, valor in info_usuario.items():
        perfil[clave] = valor

    return perfil #Devuelve el diccionario en una variable

nuevo_perfil = construir_perfil('damian','arellano',profesion = 'dev',salario=50000) #Alamacena el valor que devuelve 'return perfil'

#Importar funciones
import funcion as fc #Igual que con numpy

import modulo_una_funcion #Si el módulo solo tiene una funcion

modulo_una_funcion.funcion() #Primero indicamos qué módulo es

from modulo_varias_funciones import * #Importa todas las funciones del módulo

from modulo_varias_funciones import funcion #Si el módulo tiene varias funciones pero solo queremos una

funcion() #Directamente llamamos a la funcion

funcion(variable[:]) #Le doy una copia a la funcion, la variable original sigue intacta

# ----FUNCIONES LAMBDA----

# -- Nombres --
#PYTHON: Funciones Lambda
#Otros lenguajes: Funciones on demand, on the go, online...

#Sintaxis función normal
def area_triangulo(base,altura):
    return (base*altura/2)

#Sintaxis lambda
#   nombre funcion     parámetros      return    --> el return es ':'
area_triangulo=lambda base,altura: (base*altura/2)

#No pueden tener bucles o condicionales. Solo devuelve un cálculo.

# -- Formateo --
comisiones_empleados=lambda comision: "¡{}€!".format(comision)
comision_luis = comisiones_empleados(765) #Print: ¡765€!

# -- Filtrado --
#Función normal
def numero_par(num):
    if num % 2 == 0:
        return True

numeros=[2,3,4,7,9,10,12,3,15,17,22,21]
#    lista-función-condicion-en números 
print(list(filter(numero_par,numeros))) #Función filter de python

#Función lambda
numeros=[2,3,4,7,9,10,12,3,15,17,22,21]
print(list(filter(lambda numero_par:numero_par%2==0, numeros)))


# ----MANIPULACIÓN DE ARCHIVOS----

# Abrir archivo en modo lectura
file_name = '/home/damianar/Downloads/datos.txt'

with open(file_name) as archivo_objeto: #Dentro del archivo se puede iterar de distintas maneras
    contenido = archivo_objeto.read()
    lineas = archivo_objeto.readlines()
    for linea in archivo_objeto:
        print(linea)
    print(contenido)
    print(lineas)


# Modos de open
open(file_name, "w") #Sobreescribe el texto existente, si no existe el archivo lo crea
open(file_name, "a") #Añade texto al final del texto existente
open(file_name, "x") #Abre el archivo para escritura, pero falla si ya existe


# Sintaxis comprimida
with open(file_name) as archivo_objeto:
    contenido = archivo_objeto.read()

f = open(file_name,"w")
f.write('contenido en forma de string')
