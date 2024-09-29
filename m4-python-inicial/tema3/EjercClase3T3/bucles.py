#Pedir un número entero por pantalla
numeroUsuario = int(input('Introduce un número entero: '))
asteriscos = []

#Devolver la estructura de asteríscos
# for i in range(0,numeroUsuario):
#      print(asterisco)
#      asterisco = asterisco + '*'


for i in range(0,numeroUsuario):
     asteriscos.append('*')
     print(*asteriscos)
for i in range(1,numeroUsuario):
     asteriscos.pop()
     print(*asteriscos)