import datetime
from Operacion import *

class Cuenta:
    def __init__(self, dict):
        self.numero = dict["numero"]
        self.moneda = dict["moneda"]
        self.saldo = dict["saldo"]
        self.operaciones = dict["operaciones"]

    def retiro(self, moneda, monto):
        conversion = 1.0
        if(moneda=="D" and self.moneda=="S"):
            conversion = 4.0
        if(moneda=="S" and self.moneda=="D"):
            conversion = 0.25
        montoenmoneda = monto * conversion
        if self.saldo < montoenmoneda:
            return False
        self.saldo = self.saldo - montoenmoneda
        operacion = Operacion({
            "fecha"  : datetime.datetime.now().strftime("%c"),
            "moneda" : moneda,
            "monto"  : monto
        })
        self.operaciones.append(operacion)
        return True