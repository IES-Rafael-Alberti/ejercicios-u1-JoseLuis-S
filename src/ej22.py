frase = input("Introduce una frase: ")

vocal = input("Introduce una vocal: ").lower()

if vocal in "aeiou":
    frase_modificada = frase.replace(vocal, vocal.upper())
    print("Frase modificada:", frase_modificada)
else:
    print("No has introducido una vocal válida.")
