#
def compNum(n1,n2):
    if n1 == n2:
        return '{}'.format(0)
    if n1 > n2:
        return '{}'.format(n1)
    if n2 > n1:
        return '{}'.format(n2)

def main():
    n1 = input('Introduce el primer numero: ')
    n2 = input('Introduce el segundo numero: ')
    print(compNum(n1,n2), 'es mayor.')

if __name__ == '__main__':
    main()
