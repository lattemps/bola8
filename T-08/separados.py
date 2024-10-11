def separados(secuencia):
    '''Separa la secuencia de números en listas de positivos, negativos y ceros.
    (str) -> (list, list, list)
    '''

    numeros = list(map(int, secuencia.split(",")))
    positivos = []
    negativos = []
    ceros = []
    
    for n in numeros:
        if n > 0:
            positivos.append(n)
        elif n < 0:
            negativos.append(n)
        else:
            ceros.append(n)
    
    return positivos, negativos, ceros

def main():

    secuencia = input("Introduzca una secuencia de números enteros separados por comas: ")
    
    positivos, negativos, ceros = separados(secuencia)
    
    print("Positivos:", positivos)
    print("Negativos:", negativos)
    print("Ceros:", ceros)

main()
