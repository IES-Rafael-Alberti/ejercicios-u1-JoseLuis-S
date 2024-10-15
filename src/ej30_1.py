'''
Ej 30_1 

Este algoritmo comprueba si el numero introducido es un numero primo o no

Funciones disponibles:
    * comprobarPrimo - comprueba si un numero es primo o no
    * pedirNum - pide un numero al usuario
    * comprobarNum - comprueba que un valor introducido sea un numero entero
    * main - funcion main
'''

def comprobarPrimo(num: int) -> str:
    '''Comprueba si el numero introducido es un numero primo o no

    Args: 
        num (int): Numero a comprobar si es primo o no

    Returns:
        str: Devuelve un mensaje en funcion de si el numero es
        primo o no
    
    '''
    numDivisores = 0

    # Con este bucle for se calcula el numero de divisores,
    # comienza desde el 1 hasta 1 numero menos que el numero
    # introducido
    for i in range (1, num):
            # Si el modulo de la division es 0 se le suma un
            # divisor
            divisores = num % i
            if divisores == 0:
                numDivisores += 1

    # Si tiene mas de 1 divisor (ya que todos los numeros son divisibles
    # entre 1) no es un numero primo y viceversa
    if numDivisores > 1:
        return (f'El numero {num} no es un numero primo.')
    else:
        return (f'El numero {num} es un numero primo.')    

def pedirNum() -> int:
    ''' Pide un numero al usuario

    Returns:
        int: Devuelve el numero que introduce el usuario
    
    '''
    num = input('Introduce el numero entero a comprobar: ')
    # Llama a la funcion comprobar para asegurar que el valor introducido
    # sea un numero
    while not comprobarNum(num):
        num = input('ERROR, introduce un numero: ')
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
        if i not in '0123456789':
            return False 

    return True

def main():
    '''Funcion main'''
    num = pedirNum()
    comprobacion = comprobarPrimo(num)
    print(comprobacion)

if __name__ == '__main__':
    main()