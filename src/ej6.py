'''
Ej 6

Este algoritmo calcula la cantidad de IVA que se ha pagado por un producto

'''

# Entrada del precio con IVA
precioInicial = float(input('Introduce el precio con IVA: '))

# Calculo del precio sin IVA
precioFinal = precioInicial * 0.9 

# Calculo de la cantida de IVA
iva = precioInicial - precioFinal

# Redondea a dos decimales 
precioFinal = round(precioFinal, 2)
precioInicial = round(precioInicial, 2)
iva = round(iva, 2)

# Muestra los resultados
print('El precio sin IVA es: {precioFinal} ') 
print('Se ha pagado de IVA: {iva}')