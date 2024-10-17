'''
Ej 2 

Este algoritmo calcula el precio total por las horas trabajadas

'''

# Entrada de horas
horas = float(input('Horas de trabajo: '))

# Entrada de coste
precioHora = float(input('Coste por hora: '))

# Calcula el coste * hora
importe = str(precioHora * horas)

# Muestra el resultado
print('Importe total: ' + importe)