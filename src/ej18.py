'''
Ej 18

Este algoritmo muestra un nombre escrito en minusculas, mayusculas y en formato
tittle
 
'''

# Lee el nombre a escribir
nombre = input('Introduce tu nombre: ')

# Escribe el nombre en minuscula
print(nombre.lower())
# Escribe el nombre en mayuscula
print(nombre.upper())
# Escribe el nombre con la primera letra en mayuscula y el resto en minusculas
print(nombre.title())