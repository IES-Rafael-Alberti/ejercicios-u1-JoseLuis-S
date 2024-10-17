'''
Ej 5 funciones

Este algoritmo calcula el precio final de un producto añadiendole el IVA

Funciones disponibles:
    * calculoPrecio - calcula el precio de un producto con el IVA
    * main - funcion main
'''

def calculoPrecio():
    ''' Lee un precio y una cantidad de IVA y calcula el precio con el 
    % de IVA    
    '''
    precio = float(input('Introduce el precio del artículo: '))
    iva = 0
    while (iva > 1 or iva <= 0):
        iva = float(input('Introduce la cantidad de IVA en decimal (21% = 0.21): '))
    precioFinal = precio * (iva + 1)
    precioFinal = round(precioFinal, 2)
    print(f'El precio del articulo es: {precioFinal}')

def main():
    '''Funcion main'''
    calculoPrecio()

# Llama a la funcion main
if __name__ == '__main__':
    main()