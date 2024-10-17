'''
Ej 5

Este algoritmo calcula el precio final de un producto añadiendole el IVA

'''

# Entrada del precio
precio = float(input('Introduce el precio del artículo: '))

# Declaracion de variable
iva = 0

# Entrada del IVA 
while (iva > 1 or iva <= 0):
    iva = float(input('Introduce la cantidad de IVA en decimal (21% = 0.21): '))

# Calculo y redondeo del resultado
precioFinal = precio * (iva + 1)
precioFinal = round(precioFinal, 2)

# Muestra por pantalla el resultado
print(f'El precio del articulo es: {precioFinal}')



