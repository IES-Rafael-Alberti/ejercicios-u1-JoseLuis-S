'''
Ej 11 funciones 

Este algoritmo calcula la suma de todos los enteros hasta el numero introducido

Funciones disponibles:
    * sumNum - calcula la suma de todos los enteros hasta el numero introducido
    * main - funcion main
'''

def sumNum (num: int) -> int:
    ''' Calcula la suma de todos los enteros hasta el numero introducido
    
    Returns:
        int: La suma de todos los enteros hasta el numero introducido
    '''
    return int((num*(num + 1))/2)

def main():
    '''Funcion main'''
    n = int(input('Introduce un numero entero: '))
    print('La suma de todos los enteros desde 1 hasta {} es {}'.format(n, sumNum(n)))

if __name__ == '__main__':
    main()

