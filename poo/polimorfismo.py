class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print('Voy caminando')


class Ciclista(Persona):   # La subclase Ciclista extiende (hereda) de la super clase Persona

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):  # Polimorfismo  --> Reescribir el método avanza para la subclase Ciclista
        print('Voy sobre mi bicicleta')


def main():
    persona = Persona('David')
    persona.avanza()

    ciclista = Ciclista('Daniel')
    ciclista.avanza()


if __name__ == '__main__':
    main()
