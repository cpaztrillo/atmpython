from Cuenta import *

class Operacion:
    def __init__(self, dict):
        self.fecha = dict["fecha"]
        self.moneda = dict["moneda"]
        self.monto = dict["monto"]
    
