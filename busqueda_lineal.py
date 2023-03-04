import random

def busqueda_lineal(lista,objetivo):
    match = False
    for item in lista:
        if item==objetivo:
            match = True
            break
    return match

if __name__ == '__main__':
    tam = int(input('Tamaño de la lista? '))
    buscar=int(input('número a buscar? '))
    lista=[random.randint(1,100) for num in range(tam)]
    encontrado = busqueda_lineal(lista,buscar)
    print (lista)
    print (f'el número {buscar} { "está" if encontrado else "no está"} en la lista')
