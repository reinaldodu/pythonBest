from time import time

objetivo = int(input('Escribe un numero: '))
epsilon = 0.0001
bajo = 0.0
alto = max(1.0, objetivo)
respuesta = (alto + bajo) / 2
tiempo_inicio= time()

while abs(respuesta**2 - objetivo) >= epsilon:
    print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta

    respuesta = (alto + bajo) / 2

tiempo_total=time()-tiempo_inicio
print(f'La raiz cuadrada de {objetivo} es {respuesta}')
print(f'El tiempo de ejecución es {tiempo_total}')
