def pares(a, b):
    ''' Genera una lista de números pares en el intervalo [a, b].
    (int, int) -> list
    '''
    lista_pares = []
    
    if a > b:
        return lista_pares
    
    if a % 2 != 0:
        a +=1
        
    while a <= b:
        lista_pares.append(a)
        a +=2

    return lista_pares
    

def main():
    num = input("Introduzca el intervalo separado por comas:")
    a, b = map(int, num.split(","))
    par = pares(a, b)
    print(par)

main()
    
