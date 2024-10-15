'''
Ej 32

Este algoritmo genera la serie Fibonacci hasta el numero que introduzca

Funciones disponibles:
    * serieFibonacci - genera la serie fibonacci hasta el numero introducido
    * pedirNum - pide un numero entero al usuario
    * comprobarNum - comprueba si el numero introducido es un numero entero
    * main - funcion main

'''

def serieFibonacci(num: int) -> list:
    ''' Genera la serie Fibonacci hasta un numero introducido

    Args:
        num (int): Numero introducido para generar la serie

    Returns:
        list: La serie Fibonacci hasta el numero introducido
    
    '''
    # Crea una lista llamada serie, con los dos primeros valores de la serie, en
    # la que se iran guardando cada uno de los valores consiguientes
    serie = [0, 1]
    # Mientras la suma de los dos ultimos numeros de la lista sea menor o igual al
    # numero introducido, se sumaran esos valores y se añadira el resultado de la
    # operacion a la lista
    while serie[-1] + serie[-2] <= num: 
        serie.append(serie[-1] + serie[-2])  
    return serie  

def pedirNum():
    ''' Pide un numero entero al usuario

    Returns: 
        int: Devuelve un numero entero introducido por el usuario 
    
    '''
    # Lee el numero
    num = input('Introduce el numero hasta el que generar la serie Fibonacci: ')
    # Llama a la funcion comprobar para asegurar que el valor introducido
    # sea un numero
    while not comprobarNum(num):
        num = input('ERROR, introduce un numero: ')
    return int(num)

def comprobarNum(num: str):
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
    serie = serieFibonacci(num)
    print(f'La serie Fibonacci hasta el numero {num} es: {serie}')

if __name__ == '__main__':
    main()
