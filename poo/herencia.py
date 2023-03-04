class Rectangulo:
    def __init__(self,alto,ancho):
        self.alto=alto
        self.ancho=ancho

    def area(self):
        return self.alto * self.ancho

class Cuadrado(Rectangulo): # Clase Cuadrado extiende (hereda) de la clase Rectangulo
    def __init__(self, lado):
        super().__init__(lado, lado)   # inicializamos la clase super (clase superior -> Rectangulo)

if __name__ == '__main__':
    rectangulo = Rectangulo(5,2)
    print ('El área del rectángulo es...', rectangulo.area())

    cuadrado = Cuadrado(5)
    print ('El área del cuadrado es...', cuadrado.area())  # La subclase Cuadrado hereda el método área de la clase padre Rectangulo


