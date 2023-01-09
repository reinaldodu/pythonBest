class Automovil:
    def __init__(self,modelo,marca,motor):
        self.modelo=modelo
        self.marca=marca
        self.motor=motor
        self._estado='reposo'  #Propiedad privada (inicia con _)
        self._motor=Motor(cilindros=4) #Otra propiedad privada

    def acelera(self, tipo='despacio'):
        if tipo=='rapido':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)

class Motor:
    def __init__(self, cilindros,tipo='gasolina'):
        self.cilindros=cilindros
        self.tipo=tipo
        self._temperatura=0

    def inyecta_gasolina(self,cantidad):
        pass  # cuerpo de función en blanco
