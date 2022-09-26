from Cliente import *

class Tarjeta:
   def __init__(self, dict):
      self.numero = dict["numero"]
      self.pin = dict["pin"]
      print(type(dict["cliente"]))
      self.cliente = Cliente(dict["cliente"])

   def validaPin(self, pin):
      if(pin!=self.pin):
         return False
      return True