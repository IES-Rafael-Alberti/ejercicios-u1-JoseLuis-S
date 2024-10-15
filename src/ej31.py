'''
Ej 31

Este algoritmo muestra todos los divisores que tiene un numero entero

Funciones disponibles:
    * divisoresNum - calcula todos los divisores de un numero entero
    * pedirNum - pide un numero entero al usuario
    * comprobarNum - comprueba que el numero introducido sea un numero entero
    * main - funcion main

'''

def divisoresNum(num: int) -> list:
    ''' Calcula los divisores de un numero 

    Args:
        num (int): Numero para el que comprobar los divisores

    Returns:
        list: Lista con los divisores del numero

    '''
    # Crea una lista para guardar los divisores del numero introducido
    divisores = []
    # Comprueba desde 1 hasta el mismo numero los divisores y los va guardando
    # en la lista divisores
    for i in range (1, num + 1):
        division = num % i 
        if division == 0:
            divisores.append(i)
    return divisores

def pedirNum() -> int:
    ''' Pide un numero entero al usuario

    Returns: 
        int: Devuelve un numero entero introducido por el usuario 
    
    '''
    num = input('Introduce un numero entero para saber sus divisores: ')
    # Llama a la funcion comprobar para asegurar que el valor introducido
    # sea un numero
    while not comprobarNum(num):
        num = input('ERROR, introduce un numero entero: ')
    return int(num)

def comprobarNum(num: str) -> bool:
    ''' Comprueba que el numero introducido sea un numero entero
    
    Args:
        num (str): Numero introducido por el usuari
    
    Returns:
        bool: Retorna True si es un numero entero y False si no lo es
        
    '''
    # Elimina los espacios tras convertir num en str
    num = num.strip()

    # Comprueba con un for que los el valor introducido sea un numero entero
    for i in num:
        if i not in '0123456789.-':
            return False 
    
    return True

def main():
    '''Funcion main'''
    num = pedirNum()
    divisores = divisoresNum(num)
    print(f'Los divisores de {num} son: {divisores}')

if __name__ == '__main__':
    main()