inicio = int(input('Introduce un numero de inicio: '))

incremento = -1

while incremento < 0: 
    print('(El incremento debe ser mayor que 0)')
    incremento = int(input('Introduce el numero de incremento: '))

total = -1

while total < 0:
    print('(El total deben ser mayor que 0)')
    total = int(input('Introduce el total: '))

serie = ""

for i in range(total):
    valor = inicio + (i * incremento)  

    if i == 0:
        serie += str(valor) + '-'
    elif i == total - 1:
        serie += '-' + str(valor)
    elif i == 1:
        serie += str(valor)
    else:
        serie += '..' + str(valor)

print(f'SERIE => {serie}')

