import json
from json import JSONEncoder
from Tarjeta import *
from Cliente import *
from Cuenta import *

class MyEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, Banco) or isinstance(object, Tarjeta) or isinstance(object, Cliente) or isinstance(object, Cuenta) :
            print(type(object))
            return object.__dict__
        else:
            return json.JSONEncoder.default(self, object)

class Banco:
    def __init__(self, dict):
        self.tarjetas = {}
        for key in dict["tarjetas"]:
            self.tarjetas[key] = Tarjeta(dict["tarjetas"][key])