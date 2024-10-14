'''

Ejercicio 28_1

Este algoritmo calcula el area de un triangulo, en m o cm, a partir de los 3 lados
de un triangulo

Funciones disponibles:
    * calcularArea - calcula el area de un triangulo dado sus 3 lados
    * comprobarNum - comprueba si el valor introducido es un numero
    * pedirLado - pide al usuario que introduzca los valores de los lados del triangulo
    * pedir_unidad_medida - pide al usuario que introduzca la unidad de medida
    * pedir_lados_triangulo - pide al usuario los tres lados del triángulo
    * main - funcion main

'''

import math

def calcularArea(ladoA: float, ladoB: float, ladoC: float) -> float: 
    '''Calcula el area de un triangulo usando una formula matematica

    Args:
        ladoA (float): Valor del primer lado
        ladoB (float): Valor del segundo lado
        ladoC (float): Valor del tercer lado

    Returns:
        area (float): Valor del area del triangulo
    '''
    semiperimetro = (ladoA + ladoB + ladoC)/2
    area = math.sqrt( semiperimetro * (semiperimetro - ladoA) * (semiperimetro - ladoB) * (semiperimetro - ladoC))
    return float(area)

def comprobarNum(num: str) -> bool:
    '''Comprueba que el numero introducido sea un numero y no un str

    Args:
        num (str): Valor del numero introducido

    Returns: 
        bool: Retorna True si es un numero o False en caso de que no
    '''
    num = num.strip()

    # Comprueba que el numero no tenga mas de 1 .- o que no tenga - en medio
    if num.count('.') > 1 or num.count('-') > 1 or (num.count('-') == 1 and num[0] != '-'):
        return False

    for i in num:
        if i not in '0123456789.-':
            return False 
    
    if num == '-' or num == '.':
        return False

    return True

def pedirLado(index: int) -> float:
    '''Pide los 3 lados del triangulo y ejecuta la funcion comprobarNum para asegurar
    que los valores introducidos sean numeros

    Args:
        index (str): Orden del numero introducido (lado1, lado2 o lado3)

    Returns:
        num (float): Valor del lado 

    '''
    # Muestra los mensajes en funcion del orden de los lados 1,2,3
    mensajes = ["Introduce el primer lado: ", "Introduce el segundo lado: ", "Introduce el tercer lado: "]
    num = input(mensajes[index - 1])
    while not comprobarNum(num):
        num = input('ERROR, introduce un numero: ')
    return float(num)

def pedir_unidad_medida() -> str:
    '''Pide la unidad de medida (cm o m) y comprueba que sea una de las dos posibles

    Returns:
        unidadMedida (str): El usuario elige entre cm o m
    '''
    unidadMedida = input('Introduce la unidad de medida (cm o m): ')

    while unidadMedida != 'cm' and unidadMedida != 'm':
        unidadMedida = input('ERROR, introduce la unidad de medida (cm o m): ')
    return unidadMedida

def pedir_lados_triangulo() -> float:
    '''Pide los tres lados del triangulo 
    
    Returns:
        ladoA (float): Valor del primer lado
        ladoB (float): Valor del segundo lado
        ladoC (float): Valor del tercer lado
    '''

    print('Dime los lados del triangulo: ')

    ladoA = pedirLado(1)
    
    ladoB = pedirLado(2)

    ladoC = pedirLado(3)    

    return float(ladoA), float(ladoB), float(ladoC)

def main():
    '''Funcion main'''

    unidadMedida = pedir_unidad_medida()

    ladoA, ladoB, ladoC = pedir_lados_triangulo()

    area = calcularArea(ladoA, ladoB, ladoC)

    if unidadMedida == 'cm':
        unidadMedida = 'cm²'
    else:
        unidadMedida = 'm²'

    print(f'El area del triangulo es igual a: {area} {unidadMedida}')

if __name__ == '__main__':
    main()