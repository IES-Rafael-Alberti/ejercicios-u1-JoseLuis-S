'''

Ej 1 funciones

Este algoritmo saluda al nombre que el usuario introduce

Funciones disponibles:
    * nombre - recibe un str y lo devuelve en formato tittle
    * main - funcion main
'''

def nombre (nom: str) -> str:
    ''' Recibe un nombre y lo devuelve en formato tittle

    Args:
        nom (str): Nombre de la persona a saludar
    Returns:
        str: Nombre de la persona a saludar en formato tittle

    '''
    return nom.tittle

def main():
    ''''Funcion main'''
    nom = input('Introduce tu nombre: ')
    print('Hola,', nombre())

if __name__ == '__main__':
    main()