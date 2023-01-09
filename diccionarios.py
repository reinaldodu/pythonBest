my_dict={
    'marca':'Toyota',
    'modelo':2010,
    'cilindraje':1400
}
print(my_dict['marca'])
print(my_dict.get('marca'))

#Iterar por claves
for clave in my_dict.keys():
    print(clave)

#Iterar por valores
for valor in my_dict.values():
    print(valor)

#Iterar por claves y valores
for clave,valor in my_dict.items():
        print(clave,valor)
