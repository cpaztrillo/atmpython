from Operacion import *
class Transferencia(Operacion):
    def __init__(self, dict):
        self.destino=dict["destino"]
        super().__init__(dict)