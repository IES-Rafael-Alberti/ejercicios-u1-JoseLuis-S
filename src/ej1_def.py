# Define la funcion saludo
def saludo(nom):
    return 'Hola, ' + nom + '.'

# Define main, lee nombre y llama a la funcion saludo
def main():
    nombre = input('Introduce tu nombre: ')
    print(saludo(nombre))

# Llama la funcion main
if __name__ == '__main__':
    main()