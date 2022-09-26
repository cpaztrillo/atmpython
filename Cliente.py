from Cuenta import *

class Cliente:
    def __init__(self, dict):
        self.nombres = dict["nombres"]
        self.apellidos = dict["apellidos"]
        self.dni = dict["dni"]
        self.cuentas = {}
        print(dict["cuentas"])
        for key in dict["cuentas"]:
            print(dict["cuentas"][key])
            self.cuentas[key] = Cuenta(dict["cuentas"][key]) 

    def adicionaCuenta(self, cuenta):
        self.cuentas[cuenta.numero] = cuenta