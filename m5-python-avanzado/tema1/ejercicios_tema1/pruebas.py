#FUNCIONES
def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args, **kwargs):
        print('Vamos a realizar el cálculo:')

        funcion_parametro(*args, **kwargs)

        print('Hemos terminado el cálculo')
    
    return (funcion_interior)


@funcion_decoradora
def suma(num1,num2,num3):
    print(num1+num2+num3)

@funcion_decoradora
def resta(num1,num2):
    print(num1-num2)

@funcion_decoradora
def potencia(base,exponente):
    print(base**exponente)

#CASO DE USO
suma(25,25,50)
print()
resta(300,200)
print()
potencia(2,4)


print('----')

autores = ['Isaac Asimov', 'Frank Herbert', 'Douglas Adams']
autores.sort(key=lambda name:name.split(' ')[-1])
print(autores)