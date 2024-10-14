'''
Este algoritmo calcula el precio final de un producto añadiendole el IVA
'''

def calcula_precio(importe: float, iva: float):
    return round(importe + importe * (iva/100), 2)