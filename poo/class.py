class Persona:
    # Constructor de la clase
    def __init__ (self, nombre, edad):
        self.nombre=nombre
        self.edad=edad

    # Método de la clase
    def saluda(self, otra_persona):
        return f'Hola {otra_persona.nombre} mi nombre es {self.nombre}'

# Crear una instancia
david=Persona('David',25)
camila=Persona('Camila',20)

print(david.saluda(camila))
