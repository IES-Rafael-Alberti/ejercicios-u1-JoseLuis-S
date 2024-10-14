'''
Ej 1.2 funciones

Este algoritmo saluda a la persona de la que escribas el nombre

Funciones disponibles:
    * saludo - recibe un nombre y devuelve una cadena de texto que saluda al usuario
    * main - funcion main
'''

def saludo(nom: str) -> str:
    ''' Recibe un nombre y devuelve un saludo

    Args:
        nom (str): Nombre la persona a saludar

    Returns: 
        str: Saludo con el nombre introducido en formato tittle
    '''
    return 'Hola, ' + nom.title() + '.'

def main():
    ''''Funcion main'''
    nom = input('Introduce tu nombre: ')
    print(saludo(nom))

if __name__ == '__main__':
    main()