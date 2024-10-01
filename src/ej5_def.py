# Funcion que pide el precio e IVA, luego calcula el precio final
def calculoPrecio():
    precio = float(input('Introduce el precio del artículo: '))
    iva = 0
    while (iva > 1 or iva <= 0):
        iva = float(input('Introduce la cantidad de IVA en decimal (21% = 0.21): '))
    precioFinal = precio * (iva + 1)
    precioFinal = round(precioFinal, 2)
    print(f'El precio del articulo es: {precioFinal}')

# Imprime la funcion por pantalla
calculoPrecio()