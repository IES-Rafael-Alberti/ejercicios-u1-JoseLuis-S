pesoPayaso = 112
pesoMuñeca = 75
numPayasos = int(input('Inserta la cantidad de payasos vendidos: '))
numMuñecas = int(input('Inserta la cantidad de muñecas vendidas: '))
pesoTotal = (numPayasos*pesoPayaso + numMuñecas*pesoMuñeca)/1000

print('El peso total del envio sera de: ' + str(pesoTotal) + 'kg.')