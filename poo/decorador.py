def funcion_decoradora(funcion):
	def wrapper():
		print("Este es el último mensaje...")
		funcion()
		print("Este es el primer mensaje ;)")
	return wrapper

@funcion_decoradora  #Es lo mismo que escribir zumbido=funcion_decoradora(zumbido)
def zumbido():
	print("Buzzzzzz")

#zumbido=funcion_decoradora(zumbido)
zumbido()
