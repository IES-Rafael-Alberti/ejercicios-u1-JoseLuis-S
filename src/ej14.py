'''
Ej 14

Este algoritmo calcula el peso total de un paquete segun la cantidad de payasos
y muñecas que contenga

'''

# Guarda los valores del peso de los dos productos
pesoPayaso = 112
pesoMuñeca = 75

# Lee la cantidad de productos
numPayasos = int(input('Inserta la cantidad de payasos vendidos: '))
numMuñecas = int(input('Inserta la cantidad de muñecas vendidas: '))

# Calcula el peso total en KG del envio
pesoTotal = (numPayasos*pesoPayaso + numMuñecas*pesoMuñeca)/1000

# Imprime el resultado por pantalla
print(f'El peso total del envio sera de: {pesoTotal} kg.')