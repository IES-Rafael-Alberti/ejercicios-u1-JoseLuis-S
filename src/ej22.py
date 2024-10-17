'''
Ej 22

Este algoritmo escribe la vocal introducida en mayusculas en una frase introducida previamente 

'''

# Lee la frase
frase = input("Introduce una frase: ")

# Lee la vocal
vocal = input("Introduce una vocal: ").lower()

# Verifica que lo introducido sea una vocal
if vocal in "aeiou":
    # En caso de que si sea, sustituye la vocal y lo imprime por pantalla
    frase_modificada = frase.replace(vocal, vocal.upper())
    print("Frase modificada:", frase_modificada)
else:
    # Si no muestra un mensaje de error
    print("No has introducido una vocal válida.")
