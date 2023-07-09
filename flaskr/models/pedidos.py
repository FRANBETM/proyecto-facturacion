from flaskr.models import db, proveedores

class Pedidos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable=False)    
    id_proveedor = db.Column(db.Integer, db.ForeignKey('proveedores.id'), nullable=False)