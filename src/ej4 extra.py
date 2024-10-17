'''
Ej 4 extra

Este algoritmo convierte los grados Celsius en grados Fahrenheit

'''

# Entrada de grados Celsius
celsius = float(input('Introduce la temperatura en grados Celsius: '))

# Calculo a Fahrenheit
fahrenheit = (celsius * 9/5) + 32
fahrenheit = round(fahrenheit, 2)

# Muestra el resultado
print(f'La temperatura en grados Farenheit es {fahrenheit}ºF ({celsius}ºC)')

