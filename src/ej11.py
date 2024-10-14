'''
Este algoritmo calcula la suma de todos los enteros hasta el numero introducido
'''

# Lee el numero para la serie
n = int(input('Introduce un numero entero: '))

# Calcula la suma de todos los enteros desde 1 hasta n
resultado = int((n*(n + 1))/2)

# Muestra el resultado por pantalla
print(f'La suma de todos los enteros desde 1 hasta {n} es {resultado}')
