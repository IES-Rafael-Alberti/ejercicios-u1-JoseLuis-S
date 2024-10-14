'''
Este algoritmo pide un nombre al usuario y lo saluda
'''

# Funcion para leer nombre
def nombre (nom):
    return nom.tittle

# Define el main, lee las horas, el precio por hora y luego muestra la funcion por pantalla
def main():
    # Lee el nombre y saluda
    nom = input('Introduce tu nombre: ')
    print('Hola,', nombre())

# Llama la funcion main
if __name__ == '__main__':
    main()