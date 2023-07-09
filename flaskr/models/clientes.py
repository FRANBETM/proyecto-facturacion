from flaskr.models import db
from flaskr.models import *

class Clientes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), unique=True, nullable=False)
    tipo_documento = db.Column(db.String(2), nullable=False)
    numero_documento = db.Column(db.String(20), unique=True, nullable=False)
    direccion = db.Column(db.String(500), nullable=False)
    telefono = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(200), nullable=True)
    
