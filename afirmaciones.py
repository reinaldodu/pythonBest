# assert <expresión booleana>, <mensaje de error si no se cumple la condición>

def primera_letra(lista):
    primeras_letras=[]
    #Programación defensiva a través de assert
    for palabra in lista:
        try:
            assert type(palabra) == str, f'{palabra} no es un string'
            assert len(palabra) > 0, 'No se permiten vacios'
            primeras_letras.append(palabra[0])
        except AssertionError as e:
            print(e)

    return primeras_letras

lista=['casa','','carro','gato',2,True,'perro']
print(primera_letra(lista))

