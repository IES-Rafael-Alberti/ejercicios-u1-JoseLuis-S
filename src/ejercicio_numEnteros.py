def comprobarInt (cadena: str):
    cadena = cadena.strip()
    return cadena.isdigit() or (cadena.startswith('-') and cadena[1:].isdigit())

def dameInt():
        cadena = input('Dame un numero entero: ')
        while comprobarInt(cadena) == False:
            cadena = input('ERROR\n, introduce un entero: ')
        return cadena

# Define main 
def main ():
    num = dameInt()
    print('Escribiste el numero:', num)

# LLama a la funcion main
if __name__ == '__main__':
    main()
