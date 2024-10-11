def invertir(lista):
    ''' Modifica la lista invirtiendole el orden
    (lits) ->list
    '''
    inicio = 0
    fin = len(lista) - 1
    while inicio < fin:
        lista[inicio], lista[fin] = lista[fin], lista[inicio]
        inicio += 1
        fin -= 1
        
    return lista

def main():
    lista = list(map(int, input("Coloque una serie de números separados por comas:").split(',')))
    resultado = invertir(lista)
    print(resultado)
    

main()
    
