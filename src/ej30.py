# Lee el numero de inicio
inicio = int(input('Introduce un numero de inicio: '))

# Declara la variable incremento para asegurar que sea mayor que 0
incremento = -1

# Asegura que el incremento sea mayor que 0, en caso de que no muestra error y pide incremento de nuevo
while incremento < 0: 
    print('(El incremento debe ser mayor que 0)')
    incremento = int(input('Introduce el numero de incremento: '))

# Declara la variable total para asegurar que sea mayor que 0
total = -1

# Asegura que el total sea mayor que 0, en caso de que no muestra error y pide total de nuevo
while total < 0:
    print('(El total deben ser mayor que 0)')
    total = int(input('Introduce el total: '))

# Declara la variable serie como una variable vacia
serie = ""

# Utiliza un bucle para escribir la secuencia 
for i in range(total):
    # Guarda el valor de la serie en una variable temporal para que el total de la serie no se pierda
    valor = inicio + (i * incremento)  

    # Si es el primer numero de la serie utiliza un - para separar
    if i == 0:
        serie += str(valor) + '-'
    # Si es el ultimo numero de la serie utiliza un - para separar
    elif i == total - 1:
        serie += '-' + str(valor)
    # Si es el segundo numero no utiliza ningun elemento para separar la serie
    elif i == 1:
        serie += str(valor)
    # Si es un numero intermedio en la serie utiliza .. para separar los numeros
    else:
        serie += '..' + str(valor)

# Imprime el resultado
print(f'SERIE => {serie}')

