'''
Este algoritmo muestra el precio de una barra de pan, ademas, calcula la cantidad descontada 
por barra y el total del descuento
'''

# Lee el numero de barras vendidas
panVendido = int(input('Introduce el numero de barras que no son del dia vendidas: '))

# Declara el precio del pan como una constante
PRECIO_PAN = 3.49
#Calcula el descuento y lo rendondea
descuentoPan = 0.60 * PRECIO_PAN
descuentoPan = round(descuentoPan, 2)
#Calcula el coste final y lo redondea
costeFinal = PRECIO_PAN * descuentoPan
costeFinal = round(costeFinal, 2)

# Imprime los resultados por pantalla
print(f'El precio de una barra normal es de: {PRECIO_PAN} €')
print(f'El descuento es de: {descuentoPan} €')
print(f'El total por las barras con descuento vendidas es de: {costeFinal} €')