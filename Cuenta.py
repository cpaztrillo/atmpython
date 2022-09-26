class Cuenta:
    def __init__(self, dict):
        self.numero = dict["numero"]
        self.moneda = dict["moneda"]
        self.saldo = dict["saldo"]
        self.operaciones = []

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
        return True