'''
Ej 2 funciones

Este algoritmo calcula el precio total por las horas trabajadas

Funciones disponibles:
    * pagoTotal - calcula el pago total por las horas trabajadas
    * main - funcion main

'''

def pagoTotal (horas: float, precioHora: float) -> float:
    ''' Recibe las horas y el precio por hora y devuelve el pago total

    Args:
        horas (float): Numero de horas trabajadas
        precioHora (float): Precio por hora trabajada

    Returns:
        float: Pago total por horas
    '''
    return horas * precioHora

def main():
    '''Funcion main'''
    horas = float(input('Introduce las horas trabajadas: '))
    precioHora = float(input('Introduce el precio por hora: '))
    print('El total es', pagoTotal(horas, precioHora),'euros.')

# Llama la funcion main
if __name__ == '__main__':
    main()