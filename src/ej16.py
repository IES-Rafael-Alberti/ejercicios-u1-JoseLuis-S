panVendido = int(input('Introduce el numero de barras que no son del dia vendidas: '))

PRECIO_PAN = 3.49
descuentoPan = 0.60 * PRECIO_PAN
descuentoPan = round(descuentoPan, 2)
costeFinal = PRECIO_PAN * descuentoPan
costeFinal = round(costeFinal, 2)

print('El precio de una barra normal es de: ' + str(PRECIO_PAN) + '€')
print('El descuento es de: ' + str(descuentoPan) + '€')
print('El total por las barras con descuento vendidas es de: ' + str(costeFinal) + '€')