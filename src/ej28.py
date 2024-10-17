'''
Ej 28 

Este algoritmo calcula la diferencia entre 2 numeros

'''

# Lee los dos numeros a comparar
num1 = int(input('Introduce el primer numero entero: '))
num2 = int(input('Introduce el segundo numero entero: '))

# Si los numeros a comparar son iguales muestra un mensaje de error
if (num1 == num2): 
    print('Los números no pueden ser iguales.')

# En caso de que num1 sea mayor que num2
if (num1 > num2):
    # Calcula la diferencia
    num3 = num1 - num2
    # Muestra el resultado en pantalla
    print(f'El numero {num2} es el menor y entre ellos existen {num3} numeros enteros.')

# En caso de que num2 sea mayor que num1
else:
    # Calcula la diferencia
    num3 = num2 - num1
    # Muestra el resultado en pantalla
    print(f'El numero {num1} es el menor y entre ellos existen {num3} numeros enteros.')
