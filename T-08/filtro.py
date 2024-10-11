def filtro(secuencia, numero):
    '''Filtra los números de la secuencia que son mayores que el número dado.
    (list, int) -> list
    '''
    numeros = list(map(float, secuencia.split()))
    resultado = []
    
    for n in numeros:
        if n > numero:
            resultado.append(n)
    
    return resultado

def main():

    numeros = input("Introduzca una secuencia de números reales separados por espacios: ")
    n = int(input("Introduzca un número entero: "))
    resultado = filtro(numeros, n)
    print(resultado)

main()
