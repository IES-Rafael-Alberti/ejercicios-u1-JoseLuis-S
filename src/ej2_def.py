# Funcion para calcular el pago total por las horas trabajadas
def pagoTotal (horas, precioHora):
    return horas * precioHora

# Define el main, lee las horas, el precio por hora y luego muestra la funcion por pantalla
def main():
    horas = int(input('Introduce las horas trabajadas: '))
    precioHora = int(input('Introduce el precio por hora: '))
    print('El total es', pagoTotal(horas, precioHora),'euros.')

# Llama la funcion main
if __name__ == '__main__':
    main()