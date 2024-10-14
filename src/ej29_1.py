'''
Ej 29_1 

Este algoritmo genera un numero aleatorio entre 2 numeros

Funciones disponibles:
    * resultado - muestra el numero random entre los 2 numeros
    * comprobarNum - comprueba que el numero introducido sea un numero
    * pedirNum1 - pide el primer numero
    * pedirNum2 - pide el segundo numero
    * compararNums - compara ambos numeros
    * numeroRandom - genera un numero random entre los 2 numeros
    * main - funcion main
'''
import random

def resultado(comparacion: bool, num1: float, num2: float, num3: float):
    ''' Compara los dos numeros y en funcion de cual sea mayor muestra
    un resultado u otro

    Args:
        comparacion (bool): Decide cual de los dos numeros es mayor
        num1 = Primer numero
        num2 = Segundo numero
        num3 = Variable temporal
    '''
    if comparacion == False:
        print('Un numero aleatorio entre', num1 ,'y', num2, 'es', numeroRandom(num1, num2))
    else:
        num3 = num1
        num1 = num2
        num2 = num3
        print('Un numero aleatorio entre', num1 ,'y', num2, 'es', numeroRandom(num1, num2))

def comprobarNum(num: str) -> bool:
    '''Comprueba que el numero introduce sea un numero
    
    Args: 
        num (str): Numero que introduce el usuario

    Returns: 
        bool: Retorna True si es un numero y False si no lo es 
    '''
    # Elimina los espacios tras convertir num en str
    num = num.strip()

    # Comprueba que el numero no contenga mas de un .- o que no contenga algun - en mitad
    # del numero
    if num.count('.') > 1 or num.count('-') > 1 or (num.count('-') == 1 and num[0] != '-'):
        return False

    # Comprueba con un for que los el valor introducido no contenga letras
    for i in num:
        if i not in '0123456789.-':
            return False 
    
    # Comprueba que no se haya dado el valor de un solo - o .
    if num == '-' or num == '.':
        return False

    return True

def pedirNum1():
    ''' Pide el primer numero

    Returns:
        float: Devuelve el primer numero
    '''
    num = input('Introduce el primer numero: ')
    # Llama a la funcion comprobar para asegurar que el valor introducido
    # sea un numero
    while not comprobarNum(num):
        num = input('ERROR, introduce un numero: ')
    return float(num)

def pedirNum2():
    ''' Pide el segundo numero

    Returns:
        float: Devuelve el segundo numero
    '''
    num = input('Introduce el segundo numero: ')
    # Llama a la funcion comprobar para asegurar que el valor introducido
    # sea un numero
    while not comprobarNum(num):
        num = input('ERROR, introduce un numero: ')
    return float(num)

def compararNums(num1: float, num2: float) -> bool:
    '''Compara los numeros introducidos

    Args: 
        num1 (float): Primer numero
        num2 (float): Segundo numero
    Returns:
        bool: Si el primer numero es mayor retorna True si no False
    '''
    if num1 > num2:
        return True
    else:
        return False

def numeroRandom(num1: float, num2: float) -> float:
    '''Genera un numero random entre los dos numeros
    
    Args:
        num1 (float): Primer numero
        num2 (float): Segundo numero
    Returns:
        float: Retorna un numero random entre dos numeros
    '''
    return random.uniform(num1, num2)

def main():
    '''Funcion main'''
    num1 = pedirNum1()
    num2 = pedirNum2()
    num3 = 0

    comparacion = compararNums(num1, num2)
    resultado(comparacion, num1, num2, num3)

if __name__ == '__main__':
    main()