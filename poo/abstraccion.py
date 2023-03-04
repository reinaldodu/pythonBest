class Lavadora:
    def __init__(self):
        pass

    def lavar(self, temperatura='fria'):
        self._llenar_tanque(temperatura)
        self._anadir_jabon()
        self._lavar() # Es diferente al método lavar (lavar -> público, _lavar -> método protegido)
        self._centrifugar()

    def _llenar_tanque(self,temperatura):  #Método privado (inicia con _)
        print(f'Llenando el tanque con agua {temperatura}')

    def _anadir_jabon(self):
        print('Añadiendo jabón')

    def _lavar(self):
        print('Lavando la ropa')

    def _centrifugar(self):
        print('Centrifugando')

if __name__ == '__main__':
    lavadora=Lavadora()
    lavadora.lavar()
