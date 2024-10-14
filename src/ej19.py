'''
Este algoritmo calcula el numero de letras que tiene el nombre introducido
'''

# Lee el nombre
nombre = input('Introduce tu nombre: ')
# Lee el numero de letras del nombre
n = len(nombre)
# Pasa el nombre a mayusculas
nombre = nombre.upper()

# Muestra el resultado por pantalla
print(f'{nombre} tiene {n} letras.')