#Pedir un número entero por pantalla
numeroUsuario = int(input('Introduce un número entero: '))


#Devolver la estructura de asteríscos
# for i in range(0,numeroUsuario):
#      print(asterisco)
#      asterisco = asterisco + '*'


for i in range(1,numeroUsuario + 1):
    print('*' * i)
for i in range(numeroUsuario-1,0,-1):
    print('*' * i)