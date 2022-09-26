from flask import Flask
from Banco import * 
from Tarjeta import *
from Cliente import *
from Cuenta import *
from flask import request
import json
        
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

def load():
    f = open('/Users/cpaztrillo/banco.json')
    b = Banco(json.load(f)) 
    f.close()
    return b

def save(b):
    db = open('/Users/cpaztrillo/banco.json', 'w') 
    db.write(MyEncoder().encode(b))
    db.close()

@app.route('/vercuentas')
def vercuentas():
    num = request.args.get("tarjeta")
    pin = request.args.get("pin")
    b = load()
    t = b.tarjetas[num]
    if(not t.validaPin(pin)):
        return "Pin incorrecto", 400
    return MyEncoder().encode(t.cliente.cuentas)
#http://127.0.0.1:5000/vercuentas?tarjeta=98765432&pin=1234

@app.route('/retirosoles')
def retirosoles():
    num = request.args.get("tarjeta")
    pin = request.args.get("pin")
    cta = request.args.get("cta")
    monto = float(request.args.get("monto"))
    b = load()
    t = b.tarjetas[num]
    if(not t.validaPin(pin)):
        return "Pin incorrecto", 400
    resultado = t.cliente.cuentas[cta].retiro("S", monto)
    if(resultado == False):
        return "Saldo Insuficiente", 400
    save(b)
    return "Retiro realizado, nuevo saldo: " + str(t.cliente.cuentas[cta].saldo), 200
#http://127.0.0.1:5000/retirosoles?tarjeta=98765432&pin=1234&cta=12678&monto=20
#http://127.0.0.1:5000/retirosoles?tarjeta=98765432&pin=1234&cta=45672&monto=20