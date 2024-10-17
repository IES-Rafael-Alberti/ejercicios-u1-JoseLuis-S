'''
Ej 4 funciones 1

Este algoritmo convierte los grados Celsius en grados Fahrenheit

Funciones disponibles:
    * cambioCF - lee grados fahrenheit y los convierte en grados celsius
    * main - funcion main

'''

def cambioCF():
    ''' Lee una temperatura en grados fahrenheit, los convierte en grados celsius y muestra 
    la temperatura tanto en grados fahrenheit como celsius

    Returns:
        str: La temperatura en celsius y fahrenheit
    '''
    tempF = float(input('Introduce la temperatura en grados Fahrenheit: '))
    tempC = ((tempF - 32) * 5) /  9
    tempC = round(tempC, 2)
    tempF = round(tempF, 2)
    return 'La temperatura en celsius es {}°C ({})°F'.format(tempC, tempF)

def main():
    '''Funcion main'''
    print(cambioCF())

if __name__ == '__main__':
    main()
