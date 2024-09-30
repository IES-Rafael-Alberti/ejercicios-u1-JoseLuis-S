# Lee la frase
frase = input("Introduce una frase: ")

# Lee la vocal
vocal = input("Introduce una vocal: ").lower()

# Verifica que lo introducido sea una vocal
if vocal in "aeiou":
    # En caso de que si 
    frase_modificada = frase.replace(vocal, vocal.upper())
    print("Frase modificada:", frase_modificada)
else:
    print("No has introducido una vocal válida.")
