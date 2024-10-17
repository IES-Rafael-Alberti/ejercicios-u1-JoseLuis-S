# Define la funcion que comprueba si es un numero entero
def comprobarInt (cadena: str):
    cadena = cadena.strip()
    return cadena.isdigit() or (cadena.startswith('-') and cadena[1:].isdigit())

# Define la funcion para pedir un numero entero y llama a la 
# funcion comprobar para asegurar que se introduce un entero
def dameInt():
        cadena = input('Dame un numero entero: ')
        while comprobarInt(cadena) == False:
            cadena = input('ERROR\n Introduce un entero: ')
        return cadena

# Define main 
def main ():
    num = dameInt()
    print('Escribiste el numero:', num)

# LLama a la funcion main
if __name__ == '__main__':
    main()
